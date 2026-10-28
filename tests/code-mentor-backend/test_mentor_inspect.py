"""Read-only inspection must never repair or manufacture memory facts."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SKILL = Path(os.environ['MENTOR_SKILL'])
sys.path.insert(0, str(SKILL / 'scripts'))
import mentor_store as store


class InspectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'record'
        store.init_store(self.root, 'general')

    def run_inspect(self, action='status', success=True):
        r = subprocess.run([sys.executable, str(SKILL / 'scripts/mentor_inspect.py'),
                            '--root', str(self.root), action], capture_output=True, text=True, timeout=10)
        self.assertEqual(r.returncode, 0 if success else 1, r.stderr)
        self.assertTrue(r.stdout.startswith('{'), r.stderr)
        return json.loads(r.stdout)

    def write(self, name, text):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return p

    def contents(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes()
                for p in self.root.rglob('*') if p.is_file()}

    def test_status_does_not_infer_activation_write_permission_or_save_time(self):
        before = self.contents()
        value = self.run_inspect()
        self.assertEqual(value['scope'], 'general')
        self.assertEqual(value['source_revision'], 0)
        self.assertEqual(value['write_access'], 'not_tested')
        self.assertEqual(value['activation'], 'not_verified')
        self.assertIsNone(value['actual_last_save_at'])
        self.assertIsNone(value['latest_recorded_at'])
        self.assertEqual(self.contents(), before)

    def test_record_timestamp_remains_separate_from_actual_save_time(self):
        event = dict(id='e1', session_id='s1', recorded_at='2020-01-01T12:00:00Z', topic='methods',
                     activity='explain', modality='oral', assistance='none', outcome='correct',
                     evidence_summary='Synthetic response', review_due=None)
        store.apply_command(self.root, dict(request_id='r1', expected_revision=0,
                                           operation='record_evidence', payload=event))
        result = self.run_inspect()
        self.assertEqual(result['latest_recorded_at'], '2020-01-01T12:00:00Z')
        self.assertIsNone(result['actual_last_save_at'])
        self.assertEqual(result['last_receipt_revision'], 1)
        self.assertEqual(result['pending_coverage'], 'checkpoint_only; inspect accessible batches and conversation separately')

    def test_missing_versioned_document_is_reported_without_repair(self):
        result = store.apply_command(self.root, dict(request_id='doc1', expected_revision=0,
                    operation='save_document', payload=dict(id='profile', kind='profile', title='Profile',
                    content='Synthetic profile', recorded_at='2026-10-28T08:00:00Z')))
        (self.root / 'documents' / (result['record_id'] + '.md')).unlink()
        before = self.contents()
        result = self.run_inspect('audit')
        self.assertIn('missing_document', [f['code'] for f in result['findings']])
        self.assertEqual(self.contents(), before)

    def test_broken_index_links_and_unindexed_notes_are_visible(self):
        self.write('notes/index.md', '[Absent](sessions/absent.md)\n')
        self.write('notes/sessions/2026-10-28-note-a.md', '# A\nSynthetic note')
        result = self.run_inspect('audit')
        codes = [f['code'] for f in result['findings']]
        self.assertIn('broken_link', codes)
        self.assertIn('unindexed_note', codes)

    def test_safe_cross_directory_links_and_external_links_are_not_broken(self):
        self.write('notes/index.md', '[A](sessions/note-a.md#concept)\n')
        self.write('notes/sessions/note-a.md', '# Concept\n[Card](../../conocimientos/fichas/a.md)\n[Docs](https://learn.microsoft.com)')
        self.write('conocimientos/fichas/a.md', '# A\n')
        self.write('conocimientos/index.md', '[A](fichas/a.md)\n')
        value = self.run_inspect('audit')
        self.assertNotIn('broken_link', [f['code'] for f in value['findings']])
        self.assertNotIn('unsafe_link', [f['code'] for f in value['findings']])

    def test_unsafe_and_encoded_links_do_not_read_outside_root(self):
        outside = Path(self.tmp.name) / 'secret.md'
        outside.write_text('PRIVATE_SENTINEL')
        self.write('notes/index.md', '[X](../../secret.md)\n[Y](%2e%2e/%2e%2e/secret.md)\n[Z](javascript:alert(1))')
        self.write('notes/sessions/a.md', '# A')
        (self.root / 'notes' / 'escape.md').symlink_to(outside)
        value = self.run_inspect('audit')
        self.assertIn('unsafe_link', [f['code'] for f in value['findings']])
        self.assertIn('unsafe_path', [f['code'] for f in value['findings']])
        self.assertNotIn('PRIVATE_SENTINEL', json.dumps(value))

    def test_duplicate_current_notes_are_candidates_but_history_is_not(self):
        self.write('notes/index.md', '[A](sessions/a.md)\n[B](sessions/b.md)\n')
        for name in ['sessions/a.md', 'sessions/b.md', 'history/note-a/r0001.md']:
            self.write('notes/' + name, '# Same\nSynthetic repeated content\n')
        value = self.run_inspect('audit')
        finding = next(f for f in value['findings'] if f['code'] == 'duplicate_content')
        self.assertEqual(finding['paths'], ['notes/sessions/a.md', 'notes/sessions/b.md'])
        self.assertEqual(finding['severity'], 'review')

    def test_stale_progress_is_reported_without_regeneration(self):
        self.write('progress/index.html', '<script id="progress-data" type="application/json">'
                   + json.dumps(dict(source_revision=99, source_digest='old')) + '</script>')
        before = self.contents()
        value = self.run_inspect('audit')
        self.assertIn('stale_progress', [f['code'] for f in value['findings']])
        self.assertEqual(self.contents(), before)

    def test_large_documents_make_coverage_explicitly_incomplete(self):
        self.write('notes/index.md', 'x' * (256 * 1024 + 1))
        value = self.run_inspect('audit')
        self.assertFalse(value['coverage']['complete'])
        self.assertIn('scan_limit', [f['code'] for f in value['findings']])

    def test_invalid_state_is_diagnosed_without_creating_or_repairing_it(self):
        (self.root / 'state.json').write_text('{broken')
        before = self.contents()
        value = self.run_inspect('audit', success=False)
        self.assertFalse(value['ok'])
        self.assertEqual(value['error_code'], 'invalid_or_unreadable_record')
        self.assertEqual(self.contents(), before)

    def test_missing_root_is_not_initialized(self):
        self.root = self.root / 'not-configured'
        self.run_inspect(success=False)
        self.assertFalse(self.root.exists())

    def test_interrupted_write_artifacts_are_reported_without_removal(self):
        self.write('.write.lock', '12345')
        self.write('.pending-abcd', 'partial state')
        self.write('documents/unreferenced.md', 'partial document')
        self.write('progress/.pending-report', 'partial report')
        before = self.contents()
        value = self.run_inspect('audit')
        codes = {f['code'] for f in value['findings']}
        self.assertIn('write_lock_present', codes)
        self.assertIn('interrupted_write_candidate', codes)
        self.assertIn('unreferenced_document', codes)
        self.assertEqual(before, self.contents())
        status = self.run_inspect()
        self.assertEqual(status['write_blockers'], ['writer_or_interrupted_operation'])

    def test_empty_existing_progress_report_is_not_a_clean_audit(self):
        self.write('progress/index.html', '')
        value = self.run_inspect('audit')
        self.assertIn('unverifiable_progress', {f['code'] for f in value['findings']})

    def test_self_referential_symlink_does_not_crash_audit(self):
        self.write('notes/index.md', '[A](sessions/loop.md)')
        path = self.root / 'notes/sessions/loop.md'
        path.parent.mkdir()
        path.symlink_to('loop.md')
        value = self.run_inspect('audit')
        self.assertFalse(value['coverage']['complete'])
        self.assertIn('unsafe_path', {f['code'] for f in value['findings']})

    def test_state_symlink_loop_returns_structured_error(self):
        path = self.root / 'state.json'
        path.unlink()
        path.symlink_to('state.json')
        value = self.run_inspect('audit', success=False)
        self.assertFalse(value['ok'])
        self.assertTrue(path.is_symlink())

    def test_markdown_link_titles_do_not_create_false_missing_notes(self):
        self.write('notes/index.md', '[A](sessions/a.md "A lesson title")\n[B](<sessions/b b.md> "B title")\n')
        self.write('notes/sessions/a.md', '# A\n')
        self.write('notes/sessions/b b.md', '# B\n')
        value = self.run_inspect('audit')
        codes = {f['code'] for f in value['findings']}
        self.assertNotIn('broken_link', codes)
        self.assertNotIn('unindexed_note', codes)

    def test_invalid_utf8_counts_toward_actual_scan_budget(self):
        import mentor_inspect
        for number in range(10):
            path = self.root / f'notes/sessions/{number}.md'
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b'\xff' * (256 * 1024))
        real_open = Path.open
        total_read = 0

        class TrackedReader:
            def __init__(self, stream):
                self.stream = stream
            def __enter__(self):
                self.stream.__enter__()
                return self
            def __exit__(self, *args):
                return self.stream.__exit__(*args)
            def read(self, size=-1):
                nonlocal total_read
                data = self.stream.read(size)
                total_read += len(data)
                return data

        def monitored_open(path, *args, **kwargs):
            stream = real_open(path, *args, **kwargs)
            return TrackedReader(stream) if '/notes/sessions/' in str(path) else stream

        with patch.object(Path, 'open', monitored_open):
            value = mentor_inspect.inspect_root(self.root, 'audit')
        self.assertLessEqual(total_read, 2 * 1024 * 1024)
        self.assertFalse(value['coverage']['complete'])
        self.assertIn('unreadable_file', {f['code'] for f in value['findings']})

    def test_weekly_index_links_are_checked_within_the_same_scope(self):
        self.write('notes/weeks/index.md', '[Week](2026-W44.md)\n')
        value = self.run_inspect('audit')
        self.assertTrue(any(f['code'] == 'broken_link' and f['target'] == 'notes/weeks/2026-W44.md'
                            for f in value['findings']))

    def test_unindexed_week_is_visible_but_index_and_history_are_not_blocks(self):
        self.write('notes/weeks/index.md', '# Weeks\n')
        self.write('notes/weeks/2026-W44.md', '# Synthetic week 44\n')
        self.write('notes/history/week-2026-w44/r0001.md', '# Old week\n')
        before = self.contents()
        value = self.run_inspect('audit')
        unindexed = [f['path'] for f in value['findings'] if f['code'] == 'unindexed_week']
        self.assertEqual(unindexed, ['notes/weeks/2026-W44.md'])
        self.assertEqual(before, self.contents())


if __name__ == '__main__':
    unittest.main()
