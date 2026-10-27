import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest

SKILL = Path(os.environ['MENTOR_SKILL'])
spec = importlib.util.spec_from_file_location('mentor_store', SKILL / 'scripts/mentor_store.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def event(**changes):
    value = dict(id='e1', session_id='s1', recorded_at='2026-10-26T16:00:00+00:00',
                 topic='methods', activity='explain', modality='oral', assistance='hint',
                 outcome='correct', evidence_summary='Explicó entrada y retorno con una pista.', review_due=None)
    value.update(changes)
    return value


class SchemaTests(unittest.TestCase):
    def test_empty_state_has_no_achievements(self):
        s = m.new_state('general')
        m.validate_state(s)
        self.assertEqual(s['events'], [])
        self.assertEqual(s['sessions'], [])

    def test_invalid_scope_rejected(self):
        with self.assertRaises(ValueError):
            m.new_state('company-wide')

    def test_general_event_rejects_company_fields(self):
        s = m.new_state('general')
        s['events'] = [event(source_refs=[{'path': 'Services/A.cs'}])]
        with self.assertRaises(ValueError):
            m.validate_state(s)

    def test_invalid_event_enums_rejected(self):
        s = m.new_state('general')
        s['events'] = [event(assistance='independent-ish')]
        with self.assertRaises(ValueError):
            m.validate_state(s)

    def test_source_path_must_be_relative(self):
        s = m.new_state('project')
        for path in ['/etc/passwd', '../secrets', 'C:\\repos\\A.cs', 'https://user:token@host/A.cs']:
            s['events'] = [event(task_id='t1', source_refs=[dict(path=path, commit=None, branch='main', dirty=True, observed_at='2026-10-26T16:00:00+00:00')])]
            with self.subTest(path=path), self.assertRaises(ValueError):
                m.validate_state(s)

    def test_duplicate_evidence_rejected(self):
        s = m.new_state('general')
        s['events'] = [event(), event()]
        with self.assertRaises(ValueError):
            m.validate_state(s)

    def test_timezone_required(self):
        s = m.new_state('general')
        s['events'] = [event(recorded_at='2026-10-26')]
        with self.assertRaises(ValueError):
            m.validate_state(s)

    def test_templates_initialize_without_mastery(self):
        template = json.loads((SKILL / 'assets/templates/state.json').read_text())
        m.validate_state(template)
        self.assertEqual(template['events'], [])
        self.assertIsNone(template['checkpoint'])


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'learning'
        m.init_store(self.root, 'general')

    def command(self, op='record_evidence', payload=None, **changes):
        c = dict(request_id='req1', expected_revision=0, operation=op, payload=payload or event())
        c.update(changes)
        return c

    def test_readback_and_identical_retry(self):
        c = self.command()
        a = m.apply_command(self.root, c)
        b = m.apply_command(self.root, c)
        self.assertEqual(a['revision'], 1)
        self.assertTrue(b['replayed'])
        self.assertEqual(m.read_state(self.root)['events'][0]['evidence_summary'], 'Explicó entrada y retorno con una pista.')
        self.assertEqual(len(m.read_state(self.root)['events']), 1)

    def test_reused_id_different_payload_rejected(self):
        m.apply_command(self.root, self.command())
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command(payload=event(topic='types')))

    def test_stale_revision_preserves_data(self):
        m.apply_command(self.root, self.command())
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command(request_id='req2', payload=event(id='e2')))
        self.assertEqual(m.read_state(self.root)['revision'], 1)

    def test_corrupt_state_never_overwritten(self):
        path = self.root / 'state.json'
        path.write_text('{broken')
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command())
        self.assertEqual(path.read_text(), '{broken')

    def test_lock_rejects_writer(self):
        (self.root / '.write.lock').write_text('other writer')
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command())
        self.assertEqual(m.read_state(self.root)['revision'], 0)
        self.assertTrue((self.root / '.write.lock').exists())

    def test_completed_session_counted_once(self):
        p = dict(id='s1', recorded_at='2026-10-26T16:00:00+00:00')
        m.apply_command(self.root, self.command('complete_session', p))
        m.apply_command(self.root, self.command('complete_session', p, request_id='req2', expected_revision=1))
        self.assertEqual(len(m.read_state(self.root)['sessions']), 1)

    def test_symlink_state_is_rejected(self):
        outside = Path(self.temp.name) / 'outside.json'
        outside.write_text('{}')
        (self.root / 'state.json').unlink()
        (self.root / 'state.json').symlink_to(outside)
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command())
        self.assertEqual(outside.read_text(), '{}')

    def test_document_versions_preserve_history(self):
        p = dict(id='profile', kind='profile', title='Perfil', content='# Objetivo\nAprender C#', recorded_at='2026-10-26T16:00:00+00:00')
        m.apply_command(self.root, self.command('save_document', p))
        p2 = dict(p, content='# Objetivo\nLeer métodos')
        m.apply_command(self.root, self.command('save_document', p2, request_id='req2', expected_revision=1))
        docs = m.read_state(self.root)['documents']
        self.assertEqual(len(docs), 2)
        self.assertEqual((self.root / docs[0]['path']).read_text(), '# Objetivo\nAprender C#')
        self.assertEqual((self.root / docs[1]['path']).read_text(), '# Objetivo\nLeer métodos')

    def test_project_document_cannot_enter_general_store(self):
        p = dict(id='t1', kind='task', title='Trabajo', content='contenido laboral', recorded_at='2026-10-26T16:00:00+00:00')
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command('save_document', p))

    def test_replace_failure_preserves_previous_state(self):
        from unittest.mock import patch
        before = (self.root / 'state.json').read_bytes()
        with patch.object(m.os, 'replace', side_effect=OSError('disk failure')):
            with self.assertRaises(OSError):
                m.apply_command(self.root, self.command())
        self.assertEqual((self.root / 'state.json').read_bytes(), before)
        self.assertFalse((self.root / '.write.lock').exists())

    def test_concurrent_writers_do_not_lose_update(self):
        import subprocess
        command = [os.sys.executable, str(SKILL / 'scripts/mentor_store.py'), '--root', str(self.root), 'apply']
        a = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        b = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        a.stdin.write(json.dumps(self.command())); a.stdin.close(); a.stdin = None
        b.stdin.write(json.dumps(self.command(request_id='req2', payload=event(id='e2')))); b.stdin.close(); b.stdin = None
        a.communicate(); b.communicate()
        self.assertEqual(sorted([a.returncode, b.returncode]), [0, 1])
        self.assertEqual(len(m.read_state(self.root)['events']), 1)


class TransferTests(unittest.TestCase):
    setUp = StoreTests.setUp
    command = StoreTests.command

    def test_summary_projects_only_selected_evidence(self):
        s = m.new_state('general')
        s['events'] = [event(), event(id='e2', topic='types')]
        s['checkpoint'] = dict(session_id='s1', topic='methods', evidence_id='e1', pending_question='Qué retorna', next_step='private task text', recorded_at='2026-10-26T16:00:00+00:00')
        summary = m.prepare_summary(s, ['e1'])
        self.assertEqual([e['id'] for e in summary['events']], ['e1'])
        self.assertNotIn('private task text', json.dumps(summary))
        with self.assertRaises(ValueError):
            m.prepare_summary(s, ['missing'])

    def test_project_summary_needs_curated_text(self):
        s = m.new_state('project')
        s['events'] = [event(task_id='t1', source_refs=[])]
        with self.assertRaises(ValueError):
            m.prepare_summary(s, ['e1'])
        summary = m.prepare_summary(s, ['e1'], 'Practicar entradas y retornos con un ejemplo genérico.')
        self.assertEqual(summary['content'], 'Practicar entradas y retornos con un ejemplo genérico.')
        self.assertNotIn('task_id', json.dumps(summary))

    def test_unapproved_summary_is_not_exported(self):
        s = m.prepare_summary(m.new_state('general'), [])
        target = Path(self.temp.name) / 'summary.json'
        with self.assertRaises(ValueError):
            m.export_summary(s, '', target)
        self.assertFalse(target.exists())

    def test_modified_summary_invalidates_approval(self):
        s = m.prepare_summary(m.new_state('general'), [])
        approved = m.digest(s)
        s['content'] = 'Alterado tras revisión'
        target = Path(self.temp.name) / 'summary.json'
        with self.assertRaises(ValueError):
            m.export_summary(s, approved, target)
        self.assertFalse(target.exists())

    def test_exact_summary_export_and_no_overwrite(self):
        s = m.prepare_summary(m.new_state('general'), [])
        target = Path(self.temp.name) / 'summary.json'
        m.export_summary(s, m.digest(s), target)
        self.assertEqual(json.loads(target.read_text()), s)
        with self.assertRaises(ValueError):
            m.export_summary(s, m.digest(s), target)

    def test_observation_requires_confirmation_to_generalize(self):
        project = Path(self.temp.name) / 'project'
        m.init_store(project, 'project')
        p = dict(id='o1', task_id='t1', statement='Mantener firmas en esta tarea', source='Petición descrita por alumno', recorded_at='2026-10-26T16:00:00+00:00')
        m.apply_command(project, self.command('record_observation', p))
        self.assertFalse(m.read_state(project)['observations'][0]['confirmed'])
        with self.assertRaises(ValueError):
            m.apply_command(project, self.command('confirm_convention', dict(id='o1', user_confirmed=False, scope='proyecto', reason='probable'), request_id='r2', expected_revision=1))
        m.apply_command(project, self.command('confirm_convention', dict(id='o1', user_confirmed=True, scope='solo este proyecto', reason='Confirmado por alumno'), request_id='r3', expected_revision=1))
        self.assertTrue(m.read_state(project)['observations'][0]['confirmed'])

    def test_general_store_rejects_work_observations(self):
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command('record_observation', dict(id='o1', task_id='t1', statement='nombre laboral', source='jefe', recorded_at='2026-10-26T16:00:00+00:00')))


class LearningTests(unittest.TestCase):
    setUp = StoreTests.setUp
    command = StoreTests.command

    def test_review_after_three_distinct_sessions(self):
        for i in range(1, 4):
            m.apply_command(self.root, self.command('complete_session', dict(id=f's{i}', recorded_at='2026-10-26T16:00:00+00:00'), request_id=f'r{i}', expected_revision=i-1))
            self.assertEqual(m.review_due(m.read_state(self.root)), i == 3)
        m.apply_command(self.root, self.command('record_review', dict(id='rev1', recorded_at='2026-10-26T16:00:00+00:00', reason='Tres sesiones', result='Sin cambios necesarios'), request_id='r4', expected_revision=3))
        self.assertFalse(m.review_due(m.read_state(self.root)))

    def test_pause_does_not_complete_session(self):
        p = dict(session_id='s1', topic='methods', evidence_id=None, pending_question='¿Qué retorna?', next_step='Responder oralmente', recorded_at='2026-10-26T16:00:00+00:00')
        m.apply_command(self.root, self.command('save_checkpoint', p))
        self.assertFalse(m.review_due(m.read_state(self.root)))
        self.assertEqual(m.read_state(self.root)['sessions'], [])

    def test_requested_review_is_immediate(self):
        self.assertTrue(m.review_due(m.new_state('general'), requested=True))

    def test_difficulty_recurrence_requires_separate_sessions(self):
        s = m.new_state('general')
        s['events'] = [event(outcome='incorrect'), event(id='e2', outcome='partial')]
        self.assertFalse(m.review_due(s))
        s['events'][1]['session_id'] = 's2'
        self.assertTrue(m.review_due(s))

    def test_declared_or_copied_solution_not_autonomy(self):
        for e in [event(activity='declared', assistance='none'), event(activity='implement', modality='ide', assistance='solution')]:
            s = m.new_state('general'); s['events'] = [e]
            self.assertEqual(m.learning_status(s, 'methods'), 'explored')

    def test_oral_explanation_not_practical_autonomy(self):
        s = m.new_state('general'); s['events'] = [event(assistance='none')]
        self.assertEqual(m.learning_status(s, 'methods'), 'conceptual')

    def test_consolidation_requires_later_independent_retrieval(self):
        s = m.new_state('general')
        s['events'] = [event(activity='implement', modality='ide', assistance='none')]
        self.assertEqual(m.learning_status(s, 'methods'), 'autonomous')
        s['events'].append(event(id='e2', session_id='s2', activity='retrieve', assistance='none', recorded_at='2026-10-26T20:00:00+00:00'))
        self.assertEqual(m.learning_status(s, 'methods'), 'autonomous')
        s['events'][1]['recorded_at'] = '2026-10-27T16:00:00+00:00'
        self.assertEqual(m.learning_status(s, 'methods'), 'consolidated')

    def test_case_attempt_preserves_real_assistance(self):
        case = dict(id='c1', topic='methods', prompt='Explica el retorno', hints=['Piensa en la salida'], solution='Dato devuelto', criteria=['Distingue retorno de salida en consola'], validation='reviewed', validation_evidence='Revisión conceptual, no ejecución', mode='oral')
        m.apply_command(self.root, self.command('save_case', case))
        attempt = dict(id='a1', case_id='c1', session_id='s1', response='Dato que devuelve', assistance='hint', outcome='correct', recorded_at='2026-10-26T16:00:00+00:00')
        m.apply_command(self.root, self.command('record_case_attempt', attempt, request_id='r2', expected_revision=1))
        state = m.read_state(self.root)
        self.assertEqual(state['attempts'][0]['assistance'], 'hint')
        self.assertEqual(m.learning_status(state, 'methods'), 'pending')


class ImprovementTests(unittest.TestCase):
    setUp = StoreTests.setUp
    command = StoreTests.command

    def propose(self):
        m.apply_command(self.root, self.command())
        p = dict(id='i1', reason='Necesita ejemplos más pequeños', evidence_ids=['e1'], baseline='actual', candidate={'explanation_words': 100, 'example_lines': 6, 'analogies': True, 'diagrams': 'when_interaction'})
        m.apply_command(self.root, self.command('propose_improvement', p, request_id='p1', expected_revision=1))

    def evaluate(self):
        p = dict(id='v1', improvement_id='i1', kind='model', results='Candidata más concisa; exactitud similar. Juicio de modelo, no eficacia.',
                 cases=[dict(id='design1', split='design', baseline_response='Respuesta actual', candidate_response='Respuesta candidata'), dict(id='holdout1', split='heldout', baseline_response='Actual nuevo caso', candidate_response='Candidata nuevo caso')],
                 checks={'accuracy': True, 'one_concept': True, 'permissions': True})
        m.apply_command(self.root, self.command('record_evaluation', p, request_id='v1', expected_revision=2))

    def test_passing_evaluation_never_activates(self):
        self.propose(); self.evaluate()
        self.assertIsNone(m.active_strategy(m.read_state(self.root)))
        self.assertEqual(m.read_state(self.root)['improvements'][0]['status'], 'evaluated')

    def test_proposal_cannot_change_permissions(self):
        p = dict(id='i1', reason='más rápido', evidence_ids=[], baseline='actual', candidate={'permissions': 'edit_all'})
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command('propose_improvement', p))

    def test_unknown_evidence_rejected(self):
        p = dict(id='i1', reason='caso', evidence_ids=['missing'], baseline='actual', candidate={'example_lines': 4})
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command('propose_improvement', p))

    def test_trial_requires_explicit_choice(self):
        self.propose(); self.evaluate()
        p = dict(id='i1', action='start', user_confirmed=False, summary='Prueba una sesión')
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command('set_trial', p, request_id='t1', expected_revision=3))

    def test_final_acceptance_and_revert_restore_prior(self):
        self.propose(); self.evaluate()
        m.apply_command(self.root, self.command('set_trial', dict(id='i1', action='decline', user_confirmed=True, summary='Prefiere aprobar sin prueba'), request_id='t1', expected_revision=3))
        p = dict(id='i1', decision='accept', user_confirmed=False, reason='Quiere conservarla')
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command('decide_improvement', p, request_id='d1', expected_revision=4))
        p['user_confirmed'] = True
        m.apply_command(self.root, self.command('decide_improvement', p, request_id='d2', expected_revision=4))
        self.assertEqual(m.active_strategy(m.read_state(self.root))['example_lines'], 6)
        m.apply_command(self.root, self.command('decide_improvement', dict(id='i1', decision='revert', user_confirmed=True, reason='Volver al método anterior'), request_id='d3', expected_revision=5))
        self.assertIsNone(m.active_strategy(m.read_state(self.root)))

    def test_acceptance_blocked_during_unfinished_trial(self):
        self.propose(); self.evaluate()
        m.apply_command(self.root, self.command('set_trial', dict(id='i1', action='start', user_confirmed=True, summary='Solo esta sesión'), request_id='t1', expected_revision=3))
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command('decide_improvement', dict(id='i1', decision='accept', user_confirmed=True, reason='Sin resultado'), request_id='d1', expected_revision=4))

    def test_heldout_and_accuracy_required(self):
        self.propose()
        p = dict(id='v1', improvement_id='i1', kind='model', results='Solo una opinión', cases=[], checks={'one_concept': True})
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command('record_evaluation', p, request_id='v1', expected_revision=2))


class ReviewRegressionTests(unittest.TestCase):
    setUp = StoreTests.setUp
    command = StoreTests.command

    def test_corrupt_structured_session_does_not_pass_or_get_overwritten(self):
        state = m.read_state(self.root)
        state['sessions'] = [{'id': 's1'}]
        path = self.root / 'state.json'
        path.write_text(json.dumps(state))
        before = path.read_bytes()
        with self.assertRaises(ValueError):
            m.read_state(self.root)
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command())
        self.assertEqual(path.read_bytes(), before)

    def test_invalid_receipt_fingerprint_never_replayed(self):
        state = m.read_state(self.root)
        state['receipts'] = {'req1': {'fingerprint': 'broken', 'result': {'revision': 500, 'record_id': 'fake', 'replayed': False}}}
        (self.root / 'state.json').write_text(json.dumps(state))
        with self.assertRaises(ValueError):
            m.apply_command(self.root, self.command())

    def test_export_permissions_are_private_on_posix(self):
        if os.name == 'nt': self.skipTest('POSIX permission bits')
        import stat
        old = os.umask(0o022)
        self.addCleanup(os.umask, old)
        summary = m.prepare_summary(m.new_state('general'), [])
        target = Path(self.temp.name) / 'approved.json'
        m.export_summary(summary, m.digest(summary), target)
        self.assertEqual(stat.S_IMODE(target.stat().st_mode), 0o600)

    def test_status_cli_exposes_learning_status_and_review(self):
        import subprocess
        m.apply_command(self.root, self.command())
        cmd = [os.sys.executable, str(SKILL / 'scripts/mentor_store.py'), '--root', str(self.root), 'status']
        result = subprocess.run(cmd, text=True, capture_output=True, check=True)
        data = json.loads(result.stdout)
        self.assertEqual(data['topics']['methods'], 'guided')
        self.assertFalse(data['review_due'])

    def test_invalid_case_reference_does_not_pass_validation(self):
        state = m.read_state(self.root)
        state['attempts'] = [dict(id='a1', case_id='missing', session_id='s1', response='x', assistance='none', outcome='correct', recorded_at='2026-10-26T16:00:00+00:00')]
        with self.assertRaises(ValueError):
            m.validate_state(state)

    def test_bad_nested_improvement_never_activates(self):
        state = m.read_state(self.root)
        state['improvements'] = [dict(id='i1', status='accepted', candidate={'permissions': 'edit_all'})]
        with self.assertRaises(ValueError):
            m.active_strategy(state)
