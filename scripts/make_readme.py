#!/usr/bin/env python3
"""Write a skill's README.md (for people who download its zip) from its SKILL.md."""
import re
import sys
from pathlib import Path

d = Path(sys.argv[1])
md = (d / "SKILL.md").read_text()
fm = md.split("---")[1]
name = re.search(r"^name:\s*(.+)$", fm, re.M).group(1).strip()
desc = re.search(r"^description:\s*(.+)$", fm, re.M).group(1).strip()
desc = re.split(r"\s+(?:Usage - |Use when )", desc)[0]
title = re.search(r"^# (.+)$", md, re.M).group(1).strip()
usage = re.search(r"^## Usage\n(.*?)(?=^## )", md, re.M | re.S)
usage = usage.group(1).strip() if usage else ""
print(f"""# {title}

{desc}

## Install

**Claude app (web, desktop):** turn on Settings > Capabilities > "Code execution and file creation". Then go to Customize > Skills, click "+", then "+ Create skill" > "Upload a skill", and upload `{name}.zip` as is (don't unzip it).

**Claude Code:** install the whole Beautiful Engine collection:

```bash
claude plugin marketplace add BeautifulEngine/skills
claude plugin install beautiful-engine@beautiful-engine
```

Then use `/beautiful-engine:{name}`, or ask in plain words.

## Usage

{usage}

## Made by Beautiful Engine

Made by [Beautiful Engine](https://www.beautifulengine.com), a creative studio in Los Angeles. Questions, ideas, or something broke? [Open an issue](https://github.com/BeautifulEngine/skills/issues/new). More skills: [github.com/BeautifulEngine/skills](https://github.com/BeautifulEngine/skills).
""")
