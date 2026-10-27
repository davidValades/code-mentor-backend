# Skills

A growing collection of independent agent skills by David Valadés.

Each skill contains its own instructions, references, templates and optional utilities. Source documentation and canonical shortcuts are in English; Code Mentor Backend responds in the learner's requested or conversational language and retains its Spanish shortcut aliases.

## Available skills

| Skill | Purpose | Source version | Documentation |
| --- | --- | --- | --- |
| [Code Mentor Backend](skills/code-mentor-backend/SKILL.md) | Learn to read, implement, refactor and debug C#/.NET backend code with guided practice. | 2.8 | [Guide and shortcuts](docs/code-mentor-backend/README.md) |

Only existing skills are listed. Example ideas are not installed skills or planned commitments.

## Use a skill

Open its guide, then make that skill available through a compatible host. Reading this repository or downloading a package does not prove that the skill is installed or active in a conversation. Capabilities such as voice, filesystem access and persistent storage depend on that host and its permissions.

For Code Mentor Backend, try `/help` or `/learn C# methods` after activating the skill. Spanish aliases such as `/instrucciones` and `/aprender` remain supported; an English shortcut does not change the lesson language.

## Collection layout

| Location | Purpose |
| --- | --- |
| `skills/<name>/` | Self-contained skill instructions and resources. |
| `docs/<name>/` | Public guide, support, privacy, terms and development records for that skill. |
| `tests/<name>/` | Skill-specific checks. |
| `packages/<name>/plugin.json` | Portable packaging metadata for an individual skill. |
| `assets/<name>/` | Distribution artwork for that skill. |
| `dist/<name>/` | Built packages, versioned independently. |
| `tools/build_plugin.py` | Builds one package from its canonical source, without bundling unrelated skills. |

The collection is not a single all-purpose plugin. Build and distribute each skill separately. The original repository's history and older packages are retained; legacy documentation links point to the current guides.

## Build and check

Python 3.11+ is required for the local utilities.

```sh
python tools/build_plugin.py code-mentor-backend
MENTOR_SKILL="$PWD/skills/code-mentor-backend" python -m unittest discover -s tests/code-mentor-backend -q
```

Building does not install, publish or submit a plugin. See the [distribution status](docs/code-mentor-backend/submission-readiness.md) for those separate steps.

## Efficient context

Machine-facing instructions use concise operational prose inspired by Caveman, with selective reference loading and short factual handoffs. User-facing explanations retain each skill's own teaching and language rules. See [authoring guidance](docs/authoring.md) and the [new-skill template](templates/skill/SKILL.md). No extra skill installation or global Caveman mode is required. [Measured context footprint](docs/context-footprint.md) reports document sizes without claiming token or cost savings.

## Data and contributions

Commit instructions, empty templates and synthetic test fixtures only. Keep learner records, work code, financial/personal data and credentials in a separate authorized location. Never use this public repository as a learner's memory.

When adding a skill, give it one canonical source folder, a clear scope, its own guide and validation, and independent package/version metadata. Do not create placeholder folders for hypothetical skills.

## License

[MIT](LICENSE). Author: David Valadés.

