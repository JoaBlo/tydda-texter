#!/usr/bin/env python3
"""Bygger en fristående delningsversion av webbvisaren.

Mappen kan zippas och skickas/delas (OneDrive, Google Drive, USB …). Mottagaren
packar upp och dubbelklickar på "Öppna mig.html" (eller index.html) – ingen
webbserver, inget konto, inget internet behövs.

Användning:  python3 bygg_delning.py [målmapp] [--max 2400] [--kvalitet 82]
Standard-målmapp: ~/Desktop/Tydda texter (delning)
Kör bygg_index.py först så att pages.json är aktuell.
"""
import json, os, shutil, sys, glob, argparse
from PIL import Image, ImageOps

ROT = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("mal", nargs="?", default=os.path.expanduser("~/Desktop/Tydda texter (delning)"))
ap.add_argument("--max", type=int, default=2400, help="längsta bildsida i pixlar")
ap.add_argument("--kvalitet", type=int, default=82, help="JPEG-kvalitet")
a = ap.parse_args()
mal = a.mal
os.makedirs(os.path.join(mal, "bilder", "thumb"), exist_ok=True)
os.makedirs(os.path.join(mal, "transkriptioner"), exist_ok=True)

# 1. Data: pages.json + alla .md-filer som visaren läser, inbäddade i data.js
pages = json.load(open(os.path.join(ROT, "pages.json"), encoding="utf-8"))
files = {}
EXTRA = [os.path.join(ROT, f) for f in ("namn.md", "ordlista.md", "berattelse.md", "slakttrad.md") if os.path.exists(os.path.join(ROT, f))]
for fn in sorted(glob.glob(os.path.join(ROT, "transkriptioner", "*.md"))) + EXTRA:
    rel = os.path.relpath(fn, ROT)
    files[rel] = open(fn, encoding="utf-8").read()
    shutil.copy2(fn, os.path.join(mal, rel))   # så att länken ".md-fil" fungerar
with open(os.path.join(mal, "data.js"), "w", encoding="utf-8") as f:
    f.write("window.EMBED = ")
    json.dump({"pages": pages, "files": files}, f, ensure_ascii=False)
    f.write(";\n")

# 2. Visaren
shutil.copy2(os.path.join(ROT, "index.html"), os.path.join(mal, "index.html"))
with open(os.path.join(mal, "Öppna mig.html"), "w", encoding="utf-8") as f:
    f.write('<!doctype html><meta charset="utf-8"><title>Tydda texter</title>'
            '<meta http-equiv="refresh" content="0; url=index.html">'
            '<p><a href="index.html">Öppna Tydda texter</a></p>\n')

# 3. Bilder (förminskade) och tumnaglar
n = 0
for src in sorted(glob.glob(os.path.join(ROT, "bilder", "*.jpg"))):
    dst = os.path.join(mal, "bilder", os.path.basename(src))
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
        continue
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    im.thumbnail((a.max, a.max), Image.LANCZOS)
    im.save(dst, "JPEG", quality=a.kvalitet, optimize=True, progressive=True)
    n += 1
for src in glob.glob(os.path.join(ROT, "bilder", "thumb", "*.jpg")):
    shutil.copy2(src, os.path.join(mal, "bilder", "thumb", os.path.basename(src)))

with open(os.path.join(mal, "LÄS MIG.txt"), "w", encoding="utf-8") as f:
    f.write("Tydda texter – transkriptioner av handlingar från Sandnabba och Härmälä, Överpurmo\n\n"
            "Så här öppnar du: dubbelklicka på \"Öppna mig.html\". Sidan öppnas i webbläsaren.\n"
            "Ingen internetanslutning eller installation behövs.\n\n"
            "Om du fått mappen som .zip: packa upp den först (högerklicka → Extrahera alla / dubbelklicka på Mac).\n")

storlek = sum(os.path.getsize(os.path.join(d, x)) for d, _, fs in os.walk(mal) for x in fs)
print(f"Klart: {mal}\n  {len(pages['sidor'])} sidor, {n} bilder förminskade nu, totalt {storlek/1e6:.0f} MB")
