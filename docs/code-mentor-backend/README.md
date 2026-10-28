# Code Mentor Backend

A step-by-step C#/.NET backend tutor for understanding real code and becoming more independent.

Source version: **2.11**. Portable package version: **2.11.0**. Repository source, built package, installed skill and public approval are separate states.

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
| `/notes` | `/apuntes` | Find your private dated study notes by topic or session. |
| `/status` | `/estado` | Inspect instruction source/version, record access, verified saves and known pending items without writing. |
| `/memory-audit` | `/auditar-memoria` | Review authorized memory quality and propose corrections; apply no changes. |
| `/map` | `/mapa` | Connect a goal to concepts, evidence and linked notes/cards. |
| `/week` | `/semana` | Retrieve or refresh a Monday–Sunday learning block with dated sources and next steps. |
| `/progress` | `/progreso` | Summarize evidence and generate a private clickable calendar and concept-history report where supported. |
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

## Interactive practice and learning history

Use `/progress` or `/progreso` to consult a private report:

- Click a calendar day to inspect your attempts, concepts, help, results and evidence IDs.
- Filter practice by concept, dates, activity, help or result; reset to the initial view.
- Count actual attempts, including mistakes and guided practice. Reading/listening alone, declarations, copied solutions, teacher messages and repeated saves do not fill the calendar.
- Consult historical concept states and dated evidence separately from activity. Calendar filters do not erase the earlier practice supporting later retrieval.
- Read the latest evaluated checks by activity and medium; oral understanding and independent IDE implementation remain distinct.

A darker square means more recorded practice, not greater mastery. Empty means no qualifying record, not proof of no learning. There are no invented percentages, points for copying or automatic claims of permanent mastery.

The initial calendar shows the last twelve months; choose any interval up to 366 days, including earlier periods. Days use stored source timestamps in the displayed IANA time zone. Delayed imports preserve their original dates; unknown activity/save times are not reconstructed.

With the agreed schema-2 record, Python and authorized writing, the tutor refreshes the report on request or after a saved, verified session close. Outputs stay in the same private root: `progress/index.html` and `progress/summary.md`. A report failure leaves the view pending; it does not undo saved learning records. Corrections/deletions include these derivatives.

The HTML is self-contained and read-only, with no server or network calls. Opening it requires a compatible host or browser; inline interaction is not guaranteed in every ChatGPT chat. Without the necessary evidence, computation or writing, the tutor gives a narrative summary and leaves generation pending. The file is a dated snapshot, not a live connection or automatic cross-device memory.

Local example for an already authorized root:

```sh
python skills/code-mentor-backend/scripts/mentor_progress.py --root /absolute/learning/root report --timezone Europe/Madrid --language es
```

The main record stays at schema 2. Source instructions and test fixtures may be public; never upload your actual learning or work reports to this repository. See the [report contract](../../skills/code-mentor-backend/references/progress-report.md).

## Your private study notebook

The tutor keeps notes of all topics actually covered, including explanations, examples, vocabulary corrections, learner attempts, debugging observations, unfinished ideas and open questions. Notes are not limited to achievements. Use `/notes`, `/apuntes` or an ordinary request such as “show my notes about return values”.

Within your agreed private learning or project root:

- `notes/index.md` links notes by topic, date and session.
- `notes/sessions/YYYY-MM-DD-note-ID.md` continues one note per session.
- `notes/history/` preserves prior revisions when native document history is unavailable.

With authorized persistent writing, the tutor updates notes after significant blocks and finalizes them at session close, verifies the result and updates the index. It does not make one file per message or load the whole notebook into every prompt. File-service folders and native versions may provide the equivalent structure.

Teacher explanations, synthetic examples, learner declarations and demonstrated results are labeled separately. An entry in the notebook awards no learning achievement; curated knowledge cards still need content acceptance. Work notes stay in their project scope, not the public repository or general profile.

No destination is silently configured. Without access, notes remain clearly pending in the closing package. Past sessions can only be reconstructed from accessible sources, with uncertainty stated. See the [notebook contract](../../skills/code-mentor-backend/references/study-notes.md).

## Weekly learning blocks

Use `/week`, `/week 2026-W44` or `/semana` to consult a linked overview of a Monday–Sunday period. For example, 2026-W44 covers October 26–November 1 and W45 covers November 2–8. Week assignment uses original occurrence dates in your known time zone, not save/import dates.

Private `notes/weeks/index.md` links one `notes/weeks/YYYY-Www.md` per relevant week. Each block includes topics/tasks, evidence with assistance, difficulties, teaching aids, open questions and next practice, plus source coverage and revision history. Session notes remain the detailed sources; weekly blocks award no achievements.

The tutor updates affected weeks after verified session closes or relevant requests and reconciles stale calendar states from the weekly index when you return, including after skipped weeks. It preserves the same week identity/history and leaves undated/future material uncertain. Elapsed calendar weeks are separate from complete capture or completed sessions. This default does not create a scheduled background task. See [weekly learning history](weekly-learning.md).

## See what is saved

Use `/status` or `/estado` for a concise report of the inspected instruction source/version, actual authorized record, scope/revision, verified write receipts and known pending items. Reading repository files does not prove that version is active in every chat. Reading a folder proves neither write access nor durable storage. If actual save time is unknown, the tutor says so instead of substituting a learning-event date.

Use `/memory-audit` or `/auditar-memoria` to review memory quality. The optional read-only utility checks record structure, referenced files, current note/card indexing and links, duplicate-content candidates and progress-report freshness. Its scan is bounded; skipped files and remaining semantic checks are disclosed. The tutor then reviews relevant contradictions, project/source versions and learning claims. It proposes corrections without automatically merging, deleting, rewriting evidence or changing accepted cards.

```sh
python skills/code-mentor-backend/scripts/mentor_inspect.py --root /absolute/learning/root status
python skills/code-mentor-backend/scripts/mentor_inspect.py --root /absolute/learning/root audit
```

These commands do not modify the learning record or create its locks. No new record destination is configured by running them. With file-service/Markdown storage, the tutor uses actual identities and versions and states which calculated checks are unavailable. See [memory controls](../../skills/code-mentor-backend/references/memory-controls.md).

## Connect your knowledge

Try `/map method return values` or `/mapa contratos Result`. The tutor retrieves a small relevant selection of indexed notes/cards and evidence, shows their relationships and provides a linked table. It distinguishes material studied, conceptual understanding, guided practice, independent IDE work, later recall and unassessed areas. A broad-topic result does not prove every sub-concept.

Explicit accepted-card prerequisites remain separate from proposed teaching routes. Missing notes, source code or evidence are shown as gaps. The map ends with one useful next action, not explanations of every concept. Links use accessible notes/cards; unavailable documents are not invented.

With authorized persistent writing, `progress/map.md` is a verified derived snapshot in the same private root. It does not replace the record or automatically rewrite cards. A linked table works when Mermaid cannot render; voice lessons describe a small relationship orally and defer screen interaction while driving. See the [map contract](../../skills/code-mentor-backend/references/knowledge-map.md).

## Memory and privacy

The tutor prepares the notes; you do not need to draft the learning record yourself. Durable memory requires an agreed persistent destination, actual write access and authorization.

It records meaningful blocks, prepares a closing note, and groups updates at task completion, after three newly completed sessions, repeated difficulty across two sessions, or your request. It counts sessions, not messages. Knowledge cards require acceptance of their exact content.

With authorized writing, it saves and reads back results. Without it, it prepares one pending package and may suggest a user-initiated Work handoff. Work itself grants no file permissions; another available authorized storage tool may also suffice.

There is no background work, automatic cross-device synchronization or guaranteed cross-chat memory. General learning profiles exclude company details; work context stays in its authorized scope. See [session memory](session-memory.md) and the [knowledge library](knowledge-library.md).

Local charts/reports default to English; select `report --language es` for Spanish. Presentation language does not change stored evidence or paths.

## Verify your installation

Ask the agent to read the available skill's SKILL.md, state its version and identify its source. Reading GitHub verifies repository source, not installation in that chat. A saved private plugin is also distinct from host behavior actually tested.

Use the [end-to-end memory check](memory-check.md) to verify a real session's note, revision history, verified save, map links and resumption from another conversation with access to the same record. Automated isolated tests use synthetic data and do not establish real learning, cross-chat access or browser/mobile layout.

The tutor can make mistakes. Check code and proposed changes against the real project, tests and applicable Microsoft documentation.

## Build, support and distribution

[Portable package 2.11.0](../../dist/code-mentor-backend/code-mentor-backend-2.11.0.zip). Downloading and building remain separate from installation. Earlier archives are retained.

Build from the collection root with `python tools/build_plugin.py code-mentor-backend`. The result contains only this skill and its packaging resources.

[Support](support.md) · [Privacy](privacy.md) · [Terms](terms.md) · [Distribution status](submission-readiness.md) · [MIT license](../../LICENSE)
