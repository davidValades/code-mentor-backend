# Memory Controls Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans inline. Steps use checkboxes for tracking.

**Goal:** Make memory state inspectable, reviewable and navigable without changing its authority.

**Architecture:** One read-only inspection utility plus routed teaching references/templates. Reuse schema-2 persistence and the existing progress generator.

**Tech stack:** Python 3.11+ standard library, Markdown, host-rendered Mermaid.

**Spec:** ../specs/2026-10-28-memory-controls-design.md

## Global constraints

- Keep schema 2, existing root boundaries and all existing operations.
- Do not claim active version, write access, actual save time, semantic validity or cross-chat access from a file read alone.
- Audit reads only authorized data: 200 Markdown files, 2 MiB total, 256 KiB per file; report incomplete coverage.
- Keep student data out of public source; synthetic cases never award achievements.
- Inline execution and save/update authorization carry forward from the conversation.

## Review focus

- Symlinks, encoded traversal and local link targets must not escape the root.
- An old record timestamp cannot become a recent save receipt.
- An incomplete scan cannot report a clean complete audit.
- Topic-level evidence cannot imply card-level competence or prerequisites.
- Invalid state and interrupted writes must remain diagnosable without mutation.

### Task 1: Read-only status and mechanical audit

Files: create scripts/mentor_inspect.py in the installed skill; tests/code-mentor-backend/test_mentor_inspect.py in the collection.

Interface: `python scripts/mentor_inspect.py --root ABSOLUTE_ROOT status|audit` returns JSON. `inspect_root(root, action)` returns a snapshot with findings and read limits; does not write.

- [x] Write subprocess tests for truthful timestamps/capabilities, no mutation, missing documents, stale report, unsafe/broken links, unindexed/duplicate notes, bounds and invalid state.
- [x] Run the tests and observe missing-command failures.
- [x] Implement safe bounded reading, structured findings and unchanged-source verification.
- [x] Run new tests and existing suite.

### Task 2: Routed controls and map

Files: SKILL.md, memory/session-close/curriculum/storage/progress references; create references/memory-controls.md, references/knowledge-map.md and assets/templates/knowledge-map.md.

Interfaces: `/status`, `/memory-audit`, `/map [goal]`; reuse store state, note/card indexes, file-service receipts and current checkpoint.

- [x] Record baseline behavior with the existing skill.
- [x] Add routing, concise output contracts, semantic audit process and evidence-linked map with table fallback.
- [x] Forward-test controls and continuation in an isolated authorized fixture with fresh agents; inspect actual artifacts.

### Task 3: End-to-end continuity verification

Files: tests/code-mentor-backend/test_memory_continuity.py; docs/code-mentor-backend/memory-check.md.

Interfaces: existing store CLI, inspection CLI and progress CLI across separate processes; note identity/revision/history via file tools.

- [x] Add and run a failing integrated case for save/reopen/retry/status/audit/report and unchanged evidence after inspection.
- [x] Run the implemented flow; provide a real-user acceptance checklist with host-specific limitations.
- [x] Record browser/layout and actual user-session checks honestly as unverified when unavailable.

### Task 4: Documentation, review and save

Files: root/skill README, distribution status, manifest, portable source mirror and new 2.10.0 archive; preserve older archives.

- [x] Update shortcut tables, examples, limitations and release metadata.
- [x] Run full suite, skill validator and package build/inspection.
- [x] Obtain one fresh whole-change review; address material findings with regression tests.
- [x] Save personal skill, private plugin and public source; read back version/content and preserve existing identity/audience.

## Verified outcome and limits

Completed source v2.10 / package 2.10.0 with 106 passing tests, personal-save verification, private-release readback and synthetic fresh-context note continuation. Public source/package are saved through the collection release transaction. No real learner session, host activation, cross-chat access or browser/mobile rendering is claimed from these checks. See submission-readiness.md for current distribution evidence.
