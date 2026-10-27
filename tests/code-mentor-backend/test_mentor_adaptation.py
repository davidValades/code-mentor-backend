import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

SKILL = Path(os.environ['MENTOR_SKILL'])
sys.path.insert(0, str(SKILL / 'scripts'))
import mentor_store as store
try:
    import mentor_adaptation as adap
except ImportError:
    adap = None


class AdaptationTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(adap, 'Falta la utilidad de observaciones y gráficos')
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'learning'
        store.init_store(self.root, 'general')

    def evidence(self, id='e1', **changes):
        value = dict(id=id, session_id='s1', recorded_at='2026-10-27T10:00:00+01:00',
                     topic='operators', activity='predict', modality='text', assistance='hint',
                     outcome='correct', evidence_summary='Ejemplo sintético', review_due=None)
        value.update(changes)
        state = store.read_state(self.root)
        store.apply_command(self.root, dict(request_id='req-'+id, expected_revision=state['revision'],
                            operation='record_evidence', payload=value))

    def observation(self, **changes):
        value = dict(id='o1', evidence_id='e1', concept_id='csharp.operadores.igualdad',
                     task_kind='trace', difficulty='standard', check_kind='immediate', strategies=['diagram'],
                     learned_evidence_id=None)
        value.update(changes)
        return value

    def test_requires_existing_evidence(self):
        with self.assertRaisesRegex(ValueError, 'evidence'):
            adap.record(self.root, self.observation())
        self.assertFalse((self.root/'adaptacion/observaciones.jsonl').exists())

    def test_retry_does_not_duplicate_or_change_primary_store(self):
        self.evidence()
        before = (self.root/'state.json').read_bytes()
        adap.record(self.root, self.observation())
        result = adap.record(self.root, self.observation())
        self.assertTrue(result['replayed'])
        self.assertEqual(len((self.root/'adaptacion/observaciones.jsonl').read_text().splitlines()), 1)
        self.assertEqual((self.root/'state.json').read_bytes(), before)
        with self.assertRaisesRegex(ValueError, 'reused'):
            adap.record(self.root, self.observation(strategies=['analogy']))
        with self.assertRaisesRegex(ValueError, 'already'):
            adap.record(self.root, self.observation(id='o2'))

    def test_grouping_separates_mode_help_and_combinations(self):
        for n,changes in enumerate([{}, {'modality':'oral'}, {'assistance':'none'}, {}], 1):
            self.evidence('e'+str(n), **changes)
            adap.record(self.root, self.observation(id='o'+str(n), evidence_id='e'+str(n),
                        strategies=['diagram','analogy'] if n==4 else ['diagram']))
        result = adap.summarize(self.root)
        self.assertEqual(len(result['groups']), 4)
        self.assertTrue(all(g['attempts']==1 for g in result['groups']))
        self.assertTrue(all(g['insufficient'] for g in result['groups']))

    def test_unverified_declared_and_solution_are_not_successes(self):
        for n,changes in enumerate([{'activity':'declared','outcome':'unverified'},
                                  {'assistance':'solution'}, {'outcome':'incorrect'},
                                  {'outcome':'partial'}], 1):
            self.evidence('e'+str(n), **changes)
            adap.record(self.root, self.observation(id='o'+str(n), evidence_id='e'+str(n)))
        result = adap.summarize(self.root)
        self.assertEqual(sum(g['correct'] for g in result['groups']), 0)
        self.assertEqual(sum(g['pending'] for g in result['groups']), 2)
        self.assertEqual(sum(g['attempts'] for g in result['groups']), 2)

    def test_delayed_requires_prior_different_session_and_day(self):
        self.evidence('learn')
        self.evidence('check')
        obs = self.observation(evidence_id='check', learned_evidence_id='learn', check_kind='delayed')
        with self.assertRaises(ValueError): adap.record(self.root, obs)
        self.evidence('later', session_id='s2', recorded_at='2026-10-29T10:00:00+01:00', activity='retrieve')
        adap.record(self.root, self.observation(evidence_id='later', learned_evidence_id='learn', check_kind='delayed'))
        group = adap.summarize(self.root)['groups'][0]
        self.assertEqual(group['delays_days'], [2.0])

    def test_deleted_evidence_is_excluded_and_reported(self):
        self.evidence()
        adap.record(self.root, self.observation())
        state=store.read_state(self.root); state['events']=[]
        store.atomic_write(self.root/'state.json', store.canonical(state))
        result=adap.summarize(self.root)
        self.assertEqual(result['groups'], [])
        self.assertEqual(result['orphaned_ids'], ['o1'])

    def test_invalid_identifiers_and_fields_are_rejected(self):
        self.evidence()
        for changes in [{'concept_id':'../secret'}, {'strategies':['visual-learner']},
                        {'strategies':['diagram','diagram']}, {'raw_code':'confidential'},
                        {'check_kind':'mastered'}]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                adap.record(self.root,self.observation(**changes))

    def test_symlink_target_and_existing_lock_are_not_overwritten(self):
        self.evidence()
        external = Path(self.temp.name)/'elsewhere';external.mkdir()
        (self.root/'adaptacion').symlink_to(external, target_is_directory=True)
        with self.assertRaises(ValueError): adap.record(self.root,self.observation())
        self.assertEqual(list(external.iterdir()), [])
        (self.root/'adaptacion').unlink()
        (self.root/'.write.lock').write_text('another writer')
        with self.assertRaisesRegex(ValueError,'LOCKED'): adap.record(self.root,self.observation())

    def test_reports_empty_and_sparse_data_without_percentages(self):
        report = adap.report(self.root, language='es')
        svg = Path(report['svg']).read_text()
        self.assertIn('Sin observaciones',svg)
        self.evidence();adap.record(self.root,self.observation())
        report=adap.report(self.root, language='es')
        svg=Path(report['svg']).read_text();md=Path(report['markdown']).read_text()
        self.assertIn('1/1',svg)
        self.assertIn('Evidencia insuficiente',md)
        self.assertNotIn('%', ''.join(ET.fromstring(svg).itertext()))
        self.assertIn('o1',md)
        self.assertNotIn('Ejemplo sintético',svg)

    def test_different_learning_modes_do_not_merge_delayed_checks(self):
        self.evidence('learn1', modality='oral')
        self.evidence('learn2', modality='text')
        for n in [1, 2]:
            self.evidence('check'+str(n), session_id='later', recorded_at='2026-10-29T10:00:00+01:00', modality='ide')
            adap.record(self.root, self.observation(id='o'+str(n), evidence_id='check'+str(n),
                        check_kind='delayed', learned_evidence_id='learn'+str(n)))
        self.assertEqual(len(adap.summarize(self.root)['groups']), 2)

    def test_freshness_includes_observations_not_only_primary_revision(self):
        self.evidence()
        before = adap.summarize(self.root)
        adap.record(self.root, self.observation())
        after = adap.summarize(self.root)
        self.assertEqual(before['source_revision'], after['source_revision'])
        self.assertNotEqual(before.get('observation_digest'), after.get('observation_digest'))

    def test_pending_session_does_not_satisfy_evaluated_session_threshold(self):
        for n in range(4):
            self.evidence('e'+str(n), session_id='s2' if n==3 else 's1',
                          outcome='unverified' if n==3 else 'correct')
            adap.record(self.root, self.observation(id='o'+str(n), evidence_id='e'+str(n)))
        group=adap.summarize(self.root)['groups'][0]
        self.assertTrue(group['insufficient'])
        self.assertEqual(group['evaluated_sessions'], ['s1'])

    def test_reports_show_topic_even_when_concept_labels_match(self):
        self.evidence(topic='types')
        adap.record(self.root,self.observation())
        output=adap.report(self.root, language='es')
        self.assertIn('Tipos',Path(output['markdown']).read_text())
        self.assertIn('Tipos', ''.join(ET.fromstring(Path(output['svg']).read_text()).itertext()))

    def test_graph_uses_readable_labels_for_learning_context(self):
        self.evidence();adap.record(self.root,self.observation())
        output=adap.report(self.root, language='es')
        text=''.join(ET.fromstring(Path(output['svg']).read_text()).itertext())
        self.assertIn('Esquema',text)
        self.assertIn('pista',text)
        self.assertIn('inmediata',text)

    def test_report_language_changes_presentation_without_changing_data(self):
        for n, changes in enumerate([{}, {'outcome':'partial', 'session_id':'s2'},
                                     {'outcome':'incorrect', 'session_id':'s2'},
                                     {'outcome':'unverified', 'session_id':'s3'}], 1):
            self.evidence('e'+str(n), **changes)
            adap.record(self.root, self.observation(id='o'+str(n), evidence_id='e'+str(n)))
        state_before=(self.root/'state.json').read_bytes()
        observations_before=(self.root/'adaptacion/observaciones.jsonl').read_bytes()
        summary_before=adap.summarize(self.root)

        english=adap.report(self.root)
        english_md=Path(english['markdown']).read_text()
        english_svg=Path(english['svg']).read_text()
        spanish=adap.report(self.root, language='es')
        spanish_md=Path(spanish['markdown']).read_text()
        spanish_svg=Path(spanish['svg']).read_text()

        self.assertIn('# Results by context and strategy', english_md)
        self.assertIn('Operators / trace / standard', english_md)
        self.assertIn('Strategies: Diagram. Provisional observations.', english_md)
        self.assertIn('Correct/attempts: 1/3; partial: 1; incorrect: 1; pending: 1.', english_md)
        self.assertIn('1/3 correct; 1 pending; 2 evaluated sessions', english_svg)
        self.assertIn('# Resultados por contexto y estrategia', spanish_md)
        self.assertIn('Aciertos/intentos: 1/3; parciales: 1; incorrectos: 1; pendientes: 1.', spanish_md)
        self.assertIn('1/3 aciertos; 1 pendientes; 2 sesiones evaluadas', spanish_svg)
        for key in ['markdown', 'svg', 'source_revision', 'observation_digest']:
            self.assertEqual(english[key], spanish[key])
        self.assertEqual(set(english), {'markdown', 'svg', 'source_revision', 'generated_at', 'observation_digest'})
        self.assertEqual(set(spanish), set(english))
        self.assertEqual(Path(english['markdown']).relative_to(self.root), Path('adaptacion/balance.md'))
        self.assertEqual(Path(english['svg']).relative_to(self.root), Path('adaptacion/graficos/resultados.svg'))
        self.assertEqual((self.root/'state.json').read_bytes(), state_before)
        self.assertEqual((self.root/'adaptacion/observaciones.jsonl').read_bytes(), observations_before)
        self.assertEqual(adap.summarize(self.root), summary_before)
        english_root=ET.fromstring(english_svg)
        spanish_root=ET.fromstring(spanish_svg)
        self.assertEqual([e.attrib for e in english_root.iter()], [e.attrib for e in spanish_root.iter()])

    def test_unsupported_report_language_does_not_write(self):
        def snapshot():
            return {str(p.relative_to(self.root)):p.read_bytes()
                    for p in self.root.rglob('*') if p.is_file()}

        before=snapshot()
        with self.assertRaisesRegex(ValueError, 'language'):
            adap.report(self.root, language='fr')
        self.assertEqual(snapshot(), before)
        self.assertFalse((self.root/'adaptacion').exists())
        with self.assertRaisesRegex(ValueError, 'language'):
            adap.render({}, '2026-10-27T10:00:00+00:00', language='fr')
        adap.report(self.root)
        before=snapshot()
        with self.assertRaisesRegex(ValueError, 'language'):
            adap.report(self.root, language='fr')
        self.assertEqual(snapshot(), before)

    def test_cli_real_commands(self):
        self.evidence()
        command=[sys.executable,str(SKILL/'scripts/mentor_adaptation.py'),'--root',str(self.root)]
        r=subprocess.run(command+['record'],input=json.dumps(self.observation()),text=True,capture_output=True)
        self.assertEqual(r.returncode,0,r.stderr)
        r=subprocess.run(command+['report'],text=True,capture_output=True)
        self.assertEqual(r.returncode,0,r.stderr)
        report=json.loads(r.stdout)
        self.assertIn('Results by context and strategy', Path(report['markdown']).read_text())
        r=subprocess.run(command+['--language','es','report'],text=True,capture_output=True)
        self.assertEqual(r.returncode,0,r.stderr)
        report=json.loads(r.stdout)
        self.assertIn('Resultados por contexto y estrategia', Path(report['markdown']).read_text())
        before=Path(report['markdown']).read_bytes(),Path(report['svg']).read_bytes()
        r=subprocess.run(command+['--language','fr','report'],text=True,capture_output=True)
        self.assertNotEqual(r.returncode,0)
        self.assertEqual((Path(report['markdown']).read_bytes(),Path(report['svg']).read_bytes()), before)


if __name__ == '__main__': unittest.main()

