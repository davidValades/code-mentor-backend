# Inspecting and reviewing memory

## /status — visible state

Read the authorized root or service identities and latest accessible checkpoint/receipt. Do not create a destination, probe unrelated roots or perform a write test for a status request. Without a configured root, say "not configured" and keep learning available. With local schema 2 and Python, run:

```sh
python scripts/mentor_inspect.py --root /absolute/authorized/root status
```

Return a concise table with these fields:

| Field | Required distinction |
| --- | --- |
| Instructions | Inspected version and exact source; say whether host activation is verified or unknown. Repository/personal-package reading alone proves no active version in another chat. |
| Record | Actual authorized destination/identity, scope, revision and observation date. |
| Capabilities | Reading verified; creation/replacement/persistence only from actual service results. A read or prior write in another environment proves no current write access. |
| Saved | Latest accessible successful write receipt and verified document identity/version. If actual save time is absent, say unknown; preserve activity timestamps separately. |
| Pending | Accessible batch/checkpoint/conversation items and coverage limits. Missing access does not mean nothing is pending. |
| Next action | One useful action, or no action needed within the verified scope. |

The utility's `documents.available` means a safe referenced file exists, not that its content was independently verified. `last_receipt_revision` identifies a stored operation result; `actual_last_save_at=null` means the schema records no actual write timestamp. Do not substitute filesystem modification times or the inspection time. A checkpoint's pending question is not a complete unsaved-change queue. Inspect known batch receipts separately using existing file tools; do not enumerate an entire workspace.

With Library/Markdown alone, use returned identities, native versions and actual receipts; keep calculated fields unavailable. Status requires no mode change or recurring permission request. During driving, report orally and defer screen actions.

## /memory-audit — review, not repair

Operate only on the agreed scope. Begin with indexes/current checkpoint; audit on request, for contradictions/broken retrieval, or as useful during an existing three-session review. No additional session counter or background scan.

For local schema 2 and Python:

```sh
python scripts/mentor_inspect.py --root /absolute/authorized/root audit
```

The utility is read-only, including no write lock. It validates state, checks referenced document existence, current note/card links and indexing, whitespace-normalized duplicate candidates, and progress HTML revision/digest. It flags known writer locks, pending-file candidates and unreferenced versioned documents without opening pending contents, calling a lock stale or removing anything. Coverage is bounded to 200 text-file reads, 2 MiB total, 256 KiB per file and 1,000 metadata entries in known directories. Failed decoding still consumes the read budget. It does not follow unsafe paths, fetch external links, inspect history, validate anchors, parse every Markdown dialect or prove semantic correctness. Skipped/unreadable files make coverage incomplete. Index links are relative to their index file; code-formatted paths, optional quoted titles and angle-bracket destinations are recognized. Table-only paths without links/code require manual review. Duplicates are candidates, never an instruction to merge.

Then review only relevant flagged/retrieved sections for meaning:

1. Compare conflicting statements against current primary sources/project versions. Separate incorrect facts, different contexts and unknown reasons.
2. Compare learning claims with exact evidence, assistance, dates and modality. A studied note or broad-topic status proves no specific card competency.
3. Check relevant index IDs/revisions, prerequisite cycles and references. Keep explicit relationships separate from proposed teaching routes.
4. Inspect known pending batches and affected version history where needed. Record what could not be checked.

Show findings as **finding / source / impact / proposed action**, followed by inspected scope and remaining checks. An empty mechanical result means no mechanical finding in that bounded scope, not "all memory is correct." Do not treat absent optional folders as corrupted memory or invented pending tasks.

Apply no changes from the audit request alone. Offer one grouped correction proposal. After the user requests the correction, preserve history and use existing authorized write/retry rules; accepted-card changes still need exact-content acceptance. Do not delete duplicates, rewrite evidence, create achievements or activate teaching rules automatically. Refresh affected derived indexes/reports after verified corrections. Invalid state stays unchanged; explain the blocker and preserve pending work.
