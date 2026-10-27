# Teaching adaptation based on results — 2.8

Code Mentor Backend combines declared preferences, the needs of the concept, and real evidence. It explores teaching aids from the start, gradually within normal tasks and reviews. It does not assign learners fixed learning styles or guarantee that a method caused an improvement.

## How it works

Use one main aid per block and one learner action per turn. If prior records are unavailable, choose according to the content and environment and state that limitation. Introduce relevant, untried variants without requiring completion of a catalog before advancing. When difficulty arises, first check prerequisites, step size, and the clarity of the prompt.

The eight existing aids are diagrams, analogies, traces, worked examples, comparisons, self-explanation, retrieval, and guided debugging. Variants include mind or concept maps, call sequences, functional drawings of objects and references, decision tables, partial examples, and fragments to put in order. See the [catalog and protocol](../../skills/code-mentor-backend/references/teaching-exploration.md).

## When it asks for your opinion

It briefly asks about clarity or effort when introducing an aid for that concept or context, or when you get stuck. It offers choices and room for details when the environment supports them. If you have already commented, it uses that statement without asking again. It does not ask after every explanation or routinely at closure; you can skip the rating.

The rating is separate from the learning check, and it waits for your response before the next exercise. “That made the idea clearer” is a self-report. Explaining a decision, solving a variation, and recalling it later provide different evidence, recorded with the interaction mode and assistance received.

## How it uses results

Provisionally prioritize promising aids in comparable contexts; consider the concept, task, difficulty, prior knowledge, order, and accumulated practice. A later explanation may benefit from learning with an earlier one. Retain contradictory results, active retrieval, and relevant opportunities to explore other aids.

Narrative coverage distinguishes “untried,” “insufficient evidence,” “promising in this context,” and “needs review.” A positive rating or a single correct response is insufficient to consider an aid promising. The conclusion requires reviewing several attempts across more than one session and remains provisional, without a threshold of scientific efficacy.

The review uses the existing three-session cycle; it happens earlier when difficulty occurs in two separate sessions or on request. Support is gradually withdrawn to practice independence. Permanent changes to the tutor follow the evaluation and acceptance steps of its improvement cycle.

## Private files

Within the agreed persistent root:

| File | Purpose |
| --- | --- |
| `adaptacion/preferencias.md` | Declared preferences and restrictions, with their scope. |
| `adaptacion/exploracion.md` | Variants, reasons, feedback, coverage, and qualitative review, with dates and linked evidence. |
| `adaptacion/observaciones.jsonl` | Observations with stable IDs and references to existing evidence. |
| `adaptacion/balance.md` | Derived results with date, log revision, and observation fingerprint. |
| `adaptacion/graficos/resultados.svg` | Static chart of those results. |

These files are created during authorized use, not when the skill is installed. The public repository contains utilities and empty templates, not learner data. The main log remains the authority for progress; `exploracion.md` does not duplicate events or counters. Work details remain in their local scope. There is no transmission to the creator, automatic synchronization, or background process.

Without write access, notes join the same pending closure batch. Preparing them does not prove they were saved. While driving, interaction is oral and screen or IDE actions are deferred.

## Utility and charts

With Python 3.11+ and an already configured `state.json`, the utility retains `record`, `read`, and `report` under [the exact contract](../../skills/code-mentor-backend/references/adaptation-contract.md). This extension does not change schema 2 or permit new fields or IDs. Knowledge cards still require acceptance.

`report` generates `balance.md` and `resultados.svg` from `observaciones.jsonl`, grouping by the eight existing IDs and their combinations, concept, and context. It does not ingest `exploracion.md` or calculate its states, coverage, or efficacy by variant. Qualitative assessment is kept separately so regenerating derived files does not overwrite it.

The chart shows successes/attempts, pending evaluations, and sessions, without learning-style percentages or an overall winner. “Insufficient evidence” appears below three evaluated attempts or two sessions with evaluated attempts; this is a presentation guideline, not statistical validation. Exceeding it does not demonstrate efficacy either.

Recorded delayed retrieval requires another session and at least 24 hours since the previous evidence on the same topic. Unverified accounts, copied solutions, and pending evaluations do not count as successes. Combinations are presented together.

Before deciding, the tutor reviews sources, recency, and differences between exercises. Without access, it reports the limitation and prepares a draft; it does not invent charts or achievements.

## Report language

Reports default to English. Use `python scripts/mentor_adaptation.py --root /absolute/path report --language es` for Spanish, or `--language en` explicitly. The optional language changes presentation only: IDs, private paths, grouping, counts, revisions and digests remain unchanged. Other report languages are not implemented by the utility; explain the limitation rather than passing an unsupported value.
