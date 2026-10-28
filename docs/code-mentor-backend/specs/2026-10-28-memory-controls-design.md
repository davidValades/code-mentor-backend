# Memory visibility, audit and knowledge map

Implement the four improvements requested after v2.9: an end-to-end continuity check, `/status`, a memory-quality review, and a navigable knowledge map. The user requested all four in this session. Extend the existing skill, not a hosted application.

## Approach

Keep schema 2 and the existing private roots as authority. Add one read-only Python utility for reproducible status and mechanical audit. Use agent judgment for semantic contradictions and a small goal-specific map drawn from existing evidence, indexed notes and accepted cards. A separate database, automatic rewriting and a global graph would duplicate authority and increase reading cost.

## Status

`/status` (`/estado`) reports the inspected instruction source/version, activation uncertainty, authorized destination/scope, observed revision/digest, available document identities and last recorded evidence date. Show last verified write receipt only when accessible; a record timestamp or file modification time is not the actual save time. Reading package or repository files never proves that version is loaded in every conversation. Reading a root proves neither persistent service guarantees nor write access. Pending content comes from accessible checkpoints/batch receipts and the current conversation; unknown is not none.

## Audit

`/memory-audit` (`/auditar-memoria`) reads only the agreed scope. The utility checks state validity, referenced document files, current note/card indexes, relative Markdown links, unindexed notes/cards, exact duplicate current content, and progress-snapshot freshness. Cap scanning at 200 Markdown files, 2 MiB total and 256 KiB per file; disclose incomplete coverage. Ignore historical versions for duplicate/orphan checks. Return findings without repairs or deletion. Semantic contradictions, technical currency, unsupported learning claims and prerequisite cycles require targeted agent review and source verification. Corrections follow existing permissions; cards still require exact-content acceptance. No scheduled audit or new counters.

## Map

`/map [goal]` (`/mapa`) produces a small map and a linked table from the current objective and selected indexes. Use explicit accepted-card prerequisites where available; label proposed prerequisite routes as teaching hypotheses. Nodes distinguish studied material, demonstrated concept understanding, guided practice, independent IDE work, later recall, and unknown coverage. Broad-topic evidence does not prove every sub-concept. Include dated evidence, exact accessible note/card sections, remaining doubts and one next action. Mermaid has safe generated node IDs and concise labels; linked tables remain the navigable fallback. Save `progress/map.md` only with authorized verified file writing; it is a derived snapshot, not a second grading source. Do not load the entire notebook or add inferred edges to accepted cards automatically.

## End-to-end acceptance

Use isolated synthetic data to test separate-process save/reopen, same-note revision/history, retry idempotency, status/audit and report generation. Publish a reproducible real-session checklist covering the same steps, read-only fallback and no automatic cross-chat access. Design/QA is not student learning. Browser/mobile layout and host activation must be verified in their actual host; the previous blocked local-file browser test must not be bypassed. A synthetic pass never claims those checks or real student progress.

## Boundaries and release

No schema changes, new store operations, automatic fixes, model-weight changes, background jobs, secrets, public learner records or new services. Keep English source/canonical shortcuts and Spanish aliases. Release v2.10 / 2.10.0 to the existing personal skill, private plugin and public collection; preserve existing identities, audiences, prompts, icons and older archives.
