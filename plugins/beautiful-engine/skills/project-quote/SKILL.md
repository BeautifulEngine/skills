---
name: project-quote
description: Turns a project scope into a branded quote and statement of work PDF (phases, deliverables, hours and rates or fixed fees, contingency, payment schedule, assumptions, out of scope, timeline, terms and a signature block), with totals computed by a script so the math is always right. Also makes a one-page rate card of services and rates. Use when someone asks for a quote, estimate, proposal with pricing, SOW, budget for a creative or freelance project, a rate card, or help pricing a project. Usage - /project-quote followed by the client and a description of the work, or "rate card".
---

# Project Quote

Turn "here's what the client wants" into a quote a client can sign: what you'll make, in what phases, what it costs and why, when it's paid, what's assumed and what isn't included. The numbers come from a calculator script, never mental math. It also makes a one-page rate card.

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

## What to ask for, once

The person's own details make the quote theirs. Look in the conversation, memory and attached files first, then ask in one short message for whatever is missing:

- **Rates**: roles and hourly or day rates (or a past quote or rate card to copy from).
- **Studio details** for the letterhead: business name, contact, and colors or a logo file they attach. Their own logo can go on their own quote. Without one, use a clean typographic wordmark.
- **Payment terms** they use (deposit share, net days), if they have a standard.

If they say "just make it", proceed with clearly marked defaults: 50% on signing and 50% on delivery, net 15, two rounds of revisions per deliverable, 10% contingency, and valid for 30 days. List the defaults in the reply.

**Files.** `<skill-dir>` means this skill's folder, the one holding this SKILL.md. Templates are in `assets/`, scripts in `scripts/`, and the shared PDF steps (fonts, colors, render, check) are in `references/rendering.md`.

## Hard rules

- **All math goes through `scripts/quote_calc.py`.** Write `quote.json`, run the script, paste its tables. To change a number, edit the JSON and rerun. Never type a total by hand.
- **Hours have reasons.** Each phase lists deliverables, and each line item is a task a client would recognize. If you estimate hours, base them on the scope, say what drives the big ones, and keep them realistic for the person's seniority.
- **Never invent the person's rates.** If they ask "what should I charge?", research current market ranges for their role and region (design surveys, freelance platforms, job postings), cite them, tag them `Estimate`, and let them pick.
- **Scope is explicit both ways.** Every quote has "Included" deliverables and "Not included" items (stock, printing, media buys, extra revisions, travel, licensing fees for fonts or music), plus how changes are handled.
- **Not legal advice.** The terms are a sensible starting point. Recommend a lawyer for large or unusual contracts, and never claim the terms are enforceable.
- No Beautiful Engine credit or other third-party branding: the quote belongs to the person.

## Workflow

1. **Understand the work.** Client, project, deliverables, quantities, timeline, constraints, budget signal. If the person attached a brief or email, extract every deliverable from it.
2. **Plan phases** (usually Discovery, Concept, Design or Development, Production, Delivery) with deliverables and review points.
3. **Estimate** each phase as tasks with roles and hours, plus pass-through costs (printing, fabrication, travel, licenses) as fixed items. Decide hourly view or fixed fee per phase (`"show_hours": false`) based on what the person prefers; default to fixed fees per phase for clients, with hours kept in the JSON.
4. **Calculate**: `python3 <skill-dir>/scripts/quote_calc.py quote.json > tables.html`. It prints the total to stderr and fails if a role has no rate or the payment schedule doesn't add up to 100%. If there's a budget signal and the total misses it, offer options (reduce scope, phase the work, or a lighter tier) instead of shaving hours silently.
5. **Write the quote** from `assets/quote-template.html` following references/rendering.md (copy `base.css`): paste the ESTIMATE, SUMMARY and PAYMENTS blocks from `tables.html` where marked, fill the scope, assumptions, timeline and terms. Use the person's colors and fonts.
6. **Render, audit, check.** Confirm the total on page 1 matches the script's total exactly, and every deliverable in the client's request appears in the scope.
7. **Deliver** the PDF, plus `quote.json` so it can be revised later. In the reply: the total, the payment schedule in one line, the assumptions that carry the most risk, and any defaults you used.

Output name: `<Studio>-Quote-<Client>-<Project>-<YYYY-MM-DD>.pdf`, with a quote number like `Q-<YYYYMMDD>-01`.

## Rate card

From `assets/ratecard-template.html`: services grouped by type, each with what's included and the rate (hourly, day, or "from" project price), minimums, rush fees, revision policy, payment terms and contact. One page. Output: `<Studio>-Rate-Card-<YYYY>.pdf`.

## Options and tiers

When the person wants options, make three tiers (for example Essential, Recommended, Complete) as separate phases or separate `quote.json` files, run the calculator for each, and show a comparison table on page 1 with the recommended tier marked.
