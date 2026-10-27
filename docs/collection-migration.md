# Collection migration

The author selected a single collection named `skills`, created by renaming and reorganizing the existing Code Mentor Backend repository. Source and canonical shortcuts are in English; learner conversations follow the learner's language and Spanish aliases remain supported.

## Decisions

- Keep `skills/code-mentor-backend/` as the one canonical skill source.
- Namespace public guides, tests, package metadata and distribution artwork by skill.
- Build one independent portable package per skill; do not install unrelated skills together.
- Keep historic packages and original history; retain old documentation paths as compatibility links.
- Preserve private storage paths, IDs, JSON fields and retry identifiers. Translate explanations without migrating user data.
- Keep all real learner/work records outside the public collection.

## Rollout

Translate and verify the existing skill, rebuild its package, update the existing personal skill and private plugin where authorized, and rename the repository through GitHub settings. Update canonical URLs after the rename is actually verified. Until then the original repository URL remains valid and is used in package metadata.

The collection currently contains only Code Mentor Backend. Other topics mentioned in conversation were examples, not skills to create.

The collection root is no longer a single-plugin installation target. Use a built per-skill archive or the canonical skill folder through a compatible host. Existing installed identities are preserved; adding a skill to this collection does not add it to another skill's package.

## Context-efficiency addition

The author also requested compact internal documents and agent coordination inspired by Caveman, while preserving the tutor's output. This is implemented as a collection authoring policy, a source template and concise per-skill instructions, not an installed global response style. Expanded English sources were checkpointed outside the package before compression.
