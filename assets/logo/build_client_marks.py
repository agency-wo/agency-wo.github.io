"""Build the four client marks for the homepage logo row.

Every mark ends up as a single-colour shape the page paints with currentColor,
so the row reads as one set instead of four pasted screenshots. Two routes get
there, because the source material is not the same shape:

  SVG    Victoria Boutique and Intimo Bruna have no logo file anywhere. Their
         mark is literally text set in their own site header. Both self-host
         the webfont, so we outline the real letterforms at their own weight
         and their own tracking. This is reproduction, not invention.

  PNG    Iglisi Watch and Pro Affy have real artwork. We keep only the alpha
         channel. Iglisi's wordmark is white on transparent, so its alpha is
         already the shape we want. Pro Affy sits on a flat near-white ground
         that has to be knocked out first, which also opens the white gaps
         between the blobs. That is correct: the gaps should read as paper.

All four are consumed the same way, as a CSS mask painted with currentColor,
so the row inherits one ink colour and one hover colour. They stay separate
files rather than inline SVG because Cormorant's serifs alone are 14 KB of
path data, which does not belong in every byte of the homepage.

Run from the project root:  python assets/logo/build_client_marks.py

Deliberately NOT part of build.ps1. Marks change when a client changes, which
is roughly never, and the outputs are committed.
"""
import io
import os
import re

from PIL import Image
from fontTools.misc.transform import Transform
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

NL = chr(10)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "clients")
SRC = os.path.join(OUT, "source")
WORKSPACE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))


def rel(*parts):
    return os.path.join(WORKSPACE, *parts)


# ---------------------------------------------------------------- outlines --

def load(path, wght):
    f = TTFont(path)
    instantiateVariableFont(f, {"wght": wght}, inplace=True)
    return f


def rnd(d, p=1):
    """SVGPathPen emits long floats. One decimal is well under a pixel here."""
    return re.sub(r"-?\d+\.\d+",
                  lambda m: f"{float(m.group()):.{p}f}".rstrip("0").rstrip("."), d)


def wordmark(font_path, wght, text, tracking_em, size=100):
    """Set text on the baseline and return (path_data, viewBox) cropped to ink.

    tracking_em is CSS letter-spacing. CSS adds it after every character
    including the last; a wordmark should not carry that trailing gap, so the
    advance after the final glyph is dropped.
    """
    font = load(font_path, wght)
    upem = font["head"].unitsPerEm
    scale = size / upem
    cmap = font.getBestCmap()
    glyphs = font.getGlyphSet()
    hmtx = font["hmtx"]
    track = tracking_em * size

    paths, x = [], 0.0
    left = top = 1e9
    right = bottom = -1e9
    for ch in text:
        gname = cmap[ord(ch)]
        pen = SVGPathPen(glyphs)
        # y flips: font space is up-positive, SVG is down-positive.
        glyphs[gname].draw(TransformPen(pen, Transform().translate(x, 0).scale(scale, -scale)))
        d = pen.getCommands()
        if d:
            paths.append(rnd(d))
        bp = BoundsPen(glyphs)
        glyphs[gname].draw(bp)
        if bp.bounds:
            x0, y0, x1, y1 = bp.bounds
            left = min(left, x + x0 * scale)
            right = max(right, x + x1 * scale)
            top = min(top, -y1 * scale)
            bottom = max(bottom, -y0 * scale)
        x += hmtx[gname][0] * scale + track

    w, h = right - left, bottom - top
    body = NL.join(f'  <path d="{d}"/>' for d in paths)
    # Consumed as a CSS mask, so only the alpha matters and the fill is thrown
    # away. width/height give it an intrinsic size, without which mask-size
    # contain has nothing to scale against.
    return (f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{w:.1f}" height="{h:.1f}" '
            f'viewBox="{left:.1f} {top:.1f} {w:.1f} {h:.1f}" fill="#000">' + NL +
            body + NL + '</svg>' + NL), (w, h)


# ------------------------------------------------------------------ alphas --

def save_mask(img, name, max_w):
    """Crop to the ink, cap the width, and keep only the alpha channel.

    The result is painted by CSS, so its colour is thrown away. Storing black
    under the alpha compresses to almost nothing.
    """
    box = img.getchannel("A").getbbox()
    assert box, name + ": image is fully transparent"
    img = img.crop(box)
    if img.width > max_w:
        h = round(img.height * max_w / img.width)
        img = img.resize((max_w, h), Image.LANCZOS)
    alpha = img.getchannel("A")
    out = Image.merge("RGBA", (Image.new("L", img.size, 0),) * 3 + (alpha,))
    path = os.path.join(OUT, name)
    out.save(path, "PNG", optimize=True)
    return img.size, os.path.getsize(path)


def knockout(img, lo=225, hi=245):
    """Turn a flat light ground into transparency, keeping antialiased edges.

    Luma at or above hi is fully out, at or below lo fully in, linear between,
    so the curve edges do not go to staircase.
    """
    img = img.convert("RGB")
    luma = img.convert("L")
    lut = [0 if v >= hi else 255 if v <= lo else round(255 * (hi - v) / (hi - lo))
           for v in range(256)]
    return Image.merge("RGBA", img.split() + (luma.point(lut),))


# -------------------------------------------------------------------- main --

def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(SRC, exist_ok=True)
    report = []

    # Victoria Boutique. Her own footer lockup: Cormorant Garamond 500 at
    # 0.2em, charcoal. butik Viktoria/styles.css line 171.
    svg, size = wordmark(
        rel("butik Viktoria", "assets", "fonts",
            "CormorantGaramond-500-normal-latin.woff2"),
        500, "VICTORIA BOUTIQUE", 0.20)
    io.open(os.path.join(OUT, "victoria-boutique.svg"), "w",
            encoding="utf-8", newline=NL).write(svg)
    report.append(("victoria-boutique.svg", f"{size[0]:.0f}x{size[1]:.0f}", len(svg)))

    # Intimo Bruna. Her own header wordmark: Playfair Display 700 at 0.01em.
    # Intimo Bruna/styles.css line 193. One word, as she writes it everywhere.
    svg, size = wordmark(
        rel("Intimo Bruna", "assets", "fonts", "playfair-display-latin.woff2"),
        700, "IntimoBruna", 0.01)
    io.open(os.path.join(OUT, "intimo-bruna.svg"), "w",
            encoding="utf-8", newline=NL).write(svg)
    report.append(("intimo-bruna.svg", f"{size[0]:.0f}x{size[1]:.0f}", len(svg)))

    # Iglisi Watch. The wordmark the shop actually uses in its own header,
    # white on transparent, so the alpha channel is already the mark.
    iglisi = Image.open(rel("watch-repair-shop", "mina.github.io",
                            "logo.png")).convert("RGBA")
    size, nbytes = save_mask(iglisi, "iglisi-watch.png", 440)
    report.append(("iglisi-watch.png", f"{size[0]}x{size[1]}", nbytes))

    # Pro Affy. Symbol on a flat #F7F7F7 ground, knocked out to alpha.
    affy_src = os.path.join(HERE, "..", "..", "proaffy logo.jpeg")
    if os.path.exists(affy_src):
        kept = os.path.join(SRC, "proaffy-logo.jpeg")
        if not os.path.exists(kept):
            io.open(kept, "wb").write(io.open(affy_src, "rb").read())
    affy = Image.open(os.path.join(SRC, "proaffy-logo.jpeg"))
    size, nbytes = save_mask(knockout(affy), "pro-affy.png", 180)
    report.append(("pro-affy.png", f"{size[0]}x{size[1]}", nbytes))

    for name, dims, n in report:
        print(f"  {name:28s} {dims:>12s}  {n:>6,} bytes")


if __name__ == "__main__":
    main()
