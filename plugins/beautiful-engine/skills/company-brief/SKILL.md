---
name: company-brief
description: Researches any company from its name or URL and delivers a designed PDF brief in that company's own colors and type, plus a one-page cheat sheet: financials, history, leadership, hiring and pay, employee reviews, a brand kit with links to official logos and brand guidelines, marketing, news, competitors, risks, and how to talk to them. Use when someone asks for a company brief, company research or a deep dive, interview prep for a company, whether to accept an offer, how to pitch a company, or brand research before working with a brand. Also compares two companies or offers side by side, and refreshes an older brief with what changed. Usage - /company-brief followed by a company name or URL, optionally "for" a role, "brand kit", or "shareable"; or "compare A and B"; or "refresh" an existing brief.
---

# Company Brief

Turn a company name or URL into a deep, sourced, designed PDF and a one-page cheat sheet that tells the reader everything they need to walk into an interview, offer conversation, client pitch, or first project with a new brand: what the company is, how it's doing, who runs it, what working there is like, how its brand and marketing work, who it competes with, and how to talk to it. The PDF uses the company's own colors and type, so it feels like it belongs to them.

## Usage

People ask in plain words, and every request should work without them learning any syntax. Map what they say onto these modes:

| They say | Make |
|---|---|
| "Company brief on Figma", `/company-brief linear.app` | A full brief and a one-page cheat sheet |
| "…for Senior Brand Designer", "I'm interviewing there" | The same, with hiring, people and interview prep focused on that role |
| "…brand kit", "we just signed Oatly as a client" | Brand-work mode |
| "…shareable", "for a friend", "to send to my team" | Shareable mode |
| "Compare Figma and Canva", "help me choose between these two offers" | Compare mode (section below) |
| "Refresh my Figma brief", "update this brief" with an old PDF attached | Refresh mode (section below) |

Modes combine ("compare Figma and Canva for Senior Brand Designer, shareable").

- **Company**: a URL settles identity. A bare name may not (Step 1).
- **for <role>**: focuses hiring, people to know, and interview prep on that role and its team. Without it, default to design, brand, marketing, and creative leadership, or to whatever the person's background suggests.
- **Personal mode (default)**: written for the person asking. Use what you know about them (memory, past chats, this conversation, an attached resume or portfolio) for "Your angle", the pitch, and "Fit for you". If there is an offer in hand, add "Before you sign". If you know nothing about them, write those parts generically and offer in the reply to tailor them.
- **Brand work**: the Brand identity and Brand kit sections get the most care, and the kit includes the full asset list and the "Ask the client for" callout (references/brand-extraction.md, section 4). In Part five, "Interview prep" becomes "Kickoff prep" (what the brand team will expect, what to bring, likely questions), "Questions to ask" are for the brand team, and Fit for you and Before you sign are dropped. Keep Hiring to a short paragraph.
- **Shareable**: nothing about the person, in the brief or the cheat sheet. No "Prepared for" pill, no Fit score, no Before you sign. Part five becomes "How to talk to them" and "Your angle" becomes "Angles that land".

Keep it easy for the person:
- Don't stop to ask questions unless the company's identity is genuinely ambiguous, or a refresh can't find the old brief. Pick sensible defaults and say which you picked.
- Start in the first reply: one sentence on what they'll get (the brief and cheat sheet) and that a full brief takes a while because it reads many sources, then the task list, then research.
- Finish with the files and a few plain lines, not a tour of the method.

## Skill files

Paths below use `${CLAUDE_SKILL_DIR}`. If that text isn't replaced with a real path where you're running, find the folder once with `find / -name brief-template.html -path '*company-brief*' 2>/dev/null | head -1` and use its absolute path in every command (shell variables may not persist between commands).

| File | What it's for |
|---|---|
| `assets/brief.css` | Base stylesheet. Copy it; don't edit it. |
| `assets/brief-template.html` | Skeleton of the whole brief with `{{placeholders}}` |
| `assets/cheatsheet-template.html` | The one-page cheat sheet that ships with every brief |
| `assets/compare-template.html` | The side-by-side comparison (compare mode) |
| `scripts/fonts.py` | Installs free fonts from Fontsource and prints `<link>` tags |
| `scripts/tokens.py` | Turns brand colors into the token `<style>` block, with contrast fixes |
| `scripts/render.cjs` | Renders the PDF with Node Playwright and audits fonts, contrast, placeholders |
| `scripts/render.py` | Same in Python, falling back to Chrome CLI, then WeasyPrint |
| `scripts/audit.js` | The audit both renderers run inside the page |
| `scripts/contact_sheet.py` | One image of every page for the layout check |
| `references/research-playbook.md` | Where to look for each section, and the efficient order |
| `references/brand-extraction.md` | Getting real colors, fonts, and logo description from the live site |
| `references/components.md` | Markup for every component, section order, writing rules |

## Hard rules

- **Disambiguate first.** Many companies share names, and funding databases and job boards often merge them. Confirm each financial and hiring fact belongs to the right entity (same domain, founders, HQ). If a collision exists, open the summary with a **Name check** callout.
- **Every number gets a source, a date, and a confidence tag**: `Verified` (primary: filings, the company's own site or careers page), `Reported` (credible press), `Company claim` (their marketing), `Estimate` (third-party or your inference; say from what), `Unknown` (searched, not found; say where).
- **Write findings to `research-notes.md` as you go.** Search results get cleared from context in long research. Anything not written down is lost.
- **Recency**: use today's date; put the year in news searches; mark anything older than 18 months as dated.
- **People**: public-facing leaders and people relevant to the role, with public professional information only. No personal contact details, home locations, family, or photos of people.
- **Brand assets are links, never copies.** Describe the logo in words and link to the brand's own logo files and guidelines. Don't redraw, trace, embed, or download logos, mascots, fonts, or ad imagery into the brief or the working folder. Prefer the brand's press kit, brand portal or guidelines over third-party logo sites, label which is which, confirm each file's format by opening it, and link the usage terms that govern the files. Color swatches, type specimens, and abstract brand-colored patterns are fine.
- **Quotes**: employee review excerpts of 25 words or fewer, 4 or fewer in total, attributed to platform and date. Summarize articles; don't paste them.
- **Label it independent**: the cover says "Independent research brief. Not affiliated with or endorsed by <Company>."
- **Say what's missing** in one line instead of dropping a section silently.
- **Credit line**: the brief, comparison and cheat sheet templates end with a small "Made with the free Company Brief skill for Claude, by Beautiful Engine" line linking to the skill's repo and beautifulengine.com. Keep it in every file, including shareable ones. Leave it out only when the person asks ("no credit line", "remove the Beautiful Engine line"), and then remove it from every file.
- **Never claim a check you didn't do** ("Only Glassdoor was reviewed for this brief").
- **Shareable briefs** contain nothing private about the person asking, even if you know it.

## Workflow

Create this task list and tick items off as you finish them:

1. Identify the company and check for name collisions
2. Set up the working folder and notes file
3. Read the company's own site and careers pages
4. Research everything else in parallel batches
5. Extract brand colors and type; build tokens and fonts
6. Build the brand kit: logo files, guidelines, fonts, color specs
7. Synthesize: bottom line, scorecard, how to talk to them
8. Write brief.html and the cheat sheet
9. Render and audit
10. Check facts, links, and layout
11. Deliver

### 1. Identify

- URL given: open the homepage and About page. Name given: search `"<name>" company` and `"<name>" official site`.
- Pin down brand and legal name, domain, HQ, founding year, founders, public or private (ticker), parent.
- Search `"<name>" -<domain>` for same-name companies.
- If two or more real companies plausibly match and nothing in the request tells them apart, ask one question naming the candidates. Otherwise pick the best match and state it at the top of your reply.
- In personal mode, also search past chats and memory (if available) for the company name: an application, recruiter thread, or offer changes what matters.

### 2. Working folder

```bash
mkdir -p briefs/<company-slug> && cd briefs/<company-slug>
cp "${CLAUDE_SKILL_DIR}/assets/brief.css" . && cp "${CLAUDE_SKILL_DIR}/assets/brief-template.html" brief.html
```

Use the current working directory, or a scratch folder if it isn't writable. Create `research-notes.md` with one heading per brief section, and append findings as `- <fact> | <tag> | <source title> | <URL> | <date>`.

### 3. The company's own site first

The live site and careers pages answer a third of the brief and are the most reliable source for mission, values, products, customers, offices, open roles, pay, interview process, social handles, and brand tokens.

- **If you have a browser tool** (Claude in Chrome, an in-app browser, or a cloud browser), use it for the company's domain; approve the whole site once if asked. Read pages as text, not screenshots, except for the logo and hero.
- Visit, in order: homepage (positioning, customer logos, footer handles and links) → About → Careers (count roles by department and location) → 2–4 postings closest to the target role (pay, interview steps, reporting line, tools) → Press/newsroom (timeline, press kit, logo files, brand guidelines) → Blog/changelog (last 3 months) → Events → Customers.
- Run the brand extraction script on the homepage while you're there (references/brand-extraction.md, section 1).
- **No browser**: fetch the same pages with the fetch tool.
- The careers page beats job-board APIs, which are often stale. Use the ATS API list in the playbook only as a fallback.

Details: references/research-playbook.md, sections 1–2.

### 4. Everything else

Follow references/research-playbook.md sections 3–6. Send independent searches together in one turn (funding, revenue, news, reviews, competitors, campaigns, events, podcasts). Use standard search first and extended search for recent news, hiring and review data, or anything thin. If a fetch tool refuses a URL you typed, search for it and fetch the result link, or open it in the browser. Connectors for job sites (Indeed, ZipRecruiter, LinkedIn), if present, are good for ratings and roles.

40–80 lookups is normal for a mid-size company. When a section stays thin after two good searches, mark it `Unknown` and move on.

### 5. Brand tokens and fonts

From the extraction (references/brand-extraction.md):

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/fonts.py" "<Display Font>:400,500,600" "<Body Font>:400,600" "<Label Font>:400,500"
python3 "${CLAUDE_SKILL_DIR}/scripts/tokens.py" --brand "#…" --accent "#…" \
  --font-display "<Display Font>" --font-body "<Body Font>" --font-label "<Label Font>" \
  --display-weight 600 --tracking -0.02em --radius 8px \
  --footer "<Company> · Company Brief · <Mon YYYY>" [--cover-stops "#…,#…,#…"] > tokens.html
```

- Paste the `<link>` lines from fonts.py at the FONT LINKS marker and `tokens.html` at the TOKENS marker in brief.html.
- Every line of the tokens.py report should say `ok`. A `WARNING` means choose different colors (for a light signature color, make the dark one `--brand`).
- Proprietary brand font: run the stand-in test in brand-extraction.md section 2 and say in the brief which free font stands in.
- If npm can't install fonts, use an installed family (`fc-list : family`) and say so in the Type section.

### 6. Brand kit

Follow references/brand-extraction.md, section 4. In every mode, find the primary logo as a vector file (SVG, EPS, AI or vector PDF) and the most recent public brand guidelines; in brand-work mode, also fonts, color specs, imagery, templates, boilerplate and usage terms. Send the searches together. For each item record the link, the format you confirmed by opening it, the source (official or third-party), its date, and a status: `Current`, `Dated`, `Outdated`, `Request access`, or `Not found`. Check that the logo file matches the logo on the live site today.

### 7. Synthesize

Read the whole notes file, then decide the bottom line, the three things to know, the scorecard, their language, priorities → talking points, the 30-second pitch, the angle, interview prep, questions to ask, do's and don'ts, before you sign (offer only), and outreach. Guidance for each: references/research-playbook.md section 7.

### 8. Write brief.html and the cheat sheet

Replace every `{{placeholder}}` in the template, add rows and items as needed, and delete only the sections the template marks as conditional. Markup and writing rules: references/components.md. Keep per-brief CSS small and in the template's override block. Aim for 14–20 pages.

Then copy `assets/cheatsheet-template.html` to `cheatsheet.html`, paste the same font links and tokens block, and fill it from the finished brief, with no new facts. It must fit on one page: cut list items before shrinking type.

### 9. Render and audit

```bash
node "${CLAUDE_SKILL_DIR}/scripts/render.cjs" brief.html "<Company>-Company-Brief-<YYYY-MM>.pdf" \
  || python3 "${CLAUDE_SKILL_DIR}/scripts/render.py" brief.html "<Company>-Company-Brief-<YYYY-MM>.pdf"
```

Render `cheatsheet.html` to `<Company>-Cheat-Sheet-<YYYY-MM>.pdf` the same way, and confirm with `pdfinfo` that it is exactly one page.

- The Node renderer exits with code 2 if Playwright is missing, which triggers the Python one. render.py tries Playwright, then a Chrome binary, then WeasyPrint (`pip install weasyprint`).
- Fix every `FAIL` line (font not loaded, text under 4.5:1 contrast, leftover placeholder) and render again.
- If you're on someone's own computer and nothing renders, ask before installing a renderer (`pip install playwright && python -m playwright install chromium`).

### 10. Check

- Layout: `python3 "${CLAUDE_SKILL_DIR}/scripts/contact_sheet.py" <pdf> sheet.png`, then look at the image. The cover is full bleed with no footer; the summary fits on page 2; each part starts a new page; nothing is clipped; no table overflows; no near-empty pages; no heading is stranded at a page bottom. Render a doubtful page larger with `pdftoppm -r 150 -f N -l N -png <pdf> page` and look again.
- Facts: every number in the PDF matches the notes file, carries a tag, and appears in Sources. Dates are absolute. The other same-name company isn't mixed in.
- Copy: read references/components.md writing rules once more against the text.
- Links: open 5 or more Sources links to confirm they resolve, and open every Brand kit link to confirm it resolves to the format listed.

### 11. Deliver

- Send the brief and the cheat sheet as files. In brand-work mode, also send `<Company>-Brand-Kit.md`: the kit table as plain links, ready to paste into a project doc or channel. If the person keeps briefs in a folder on their computer and you can reach it, save it there too.
- Reply in a few lines: the bottom line in two sentences, the 2–3 sharpest talking points, anything important you couldn't find, and one useful next step (a tailored cover letter, an outreach note, mock interview questions, a kickoff agenda, or a shareable version). In brand-work mode, say which logo and guideline files you found and what the team will need to request.

## Compare two companies

For "compare A and B", "A or B?", or two offers to choose between.

1. Identify both companies (Step 1 for each) and keep notes in `briefs/<a>/` and `briefs/<b>/`. If a brief for either already exists in this conversation or the working folder, reuse its notes.
2. Research each one at cheat-sheet depth, about 20–30 lookups each: their own site and careers page, money (revenue, growth, funding or market cap), leadership, hiring and pay for the role, employee reviews, culture, the last 12 months of news, risks, and each brand's main color. Use the same rows and the same depth for both, and say when one side has no data.
3. Make neutral tokens for the comparison (`tokens.py --brand "#1f2430" --accent "#3d4452"`, fonts `Inter`), and use each company's own main color only through `--co` on its column header and dot.
4. Fill `assets/compare-template.html` as `compare.html`: bottom line, side-by-side table, scorecard, the case for each, and what would settle it. Personal mode adds a Fit row and, with offers in hand, a "Before you decide" table (pay, equity, start date, deadlines, benefits). Shareable mode leaves the person out.
5. Make a cheat sheet for each company, using its own brand tokens.
6. Render `<A>-vs-<B>-<YYYY-MM>.pdf` and both cheat sheets, check them as in Step 10, and deliver all three. In the reply, give the deciding factor in two sentences and offer a full brief on either company.

## Refresh a brief

For "refresh", "update" or "what's changed at X" when an older brief exists.

1. Find the old brief: research notes in `briefs/<company-slug>/` (best), an attached PDF (read it with `pdftotext -layout`), or a folder on the person's computer. If you can't find one, say so in one line and make a fresh brief.
2. Note the old research date and its main facts.
3. Research what moves: news since that date, money, leadership, hiring and pay, reviews, brand and campaigns, competitors' big moves. Re-open every Brand kit link. Re-check other facts only if they are now older than 18 months.
4. Update every changed figure with its new source and date; unchanged facts keep their original sources.
5. Fill the template's "What's changed" part (right after the summary): a Then / Now table and the news since last time. If little changed, say that plainly.
6. Use today's research date and a new file name, refresh the cheat sheet, render, check, and deliver. In the reply, lead with the three biggest changes.

