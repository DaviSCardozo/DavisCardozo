"""Renderiza SVGs em PNG no Chromium em instantes específicos da animação (conferência visual).
uso: python scripts/render.py saida_dir arquivo.svg[:t1,t2,...] ...
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    for spec in sys.argv[2:]:
        f, _, ts = spec.partition(":")
        times = [float(t) for t in ts.split(",")] if ts else [None]
        src = Path(f).read_text()
        vb = src.split('viewBox="0 0 ')[1].split('"')[0].split()
        w, h = int(float(vb[0])), int(float(vb[1]))
        for t in times:
            pg = b.new_page(viewport={"width": w, "height": h})
            pg.goto(Path(f).resolve().as_uri())
            if t is not None:
                pg.evaluate("t=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=t*1000})", t)
            else:
                pg.emulate_media(reduced_motion="reduce")
            name = Path(f).stem + (f"@{t:g}" if t is not None else "") + ".png"
            pg.screenshot(path=str(out / name))
            pg.close()
    b.close()
