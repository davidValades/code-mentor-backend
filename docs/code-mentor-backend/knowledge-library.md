# Studying documentation and retaining knowledge

Code Mentor Backend 2.8 includes guided documentation study and personal concept cards, introduced in version 2.2. It does not require a separate app or server.

## How information is consulted

[SKILL.md](../../skills/code-mentor-backend/SKILL.md) contains the rules and reference-selection table. To study a source, the assistant consults [documentation-study.md](../../skills/code-mentor-backend/references/documentation-study.md); to find or maintain cards, it uses [knowledge-library.md](../../skills/code-mentor-backend/references/knowledge-library.md). The assistant opens those files with the environment's tools: Markdown files do not run searches by themselves.

At the start, it retrieves the accessible log, checkpoint, and knowledge index. It then opens only related cards and their prerequisites. It compares their summaries against log evidence and applicable documentation. A card is not, by itself, proof of mastery.

## External private library

The agreed persistent location is organized as follows:

- `conocimientos/index.md`: catalog by ID, relationships, revision, and review.
- `conocimientos/fichas/<id>.md`: current card for each concept.
- `conocimientos/historial/<id>/r0001.md`: previous revisions preserved before an update.

This structure is created when its use is configured and authorized, outside the skill package. The public repository contains instructions and empty templates, never the learner's actual library. The general profile contains concepts and synthetic examples; company tasks, names, and code remain in their authorized project context.

The library can sit alongside the agreed general log. It must not be created automatically inside a work repository or published on GitHub. If ChatGPT and Codex cannot access the same location, they do not share changes by themselves; an allowed continuity summary is prepared.

## What a card contains

A stable ID such as `csharp.operadores.igualdad`, title, scope, incremental revision, ISO dates with timezone, topics, prerequisites, consulted sources and applicable version, brief explanation, synthetic example, evidence and assistance received, questions, next practice, and suggested review. The creation date and ID are preserved even if the title changes. Consulting documentation does not demonstrate learning; self-reported understanding, conceptual understanding, guided practice, and independence are distinguished.

## When saving is proposed

The tutor uses a combined system: at the end of a topic or task with relevant new findings, every three sessions since the last review, earlier if a difficulty recurs in two separate sessions, or at the learner's request. It groups coinciding reasons and does not create empty revisions.

It shows the proposal and asks for acceptance of its content before writing cards or the index. Previously authorized evidence and checkpoint logging continues without requesting permission for each block. If a proposal is deferred, it remains pending in the checkpoint; it is not presented as knowledge already saved.

## Example study request

“Use Code Mentor Backend. I've been asked to review C# operators. Check what I've demonstrated I know and suggest where to start.”

The tutor reviews accessible prior knowledge, consults primary sources, checks the version when it affects the project, and prepares a short route. It explains one idea, proposes a prediction or practice task, and waits for the response. At the end of the block it can propose a card; it does not mark the whole topic mastered because the learner read the documentation.

## Technical limits

`mentor_store.py` still uses schema 2 for evidence and counters. Cards and the index are managed with file tools; there is no `save_knowledge` command or `kind=knowledge`. Manual writes do not have the utility's locking and receipt guarantees. Without access or persistence, a pending draft is shown without claiming it was saved. There is no background work, automatic synchronization, or model-weight training.
