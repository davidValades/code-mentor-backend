# Weekly Learning Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans inline; maintain the existing authorized save workflow.

**Goal:** Organize actual covered material into evidence-linked Monday–Sunday blocks.

**Architecture:** File-tool weekly summaries and history in the existing notebook; two bounded-inspector checks. No new schema, store operation, app or scheduled task.

**Tech stack:** Markdown, Python 3.11+ stdlib, existing file services.

**Spec:** ../specs/2026-10-28-weekly-learning-design.md

## Constraints and review focus

- Preserve scope, occurrence dates, source authority, retry identity and accepted-card rules.
- Unknown dates and future material cannot become observed weekly achievements.
- Calendar closure is separate from completeness and session completion.
- Read only relevant indexes/sections; retain bounded scans and history exclusion.

## Task 1 — Weekly contract and inspector

- [x] Run baseline scenario and new failing weekly-index tests.
- [x] Add weekly reference/template, `/week` route and session-close integration.
- [x] Extend inspector indexed groups; verify green tests and full suite.

## Task 2 — Forward check and release

- [x] Verify actual synthetic weekly artifacts, links, dates, evidence limits and state integrity.
- [x] Update guide, root README, manifest and distribution record; build 2.11.0, preserving older archives.
- [x] Validate/save installed skill, private plugin and public source, then read back versions/content.

## Verified outcome and limits

108 tests passed, installed validation passed and synthetic weekly creation/update/history/no-op checks completed. Review corrected hiatus calendar-state selection; source remains schema 2. Personal and private saves were read back. Public source/package use the same collection transaction. Session-driven summaries require an accessible authorized record; no scheduled task or real learner history was created.
