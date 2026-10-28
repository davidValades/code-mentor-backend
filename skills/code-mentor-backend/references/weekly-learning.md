# Weekly learning blocks

## Location and purpose

Use for `/week [ISO-week/date]`, `/semana`, weekly history, or after a verified session close. Group the actual material covered into Monday–Sunday blocks in the existing authorized general/project root:

- `notes/weeks/index.md`: derived week/date/status/source-coverage index.
- `notes/weeks/YYYY-Www.md`: one continuing summary per ISO week, e.g. `2026-W44.md`.
- `notes/history/week-yyyy-www/rNNNN.md`: immutable prior revisions without native version history.

Keep session notes, accepted cards and schema-2 evidence authoritative. A weekly summary links their relevant sections; it adds no grades, evidence events, completed sessions, teacher-review counters or permanent teaching preferences. Keep work context in project scope. No learner data belongs in the skill/public repository.

## Choose the period

Use the learner's known IANA time zone, e.g. Europe/Madrid; ask once if missing and material, otherwise disclose UTC as a fallback. Default to the current week. Resolve ISO week-year, Monday start and the following Monday's exclusive boundary using actual calendar tools/Python when available. For example, 2026-W44 is October 26–November 1; W45 is November 2–8. At year boundaries the ISO year may differ from the date's calendar year. Validate requested week/date; ask only if ambiguity changes the period.

Assign each known block/event by its original occurrence date converted to that zone, not its save/import/file-creation date. A session crossing weeks can appear in both through its distinct dated blocks, with each event counted once. Without sufficient occurrence dates, keep the source unassigned and disclose it; do not infer dates from filenames alone. Future-dated material remains proposed/planned or pending verification, never already-observed learning. Label synthetic fixtures separately throughout.

Set calendar state to upcoming, in_progress or elapsed from the current local date. Elapsed means the period ended, not that capture is complete or learning sessions were completed. Preserve original dates and flag conflicts rather than reconstructing unknown activity. A late authorized import may revise a prior week's summary with history; never rewrite its original occurrence time.

## Retrieve and summarize

Read the weekly index/checkpoint, then only relevant session-index rows, note sections, evidence and accepted cards. Known pending imports may identify earlier affected weeks. Do not scan every historical note at each turn or fill missing days with invented activity. Use assets/templates/weekly-learning.md.

Include:

1. Period, time zone, calendar state, actual generation/update dates, revision, authorized scope and source cutoff/coverage.
2. Relevant sessions/tasks and material covered, including vocabulary corrections, examples and unfinished topics; link exact accessible note sections and retained file-service identities.
3. Demonstrated progress with existing evidence IDs, original dates, modality, assistance and outcome. Separate teacher explanation, learner declaration, conceptual understanding, guided attempts, actual independent IDE work and later recall. Reuse existing status rules; a weekly note or copied solution proves no mastery.
4. Difficulties, mistaken predictions and corrections, unknowns and observations requiring confirmation. Keep team decisions sourced and task-scoped.
5. Teaching aids and context, declared clarity/effort, observed outcomes and limits. Do not credit a format for learning from feedback alone or infer a fixed learning style.
6. Open task state, pending card proposals, next small practice/review and links to accepted cards. Suggested review dates are not reminders or scheduled jobs.

Write a compact weekly overview with linked detail, not a transcript, a copy of all session notes or a table of empty days. Show incomplete coverage and undated/future items separately. On request, compare weeks using observed evidence and help levels; no invented scores, streaks or causal improvement claims. In conversation, give the requested overview or one selected concept, not lessons on every listed topic.

## Update, history and cadence

After a saved and verified session close, update only the affected week's summary and index when actual material changed. Also refresh on `/week`, `/save` or a weekly-history request with authorized writing. On resumption, inspect the compact weekly index for existing rows whose calendar state differs from the state calculated from today's local date; include these and specifically known pending/source-affected weeks. This covers a W44 in_progress block when the next visit is W48, and upcoming blocks whose period has now begun. Reconcile changed calendar metadata with history while retaining coverage gaps; do not reread unchanged historical source notes or create empty skipped weeks. Add the current week only when relevant material exists. Preserve pending weekly updates in the existing checkpoint/batch when writing is unavailable. No extra counter and no per-message regeneration.

Before replacing, read current identity/revision, preserve exact prior content in native history or the history path, then update the same week ID. Increment revision/updated_at only for a real change; retain created_at. Reread the summary, verify source links/dates, then write and verify its index row. Index columns: week ID, local start/end, calendar state, coverage/cutoff, summary path/revision, updated date. Links are relative to the index file; `2026-W44.md` resolves inside notes/weeks/.

Use existing retry/version checks. A failed index update leaves index refresh pending, not another weekly file or duplicate evidence. Conflict requires rereading/reconciliation; preserve original sources. If history cannot be retained, leave replacement pending. Include weekly saved/pending status in the same closing receipt. Corrections/deletions include affected weekly summaries, histories and indexes under existing memory rules.

## Execution limits

This default runs during active sessions. It does not execute at midnight, close chats from silence, retrieve inaccessible conversations or automatically activate Work. Do not create a real folder or weekly history until an authorized persistent destination exists. With native document storage use real folder/document identities and native history; state any folder/view limitation.

A separately requested scheduled closure requires an actual automation and verified access to the same sources/destination. Installing this skill creates no such automation. Without access, provide one pending weekly draft/continuity package and report what is missing. While driving, give a short oral recap and defer screen interaction. Design sessions and synthetic QA create no real weekly learner archive.
