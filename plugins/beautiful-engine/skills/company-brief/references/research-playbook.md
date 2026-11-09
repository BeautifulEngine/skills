# Research playbook

Section-by-section sources, in the order that wastes the least time. Write every finding to `research-notes.md` as you go, in this shape:

`- <fact> | <tag> | <source title> | <URL> | <date published or accessed>`

Tags: `Verified` (primary source: filing, the company's own site or careers page), `Reported` (credible press), `Company claim` (their marketing, unverified), `Estimate` (third-party estimate or your inference; say from what), `Unknown` (searched, not found; say where you looked).

## Contents
1. Order of work and efficiencies
2. Reading the company's own site in a browser
3. The company (glance, products, mission, history, financials)
4. People, hiring, reviews, culture
5. Brand, advertising, activations, social, media, news
6. Market, competitors, customers, risks
7. Synthesis

---

## 1. Order of work and efficiencies

1. **Context first (10 seconds).** If the person has memory or past chats available, search them for the company name: an application, an offer, a recruiter thread, or a prior brief changes what matters (an offer adds "Before you sign"). Note it; don't put private details in a shareable brief.
2. **The company's own site next, in a browser if you have one.** It is the primary source for mission, values, products, customers, offices, open roles, pay, interview process, social handles, and brand tokens. One pass through 6–10 pages covers a third of the brief. See section 2.
3. **Then search in parallel batches.** Send independent searches in the same turn: funding + revenue + valuation; news last 12 months; reviews; competitors; campaigns; events; podcasts. Use `standard` mode first, `extended` for recent news, hiring and review data, or anything that comes back thin. Put the current year in news queries.
4. **Fetch the best result links.** Some fetch tools only accept URLs that came from a search result or the user, and refuse ones you typed from memory. If a fetch is refused, search for the page and fetch the result link, or open it in the browser.
5. **Stop at coverage, not page count.** 40–80 lookups is normal for a mid-size company. When a section is thin after two good searches, mark it `Unknown` with where you looked and move on.

Efficiencies that paid off:
- The careers page beats ATS APIs. Public job-board APIs (Greenhouse, Lever, Ashby) are often stale, renamed, or 404. Use them only when the careers page won't load.
- Read 2–4 individual job postings closest to the target role. They carry pay ranges, interview steps, the hiring manager's title, tools, team rituals, and the company's own description of where it's heading.
- The site footer lists the official social handles. Use those instead of guessing; same-name accounts are common.
- The press or newsroom page gives a dated timeline for free. Funding press releases (BusinessWire, PR Newswire) give round, amount, valuation and investors in one place.
- Third-party company profiles that read as AI-generated (directory sites, "company overview" pages) get tagged `Estimate` at most. Prefer press and primary sources.
- Revenue for private companies: Sacra, GetLatka, and press interviews where the CEO states ARR. Tag by source.
- Social follower counts usually need the platform page itself. If it won't load, write the handle and `Unknown` rather than an old number.

## 2. Reading the company's own site in a browser

If a browser tool is available (Claude in Chrome, the in-app browser, a cloud browser), use it for the company's domain. Ask for site access once for the whole domain if the tool requires approval. Read pages as text where the tool offers it; it's faster than screenshots.

Visit, in order:
1. **Homepage**: positioning line, product names, customer logos (read alt text), the footer (social handles, press/brand links, offices). Run the brand extraction script here (references/brand-extraction.md).
2. **About / company**: mission (exact wording), founding story, leadership list, investors, live counters (customers, employees).
3. **Careers**: total open roles; count by department and by location (remote vs. office); values text; benefits; any culture video or handbook link.
4. **2–4 job postings** nearest the target role (or design, brand, marketing leadership by default): title, location, pay range, hiring manager or reporting line, interview steps, tools, what the first 90 days look like.
5. **Press / newsroom**: dated announcements for the timeline and news section; press kit, logo files, brand guidelines, and the official boilerplate paragraph (brand-extraction.md, section 4).
6. **Blog / changelog**: the last 3 months of launches and posts; who on the team writes; any rebrand or design post.
7. **Events / community**: user conference, meetups, webinars, sponsorships (activations section).
8. **Customers / case studies**: named customers and the outcomes they claim.

Count roles with a quick script when the careers page is long, for example in the page console:
```js
(() => { const t = document.body.innerText; const m = t.match(/\b\d+\s+(open\s+)?(roles|positions|jobs)\b/i); return m ? m[0] : t.slice(0, 3000); })()
```
then read department and location headings from the page text and tally them.

Without a browser: fetch the homepage, About, careers and 2 postings with the fetch tool. Brand tokens then come from the press kit, Brandfetch, or searches (see brand-extraction.md).

## 3. The company

- **At a glance**: brand and legal name, domain, HQ and offices, founded, founders, employees (range + source + date), public or private (ticker), parent company, industry, investors, mission in their words.
- **What they do**: products and the flagship, how they make money, pricing model, who buys, notable customers, geographic reach. Explain it in plain words a smart friend outside the industry would follow.
- **Mission, vision, goals**: the official wording, then stated near-term priorities from CEO letters, earnings calls, keynotes, launch posts, interviews, and what the job postings hire for.
- **History**: founding story, pivots, launches, funding, acquisitions made and received, leadership changes, rebrands, layoffs, IPO. 8–20 dated entries.
- **Financials**
  - Public: SEC EDGAR (10-K, 10-Q, 8-K; DEF 14A for exec pay), investor relations, last earnings (revenue, growth, profit, guidance), market cap, 12-month stock trend, risk factors.
  - Private: rounds (date, amount, lead, valuation) from press releases, TechCrunch, Axios, Bloomberg, Crunchbase/PitchBook/Tracxn snippets; SEC Form D on EDGAR; revenue estimates (Sacra, GetLatka, press); runway signals (time since last raise, hiring pace, layoffs).
  - Nonprofit: ProPublica Nonprofit Explorer (Form 990).
  - Everyone: layoffs.fyi, state WARN notices, debt, profitability claims, acquisition bids.

## 4. People, hiring, reviews, culture

- **People to know**: CEO and founders; leaders over the target role's team; the likely hiring manager; recent exec hires and departures (last 18 months). Public professional info only: title, background, public talks, posts, articles. No personal contact details, home locations, family, or photos.
- **Hiring**: open roles total and by department and location (careers page, dated); remote policy; pay ranges from postings (CA, NY, CO, WA require them), Levels.fyi, Glassdoor salaries; headcount trend (LinkedIn snippets, press); interview process (postings, Glassdoor interviews, Reddit, Blind). ATS APIs only as a fallback:
  - Greenhouse `https://boards-api.greenhouse.io/v1/boards/<token>/jobs?content=true`
  - Lever `https://api.lever.co/v0/postings/<company>?mode=json`
  - Ashby `https://api.ashbyhq.com/posting-api/job-board/<name>?includeCompensation=true`
  If an Indeed, ZipRecruiter or LinkedIn connector is available, use it for ratings and open roles.
- **Employee reviews**: Glassdoor first (rating, review count, % recommend, CEO approval, trend), then Indeed, Comparably, Blind, Built In, kununu for Europe. Top 3 recurring pros and cons. Flag samples under 20 reviews. Say which platforms you actually checked.
- **Culture**: values on paper vs. in practice (reviews, postings), benefits, return-to-office news, best-place-to-work lists, controversies.

## 5. Brand and marketing

- **Brand identity**: logo described in words; colors with hex; typefaces and stand-ins; voice (3–4 traits, each with a real line from their site); tagline history; photography, illustration, motion; recent redesigns. Method in brand-extraction.md.
- **Brand kit**: official vector logo files, the most recent public brand guidelines, and, in brand-work mode, fonts, color specs, imagery, templates, boilerplate and usage terms. Sources, searches, how to confirm a file's format and recency, and the status labels are in brand-extraction.md, section 4. Link everything; never download or embed logos.
- **Who made the brand**: in-house brand and design leads and team size (LinkedIn snippets, blog bylines); agency or studio credits (search `"<company>" rebrand`, Behance, Dribbble, Brand New, It's Nice That).
- **Advertising**: the last 24 months: campaign, date, idea, channels, agency, results. Ad Age, Adweek, The Drum, Campaign, Muse by Clio, LBBOnline, iSpot.tv; Meta Ad Library, Google Ads Transparency Center and LinkedIn Ad Library through a browser for what's running now. If you find no paid brand campaigns, say so; that is a finding.
- **Activations and events**: owned conferences, pop-ups, stunts, festival and conference presence (SXSW, CES, Cannes Lions, Web Summit, industry shows), sponsorships. Event Marketer, BizBash, the events page, social posts.
- **Awards**: Cannes Lions, Clio, One Show, D&AD, Webby, Fast Company lists.
- **Social**: handles from the site footer; follower counts dated or `Unknown`; what they post and what performs.
- **Videos and podcasts**: company YouTube channel, keynotes, launch videos; the company podcast; exec appearances (search `"<CEO name>" podcast`, and each key leader). Pick 3–6 worth the reader's time and say why.
- **In the news**: last 12 months, newest first, 8–15 items, each with a one-line takeaway.

## 6. Market, competitors, customers, risks

- **Market**: category, size and growth with a source, tailwinds and headwinds, where the company sits.
- **Competitors**: 4–8 direct and adjacent. What they do, scale, positioning, how the target differs. 10-K "Competition", G2/Capterra, app store rankings, comparison posts (including the company's own "vs." pages, tagged `Company claim`).
- **Customers and partners**: named customers, case studies, strategic and integration partners.
- **Risks**: lawsuits (CourtListener, news), regulators, breaches, controversies, leadership churn, layoffs, review decline, debt, customer concentration, platform dependency, pending deals.

## 7. Synthesis

Read the whole notes file before writing. Decide:
- **Bottom line** (3–4 sentences): what it is, how it's doing, what that means for someone joining or pitching, the main tension. Direct, not hedged.
- **Three things to know**: the facts that would most embarrass someone who didn't know them.
- **Scorecard**, 1–5 dots each with evidence: Stability, Momentum, Culture, Hiring and pay, Brand ambition, plus Fit for you in personal mode. Missing data gets empty dots and "Not enough data".
- **Their language**: 8–15 terms (product names, internal words, values words), with pronunciation if the name is often said wrong.
- **Priorities → how to talk about them**: 4–6 current priorities, each with evidence and a line the reader could say.
- **30-second pitch**: in personal mode, built from the reader's real background; in shareable mode, a fill-in template.
- **Your angle** (personal mode): specific past work to lead with, and gaps you saw that the reader could offer to fix. Shareable mode: "Angles that land" by background.
- **Interview prep**: process, likely questions (say what they're inferred from), how to frame answers. In brand-work mode this is **Kickoff prep**: what the brand team will expect to see, what to bring (references, a point of view on their brand), and the questions they'll likely ask.
- **Ask the client for** (brand-work mode): the kit gaps turned into a short request list for kickoff (brand-extraction.md, section 4).
- **Questions to ask**: 8–12, each with a "why" grounded in the research.
- **Do's and don'ts**: sensitive topics, recent news to be ready for, competitor landmines.
- **Before you sign** (only with an offer): equity, refreshers, leveling, remote terms, start date, what's typical at this stage. Not legal or financial advice.
- **Outreach**: which public roles to approach and through what (warm intro, event, content to reference). No personal contact details.
