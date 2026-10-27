"""Local evidence store for Code Mentor Backend. No network or background work."""
from __future__ import annotations

from datetime import datetime, timedelta
import json
from pathlib import Path, PurePosixPath, PureWindowsPath


def require(condition, message):
    if not condition:
        raise ValueError(message)


def timestamp(value):
    require(isinstance(value, str), 'timestamp must be text')
    try:
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as exc:
        raise ValueError('invalid timestamp') from exc
    require(parsed.tzinfo is not None, 'timestamp requires timezone')
    return parsed


def text_field(value):
    require(isinstance(value, str) and bool(value.strip()), 'nonempty text required')


def relative_path(value):
    text_field(value)
    p = PurePosixPath(value.replace('\\', '/'))
    require(not p.is_absolute() and not PureWindowsPath(value).drive and '..' not in p.parts
            and ':' not in value and '\x00' not in value, 'relative source path required')


def new_state(scope):
    require(scope in ('general', 'project'), 'invalid scope')
    return dict(schema_version=2, revision=0, scope=scope, events=[], sessions=[], reviews=[],
                checkpoint=None, cases=[], attempts=[], observations=[], improvements=[], documents=[], receipts={})


def unique_ids(items):
    require(isinstance(items, list), 'list required')
    ids = []
    for item in items:
        require(isinstance(item, dict), 'record must be object')
        text_field(item.get('id'))
        ids.append(item['id'])
    require(len(ids) == len(set(ids)), 'duplicate record id')


def validate_event(e, scope):
    fields = {'id', 'session_id', 'recorded_at', 'topic', 'activity', 'modality', 'assistance',
              'outcome', 'evidence_summary', 'review_due'}
    if scope == 'project':
        fields |= {'task_id', 'source_refs'}
    require(set(e) == fields, 'invalid event fields for scope')
    for key in ('id', 'session_id', 'topic', 'evidence_summary'):
        text_field(e[key])
    timestamp(e['recorded_at'])
    require(e['activity'] in ('declared', 'explain', 'predict', 'implement', 'debug', 'retrieve'), 'invalid activity')
    require(e['modality'] in ('oral', 'text', 'ide'), 'invalid modality')
    require(e['assistance'] in ('none', 'hint', 'guided', 'solution'), 'invalid assistance')
    require(e['outcome'] in ('correct', 'partial', 'incorrect', 'unverified'), 'invalid outcome')
    if e['review_due'] is not None:
        timestamp(e['review_due'])
    if scope == 'project':
        text_field(e['task_id'])
        require(isinstance(e['source_refs'], list), 'source refs required')
        for ref in e['source_refs']:
            require(set(ref) == {'path', 'commit', 'branch', 'dirty', 'observed_at'}, 'invalid source reference')
            relative_path(ref['path'])
            require(type(ref['dirty']) is bool, 'dirty flag required')
            require(ref['commit'] is None or (isinstance(ref['commit'], str) and len(ref['commit']) in (40, 64)
                    and all(c in '0123456789abcdef' for c in ref['commit'])), 'invalid commit')
            text_field(ref['branch'])
            timestamp(ref['observed_at'])


def validate_state(state):
    require(isinstance(state, dict), 'state must be object')
    require(set(state) == set(new_state('general')), 'invalid state fields')
    require(state['schema_version'] == 2, 'unsupported schema')
    require(type(state['revision']) is int and state['revision'] >= 0, 'invalid revision')
    require(state['scope'] in ('general', 'project'), 'invalid scope')
    for key in ('events', 'sessions', 'reviews', 'cases', 'attempts', 'observations', 'improvements', 'documents'):
        unique_ids(state[key])
    for e in state['events']:
        validate_event(e, state['scope'])
    require(state['checkpoint'] is None or isinstance(state['checkpoint'], dict), 'invalid checkpoint')
    require(isinstance(state['receipts'], dict), 'invalid receipts')
    validate_nested(state)

import argparse
from contextlib import contextmanager
import copy
import hashlib
import os
import sys
import tempfile


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def safe_root(root):
    root = Path(root)
    require(root.is_absolute(), 'absolute root required')
    require(root.resolve() == root, 'root must not contain symlinks or traversal')
    skill = Path(__file__).resolve().parents[1]
    require(root != skill and skill not in root.parents, 'data must be outside the skill')
    return root


def safe_file(root, name):
    relative_path(name)
    p = root / name
    require(p.resolve() == p and root in p.parents, 'unsafe or symlink path')
    return p


@contextmanager
def writer_lock(root):
    lock = safe_file(root, '.write.lock')
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise ValueError('LOCKED: another writer or interrupted operation; investigate before removal') from exc
    try:
        with os.fdopen(fd, 'w') as stream:
            stream.write(str(os.getpid()))
        yield
    finally:
        lock.unlink()


def atomic_write(path, content):
    fd, temp = tempfile.mkstemp(prefix='.pending-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def init_store(root, scope):
    root = safe_root(root)
    state = new_state(scope)
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    with writer_lock(root):
        p = safe_file(root, 'state.json')
        require(not p.exists(), 'store already exists; read instead')
        atomic_write(p, canonical(state) + '\n')
    return state


def read_state(root):
    root = safe_root(root)
    p = safe_file(root, 'state.json')
    state = json.loads(p.read_text(encoding='utf-8'))
    validate_state(state)
    return state


def fields(p, required):
    require(isinstance(p, dict) and set(p) == set(required.split()), 'invalid payload fields: expected ' + required)


def checkpoint_payload(p):
    fields(p, 'session_id topic evidence_id pending_question next_step recorded_at')
    for k in ('session_id', 'topic', 'pending_question', 'next_step'):
        text_field(p[k])
    require(p['evidence_id'] is None or isinstance(p['evidence_id'], str), 'invalid evidence id')
    timestamp(p['recorded_at'])


def reduce_command(state, op, p, request_id):
    if op == 'record_evidence':
        validate_event(p, state['scope'])
        require(not any(e['id'] == p['id'] for e in state['events']), 'evidence already exists')
        state['events'].append(p)
        return p['id']
    if op == 'save_checkpoint':
        checkpoint_payload(p)
        require(p['evidence_id'] is None or any(e['id'] == p['evidence_id'] for e in state['events']), 'unknown evidence')
        state['checkpoint'] = p
        return p['session_id']
    if op == 'complete_session':
        fields(p, 'id recorded_at')
        text_field(p['id']); timestamp(p['recorded_at'])
        if not any(s['id'] == p['id'] for s in state['sessions']):
            state['sessions'].append(p)
        return p['id']
    if op == 'record_review':
        fields(p, 'id recorded_at reason result')
        for key in ('id', 'reason', 'result'):
            text_field(p[key])
        timestamp(p['recorded_at'])
        state['reviews'].append(dict(p, session_ids=[x['id'] for x in state['sessions']],
                                     event_ids=[x['id'] for x in state['events']]))
        return p['id']
    if op == 'save_case':
        validate_case(p)
        state['cases'].append(p)
        return p['id']
    if op == 'record_case_attempt':
        fields(p, 'id case_id session_id response assistance outcome recorded_at')
        require(any(c['id'] == p['case_id'] for c in state['cases']), 'unknown case')
        for key in ('id', 'session_id', 'response'):
            text_field(p[key])
        require(p['assistance'] in ('none', 'hint', 'guided', 'solution'), 'invalid assistance')
        require(p['outcome'] in ('correct', 'partial', 'incorrect', 'unverified'), 'invalid outcome')
        timestamp(p['recorded_at'])
        state['attempts'].append(p)
        return p['id']
    if op == 'propose_improvement':
        fields(p, 'id reason evidence_ids baseline candidate')
        for k in ('id', 'reason', 'baseline'):
            text_field(p[k])
        require(isinstance(p['evidence_ids'], list) and bool(p['evidence_ids']), 'evidence required')
        require(set(p['evidence_ids']) <= {e['id'] for e in state['events']}, 'unknown evidence')
        validate_strategy(p['candidate'])
        state['improvements'].append(dict(p, status='proposed', evaluations=[], trial=None, decisions=[]))
        return p['id']
    if op == 'record_evaluation':
        fields(p, 'id improvement_id kind results cases checks')
        text_field(p['id']); text_field(p['results'])
        proposal = find_improvement(state, p['improvement_id'])
        require(proposal['status'] in ('proposed', 'evaluated'), 'evaluation not allowed in this state')
        require(p['kind'] in ('deterministic', 'model', 'manual'), 'invalid evaluation provenance')
        require(isinstance(p['cases'], list), 'cases required')
        unique_ids(p['cases'])
        for case in p['cases']:
            fields(case, 'id split baseline_response candidate_response')
            require(case['split'] in ('design', 'heldout'), 'invalid split')
            text_field(case['baseline_response']); text_field(case['candidate_response'])
        require({c['split'] for c in p['cases']} == {'design', 'heldout'}, 'design and heldout cases required')
        require(isinstance(p['checks'], dict) and len(p['checks']) >= 3
                and {'accuracy', 'permissions'} <= set(p['checks'])
                and all(type(v) is bool for v in p['checks'].values()), 'three checks including accuracy and permissions required')
        require(not any(e['id'] == p['id'] for e in proposal['evaluations']), 'duplicate evaluation')
        proposal['evaluations'].append(p)
        proposal['status'] = 'evaluated'
        return p['id']
    if op == 'set_trial':
        fields(p, 'id action user_confirmed summary')
        require(p['user_confirmed'] is True, 'explicit trial choice required')
        text_field(p['summary'])
        proposal = find_improvement(state, p['id'])
        if p['action'] in ('start', 'decline'):
            require(proposal['status'] == 'evaluated', 'evaluate before offering trial')
            require(evaluation_passed(proposal), 'failed evaluation blocks trial')
            require(proposal['trial'] is None, 'trial choice already recorded')
            proposal['trial'] = dict(status='active' if p['action'] == 'start' else 'declined', summary=p['summary'])
            if p['action'] == 'start':
                proposal['status'] = 'trial'
        elif p['action'] == 'complete':
            require(proposal['status'] == 'trial', 'no trial active')
            proposal['trial']['status'] = 'completed'
            proposal['trial']['result'] = p['summary']
            proposal['status'] = 'evaluated'
        else:
            raise ValueError('invalid trial action')
        return p['id']
    if op == 'decide_improvement':
        fields(p, 'id decision user_confirmed reason')
        require(p['user_confirmed'] is True, 'explicit user decision required')
        text_field(p['reason'])
        proposal = find_improvement(state, p['id'])
        if p['decision'] == 'accept':
            require(proposal['status'] == 'evaluated' and evaluation_passed(proposal), 'successful evaluation required')
            require(proposal['trial'] is not None and proposal['trial']['status'] in ('completed', 'declined'), 'trial must finish or be explicitly declined')
            proposal['status'] = 'accepted'
        elif p['decision'] == 'reject':
            require(proposal['status'] in ('proposed', 'evaluated', 'trial'), 'cannot reject this state')
            proposal['status'] = 'rejected'
        elif p['decision'] == 'revert':
            require(proposal['status'] == 'accepted', 'only accepted strategy can be reverted')
            proposal['status'] = 'reverted'
        else:
            raise ValueError('invalid decision')
        proposal['decisions'].append(p)
        return p['id']
    if op == 'record_observation':
        require(state['scope'] == 'project', 'observations belong to project scope')
        fields(p, 'id task_id statement source recorded_at')
        for key in ('id', 'task_id', 'statement', 'source'):
            text_field(p[key])
        timestamp(p['recorded_at'])
        require(not any(o['id'] == p['id'] for o in state['observations']), 'observation already exists')
        state['observations'].append(dict(p, confirmed=False, confirmation=None))
        return p['id']
    if op == 'confirm_convention':
        require(state['scope'] == 'project', 'conventions belong to project scope')
        fields(p, 'id user_confirmed scope reason')
        require(p['user_confirmed'] is True, 'explicit user confirmation required')
        text_field(p['scope']); text_field(p['reason'])
        matches = [o for o in state['observations'] if o['id'] == p['id']]
        require(len(matches) == 1, 'unknown observation')
        require(not matches[0]['confirmed'], 'already confirmed; record a new observation to revise')
        matches[0]['confirmed'] = True
        matches[0]['confirmation'] = dict(scope=p['scope'], reason=p['reason'])
        return p['id']
    raise ValueError('unknown operation')


def apply_command(root, command):
    root = safe_root(root)
    fields(command, 'request_id expected_revision operation payload')
    text_field(command['request_id'])
    require(type(command['expected_revision']) is int and command['expected_revision'] >= 0, 'invalid expected revision')
    fingerprint = digest(command)
    with writer_lock(root):
        state = read_state(root)
        receipt = state['receipts'].get(command['request_id'])
        if receipt:
            require(receipt['fingerprint'] == fingerprint, 'request id reused with different content')
            return dict(receipt['result'], replayed=True)
        require(state['revision'] == command['expected_revision'], 'CONFLICT: reload state and reconcile')
        p = copy.deepcopy(command['payload'])
        if command['operation'] == 'save_document':
            fields(p, 'id kind title content recorded_at')
            for k in ('id', 'title', 'content'):
                text_field(p[k])
            timestamp(p['recorded_at'])
            allowed = ('profile',) if state['scope'] == 'general' else ('project', 'task', 'checkpoint', 'improvement')
            require(p['kind'] in allowed, 'document kind not allowed in scope')
            name = digest(dict(request_id=command['request_id'], payload=p))
            directory = safe_file(root, 'documents')
            directory.mkdir(exist_ok=True, mode=0o700)
            path = safe_file(root, 'documents/' + name + '.md')
            require(not path.exists() or path.read_text(encoding='utf-8') == p['content'], 'document collision')
            if not path.exists():
                atomic_write(path, p['content'])
            state['documents'].append(dict(id=name, document_id=p['id'], kind=p['kind'], title=p['title'],
                                           path='documents/' + name + '.md', recorded_at=p['recorded_at']))
            record_id = name
        else:
            record_id = reduce_command(state, command['operation'], p, command['request_id'])
        state['revision'] += 1
        result = dict(revision=state['revision'], record_id=record_id, replayed=False)
        state['receipts'][command['request_id']] = dict(fingerprint=fingerprint, result=result)
        validate_state(state)
        atomic_write(safe_file(root, 'state.json'), canonical(state) + '\n')
        return result


def validate_strategy(candidate):
    require(isinstance(candidate, dict) and bool(candidate)
            and set(candidate) <= {'explanation_words', 'example_lines', 'analogies', 'diagrams'}, 'invalid strategy fields')
    for key, value in candidate.items():
        if key == 'explanation_words':
            require(type(value) is int and 40 <= value <= 250, 'explanation words out of range')
        elif key == 'example_lines':
            require(type(value) is int and 1 <= value <= 20, 'example lines out of range')
        elif key == 'analogies':
            require(type(value) is bool, 'analogies must be boolean')
        else:
            require(value in ('when_interaction', 'on_request', 'frequent'), 'invalid diagrams strategy')


def find_improvement(state, record_id):
    matches = [p for p in state['improvements'] if p['id'] == record_id]
    require(len(matches) == 1, 'unknown improvement')
    return matches[0]


def evaluation_passed(proposal):
    return bool(proposal['evaluations']) and all(proposal['evaluations'][-1]['checks'].values())


def active_strategy(state):
    validate_state(state)
    result = {}
    for p in state['improvements']:
        if p['status'] == 'accepted':
            result.update(p['candidate'])
    return result or None



def validate_nested(state):
    events = {e['id'] for e in state['events']}
    session_ids = {x['id'] for x in state['sessions']}
    case_ids = {x['id'] for x in state['cases']}
    if state['checkpoint'] is not None:
        checkpoint_payload(state['checkpoint'])
        require(state['checkpoint']['evidence_id'] is None or state['checkpoint']['evidence_id'] in events, 'checkpoint evidence missing')
    for item in state['sessions']:
        fields(item, 'id recorded_at'); timestamp(item['recorded_at'])
    for item in state['reviews']:
        fields(item, 'id recorded_at reason result session_ids event_ids')
        timestamp(item['recorded_at']); text_field(item['reason']); text_field(item['result'])
        for key, allowed in (('session_ids', session_ids), ('event_ids', events)):
            require(isinstance(item[key], list) and all(isinstance(x, str) for x in item[key]) and len(item[key]) == len(set(item[key])) and set(item[key]) <= allowed, 'invalid review references')
    for item in state['cases']:
        validate_case(item)
    for item in state['attempts']:
        fields(item, 'id case_id session_id response assistance outcome recorded_at')
        require(item['case_id'] in case_ids, 'attempt references missing case')
        text_field(item['session_id']); text_field(item['response']); timestamp(item['recorded_at'])
        require(item['assistance'] in ('none', 'hint', 'guided', 'solution') and item['outcome'] in ('correct', 'partial', 'incorrect', 'unverified'), 'invalid attempt')
    require(state['scope'] == 'project' or not state['observations'], 'observations require project scope')
    for item in state['observations']:
        fields(item, 'id task_id statement source recorded_at confirmed confirmation')
        for key in ('task_id', 'statement', 'source'): text_field(item[key])
        timestamp(item['recorded_at']); require(type(item['confirmed']) is bool, 'invalid confirmation')
        if item['confirmed']:
            fields(item['confirmation'], 'scope reason'); text_field(item['confirmation']['scope']); text_field(item['confirmation']['reason'])
        else:
            require(item['confirmation'] is None, 'unconfirmed observation has confirmation')
    for doc in state['documents']:
        fields(doc, 'id document_id kind title path recorded_at')
        text_field(doc['document_id']); text_field(doc['title']); timestamp(doc['recorded_at'])
        relative_path(doc['path'])
        require(doc['path'] == 'documents/' + doc['id'] + '.md', 'invalid document path')
        allowed = ('profile',) if state['scope'] == 'general' else ('project', 'task', 'checkpoint', 'improvement')
        require(doc['kind'] in allowed, 'invalid document scope')
    for proposal in state['improvements']:
        fields(proposal, 'id reason evidence_ids baseline candidate status evaluations trial decisions')
        text_field(proposal['reason']); text_field(proposal['baseline']); validate_strategy(proposal['candidate'])
        require(isinstance(proposal['evidence_ids'], list) and bool(proposal['evidence_ids']) and all(isinstance(i, str) for i in proposal['evidence_ids']) and set(proposal['evidence_ids']) <= events, 'invalid improvement evidence')
        require(proposal['status'] in ('proposed', 'evaluated', 'trial', 'accepted', 'rejected', 'reverted'), 'invalid proposal status')
        unique_ids(proposal['evaluations'])
        for ev in proposal['evaluations']:
            fields(ev, 'id improvement_id kind results cases checks')
            require(ev['improvement_id'] == proposal['id'] and ev['kind'] in ('manual', 'model', 'deterministic'), 'invalid evaluation')
            text_field(ev['results']); unique_ids(ev['cases'])
            for case in ev['cases']:
                fields(case, 'id split baseline_response candidate_response')
                require(case['split'] in ('design', 'heldout'), 'invalid split'); text_field(case['baseline_response']); text_field(case['candidate_response'])
            require({c['split'] for c in ev['cases']} == {'design', 'heldout'}, 'missing evaluation split')
            require(isinstance(ev['checks'], dict) and len(ev['checks']) >= 3 and {'accuracy', 'permissions'} <= set(ev['checks']) and all(type(v) is bool for v in ev['checks'].values()), 'invalid evaluation checks')
        if proposal['trial'] is not None:
            trial = proposal['trial']
            require(isinstance(trial, dict) and trial.get('status') in ('active', 'completed', 'declined'), 'invalid trial')
            fields(trial, 'status summary result' if trial['status'] == 'completed' else 'status summary')
            text_field(trial['summary'])
            if trial['status'] == 'completed': text_field(trial['result'])
        require(isinstance(proposal['decisions'], list), 'invalid decisions')
        for decision in proposal['decisions']:
            fields(decision, 'id decision user_confirmed reason')
            require(decision['id'] == proposal['id'] and decision['decision'] in ('accept', 'reject', 'revert') and decision['user_confirmed'] is True, 'invalid decision')
            text_field(decision['reason'])
        if proposal['status'] in ('evaluated', 'trial', 'accepted', 'reverted'):
            require(bool(proposal['evaluations']), 'evaluated status requires evaluation')
        if proposal['status'] == 'trial':
            require(proposal['trial'] is not None and proposal['trial']['status'] == 'active', 'trial state mismatch')
        if proposal['status'] in ('accepted', 'reverted'):
            require(any(d['decision'] == 'accept' for d in proposal['decisions']) and evaluation_passed(proposal), 'acceptance requires evaluated decision')
            require(proposal['trial'] is not None and proposal['trial']['status'] in ('completed', 'declined'), 'trial decision missing')
        if proposal['status'] == 'reverted':
            require(any(d['decision'] == 'revert' for d in proposal['decisions']), 'revert decision missing')
        if proposal['status'] == 'rejected':
            require(any(d['decision'] == 'reject' for d in proposal['decisions']), 'rejection decision missing')
    for key, receipt in state['receipts'].items():
        text_field(key); fields(receipt, 'fingerprint result')
        fingerprint = receipt['fingerprint']
        require(isinstance(fingerprint, str) and len(fingerprint) == 64 and all(c in '0123456789abcdef' for c in fingerprint), 'invalid receipt fingerprint')
        result = receipt['result']; fields(result, 'revision record_id replayed')
        require(type(result['revision']) is int and 0 < result['revision'] <= state['revision'], 'invalid receipt revision')
        text_field(result['record_id']); require(result['replayed'] is False, 'invalid receipt result')


def validate_case(p):
    fields(p, 'id topic prompt hints solution criteria validation validation_evidence mode')
    for key in ('id', 'topic', 'prompt', 'solution'):
        text_field(p[key])
    for key in ('hints', 'criteria'):
        require(isinstance(p[key], list) and bool(p[key]), 'nonempty list required')
        for value in p[key]:
            text_field(value)
    require(p['validation'] in ('draft', 'reviewed', 'executed'), 'invalid case validation')
    require(p['mode'] in ('oral', 'ide'), 'invalid case mode')
    require(isinstance(p['validation_evidence'], str), 'validation evidence must be text')
    if p['validation'] != 'draft':
        text_field(p['validation_evidence'])


def review_due(state, requested=False):
    validate_state(state)
    if requested:
        return True
    review = state['reviews'][-1] if state['reviews'] else {}
    previous_sessions = set(review.get('session_ids', []))
    if len([s for s in state['sessions'] if s['id'] not in previous_sessions]) >= 3:
        return True
    previous_events = set(review.get('event_ids', []))
    topics = {}
    for e in state['events']:
        if e['id'] not in previous_events and e['activity'] != 'declared' and e['outcome'] in ('partial', 'incorrect'):
            topics.setdefault(e['topic'], set()).add(e['session_id'])
    return any(len(sessions) >= 2 for sessions in topics.values())


def learning_status(state, topic):
    validate_state(state)
    events = [e for e in state['events'] if e['topic'] == topic]
    practice = [e for e in events if e['activity'] in ('implement', 'debug') and e['modality'] == 'ide'
                and e['assistance'] == 'none' and e['outcome'] == 'correct']
    for applied in practice:
        for later in events:
            if (later['activity'] == 'retrieve' and later['outcome'] == 'correct' and later['assistance'] == 'none'
                    and later['session_id'] != applied['session_id']
                    and timestamp(later['recorded_at']) - timestamp(applied['recorded_at']) >= timedelta(days=1)):
                return 'consolidated'
    if practice:
        return 'autonomous'
    if any(e['activity'] in ('explain', 'predict', 'retrieve') and e['assistance'] == 'none'
           and e['outcome'] == 'correct' for e in events):
        return 'conceptual'
    if any(e['activity'] != 'declared' and e['assistance'] in ('hint', 'guided')
           and e['outcome'] in ('correct', 'partial') for e in events):
        return 'guided'
    return 'explored' if events else 'pending'


def prepare_summary(state, selected_ids, curated_text=None):
    validate_state(state)
    require(isinstance(selected_ids, list) and all(isinstance(i, str) for i in selected_ids), 'selected ids required')
    require(len(selected_ids) == len(set(selected_ids)), 'duplicate selection')
    selected = [e for e in state['events'] if e['id'] in selected_ids]
    require(len(selected) == len(selected_ids), 'unknown selected evidence')
    if state['scope'] == 'project':
        text_field(curated_text)
        return dict(schema_version=1, source_scope='project', source_revision=state['revision'],
                    content=curated_text)
    require(curated_text is None, 'general summary uses only selected evidence')
    return dict(schema_version=1, source_scope='general', source_revision=state['revision'],
                events=copy.deepcopy(selected))


def export_summary(summary, approved_digest, destination):
    require(isinstance(summary, dict) and summary.get('schema_version') == 1, 'invalid summary')
    expected = {'schema_version', 'source_scope', 'source_revision'}
    require(summary.get('source_scope') in ('general', 'project'), 'invalid summary scope')
    expected.add('content' if summary['source_scope'] == 'project' else 'events')
    require(set(summary) == expected, 'invalid summary fields')
    if summary['source_scope'] == 'general':
        for e in summary['events']:
            validate_event(e, 'general')
    else:
        text_field(summary['content'])
    require(bool(approved_digest) and approved_digest == digest(summary), 'exact summary approval required')
    destination = Path(destination)
    require(destination.is_absolute() and destination.resolve() == destination, 'unsafe destination')
    require(not destination.exists(), 'destination already exists')
    fd = os.open(destination, os.O_CREAT | os.O_EXCL | os.O_WRONLY | getattr(os, 'O_NOFOLLOW', 0), 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as stream:
        stream.write(canonical(summary) + '\n')
    return dict(exported=True, digest=approved_digest, destination=str(destination))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('action', choices=['init', 'read', 'validate', 'status', 'apply', 'prepare-summary', 'export-summary'])
    parser.add_argument('--scope', choices=['general', 'project'])
    args = parser.parse_args()
    try:
        if args.action == 'init':
            result = init_store(args.root, args.scope)
        elif args.action == 'prepare-summary':
            data = json.load(sys.stdin)
            result = prepare_summary(read_state(args.root), data['selected_ids'], data.get('curated_text'))
            result = dict(summary=result, digest=digest(result), approval_pending=True)
        elif args.action == 'export-summary':
            data = json.load(sys.stdin)
            result = export_summary(data['summary'], data['approved_digest'], Path(data['destination']))
        elif args.action == 'status':
            state = read_state(args.root)
            result = dict(revision=state['revision'], review_due=review_due(state),
                          topics={topic: learning_status(state, topic) for topic in sorted({e['topic'] for e in state['events']})},
                          active_strategy=active_strategy(state), checkpoint=state['checkpoint'])
        elif args.action == 'apply':
            result = apply_command(args.root, json.load(sys.stdin))
        else:
            result = read_state(args.root)
            if args.action == 'validate':
                result = {'valid': True, 'revision': result['revision']}
        print(canonical(result))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())

