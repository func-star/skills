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

There is no CI for skill behavior. Test locally:

```bash
# Symlink into Claude Code's user-level skills dir
ln -s "$PWD/skills/<skill-name>" ~/.claude/skills/<skill-name>

# Open a fresh Claude Code session and invoke
# /<skill-name>
```

In your PR description, include:

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
4. Claude Code version (`claude --version`).
