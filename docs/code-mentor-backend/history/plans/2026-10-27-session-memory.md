# Session memory implementation plan

> Historical translated plan dated October 27, 2026. Checkboxes and verification claims are preserved from that work, not reassessed for the current release or installation. Historical execution instructions below are inactive.

> **Historical instruction for agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task by task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Close sessions with continuity and update memory in verifiable batches.

**Architecture:** Extend existing instructions and templates without adding executors or a schema. Keep the personal skill, private plugin, and public source consistent.

**Tech stack:** Markdown, YAML, JSON; existing Python utilities unchanged.

**Spec:** [Session memory design](../specs/2026-10-27-session-memory-design.md).

## Global constraints

- Review every three sessions; group triggers and do not count messages.
- No implicit synchronization or mode transition; check actual write access.
- Company data only within its authorized scope; accept cards before writing.

## Review focus

- Chat without write access: a pending package, without fictional success.
- Reported or copied evidence: do not turn it into independence.
- Retries and partial writes: apply only pending changes after reading current state.
- Mode change or voice: do not assume transferred context or request screen interaction while driving.
- Portable plugin: do not include incompatible `policy.products`; preserve identity and prompts.

### Task 1: Closure and persistence contract

**Files at the time:** `SKILL.md`, `references/session-close.md`, `references/memory.md`, `references/storage-contract.md`, `references/voice.md`, `assets/templates/session-close.md`, `agents/openai.yaml` within the skill.

- [x] Read source and run the initial scenario with version 2.3.
- [x] Add the reference and template, connect them, and clarify capability-based storage.
- [x] Test closure without writing and repeated/partial application; validate the skill and run the existing suite.
- [x] Save and verify the personal update.

### Task 2: Consistent distribution

**Files at the time:** `plugin.json` and private overlay, `README.md`, session-memory and submission-readiness documentation, skill source, and ZIP 2.4.0. The maintained guides now live in [session-memory.md](../../session-memory.md) and [submission-readiness.md](../../submission-readiness.md).

- [x] Update the private plugin while preserving identity and check through a subsequent read.
- [x] Refresh public documentation and package, correcting the actual publication status.
- [x] Verify file publication and package equivalence; document tests and limits.

## Recorded verification result

62 utility tests, basic skill validation, portable schema, links, and metadata: passed. Closure without writing preserved preferences and provenance; recovery respected exact replay and concurrent state. Independent review found an insufficient prior journal; it was added to the reference and template. Synthetic CLI test: replay did not duplicate a version or overwrite the later profile. Private update 2.4.0 was saved and reread; source and package publication was pending final distribution verification.
