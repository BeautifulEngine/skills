#!/usr/bin/env python3
"""Render the looping how-to-ask GIF for a skill.

Usage (from tools/demo):
  python3 ../../shared/scripts/fonts.py "Inter:400,500,600,700" "JetBrains Mono:400,500"   # once
  python3 make_gif.py <skill> [<skill> ...]       # or: make_gif.py all

Prompts live in prompts.json. Output: docs/<skill>/how-to-ask.gif at the repo root.
Needs Playwright (Python) and ffmpeg.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SCALE = 1.5
WHERE = {
    "app": ("In the Claude app", "Ask in plain words; there's no command to learn."),
    "code": ("In Claude Code", "Type the slash command, or ask in plain words."),
}


def frames_for(skill, title, examples):
    frames = []

    def add(state, secs):
        frames.append((dict(state), secs))

    for i, (kind, prompt, gets) in enumerate(examples):
        where, hint = WHERE[kind]
        base = dict(n=len(examples), i=i, app=kind == "app", where=where, hint=hint, gets=gets, title=title, skill=skill,
                    typed="", caret=True, send="idle", result=0)
        add(base, 0.45)
        add({**base, "caret": False}, 0.35)
        add(base, 0.25)
        for k in range(1, len(prompt) + 1):
            add({**base, "typed": prompt[:k], "send": "ready"}, 0.04 if prompt[k - 1] != " " else 0.065)
        done = {**base, "typed": prompt, "send": "ready"}
        add(done, 0.35)
        add({**done, "caret": False}, 0.3)
        add({**done, "send": "pressed", "caret": False}, 0.25)
        add({**done, "send": "pressed", "caret": False, "result": 0.5}, 0.08)
        add({**done, "send": "pressed", "caret": False, "result": 1}, 2.3)
    return frames


def make(skill, cfg):
    frames = frames_for(skill, cfg["title"], cfg["examples"])
    out_dir = os.path.join(ROOT, "docs", skill)
    os.makedirs(out_dir, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        lines = []
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={"width": 880, "height": 380}, device_scale_factor=SCALE)
            pg.goto("file://" + os.path.join(HERE, "demo.html"))
            pg.evaluate("document.fonts.ready")
            for n, (s, secs) in enumerate(frames):
                pg.evaluate("s => render(s)", s)
                f = os.path.join(tmp, f"f{n:04d}.png")
                pg.screenshot(path=f)
                lines += [f"file '{f}'", f"duration {secs:.3f}"]
            b.close()
        lines.append(f"file '{os.path.join(tmp, f'f{len(frames) - 1:04d}.png')}'")
        lst = os.path.join(tmp, "list.txt")
        open(lst, "w").write("\n".join(lines) + "\n")
        out = os.path.join(out_dir, "how-to-ask.gif")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-vf",
                        "split[a][b];[a]palettegen=max_colors=48:stats_mode=full[p];[b][p]paletteuse=dither=none",
                        "-fps_mode", "vfr", "-loop", "0", out], check=True)
    secs = sum(s for _, s in frames)
    print(f"{skill}: {len(frames)} frames, {secs:.0f}s, {os.path.getsize(out) // 1024} KB -> {os.path.relpath(out, ROOT)}")


def main():
    cfgs = json.load(open(os.path.join(HERE, "prompts.json")))
    names = list(cfgs) if sys.argv[1:] in (["all"], []) else sys.argv[1:]
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg is required")
    for name in names:
        make(name, cfgs[name])


if __name__ == "__main__":
    main()
