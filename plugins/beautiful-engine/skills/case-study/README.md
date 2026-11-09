# Case Study

Turns project notes, images, a deck or links into a portfolio case study - a responsive web page, a PDF and Markdown ready to paste into a portfolio site, Behance, Notion or LinkedIn - covering the challenge, insight, idea, process, craft, results and credits. Can tailor the story to a target company or role. Never invents results or quotes.

## Install

**Claude app (web, desktop):** turn on Settings > Capabilities > "Code execution and file creation". Then go to Customize > Skills, click "+", then "+ Create skill" > "Upload a skill", and upload `case-study.zip` as is (don't unzip it).

**Claude Code:** install the whole Beautiful Engine collection:

```bash
claude plugin marketplace add BeautifulEngine/skills
claude plugin install beautiful-engine@beautiful-engine
```

Then use `/beautiful-engine:case-study`, or ask in plain words.

## Usage

```
/case-study <project name> [for <company or role>] [short | long]
```

Attach whatever exists: images, a PDF deck, notes, press links, results. Plain requests work too:

- "Write a case study for the Sphere partnership launch. Notes and images attached."
- "Turn this deck into a portfolio case study, short version."
- "Case study for my art car project, aimed at experiential agency roles."
- "Rewrite this case study for a Netflix design lead application." (attach the existing one)

**Length.** Default is about 600–900 words with 6–10 images. "short" is a 150–250 word card for a portfolio grid or LinkedIn post. "long" adds process detail for a design-team audience.

## Made by Beautiful Engine

Made by [Beautiful Engine](https://www.beautifulengine.com), a creative studio in Los Angeles. Questions, ideas, or something broke? [Open an issue](https://github.com/BeautifulEngine/skills/issues/new). More skills: [github.com/BeautifulEngine/skills](https://github.com/BeautifulEngine/skills).

