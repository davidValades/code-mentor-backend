# Check memory end to end

This checks storage and continuity, not learning effectiveness or automatic cross-chat memory. Installing the skill does not configure a record destination. Keep work data in its authorized project scope.

## One-time setup

1. Request `/status`. Confirm the inspected instruction source/version and the actual authorized record identity. Host activation may remain unverified.
2. Agree on a private persistent destination and operational recording permission if not configured. Reading alone does not establish creation/replacement permission.
3. Use a short real learning task. Predict or explain one example in your own words. Reserve IDE achievements for actual observed implementation/debugging.

## Save, revise and reopen

1. Finish a meaningful block and request `/save`. Check the receipt: saved destinations/identities, versions and remaining pending items. Activity dates and actual save times are separate; unknown save time stays unknown.
2. Request `/notes` and inspect the same session's note, its topic link and provenance. Continue the topic, then save an actual addition. The same note ID must remain; revision/history must advance without creating a duplicate session or achievement.
3. Request `/status`, `/memory-audit` and `/map [current goal]`. Check that map links open the correct authorized note/card and that studied material is separate from demonstrated evidence. Use `/week` to verify its occurrence-date grouping, source links and weekly coverage without creating a second progress record. An empty bounded mechanical audit is not a full semantic guarantee.
4. Open another conversation in an environment that can access that same destination. Activate/request Code Mentor Backend and supply the record identity or continuity package; never assume it inherits context. Ask for `/status`, then `/resume`. Compare the retrieved note ID/revision and exact pending next action.
5. Reapply the identical pending batch only if needed. Existing retry IDs must prevent duplicate operations. A saved derivative failure must not replay already-saved learning evidence.

If the second environment cannot access the destination, a truthful limitation and self-contained continuity package is the expected result. If original-file replacement fails, it must not silently create a suffixed copy or claim the original changed. While driving, defer all screen/file actions until stopped.

## Report display check

Open the generated private `progress/index.html` in a permitted host. On desktop and a narrow/mobile screen, check day selection, topic/date/assistance filters, reset, keyboard arrows, calendar table fallback, visible legends and details. Compare a selected day to the actual record. Verify that concept milestones remain historical when the date filter changes. Use `/map`'s linked table when Mermaid is unavailable.

Actual browser layout, CSP enforcement, host activation and the real learner's cross-chat access require observation in that host. Computational DOM tests and synthetic saves do not establish these properties.

## Automated isolated verification

From the collection root:

```sh
MENTOR_SKILL=/absolute/path/to/installed/code-mentor-backend \
python -m unittest discover -s tests/code-mentor-backend -q
```

The continuity case starts separate Python processes to initialize an isolated synthetic root, save/reopen/retry an immutable profile, generate a clearly marked demo report, inspect it without mutation and detect a missing referenced file. The inspection cases cover bounded scans, unsafe paths, incomplete coverage and truthful timestamps. Fresh-agent notebook/map checks are recorded separately in release verification. None of these cases is personal learning data or proof of teaching effectiveness.
