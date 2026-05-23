# claude-skills

A curated collection of [Claude Code](https://docs.claude.com/en/docs/claude-code) skills.

Skills are reusable, model-invokable capabilities packaged as a directory with a `SKILL.md` file. Each skill defines a focused workflow that Claude can trigger via `/skill-name`.

## Repository layout

```
.
├── skills/                  # All published skills live here, one folder per skill
│   └── <skill-name>/
│       ├── SKILL.md         # Skill frontmatter + instructions (required)
│       ├── scripts/         # Optional: executable helpers the skill calls
│       └── references/      # Optional: long-form docs the skill reads on demand
├── templates/
│   └── SKILL_TEMPLATE.md    # Starting point for new skills
├── docs/
│   └── SKILL_SPEC.md        # Authoring spec and conventions
├── scripts/
│   └── new-skill.sh         # Scaffold a new skill from the template
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Installation

To use a skill locally, symlink or copy it into your Claude Code skills directory:

```bash
# User-level (available across all projects)
ln -s "$PWD/skills/<skill-name>" ~/.claude/skills/<skill-name>

# Project-level (available only in the current repo)
ln -s "$PWD/skills/<skill-name>" .claude/skills/<skill-name>
```

Then invoke it in Claude Code with `/<skill-name>`.

## Creating a new skill

```bash
./scripts/new-skill.sh my-new-skill
```

This copies the template into `skills/my-new-skill/` and prefills the frontmatter. Then edit `SKILL.md` to fit the workflow.

See [`docs/SKILL_SPEC.md`](docs/SKILL_SPEC.md) for the full authoring guide.

## Contributing

Contributions welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a PR.

## License

[MIT](LICENSE)
