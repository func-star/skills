# skills

A curated collection of **agent skills** — reusable, model-invokable capabilities packaged as a directory with a `SKILL.md` file.

These skills follow [Anthropic's skill specification](https://docs.claude.com/en/docs/claude-code), which is also adopted by other AI coding agents (Antigravity, Cursor, and others). The same skill directory can be consumed by any compatible agent — just point the agent at it.

## Repository layout

```
.
├── skills/                  # All published skills live here, one folder per skill
│   └── <skill-name>/
│       ├── SKILL.md         # Skill frontmatter + instructions (required)
│       ├── scripts/         # Optional: executable helpers the skill calls
│       └── references/      # Optional: long-form docs loaded on demand
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

To use a skill, copy or symlink its directory into your agent's skills location.

**Claude Code:**
```bash
# User-level (available across all projects)
ln -s "$PWD/skills/<skill-name>" ~/.claude/skills/<skill-name>

# Project-level (current repo only)
ln -s "$PWD/skills/<skill-name>" .claude/skills/<skill-name>
```

**Other agents (Antigravity, Cursor, etc.):** follow your agent's documentation for where it loads skills from — the `SKILL.md` format is the same. If your agent expects a single root `skills/` directory, point it at this repo's `skills/` folder directly.

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
