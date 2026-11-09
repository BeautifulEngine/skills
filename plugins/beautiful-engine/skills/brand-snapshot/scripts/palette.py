#!/usr/bin/env python3
"""Turn a brand's colors and fonts into design tokens plus a swatch table with contrast checks.

Usage:
  python3 palette.py --colors "Ink:#141213,Mint:#40DE9E,Forest:#0F492E,Paper:#FFFFFF" \
      --font-display "Inter Tight" --font-body "Inter" --font-mono "DM Mono" \
      --radius 10px --brand "Acme" > swatches.html

Writes tokens.json (W3C design tokens format) and tokens.css beside where it's run,
and prints an HTML swatch table for the snapshot: each color with hex, RGB, and its
contrast against white and against the darkest color, marked for text use (AA 4.5:1)
and large text or shapes (3:1).
"""
import argparse
import html
import json
import re
import sys


def rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(h):
    def f(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb(h)
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True)
    return (x + 0.05) / (y + 0.05)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def grade(r):
    return "Text" if r >= 4.5 else ("Large text, shapes" if r >= 3 else "Decoration only")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--colors", required=True, help='comma list of Name:#hex, most important first')
    ap.add_argument("--font-display")
    ap.add_argument("--font-body")
    ap.add_argument("--font-mono")
    ap.add_argument("--radius")
    ap.add_argument("--brand", default="brand")
    a = ap.parse_args()

    colors = []
    for part in a.colors.split(","):
        name, _, hexv = part.rpartition(":")
        hexv = "#" + hexv.strip().lstrip("#").upper()
        rgb(hexv)  # validates
        colors.append((name.strip() or hexv, hexv))
    darkest = min((c[1] for c in colors), key=lum)

    tokens = {"color": {slug(n): {"$type": "color", "$value": h} for n, h in colors}}
    fonts = {k: v for k, v in (("display", a.font_display), ("body", a.font_body), ("mono", a.font_mono)) if v}
    if fonts:
        tokens["font"] = {k: {"$type": "fontFamily", "$value": v} for k, v in fonts.items()}
    if a.radius:
        tokens["radius"] = {"default": {"$type": "dimension", "$value": a.radius}}
    json.dump({slug(a.brand): tokens}, open("tokens.json", "w"), indent=2)

    css = [f"/* {a.brand} design tokens, from the live site. Check against official guidelines before production use. */", ":root {"]
    css += [f"  --color-{slug(n)}: {h};" for n, h in colors]
    css += [f'  --font-{k}: "{v}";' for k, v in fonts.items()]
    if a.radius:
        css.append(f"  --radius: {a.radius};")
    css.append("}")
    open("tokens.css", "w").write("\n".join(css) + "\n")

    rows = ['<table class="data swatch-table"><thead><tr><th></th><th>Name</th><th>Hex</th><th>RGB</th>'
            '<th class="num">On white</th><th class="num">With darkest</th><th>Use for</th></tr></thead><tbody>']
    dark_name = next(n for n, h in colors if h == darkest)
    for n, h in colors:
        cw, cd = contrast(h, "#FFFFFF"), contrast(h, darkest)
        best = max(cw, cd)
        on = "white" if cw >= cd else dark_name
        rows.append(f'<tr><td><span class="chip" style="background:{h}"></span></td><td><b>{html.escape(n)}</b></td><td>{h}</td>'
                    f'<td>{", ".join(map(str, rgb(h)))}</td><td class="num">{cw:.1f}:1</td>'
                    f'<td class="num">{"—" if h == darkest else f"{cd:.1f}:1"}</td><td>{grade(best) + ("" if best < 3 else f" on {html.escape(on)}")}</td></tr>')
    rows.append("</tbody></table>")
    print("\n".join(rows))
    print("wrote tokens.json and tokens.css", file=sys.stderr)


if __name__ == "__main__":
    main()
