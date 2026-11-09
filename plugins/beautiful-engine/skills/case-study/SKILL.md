---
name: case-study
description: Turns project notes, images, a deck or links into a portfolio case study - a responsive web page, a PDF and Markdown ready to paste into a portfolio site, Behance, Notion or LinkedIn - covering the challenge, insight, idea, process, craft, results and credits. Can tailor the story to a target company or role. Never invents results or quotes. Use when someone asks for a case study, portfolio write-up, project page, project story, or help presenting past work for a job or a pitch. Usage - /case-study followed by the project name, with notes or images attached.
---

# Case Study

Turn the raw material of a project (notes, images, a deck, links, a client email) into a case study that shows how the person thinks and what changed because of their work. One story, three formats: a web page, a PDF, and Markdown.

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

## Ask once for what only the person knows

Before writing, collect: their role and what they personally did (versus the team), the team and collaborators to credit, the client and whether the client can be named, results (numbers, press, awards, quotes) with where they come from, and what's under NDA. If anything is missing, ask in one short message, then continue with what's available and mark gaps in the reply.

**Files.** `<skill-dir>` means this skill's folder, the one holding this SKILL.md. Templates are in `assets/`, scripts in `scripts/`, and the shared PDF steps (fonts, colors, render, check) are in `references/rendering.md`.

## Hard rules

- **Never invent results, quotes, numbers, clients or awards.** Use only what the person gave or what you verified in a public source (cite it). Without results, write about what the work made possible and say what to add.
- **Their role, clearly.** Say what the person did, and credit others by name or role. "I led" only where they led.
- **Respect confidentiality.** Leave out anything under NDA or unreleased. Ask if unsure whether a client can be named; offer an anonymized version ("a global sports and entertainment company").
- **Images are theirs.** Use only images the person provided or owns the rights to show. Write alt text and a caption for each. Don't pull client or brand images from the web into the case study.
- **Show the thinking.** Every case study answers: what was the problem, what did you notice, what did you decide and why, what did you make, what changed.
- No Beautiful Engine credit or other third-party branding: the case study belongs to the person.

## Workflow

1. **Gather and read** everything attached. If it's a deck or PDF, pull out the key frames as images (`pdftoppm -r 110 -png deck.pdf frame`) and pick the strongest.
2. **Find the story** in 4 sentences: the challenge, the insight, the idea, the outcome. That becomes the dek and the section leads.
3. **Tailor** (when a company or role is given): lead with the part of the work that matches their needs, use their vocabulary where it honestly fits, and choose the images that prove it. If a Company Brief for that company is in the conversation, use it.
4. **Write `case-study.md`**: title, one-line dek, a meta block (client, role, team, year, disciplines), then Challenge, Insight, Idea, Process, Craft, Results, Credits. Short paragraphs, image placements with captions, and pull quotes only if real.
5. **Build the page** from `assets/case-study-template.html`:
   - copy the images into `images/` beside it;
   - set colors and fonts with the person's own portfolio style if they have one (look at their site), otherwise neutral, letting the work carry the color;
   - for the PDF: link fonts with `scripts/fonts.py` and render per references/rendering.md;
   - for the web version: save a copy as `index.html` with the FONT LINKS replaced by a Google Fonts `<link>` for the same families, so it works when hosted.
6. **Render, audit, check** the PDF contact sheet, and open the web page at phone width if a browser is available.
7. **Deliver** the PDF, the web folder (`index.html` + `images/`, zipped), and `case-study.md`. In the reply: the 4-sentence story, anything left out for confidentiality, and the facts or numbers that would make it stronger.

Output names: `<Project>-Case-Study.pdf`, `<Project>-Case-Study-web.zip`, `<Project>-Case-Study.md`.
