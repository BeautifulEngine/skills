# Brand Snapshot

Reads any brand's live website and returns a two-page brand snapshot PDF plus design tokens (JSON and CSS) - the color palette with hex, RGB and contrast checks, typefaces with free stand-ins, the logo described in words with links to official files, UI patterns like corner radius and buttons, voice samples, imagery style, and where the official guidelines live.

## Install

**Claude app (web, desktop):** turn on Settings > Capabilities > "Code execution and file creation". Then go to Customize > Skills, click "+", then "+ Create skill" > "Upload a skill", and upload `brand-snapshot.zip` as is (don't unzip it).

**Claude Code:** install the whole Beautiful Engine collection:

```bash
claude plugin marketplace add BeautifulEngine/skills
claude plugin install beautiful-engine@beautiful-engine
```

Then use `/beautiful-engine:brand-snapshot`, or ask in plain words.

## Usage

```
/brand-snapshot <url or brand name> [tokens only]
```

Plain requests work too:

- "Brand snapshot for linear.app."
- "What colors and fonts does Patagonia use?"
- "Pull design tokens from stripe.com for a pitch mockup."
- "Snapshot of Oatly and Liquid Death, side by side." (makes one snapshot each)

"tokens only" skips the PDF and returns `tokens.json` and `tokens.css`.

**Files.** `<skill-dir>` means this skill's folder, the one holding this SKILL.md. Templates are in `assets/`, scripts in `scripts/`, and the shared PDF steps (fonts, colors, render, check) are in `references/rendering.md`.

## Made by Beautiful Engine

Made by [Beautiful Engine](https://www.beautifulengine.com), a creative studio in Los Angeles. Questions, ideas, or something broke? [Open an issue](https://github.com/BeautifulEngine/skills/issues/new). More skills: [github.com/BeautifulEngine/skills](https://github.com/BeautifulEngine/skills).

