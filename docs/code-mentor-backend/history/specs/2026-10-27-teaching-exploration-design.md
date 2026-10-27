# Design for gradual exploration of teaching aids

> Historical translated design record dated October 27, 2026. Approval described here applies to that design, not to the current installation, package, or public review state.

Approved in conversation on October 27, 2026: integrate the design into the skill and README.

## Goal and decisions

Explore teaching approaches within normal tasks and reviews, using one main aid per block. Ask about clarity when trying an aid new to that context or when the learner gets stuck. Separate that self-report from understanding, transfer, and recall; withdraw support as the learner progresses.

## Approaches considered

- A dedicated initial session: concentrates exploration but takes the learner away from their tasks.
- Integrated gradual exploration: chosen by the user, allowing contextual observations without an initial diagnosis.
- Ask before every trial: offers frequent control but adds interruptions; it was not selected.

## Scope

Document variants and selection, brief feedback, qualitative coverage, and review through the existing three-session cycle. Preserve preferences, accessibility, tutor mode, verified contracts, and card authorization.

## Chosen implementation

Keep the eight IDs and utilities unchanged; extend references and templates with `exploracion.md`, a narrative supplement linked to the main log. Existing charts retain their grouping and do not calculate efficacy by subformat. This decision avoids changing the contract and is an implementation choice, not a claim of new automatic metrics.

## Limits

No fixed styles, causal guarantee, synthetic data counted as achievements, duplicate counters, automatic transfer of work data, background work, or fictional saves. Published source and active installation are separate states.
