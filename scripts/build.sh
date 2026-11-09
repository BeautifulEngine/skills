#!/usr/bin/env bash
# Copy the shared scripts, stylesheets and references into every skill, write each
# skill's README, and build dist/<skill>.zip for the Claude app.
# Run from anywhere after editing anything in shared/ or a skill.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SK="$ROOT/plugins/beautiful-engine/skills"
mkdir -p "$ROOT/dist"
for d in "$SK"/*/; do
  name="$(basename "$d")"
  [ "$name" = "company-brief" ] && continue   # lives in its own repo; sync it with sync-skill.sh
  mkdir -p "$d/scripts" "$d/assets" "$d/references"
  cp "$ROOT"/shared/scripts/* "$d/scripts/"
  cp "$ROOT"/shared/assets/*.css "$d/assets/"
  cp "$ROOT"/shared/references/rendering.md "$d/references/"
  if grep -q 'brand-extraction.md' "$d/SKILL.md"; then cp "$ROOT/shared/references/brand-extraction.md" "$d/references/"; fi
  python3 "$ROOT/scripts/make_readme.py" "$d" > "$d/README.md"
  find "$d" -name '__pycache__' -prune -exec rm -rf {} +
  rm -f "$ROOT/dist/$name.zip"
  (cd "$SK" && zip -rq "$ROOT/dist/$name.zip" "$name" -x '*.DS_Store' '*/node_modules/*')
  echo "built dist/$name.zip"
done
