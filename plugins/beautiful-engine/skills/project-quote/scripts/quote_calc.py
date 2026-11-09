#!/usr/bin/env python3
"""Compute a project quote from a JSON file and print the HTML tables for quote-template.html.

Usage:
  python3 quote_calc.py quote.json > tables.html      # tables to paste at the ESTIMATE marker
  python3 quote_calc.py quote.json --check            # totals only

quote.json:
{
  "currency": "USD",
  "rates": {"Design Director": 175, "Designer": 120},       # per hour
  "show_hours": true,                                         # false = fixed fee per phase, hours hidden
  "phases": [
    {"name": "Discovery", "items": [
      {"task": "Kickoff and research", "role": "Design Director", "hours": 6},
      {"task": "Moodboards", "role": "Designer", "hours": 10},
      {"task": "Venue survey travel", "fixed": 450, "note": "pass-through"}
    ]}
  ],
  "passthrough_markup_pct": 0,    # added to items with "fixed"
  "contingency_pct": 10,          # optional
  "discount_pct": 0,              # optional, applied before contingency and tax
  "tax_pct": 0,                   # optional
  "payment_schedule": [{"milestone": "On signing", "pct": 50}, {"milestone": "On final delivery", "pct": 50}]
}
Totals and the payment schedule are checked: the schedule must add up to 100%.
"""
import html
import json
import sys

SYMBOLS = {"USD": "$", "CAD": "CA$", "AUD": "A$", "EUR": "€", "GBP": "£", "JPY": "¥"}


def money(x, cur):
    sym = SYMBOLS.get(cur, cur + " ")
    sign, x = ("−" if x < 0 else ""), abs(x)
    return f"{sign}{sym}{x:,.0f}" if abs(x - round(x)) < 0.005 else f"{sign}{sym}{x:,.2f}"


def main():
    q = json.load(open(sys.argv[1]))
    cur = q.get("currency", "USD")
    rates = q.get("rates", {})
    show_hours = q.get("show_hours", True)
    markup = q.get("passthrough_markup_pct", 0) / 100
    out, phase_rows, errors = [], [], []
    subtotal = hours_total = 0.0

    for ph in q["phases"]:
        rows, ph_total, ph_hours = [], 0.0, 0.0
        for it in ph["items"]:
            if "fixed" in it:
                amt = it["fixed"] * (1 + markup)
                rows.append((it["task"], it.get("note", ""), "", "", amt))
            else:
                role = it["role"]
                if role not in rates:
                    errors.append(f"no rate for role '{role}' (task '{it['task']}')")
                    continue
                amt = it["hours"] * rates[role]
                ph_hours += it["hours"]
                rows.append((it["task"], role, f"{it['hours']:g}", money(rates[role], cur), amt))
            ph_total += amt
        subtotal += ph_total
        hours_total += ph_hours
        phase_rows.append((ph["name"], ph_hours, ph_total))
        if show_hours:
            out.append(f'<h4>{html.escape(ph["name"])}</h4>\n<table class="data">\n<thead><tr><th>Task</th><th>Role</th>'
                       '<th class="num">Hours</th><th class="num">Rate</th><th class="num">Amount</th></tr></thead><tbody>')
            for task, role, hrs, rate, amt in rows:
                out.append(f'<tr><td>{html.escape(task)}</td><td>{html.escape(role)}</td><td class="num">{hrs}</td>'
                           f'<td class="num">{rate}</td><td class="num">{money(amt, cur)}</td></tr>')
            out.append(f'<tr class="us"><td colspan="4"><b>{html.escape(ph["name"])} total</b></td><td class="num"><b>{money(ph_total, cur)}</b></td></tr></tbody></table>')

    discount = subtotal * q.get("discount_pct", 0) / 100
    after_discount = subtotal - discount
    contingency = after_discount * q.get("contingency_pct", 0) / 100
    pretax = after_discount + contingency
    tax = pretax * q.get("tax_pct", 0) / 100
    total = pretax + tax

    summary = ['<table class="data summary">\n<thead><tr><th>Phase</th>' + ('<th class="num">Hours</th>' if show_hours else '') +
               '<th class="num">Amount</th></tr></thead><tbody>']
    for name, hrs, amt in phase_rows:
        summary.append(f'<tr><td>{html.escape(name)}</td>' + (f'<td class="num">{hrs:g}</td>' if show_hours else '') +
                       f'<td class="num">{money(amt, cur)}</td></tr>')
    span = 2 if show_hours else 1

    def line(label, amt, bold=False):
        b0, b1 = ("<b>", "</b>") if bold else ("", "")
        return f'<tr class="us"><td colspan="{span}">{b0}{label}{b1}</td><td class="num">{b0}{money(amt, cur)}{b1}</td></tr>'
    summary.append(line("Subtotal", subtotal))
    if discount:
        summary.append(line(f"Discount ({q['discount_pct']:g}%)", -discount))
    if contingency:
        summary.append(line(f"Contingency ({q['contingency_pct']:g}%)", contingency))
    if tax:
        summary.append(line(f"Tax ({q['tax_pct']:g}%)", tax))
    summary.append(line("Total", total, bold=True))
    summary.append("</tbody></table>")

    sched = q.get("payment_schedule", [])
    pct_sum = sum(s["pct"] for s in sched)
    if sched and abs(pct_sum - 100) > 0.01:
        errors.append(f"payment schedule adds up to {pct_sum:g}%, not 100%")
    pay = ['<table class="data">\n<thead><tr><th>Payment</th><th class="num">Share</th><th class="num">Amount</th></tr></thead><tbody>']
    for s in sched:
        pay.append(f'<tr><td>{html.escape(s["milestone"])}</td><td class="num">{s["pct"]:g}%</td><td class="num">{money(total * s["pct"] / 100, cur)}</td></tr>')
    pay.append("</tbody></table>")

    report = {"subtotal": round(subtotal, 2), "discount": round(discount, 2), "contingency": round(contingency, 2),
              "tax": round(tax, 2), "total": round(total, 2), "hours": hours_total, "total_display": money(total, cur)}
    print(json.dumps(report), file=sys.stderr)
    for e in errors:
        print("FAIL " + e, file=sys.stderr)
    if "--check" in sys.argv:
        sys.exit(1 if errors else 0)
    print("<!-- ESTIMATE (generated by quote_calc.py; edit quote.json and rerun rather than editing numbers here) -->")
    print("\n".join(out))
    print("<!-- SUMMARY -->")
    print("\n".join(summary))
    print("<!-- PAYMENTS -->")
    print("\n".join(pay))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
