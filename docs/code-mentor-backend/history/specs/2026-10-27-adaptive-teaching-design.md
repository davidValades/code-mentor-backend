# Proposed design: teaching adaptation based on evidence

> Historical translated design record dated October 27, 2026. Status and version claims describe that work, not the current installation or public review state. See the maintained [distribution record](../../submission-readiness.md).

Recorded status: implemented in Code Mentor Backend 2.3.0; validation and limits in [submission-readiness.md](../../submission-readiness.md). Date: 2026-10-27.
Chosen approach: combine learner preferences, the needs of the concept, and observed results.

## Goal and approaches considered

Guide the tutor toward helpful aids in similar situations without assigning the learner a fixed style.
Preferences alone were considered (easy to collect but do not measure learning), results alone (better evidence but may overlook comfort and accessibility), and a combined approach (selected). Personal observations support provisional decisions; they are neither a causal experiment nor proof of general efficacy.

## How the tutor decides

1. Retrieve preferences, recent evidence, the checkpoint, and permitted context; open only relevant results.
2. When difficulty arises, first check for a missing prerequisite, overload, or an ambiguous prompt.
3. Choose an aid appropriate to the concept and environment: diagram, analogy with limits, trace, worked example followed by practice, case comparison, self-explanation, prediction, or guided debugging.
4. If comparable prior records exist, prioritize a promising strategy. Otherwise, apply a reasonable option for the content and note the lack of personal evidence.
5. Observe the response and assistance needed; prepare a check using a different example and later retrieval when appropriate.
6. If it does not work, reduce the step, revisit prerequisites, or change an aid. Do not persist because of a prior classification.

Retrieval practice and reviews are retained. During voice interaction while driving, screens, writing, and device handling are not required; an oral response does not demonstrate independent programming ability.

## Private memory

Within the already agreed persistent root, an `adaptacion/` folder separate from the cards:

- `preferencias.md`: declared preferences and restrictions, date, and scope.
- `observaciones.jsonl`: records with a stable ID and a reference to existing evidence, session, date, concept, task, interaction mode, aids used, assistance level, criterion, and observable result. It can record a combination of strategies without attributing the effect to one alone.
- `balance.md`: derived summary by concept, task type, and interaction mode, with observation count, limits, recency, and provisional recommendations.
- `graficos/`: representations derived from the same log, with generation date.

The exact format was to be validated during implementation. Do not invent fields or commands for `mentor_store.py`; the existing schema 2 remains the source of evidence and counters. If evidence was not saved, an observation must not invent its ID or be considered confirmed. General and project scopes remain separate, and personal records are not published in the public repository.

## What success means

Record separately:

- observed immediate understanding;
- application to a new case;
- retrieval in a later session, with the actual delay;
- assistance level;
- clarity, effort, and preferences reported by the learner.

Do not use speed as the main criterion or equate satisfaction with mastery. Retain errors and missing evaluations; distinguish zero successes from a pending check. Do not combine oral and IDE checks, very different tasks, or different assistance levels into one overall rate.

## Charts

Use a table or chart by context and strategy, with results such as successes/comparable attempts, assistance, and delayed retention, always showing the denominator and pending data. With little data, show observations and “insufficient evidence,” without percentages that imply precision or an overall learner ranking. There will be no fictional data or “80% visual” profiles.

Generate Markdown and an exportable static chart when useful observations exist; no new app or dashboard. The chart is not the memory: it is rebuilt from records. It is updated during review in an active session.

## Frequency and autonomy

Choose next-step adaptations without interrupting every explanation, within tutor mode and existing permissions. A brief variant can occasionally be proposed during normal practice without turning lessons into continuous experiments.

Review every three sessions, earlier if a difficulty repeats or the learner requests it. Identify confounders such as prior experience, difficulty, sequence, or multiple simultaneous aids; do not proclaim causality. Reuse `review_due` and the cycle in [improvement-loop.md](../../../../skills/code-mentor-backend/references/improvement-loop.md), without a second counter.

Save operational observations only within the authorized scope. Request setup if none exists and distinguish it from acceptance of knowledge cards. A new permanent teaching preference is proposed, evaluated, and accepted through the existing cycle; trying an explanation does not modify the package or activate a general rule.

## Planned verification

Check sparse data, preference without success, multiple simultaneous aids, successes only with hints, pending retention, voice without an IDE, inaccessible records, old data, and company-specific preferences. Charts and summaries must be traceable to real evidence; reviews do not guarantee educational efficacy.

## Research basis and limits

The research informs the general design; it does not validate this personalized tutor:

- Clinton-Lisell and Litzinger (2024), learning-style review: [DOI](https://doi.org/10.3389/fpsyg.2024.1428732).
- Dunlosky et al. (2013), learning techniques: [DOI](https://doi.org/10.1177/1529100612453266).
- Karpicke and Blunt (2011), retrieval and conceptual learning: [DOI](https://doi.org/10.1126/science.1199327).
- Kalyuga et al. (2003), expertise interaction: [DOI](https://doi.org/10.1207/S15326985EP3801_4).

There is no diagnosis, fixed style, background process, model-weight training, or automatic synchronization.
