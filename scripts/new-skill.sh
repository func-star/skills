#!/usr/bin/env bash
# new-skill.sh — scaffold a new skill from the template.
#
# Usage:
#   ./scripts/new-skill.sh <skill-name>
#
# Example:
#   ./scripts/new-skill.sh my-pre-merge-audit
#
# Exit codes:
#   0  success
#   1  bad arguments
#   2  skill already exists

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 <skill-name>" >&2
  exit 1
fi

SKILL_NAME="$1"

# Validate kebab-case, lowercase, no leading/trailing dash.
if [[ ! "$SKILL_NAME" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "error: skill name must be lowercase kebab-case (got: $SKILL_NAME)" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATE="$ROOT/templates/SKILL_TEMPLATE.md"
TARGET_DIR="$ROOT/skills/$SKILL_NAME"
TARGET_FILE="$TARGET_DIR/SKILL.md"

if [[ -e "$TARGET_DIR" ]]; then
  echo "error: skill already exists at $TARGET_DIR" >&2
  exit 2
fi

if [[ ! -f "$TEMPLATE" ]]; then
  echo "error: template not found at $TEMPLATE" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"
sed "s/__SKILL_NAME__/$SKILL_NAME/g" "$TEMPLATE" > "$TARGET_FILE"

echo "Created $TARGET_FILE"
echo
echo "Next steps:"
echo "  1. Edit $TARGET_FILE — fill in the description and steps."
echo "  2. Test locally:"
echo "       ln -s \"$TARGET_DIR\" ~/.claude/skills/$SKILL_NAME"
echo "  3. Invoke in Claude Code: /$SKILL_NAME"
