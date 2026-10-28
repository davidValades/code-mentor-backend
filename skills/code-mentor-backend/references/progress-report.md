# Interactive progress report

## Route and source

Use for /progress, /progreso, a progress/calendar request and verified session close. Read memory.md and storage-contract.md first. Keep a short conversational summary; generate the artifact when requested or closing an authorized saved session. No new command, separate memory source, service or background task.

Use the agreed persistent general or project root, schema 2 evidence and Python 3.11+. Preserve scope; never aggregate company details into a general report or publish it. Source instructions/templates may be public; actual reports remain private. The generator reads only state.json, not the full knowledge library or adaptation history.

```bash
python scripts/mentor_progress.py --root /absolute/authorized/root report --timezone Europe/Madrid --language es
```

Set the learner's known IANA time zone; otherwise disclose UTC. Languages: en/es, default en; preserve topic identifiers. For other conversational languages explain the report limitation rather than passing an unsupported option. Use --demo only with clearly synthetic QA, never actual learner records. No init, record, import or save operations exist in this utility.

## Meaning

- Practice: an actual learner explain/predict/implement/debug/retrieve event with none/hint/guided assistance. Incorrect, partial and unchecked own attempts count. Reading/listening alone, declarations, solution-assisted responses, teacher answers, messages and repeated writes do not. Record one event per actual attempt; do not split an action to inflate activity.
- Calendar: distinct qualifying event IDs per local day; intensity 0/1/2/3/4+. Default last 12 months; select an older interval, at most 366 days. Empty means no qualifying record, not no learning.
- Clicking days shows attempts, help, results, source dates and IDs. Keyboard arrows select adjacent days/weeks; the table is an alternative. Topic/date/activity/help/result filters affect practice. Reset restores defaults.
- Learning history: selected topics over all available evidence, regardless of calendar/activity filters. Reuse the store's historical states, with witness IDs/dates; distinguish oral concepts from independent IDE practice. Later retrieval uses another session at least 24 hours after independent IDE practice. No mastery percentage or fixed learning style.
- Latest checks remain grouped by topic/activity/modality, with help and date. Exclude declarations, unverified and solution-assisted responses from evaluated checks. These are observations, not a new recency/forgetting rule. Use existing review triggers for reinforcement decisions.

## Dates and refresh

Preserve each supplied recorded_at and exact pending/retry payload. Convert for display, never rewrite timestamps or move old events to import day. Existing timestamps establish only what their sources support; do not infer missing historical activity/save times. Generated-at describes the report, not the learner's effort or last data write.

After authorized evidence/checkpoint writes and session completion are verified, generate once at close. Also generate on a progress request with suitable access; do not rebuild after each message. Read the real JSON result and verify both returned files:

- progress/index.html: self-contained interactive snapshot, with inline resources and no network calls.
- progress/summary.md: default-range summary, up to ten recent attempts and all-topic historical evidence.

Revision, source fingerprint, generation date and zone identify the snapshot. Report failures leave the view pending; do not replay already-saved evidence or undo a completed session. The utility checks safe paths, holds the existing lock, reads outputs back, detects source changes during generation and tries to restore previous outputs on failure. Report partial-restoration errors honestly. It cannot exclude writers ignoring its lock or guarantee multi-file transactions after abrupt process termination.

## Host and privacy boundaries

The file is read-only: clicks/filters save nothing. Opening interactive HTML needs a compatible host or browser; attachment access does not prove preview/execution support. Do not promise inline interaction in every ChatGPT session. With JSON/computation/writing unavailable, show an evidence-grounded narrative and keep report generation pending under session-close.md. Do not manufacture dates, counters, achievements or parallel JSON from Markdown alone. Old snapshots must retain their dates; claim no live synchronization.

The report omits project task IDs, source_refs and code paths, but evidence summaries remain private within their original scope. Review them before any authorized sharing. On correction/deletion, regenerate or remove affected HTML/Markdown and authorized copies; do not claim erasure from inaccessible services. Never use generated HTML or synthetic tests as learning evidence.
