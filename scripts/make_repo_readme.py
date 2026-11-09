#!/usr/bin/env python3
"""Write the landing README for a skill's own GitHub repo (BeautifulEngine/<skill>) from its SKILL.md."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAMPLES = json.loads((ROOT / "tools" / "samples" / "samples.json").read_text())

PAIRS = {
    "application-kit": ["company-brief", "case-study"],
    "case-study": ["application-kit", "company-brief"],
    "sponsorship-pitch": ["company-brief", "activation-concepts", "project-quote"],
    "activation-concepts": ["sponsorship-pitch", "build-spec", "project-quote"],
    "project-quote": ["activation-concepts", "build-spec"],
    "build-spec": ["activation-concepts", "project-quote", "print-listing-kit"],
    "brand-snapshot": ["company-brief", "sponsorship-pitch"],
    "print-listing-kit": ["build-spec", "brand-snapshot"],
}

d = Path(sys.argv[1])
name = d.name
md = (d / "SKILL.md").read_text()
fm = md.split("---")[1]
desc = re.search(r"^description:\s*(.+)$", fm, re.M).group(1).strip()
what = re.split(r"\s+(?:Usage - |Use when )", desc)[0]
when = re.search(r"Use when (.+?)(?:\s+Usage - |$)", desc)
when = when.group(1).rstrip(".") if when else ""
title = re.search(r"^# (.+)$", md, re.M).group(1).strip()
intro = md.split(f"# {title}", 1)[1].split("\n## ", 1)[0].strip()
usage = re.search(r"^## Usage\n(.*?)(?=^## )", md, re.M | re.S)
usage = usage.group(1).strip() if usage else ""


def tree(root):
    lines = [f"{root.name}/"]
    for sub in ["SKILL.md", "assets", "scripts", "references"]:
        p = root / sub
        if p.is_file():
            lines.append(f"├── {sub}")
        elif p.is_dir():
            files = sorted(x.name for x in p.iterdir() if x.is_file())
            lines.append(f"├── {sub}/  {', '.join(files)}")
    return "\n".join(lines)


def label(n):
    return " ".join(w.capitalize() for w in n.split("-"))


how = ("PDFs are built from HTML templates, colored and typeset with the right brand, rendered by headless Chrome, then checked "
       "for fonts, text contrast and leftover blanks before delivery. Anything with numbers in it is calculated by a script, not estimated.")
if name == "print-listing-kit":
    how = ("Listings are written from the search terms and comparable models Claude finds on each marketplace, then checked by "
           "`listing_check.py` against title and tag limits and your list of trademark terms before you paste them.")

sample = SAMPLES.get(name)
visuals = ""
if sample:
    pages = ", ".join(c[0].lower() + c[1:] for c in sample["preview"]["captions"])
    who = ("a snapshot of beautifulengine.com" if name == "brand-snapshot"
           else "fictional names and figures")
    visuals = (f"![Pages from a sample {title}: {pages}](docs/preview.png)\n\n"
               f"**See the full sample:** [{sample['pdf']}](examples/{sample['pdf']}) ({who})\n")
gif = (f"![Animated demo: example requests typed into Claude, each followed by what the {title} skill makes](docs/how-to-ask.gif)\n\n"
       if (ROOT / "docs" / name / "how-to-ask.gif").exists() else "")

pairs = "\n".join(f"- [{label(p)}](https://github.com/BeautifulEngine/{p})" for p in PAIRS.get(name, []))

print(f"""# {title}

{intro}

**What you get:** {what}

{visuals}
Made by Beautiful Engine · [beautifulengine.com](https://www.beautifulengine.com) · [Questions or ideas? Open an issue](https://github.com/BeautifulEngine/{name}/issues/new)

## Install

### Claude app (web or desktop)

1. Download **[{name}.zip]({name}.zip)** from this repo (open the file, then use the download button). Don't unzip it.
2. Turn on **Settings > Capabilities > "Code execution and file creation"**.
3. Go to **Customize > Skills**, click **+**, then **+ Create skill > Upload a skill**, and upload the zip.
4. Start a new chat and ask in plain words. Claude picks the skill up on its own.

> GitHub's green "Code > Download ZIP" button won't work for this; it wraps everything in an extra folder. Use `{name}.zip`.

### Claude Code

As part of the Beautiful Engine collection (you get updates and the other skills):

```bash
claude plugin marketplace add BeautifulEngine/skills
claude plugin install beautiful-engine@beautiful-engine
```

Then use `/beautiful-engine:{name}`, or ask in plain words. Or install just this one:

```bash
git clone https://github.com/BeautifulEngine/{name}.git
mkdir -p ~/.claude/skills && cp -r {name}/{name} ~/.claude/skills/
```

Then use `/{name}`.

## Usage

{gif}{usage}

## When Claude uses it

{when[0].upper() + when[1:] if when else ""}.

## How it works

```
{tree(d)}
```

{how}

## Works well with

{pairs}
- [All Beautiful Engine skills](https://github.com/BeautifulEngine/skills)

## Made by Beautiful Engine

{title} is made by [Beautiful Engine](https://www.beautifulengine.com), a creative studio in Los Angeles working across brand, experiential and interactive design.

- **Website:** [beautifulengine.com](https://www.beautifulengine.com)
- **Questions, ideas, or something broke?** [Open an issue](https://github.com/BeautifulEngine/{name}/issues/new) and describe what you asked for and what happened.

This repo is published from [BeautifulEngine/skills](https://github.com/BeautifulEngine/skills); changes are made there and copied here.

## License

MIT. See [LICENSE](LICENSE).
""")
