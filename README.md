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

## Skills index

| Skill | What it does |
|---|---|
| [`write-ai-article`](skills/write-ai-article/) | Generate a Chinese-language AI technical article following the in-repo style guide (plain narrative, inline citations, short sentences, diagrams at cognitive-load peaks). Ready to drop into a book/blog repo. |
| [`generate-article-image`](skills/generate-article-image/) | Generate hand-drawn / isometric infographic illustrations via the Gemini image API ("Nano Banana"). Pairs with `write-ai-article`. Requires `GEMINI_API_KEY`. |

## Installation

Three install paths, pick the one that matches your agent.

### Option A — `npx skill` (CodeBuddy, one-shot)

The community [`skill`](https://www.npmjs.com/package/skill) CLI fetches a skill folder from GitHub and writes it into `.codebuddy/skills/<name>` of the current directory. It hardcodes its source to `vercel-labs/agent-skills`; point it at this repo with the `SKILL_BASE_URL` env var:

```bash
SKILL_BASE_URL=https://github.com/func-star/skills/tree/main \
  npx skill skills/write-ai-article
```

Note the syntax: `npx skill skills/<name>` — there is no `add` subcommand. To make it permanent, put the export in your shell rc:

```bash
export SKILL_BASE_URL=https://github.com/func-star/skills/tree/main
# then just:
npx skill skills/generate-article-image
```

Target is fixed at `.codebuddy/skills/`, so this path is most useful for CodeBuddy users. For Claude Code / Cursor / Antigravity, see Option B.

### Option B — `npx tiged` (any agent, custom target)

[`tiged`](https://github.com/tiged/tiged) is a generic GitHub subtree fetcher with no opinions about the target directory:

```bash
# Claude Code — user-level (all projects see the skill)
npx tiged func-star/skills/skills/write-ai-article ~/.claude/skills/write-ai-article

# Claude Code — project-level (current repo only)
npx tiged func-star/skills/skills/write-ai-article .claude/skills/write-ai-article

# Any other agent — substitute your agent's skills directory
npx tiged func-star/skills/skills/write-ai-article <your-agent-skills-dir>/write-ai-article
```

This is the recommended path for non-CodeBuddy users.

### Option C — clone + symlink (track upstream)

If you want to pull updates as the repo evolves:

```bash
git clone git@github.com:func-star/skills.git ~/repos/skills
ln -s ~/repos/skills/skills/write-ai-article    ~/.claude/skills/write-ai-article
ln -s ~/repos/skills/skills/generate-article-image ~/.claude/skills/generate-article-image
```

A future `git pull` in `~/repos/skills` updates every installed skill at once.

### Post-install: scripts and the executable bit

GitHub raw downloads do not preserve the executable bit. Skills that bundle `scripts/` (e.g. `generate-article-image`) work fine because every `SKILL.md` here invokes its helpers via `python <script>` rather than `./<script>`. If you ever want to call a helper directly, run `chmod +x <skill-dir>/scripts/*.py` once after install.

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
