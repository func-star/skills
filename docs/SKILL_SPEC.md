# Skill authoring spec

This document defines the conventions every skill in this repository must follow.

Skills here follow [Anthropic's skill specification](https://docs.claude.com/en/docs/claude-code) — the same format consumed by Claude Code, Antigravity, Cursor, and other compatible agents. Nothing in this spec is agent-specific; if a rule below references Claude Code as an example, it applies equally to any agent that loads `SKILL.md`-format skills.

## 1. Directory layout

Each skill is a directory under `skills/` whose name matches the skill's invocation slug:

```
skills/<skill-name>/
├── SKILL.md         # required
├── scripts/         # optional: executable helpers
├── references/      # optional: long-form docs loaded on demand
└── assets/          # optional: static files (images, templates, etc.)
```

- `<skill-name>` must be **kebab-case**, lowercase, ASCII-only, and unique within the repo.
- The invocation slug is `<skill-name>`. How the user triggers it depends on the host agent (e.g. `/<skill-name>` in Claude Code).

## 2. `SKILL.md` format

Every skill **must** have a `SKILL.md` at its root with YAML frontmatter and a Markdown body.

### Required frontmatter

```yaml
---
name: <skill-name>            # must match the directory name
description: <one sentence>   # when to trigger this skill (used by the model to decide)
---
```

### Optional frontmatter

```yaml
allowed-tools:                # restrict which tools the skill may call
  - Read
  - Bash
  - Edit
model: sonnet                 # pin to a specific model family (sonnet | opus | haiku)
```

If `allowed-tools` is omitted, the skill inherits the parent session's tool set.

### Body

The body is the instructions the model receives when the skill is invoked. Treat it as a system prompt for a focused sub-task. Follow these rules:

- **Open with the goal in one sentence.** What does the skill accomplish?
- **List preconditions explicitly.** What must be true before running? (e.g. "must be inside a git repo")
- **Define the step sequence.** Numbered steps the model should follow.
- **Specify the success criteria.** How does the model know it's done?
- **State stop conditions.** When should the skill abort and report back to the user?

Skills are not free-form prose — they are operational playbooks. Be concrete.

## 3. Description field rules

The `description` is the single most important piece of metadata: it's what the model reads to decide whether to invoke the skill. Write it so a future Claude (with no other context) can tell whether the skill applies.

- Lead with the verb: `"Deploy …"`, `"Audit …"`, `"Generate …"`.
- Name the trigger conditions: *when* should this skill fire?
- Keep it under ~200 characters.
- Avoid vague words like "helps with" or "manages" — say what it does.

**Good:** `"Run a pre-merge audit of the current branch: check for failing tests, missing types, and unstaged files. Use before opening a PR."`

**Bad:** `"Helps with PRs."`

## 4. Scripts and references

- **`scripts/`** — executable helpers. Mark them executable (`chmod +x`) and invoke from `SKILL.md` with the absolute path `${SKILL_DIR}/scripts/<name>`. Document inputs and exit codes in a comment at the top.
- **`references/`** — long-form documentation the skill references but doesn't need loaded by default. Have `SKILL.md` instruct the model to `Read references/<name>.md` only when it hits a specific condition. This keeps the skill's initial context small.

## 5. Versioning

This repo uses **rolling skills** — no version pins. Breaking changes to a skill go through:

1. Open an issue describing the breakage.
2. Update `SKILL.md` and bump the `last-updated` date in a comment if helpful.
3. Note the breaking change in the commit message and `CHANGELOG.md` (if present).

If a skill becomes obsolete, move it to `skills/_archive/` rather than deleting — history matters.

## 6. Testing a skill before merging

There is no automated test harness for skills. Before merging:

1. Load the skill into at least one host agent (e.g. symlink into `~/.claude/skills/<skill-name>` for Claude Code).
2. Start a fresh session in that agent.
3. Invoke the skill and verify it does what its description claims.
4. Try at least one **negative case** — a situation where the skill should refuse or abort.

Document the test scenarios — and which agent(s) you tested against — in the PR description.

## 7. Style conventions

- Markdown headings start at `##` in the body (frontmatter handles the title).
- Use fenced code blocks with language tags.
- Prefer imperative voice: *"Run X"*, not *"You should run X"*.
- No emojis unless the skill's output specifically needs them.
- Wrap long lines at ~100 chars where reasonable; don't hard-wrap prose.
