# Teaching adaptation and submission preparation — implementation plan

> Historical translated plan dated October 27, 2026. Checkboxes and results are preserved from that record, not reassessed for the current release. Historical execution instructions below are inactive.

> **Historical instruction for agentic workers:** Execute in that session; the design was approved by the request to finish everything.

**Goal:** Complete evidence-based adaptation and a verifiable 2.3.0 package.
**Architecture:** Teaching references and a local utility for observations and derived representations, retaining `mentor_store` schema 2 as the source of evidence.
**Tech stack:** Standard Python 3.11, Markdown, JSONL, SVG; no network or background process in the utilities.
**Spec:** [Adaptive teaching design](../specs/2026-10-27-adaptive-teaching-design.md).

## Global constraints

Respect existing scopes and permissions; do not invent mastery, causality, data, or approval. Do not save personal learning in the public repository.

## Review focus

Sparse data; missing or corrected evidence; combined strategies; retention checks still pending; voice and different assistance levels not comparable.

## Tasks

- [x] Establish a comparison baseline with the previous tutor and RED tests for the new utility.
- [x] Implement logging by evidence ID, grouping by context/aid/check type, and derived charts; protect retries, paths, and pending data.
- [x] Update the guide, templates, memory, and improvement cycle; test scenarios and review independently.
- [x] Validate previous storage, the new utility, the package, and content privacy; publish source and record checks.
- [x] Verify public links and metadata, check current official guidance, and prepare ZIP 2.3.0.
- [x] Inspect portal access; access was not completed. Draft, scans, and declarations remained pending and were not presented as a completed submission.
