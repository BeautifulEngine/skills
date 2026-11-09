#!/usr/bin/env python3
"""Draw the placeholder illustrations used by the Case Study sample (tools/samples/images/).

They're simple flat illustrations, so the sample doesn't depend on anyone's photography.
Usage: python3 make_images.py
"""
import math
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "images")
S = 2  # supersample factor


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def gradient(w, h, stops):
    im = Image.new("RGB", (w, h))
    px = im.load()
    stops = [(p, hexrgb(c)) for p, c in stops]
    for y in range(h):
        t = y / (h - 1)
        for i in range(len(stops) - 1):
            if stops[i][0] <= t <= stops[i + 1][0]:
                u = (t - stops[i][0]) / (stops[i + 1][0] - stops[i][0])
                c = lerp(stops[i][1], stops[i + 1][1], u)
                break
        for x in range(w):
            px[x, y] = c
    return im


def crowd(d, w, base, color, n, rng, hmin, hmax):
    d.rectangle([0, base - hmin * 0.45, w, base + 4000], fill=color)
    for _ in range(n):
        x = rng.uniform(-20, w + 20)
        hh = rng.uniform(hmin, hmax)
        r = hh * 0.16
        d.ellipse([x - r, base - hh - r, x + r, base - hh + r], fill=color)
        d.rounded_rectangle([x - r * 1.6, base - hh + r * 0.9, x + r * 1.6, base + 40], radius=r, fill=color)
        if rng.random() < 0.18:  # a raised arm with a phone light
            d.line([x + r, base - hh + r * 1.4, x + r * 2.4, base - hh - r * 2.2], fill=color, width=max(2, int(r * 0.55)))
            d.ellipse([x + r * 2.4 - r * 0.4, base - hh - r * 2.6, x + r * 2.4 + r * 0.4, base - hh - r * 1.8], fill="#ffe7b0")


def palm(d, x, base, h, color, lean=0.0):
    pts = []
    for i in range(30):
        t = i / 29
        pts.append((x + math.sin(t * 1.4) * lean * h, base - t * h))
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=color, width=int(h * 0.035 * (1.2 - pts.index(pts[i]) / 60)))
    tx, ty = pts[-1]
    for a in range(0, 360, 40):
        ang = math.radians(a + 10)
        for k in range(60):
            t = k / 59
            px = tx + math.cos(ang) * h * 0.34 * t
            py = ty + math.sin(ang) * h * 0.12 * t + (t ** 2) * h * 0.16
            r = h * 0.03 * (1 - t * 0.8)
            d.ellipse([px - r, py - r, px + r, py + r], fill=color)


def hero():
    w, h = 1600 * S, 900 * S
    im = gradient(w, h, [(0, "#2a1740"), (0.38, "#7a2a63"), (0.62, "#e0565b"), (0.8, "#ff9a5a"), (1, "#ffc77a")])
    sun = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sun)
    cx, cy, r = int(w * 0.66), int(h * 0.6), int(h * 0.2)
    sd.ellipse([cx - r * 1.9, cy - r * 1.9, cx + r * 1.9, cy + r * 1.9], fill=(255, 190, 120, 40))
    sd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 214, 140, 255))
    sun = sun.filter(ImageFilter.GaussianBlur(14 * S))
    im.paste(sun, (0, 0), sun)
    d = ImageDraw.Draw(im)
    # stripes across the sun
    for i in range(5):
        y = cy + r * 0.15 + i * r * 0.17
        d.rectangle([cx - r, y, cx + r, y + r * 0.05 + i * 3 * S], fill=lerp(hexrgb("#ff9a5a"), hexrgb("#e0565b"), i / 5))
    # stage
    sx, sy = int(w * 0.18), int(h * 0.62)
    d.rectangle([sx, sy, sx + w * 0.26, sy + h * 0.1], fill="#1a0e29")
    d.arc([sx - w * 0.02, sy - h * 0.28, sx + w * 0.28, sy + h * 0.2], 180, 360, fill="#1a0e29", width=18 * S)
    for i in range(9):
        lx = sx + w * 0.02 + i * w * 0.028
        d.ellipse([lx - 6 * S, sy - 10 * S, lx + 6 * S, sy + 2 * S], fill="#ffd79a")
    # string lights
    for k in range(2):
        y0 = h * (0.2 + k * 0.08)
        pts = [(x, y0 + math.sin(x / w * math.pi * 3) * h * 0.04) for x in range(0, w, 6 * S)]
        d.line(pts, fill=(26, 14, 41), width=2 * S)
        for x, y in pts[:: 14]:
            d.ellipse([x - 5 * S, y, x + 5 * S, y + 10 * S], fill="#ffe2a8")
    palm(d, w * 0.92, h * 0.78, h * 0.62, "#1a0e29", lean=0.06)
    palm(d, w * 0.05, h * 0.8, h * 0.5, "#1a0e29", lean=-0.05)
    rng = random.Random(7)
    crowd(d, w, h * 0.86, "#2a1531", 70, rng, h * 0.1, h * 0.16)
    crowd(d, w, h * 1.02, "#1a0e29", 46, rng, h * 0.16, h * 0.24)
    return im.resize((w // S, h // S), Image.LANCZOS)


def posters():
    w, h = 1200 * S, 900 * S
    im = Image.new("RGB", (w, h), "#efe6da")
    d = ImageDraw.Draw(im)
    font_path = None
    for p in [os.path.join(HERE, "node_modules/@fontsource/inter-tight/files/inter-tight-latin-700-normal.woff"),
              "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
        if os.path.exists(p):
            font_path = p
            break
    palettes = [("#2a1740", "#ff6b4a", "#ffc77a"), ("#c2416b", "#2a1740", "#ffe2a8"),
                ("#ff9a5a", "#2a1740", "#fff3e0"), ("#1f4b5a", "#ffb46b", "#ffe2a8")]
    dates = ["JUN 03", "JUN 17", "JUL 08", "AUG 12"]
    pw, ph = int(w * 0.2), int(h * 0.62)
    for i, (bg, a, b) in enumerate(palettes):
        x = int(w * 0.06 + i * (pw + w * 0.027))
        y = int(h * 0.17 + (i % 2) * h * 0.04)
        d.rectangle([x + 10 * S, y + 14 * S, x + pw + 10 * S, y + ph + 14 * S], fill="#d8cdbf")
        d.rectangle([x, y, x + pw, y + ph], fill=bg)
        r = pw * 0.36
        cx, cy = x + pw / 2, y + ph * 0.42
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=a)
        for k in range(4):
            yy = cy + r * 0.2 + k * r * 0.2
            d.rectangle([cx - r, yy, cx + r, yy + r * 0.06 + k * 2 * S], fill=bg)
        d.rectangle([x, y + ph * 0.62, x + pw, y + ph * 0.66], fill=b)
        try:
            f1 = ImageFont.truetype(font_path, int(pw * 0.17))
            f2 = ImageFont.truetype(font_path, int(pw * 0.08))
        except Exception:
            f1 = f2 = ImageFont.load_default()
        d.text((x + pw * 0.08, y + ph * 0.7), "PALOMA", font=f1, fill=b)
        d.text((x + pw * 0.08, y + ph * 0.8), "PARK", font=f1, fill=b)
        d.text((x + pw * 0.08, y + ph * 0.92), dates[i], font=f2, fill=a)
    return im.resize((w // S, h // S), Image.LANCZOS)


def lawn():
    w, h = 1200 * S, 900 * S
    im = gradient(w, h, [(0, "#5b2160"), (0.3, "#c2416b"), (0.55, "#ff8a5c"), (0.7, "#ffb46b"), (1, "#ffc77a")])
    d = ImageDraw.Draw(im)
    sx, sy, sr = w * 0.78, h * 0.5, h * 0.11
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill="#ffd68c")
    d.polygon([(0, h * 0.6), (w * 0.3, h * 0.53), (w * 0.62, h * 0.58), (w, h * 0.5), (w, h), (0, h)], fill="#7a2a63")
    d.polygon([(0, h * 0.7), (w * 0.4, h * 0.66), (w, h * 0.72), (w, h), (0, h)], fill="#4a1b4f")
    # string lights
    pts = [(x, h * 0.12 + math.sin(x / w * math.pi * 2.2) * h * 0.05) for x in range(0, w, 6 * S)]
    d.line(pts, fill=(42, 23, 64), width=2 * S)
    for x, y in pts[::12]:
        d.ellipse([x - 7 * S, y, x + 7 * S, y + 14 * S], fill="#ffe2a8")
    # sampling cart
    cw, ch = w * 0.36, h * 0.2
    cx, cy = w * 0.24, h * 0.56
    d.polygon([(cx - cw * 0.06, cy), (cx + cw * 0.5, cy - ch * 0.62), (cx + cw * 1.06, cy)], fill="#ff6b4a")
    for k in range(6):  # awning scallops
        ax = cx - cw * 0.06 + k * cw * 0.187
        d.pieslice([ax, cy - ch * 0.1, ax + cw * 0.187, cy + ch * 0.12], 0, 180, fill="#ff6b4a")
    d.rounded_rectangle([cx, cy + ch * 0.1, cx + cw, cy + ch], radius=14 * S, fill="#fff3e0")
    d.rectangle([cx, cy + ch * 0.62, cx + cw, cy + ch * 0.7], fill="#ff6b4a")
    for k in range(8):
        bx = cx + cw * 0.06 + k * cw * 0.115
        d.rounded_rectangle([bx, cy + ch * 0.24, bx + cw * 0.07, cy + ch * 0.54], radius=5 * S, fill=["#ff6b4a", "#ffc77a", "#c2416b", "#2a1740"][k % 4])
    for k in range(2):
        wx = cx + cw * (0.18 + k * 0.64)
        d.ellipse([wx - 26 * S, cy + ch * 0.92, wx + 26 * S, cy + ch * 0.92 + 52 * S], fill="#2a1740")
    rng = random.Random(3)
    crowd(d, w, h * 0.97, "#3a1640", 18, rng, h * 0.1, h * 0.15)
    crowd(d, w, h * 1.08, "#2a1740", 10, rng, h * 0.16, h * 0.22)
    return im.resize((w // S, h // S), Image.LANCZOS)


def main():
    os.makedirs(OUT, exist_ok=True)
    hero().save(os.path.join(OUT, "hero.jpg"), quality=86)
    posters().save(os.path.join(OUT, "posters.jpg"), quality=86)
    lawn().save(os.path.join(OUT, "lawn.jpg"), quality=86)
    print("wrote", ", ".join(sorted(os.listdir(OUT))))


if __name__ == "__main__":
    main()
