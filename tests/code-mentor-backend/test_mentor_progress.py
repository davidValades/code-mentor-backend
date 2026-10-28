"""Behavioral checks against synthetic records; never learner progress."""
import copy
import json
import os
import shutil
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SKILL = Path(os.environ['MENTOR_SKILL'])
sys.path.insert(0, str(SKILL / 'scripts'))
import mentor_store as store
try:
    import mentor_progress as progress
except ImportError:
    progress = None


def event(ident='e1', **changes):
    value = dict(id=ident, session_id='s1', recorded_at='2026-10-27T10:00:00+01:00',
                 topic='methods', activity='explain', modality='oral', assistance='none',
                 outcome='correct', evidence_summary='Synthetic learner attempt', review_due=None)
    value.update(changes)
    return value


class ProgressModelTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(progress, 'Interactive progress utility is missing')

    def model(self, events=(), **options):
        state = store.new_state('general')
        state['events'] = list(events)
        return progress.build_model(state, generated_at='2026-10-28T12:00:00+00:00', **options)

    def test_only_own_attempts_count_even_when_wrong_or_unchecked(self):
        data = self.model([
            event('own-wrong', outcome='incorrect', assistance='hint'),
            event('own-unchecked', activity='implement', outcome='unverified', assistance='guided'),
            event('declaration', activity='declared', outcome='unverified'),
            event('copied', activity='implement', modality='ide', assistance='solution')])
        self.assertEqual([e['id'] for e in data['events'] if e['practice']], ['own-unchecked', 'own-wrong'])
        self.assertEqual(data['concepts'][0]['milestones'], [])

    def test_uses_selected_zone_for_midnight_and_both_dst_offsets(self):
        data = self.model([
            event('midnight', recorded_at='2026-10-27T23:30:00Z'),
            event('dst-before', recorded_at='2026-10-25T00:30:00Z'),
            event('dst-after', recorded_at='2026-10-25T01:30:00Z')], time_zone='Europe/Madrid')
        self.assertEqual({e['id']:e['day'] for e in data['events']},
                         {'midnight':'2026-10-28', 'dst-before':'2026-10-25', 'dst-after':'2026-10-25'})
        self.assertEqual(data['time_zone'], 'Europe/Madrid')

    def test_old_support_remains_available_for_later_retrieval(self):
        data = self.model([
            event('practice', activity='debug', modality='ide', recorded_at='2024-02-29T10:00:00Z'),
            event('later', activity='retrieve', session_id='s2', recorded_at='2026-10-27T10:00:00Z')])
        concept = data['concepts'][0]
        self.assertEqual(concept['status'], 'consolidated')
        witness = next(m for m in concept['milestones'] if m['kind']=='consolidated')
        self.assertEqual(witness['event_ids'], ['practice','later'])
        self.assertEqual(witness['day'], '2026-10-27')
        self.assertEqual(data['range'], {'start':'2025-10-29','end':'2026-10-28'})

    def test_oral_conceptual_success_is_not_an_ide_achievement(self):
        data=self.model([event()])
        self.assertEqual(data['concepts'][0]['status'], 'conceptual')
        self.assertEqual([m['kind'] for m in data['concepts'][0]['milestones']], ['conceptual'])

    def test_latest_checks_separate_context_and_preserve_historical_achievement(self):
        data=self.model([
            event('success', activity='debug', modality='ide', recorded_at='2026-10-26T10:00:00Z'),
            event('failure', activity='debug', modality='ide', outcome='incorrect'),
            event('oral', outcome='partial', assistance='guided'),
            event('unverified', activity='debug', modality='ide', outcome='unverified',
                  recorded_at='2026-10-28T10:00:00Z')])
        concept=data['concepts'][0]
        self.assertEqual(concept['status'], 'autonomous')
        self.assertEqual({e['id'] for e in concept['latest_checks']}, {'failure','oral'})
        self.assertEqual(concept['milestones'][-1]['event_ids'], ['success'])

    def test_recall_needs_other_session_and_full_day(self):
        for sid, when in [('s1','2026-10-29T10:00:00Z'), ('s2','2026-10-27T23:00:00Z')]:
            with self.subTest(sid=sid,when=when):
                data=self.model([event('practice', activity='implement', modality='ide',
                                       recorded_at='2026-10-27T10:00:00Z'),
                                 event('later', activity='retrieve', session_id=sid, recorded_at=when)])
                self.assertEqual(data['concepts'][0]['status'], 'autonomous')

    def test_project_projection_omits_file_references_and_task_ids(self):
        state=store.new_state('project')
        state['events']=[event(task_id='private-task',source_refs=[dict(path='Secret/Code.cs',commit=None,
                            branch='private-branch',dirty=True,observed_at='2026-10-27T10:00:00Z')])]
        data=progress.build_model(state)
        encoded=json.dumps(data)
        for value in ['Secret/Code.cs','private-task','private-branch','source_refs','task_id']:
            self.assertNotIn(value,encoded)
        self.assertEqual(data['scope'],'project')

    def test_invalid_configuration_or_duplicate_evidence_is_rejected(self):
        for options in [dict(language='fr'),dict(time_zone='../zone'),dict(generated_at='2026-10-28T12:00:00')]:
            with self.subTest(options=options), self.assertRaises(ValueError):
                progress.build_model(store.new_state('general'),**options)
        with self.assertRaisesRegex(ValueError,'duplicate'):
            self.model([event(),event()])

    def test_late_report_generation_does_not_move_old_activity_dates(self):
        data=self.model([event(recorded_at='2025-05-01T15:00:00Z')])
        self.assertEqual(data['events'][0]['day'],'2025-05-01')
        self.assertEqual(data['generated_at'],'2026-10-28T12:00:00+00:00')
        self.assertNotIn('saved_at',data['events'][0])

    def test_compact_iso_dates_project_browser_instants_without_changing_sources(self):
        state=store.new_state('general')
        state['events']=[event(recorded_at='20261028T100000+0000')]
        state['sessions']=[dict(id='s1',recorded_at='20261028T120000+0000')]
        data=progress.build_model(state,generated_at='20261028T130000+0000')
        self.assertEqual(data['events'][0]['recorded_at'],'20261028T100000+0000')
        self.assertEqual(data['events'][0]['display_at'],'2026-10-28T10:00:00.000+00:00')
        self.assertEqual(data['events'][0]['session_completed_display_at'],'2026-10-28T12:00:00.000+00:00')
        self.assertEqual(data['display_generated_at'],'2026-10-28T13:00:00.000+00:00')
        self.assertEqual(state['events'][0]['recorded_at'],'20261028T100000+0000')

    def test_language_changes_labels_without_changing_ids_counts_or_state(self):
        state=store.new_state('general');state['events']=[event(topic='csharp.metodos')]
        before=copy.deepcopy(state)
        en=progress.build_model(state,language='en');es=progress.build_model(state,language='es')
        self.assertEqual(en['events'],es['events'])
        self.assertEqual(en['concepts'],es['concepts'])
        self.assertEqual(en['source_digest'],es['source_digest'])
        self.assertEqual(state,before)
        self.assertEqual(es['labels']['title'],'Progreso de aprendizaje')


class ReportMarkup(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.scripts=[]; self.tags=[]; self.active=None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs); self.tags.append((tag,attrs))
        if tag=='script':
            self.active={'attrs':attrs,'text':''}; self.scripts.append(self.active)

    def handle_data(self, data):
        if self.active is not None: self.active['text']+=data

    def handle_endtag(self, tag):
        if tag=='script': self.active=None


class ProgressReportTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(progress)
        self.assertTrue(hasattr(progress,'report'), 'Interactive report renderer is missing')
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'learning'; store.init_store(self.root,'general')

    def add(self, **changes):
        state=store.read_state(self.root)
        return store.apply_command(self.root,dict(request_id='qa-'+str(state['revision']),
            expected_revision=state['revision'],operation='record_evidence',payload=event(**changes)))

    def test_report_writes_both_private_derivatives_without_changing_evidence(self):
        self.add()
        before=(self.root/'state.json').read_bytes()
        result=progress.report(self.root,time_zone='Europe/Madrid',language='es',demo=True)
        self.assertEqual(Path(result['html']).relative_to(self.root),Path('progress/index.html'))
        self.assertEqual(Path(result['markdown']).relative_to(self.root),Path('progress/summary.md'))
        self.assertEqual(result['source_revision'],1)
        self.assertEqual(len(result['source_digest']),64)
        self.assertIn('Progreso de aprendizaje',Path(result['html']).read_text())
        self.assertIn('sintéticos',Path(result['markdown']).read_text())
        self.assertIn('e1',Path(result['markdown']).read_text())
        self.assertEqual((self.root/'state.json').read_bytes(),before)

    def test_embedded_hostile_data_round_trips_as_data_not_markup(self):
        attack='</script><img src=x onerror="alert(1)">|\n<script>bad()</script>'
        state=store.new_state('general');state['events']=[event(topic=attack,evidence_summary=attack)]
        model=progress.build_model(state,demo=True)
        html,md=progress.render(model)
        parsed=ReportMarkup(html)
        data=next(s for s in parsed.scripts if s['attrs'].get('id')=='progress-data')
        self.assertEqual(json.loads(data['text'])['events'][0]['evidence_summary'],attack)
        self.assertFalse(any(tag=='img' for tag,attrs in parsed.tags))
        self.assertFalse(any(attrs.get('src') or attrs.get('href','').startswith('http') for tag,attrs in parsed.tags))
        self.assertIn('\\|',md)
        self.assertIn('Content-Security-Policy',html)

    def test_empty_report_discloses_missing_evidence(self):
        result=progress.report(self.root)
        md=Path(result['markdown']).read_text()
        self.assertIn('No qualifying practice',md)
        self.assertIn('snapshot',md.lower())
        self.assertEqual(store.read_state(self.root)['revision'],0)

    def test_bad_options_create_no_outputs(self):
        for kwargs in [dict(time_zone='missing/zone'),dict(language='fr')]:
            with self.subTest(kwargs=kwargs),self.assertRaises(ValueError):
                progress.report(self.root,**kwargs)
        self.assertFalse((self.root/'progress').exists())
        self.assertFalse((self.root/'.write.lock').exists())

    def test_symlink_and_existing_lock_leave_other_files_untouched(self):
        other=Path(self.temp.name)/'external';other.mkdir()
        (self.root/'progress').symlink_to(other,target_is_directory=True)
        with self.assertRaises(ValueError): progress.report(self.root)
        self.assertEqual(list(other.iterdir()),[])
        (self.root/'progress').unlink()
        (self.root/'.write.lock').write_text('other writer')
        with self.assertRaisesRegex(ValueError,'LOCKED'): progress.report(self.root)
        self.assertFalse((self.root/'progress').exists())

    def test_failure_of_second_write_restores_previous_report(self):
        old=progress.report(self.root)
        paths=[Path(old[k]) for k in ['html','markdown']]
        before=[p.read_bytes() for p in paths]
        self.add()
        real=store.atomic_write;failed=False
        def fail_once(path,content):
            nonlocal failed
            if path.name=='summary.md' and not failed:
                failed=True;raise OSError('disk full')
            return real(path,content)
        with patch.object(store,'atomic_write',side_effect=fail_once):
            with self.assertRaisesRegex(OSError,'disk full'):
                progress.report(self.root)
        self.assertEqual([p.read_bytes() for p in paths],before)
        self.assertEqual(store.read_state(self.root)['revision'],1)
        self.assertFalse((self.root/'.write.lock').exists())

    def test_source_changed_by_noncooperating_writer_is_not_reported_as_current(self):
        old=progress.report(self.root);old_html=Path(old['html']).read_bytes()
        real=store.atomic_write;changed=False
        def concurrent_change(path,content):
            nonlocal changed
            real(path,content)
            if path.name=='index.html' and not changed:
                changed=True;state=store.read_state(self.root);state['revision']=1
                real(self.root/'state.json',store.canonical(state))
        with patch.object(store,'atomic_write',side_effect=concurrent_change):
            with self.assertRaisesRegex(ValueError,'STALE'):
                progress.report(self.root)
        self.assertEqual(Path(old['html']).read_bytes(),old_html)
        self.assertEqual(store.read_state(self.root)['revision'],1)

    def test_cli_generates_real_report_and_rejects_invalid_arguments(self):
        command=[sys.executable,str(SKILL/'scripts/mentor_progress.py'),'--root',str(self.root),'report']
        result=subprocess.run(command+['--language','es','--timezone','Europe/Madrid','--demo'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        response=json.loads(result.stdout)
        self.assertTrue(Path(response['html']).is_file())
        self.assertIn('Progreso de aprendizaje',Path(response['markdown']).read_text())
        before=Path(response['html']).read_bytes()
        bad=subprocess.run(command+['--language','fr'],capture_output=True,text=True)
        self.assertNotEqual(bad.returncode,0)
        self.assertEqual(Path(response['html']).read_bytes(),before)

    @unittest.skipUnless(shutil.which('node'), 'Node is only required for offline DOM interaction checks')
    def test_shipped_script_handles_clicks_filters_keyboard_and_empty_or_hostile_data(self):
        rows=[
            event('explain',topic='csharp.methods',recorded_at='2026-10-12T10:00:00Z',assistance='guided',outcome='partial'),
            event('debug',topic='csharp.methods',recorded_at='2026-10-15T10:00:00Z',activity='debug',modality='ide'),
            event('recall',topic='csharp.methods',recorded_at='2026-10-28T08:00:00Z',activity='retrieve',session_id='s3'),
            event('predict',topic='csharp.operators',recorded_at='2026-10-28T08:05:00Z',activity='predict',outcome='incorrect',assistance='hint'),
            event('unchecked',topic='csharp.results',recorded_at='2026-10-28T08:10:00Z',activity='implement',outcome='unverified',assistance='guided'),
            event('declared',topic='csharp.results',recorded_at='2026-10-28T08:15:00Z',activity='declared',outcome='unverified'),
            event('solution',topic='csharp.results',recorded_at='2026-10-28T08:20:00Z',activity='implement',assistance='solution')]
        hostile='</script><img src=x onerror=alert(1)>'
        paths=[]
        for name,events in [('practice',rows),('empty',[]),('hostile',[event(topic=hostile,evidence_summary=hostile)]),
                            ('compact',[event(recorded_at='20261028T100000+0000')])]:
            state=store.new_state('general');state['events']=events
            if name=='compact': state['sessions']=[dict(id='s1',recorded_at='20261028T120000+0000')]
            model=progress.build_model(state,time_zone='Europe/Madrid',language='es',demo=True,
                                       generated_at='20261028T130000+0000' if name=='compact' else '2026-10-28T12:00:00Z')
            html,md=progress.render(model)
            path=Path(self.temp.name)/(name+'.html');path.write_text(html);paths.append(str(path))
        result=subprocess.run([shutil.which('node'),str(Path(__file__).with_name('test_progress_ui.js')),*paths],
                              text=True,capture_output=True,timeout=10)
        self.assertEqual(result.returncode,0,result.stderr+result.stdout)


if __name__ == '__main__':
    unittest.main()
