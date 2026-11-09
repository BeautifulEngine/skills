#!/usr/bin/env bash
# Copy a built skill into its own repo checkout (BeautifulEngine/<skill>): the skill folder,
# its zip, a landing README, LICENSE, .gitignore, and its demo GIF, preview and sample PDF
# (docs/<skill>/ and examples/<skill>/ in this repo). Run scripts/build.sh first.
# Usage: scripts/publish-standalone.sh <skill> <path to that repo's checkout>
# Example: scripts/publish-standalone.sh build-spec ../build-spec
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
name="${1:?skill name}"
dest="${2:?path to the checkout of the skill repo}"
src="$ROOT/plugins/beautiful-engine/skills/$name"
[ -f "$src/SKILL.md" ] || { echo "No skill named $name" >&2; exit 1; }
[ -f "$ROOT/dist/$name.zip" ] || { echo "Run scripts/build.sh first" >&2; exit 1; }
mkdir -p "$dest"
rm -rf "$dest/$name"
cp -r "$src" "$dest/$name"
find "$dest/$name" -name '__pycache__' -prune -exec rm -rf {} +
cp "$ROOT/dist/$name.zip" "$dest/$name.zip"
cp "$ROOT/LICENSE" "$dest/LICENSE"
printf '__pycache__/\n*.pyc\nnode_modules/\n.DS_Store\n' > "$dest/.gitignore"
for kind in docs examples; do
  if [ -d "$ROOT/$kind/$name" ]; then rm -rf "$dest/$kind"; mkdir -p "$dest/$kind"; cp "$ROOT/$kind/$name"/* "$dest/$kind/"; fi
done
python3 "$ROOT/scripts/make_repo_readme.py" "$src" > "$dest/README.md"
echo "published $name to $dest"
