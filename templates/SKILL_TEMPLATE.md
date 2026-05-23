---
name: __SKILL_NAME__
description: __ONE_SENTENCE_DESCRIBING_WHEN_TO_INVOKE_THIS_SKILL__
# allowed-tools:    # uncomment to restrict tools
#   - Read
#   - Bash
#   - Edit
# model: sonnet     # uncomment to pin a model family
---

## Goal

State in one sentence what this skill accomplishes.

## Preconditions

- List things that must be true before this skill runs.
- e.g. "Current directory is a git repository."
- e.g. "`gh` CLI is authenticated."

## Steps

1. First action — be concrete about which tool to use and what arguments.
2. Second action.
3. Third action.

## Success criteria

Describe what the final state looks like when this skill is done. The model uses this to know when to stop.

## Stop conditions

Describe situations where the skill should abort and report back to the user rather than continue:

- e.g. "If the working tree is dirty, stop and ask the user to commit or stash first."
- e.g. "If a required env var is missing, stop and surface the missing key."

## Notes

Anything else the model should know — edge cases, prior incidents, links to references.
