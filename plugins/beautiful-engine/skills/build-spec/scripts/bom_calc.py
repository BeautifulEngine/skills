#!/usr/bin/env python3
"""Totals for a build: bill of materials, power budget, and sheet-goods estimate.

Usage:
  python3 bom_calc.py bom.csv [--cuts cuts.csv] [--sheet 48x96] [--waste 15] [--bed 24x16]
                      [--volts 120] [--headroom 25] [--battery-wh 3600] [--tax 9.5] > tables.html

bom.csv columns (header row required):
  category,part,qty,unit,unit_cost,source,notes,watts
  - watts is per unit and optional; rows with watts go into the power budget.
cuts.csv columns (optional):
  part,qty,width_in,height_in,material[,sheet_in]
  - estimates how many sheets of each material you need (area x waste), and flags parts
    that don't fit the sheet or the laser bed. sheet_in (e.g. 24x18) overrides --sheet for
    that material, for stock that comes in other sizes such as acrylic.

Prints HTML tables (BOM, power, sheets) to stdout and a JSON summary to stderr.
Writes bom-totals.csv beside bom.csv with line totals. Everything printed is an estimate.
"""
import argparse
import csv
import html
import json
import math
import os
import sys
from collections import OrderedDict


def num(v, default=0.0):
    try:
        return float(str(v).replace("$", "").replace(",", "").strip())
    except ValueError:
        return default


def dims(s):
    w, h = s.lower().split("x")
    return float(w), float(h)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bom")
    ap.add_argument("--cuts")
    ap.add_argument("--sheet", default="48x96", help="sheet size in inches, WxH")
    ap.add_argument("--waste", type=float, default=15, help="waste and kerf allowance, %%")
    ap.add_argument("--bed", help="laser or CNC bed size in inches, WxH")
    ap.add_argument("--volts", type=float, default=120)
    ap.add_argument("--headroom", type=float, default=25, help="power headroom, %%")
    ap.add_argument("--battery-wh", type=float, help="battery capacity in Wh, for runtime")
    ap.add_argument("--tax", type=float, default=0, help="sales tax %% on materials")
    a = ap.parse_args()

    rows = list(csv.DictReader(open(a.bom, newline="")))
    groups = OrderedDict()
    subtotal, power_rows, warnings = 0.0, [], []
    for r in rows:
        qty, cost = num(r.get("qty"), 1), num(r.get("unit_cost"))
        line = qty * cost
        r["line_total"] = f"{line:.2f}"
        subtotal += line
        groups.setdefault(r.get("category") or "Parts", []).append(r)
        if not r.get("unit_cost"):
            warnings.append(f"no unit_cost for '{r.get('part')}'")
        w = num(r.get("watts"))
        if w:
            power_rows.append((r.get("part", ""), qty, w, qty * w))

    out = ['<table class="data">', '<thead><tr><th>Part</th><th class="num">Qty</th><th>Unit</th><th class="num">Each</th>'
           '<th class="num">Total</th><th>Source</th><th>Notes</th></tr></thead><tbody>']
    for cat, items in groups.items():
        out.append(f'<tr class="us"><td colspan="7"><b>{html.escape(cat)}</b></td></tr>')
        for r in items:
            src = r.get("source", "")
            src_html = f'<a href="{html.escape(src)}">link</a>' if src.startswith("http") else html.escape(src)
            out.append(f'<tr><td>{html.escape(r.get("part", ""))}</td><td class="num">{num(r.get("qty"), 1):g}</td>'
                       f'<td>{html.escape(r.get("unit", ""))}</td><td class="num">${num(r.get("unit_cost")):,.2f}</td>'
                       f'<td class="num">${num(r["line_total"]):,.2f}</td><td>{src_html}</td><td>{html.escape(r.get("notes", ""))}</td></tr>')
    tax = subtotal * a.tax / 100
    out.append(f'<tr class="us"><td colspan="4"><b>Materials subtotal</b></td><td class="num"><b>${subtotal:,.2f}</b></td><td colspan="2"></td></tr>')
    if tax:
        out.append(f'<tr class="us"><td colspan="4">Tax ({a.tax:g}%)</td><td class="num">${tax:,.2f}</td><td colspan="2"></td></tr>')
        out.append(f'<tr class="us"><td colspan="4"><b>Total</b></td><td class="num"><b>${subtotal + tax:,.2f}</b></td><td colspan="2"></td></tr>')
    out.append("</tbody></table>")

    summary = {"materials_subtotal": round(subtotal, 2), "tax": round(tax, 2), "total": round(subtotal + tax, 2), "lines": len(rows)}

    if power_rows:
        total_w = sum(p[3] for p in power_rows)
        planned_w = total_w * (1 + a.headroom / 100)
        amps = planned_w / a.volts
        circuits = math.ceil(planned_w / (a.volts * 20 * 0.8)) if a.volts >= 100 else None
        out.append('<h4>Power budget</h4>\n<table class="data"><thead><tr><th>Device</th><th class="num">Qty</th>'
                   '<th class="num">Watts each</th><th class="num">Watts</th></tr></thead><tbody>')
        for part, qty, w, tw in power_rows:
            out.append(f'<tr><td>{html.escape(part)}</td><td class="num">{qty:g}</td><td class="num">{w:g}</td><td class="num">{tw:,.0f}</td></tr>')
        out.append(f'<tr class="us"><td colspan="3">Total draw</td><td class="num">{total_w:,.0f} W</td></tr>')
        out.append(f'<tr class="us"><td colspan="3">With {a.headroom:g}% headroom</td><td class="num"><b>{planned_w:,.0f} W</b> · {amps:,.1f} A at {a.volts:g} V</td></tr>')
        if circuits:
            out.append(f'<tr class="us"><td colspan="3">20 A circuits needed (80% continuous rule)</td><td class="num">{circuits}</td></tr>')
        if a.battery_wh:
            hours = a.battery_wh * 0.85 / total_w
            out.append(f'<tr class="us"><td colspan="3">Runtime on {a.battery_wh:,.0f} Wh battery (85% usable, at total draw)</td><td class="num">{hours:,.1f} h</td></tr>')
            summary["battery_hours"] = round(hours, 1)
        out.append("</tbody></table>")
        summary.update({"draw_w": round(total_w), "planned_w": round(planned_w), "amps": round(amps, 1), "circuits_20a": circuits})

    if a.cuts:
        bed = dims(a.bed) if a.bed else None
        by_mat = OrderedDict()
        for c in csv.DictReader(open(a.cuts, newline="")):
            q, w, h = num(c.get("qty"), 1), num(c.get("width_in")), num(c.get("height_in"))
            mat = c.get("material") or "sheet"
            size = (c.get("sheet_in") or "").strip() or a.sheet
            mw, mh = dims(size)
            key = (mat, size)
            by_mat[key] = by_mat.get(key, 0) + q * w * h
            fits_sheet = (w <= mw and h <= mh) or (w <= mh and h <= mw)
            if not fits_sheet:
                warnings.append(f"'{c.get('part')}' ({w:g}x{h:g} in) is bigger than a {size} sheet: split it or join panels")
            if bed and not ((w <= bed[0] and h <= bed[1]) or (w <= bed[1] and h <= bed[0])):
                warnings.append(f"'{c.get('part')}' ({w:g}x{h:g} in) won't fit the {a.bed} bed: cut it on a CNC or split it")
        out.append(f'<h4>Sheet goods</h4>\n<table class="data"><thead><tr><th>Material</th><th>Sheet size (in)</th><th class="num">Part area (sq ft)</th>'
                   f'<th class="num">Sheets (+{a.waste:g}% waste)</th></tr></thead><tbody>')
        sheets = {}
        for (mat, size), area in by_mat.items():
            mw, mh = dims(size)
            n = math.ceil(area * (1 + a.waste / 100) / (mw * mh))
            sheets[f"{mat} ({size})"] = n
            out.append(f'<tr><td>{html.escape(mat)}</td><td>{mw:g} × {mh:g}</td><td class="num">{area / 144:,.1f}</td><td class="num">{n}</td></tr>')
        out.append("</tbody></table>")
        out.append('<p class="small muted">Sheet counts come from part area plus a waste allowance; real nesting can need one more sheet. Check the layout in your nesting or laser software.</p>')
        summary["sheets"] = sheets

    base, _ = os.path.splitext(a.bom)
    with open(base + "-totals.csv", "w", newline="") as f:
        wtr = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["part"])
        wtr.writeheader()
        wtr.writerows(rows)

    print("\n".join(out))
    print(json.dumps(summary), file=sys.stderr)
    for w in warnings:
        print("WARN " + w, file=sys.stderr)


if __name__ == "__main__":
    main()
