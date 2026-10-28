# Context footprint

Measured 2026-10-28 against the expanded English 2.8 checkpoint. Counts are whitespace-separated words and UTF-8 bytes, not tokenizer usage, cost, hidden reasoning or latency. This is a complete-file comparison, not proof every session loads every file.

| Scope | Before words | After words | Change |
| --- | ---: | ---: | ---: |
| References | 12764 | 9804 | -23.2% |
| SKILL.md and references | 14546 | 11641 | -20.0% |

The installed-source total includes the new context-efficiency paragraph. Repository-only authoring guidance and templates are separate: they are not bundled as an extra runtime skill.

Protected-content checks compare all reference headings, fenced examples, inline code and Markdown links verbatim. Semantic review and a synthetic learner response supplement those checks; none is evidence of student learning.

No upstream Caveman runtime, hooks, provider calls or telemetry were installed. The tutor's output format and permissions remain in force.

These are historical version-2.8 measurements. Version 2.9 adds a routed progress reference and executable/report assets; the percentages above are not a new whole-release or token-cost measurement.
