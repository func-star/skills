# Contributing

Thanks for the interest in contributing.

## Quick start

1. Fork and clone the repo.
2. Create a new skill: `./scripts/new-skill.sh <skill-name>`
3. Edit `skills/<skill-name>/SKILL.md` to fit your workflow. Follow [`docs/SKILL_SPEC.md`](docs/SKILL_SPEC.md).
4. Test the skill locally (see [Testing](#testing)).
5. Open a PR.

## Skill checklist

Before opening a PR, confirm:

- [ ] Directory name is **kebab-case** and matches the `name:` field in frontmatter.
- [ ] `description:` clearly states *when* the skill should be invoked.
- [ ] `SKILL.md` has Goal / Preconditions / Steps / Success criteria / Stop conditions sections.
- [ ] If the skill uses scripts, they are marked executable and documented.
- [ ] You manually tested at least one positive case and one negative case.
- [ ] No secrets, tokens, or absolute paths to personal directories.

## Testing

There is no CI for skill behavior. Test locally against at least one host agent.

**While developing inside this repo**, symlink so edits are live:

```bash
ln -s "$PWD/skills/<skill-name>" ~/.claude/skills/<skill-name>
# Open a fresh session and invoke the skill (e.g. /<skill-name> in Claude Code)
```

**For a one-shot trial of a published skill** (no editing), use the install paths documented in [README.md](README.md#installation) — `npx tiged` is the fastest for arbitrary targets:

```bash
npx tiged func-star/skills/skills/<skill-name> /tmp/test-<skill-name>
```

For other agents (Antigravity, Cursor, …) follow their docs for loading `SKILL.md`-format skills.

In your PR description, include:

- Which host agent(s) you tested in.
- The exact invocations you tested.
- The expected vs observed behavior.
- Any edge cases you confirmed handle correctly.

## Commit conventions

Use conventional commits:

- `feat(skill): add <skill-name>`
- `fix(<skill-name>): <what>`
- `docs(spec): <what>`
- `chore: <what>`

Keep commits focused — one logical change per commit.

## PR review

PRs need at least one approval. Reviewers will check:

- Skill spec compliance ([`docs/SKILL_SPEC.md`](docs/SKILL_SPEC.md))
- Clarity of the description field (does the trigger make sense?)
- That tested scenarios are documented
- No leaked secrets or personal info

## Reporting issues

For broken or misbehaving skills, open an issue with:

1. Skill name.
2. Exact invocation.
3. Expected vs actual behavior.
4. Host agent and version (e.g. `claude --version` for Claude Code).
