# Knowledge library — implementation plan

> Historical translated plan dated October 27, 2026. The original unchecked tasks are preserved; they are not a claim about the current release. Historical execution instructions below are inactive.

> **Historical instruction for agentic workers:** Use superpowers:executing-plans for this small, authorized update.

**Goal:** Add personal cards and documentation study to the existing tutor.
**Architecture:** Markdown references and templates separate from personal records; the memory script and its schema 2 remain unchanged.
**Tech stack:** Markdown, YAML, Python for existing checks and packaging.
**Spec:** [Knowledge library design](../specs/2026-10-27-knowledge-library-design.md).

## Global constraints

Preserve general/project separation, save cards only after acceptance, consult only relevant context, and do not claim persistence or execution without evidence.

## Review focus

Missing log; inaccessible sources or sources for a different version; duplicate card under a different title; oral understanding without practical independence; pending proposal after the three-session review.

## Task 1: Guide and templates

- [ ] Run a baseline scenario with the previous skill and record observed gaps.
- [ ] Add `references/documentation-study.md` and `references/knowledge-library.md`; add `knowledge-card.md` and `knowledge-index.md` templates.
- [ ] Connect references from `SKILL.md`, `curriculum.md`, `memory.md`, and `storage-contract.md`.
- [ ] Resolve access, IDs, approval, history, recovery after partial saves, and company-data separation without new CLI commands.
- [ ] Run a scenario with the updated skill and an alternative without log access; review results.

## Task 2: Documentation and distribution

- [ ] Extend the README and [knowledge-library.md](../../knowledge-library.md); clarify that data is external and private.
- [ ] Raise the package version to 2.2.0, preserve links and the original icon, and update the description and prompts.
- [ ] Validate the installed skill, local links, absence of personal learning data, ZIP, and the utility's 47 tests.
- [ ] Save and verify updates to the personal skill and GitHub repository; compare published files against validated content.
