# Components and writing rules

`assets/brief-template.html` already contains every section with this markup. Use this file when you need a component the template doesn't show in a given spot, or to check the writing rules before the final pass.

## Body order

Each `.part` starts on a new page; sections inside a part flow.

1. **Cover** (`.cover`, full bleed, no footer): kicker, company name, one-line dek, "Prepared for" pill (personal mode only), 6-cell TOC, meta line, swatch strip of 5 brand colors, independence disclaimer.
2. **Executive summary** (`.summary`, must fit on page 2): Bottom line, Name check callout if needed, 6 stat tiles, three things to know, scorecard.
3. **Part one, The company**: At a glance, What they do, Mission/vision/goals, History, Financials.
4. **Part two, People & culture**: People to know, Hiring, What employees say, Culture & values.
5. **Part three, Brand & marketing**: Brand identity, Brand kit & who makes it, Advertising & campaigns, Activations & events, Social/video/podcasts, In the news.
6. **Part four, Market & competition**: Market, Competitors, Customers & partners, Risks & red flags.
7. **Part five, Your play** (shareable: "How to talk to them"): Their language, Priorities → talking points, 30-second pitch, Your angle (shareable: Angles that land), Interview prep (brand work: Kickoff prep), Questions to ask, Do's & don'ts, Before you sign (offer only), Outreach, Sources.

Delete a section only when the template says it's conditional. For thin data, keep the section and write one line saying what you looked for.

## Markup

```html
<div class="part"><div class="part-head"><div class="label">Part one</div><h2>The company</h2></div>
<section><h3><span class="num">01</span>At a glance</h3> … </section></div>

<!-- callouts: .big (bottom line), .accent (key points), .warn (risks, name check) -->
<div class="callout warn"><div class="title">Name check</div><p>Two companies are called Acme. This brief covers acme.io (Austin, founded 2018), not Acme Corp (acme.com).</p></div>

<div class="stats"><div class="stat"><div class="v">$40M</div><div class="k">Funding</div><div class="n">Series B, May 2026</div></div></div>   <!-- .stats.four for 4 across -->
<p class="kpi-note">Counts from the careers page, Nov 6, 2026.</p>

<table class="glance"><tr><th>Founded</th><td>2019 <span class="tag verified">Verified</span></td></tr></table>
<span class="tag reported">Reported</span> <span class="tag claim">Company claim</span> <span class="tag estimate">Estimate</span> <span class="tag unknown">Unknown</span>

<div class="score"><div class="k">Stability</div><div class="meter"><i class="on"></i><i class="on"></i><i></i><i></i><i></i></div><div class="why">Evidence.</div></div>
<div class="timeline"><div class="tl"><div class="when">2019</div><div>Founded in Austin by …</div></div></div>
<table class="data"><thead><tr><th>…</th></tr></thead><tbody><tr class="us"><td>…</td><td class="num">…</td></tr></tbody></table>
<div class="cols"><div class="card good"><h4>Praised</h4><ul><li>…</li></ul></div><div class="card bad"><h4>Criticized</h4>…</div></div>   <!-- .cols.three, .card.plain -->
<div class="people"><div class="person"><div class="name">…</div><div class="role">…</div><p>…</p></div></div>
<blockquote><p>“…”</p><cite>Glassdoor · Designer · Mar 2026</cite></blockquote>
<div class="swatches"><div class="sw"><div class="chip" style="background:#…"></div><div class="lbl"><b>Name</b>#HEX · use</div></div></div>
<div class="type-spec"><div class="sample" style="font-family:var(--font-display)">Headline</div><div class="small muted">Font · foundry · stand-in note</div></div>
<div class="media"><div class="item"><div class="date">Oct 2026</div><div><div class="t"><a href="…">Title</a></div><div class="src">Outlet · format · length</div><p>Takeaway.</p></div></div></div>
<dl class="lingo"><dt>Term</dt><dd>Meaning</dd></dl>
<ol class="big"><li>Question? <span class="why">Why it matters.</span></li></ol>
<ol class="sources"><li><a href="…">Title</a> <span class="d">· Outlet · date</span></li></ol>

<!-- brand kit row: link on the asset name; tag shows official vs third-party; status is one of Current, Dated, Outdated, Request access, Not found -->
<table class="data"><thead><tr><th>Asset</th><th>Format</th><th>Source</th><th>Date</th><th>Status</th></tr></thead>
<tbody><tr><td><b><a href="…">Primary logo</a></b></td><td>SVG, EPS</td><td>Press kit <span class="tag verified">Official</span></td><td class="num">Mar 2026</td><td>Current</td></tr></tbody></table>
```

Utility classes: `.lede` (larger intro paragraph), `.muted`, `.small`, `.avoid-break`.

## Writing rules

- Plain, specific, and confident. Lead each section with what matters, then the evidence. Tables and short bullets over long paragraphs.
- Every number has a source in the Sources list, a date, and a tag. Dates are absolute ("Oct 2026", never "last month").
- Use the company's own words for mission, values, and product names, in quotation marks.
- Quotes from employee reviews: short (25 words or fewer), 4 or fewer in total, attributed to platform and date. Summarize articles; don't paste them.
- Avoid buzzwords ("revolutionary", "cutting-edge", "game-changing", "seamless") except inside quotes you attribute.
- Avoid aphoristic one-liners and staged contrasts ("No X. Just Y.", "It's not A, it's B.", "Lead with it."). Write the full sentence.
- Never claim a check you didn't do. If you only read Glassdoor, say "Only Glassdoor was reviewed for this brief."
- People: titles, public work, and public statements only. No photos, personal contact details, or private life.
- Personal mode can name the reader's real work; shareable mode names no one but the company's public people.
- Brand kit: links only, each one opened before delivery, with the format you confirmed. Label third-party files `Third-party` (tag class `reported`) and official ones `Official` (tag class `verified`). Paraphrase guideline rules in one line each.
- Make every link clickable. Aim for 14–20 pages; don't pad.

## Cheat sheet and comparison

- **Cheat sheet** (`assets/cheatsheet-template.html`): one page, made from the finished brief with no new facts. Bottom line, six numbers, three things to know, the pitch (shareable: angles), 3–4 talking points, 4–5 terms, people to know, 4–5 questions, 2–3 risks, one do and one don't. If it spills onto a second page, cut items; don't shrink type below the template's sizes.
- **Comparison** (`assets/compare-template.html`): neutral tokens; each company's color appears only as `style="--co:#hex"` on its column header and `.co-dot`. Same rows for both companies. Mark the clearly stronger cell with `class="edge"` only when the difference is sourced. Scorecard rows use `.score.vs-score` with two meters.
- **What's changed** (refresh mode, in brief-template.html after the summary): Then / Now table with dates on both sides, then "New since last time" as `.media` items. Delete the whole part in a normal brief.

