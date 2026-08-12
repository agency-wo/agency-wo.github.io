"""One-time MINARANK logo-suite builder.
Extracts outlined glyph paths from the Fontshare variable TTFs (Clash Display
wght 500 for the wordmark, Satoshi wght 500 for the lockup tagline) and writes
the SVG suite into the project's assets/logo/.
Geometry source of truth: 120-unit em, baseline of letter i at y = 160 - i*3.36
(2.8% of em per letter, from the brand PDF)."""
import os
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.misc.transform import Transform

SC = os.path.dirname(os.path.abspath(__file__))
OUT = r"c:\Users\aceto\OneDrive\Desktop\web and apps\MINA RANK\assets\logo"
INK, INK2, CORAL, PAPER = "#1B1F3B", "#2E3358", "#FF6B4A", "#F7F5F2"

def load(path, wght):
    f = TTFont(path)
    instantiateVariableFont(f, {"wght": wght}, inplace=True)
    return f

clash = load(os.path.join(SC, "clash-display/ClashDisplay_Complete/Fonts/TTF/ClashDisplay-Variable.ttf"), 500)
satoshi = load(os.path.join(SC, "satoshi/Satoshi_Complete/Fonts/TTF/Satoshi-Variable.ttf"), 500)

def rnd(d, p=2):
    # compact the huge float coords SVGPathPen emits
    import re
    return re.sub(r"-?\d+\.\d+", lambda m: f"{float(m.group()):.{p}f}".rstrip("0").rstrip("."), d)

def set_text(font, text, size, tracking_em, baseline_fn, x0=0.0, dx=None):
    """dx: optional {letter_index: em_offset} of per-pair optical corrections,
    applied to that letter's pen position (and everything after it)."""
    upem = font["head"].unitsPerEm
    s = size / upem
    cmap = font.getBestCmap()
    gs = font.getGlyphSet()
    hmtx = font["hmtx"]
    track = tracking_em * size
    out, x = [], x0
    for i, ch in enumerate(text):
        gname = cmap[ord(ch)]
        if dx:
            x += dx.get(i, 0.0) * size
        y = baseline_fn(i)
        spen = SVGPathPen(gs)
        gs[gname].draw(TransformPen(spen, Transform().translate(x, y).scale(s, -s)))
        d = rnd(spen.getCommands())
        bp = BoundsPen(gs)
        gs[gname].draw(bp)
        ink_top = y - bp.bounds[3] * s if bp.bounds else y
        ink_bot = y - bp.bounds[1] * s if bp.bounds else y
        ink_l = x + bp.bounds[0] * s if bp.bounds else x
        out.append({"ch": ch, "x": x, "base": y, "d": d, "top": ink_top,
                    "bot": ink_bot, "inkl": ink_l})
        x += hmtx[gname][0] * s + track
    return out, x - track

def svg(viewbox, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" role="img" '
            f'aria-label="{title}">\n{body}\n</svg>\n')

def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name, len(content), "bytes")

WORD = "minarank"
RISE = 3.36          # even 3.36/letter kept after side-by-side test: a 1.25x
                     # final-step overshoot is imperceptible at any real size.
PADX, PADY = 8, 8

# Optical pair corrections (em units, applied at the named letter index).
# k (index 7): the climb + the ink->coral break visually detach the k; -0.012em
# re-couples it to the word. Verified against 0 and -0.022em (too tight) crops.
WORD_DX = {7: -0.012}

# ---- A. ascending wordmark -------------------------------------------------
asc, wA = set_text(clash, WORD, 120, 0.01, lambda i: 160 - i * RISE, x0=PADX, dx=WORD_DX)
top = min(g["top"] for g in asc) - PADY          # ~48
bot = max(g["bot"] for g in asc) + PADY          # 168
W = wA + PADX
vb = f"0 {top:.0f} {W:.0f} {bot - top:.0f}"

def wordmark_body(letters, ink_fill, coral_fill):
    paths = []
    for g in letters:
        fill = coral_fill if g["ch"] == "k" and g is letters[-1] else ink_fill
        paths.append(f'  <path fill="{fill}" d="{g["d"]}"/>')
    return "\n".join(paths)

write("minarank-wordmark.svg", svg(vb, wordmark_body(asc, INK, CORAL), "minarank"))
write("minarank-wordmark-paper.svg", svg(vb, wordmark_body(asc, PAPER, CORAL), "minarank"))
write("minarank-wordmark-mono.svg", svg(vb, wordmark_body(asc, "currentColor", "currentColor"), "minarank"))

# ---- C. bar signature (flat wordmark + four ascending bars) ---------------
flat, wF = set_text(clash, WORD, 120, 0.01, lambda i: 160, x0=PADX, dx=WORD_DX)
ftop = min(g["top"] for g in flat) - PADY
bars = []
# Bars hang from the m: left edge on the m's INK left (not its pen position),
# otherwise the bars jut past the wordmark's optical left edge and read stuck-on.
bx, bw, gap = flat[0]["inkl"], 14, 10
for i, h in enumerate((20, 30, 42, 56)):
    fill = CORAL if i == 3 else INK
    bars.append(f'  <rect fill="{fill}" x="{bx + i*(bw+gap):.2f}" y="{240 - h}" width="{bw}" height="{h}"/>')
barsig_body = wordmark_body(flat, INK, INK) + "\n" + "\n".join(bars)
write("minarank-barsig.svg", svg(f"0 {ftop:.0f} {wF + PADX:.0f} {248 - ftop:.0f}", barsig_body, "minarank"))

# ---- D. lockup (ascending wordmark + DESIGN — RANKING tagline) ------------
TAG = "DESIGN \u2014 RANKING"
TAG_BASE = 202  # was 208; at 208 the tagline floats off the wordmark
# Optically align the tagline's D ink-left with the m's ink-left (their
# sidebearings differ), instead of sharing the raw pen origin.
d_lsb = set_text(satoshi, "D", 26, 0.0, lambda i: 0)[0][0]["inkl"]
tag, wT = set_text(satoshi, TAG, 26, 0.14, lambda i: TAG_BASE, x0=asc[0]["inkl"] - d_lsb)
tag_paths = []
for g in tag:
    if g["ch"] == "\u2014":
        tag_paths.append(f'  <path fill="{CORAL}" d="{g["d"]}"/>')
    elif g["ch"] != " ":
        tag_paths.append(f'  <path fill="{INK2}" d="{g["d"]}"/>')
tag_bot = max(g["bot"] for g in tag) + PADY
lockup_body = wordmark_body(asc, INK, CORAL) + "\n" + "\n".join(tag_paths)
write("minarank-lockup.svg", svg(f"0 {top:.0f} {W:.0f} {tag_bot - top:.0f}", lockup_body, "minarank — design, ranking"))

# ---- B. monogram (hand geometry, 8-unit grid, reads at 32px) --------------
def monogram(ink, coral):
    # Final geometry after design review: bevel-limited miters, tick collinear
    # with the final diagonal (direction 3,-4), M shifted down 2 for balance.
    return (f'  <path fill="none" stroke="{ink}" stroke-width="8" stroke-linejoin="miter" '
            f'stroke-miterlimit="2" stroke-linecap="butt" d="M14 54 L14 18 L32 42 L50 18 L50 54" class="ink"/>\n'
            f'  <path fill="none" stroke="{coral}" stroke-width="7" stroke-linecap="butt" '
            f'd="M53 14 L60.5 4"/>')
# Monogram files are owned by a concurrent agent — do not write them from here.
# write("minarank-monogram.svg", svg("0 0 64 64", monogram(INK, CORAL), "minarank monogram"))
# write("minarank-monogram-mono.svg", svg("0 0 64 64", monogram("currentColor", "currentColor"), "minarank monogram"))

print("ASC viewBox:", vb, "| letter data: " + ", ".join(f"{g['ch']}@{g['x']:.1f}/{g['base']:.1f}" for g in asc))
