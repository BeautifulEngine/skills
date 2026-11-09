#!/usr/bin/env python3
"""Check 3D model listings against each marketplace's limits and write listings.csv.

Usage:
  python3 listing_check.py listing.json

listing.json:
{
  "model": "Modular Desk Planter",
  "watch_terms": ["pokemon", "marvel"],        # optional: words to flag (brands, characters)
  "limits": {                                  # verify current limits before relying on these
    "etsy": {"title": 140, "tags": 13, "tag_len": 20}
  },
  "listings": {
    "etsy":      {"title": "...", "tags": ["..."], "price": 6.5, "license": "Personal use", "description": "..."},
    "printables": {"title": "...", "tags": ["..."], "price": 0, "license": "CC BY-NC", "description": "..."}
  }
}
Etsy's limits (title 140 characters, 13 tags of up to 20 characters) are built in; add others
under "limits" after checking each marketplace's current rules. Exits non-zero on any FAIL.
"""
import csv
import json
import sys

DEFAULTS = {"etsy": {"title": 140, "tags": 13, "tag_len": 20}}


def main():
    d = json.load(open(sys.argv[1]))
    limits = {**DEFAULTS, **{k.lower(): v for k, v in d.get("limits", {}).items()}}
    watch = [w.lower() for w in d.get("watch_terms", [])]
    fails = 0
    rows = []
    for market, L in d["listings"].items():
        lim = limits.get(market.lower(), {})
        title, tags, desc = L.get("title", ""), L.get("tags", []), L.get("description", "")
        msgs = []
        if "title" in lim and len(title) > lim["title"]:
            msgs.append(f"FAIL title is {len(title)} characters (limit {lim['title']})")
        if "tags" in lim and len(tags) > lim["tags"]:
            msgs.append(f"FAIL {len(tags)} tags (limit {lim['tags']})")
        for t in tags:
            if "tag_len" in lim and len(t) > lim["tag_len"]:
                msgs.append(f"FAIL tag '{t}' is {len(t)} characters (limit {lim['tag_len']})")
        dupes = {t for t in tags if [x.lower() for x in tags].count(t.lower()) > 1}
        if dupes:
            msgs.append("WARN duplicate tags: " + ", ".join(sorted(dupes)))
        if not lim:
            msgs.append("note: no limits on file for this marketplace; check its current rules")
        text = " ".join([title, desc, " ".join(tags)]).lower()
        hits = [w for w in watch if w in text]
        if hits:
            msgs.append("FAIL mentions watched terms (trademark or character risk): " + ", ".join(hits))
        if not L.get("license"):
            msgs.append("WARN no license set")
        fails += sum(m.startswith("FAIL") for m in msgs)
        status = "ok" if not any(m.startswith(("FAIL", "WARN")) for m in msgs) else ""
        print(f"[{market}] title {len(title)} chars, {len(tags)} tags {status}")
        for m in msgs:
            print("  " + m)
        rows.append({"marketplace": market, "title": title, "tags": ", ".join(tags), "price": L.get("price", ""),
                     "license": L.get("license", ""), "description": desc})
    with open("listings.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["marketplace", "title", "tags", "price", "license", "description"])
        w.writeheader()
        w.writerows(rows)
    print("wrote listings.csv")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
