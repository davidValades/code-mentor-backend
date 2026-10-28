import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('collection_packaging', ROOT / 'tools/build_plugin.py')
packaging = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packaging)


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.name = 'code-mentor-backend'
        shutil.copytree(ROOT / 'skills' / self.name, self.root / 'skills' / self.name)
        shutil.copytree(ROOT / 'packages' / self.name, self.root / 'packages' / self.name)
        shutil.copytree(ROOT / 'assets' / self.name, self.root / 'assets' / self.name)
        shutil.copy2(ROOT / 'LICENSE', self.root / 'LICENSE')

    def test_package_contains_one_skill_and_complete_resources(self):
        other = self.root / 'skills' / 'not-to-be-bundled'
        other.mkdir()
        (other / 'SKILL.md').write_text('unrelated', encoding='utf-8')
        output = packaging.build(self.name, self.root)
        with zipfile.ZipFile(output) as archive:
            names = archive.namelist()
            self.assertEqual(len(names), len(set(names)))
            self.assertTrue(all(p.startswith('skills/code-mentor-backend/') or p.startswith('assets/') or p in {'plugin.json', 'LICENSE'} for p in names))
            self.assertIn('skills/code-mentor-backend/references/teaching-exploration.md', names)
            self.assertIn('skills/code-mentor-backend/assets/templates/state.json', names)
            self.assertIn('assets/logo.png', names)
            self.assertEqual(json.loads(archive.read('plugin.json'))['version'], '2.10.0')
            self.assertNotIn('unrelated', ''.join(names))
            self.assertFalse(any('__pycache__' in p or p.endswith('.pyc') for p in names))

    def test_build_is_reproducible(self):
        first = packaging.build(self.name, self.root).read_bytes()
        self.assertEqual(first, packaging.build(self.name, self.root).read_bytes())

    def test_version_mismatch_rejected_before_output(self):
        path = self.root / 'packages' / self.name / 'plugin.json'
        data = json.loads(path.read_text())
        data['version'] = '9.0.0'
        path.write_text(json.dumps(data))
        output = self.root / 'should-not-exist.zip'
        with self.assertRaisesRegex(ValueError, 'versions differ'):
            packaging.build(self.name, self.root, output)
        self.assertFalse(output.exists())

    def test_symlink_and_path_traversal_rejected(self):
        with self.assertRaisesRegex(ValueError, 'invalid skill name'):
            packaging.build('../outside', self.root)
        outside = self.root / 'private-note.md'
        outside.write_text('not package data')
        (self.root / 'skills' / self.name / 'assets' / 'leak.md').symlink_to(outside)
        with self.assertRaisesRegex(ValueError, 'symlinks'):
            packaging.build(self.name, self.root)
