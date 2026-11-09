---
name: activation-concepts
description: Develops three experiential activation concepts for a brand at a venue, event or public space and delivers them as a designed 16:9 concept deck PDF with presenter notes. Each concept gets the big idea, the guest journey step by step, a simple floor plan diagram, materials and fabrication notes, tech, staffing, timeline, a budget range, risks and permits, and how success is measured. Use when someone asks for activation ideas, experiential concepts, a pop-up, booth or installation concept, a brand experience for an event, or a creative response to an activation brief. Usage - /activation-concepts followed by the brand, the venue or event, and a budget range.
---

# Activation Concepts

Turn a brand, a place and a budget into three experiential concepts a client can choose from: one safe, one stretch, one bold. Each concept explains what guests do, what gets built, what it costs roughly, and what could go wrong, so the conversation can move straight to "which one?".

## Usage

```
/activation-concepts <brand> at <venue or event> [budget range] [audience] [goal]
```

Plain requests work too:

- "Three activation concepts for Patagonia at Outside Lands, budget $150–250K."
- "Pop-up ideas for a skincare launch in a 1,200 sq ft SoHo storefront, two weeks."
- "We have a 20×20 booth at CES for a robotics startup. Give me concepts."
- "Here's the client brief (attached). Turn it into three activation concepts."
- Add "one concept" for a single concept in depth, or "rough" for a quick 6-slide version.

If the person has a brief, follow it exactly and quote its objectives back on the second slide. If key facts are missing (budget, footprint, dates, audience), pick sensible defaults, list them on the brief slide as assumptions, and say so in the reply.

**Files.** `<skill-dir>` means this skill's folder, the one holding this SKILL.md. Templates are in `assets/`, scripts in `scripts/`, and the shared PDF steps (fonts, colors, render, check) are in `references/rendering.md`.

## Hard rules

- **Buildable.** Every concept must be something a fabricator could quote: real materials, real dimensions, real tech that exists today. Flag anything that needs a specialist (rigging, structural engineering, permits, licensed electrical work, food handling, alcohol, drones, lasers aimed at crowds).
- **Budgets are ranges, labeled `Estimate`,** with what's included (design, fabrication, tech, staffing, logistics, permits, contingency) and what isn't. Never present a single precise number unless the person gave the costs.
- **Safety and access are part of the design.** Note crowd flow, capacity, ADA access (ramps, reach ranges, quiet options), weather plans for outdoor sites, and power needs.
- **The brand's own world.** Base ideas on the brand's real voice, products and recent marketing (research it). No logos or brand artwork reproduced in the deck; describe them, and use the brand's colors and type for the deck itself.
- **Credit others' work.** If a concept is close to a known activation, say so and say how this one differs.
- Keep `notes.md` as you research; tool results get cleared from context.

## Workflow

Make a task list from these steps and tick them off.

1. **Read the brief or build one.** Brand, objective (awareness, trial, sales, data capture, content, loyalty), audience, place and footprint, dates and hours, expected traffic, budget, must-haves, constraints (venue rules, union labor, load-in windows, sound limits). Write it as a short brief slide.
2. **Research** (10–20 lookups): the brand's recent campaigns, products, voice and audience; the venue or event (footprint, rules, typical activations there, audience); and 3–5 recent activations in the category, to avoid repeating them and to calibrate cost.
3. **Concept** three directions at different levels of risk:
   - **Safe:** proven format done exceptionally well.
   - **Stretch:** a familiar format with a twist only this brand could do.
   - **Bold:** a new idea that earns press and social on its own.
   Each needs a name, the idea in one sentence, why it fits the brand, and the moment people will photograph or talk about.
4. **Develop each concept:**
   - Guest journey in 4–6 steps, from first sight to leaving (and what they take with them: product, content, sign-up).
   - Floor plan as an inline SVG: footprint rectangle to scale, labeled zones, entry and exit arrows, queue area, staff positions. See the SVG pattern in the template.
   - Build: structure and materials, finishes, graphics, lighting, AV and interactive tech, power estimate, load-in and strike time.
   - Staffing: roles and counts per shift.
   - Throughput: guests per hour and how that was worked out (dwell time × capacity).
   - Budget range with a line-item breakdown by category, labeled `Estimate`.
   - Risks and mitigations, permits and approvals.
   - Measurement: KPIs tied to the objective, and how each is captured.
5. **Compare:** one table across the three concepts (impact, cost range, build time, risk, content potential, throughput), plus your recommendation and why.
6. **Brand the deck** in the brand's colors and type (references/brand-extraction.md). Use the brand's palette for floor-plan zones.
7. **Build** from `assets/concepts-template.html` following references/rendering.md (copy `base.css` and `deck.css`). Default: title, brief, insight, three concepts (3 slides each: idea and journey, floor plan and build, budget and risks), comparison, timeline, next steps.
8. **Presenter notes** in `<Brand>-Activation-Notes.md`: what to say for each slide and the questions the client is likely to ask.
9. **Render, audit and check** the contact sheet. Check every floor plan reads at a glance and every budget adds up (run the arithmetic).
10. **Deliver** the PDF and notes. In the reply: the three concept names in one line each, your recommendation, the assumptions that most affect cost, and one next step (site visit, fabricator quotes, or a mood board).

Output name: `<Brand>-Activation-Concepts-<YYYY-MM>.pdf`.

## Throughput and power, quick math

- Guests per hour ≈ (capacity of the experience at once) × (60 ÷ average dwell minutes). Add queue capacity for peak.
- Power: add up watts per device (LED wall, projectors, lighting, audio, compute), add 25% headroom, and divide by 120 V for amps in the US. A standard 20 A circuit gives about 1,900 W of continuous load; above that, plan dedicated circuits or a generator, and flag licensed electrical work.
