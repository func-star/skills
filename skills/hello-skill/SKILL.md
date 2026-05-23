---
name: hello-skill
description: A minimal example skill that prints a greeting and demonstrates the SKILL.md format. Invoke when you want to verify your skills directory is wired up correctly.
---

## Goal

Print a friendly greeting and confirm the skill loader is working.

## Preconditions

- None.

## Steps

1. Output a single line: `Hello from hello-skill — your Claude Code skills directory is wired up correctly.`
2. Report the current working directory to the user.

## Success criteria

The user sees the greeting and the current working directory in the response.

## Stop conditions

This skill should never fail. If for some reason the current working directory cannot be determined, output the greeting alone and note the issue.

## Notes

This is the canonical example skill. Use it as a sanity check after setting up the repo, and as the simplest reference for the `SKILL.md` structure.
