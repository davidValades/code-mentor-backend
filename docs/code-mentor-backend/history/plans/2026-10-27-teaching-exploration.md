# Gradual exploration of teaching aids — implementation plan

> Historical translated plan dated October 27, 2026. Checkboxes, versions, hashes, and verification results are preserved from that work. They do not establish current installation or publication status. Historical execution instructions below are inactive.

> **Historical instruction for agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task by task. Steps use checkbox syntax for tracking.

**Goal:** Add the agreed gradual exploration and feedback to the skill and README.

**Architecture:** Retain the existing CLI, IDs, and schema. Add a protocol and narrative template with evidence links; connect teaching, closure, and documentation.

**Tech stack:** Markdown; existing Python utilities unchanged.

**Spec:** [Teaching exploration design](../specs/2026-10-27-teaching-exploration-design.md).

## Global constraints

- One main aid per block; normal tasks and reviews.
- Feedback when an aid is new in that context or the learner gets stuck, separate from evaluation.
- No new fields, IDs, operations, or counters in the CLI.
- No learner data in the package or installation promises.

## Review focus

- No accessible memory: state the limit and retain pending items.
- Positive rating without practice: do not establish mastery.
- Driving: oral interaction and screen practice left pending.
- Combined aids: do not attribute the result to isolated components.
- Regenerating `report`: retain narrative analysis outside the derived summary.

## Task 1 — Protocol and log

- [x] Create `references/teaching-exploration.md` and `assets/templates/teaching-exploration.md` in `skills/code-mentor-backend`.
- [x] Connect `SKILL.md`, `teaching.md`, `adaptive-teaching.md`, and `adaptation-contract.md`.
- [x] Integrate episodes and pending items into the closure reference and template and the preferences template.
- [x] Review links, IDs, separation of self-report and evidence, and the five review-focus conditions.

## Task 2 — Documentation and verification

- [x] Update `README.md` and adaptive-teaching documentation; declare source 2.7 and portable package 2.4.0. The maintained guide now lives in [adaptive-teaching.md](../../adaptive-teaching.md).
- [x] Verify links and preservation of shortcuts and contracts; reread all saved files.
- [x] Check with a synthetic scenario without recording learner progress.
- [x] Report source updates separately from unverified installation and execution.

## Execution environment at the time

The local environment was disconnected. No Python scripts were run or modified, no ZIP was prepared, and no update to the personal installation or private plugin was claimed. Repository changes were saved through the GitHub connector.

## Recorded verification

- Input snapshot: `12b68e23f3e36e05c948d76789c90913e6a72d4f`.
- Reviewed candidate source: `b5681ca8a68f9fcf525459472c8f62491574c009`.
- Nine static checks: 16 shortcuts preserved; explicit versions; 14 variants with supported IDs; frontmatter preserved; scripts/state/manifest unchanged; feedback separate from evaluation; compatible delay; 42 relative links resolved; input reads matched the snapshot.
- All 13 candidate files were reread and exactly matched the proposed content.
- Tree comparison: no files deleted and no changes outside the 13 expected files.
- Independent review of source, teaching, adaptation, memory, and closure: no major errors identified.
- Synthetic scenario: a learner who knows `true`/`false`, gets lost following calls, and has no memory folder. The response introduced a trace with a small C# example, distinguished the call from the `if` body, asked only about clarity at the end, and stated that no progress had been saved.
- The test was a model response using the candidate source, not use of an active installation or evidence of efficacy or progress by a real learner.
- No Python execution or `quick_validate` because of the lack of a local environment. No scripts were modified. Updating the personal installation and private plugin remained pending.
