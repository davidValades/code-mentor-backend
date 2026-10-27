"""Build one portable plugin from the canonical sources in this collection."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import tempfile
import zipfile


def build(name: str, root: Path, output: Path | None = None) -> Path:
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
        raise ValueError('invalid skill name')
    root = root.resolve()
    skill = root / 'skills' / name
    manifest_path = root / 'packages' / name / 'plugin.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    version = manifest.get('version', '')
    if manifest.get('name') != name or manifest.get('$schema') != 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json':
        raise ValueError('manifest identity or schema mismatch')
    if not isinstance(version, str) or not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError('strict release version required')
    source = (skill / 'SKILL.md').read_text(encoding='utf-8')
    declared = re.search(r'^# Code Mentor Backend — v([0-9.]+)$', source, re.M) if name == 'code-mentor-backend' else None
    if name == 'code-mentor-backend' and (not declared or version != declared[1] + '.0'):
        raise ValueError('source and package versions differ')
    entries = {'plugin.json': manifest_path.read_bytes(), 'LICENSE': (root / 'LICENSE').read_bytes()}
    for path in sorted(skill.rglob('*')):
        relative = path.relative_to(skill)
        if path.is_symlink():
            raise ValueError('symlinks are not packaged')
        if '__pycache__' in relative.parts or path.suffix == '.pyc':
            continue
        if path.is_file():
            if relative.parts[0] not in {'SKILL.md', 'references', 'assets', 'agents', 'scripts'}:
                raise ValueError('unexpected file in skill source: ' + str(relative))
            entries['skills/' + name + '/' + relative.as_posix()] = path.read_bytes()
    artwork = root / 'assets' / name
    if artwork.exists():
        for path in sorted(artwork.rglob('*')):
            if path.is_symlink():
                raise ValueError('symlinks are not packaged')
            if path.is_file():
                entries['assets/' + path.relative_to(artwork).as_posix()] = path.read_bytes()
    interface = manifest.get('extensions', {}).get('com.openai', {}).get('interface', {})
    for key in ['logo', 'composerIcon']:
        value = interface.get(key)
        if value and not value.startswith('https://') and value.removeprefix('./') not in entries:
            raise ValueError('missing interface asset: ' + str(value))
    output = output or root / 'dist' / name / (name + '-' + version + '.zip')
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=output.parent, suffix='.zip', delete=False) as temporary:
        pending = Path(temporary.name)
    try:
        with zipfile.ZipFile(pending, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path, data in sorted(entries.items()):
                item = zipfile.ZipInfo(path, date_time=(1980, 1, 1, 0, 0, 0))
                item.compress_type = zipfile.ZIP_DEFLATED
                item.create_system = 3
                item.external_attr = 0o100644 << 16
                archive.writestr(item, data)
        pending.replace(output)
    finally:
        pending.unlink(missing_ok=True)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skill')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        path = build(args.skill, Path(__file__).resolve().parents[1], args.output)
    except (ValueError, OSError, KeyError) as error:
        parser.error(str(error))
    print(json.dumps({'archive': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
