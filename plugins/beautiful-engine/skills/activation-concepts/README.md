# Activation Concepts

Develops three experiential activation concepts for a brand at a venue, event or public space and delivers them as a designed 16:9 concept deck PDF with presenter notes. Each concept gets the big idea, the guest journey step by step, a simple floor plan diagram, materials and fabrication notes, tech, staffing, timeline, a budget range, risks and permits, and how success is measured.

## Install

**Claude app (web, desktop):** turn on Settings > Capabilities > "Code execution and file creation". Then go to Customize > Skills, click "+", then "+ Create skill" > "Upload a skill", and upload `activation-concepts.zip` as is (don't unzip it).

**Claude Code:** install the whole Beautiful Engine collection:

```bash
claude plugin marketplace add BeautifulEngine/skills
claude plugin install beautiful-engine@beautiful-engine
```

Then use `/beautiful-engine:activation-concepts`, or ask in plain words.

## Usage

```
/activation-concepts <brand> at <venue or event> [budget range] [audience] [goal]
```

Plain requests work too:

- "Three activation concepts for Patagonia at Outside Lands, budget $150–250K."
- "Pop-up ideas for a skincare launch in a 1,200 sq ft SoHo storefront, two weeks."
- "We have a 20×20 booth at CES for a robotics startup. Give me concepts."
- "Here's the client brief (attached). Turn it into three activation concepts."
- Add "one concept" for a single concept in depth, or "rough" for a quick 6-slide version.

If the person has a brief, follow it exactly and quote its objectives back on the second slide. If key facts are missing (budget, footprint, dates, audience), pick sensible defaults, list them on the brief slide as assumptions, and say so in the reply.

**Files.** `<skill-dir>` means this skill's folder, the one holding this SKILL.md. Templates are in `assets/`, scripts in `scripts/`, and the shared PDF steps (fonts, colors, render, check) are in `references/rendering.md`.

## Made by Beautiful Engine

Made by [Beautiful Engine](https://www.beautifulengine.com), a creative studio in Los Angeles. Questions, ideas, or something broke? [Open an issue](https://github.com/BeautifulEngine/skills/issues/new). More skills: [github.com/BeautifulEngine/skills](https://github.com/BeautifulEngine/skills).

