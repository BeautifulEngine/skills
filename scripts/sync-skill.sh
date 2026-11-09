#!/usr/bin/env bash
# Copy a skill folder from its own repo into this plugin, replacing the old copy.
# Usage: scripts/sync-skill.sh <path to the skill folder> <skill name>
# Example: scripts/sync-skill.sh ../company-brief/company-brief company-brief
set -euo pipefail
src="${1:?path to the skill folder (the one with SKILL.md)}"
name="${2:?skill name, e.g. company-brief}"
dest="$(cd "$(dirname "$0")/.." && pwd)/plugins/beautiful-engine/skills/$name"
[ -f "$src/SKILL.md" ] || { echo "No SKILL.md in $src" >&2; exit 1; }
rm -rf "$dest" && mkdir -p "$dest"
(cd "$src" && tar --exclude='__pycache__' --exclude='.DS_Store' --exclude='node_modules' --exclude='README.md' -cf - .) | (cd "$dest" && tar -xf -)
echo "Synced $name from $src"
