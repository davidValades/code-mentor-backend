# Weekly learning blocks

The user requested chronological weekly blocks: October 26–November 1, November 2–8, and so on. Maintain these through active-session saves in the existing notebook. No option was selected in the scheduling question; use the stated session-based default. No background automation is created or implied.

## Design

- Add `/week [ISO-week/date]`, Spanish `/semana`, and an ordinary-language route. Default to the current Monday–Sunday calendar week in the learner's known IANA zone; disclose UTC only when no zone is known. Preserve ISO week-year at year boundaries.
- Store derived summaries at `notes/weeks/YYYY-Www.md` and their small index at `notes/weeks/index.md`. Keep original session notes/cards/evidence authoritative. Historical revisions use native history or `notes/history/week-yyyy-www/rNNNN.md`.
- Include dated sessions/work, concepts/explanations, evidence with assistance, unresolved difficulties, teaching aids/feedback, decisions with provenance, accepted-card links and next practice. Separate studied material, declaration, conceptual checks and actual IDE results.
- Assign material by its original occurrence date in the week zone, not file/save/import dates. Split cross-week sessions only by known dated blocks; retain uncertainty for undated material. Future-dated items are plans or data requiring verification, never observed learning. An elapsed calendar week does not prove complete capture or session completion.
- Refresh the affected current week after a verified session close, on `/week`/save request, or when relevant delayed records change it. On resumption, reconcile existing index rows with stale calendar states and known pending/source-affected weeks, including gaps of several weeks. Preserve capture uncertainty and create no empty skipped periods. No message count, new review counter, forced lessons or whole-history reread.
- Read index and relevant session sections only. Keep source identities/revisions and coverage dates. Preserve same week ID, actual creation/update dates and history; no-op retries create no new revision. Never duplicate evidence or promote cards without acceptance.
- Keep the same authorized general/project root and existing read-only/pending fallback. No destination is silently configured and no real learner archive is generated from design/QA.
- Extend the bounded inspector to include current weekly blocks/index, preserving budgets and history exclusions.

## Alternatives

Session-driven summaries reuse existing permission and work in both hosts; selected as the default. A scheduled Monday closure additionally needs a real automation with verified source/destination access. A manually requested report alone would not meet the desired ongoing organization.

## Verification

Regressions cover missing weekly links and unindexed blocks. A baseline/new-skill scenario checks dated grouping, the Madrid midnight boundary, undated/future material, evidence limits, stable identity/history and unchanged state. Validate the installed skill, run the full suite, build 2.11.0 and verify saves in the same personal skill, private plugin and public collection. No public OpenAI approval is implied.
