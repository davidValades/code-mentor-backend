# Weekly learning history

Use `/week`, `/semana` or an ordinary request for a weekly recap. The default organizes your authorized study record into Monday–Sunday blocks in your known time zone.

| Example ISO week | Local period | Derived summary |
| --- | --- | --- |
| 2026-W44 | October 26–November 1, 2026 | `notes/weeks/2026-W44.md` |
| 2026-W45 | November 2–8, 2026 | `notes/weeks/2026-W45.md` |

`notes/weeks/index.md` links the periods, source coverage, calendar state and summary revisions. All files stay in your agreed private general or project root, outside this repository. Existing session notes remain in `notes/sessions/`; older notes are not moved or copied into another memory database.

## What a block contains

- Sessions/tasks and concepts actually covered, with links to detailed notes, examples and vocabulary corrections.
- What you demonstrated, with original evidence dates, modality, help and outcome; studied material and declarations remain distinct.
- Difficulties, unfinished ideas, corrected errors and what still needs checking.
- Teaching aids used, your clarity/effort feedback and actual outcomes without inferring a fixed learning style.
- Task decisions with provenance, accepted-card links, pending proposals and the next small practice/review.
- Week/date range, time zone, source identities/revisions, cutoff, coverage gaps and document history.

The block is a compact overview with linked detail. It does not copy the full conversation, create achievements or turn exposure into independent implementation. General summaries exclude company details; work material remains in its authorized project scope.

## When it updates

After a verified session close, the tutor refreshes only the affected weekly block/index when there is an actual change. `/week` or a relevant save/history request can also refresh it. On resumption, it checks the compact weekly index for stale calendar states and known pending/source-affected weeks. If you stop in W44 and return in W48, W44 becomes elapsed while retaining its coverage gaps; it creates no empty skipped weeks or new learning sessions.

The same week keeps its ID and creation date. Real updates preserve prior revisions through native history or `notes/history/week-yyyy-www/`. A repeated request with unchanged material creates no new revision. Failed derived updates stay pending without replaying saved evidence or duplicating notes.

The default operates during active sessions. It does not run every Sunday/Monday while chats are closed. A separately requested scheduled automation requires real access to the same record and destination; installing the skill creates none. Updating this feature does not configure a learner's storage automatically.

## Dates and uncertainty

Original occurrence dates determine the week, not saving/import dates or file creation times. Convert to the selected IANA zone before grouping; an event late Sunday in UTC may already be Monday in Madrid. ISO week-years can differ from calendar years around New Year.

Known cross-week session blocks may link to the same source note in different weeks without duplicating events. Undated material stays unassigned. Future-dated entries are plans or pending verification, never observed learning. Calendar state is upcoming, in_progress or elapsed; elapsed does not mean full capture or a completed learning session.

Without persistent write access, the tutor prepares a clearly pending weekly draft in the existing continuity package. It does not assume another chat can read it. Ask `/status` to inspect the actual destination and `/memory-audit` to check current weekly links/indexing within the same bounded audit.

See the [operational weekly contract](../../skills/code-mentor-backend/references/weekly-learning.md), [study notebook](README.md#your-private-study-notebook), [memory check](memory-check.md), and [privacy](privacy.md).
