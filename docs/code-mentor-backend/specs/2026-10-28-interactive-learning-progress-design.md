# Interactive learning progress

Status: approved by the learner on 2026-10-28; implementation tracked in [the plan](../plans/2026-10-28-interactive-progress.md).

## Intent and agreed choices

Extend Code Mentor Backend with a private, interactive progress report. Show practice over time and evidence of learning separately. Keep this a skill-generated artifact, using the existing record rather than a hosted application or an additional progress database.

The learner selected two requirements:

- Count a practice day after an actual learner attempt to explain, solve or debug, including attempts with help or an incorrect result.
- Support clicking calendar days and filtering concepts from the first release.

Keep canonical source instructions in English, retain Spanish aliases, and present the report in the learner's language where supported. Preserve current personal and private-plugin identities. Do not store actual learner data in this public repository.

## Approaches

1. Markdown with static SVG: portable and consistent with current reports, but does not provide the requested day selection and filtering.
2. Self-contained HTML with embedded data, CSS and JavaScript: selected. Supports those interactions offline, without a server or a new service. Opening interactive HTML depends on the host or a compatible browser.

Retain a small Markdown companion for conversation and environments that cannot display the HTML. Do not promise that every ChatGPT conversation can execute or preview it.

## Current foundations

Source 2.8 already has schema-2 events and completed sessions with zoned `recorded_at` dates, stable IDs, revision checks and exact-request replay. Events retain topic, activity, modality, assistance, outcome and evidence summary. `mentor_store.py` derives explored, guided, conceptual, autonomous and consolidated states. `mentor_adaptation.py` generates a separate strategy-results report.

Preserve these schemas, private paths, commands and retry semantics. This extension reads the record and produces derivatives; it does not replace the learning-status algorithm, adaptation report or knowledge-card acceptance process.

## Report and interactions

- Show a GitHub-like calendar, initially the last 12 months, with an accessible date-range selector.
- Make each day keyboard-selectable. Selecting it shows saved learner attempts, concepts, assistance, result and evidence identifiers, grouped by session ID. A completed session's closing date may be shown as metadata, but there is no completed-session KPI in this release. A session may have activity on several days.
- Filter by existing event topic, with optional activity, assistance and outcome filters. Provide a clear reset. Do not merge or translate topic identifiers implicitly.
- Apply date, activity, assistance and outcome filters to the calendar, activity counts and day details consistently. Label these as filtered practice. The topic filter also selects concepts in the separate learning-history pane; label that pane as all available history. Activity filters must not recompute a lower historical learning status or discard supporting practice outside the date range.
- Show a concept table with highest observed evidence, its date and supporting IDs, calculated from the full authorized root history for selected topics. Explain the current status rules. Label these as observations, not a measured percentage of mastery.
- Show historical milestones supported by the existing statuses: explanation/prediction without help, independent IDE implementation/debugging, and later independent retrieval under the current rule. Supporting evidence may precede the calendar date range. Distinguish conceptual and IDE evidence. Show the latest evaluated attempt for each topic/activity/modality context with date, result and assistance; exclude declarations, unverified and solution-assisted responses from this latest-check view. Order equal timestamps by stable event ID for deterministic display. Do not introduce a recency window, a new mastery-loss heuristic or a permanent-mastery claim. Older results remain available in activity history. Existing tutor review triggers still govern reinforcement decisions.
- Display scope, time zone, generation time and source revision. State that the file is a snapshot. Offline HTML cannot detect later source changes.
- Use text labels and a tabular alternative as well as color. Avoid hover-only details. Keep the report usable on a narrow screen, with an accessible calendar alternative.

The report is read-only. Clicking and filtering neither changes learner records nor awards achievements.

## Activity and dates

Calendar intensity counts distinct qualifying event IDs: 0, 1, 2, 3 and 4+ attempts per local day. This scale describes recorded practice, not learning quality. No rewards for messages, tokens, generated teacher answers, copied solutions, saving documents or replaying writes.

A qualifying event records an actual learner explanation, prediction, implementation, debugging or retrieval attempt; assistance is none, hint or guided. Correct, partial, incorrect and genuinely unchecked learner attempts can count for activity. Declared understanding and solution-assisted responses do not count. Unverified results grant no learning milestone. Do not manufacture or split events to fill the calendar. Session closure alone cannot establish practice. Empty cells mean no qualifying practice is recorded, not proof that no learning occurred.

Use the stored event timestamp after conversion to the report's explicitly displayed time zone. Preserve the original timestamp when applying a delayed pending batch; do not replace it with import time. Older records do not establish an actual activity date beyond what their source supports: disclose that limitation, exclude undated narrative notes and never invent dates. Report generation time is separate from activity time. Actual save time may be shown only when a real write receipt/journal supplies it; do not derive it from file modification time or claim old save times are known. Preserve schema 2 and exact retry payloads.

Use a known learner IANA time zone when available; otherwise explicitly label UTC. No duration tracking, background monitoring or guessed study minutes. Time-zone presentation changes do not rewrite event timestamps.

## Storage and lifecycle

Generate `progress/index.html` and `progress/summary.md` inside the already agreed, persistent general or project record root. These are rebuildable views, never the source of truth. Use exactly one root per report. Do not silently aggregate project data into a general profile, copy company details elsewhere or publish the report.

Extend `/progress` and `/progreso`; no new shortcut is needed. Generate on request and at session close after authorized changes have actually been saved and verified. During active use, do not rebuild after every message. Use source revision and the report's date/time-zone/range options to determine freshness. The report does not require adaptation observations or scan their entire history.

Without usable JSON evidence and computation, provide an honest narrative summary and a pending report request. With no write access, do not claim the report was refreshed or create a second memory source. An older accessible report must show its snapshot information. A user-initiated Work/other-environment handoff follows the existing batched close process. No scheduled/background work or automatic cross-device transfer.

## Implementation boundaries and validation

Add a small deterministic report generator and a routed reference, keeping the main skill concise. Use standard-library Python, inline browser resources and escaped data. Load only required record fields. Include no telemetry, CDN, network requests, remote fonts or executable learner content. Render record strings as text; prevent HTML/script injection. Omit company file paths, snippets and source references from the initial report. Evidence summaries remain within their original authorized scope.

Respect existing root validation, locking, safe paths and atomic writes. Validate all report inputs before creating outputs; report both output paths only after successful verification. A generation failure must not mutate events or report a complete refresh. Preserve a previously usable report where feasible and disclose partial output failures. Treat a source revision change during generation as stale, not as a current report.

Test dates across local midnight and DST, delayed batches, duplicate/replayed IDs, open/multi-day sessions, qualification rules, no data, filtered totals, conceptual versus IDE milestones, supporting evidence outside the calendar range, latest-check ordering and assistance labels, escaped hostile text, unsafe destinations, stale snapshots and write failure. Exercise real browser day selection, filters, reset, keyboard access and narrow-screen layout with clearly labeled synthetic fixtures. Never save QA as learner achievements.

Update the skill references and English public guide. Keep installed source and private distribution consistent when the new release is authorized. Preserve old archives; version a new package rather than replacing release 2.8.0. Public submission/approval remains a separate process.

## Proposed defaults for review

The 12-month default, five intensity buckets, optional secondary filters, output paths and automatic refresh at verified session close are design proposals, not additional preferences already chosen by the learner. Review resolved three builder choices: use all-history evidence for milestones, show factual latest checks rather than an undefined recency flag, and omit completed-session totals to avoid misleading day/topic attribution. The builder may settle visual styling, internal helper names and other routine implementation details within this contract.

## User-requested notebook addition — 2026-10-28

The learner also requested a folder containing notes of everything covered. Include all relevant explanations, examples, corrections and doubts, not only demonstrated achievements. Implement the private notes/index.md and per-session notes contract with a reusable template, native/immutable version history and /notes (/apuntes) routing. Use existing authorized file tools and memory boundaries; add no evidence fields or unsupported CLI operation. Notes remain separate from accepted cards and progress evidence. Retrieve only indexed relevant sections.
