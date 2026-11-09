---
name: build-spec
description: Turns a design, sketch, photo, CAD file or description of something to make into a fabrication package PDF plus a bill of materials CSV - overview diagram, parts and cut lists, sheet counts, file checklists and starting settings for laser cutting, 3D printing and CNC, hardware, a power budget with battery runtime, tools, numbered build steps with checkpoints, finishing, install and teardown, safety, vendors and a timeline. Totals come from a calculator script. Use when someone asks for a build spec, fabrication plan, BOM, cut list, how to build a prop, sign, installation, booth element, art car or festival piece, or a parts list for a maker project. Usage - /build-spec followed by what you're building and its size.
---

# Build Spec

Turn "here's what I want to build" into a package someone could build from: what it is, every part and what it costs, how to cut and print the parts, how much power it pulls, the order to build it in, and how to install it and take it down safely.

## Usage

```
/build-spec <what you're building> [size] [where it will live] [tools you have] [budget] [deadline]
```

Plain requests work too:

- "Build spec for an 8 ft tall LED-lit sign that says OPEN LATE, for an outdoor festival, running off a battery."
- "Here's a sketch (attached) of a DJ booth facade. Make a cut list for 1/2 in plywood."
- "Parts list and build plan for a 3D printed lamp, 300 mm tall, on a Bambu H2D."
- "Fabrication plan for this booth element from our activation deck."
- Add "quick" for a two-page version: BOM, cut list and build steps only.

## Ask for the shop, once

What the person can build with changes the plan. Check the conversation, memory and attached files first, then ask once for anything missing: the machines they have and their bed or build-volume sizes (laser, 3D printer, CNC), hand and power tools, where it will be built and where it will live (indoor, outdoor, desert, venue rules), power available (wall, generator, battery), budget and deadline. If they say "just go", assume a standard home shop (circular saw, drill, jigsaw, sander) and say so.

**Files.** `<skill-dir>` means this skill's folder, the one holding this SKILL.md. Templates are in `assets/`, scripts in `scripts/`, and the shared PDF steps (fonts, colors, render, check) are in `references/rendering.md`.

## Hard rules

- **All totals go through `scripts/bom_calc.py`**: material costs, power draw, battery runtime, circuits and sheet counts. Write `bom.csv` (and `cuts.csv`), run the script, paste its tables. Never add up costs by hand.
- **Prices are estimates with sources.** Look up current prices from real vendors and link them. Note the date you checked.
- **Settings are starting points.** Laser, print and CNC settings vary by machine and material batch. Label them "starting point, test on scrap first".
- **Safety is part of the spec, not a footnote:**
  - Never laser-cut PVC, vinyl, or anything with chlorine (it releases chlorine gas), and flag polycarbonate, ABS and fiberglass as poor laser materials. Laser cutting needs ventilation and a fire watch.
  - Prefer low-voltage DC for anything people touch. Fuse every battery output and size wire for the current. Anything wired to mains power, or a generator distribution panel, should be done or checked by a licensed electrician; say so.
  - Structures people climb on, stand under, or that must survive wind (tall signs, shade structures, rigging overhead) need an engineer's or rigger's review; say so and give the loads you can.
  - Note PPE, ventilation for resins and paints, and fire safety for events.
- **Respect the design's owner.** Build what the person designed or described. Don't copy a commercial product's protected design or a brand's artwork into the files.
- **Credit line:** the spec ends with a small Beautiful Engine credit. Keep it unless the person asks to leave it out.
- Keep `notes.md` as you research; tool results get cleared from context.

## Workflow

1. **Understand the object**: what it does, overall dimensions, where it lives, how it gets there (does it need to break down to fit a vehicle?), how long it must last, and the budget. Read attached sketches, photos, CAD or STL files for dimensions.
2. **Break it into parts and sub-assemblies.** Choose a material and process for each part (sheet goods, lumber, printed parts, laser-cut parts, metal, off-the-shelf), favoring what the person's shop can make.
3. **Draw an overview**: an inline SVG with front and side views, overall dimensions, and labeled sub-assemblies (see the template's diagram block).
4. **Write `bom.csv`** with category, part, qty, unit, unit_cost, source (a URL where possible), notes, and watts for anything electrical. **Write `cuts.csv`** for sheet parts with width_in, height_in and material.
5. **Calculate**: `python3 <skill-dir>/scripts/bom_calc.py bom.csv --cuts cuts.csv --sheet 48x96 --bed <laser bed> [--volts 12] [--battery-wh N] [--tax N] > tables.html`. Read the WARN lines: resolve every part that doesn't fit a sheet or the bed (split it, change the process, or change the design).
6. **Files and settings**: for each process, list the files needed (DXF or SVG for laser and CNC with layers for cut, score and engrave; STL or 3MF for printing), material and thickness, starting settings, orientation and supports for prints, estimated machine time, and whether files exist or need making.
7. **Build steps**: numbered, in the order that avoids rework, grouped by sub-assembly, each with the tools needed and a checkpoint ("dry-fit before glue", "test LEDs before sealing").
8. **Finishing, transport, install and teardown**: finishes and cure times, how it breaks down, crate or packing notes, crew and time to install, anchoring and ballast, and strike.
9. **Timeline** backward from the deadline, including ordering lead times and print or cut machine hours.
10. **Build the PDF** from `assets/spec-template.html` following references/rendering.md (copy `base.css`). Use the person's own colors if they have a studio brand; otherwise near-black with one accent.
11. **Render, audit, check** the contact sheet, and re-read the safety section against what the build actually involves.
12. **Deliver** the PDF, `bom-totals.csv` and `cuts.csv`. In the reply: the total materials estimate, power and runtime if relevant, the riskiest step, anything that needs a professional, and the first thing to order (longest lead time).

Output name: `<Project>-Build-Spec-<YYYY-MM>.pdf`.
