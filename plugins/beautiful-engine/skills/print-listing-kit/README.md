# Print Listing Kit

Writes ready-to-paste listings for selling or sharing a 3D print model file on marketplaces such as Etsy, Printables, MakerWorld, Cults3D and Thangs - titles, descriptions, tags, print settings, assembly notes, license, price based on comparable models, a photo shot list and a download README - and checks titles and tags against each marketplace's limits with a script. Flags trademark and character risks and AI-disclosure rules.

## Install

**Claude app (web, desktop):** turn on Settings > Capabilities > "Code execution and file creation". Then go to Customize > Skills, click "+", then "+ Create skill" > "Upload a skill", and upload `print-listing-kit.zip` as is (don't unzip it).

**Claude Code:** install the whole Beautiful Engine collection:

```bash
claude plugin marketplace add BeautifulEngine/skills
claude plugin install beautiful-engine@beautiful-engine
```

Then use `/beautiful-engine:print-listing-kit`, or ask in plain words.

## Usage

```
/print-listing-kit <model name> [marketplaces] [free | paid] [price]
```

Attach photos, renders, the STL or 3MF (or a slicer screenshot), and any notes. Plain requests work too:

- "Listing kit for my modular hex planter. Selling on Etsy and Printables (free there)."
- "Write the MakerWorld listing for this articulated dragon. Printed on a Bambu H2D in PLA."
- "What should I charge for this STL bundle of 12 cable clips?"
- "Rewrite my Etsy listing; it's not getting views." (paste it)

Default marketplaces: Etsy, Printables, MakerWorld and Cults3D. Say which ones you use to narrow it.

## Made by Beautiful Engine

Made by [Beautiful Engine](https://www.beautifulengine.com), a creative studio in Los Angeles. Questions, ideas, or something broke? [Open an issue](https://github.com/BeautifulEngine/skills/issues/new). More skills: [github.com/BeautifulEngine/skills](https://github.com/BeautifulEngine/skills).

