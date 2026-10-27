"""Evidence-linked teaching observations and derived reports. No network or background work."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from html import escape
import json
from pathlib import Path
import re
import sys

import mentor_store as store

STRATEGIES = {'diagram', 'analogy', 'trace', 'worked-example', 'comparison',
              'self-explanation', 'retrieval', 'guided-debugging'}
INPUT_FIELDS = {'id', 'evidence_id', 'concept_id', 'task_kind', 'difficulty',
                'check_kind', 'strategies', 'learned_evidence_id'}
ROW_FIELDS = INPUT_FIELDS | {'schema_version', 'recorded_at'}
LABELS = {'diagram':'Esquema', 'analogy':'Analogía', 'trace':'trazado',
          'worked-example':'Ejemplo resuelto', 'comparison':'Comparación',
          'self-explanation':'Explicación propia', 'retrieval':'Recuperación',
          'guided-debugging':'Depuración guiada', 'read':'lectura', 'explain':'explicación',
          'implement':'implementación', 'debug':'depuración', 'predict':'predicción',
          'retrieve':'recuperación', 'declared':'declaración', 'introductory':'inicial',
          'standard':'media', 'complex':'compleja', 'text':'texto', 'oral':'voz', 'ide':'IDE',
          'none':'sin ayuda', 'hint':'pista', 'guided':'guía', 'solution':'solución',
          'immediate':'inmediata', 'transfer':'transferencia', 'delayed':'diferida',
          'operators':'Operadores', 'types':'Tipos', 'methods':'Métodos', 'classes':'Clases',
          'flow':'Flujo', 'results':'Resultados', 'async':'Asincronía',
          'dependencies':'Dependencias', 'http':'HTTP', 'data':'Datos', 'testing':'Pruebas',
          'debugging':'Depuración', 'refactoring':'Refactorización', 'architecture':'Arquitectura',
          'vocabulary':'Vocabulario'}


def identifier(value):
    store.require(isinstance(value, str) and re.fullmatch(r'[a-z0-9][a-z0-9.-]{0,127}', value),
                  'safe identifier required')


def validate_input(data):
    store.require(isinstance(data, dict) and set(data) == INPUT_FIELDS, 'invalid observation fields')
    for key in ('id', 'concept_id'):
        identifier(data[key])
    store.text_field(data['evidence_id'])
    store.require(data['task_kind'] in {'read', 'trace', 'explain', 'implement', 'debug'}, 'invalid task kind')
    store.require(data['difficulty'] in {'introductory', 'standard', 'complex'}, 'invalid difficulty')
    store.require(data['check_kind'] in {'immediate', 'transfer', 'delayed'}, 'invalid check kind')
    strategies = data['strategies']
    store.require(isinstance(strategies, list) and strategies and all(isinstance(x, str) for x in strategies),
                  'strategies required')
    store.require(len(strategies) == len(set(strategies)) and set(strategies) <= STRATEGIES,
                  'invalid or duplicate strategies')
    if data['learned_evidence_id'] is not None:
        store.text_field(data['learned_evidence_id'])
    store.require(data['check_kind'] == 'immediate' or data['learned_evidence_id'] is not None,
                  'prior learning evidence required')


def contextualize(data, events):
    store.require(data['evidence_id'] in events, 'unknown evidence')
    event = events[data['evidence_id']]
    delay = None
    if data['learned_evidence_id'] is not None:
        prior = events.get(data['learned_evidence_id'])
        store.require(prior is not None, 'unknown learning evidence')
        elapsed = store.timestamp(event['recorded_at']) - store.timestamp(prior['recorded_at'])
        store.require(prior['id'] != event['id'] and elapsed.total_seconds() >= 0
                      and prior['topic'] == event['topic'], 'incompatible learning evidence')
        delay = elapsed.total_seconds()/86400
        if data['check_kind'] == 'delayed':
            store.require(delay >= 1 and prior['session_id'] != event['session_id'],
                          'delayed check requires another session and at least one day')
    return event, delay


def rows_at(root):
    path = store.safe_file(root, 'adaptacion/observaciones.jsonl')
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding='utf-8').splitlines():
        row = json.loads(line)
        store.require(isinstance(row, dict) and set(row) == ROW_FIELDS and row['schema_version'] == 1,
                      'unsupported observation schema')
        store.timestamp(row['recorded_at'])
        validate_input({k: row[k] for k in INPUT_FIELDS})
        rows.append(row)
    store.require(len({r['id'] for r in rows}) == len(rows), 'duplicate observation id')
    store.require(len({r['evidence_id'] for r in rows}) == len(rows), 'duplicate evidence observations')
    return rows


def record(root, data):
    root = store.safe_root(root)
    validate_input(data)
    data = dict(data, strategies=sorted(data['strategies']))
    with store.writer_lock(root):
        state = store.read_state(root)
        contextualize(data, {e['id']: e for e in state['events']})
        rows = rows_at(root)
        for old in rows:
            if old['id'] == data['id']:
                store.require(all(old[k] == data[k] for k in INPUT_FIELDS), 'observation id reused')
                return {'id': data['id'], 'replayed': True}
        store.require(not any(r['evidence_id'] == data['evidence_id'] for r in rows),
                      'evidence already has an observation')
        row = dict(data, schema_version=1, recorded_at=datetime.now(timezone.utc).isoformat())
        directory = store.safe_file(root, 'adaptacion')
        directory.mkdir(exist_ok=True, mode=0o700)
        path = store.safe_file(root, 'adaptacion/observaciones.jsonl')
        # Rewrite under the same lock as the primary store; no partial appended JSON line.
        store.atomic_write(path, ''.join(store.canonical(r)+'\n' for r in rows+[row]))
        return {'id': data['id'], 'replayed': False}


def summarize(root):
    root = store.safe_root(root)
    with store.writer_lock(root):
        return summarize_locked(root)


def summarize_locked(root):
    state = store.read_state(root)
    events = {e['id']: e for e in state['events']}
    buckets = {}
    orphaned, invalid = [], []
    rows = rows_at(root)
    for row in rows:
        refs = [row['evidence_id'], row['learned_evidence_id']]
        if any(x is not None and x not in events for x in refs):
            orphaned.append(row['id'])
            continue
        try:
            event, delay = contextualize(row, events)
        except ValueError:
            invalid.append(row['id'])
            continue
        learning_mode = events[row['learned_evidence_id']]['modality'] if row['learned_evidence_id'] else event['modality']
        key = (row['concept_id'], event['topic'], row['task_kind'], row['difficulty'],
               event['modality'], event['activity'], event['assistance'], row['check_kind'],
               tuple(sorted(row['strategies'])), learning_mode)
        if key not in buckets:
            buckets[key] = dict(concept_id=key[0], topic=key[1], task_kind=key[2], difficulty=key[3],
                                modality=key[4], activity=key[5], assistance=key[6], check_kind=key[7],
                                strategies=list(key[8]), learning_modality=key[9], correct=0, partial=0, incorrect=0, pending=0,
                                attempts=0, evaluated_sessions=[], observation_ids=[], evidence_ids=[], sessions=[],
                                dates=[], delays_days=[])
        group = buckets[key]
        group['observation_ids'].append(row['id'])
        group['evidence_ids'].append(event['id'])
        group['sessions'].append(event['session_id'])
        group['dates'].append(event['recorded_at'])
        if delay is not None:
            group['delays_days'].append(round(delay, 3))
        if event['activity'] == 'declared' or event['outcome'] == 'unverified' or event['assistance'] == 'solution':
            group['pending'] += 1
        else:
            group['evaluated_sessions'].append(event['session_id'])
            group['attempts'] += 1
            group[event['outcome']] += 1
    groups = []
    for key in sorted(buckets):
        group = buckets[key]
        group['sessions'] = sorted(set(group['sessions']))
        group['evaluated_sessions'] = sorted(set(group['evaluated_sessions']))
        group['insufficient'] = group['attempts'] < 3 or len(group['evaluated_sessions']) < 2
        groups.append(group)
    return dict(source_revision=state['revision'], observation_digest=store.digest(rows), scope=state['scope'], groups=groups,
                orphaned_ids=orphaned, invalid_ids=invalid)


def render(result, generated_at):
    lines = ['# Resultados por contexto y estrategia', '',
             f'Generado: {generated_at}; revisión del registro: {result["source_revision"]}.',
             f'Huella de observaciones: {result["observation_digest"]}.', '',
             'Asociaciones observadas, no causalidad ni estilo fijo. Sin ranking global.',
             'Umbral orientativo: 3 intentos y 2 sesiones evaluadas; superarlo no demuestra eficacia.',
             'Aciertos se distinguen por ayuda. Pendientes, declaraciones y soluciones no cuentan como intentos evaluados.', '']
    height = max(220, 150+len(result['groups'])*150)
    width = 1200
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
           f'<rect width="{width}" height="{height}" fill="white"/>',
           '<g fill="#172554" font-family="sans-serif" font-size="16">',
           '<text x="20" y="30">Resultados observados por contexto; no causalidad ni estilo fijo</text>',
           f'<text x="20" y="58">Revisión {result["source_revision"]}; generado {escape(generated_at)}</text>']
    if not result['groups']:
        lines.append('Sin observaciones válidas: no hay datos para comparar.')
        svg.append('<text x="20" y="110">Sin observaciones válidas. No hay datos para comparar.</text>')
    for n, g in enumerate(result['groups'], 1):
        label = ' / '.join([LABELS.get(g[k], g[k]) for k in ['topic', 'task_kind', 'difficulty']]+
                            [LABELS[g['learning_modality']]+' → '+LABELS[g['modality']]]+
                            [LABELS[g[k]] for k in ['activity', 'assistance', 'check_kind']])
        strategy = ' + '.join(LABELS[x] for x in g['strategies'])
        status = 'Evidencia insuficiente' if g['insufficient'] else 'Observaciones provisionales'
        lines.extend([f'## Grupo {n}: {g["concept_id"]} / {label}', '', f'Estrategias: {strategy}. {status}.',
                      f'Aciertos/intentos: {g["correct"]}/{g["attempts"]}; parciales: {g["partial"]}; '
                      f'incorrectos: {g["incorrect"]}; pendientes: {g["pending"]}.',
                      'Observaciones: '+', '.join(g['observation_ids'])+'.',
                      'Evidencias: '+', '.join(g['evidence_ids'])+'.',
                      'Fechas: '+', '.join(g['dates'])+'.',
                      'Demora observada en días: '+(', '.join(map(str,g['delays_days'])) or 'no comprobada')+'.', ''])
        y = 95+(n-1)*150
        svg.extend([f'<text x="20" y="{y}">{escape(g["concept_id"])}</text>',
                    f'<text x="20" y="{y+24}">{escape(label)}</text>',
                    f'<text x="20" y="{y+48}">{escape(strategy)}; {status}</text>',
                    f'<rect x="20" y="{y+62}" width="400" height="18" fill="#e2e8f0"/>'])
        width = 400*g['correct']/g['attempts'] if g['attempts'] else 0
        svg.extend([f'<rect x="20" y="{y+62}" width="{width:.1f}" height="18" fill="#7c3aed"/>',
                    f'<text x="435" y="{y+78}">{g["correct"]}/{g["attempts"]} aciertos; '
                    f'{g["pending"]} pendientes; {len(g["evaluated_sessions"])} sesiones evaluadas</text>'])
    lines.extend(['Referencias huérfanas excluidas: '+(', '.join(result['orphaned_ids']) or 'ninguna')+'.',
                  'Referencias incompatibles excluidas: '+(', '.join(result['invalid_ids']) or 'ninguna')+'.'])
    svg.extend(['</g>', '</svg>'])
    return '\n'.join(lines)+'\n', '\n'.join(svg)+'\n'


def report(root):
    root = store.safe_root(root)
    with store.writer_lock(root):
        result = summarize_locked(root)
        generated_at = datetime.now(timezone.utc).isoformat()
        md, svg = render(result, generated_at)
        for folder in ['adaptacion', 'adaptacion/graficos']:
            store.safe_file(root, folder).mkdir(exist_ok=True, mode=0o700)
        markdown = store.safe_file(root, 'adaptacion/balance.md')
        image = store.safe_file(root, 'adaptacion/graficos/resultados.svg')
        store.atomic_write(markdown, md)
        store.atomic_write(image, svg)
        return dict(markdown=str(markdown), svg=str(image), source_revision=result['source_revision'],
                    generated_at=generated_at, observation_digest=result['observation_digest'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('action', choices=['record', 'read', 'report'])
    args = parser.parse_args()
    try:
        if args.action == 'record':
            result = record(args.root, json.load(sys.stdin))
        elif args.action == 'read':
            result = summarize(args.root)
        else:
            result = report(args.root)
        print(store.canonical(result))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
