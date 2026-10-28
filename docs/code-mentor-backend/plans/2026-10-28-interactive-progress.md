# Interactive Progress Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Add private, clickable practice calendars and evidence-linked concept history to Code Mentor Backend.

**Architecture:** Read the existing schema-2 root; derive a minimal model; render a self-contained HTML snapshot and a Markdown summary. No record mutations, new service, automatic transfer or background work.

**Tech Stack:** Python 3.11+ standard library, inline HTML/CSS/JavaScript, unittest and shipped-script in-memory DOM interaction checks; browser/layout verification remains blocked.

**Spec:** ../specs/2026-10-28-interactive-learning-progress-design.md

## Global Constraints

- Preserve schema 2, existing fields, IDs, commands, private paths and retry payloads.
- Data and generated reports remain in an agreed persistent root outside the skill and public repository.
- Count actual learner attempts, including incorrect/helped attempts; exclude declarations and solution assistance.
- Calendar filters describe activity; topic-filtered milestones use all history, including support outside the date range.
- Preserve original event timestamps in delayed batches; disclose unknown actual activity/save times.
- Support English and Spanish report presentation without translating topic identifiers.
- Use a self-contained offline artifact and safe text rendering; no network dependencies or executable record content.
- Publish a new version; preserve the 2.8.0 archive and installed identities.

## Review Focus

- Local midnight, DST and leap-day grouping must use the selected IANA zone, not the browser's zone.
- A later recall can retain its prior supporting practice outside the selected calendar range.
- Hostile summaries/topic strings must display as text; project paths and source references must be absent.
- A failed output write must report failure and preserve an earlier usable report where restoration is possible.
- Narration-only or disconnected chats must not be presented as saved, computed or live progress.

## Task 1: Evidence projection and historical milestones

**Files:** Create canonical `scripts/mentor_progress.py`; create `tests/code-mentor-backend/test_mentor_progress.py`.

**Interfaces:** `build_model(state: dict, *, time_zone: str = 'UTC', language: str = 'en', generated_at: str | None = None, demo: bool = False) -> dict`. Produces source revision/digest, scope, timestamp, zone, localized labels, safe event projections with local days, and all-history topic states/witness IDs/latest checks. No writes.

- [x] Write and run failing tests for qualification, zoned dates, latest-check grouping, state parity, late import timestamps, out-of-range milestone support, project-field omission and invalid options.
- [x] Implement the model using current validation and learning-status semantics; validate unsupported language/zone before side effects. Use deterministic timestamp/ID ordering and include a labeled synthetic-demo option.
- [x] Run the model tests and existing suite with MENTOR_SKILL pointing at the canonical personal skill.
- [x] Record changes and verification in the execution ledger.

## Task 2: Interactive rendering and verified persistence

**Files:** Extend `scripts/mentor_progress.py`; create `assets/progress/report.html`, `report.css`, `report.js`; extend progress tests.

**Interfaces:** `render(model: dict) -> tuple[str, str]` returns HTML/Markdown; `report(root: Path, *, time_zone='UTC', language='en', demo=False) -> dict` returns verified html/markdown paths and snapshot provenance. CLI: `python scripts/mentor_progress.py --root /absolute/root report --timezone Europe/Madrid --language es [--demo]`.

- [x] Write and observe failing tests for empty/demo reports, escaped embedded JSON, Markdown evidence labels, actual CLI, safe destinations, existing locks, unchanged state, stale-source detection and failed-write recovery.
- [x] Render inline assets with a restrictive CSP and textContent for record strings. Provide clickable/keyboard-accessible days, dates/topic/activity/help/result filters, reset, filtered totals, day details, a table alternative, all-history concepts and latest-check evidence.
- [x] Use a 12-month default, a maximum 366-day visible calendar range, and 0/1/2/3/4+ intensity buckets. The input range can move to older dates; model evidence remains full history. Clearly label the snapshot and its actual scope.
- [x] Generate under the existing root lock, preflight all targets, atomically replace each file, verify both and source identity; restore previous outputs on failure when possible. Never mutate state.
- [x] Run unit/CLI checks and execute the shipped JavaScript in an in-memory DOM for day selection, filters/reset, keyboard navigation, empty/hostile data and date boundaries. Attempted local-file browser navigation was rejected by policy; no workaround was attempted.
- [ ] Verify actual browser rendering, CSP enforcement and narrow-screen layout when an authorized test surface is available.
- [x] Record results and decisions in the ledger.

## Task 3: Tutor integration, distribution and independent checks

**Files:** Update canonical SKILL.md, memory/session-close/storage references; create references/progress-report.md. Update public root/skill READMEs, package manifest and readiness; add release 2.9.0 archive; preserve old archives.

**Interfaces:** `/progress` and `/progreso` route to the new contract; closing refreshes after verified authorized saves. Hosts without JSON/computation/writing keep an honest narrative/pending request. Progress adds no new shortcut or progress source. The later notebook addition introduces /notes and /apuntes.

- [x] Run a baseline skill scenario before editing instructions; retain only synthetic output.
- [x] Add concise routing and the report contract: exact CLI/output paths, qualifications, snapshot/date/filter meanings, host/permission boundaries and pending behavior.
- [x] Validate the actual personal skill and run all tests. Run a fresh application scenario against the updated skill, then a whole-change review; fix important findings with reproducing tests.
- [x] Save and verify the personal skill. Update the existing private plugin to 2.9.0, preserving identity/audience; verify source readback.
- [x] Publish source/tests/docs and the immutable new package to the collection; read back current source and record actual installation/package status. Public OpenAI approval remains separate.

## Execution decisions

- Execute inline in this session; the user explicitly approved implementation. Do not ask for another plan/method approval.
- Skill Creator requires edits in the canonical personal-skills checkout. Use that authoritative directory and stage only this skill; do not create a second installable scratch copy. Tests and public documentation stay in the collection workspace.
- Existing public source changes are saved through the GitHub connector. Local task bookkeeping does not become learner memory.
- The static artifact cannot know it became stale offline. Display revision/digest/generation time; regenerate on request or verified close rather than claiming a live connection.

## Completion and notebook addition

User-authorized notebook scope is implemented in references/study-notes.md and assets/templates/study-notes.md, with routing, session closure and public guide updates. File-tool scenario validates creation, indexing and retrieval without fabricated learning evidence. The final timestamp regression is covered. See submission-readiness.md for exact installation/release evidence, the deferred session-grouping minor and browser/layout limits.
