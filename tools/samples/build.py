#!/usr/bin/env python3
"""Build the sample output and preview image for each skill.

Each sample is the skill's own template head (styles, fonts, tokens) plus a sample body in
bodies/<skill>.html. Samples use real brands: pitch, activation and quote samples are unofficial
spec work with sourced figures; Case Study and Brand Snapshot cover Beautiful Engine's own work.

Usage (from tools/samples):
  python3 build.py all | <skill> ...
Outputs: examples/<skill>/<file>.pdf and docs/<skill>/preview.png at the repo root.
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SHARED = os.path.join(ROOT, "shared")
SKILLS = os.path.join(ROOT, "plugins", "beautiful-engine", "skills")


def fonts_html(specs):
    """Install fonts once into tools/samples/node_modules and return <link> tags relative to build/<skill>/."""
    r = subprocess.run(["python3", os.path.join(SHARED, "scripts", "fonts.py"), *specs], cwd=HERE, capture_output=True, text=True)
    return r.stdout.replace('href="node_modules/', 'href="../../node_modules/')


def tokens_html(args):
    r = subprocess.run(["python3", os.path.join(SHARED, "scripts", "tokens.py"), *args], capture_output=True, text=True)
    if "FAIL" in r.stderr or "WARNING" in r.stderr:
        print(r.stderr, file=sys.stderr)
    return r.stdout


def label_font(size):
    for f in glob.glob(os.path.join(HERE, "node_modules/@fontsource/inter/files/inter-latin-500-normal.woff*")):
        pass
    for path in ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def preview(pdf, pages, captions, out, landscape):
    tmp = os.path.join(HERE, "build", "_pv")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    ims = []
    for p in pages:
        subprocess.run(["pdftoppm", "-r", "110", "-f", str(p), "-l", str(p), "-png", pdf, os.path.join(tmp, f"p{p:02d}")], check=True)
        ims.append(Image.open(sorted(glob.glob(os.path.join(tmp, f"p{p:02d}*.png")))[0]).convert("RGB"))
    W, pad, gap, cap = 1800, 56, 36, 44
    cols = 2 if landscape else len(ims)
    rows = (len(ims) + cols - 1) // cols
    cell_w = (W - 2 * pad - (cols - 1) * gap) // cols
    scaled = [im.resize((cell_w, round(im.height * cell_w / im.width)), Image.LANCZOS) for im in ims]
    cell_h = max(s.height for s in scaled)
    H = 2 * pad + rows * (cell_h + cap) + (rows - 1) * gap
    canvas = Image.new("RGB", (W, H), "#ecebe7")
    draw = ImageDraw.Draw(canvas)
    font = label_font(19)
    for i, s in enumerate(scaled):
        x = pad + (i % cols) * (cell_w + gap)
        y = pad + (i // cols) * (cell_h + cap + gap)
        shadow = Image.new("RGB", (s.width, s.height), "#cfcdc6")
        canvas.paste(shadow, (x + 5, y + 6))
        canvas.paste(s, (x, y))
        draw.rectangle([x, y, x + s.width - 1, y + s.height - 1], outline="#d6d4cd")
        draw.text((x + s.width / 2, y + s.height + 14), captions[i], fill="#55524b", font=font, anchor="mt")
    canvas.save(out, optimize=True)


def build(skill, cfg):
    work = os.path.join(HERE, "build", skill)
    shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work)
    for css in ("base.css", "deck.css"):
        shutil.copy(os.path.join(SHARED, "assets", css), work)
    tpl = open(os.path.join(SKILLS, skill, "assets", cfg["template"])).read()
    head = tpl.split("<body>")[0] + "<body>\n"
    head = head.replace("<!-- FONT LINKS (scripts/fonts.py) -->", fonts_html(cfg["fonts"]))
    head = head.replace("<!-- TOKENS (scripts/tokens.py) -->", tokens_html(cfg["tokens"]))
    head = re.sub(r"<title>.*?</title>", f"<title>{cfg['title']}</title>", head, flags=re.S)
    if cfg.get("extra_css"):
        head = head.replace("</head>", f"<style>{cfg['extra_css']}</style>\n</head>")
    body = open(os.path.join(HERE, "bodies", f"{skill}.html")).read()
    open(os.path.join(work, "doc.html"), "w").write(head + body + "\n</body></html>\n")
    for img in cfg.get("images", []):
        shutil.copytree(os.path.join(HERE, img), os.path.join(work, os.path.basename(img)), dirs_exist_ok=True)
    out_dir = os.path.join(ROOT, "examples", skill)
    os.makedirs(out_dir, exist_ok=True)
    pdf = os.path.join(out_dir, cfg["pdf"])
    r = subprocess.run(["node", os.path.join(SHARED, "scripts", "render.cjs"), "doc.html", pdf], cwd=work, capture_output=True, text=True)
    problems = [l for l in r.stdout.splitlines() if l.startswith("FAIL")]
    pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    os.makedirs(os.path.join(ROOT, "docs", skill), exist_ok=True)
    pv = cfg["preview"]
    preview(pdf, [p for p in pv["pages"] if p <= pages], pv["captions"], os.path.join(ROOT, "docs", skill, "preview.png"), pv.get("landscape", False))
    print(f"{skill}: {pages} pages -> examples/{skill}/{cfg['pdf']}" + (f"  {len(problems)} audit problem(s): " + "; ".join(problems) if problems else ""))


def main():
    cfgs = json.load(open(os.path.join(HERE, "samples.json")))
    names = list(cfgs) if sys.argv[1:] in (["all"], []) else sys.argv[1:]
    for n in names:
        build(n, cfgs[n])


if __name__ == "__main__":
    main()
