# Session closure and batched memory — 2.4.0

> Historical translated design record dated October 27, 2026. The authorization, implementation, and verification described here concern that work and do not establish the current installation or public review state.

## Goal and authorization

The user requested implementation in that session of tutor closure, with a summary of work, demonstrated learning, and outstanding items, plus a periodic proposal to update memory with Work when Chat cannot write. Retain the existing skill; do not create an app, server, or scheduled task. Reuse the already agreed preferences for privacy, approved cards, and review every three sessions. The routine choices below are implementation decisions, not newly attributed user preferences.

## Approaches

- Save every message with Work: interrupts and consumes usage without providing a learning unit; rejected.
- Save in batches at task closure, every three completed sessions, after repeated difficulty, or on request: implemented using the existing review. Prepare a brief note at the end of each session and accumulate pending items.
- Only copy the entire conversation manually: does not provide the requested verifiable record; retain only as a fallback when tools are unavailable.

## Design

A closure reference and template define a package with stable identity, included sessions, scope and destination, facts with provenance, proposed changes, and a persistence receipt. Separate authorized operational notes from cards awaiting acceptance. Do not invent evidence, mastery, or sessions. Preparing the package in the conversation does not establish persistence or transfer between modes.

With verified persistent write access, apply authorized changes to the same log and read the results. Otherwise, leave one visible package and a short prompt for the user to activate Work or take it to an environment with access. Work does not have permissions because of its name: discover actual capability, check the destination and revision, reconcile pending items, avoid duplicates, and verify the write. In Library, replace the same identity; a read-only attachment is not modified through the shell. Without an accessible JSON log, Markdown is narrative and does not establish calculated counters or charts.

## Restrictions

Do not switch to Work, spend purchased credits, grant permissions, or create synchronization automatically. Cards require exact acceptance. Keep work data in the local project and request authorization of the exact summary before transferring it. While driving, do not request screen interaction. Do not record this design conversation or synthetic test data as learning.

## Verification

Initial scenario with skill 2.3: it offered a summary without a fictional save, but no application package with identity/status or instruction for batched updates. Later test with the new closure; additional case with a repeated package, partial write, and concurrent state. Validate the private package through actual ingestion and check the saved version's files. The public portal remained a separate channel, and this update did not resolve its skills-only restriction.
