"""Separate interpreter processes must reopen the same authoritative record."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SKILL = Path(os.environ['MENTOR_SKILL'])


class MemoryContinuityTests(unittest.TestCase):
    def test_save_reopen_retry_inspect_and_report_keep_one_record(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / 'private-record'

            def call(script, action, payload=None, extra=()):
                command = [sys.executable, str(SKILL / 'scripts' / script), '--root', str(root), action, *extra]
                result = subprocess.run(command, input=None if payload is None else json.dumps(payload),
                                        capture_output=True, text=True, timeout=15)
                self.assertEqual(result.returncode, 0, result.stderr)
                return json.loads(result.stdout)

            call('mentor_store.py', 'init', extra=['--scope', 'general'])
            command = dict(request_id='continuity-profile-v1', expected_revision=0, operation='save_document',
                           payload=dict(id='profile', kind='profile', title='Synthetic profile',
                                        content='Synthetic QA only. Need method return-value practice.',
                                        recorded_at='2026-10-28T08:00:00Z'))
            first = call('mentor_store.py', 'apply', command)
            replay = call('mentor_store.py', 'apply', command)
            self.assertTrue(replay['replayed'])
            self.assertEqual(replay['record_id'], first['record_id'])
            record = call('mentor_store.py', 'read')
            self.assertEqual(record['revision'], 1)
            self.assertEqual(len(record['documents']), 1)
            saved = root / record['documents'][0]['path']
            self.assertEqual(saved.read_text(), command['payload']['content'])

            report = call('mentor_progress.py', 'report', extra=['--demo', '--language', 'es'])
            self.assertTrue(Path(report['html']).exists())
            before = {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            status = call('mentor_inspect.py', 'status')
            self.assertIn('available', status['documents'][0])
            self.assertTrue(status['documents'][0]['available'])
            self.assertEqual(status['source_revision'], 1)
            self.assertEqual(status['counts']['events'], 0)
            self.assertIsNone(status['actual_last_save_at'])
            audit = call('mentor_inspect.py', 'audit')
            self.assertEqual(audit['findings'], [])
            self.assertTrue(audit['coverage']['complete'])
            self.assertEqual(before, {p.relative_to(root).as_posix(): p.read_bytes()
                                      for p in root.rglob('*') if p.is_file()})
            saved.unlink()
            unavailable = call('mentor_inspect.py', 'status')
            self.assertFalse(unavailable['documents'][0]['available'])


if __name__ == '__main__':
    unittest.main()
