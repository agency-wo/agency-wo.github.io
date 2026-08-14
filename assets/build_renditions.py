"""Emit the 720w rendition beside each proof chart and each plate.

The originals are 900 to 1440 pixels wide because that is what the layout
needs at desktop density. A phone in the sidebar column never paints more
than about 400 CSS pixels of plate, so shipping it the 1120px original is
paying full-width bytes for a thumbnail's worth of glass. The 720w file is
the srcset's smaller candidate; the browser does the arithmetic, not us.

720 and not a ladder of 4: the originals are already modest (the largest is
66 KB), so one intermediate step captures nearly all the saving and keeps
the directory listable. A rendition nobody can name is a rendition that gets
deleted as clutter.

LANCZOS, because these are screenshots full of 1px hairlines and small text:
a cheaper filter smears exactly the details the charts exist to show.

Write-if-changed on bytes, so a re-run with unchanged sources writes nothing
and the build stays deterministic. If a source image changes, re-run this;
gen_cases.py emits the -720 names into srcset and the gate fails any srcset
URL that does not resolve, so a forgotten re-run cannot ship silently.

Run from the project root:  python assets/build_renditions.py
"""
import io
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
WIDTH = 720

SOURCES = [
    os.path.join("proof", "watch-al-3-months.webp"),
    os.path.join("proof", "watch-al-28-days.webp"),
    os.path.join("plates", "iglisi-shop.webp"),
    os.path.join("plates", "victoria-home.webp"),
    os.path.join("plates", "bruna-home.webp"),
    os.path.join("plates", "proaffy-home.webp"),
]

for rel in SOURCES:
    src = os.path.join(HERE, rel)
    stem, ext = os.path.splitext(src)
    out = f"{stem}-{WIDTH}{ext}"
    im = Image.open(src)
    assert im.width > WIDTH, f"{rel} is {im.width}px wide; a 720w copy of it would upscale"
    h = round(im.height * WIDTH / im.width)
    small = im.resize((WIDTH, h), Image.LANCZOS)
    buf = io.BytesIO()
    # method=6 spends encoder time for bytes, which is the right trade for a
    # file encoded once and served forever.
    small.save(buf, "WEBP", quality=82, method=6)
    body = buf.getvalue()
    old = open(out, "rb").read() if os.path.exists(out) else None
    if old == body:
        print(f"unchanged {os.path.relpath(out, HERE)} ({WIDTH}x{h})")
    else:
        open(out, "wb").write(body)
        kb_in = os.path.getsize(src) / 1024
        kb_out = len(body) / 1024
        print(f"wrote     {os.path.relpath(out, HERE)} ({WIDTH}x{h}, "
              f"{kb_in:.0f} KB -> {kb_out:.0f} KB)")
