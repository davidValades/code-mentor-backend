# Memory and evidence v2

## Retrieve before teaching

Read [the contract](storage-contract.md) before the first write. Locate the general record and, for work, the agreed project's record. Use read for revision, current documents, active tasks, and checkpoint; load only relevant content. Do not search company code from ChatGPT if only a summary is authorized. Without access, use that summary and state its date and limits.

For a configured knowledge library, consult its index and relevant cards per [the knowledge library](knowledge-library.md). Include pending checkpoint proposals even if review_due is already false.

Keep two scopes: general (concepts, transferable difficulties, demonstrated achievements) and project (tasks, context, files/versions, necessary snippets). Do not copy work content into the general profile. On first use without agreed locations, ask where to save using options; a temporary directory does not guarantee persistence.

## Saving during use

For session closes, mode changes, and pending batches, follow [session close](session-close.md). Prepare a note after every session; batch updates through Work only at its defined triggers when Chat cannot write. The session-close.md template preserves batch identity, provenance, destination, pending items, teaching aids, and receipt. Do not save design sessions or synthetic data as learning.

After each significant block, record observations and checkpoint. At close, save the checkpoint and complete the session exactly once. A pause keeps the same session_id; an unprocessed disconnection does not prove saving. Do not repeatedly request permission to save already authorized content within the agreed scope.

Use stable IDs and the latest revision. Retry uncertain writes with identical ID, original revision, and content. On conflict, reread and reconcile; do not invent new evidence for the same event. Check the actual result and saved revision. On failure, report saving pending and prepare continuity; never record fictitious success.

For narrative, use assets/templates and save_document: general profile or local project/task. Keep previous decisions/context versions; history need not copy whole conversations. Allow corrections: preserve an explicit correction and explain its effect. For deletion requests, also remove receipts/documents retaining that content and verify removal; do not claim deletion of external copies. The utility does not automate deletion or migrations; do not use apply for unsupported operations.

## Evidence and progress

Record activity, modality, assistance, outcome, and specific response/action evidence. Self-reports use activity=declared, outcome=unverified. “I understand” and copied solutions do not prove mastery. Correct explanations can demonstrate conceptual understanding; practical independence requires unaided IDE implementation or debugging with observed outcomes. Consolidation requires independent retrieval in another session at least one day after that practice. Do not turn purely oral concepts into programming achievements.

learning_status calculates status from evidence; conceptual distinguishes understanding, not a practical level above guided. Case attempts do not automatically create evidence: evaluate the response first. Recalculate status after correcting a record.

After a brief task check, prepare a small challenge for another session: oral in voice mode; reserve an IDE exercise for practical goals. Use approximate 1/3/7/14-day intervals, adjusted to actual retrieval; these are neither individual predictions nor created reminders. A “yes” does not postpone a review earned through actual practice.

## Teacher review

Check review_due after each completed session. Review every three new sessions since the last review; sooner on user request or same-topic difficulty in two different sessions. Reviews need not change anything: save reason, evidence, and outcome, including “no changes.” Base the counter on sessions and reviews, not a manually edited number.

Show progress in conversation with a small competencies/evidence/next-steps table; do not create a dashboard or app. Without the same record, do not claim ChatGPT shares memory with Codex.

Without an accessible record, a reported third session permits a provisional review and pending batch, not a claim that review_due was calculated. Do not rely on app closes or equate three messages or chats with three sessions.

## Learning and review document

At task completion, three-session review, recurring difficulty, or student request, prepare a brief Markdown note for future sessions. Include date, concepts, demonstrated facts with evidence references and assistance level, declared but unverified understanding, difficulties, corrected terms, open questions, next exercise, and approximate review date. Distinguish observation from hypothesis; never treat copied or oral responses as practical independence.

Update the general profile without company names, code, or details using save_document kind=profile and a stable logical ID; preserve previous versions and check results. Save work-task details/references only in the authorized project record with kind=task and a stable logical ID, following project-context.md. Share work summaries only after exact-text authorization. Do not put professional content into the general profile.

Compare with the previous note: evidence-supported progress, reinforcement needs, and unchecked areas. Reuse relevant content next session and agree on brief adapted practice with the student. Do not change skill instructions from this record; proposing/accepting teaching changes follows a separate process. Without persistent storage, offer the note in conversation as a summary to save and state it is unsaved. Work only during active sessions, not in the background.

## Concept cards and documentation study

Save learning notes and operational evidence within the authorized scope. Concept cards and updates require specific proposal acceptance per knowledge-library.md; automatic notes are not approved cards. Propose additions at topic/task close, each three-session review, or same-topic difficulty in two different sessions. Deduplicate reasons and keep deferrals in the checkpoint.

Use documentation-study.md for study paths from sources or study requests. The profile/task may retain the path and card-ID links; do not duplicate counters or grant mastery for reading.

## Teaching observations

With operational recording authorized, link aids to actual evidence per adaptation-contract.md; do not turn declarations into correct answers. Retrieve preferencias.md and only the relevant assessment to adapt the next step. At the three-session review, assessment/chart generation is optional; retain pending data and references. Revalidate derived outputs after record changes. Review adaptation records and copies during corrections or deletion requests.
