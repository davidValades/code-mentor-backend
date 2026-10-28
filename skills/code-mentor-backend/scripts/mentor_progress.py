"""Private, offline practice report. Reads evidence; never awards or records learning."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import argparse
import base64
import hashlib
from html import escape
import json
import sys

import mentor_store as store


TITLES = {'en': 'Learning progress', 'es': 'Progreso de aprendizaje'}
ASSETS = Path(__file__).resolve().parents[1] / 'assets' / 'progress'


def options(time_zone, language):
    store.require(language in TITLES, 'unsupported report language')
    try:
        return ZoneInfo(time_zone)
    except (ZoneInfoNotFoundError, ValueError, TypeError) as exc:
        raise ValueError('unknown IANA time zone') from exc


def practice(event):
    return event['activity'] != 'declared' and event['assistance'] != 'solution'


def evaluated(event):
    return practice(event) and event['outcome'] in ('correct', 'partial', 'incorrect')


def order(event):
    return store.timestamp(event['recorded_at']), event['id']


def milestones(events, zone):
    """Witnesses for the store's existing rules; these are historical observations."""
    guided = [e for e in events if e['activity'] != 'declared'
              and e['assistance'] in ('hint', 'guided') and e['outcome'] in ('correct', 'partial')]
    conceptual = [e for e in events if e['activity'] in ('explain', 'predict', 'retrieve')
                  and e['assistance'] == 'none' and e['outcome'] == 'correct']
    independent = [e for e in events if e['activity'] in ('implement', 'debug') and e['modality'] == 'ide'
                   and e['assistance'] == 'none' and e['outcome'] == 'correct']
    result = []

    def witness(kind, supporting):
        last = supporting[-1]
        result.append(dict(kind=kind, event_ids=[e['id'] for e in supporting],
                           recorded_at=last['recorded_at'],
                           day=store.timestamp(last['recorded_at']).astimezone(zone).date().isoformat()))

    for kind, candidates in [('guided', guided), ('conceptual', conceptual), ('autonomous', independent)]:
        if candidates:
            witness(kind, [candidates[0]])
    for later in conceptual:
        if later['activity'] != 'retrieve':
            continue
        earlier = next((e for e in independent if e['session_id'] != later['session_id']
                        and store.timestamp(later['recorded_at']) - store.timestamp(e['recorded_at'])
                        >= timedelta(days=1)), None)
        if earlier:
            witness('consolidated', [earlier, later])
            break
    return result


def build_model(state: dict, *, time_zone: str = 'UTC', language: str = 'en',
                generated_at: str | None = None, demo: bool = False) -> dict:
    zone = options(time_zone, language)
    store.require(type(demo) is bool, 'demo must be boolean')
    store.validate_state(state)
    generated_at = generated_at or datetime.now(timezone.utc).isoformat()
    today = store.timestamp(generated_at).astimezone(zone).date()
    try:
        previous_year = today.replace(year=today.year-1)
    except ValueError:
        previous_year = today.replace(year=today.year-1, day=28)
    closed = {s['id']: s['recorded_at'] for s in state['sessions']}
    projected = []
    for event in sorted(state['events'], key=order):
        selected = {key:event[key] for key in ('id', 'session_id', 'recorded_at', 'topic', 'activity',
                                              'modality', 'assistance', 'outcome', 'evidence_summary')}
        selected.update(day=store.timestamp(event['recorded_at']).astimezone(zone).date().isoformat(),
                        practice=practice(event), session_completed_at=closed.get(event['session_id']),
                        display_at=store.timestamp(event['recorded_at']).astimezone(timezone.utc).isoformat(timespec='milliseconds'),
                        session_completed_display_at=(store.timestamp(closed[event['session_id']]).astimezone(timezone.utc).isoformat(timespec='milliseconds')
                                                      if event['session_id'] in closed else None))
        projected.append(selected)
    concepts = []
    for topic in sorted({e['topic'] for e in projected}):
        events = [e for e in projected if e['topic'] == topic]
        latest = {}
        for event in events:
            if evaluated(event):
                latest[(event['activity'], event['modality'])] = event
        concepts.append(dict(topic=topic, status=store.learning_status(state, topic),
                             milestones=milestones(events, zone),
                             latest_checks=[latest[k] for k in sorted(latest)]))
    return dict(report_schema=1, source_revision=state['revision'], source_digest=store.digest(state),
                scope=state['scope'], generated_at=generated_at,
                display_generated_at=store.timestamp(generated_at).astimezone(timezone.utc).isoformat(timespec='milliseconds'),
                time_zone=time_zone, language=language,
                demo=demo, range={'start':(previous_year+timedelta(days=1)).isoformat(), 'end':today.isoformat()},
                events=projected, concepts=concepts,
                labels=json.loads((ASSETS/'strings.json').read_text(encoding='utf-8'))[language])


def markdown_text(value):
    value = escape(str(value).replace('\n', ' ').replace('\r', ' '), quote=False).replace('\\', '\\\\')
    for char in '|`[]*_':
        value = value.replace(char, '\\'+char)
    return value


def render(model: dict) -> tuple[str, str]:
    options(model['time_zone'], model['language'])
    labels = model['labels']
    css = (ASSETS/'report.css').read_text(encoding='utf-8')
    script = (ASSETS/'report.js').read_text(encoding='utf-8')
    html = (ASSETS/'report.html').read_text(encoding='utf-8')
    replacements = {
        'LANG': escape(model['language'], quote=True), 'TITLE': escape(labels['title']),
        'CSS_HASH': base64.b64encode(hashlib.sha256(css.encode()).digest()).decode(),
        'SCRIPT_HASH': base64.b64encode(hashlib.sha256(script.encode()).digest()).decode(),
        'CSS': css, 'SCRIPT': script,
    }
    for key, value in replacements.items():
        html = html.replace('@@'+key+'@@', value)
    encoded = store.canonical(model)
    for char in '<>&\u2028\u2029':
        encoded = encoded.replace(char, '\\u'+format(ord(char), '04x'))
    html = html.replace('@@MODEL@@', encoded)
    m = markdown_text
    lines = ['# '+labels['title'], '']
    if model['demo']:
        lines += ['**'+labels['demo']+'**', '']
    lines += [labels['scope'][model['scope']],
              f"{labels['generated']}: {model['generated_at']} · {labels['zone']}: {model['time_zone']}",
              f"{labels['revision']}: {model['source_revision']} · {labels['digest']}: `{model['source_digest']}`", '',
              labels['snapshot'], '', labels['datesNote'], '', '## '+labels['calendar'], '',
              model['range']['start']+' — '+model['range']['end'], '', labels['calendarNote'], '']
    attempts = [e for e in model['events'] if e['practice']
                and model['range']['start'] <= e['day'] <= model['range']['end']]
    days = {e['day'] for e in attempts}
    lines += [f"{labels['days']}: {len(days)} · {labels['attempts']}: {len(attempts)}", '']
    if not attempts:
        lines += [labels['noPractice'], '']
    else:
        lines += ['| '+ ' | '.join(labels[k] for k in ['date','topic','activity','assistance','outcome','evidence'])+' |',
                  '| --- | --- | --- | --- | --- | --- |']
        for event in attempts[-10:]:
            lines.append('| '+' | '.join(m(x) for x in [event['day'],event['topic'],
                         labels['activities'][event['activity']], labels['helps'][event['assistance']],
                         labels['outcomes'][event['outcome']],event['id']])+' |')
        lines += ['', 'HTML: `index.html` · '+labels['table'], '']
    lines += ['## '+labels['history'], '', labels['historyNote'], '', labels['statusNote'], '']
    for concept in model['concepts']:
        lines += ['### '+m(concept['topic']), '', labels['status']+': '+labels['statuses'][concept['status']], '']
        for milestone in concept['milestones']:
            lines.append('- '+labels['statuses'][milestone['kind']]+' · '+milestone['day']+' · '
                         +labels['evidence']+': '+', '.join(m(x) for x in milestone['event_ids']))
        if not concept['milestones']:
            lines.append(labels['noMilestones'])
        lines += ['', labels['latest']+':']
        for event in concept['latest_checks']:
            lines.append('- '+ ' · '.join(m(x) for x in [labels['activities'][event['activity']],
                         labels['modes'][event['modality']], labels['outcomes'][event['outcome']],
                         labels['helps'][event['assistance']],event['day'],event['id']]))
        if not concept['latest_checks']:
            lines.append(labels['noChecks'])
        lines.append('')
    if not model['concepts']:
        lines += [labels['noConcepts'], '']
    return html, '\n'.join(lines)+'\n'


def report(root: Path, *, time_zone='UTC', language='en', demo=False) -> dict:
    options(time_zone, language)
    root = store.safe_root(root)
    with store.writer_lock(root):
        state = store.read_state(root)
        model = build_model(state, time_zone=time_zone, language=language, demo=demo)
        html, markdown = render(model)
        directory = store.safe_file(root, 'progress')
        targets = {store.safe_file(root, 'progress/index.html'):html,
                   store.safe_file(root, 'progress/summary.md'):markdown}
        previous = {p:p.read_text(encoding='utf-8') if p.exists() else None for p in targets}
        directory.mkdir(exist_ok=True, mode=0o700)
        attempted = []
        try:
            for path, content in targets.items():
                store.safe_file(root, path.relative_to(root).as_posix())
                attempted.append(path)
                store.atomic_write(path, content)
            for path, content in targets.items():
                store.require(path.read_text(encoding='utf-8') == content, 'report readback failed')
            store.require(store.digest(store.read_state(root)) == model['source_digest'],
                          'STALE: source changed during report generation; regenerate')
        except (OSError, ValueError) as exc:
            errors = []
            for path in reversed(attempted):
                try:
                    store.safe_file(root, path.relative_to(root).as_posix())
                    if previous[path] is None:
                        path.unlink(missing_ok=True)
                    else:
                        store.atomic_write(path, previous[path])
                except (OSError, ValueError) as rollback:
                    errors.append(str(rollback))
            if errors:
                raise OSError('incomplete report update; restoration failed: '+'; '.join(errors)) from exc
            raise
        return dict(html=str(root/'progress/index.html'), markdown=str(root/'progress/summary.md'),
                    source_revision=model['source_revision'], source_digest=model['source_digest'],
                    generated_at=model['generated_at'], time_zone=time_zone, language=language)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('action', choices=['report'])
    parser.add_argument('--timezone', default='UTC', help='IANA zone; UTC is an explicit fallback')
    parser.add_argument('--language', choices=['en','es'], default='en')
    parser.add_argument('--demo', action='store_true', help='Label synthetic QA; never real learner progress')
    args = parser.parse_args()
    try:
        print(store.canonical(report(args.root, time_zone=args.timezone, language=args.language, demo=args.demo)))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
