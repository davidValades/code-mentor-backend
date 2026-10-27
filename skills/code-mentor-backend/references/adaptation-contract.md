# Observations and charts contract

## Location and authorization

Use the agreed general/project root and schema 2 state.json. Do not create/migrate the main record. If unset, agree storage once with the learner; temporary directories guarantee no persistence. Operational authorization covers observation writes without repeated questions; card content still needs acceptance. Keep team preferences/company code out of general scope.

## Available CLI

Python 3.11+: `python scripts/mentor_adaptation.py --root /absolute/path record`, `read`, or `report`. record reads JSON stdin; read is read-only; report writes local summary/SVG. No other commands. Never interpolate inputs/secrets into shell commands.

| record field | Value |
| --- | --- |
| id | Stable observation ID: lowercase letters, numbers, dots, hyphens; maximum 128 characters. |
| evidence_id | ID actually present in this root's events. |
| concept_id | Stable, generic concept ID; reuse when resuming, with the same safe convention. |
| task_kind | read / trace / explain / implement / debug. |
| difficulty | introductory / standard / complex; explicit contextual estimate. |
| check_kind | immediate / transfer / delayed. |
| strategies | Nonempty list without duplicate IDs from adaptive-teaching.md; include every aid used, never credit combination success to each component. |
| learned_evidence_id | null for an immediate check, or prior learning evidence ID; required for transfer/delayed. |

The utility rejects other fields and derives result, activity, modality, assistance, session, and date from real evidence, without another mutable copy. It separates learning/check modalities. For transfer, the tutor must verify a new case; the utility cannot judge semantic content. delayed requires another session, same topic, and at least 24 hours since prior evidence; the summary shows actual delay.

strategies describes the evaluated learning episode's aids. For later checks, preserve its set and inspect history. The event's assistance field separately records help during the check. Never change strategies to attribute review to another method.

Retry exact id/content; strategies order is normalized. Identical repeats are idempotent. Reject reused IDs with different data and duplicate evidence under different observation IDs. Correct by reviewing record/derived outputs, never by adding another observation of the same attempt. History edit/delete is not automated.

## Guarantees and limitations

The utility atomically rewrites adaptacion/observaciones.jsonl under mentor_store.py's root lock. It never breaks locks; it rejects unsafe paths/symlink destinations and preserves private POSIX permissions where available. These measures replace no environmental security and guarantee no exclusion against tools ignoring the lock.

read revalidates current-state links, excluding deleted evidence as orphaned and contract failures as incompatible. Main evidence/counters stay unchanged. For deletion requests, review affected observations, preferences, summaries, charts, and copies; promise no external-system erasure.

Statements, unverified results, and responses with solution assistance remain pending, never evaluated attempts/correct responses. Separate other attempts into correct, partial, incorrect; hinted success is not autonomy.

report generates adaptacion/balance.md and adaptacion/graficos/resultados.svg with date, source_revision, observation_digest. These are rebuildable derivatives, not memory sources. On write failure, claim no complete update; rerun report and verify both files. Changed record revision requires summary review/regeneration before decisions. Keep preferences in separate Markdown, not JSONL.

Never fabricate observations from teaching examples/test-agent outputs. Empty charts are valid; do not generate learner data to fill them.

Check both source_revision and observation_digest against read: adding observations does not increment state.json revision. Regenerate before use if either differs.

## Narrative variants and assessments

Keep the eight strategies IDs. Describe maps, tables, partial exercises, and other variants per [gradual exploration](teaching-exploration.md) in same-scope adaptacion/exploracion.md with feedback/evidence links. Send no variant, feedback, coverage, clarity, or other new fields to record; add no variants to candidate or state.json.

This Markdown supplements the main record without events, counters, or changes to observaciones.jsonl. report ignores it: balance.md and resultados.svg group by existing IDs, calculating neither narrative states nor subformat effectiveness. Keep qualitative analysis outside regenerated derivatives to preserve it.

Before updating exploracion.md, read current identity/version; preserve others' contributions/history. Verify afterward. Keep work details in authorized local scope. Deletion requests include this document/authorized copies. Without access, keep changes in the same pending batch; claim no save.

## Report language

Reports default to English. For Spanish, use `python scripts/mentor_adaptation.py --root /absolute/path report --language es`; explicit English: `--language en`. Language changes presentation only; IDs, private paths, grouping, counts, revisions, and digests stay unchanged. Other report languages are unimplemented; explain rather than pass unsupported values.
