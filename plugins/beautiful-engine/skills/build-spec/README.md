# Build Spec

Turns a design, sketch, photo, CAD file or description of something to make into a fabrication package PDF plus a bill of materials CSV - overview diagram, parts and cut lists, sheet counts, file checklists and starting settings for laser cutting, 3D printing and CNC, hardware, a power budget with battery runtime, tools, numbered build steps with checkpoints, finishing, install and teardown, safety, vendors and a timeline. Totals come from a calculator script.

## Install

**Claude app (web, desktop):** turn on Settings > Capabilities > "Code execution and file creation". Then go to Customize > Skills, click "+", then "+ Create skill" > "Upload a skill", and upload `build-spec.zip` as is (don't unzip it).

**Claude Code:** install the whole Beautiful Engine collection:

```bash
claude plugin marketplace add BeautifulEngine/skills
claude plugin install beautiful-engine@beautiful-engine
```

Then use `/beautiful-engine:build-spec`, or ask in plain words.

## Usage

```
/build-spec <what you're building> [size] [where it will live] [tools you have] [budget] [deadline]
```

Plain requests work too:

- "Build spec for an 8 ft tall LED-lit sign that says OPEN LATE, for an outdoor festival, running off a battery."
- "Here's a sketch (attached) of a DJ booth facade. Make a cut list for 1/2 in plywood."
- "Parts list and build plan for a 3D printed lamp, 300 mm tall, on a Bambu H2D."
- "Fabrication plan for this booth element from our activation deck."
- Add "quick" for a two-page version: BOM, cut list and build steps only.

## Made by Beautiful Engine

Made by [Beautiful Engine](https://www.beautifulengine.com), a creative studio in Los Angeles. Questions, ideas, or something broke? [Open an issue](https://github.com/BeautifulEngine/skills/issues/new). More skills: [github.com/BeautifulEngine/skills](https://github.com/BeautifulEngine/skills).

