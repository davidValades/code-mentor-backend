# Code Mentor Backend

A step-by-step C#/.NET backend tutor for understanding real code and becoming more independent.

Source version: **2.8**. Portable package version: **2.8.0**. Repository source, built package, installed skill and public approval are separate states.

## What it helps with

- Read complex code by following calls, intermediate values and responsibilities.
- Refactor verified contracts, such as changing a nullable return value to a result with explicit states.
- Debug by forming hypotheses, choosing breakpoints/log observations and checking the evidence.
- Study official documentation from demonstrated prerequisites and turn it into practice.
- Learn precise technical vocabulary, with respectful corrections when needed.
- Practice recall, transfer and later application with progressively less help.

It uses one main concept per step, small examples and one learner action at a time. Ask for a direct solution when needed; editing files still requires an explicit request for that action.

## Language

The instructions, documentation and canonical shortcuts are in English. The tutor responds in your requested language or the language you are using, including Spanish. English is only the fallback when no language can be inferred. Code identifiers remain exact.

Language changes do not rename existing private folders, IDs or JSON fields. Names such as `adaptacion/exploracion.md` are kept for compatibility.

## Shortcuts

These are optional text requests interpreted while the skill is active, not native ChatGPT/Codex commands or an installation mechanism. Ordinary language works too.

| Shortcut | Spanish alias | Purpose |
| --- | --- | --- |
| `/help` | `/instrucciones` | Show a short menu; `/help all` shows the complete list. |
| `/learn` | `/aprender` | Learn one concept and check understanding. |
| `/study` | `/estudiar` | Plan study of a topic or documentation. |
| `/review` | `/repaso` | Retrieve earlier learning and practice recall. |
| `/debug` | `/depurar` | Investigate a bug step by step. |
| `/progress` | `/progreso` | Summarize accessible evidence, difficulties and helpful aids. |
| `/save` | `/guardar` | Save authorized records if writing is available; show saved and pending items. |
| `/task` | `/tarea` | Clarify scope and choose a first step. |
| `/read` | `/leer` | Follow a code fragment and its calls. |
| `/refactor` | `/refactorizar` | Reason about a verified contract and affected cases. |
| `/hint` | `/pista` | Get a small hint. |
| `/solution` | `/solución`, `/solucion` | Request a direct explanation/solution without granting editing permission. |
| `/glossary` | `/vocabulario` | Explain a term in context. |
| `/voice` | `/voz` | Adapt an oral lesson to available time, where voice is supported. |
| `/resume` | `/continuar` | Resume from accessible context without inventing memory. |
| `/check` | `/corregir` | Review your explanation or code and explain corrections. |

For example: `/study C# operators`, or `/leer Explícame este método paso a paso`. Neither request forces the conversation into English.

## Teaching that adapts

The tutor gradually explores relevant aids inside normal tasks and reviews: analogies, concept/mind maps, call sequences, object/reference drawings, decision tables, traces, partial examples, ordering exercises and guided debugging. It uses one main aid per block.

When introducing an aid in that context or detecting a blockage, it asks one brief question about clarity or effort, using options and optional details where supported. Feedback already offered is not requested again. A learning check happens separately.

Clarity, immediate understanding, transfer and later recall remain distinct. The tutor records assistance and context and provisionally favors promising aids for particular tasks. It does not assign fixed learning styles or infer mastery from “I understand”.

See [adaptive teaching](adaptive-teaching.md) and the [exploration protocol](../../skills/code-mentor-backend/references/teaching-exploration.md). The current chart groups eight strategy IDs and their combinations; narrative subformats and feedback live in `adaptacion/exploracion.md`, not new automatic chart metrics.

## Memory and privacy

The tutor prepares the notes; you do not need to draft the learning record yourself. Durable memory requires an agreed persistent destination, actual write access and authorization.

It records meaningful blocks, prepares a closing note, and groups updates at task completion, after three newly completed sessions, repeated difficulty across two sessions, or your request. It counts sessions, not messages. Knowledge cards require acceptance of their exact content.

With authorized writing, it saves and reads back results. Without it, it prepares one pending package and may suggest a user-initiated Work handoff. Work itself grants no file permissions; another available authorized storage tool may also suffice.

There is no background work, automatic cross-device synchronization or guaranteed cross-chat memory. General learning profiles exclude company details; work context stays in its authorized scope. See [session memory](session-memory.md) and the [knowledge library](knowledge-library.md).

Local charts/reports default to English; select `report --language es` for Spanish. Presentation language does not change stored evidence or paths.

## Verify your installation

Ask the agent to read the available skill's SKILL.md, state its version and identify its source. Reading GitHub verifies repository source, not installation in that chat. A saved private plugin is also distinct from host behavior actually tested.

The tutor can make mistakes. Check code and proposed changes against the real project, tests and applicable Microsoft documentation.

## Build, support and distribution

[Portable package 2.8.0](../../dist/code-mentor-backend/code-mentor-backend-2.8.0.zip). Downloading and building remain separate from installation.

Build from the collection root with `python tools/build_plugin.py code-mentor-backend`. The result contains only this skill and its packaging resources.

[Support](support.md) · [Privacy](privacy.md) · [Terms](terms.md) · [Distribution status](submission-readiness.md) · [MIT license](../../LICENSE)
