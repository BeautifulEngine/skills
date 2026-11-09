#!/usr/bin/env python3
"""Turn a resume or cover letter written in simple Markdown into an ATS-friendly .docx,
and optionally an HTML fragment for the PDF template.

Usage:
  python3 md_doc.py resume.md Resume.docx [--font Calibri] [--size 10.5] [--margin 0.7] [--html resume-body.html]

Markdown it understands (keep to this, so applicant tracking systems read the result):
  # Full Name                  -> name at the top
  a line right after the name  -> contact line (email · phone · city · portfolio URL)
  ## Section                   -> section heading (Experience, Skills, Education...)
  ### Title, Company | Dates   -> role line; the part after " | " is right-aligned dates
  - bullet                     -> bullet point
  plain lines                  -> paragraphs (cover letters)
  **bold** and *italic*        -> inline emphasis
Needs python-docx (pip install python-docx).
"""
import argparse
import html
import re
import sys

INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")


def runs(par, text, size=None, bold=False):
    for part in INLINE.split(text):
        if not part:
            continue
        b, i = bold, False
        if part.startswith("**") and part.endswith("**"):
            part, b = part[2:-2], True
        elif part.startswith("*") and part.endswith("*"):
            part, i = part[1:-1], True
        r = par.add_run(part)
        r.bold, r.italic = b, i
        if size:
            r.font.size = size


def inline_html(text):
    t = html.escape(text)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    return re.sub(r"\*([^*]+)\*", r"<i>\1</i>", t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--font", default="Calibri")
    ap.add_argument("--size", type=float, default=10.5)
    ap.add_argument("--margin", type=float, default=0.7)
    ap.add_argument("--html")
    a = ap.parse_args()
    try:
        from docx import Document
        from docx.enum.text import WD_TAB_ALIGNMENT
        from docx.oxml.ns import qn
        from docx.shared import Inches, Pt
    except ImportError:
        sys.exit("python-docx is missing: pip install python-docx")

    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, side, Inches(a.margin))
    normal = doc.styles["Normal"]
    normal.font.name = a.font
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), a.font)
    normal.font.size = Pt(a.size)
    normal.paragraph_format.space_after = Pt(4)
    right_tab = sec.page_width - sec.left_margin - sec.right_margin

    lines = open(a.src, encoding="utf-8").read().splitlines()
    out_html, after_name, in_list = [], False, False
    for raw in lines:
        line = raw.rstrip()
        if in_list and not line.startswith("- "):
            out_html.append("</ul>")
            in_list = False
        if not line.strip():
            continue
        if line.startswith("# "):
            p = doc.add_paragraph()
            runs(p, line[2:], size=Pt(a.size + 9), bold=True)
            p.paragraph_format.space_after = Pt(2)
            out_html.append(f'<h1 class="name">{inline_html(line[2:])}</h1>')
            after_name = True
            continue
        if after_name and not line.startswith("#"):
            p = doc.add_paragraph()
            runs(p, line, size=Pt(a.size - 0.5))
            out_html.append(f'<p class="contact">{inline_html(line)}</p>')
            after_name = False
            continue
        after_name = False
        if line.startswith("## "):
            p = doc.add_paragraph()
            runs(p, line[3:].upper(), size=Pt(a.size + 0.5), bold=True)
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            out_html.append(f"<h2>{inline_html(line[3:])}</h2>")
        elif line.startswith("### "):
            left, _, right = line[4:].partition(" | ")
            p = doc.add_paragraph()
            p.paragraph_format.tab_stops.add_tab_stop(right_tab, WD_TAB_ALIGNMENT.RIGHT)
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.keep_with_next = True
            runs(p, left, bold=True)
            if right:
                p.add_run("\t" + right)
            out_html.append(f'<h3><span>{inline_html(left)}</span><span class="when">{inline_html(right)}</span></h3>')
        elif line.startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            runs(p, line[2:])
            p.paragraph_format.space_after = Pt(2)
            if not in_list:
                out_html.append("<ul>")
                in_list = True
            out_html.append(f"<li>{inline_html(line[2:])}</li>")
        else:
            p = doc.add_paragraph()
            runs(p, line)
            p.paragraph_format.space_after = Pt(8)
            out_html.append(f"<p>{inline_html(line)}</p>")
    if in_list:
        out_html.append("</ul>")
    doc.save(a.out)
    if a.html:
        open(a.html, "w", encoding="utf-8").write("\n".join(out_html) + "\n")
    print(f"wrote {a.out}" + (f" and {a.html}" if a.html else ""))


if __name__ == "__main__":
    main()
