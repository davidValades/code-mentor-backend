"""Read-only memory status and bounded mechanical audit. Never repairs records."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import mentor_store as store


MAX_FILES = 200
MAX_BYTES = 2 * 1024 * 1024
MAX_FILE_BYTES = 256 * 1024
MAX_ENTRIES = 1000


def safe_file(root, name):
    try:
        return store.safe_file(root, name)
    except RuntimeError as exc:
        raise ValueError('unsafe path resolution loop') from exc


def inspect_root(root: Path, action: str = 'status') -> dict:
    store.require(action in ('status', 'audit'), 'unknown inspection action')
    root = store.safe_root(root)
    state = store.read_state(root)
    source_digest = store.digest(state)
    skill_file = Path(__file__).resolve().parents[1] / 'SKILL.md'
    version = re.search(r'^# Code Mentor Backend — v(\S+)', skill_file.read_text(), re.M)
    latest = {}
    for doc in state['documents']:
        latest[doc['document_id']] = doc
    documents = []
    for doc in latest.values():
        try:
            available = safe_file(root, doc['path']).is_file()
        except (ValueError, OSError):
            available = False
        documents.append(dict(id=doc['document_id'], path=doc['path'],
                              recorded_at=doc['recorded_at'], available=available))
    dates = [item['recorded_at'] for key in ('events', 'sessions', 'reviews', 'documents')
             for item in state[key]]
    try:
        blockers = ['writer_or_interrupted_operation'] if safe_file(root, '.write.lock').exists() else []
    except (ValueError, OSError):
        blockers = ['unsafe_or_unreadable_lock_path']
    result = dict(ok=True, action=action, inspected_skill_source=str(skill_file),
                  inspected_skill_version=version.group(1) if version else None,
                  activation='not_verified', root=str(root), scope=state['scope'],
                  observed_at=datetime.now(timezone.utc).isoformat(),
                  source_revision=state['revision'], source_digest=source_digest,
                  write_access='not_tested', persistence='not_established_by_read',
                  write_blockers=blockers,
                  actual_last_save_at=None,
                  latest_recorded_at=max(dates, key=store.timestamp) if dates else None,
                  last_receipt_revision=max((r['result']['revision'] for r in state['receipts'].values()), default=None),
                  checkpoint=state['checkpoint'],
                  pending_coverage='checkpoint_only; inspect accessible batches and conversation separately',
                  documents=documents,
                  counts={k:len(state[k]) for k in ('events', 'sessions', 'reviews', 'documents')})
    if action == 'audit':
        result.update(audit_files(root, state))
    store.require(store.digest(store.read_state(root)) == source_digest,
                  'STALE: record changed during inspection; retry without writing')
    return result


def audit_files(root: Path, state: dict) -> dict:
    findings, contents = [], {}
    coverage = dict(complete=True, checked_files=0, checked_bytes=0,
                    max_files=MAX_FILES, max_bytes=MAX_BYTES, max_file_bytes=MAX_FILE_BYTES,
                    metadata_entries=0, max_metadata_entries=MAX_ENTRIES,
                    scope='referenced documents, current note/card indexes and files, progress HTML',
                    anchors_checked=False, semantic_review=False)

    def finding(code, path, *, severity='review', **extra):
        findings.append(dict(code=code, path=path, severity=severity, **extra))

    def read(name, *, required=False):
        if name in contents:
            return contents[name]
        try:
            path = safe_file(root, name)
            if not path.exists():
                if required:
                    finding('missing_document', name)
                return None
            if not path.is_file():
                finding('not_a_file', name)
                coverage['complete'] = False
                return None
            size = path.stat().st_size
            if (coverage['checked_files'] >= MAX_FILES or size > MAX_FILE_BYTES
                    or coverage['checked_bytes'] + size > MAX_BYTES):
                coverage['complete'] = False
                finding('scan_limit', name)
                return None
            # Charge every read before decoding, including corrupt input.
            with path.open('rb') as stream:
                data = stream.read(min(MAX_FILE_BYTES, MAX_BYTES-coverage['checked_bytes']))
            coverage['checked_files'] += 1
            coverage['checked_bytes'] += len(data)
            if path.stat().st_size > len(data):
                coverage['complete'] = False
                finding('scan_limit', name)
                return None
            text = data.decode('utf-8')
            contents[name] = text
            return text
        except UnicodeError:
            coverage['complete'] = False
            finding('unreadable_file', name)
        except ValueError:
            coverage['complete'] = False
            finding('unsafe_path', name)
        except OSError:
            coverage['complete'] = False
            finding('unreadable_file', name)
        return None

    def local_target(source, target):
        match = re.fullmatch(r'''(?:<([^>]+)>|(\S+?))(?:\s+(?:"[^"]*"|'[^']*'|\([^)]*\)))?''', target.strip())
        store.require(match is not None, 'unsupported Markdown destination')
        target = match.group(1) or match.group(2)
        parsed = urlsplit(target)
        if parsed.scheme in ('https', 'http', 'mailto'):
            return None
        if parsed.scheme or parsed.netloc or '\\' in target:
            raise ValueError('unsupported or unsafe link')
        decoded = unquote(parsed.path)
        if not decoded:
            return None
        store.require(not Path(decoded).is_absolute(), 'absolute link')
        name = os.path.normpath(str(Path(source).parent / decoded))
        return safe_file(root, name).relative_to(root).as_posix()

    def children(directory):
        try:
            folder = safe_file(root, directory) if directory else root
            if not folder.exists():
                return []
            store.require(folder.is_dir(), 'not a directory')
            found = []
            for path in folder.iterdir():
                if coverage['metadata_entries'] >= MAX_ENTRIES:
                    coverage['complete'] = False
                    finding('scan_limit', directory or '.')
                    break
                coverage['metadata_entries'] += 1
                name = path.relative_to(root).as_posix()
                if path.is_symlink():
                    coverage['complete'] = False
                    finding('unsafe_path', name)
                    continue
                if path.name == '.write.lock':
                    finding('write_lock_present', name)
                elif path.name.startswith('.pending-'):
                    finding('interrupted_write_candidate', name)
                found.append(path)
            return found
        except (ValueError, OSError):
            coverage['complete'] = False
            finding('unsafe_path', directory or '.')
            return []

    referenced = {d['path'] for d in state['documents']}
    candidates = set(referenced)
    children('')
    children('progress')
    for path in children('documents'):
        name = path.relative_to(root).as_posix()
        if path.suffix == '.md' and name not in referenced:
            finding('unreferenced_document', name)
    indexed_groups = [('notes/index.md', 'notes/sessions', 'unindexed_note'),
                      ('conocimientos/index.md', 'conocimientos/fichas', 'unindexed_card')]
    current = set()
    for index, directory, orphan_code in indexed_groups:
        read(index)
        children(str(Path(index).parent))
        found = [p.relative_to(root).as_posix() for p in children(directory) if p.suffix == '.md']
        candidates.update(found)
        current.update(found)
        if found and index not in contents:
            finding('missing_or_unreadable_index', index)

    for name in sorted(candidates):
        read(name, required=name in referenced)

    links = {}
    for name, text in list(contents.items()):
        cleaned = re.sub(r'```.*?```', '', text, flags=re.S)
        targets = re.findall(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)', cleaned)
        # Existing table-style indexes may use code-formatted relative paths.
        if name.endswith('/index.md'):
            targets += re.findall(r'`([^`\n]+\.md(?:#[^`\n]*)?)`', cleaned)
        for target in targets:
            try:
                resolved = local_target(name, target)
                if resolved:
                    links.setdefault(name, set()).add(resolved)
                    if not safe_file(root, resolved).is_file():
                        finding('broken_link', name, target=resolved)
            except (ValueError, OSError):
                finding('unsafe_link', name)

    for index, directory, code in indexed_groups:
        if index in contents:
            for name in sorted(current):
                if name.startswith(directory + '/') and name not in links.get(index, set()):
                    finding(code, name)

    duplicates = {}
    for name in sorted(current & contents.keys()):
        normalized = ' '.join(contents[name].split())
        if normalized:
            key = hashlib.sha256(normalized.encode()).hexdigest()
            duplicates.setdefault(key, []).append(name)
    for paths in duplicates.values():
        if len(paths) > 1:
            finding('duplicate_content', paths[0], paths=paths)

    text = read('progress/index.html')
    if text is not None:
        match = re.search(r'<script id="progress-data" type="application/json">(.*?)</script>', text, re.S)
        try:
            model = json.loads(match.group(1)) if match else None
            if not isinstance(model, dict) or 'source_digest' not in model or 'source_revision' not in model:
                finding('unverifiable_progress', 'progress/index.html')
            elif model['source_digest'] != store.digest(state) or model['source_revision'] != state['revision']:
                finding('stale_progress', 'progress/index.html')
        except (ValueError, TypeError):
            finding('unverifiable_progress', 'progress/index.html')
    return dict(findings=findings, coverage=coverage,
                manual_review=['technical contradictions and applicable versions',
                               'learning claims versus exact evidence and assistance',
                               'prerequisite cycles and index metadata consistency',
                               'pending batches, history and inaccessible copies'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('action', choices=['status', 'audit'])
    args = parser.parse_args()
    try:
        result = inspect_root(args.root, args.action)
    except (ValueError, OSError, TypeError, KeyError, RuntimeError) as exc:
        print(store.canonical(dict(ok=False, error_code='invalid_or_unreadable_record', error=str(exc))))
        return 1
    print(store.canonical(result))
    return 0


if __name__ == '__main__':
    sys.exit(main())
