# Storage contract v2

## Location and boundaries

Keep data outside the skill package. Agree on a personal profile root and separate local root per project. Check access, persistence, and company policies; avoid company-Git-tracked or externally synchronized directories without authorization. Do not change repository configuration on your own initiative. Use absolute roots; temporary directories do not guarantee continuity.

Each root has `state.json`: schema 2, revision, general/project scope, events, sessions, reviews, cases, attempts, observations, improvements, documents, and receipts. JSON supplies evidence/counters; Markdown preserves narrative. Read each document's latest referenced version; orphaned files after interruptions are not current. Do not edit versions directly.

The optional conocimientos/ library uses cards/index written with file tools per knowledge-library.md. The CLI does not manage it: no kind=knowledge or save_knowledge command. state.json retains evidence/counters; the index is derived; cards summarize learning. Do not change schema 2 for this extension.

The CLI neither uses the network nor synchronizes devices. Without Python or persistence, prepare continuity and report saving pending. Do not attribute script guarantees to manual writes.

## CLI

For document-service notes or no write access, follow session-close.md. Service-returned remote identities are not local CLI roots. Read-only attachments are not editable records. Replacement requires the service tool and current version, not another copy. With Markdown alone, preserve narrative/batch receipts; do not simulate state.json, calculations, or charts. Preserve any JSON root's authority. Closing packages add no apply operations/fields; preparation does not configure storage.

Run `python scripts/mentor_store.py --root /absolute/path init --scope general` with Python 3.11+. Other commands: read, validate, status, apply, prepare-summary, export-summary. `status` returns revision, review_due, derived topic statuses, active strategy, and checkpoint. Supply JSON via stdin; never interpolate content or secrets into shell.

`apply` receives request_id, expected_revision, operation, and payload; returns revision, record_id, and replayed. Retry with identical ID/content. On conflict, reread and reconcile. Do not break locks without investigating another writer.

Operations: record_evidence, save_checkpoint, complete_session, record_review, save_case, record_case_attempt, record_observation, confirm_convention, propose_improvement, record_evaluation, set_trial, decide_improvement, save_document. Exact fields/examples follow. Send user_confirmed=true only after explicit acceptance; the script does not verify conversation.

## Evidence and privacy

General event: id, session_id, recorded_at in ISO format with a time zone, topic, activity (declared/explain/predict/implement/debug/retrieve), modality (oral/text/ide), assistance (none/hint/guided/solution), outcome (correct/partial/incorrect/unverified), evidence_summary, review_due (date with a time zone or null). Project events add task_id and source_refs.

Reference: relative path, full commit or null, branch, boolean dirty, observed_at. Commits do not represent local changes: use dirty=true when appropriate. Never save authenticated remote URLs.

The schema rejects additional work fields in general events but does not anonymize free text. Review before saving: generic concepts/transferable difficulties are allowed; company names, paths, code, requests, and decisions are not. Sharing work context requires exact-summary approval.

save_document receives id, kind (profile/project/task/checkpoint/improvement), title, Markdown content, and recorded_at. General scope allows only profile; others belong in project scope. Versions are immutable. The script cannot identify every secret: review text before persistence.

Do not overwrite unknown schemas or automatically migrate v1. Prepare and confirm migrations, preserving provenance and evidence.

## Exact CLI inputs

`apply` receives a stdin object: `{"request_id":"identificador-estable", "expected_revision":0, "operation":"...", "payload":{...}}`. Obtain revision from `read` or an actual write. Event and request IDs differ. On save failure, retain exact input for retry.

| Operation | Exact payload fields |
| --- | --- |
| record_evidence | The event fields defined above; add task_id and source_refs only for project. |
| save_checkpoint | session_id, topic, evidence_id (string or null), pending_question, next_step, recorded_at. |
| complete_session | id, recorded_at. A repeated id does not create a new session. |
| record_review | id, recorded_at, reason, result. The script automatically captures the sessions and evidence reviewed. |
| save_case | id, topic, prompt, hints (list), solution, criteria (list), validation (draft/reviewed/executed), validation_evidence (text), mode (oral/ide). |
| record_case_attempt | id, case_id, session_id, response, assistance, outcome, recorded_at. |
| record_observation | id, task_id, statement, source, recorded_at; project only. |
| confirm_convention | Observation id, user_confirmed=true, scope, reason; only after actual confirmation. |
| save_document | Logical id, kind, title, Markdown content, recorded_at. |
| propose_improvement | id, reason, evidence_ids (nonempty list), baseline, candidate. candidate accepts only explanation_words (40–250), example_lines (1–20), analogies (boolean), and diagrams (when_interaction/on_request/frequent). |
| record_evaluation | id, improvement_id, kind (deterministic/model/manual), results, cases, checks. cases contains at least one design and one heldout, each with id, split, baseline_response, and candidate_response. checks contains at least three booleans, including accuracy and permissions. |
| set_trial | Improvement id, action (start/complete/decline), user_confirmed=true, and summary. Only after that choice has actually been made; complete describes the observed outcome. |
| decide_improvement | Improvement id, decision (accept/reject/revert), user_confirmed=true, reason. accept requires a favorable evaluation and a completed or explicitly declined trial. |

**Hypothetical** evidence example; do not save as a student's response:

```json
{"request_id":"req-001","expected_revision":0,"operation":"record_evidence","payload":{"id":"e-001","session_id":"s-001","recorded_at":"2026-10-26T18:00:00+01:00","topic":"methods","activity":"declared","modality":"oral","assistance":"none","outcome":"unverified","evidence_summary":"Says they understand what is returned; this still needs to be checked.","review_due":null}}
```

Prepare exports with `prepare-summary` and stdin `{"selected_ids":["e-001"]}`; project scope also requires `curated_text`, a manually written minimal summary. Output contains `summary`, `digest`, and `approval_pending=true`. Show the entire summary. Only after the user accepts that exact content, call `export-summary` with stdin `{"summary":<shown object>,"approved_digest":"<received digest>","destination":"/absolute/path/nueva.json"}`. A digest alone is never authorization. Export refuses existing-file overwrites and uses private POSIX permissions where available; still review destination policies.

Use `status` for calculated statuses; do not call Python functions directly from conversation. The review counter uses newly completed sessions and observed evidence since the last review. Recurring-difficulty adjustment requires two different sessions.

## Separate adaptation utility

mentor_adaptation.py follows adaptation-contract.md, retains referenced observations, and produces assessment/SVG. It neither extends apply operations nor changes schema_version=2. Cards/index still use file tools.

## Separate progress utility

For a clickable practice calendar and topic-filtered historical evidence, use mentor_progress.py per [progress-report.md](progress-report.md). It reads this same schema-2 record and writes only progress/index.html and progress/summary.md. No new state fields, apply operations or record IDs. Saved derivatives are snapshots, never memory authority; without JSON/computation, retain the narrative/pending flow above. Correction/deletion review includes these files and authorized copies.
