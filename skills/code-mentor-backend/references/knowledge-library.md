# Personal knowledge library

## Access and organization

Keep outside skill/public repository in agreed persistent storage. If unset, ask once with options. Never create real cards in assets/templates. .md files open nothing themselves; consult other files with available tools.

Each authorized root uses `conocimientos/index.md`, `conocimientos/fichas/<id>.md`, and `conocimientos/historial/<id>/r0001.md`, r0002.md, etc. General scope: concepts/synthetic examples without company names, paths, code, or requests. Keep team knowledge in local project root; sharing requires authorization for the exact summary.

Derived index: ID, title, relative card path, revision, topics/topic, prerequisite IDs, update date, pending review. Read index first, then relevant cards/prerequisites only. Evidence/counters remain in state.json; cards summarize, never create another grading source. A study plan may be summarized in profile/current task; no extra counter.

## Identity and content

Use assets/templates/knowledge-card.md. IDs must be stable, readable, without private data; e.g. `csharp.operadores.igualdad`. Allow lowercase letters, numbers, dots, hyphens; exclude dates. Search index by ID/title/synonyms before creation; update existing cards. Preserve existing IDs/creation dates despite new conventions. Validate filenames; never use unsafe IDs as paths. Renaming titles creates no new concept.

Include zoned ISO 8601 created_at/updated_at, integer revision starting at 1, scope, record topic(s), sources (URL/section/access date/applicable version), relationships/prerequisites, brief explanation in own words, minimal synthetic example, questions, next practice, suggested review. Sources explain concepts, never prove learning.

Separate verified technical content, stated understanding, demonstrated conceptual understanding, guided practice, practical autonomy. Support each advance with real evidence IDs, date, activity, modality, assistance degree. Without accessible records, label conversational observation/statement pending recording; invent no IDs. Reading cards, choosing options, copying code prove no mastery. Preserve relevant questions/incorrect results; history need not rise in level.

## When to propose and when to save

Propose at topic/task close with useful material, every review after three new sessions since last review, sooner for the same difficulty in two different sessions, or on request. Use review_due per memory.md; count no messages. Merge coinciding triggers into one proposal. Without relevant additions, report “no changes”; create no empty revisions.

Show ID, reason, exact changes, evidence-supported learning status. New card: full content. Update: changes with prior content accessible. Obtain proposal acceptance before writing card/index. Rejection/deferral preserves current card. This consent neither replaces nor interrupts authorized evidence/checkpoint saves. Cards do not change tutor instructions.

On deferral, save pending IDs/changes in authorized checkpoint, never as approved card. Record learning reviews even if cards are refused. Next session, inspect pending items as well as review_due. Never seek renewed acceptance for accepted, unsaved proposals; retry exact content after version checks.

## Writing and recovery

Use file tools for cards/index; mentor_store.py has no save operation for them. Send no `kind=knowledge`; change no schema. Manual writes inherit none of its locking, receipt, or atomicity guarantees.

After acceptance:

1. Reread card/revision. If changed since proposal, reconcile and present new changes before overwriting. Verify paths/destination stay within agreed root without symlinks into other scopes.
2. Before updates, preserve exact current content in historial/<id>/rNNNN.md. Never overwrite history with different content. Increment revision once; preserve created_at; record actual updated_at.
3. Write card, then its index row with revision/relationships. Touch no cards outside proposal.
4. Read saved results; verify ID, revision, dates, relative links, history before claiming success. On failure, report saved/pending parts. Matching retries create no extra revision.

After interruption, resolve card/index disagreement by checking card/history; verify and repair only derived index row. Infer no progress from index. With concurrent writers, stop on conflict and coordinate; promise no safe manual locking.

Without access/persistence, present pending draft in conversation. Claim neither saving, reading the whole library, nor cross-environment synchronization. Update during active sessions only; no model training/background work.
