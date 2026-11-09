---
name: print-listing-kit
description: Writes ready-to-paste listings for selling or sharing a 3D print model file on marketplaces such as Etsy, Printables, MakerWorld, Cults3D and Thangs - titles, descriptions, tags, print settings, assembly notes, license, price based on comparable models, a photo shot list and a download README - and checks titles and tags against each marketplace's limits with a script. Flags trademark and character risks and AI-disclosure rules. Use when someone wants to list, sell, upload or price an STL or 3MF model, write a 3D model description, or set up a 3D print file shop. Usage - /print-listing-kit followed by the model name, with photos or files attached.
---

# Print Listing Kit

Turn a finished 3D model into listings that get found and printed successfully: a title and tags people actually search, a description that sells it and sets expectations, the settings that worked, a fair price, the photos to take, and a README for the download. One kit covers every marketplace the person sells on.

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

## What to ask for, once

Collect from the conversation, memory and attachments first, then ask once for what's missing: what the model is and does, dimensions, the printer, material, layer height, infill, supports, print time and filament used for a real print, multi-part or assembly details, multi-color or AMS setup, whether the person designed it (fully, remixed, or with an AI tool, and which), the license they want, and the price goal.

**Files.** `<skill-dir>` means this skill's folder, the one holding this SKILL.md. Templates are in `assets/`, scripts in `scripts/`, and the shared PDF steps (fonts, colors, render, check) are in `references/rendering.md`.

## Hard rules

- **Only list what the person has rights to.** If the model depicts a trademarked character, logo, brand product, sports team, game or film property, or is a remix of someone else's model, say so before writing anything. Explain the risk, check the original's license for remixes, and offer to write the listing for an original or properly licensed version instead. Put those names in `watch_terms` so the checker catches them.
- **AI disclosure.** If any part of the model was made with an AI tool, look up each marketplace's current policy on AI-generated content and follow it in the listing. Don't rely on remembered rules; they change.
- **Settings come from a real print.** Only say "tested" or list print settings that the person actually used. Otherwise mark settings as suggested starting points.
- **Check every listing with `scripts/listing_check.py`.** Etsy's limits are built in (140-character title, 13 tags of up to 20 characters). For other marketplaces, look up current title, tag and description limits and add them to `limits` in `listing.json`.
- **Prices from real comparables.** Look at 4–8 similar models on each marketplace, note their prices, downloads or sales signals, and links, and recommend a price with that evidence. Pricing is the person's call; present options.
- **Honest photos.** Shot list uses real prints. Renders are labeled as renders where a marketplace expects that.

## Workflow

1. **Understand the model**: what it is, who it's for, why someone would print it, size, parts, print profile, and what makes it better than similar models (no supports, print-in-place, fits a standard part, tolerance-tested).
2. **Research search terms and comparables** on each marketplace (and Etsy search suggestions): the words buyers use, what top listings show in their first image, prices and licenses, and common complaints in reviews or comments to answer up front.
3. **Write `listing.json`** with, for each marketplace: title (front-load the searched words), tags, price, license and description. Description order: one-line hook; what it is and what it's for; features as short bullets; size and what's included (STL, 3MF with plate setup, parts count); print settings table; assembly steps; license in plain words; support or contact line.
4. **Check**: `python3 <skill-dir>/scripts/listing_check.py listing.json`. Fix every FAIL and rerun until it passes. It writes `listings.csv`.
5. **Write the kit** in `<Model>-Listing-Kit.md` from `assets/listing-kit-template.md`: per-marketplace copy ready to paste, pricing with comparables, photo shot list, file packaging checklist, and the download README.
6. **Write `README.txt`** for the download: model name, version, files included, print settings, assembly, license, and how to get help.
7. **Deliver** the kit, `listings.csv` and `README.txt`. In the reply: the recommended price and why, any IP or AI-disclosure issue, and the single most important photo to take.
