# Project Quote

Turns a project scope into a branded quote and statement of work PDF (phases, deliverables, hours and rates or fixed fees, contingency, payment schedule, assumptions, out of scope, timeline, terms and a signature block), with totals computed by a script so the math is always right. Also makes a one-page rate card of services and rates.

## Install

**Claude app (web, desktop):** turn on Settings > Capabilities > "Code execution and file creation". Then go to Customize > Skills, click "+", then "+ Create skill" > "Upload a skill", and upload `project-quote.zip` as is (don't unzip it).

**Claude Code:** install the whole Beautiful Engine collection:

```bash
claude plugin marketplace add BeautifulEngine/skills
claude plugin install beautiful-engine@beautiful-engine
```

Then use `/beautiful-engine:project-quote`, or ask in plain words.

## Usage

```
/project-quote <client>: <what they want> [budget] [deadline]
/project-quote rate card
```

Plain requests work too:

- "Quote for a brand identity for a coffee roaster: logo, palette, packaging for 3 SKUs, done in 6 weeks."
- "Estimate a 20×20 trade show booth design and fabrication management for Acme, budget around $60K."
- "Make my rate card: Design Director $175/hr, Designer $120/hr, day rate $1,300."
- "Turn this client email (attached) into an SOW."
- "Same quote, but as fixed fees per phase instead of hours."

## Made by Beautiful Engine

Made by [Beautiful Engine](https://www.beautifulengine.com), a creative studio in Los Angeles. Questions, ideas, or something broke? [Open an issue](https://github.com/BeautifulEngine/skills/issues/new). More skills: [github.com/BeautifulEngine/skills](https://github.com/BeautifulEngine/skills).

