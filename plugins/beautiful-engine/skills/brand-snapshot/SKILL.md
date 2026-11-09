---
name: brand-snapshot
description: Reads any brand's live website and returns a two-page brand snapshot PDF plus design tokens (JSON and CSS) - the color palette with hex, RGB and contrast checks, typefaces with free stand-ins, the logo described in words with links to official files, UI patterns like corner radius and buttons, voice samples, imagery style, and where the official guidelines live. Use when someone asks for a brand's colors, fonts, style, brand guidelines summary, design tokens, or a quick brand reference before starting design work. Usage - /brand-snapshot followed by a website URL or brand name.
---

# Brand Snapshot

Get a brand's visual and verbal basics onto two pages in minutes: colors you can use with confidence, the type and its free stand-ins, how the logo and UI behave, how the brand sounds, and links to the official files. It's the quick version of the brand section in the Company Brief skill.

## Usage

```
/brand-snapshot <url or brand name> [tokens only]
```

Plain requests work too:

- "Brand snapshot for linear.app."
- "What colors and fonts does Patagonia use?"
- "Pull design tokens from stripe.com for a pitch mockup."
- "Snapshot of Oatly and Liquid Death, side by side." (makes one snapshot each)

"tokens only" skips the PDF and returns `tokens.json` and `tokens.css`.

**Files.** `<skill-dir>` means this skill's folder, the one holding this SKILL.md. Templates are in `assets/`, scripts in `scripts/`, and the shared PDF steps (fonts, colors, render, check) are in `references/rendering.md`.

## Hard rules

- **Live site first.** Colors and fonts come from the site's computed styles (references/brand-extraction.md), tagged `Verified` and dated. Official guidelines or a press kit win over the site when they disagree; note both. Third-party sources like Brandfetch are `Reported`.
- **Describe logos, don't copy them.** Describe the mark and wordmark in words and link the official press kit or brand portal. Never redraw, trace, or embed a logo, mascot or ad imagery. Swatches and type specimens set in a stand-in font are fine.
- **Say what's a stand-in.** If a brand font is paid or custom, name it, name its foundry, and set specimens in the closest free match, labeled as such.
- **Usage terms apply.** Remind the reader that the brand's assets belong to the brand and its guidelines govern use.
- **Credit line:** the snapshot ends with a small Beautiful Engine credit. Keep it unless the person asks to leave it out.

## Workflow

1. **Open the site** in a browser if one is available (approve the domain once if asked); otherwise fetch it. Confirm it's the brand the person means.
2. **Extract** with the script in references/brand-extraction.md, section 1, on the homepage and one more page (pricing, product or about): headline style, loaded fonts, colors by on-screen area, stylesheet colors, CSS custom properties, gradients, button and card styles, and logo info. Zoom a screenshot on the logo to describe it, and on the hero to describe the imagery.
3. **Check official sources**: search for the brand's press kit, brand portal, design system site or guidelines PDF, and the foundry for its typefaces. Note sub-brands (events, product lines) separately.
4. **Choose the palette**: 4–8 colors in order of importance (primary, secondary, accents, neutrals), each with a plain name and role. Then run:
   `python3 <skill-dir>/scripts/palette.py --colors "Name:#hex,..." --font-display "…" --font-body "…" --font-mono "…" --radius 8px --brand "<Brand>" > swatches.html`
   It writes `tokens.json` and `tokens.css` and prints the swatch table with contrast checks.
5. **Fonts for the PDF**: install the brand's free fonts or stand-ins with `scripts/fonts.py`, and run `scripts/tokens.py` with the brand's primary and accent so the snapshot itself wears the brand (references/rendering.md).
6. **Voice**: 3–4 traits, each with a real line from the site in quotes.
7. **Build** from `assets/snapshot-template.html` (copy `base.css`), paste the swatch table, render, audit, and check the contact sheet. Two pages; trim rather than spill onto a third.
8. **Deliver** the PDF, `tokens.json` and `tokens.css`. In the reply: the primary and accent colors with hex, the fonts and stand-ins, and where the official guidelines are (or that none are public).

Output name: `<Brand>-Brand-Snapshot-<YYYY-MM>.pdf`.
