"""Build favicon.ico and apple-touch-icon.png from the monogram geometry.

These two were rasterised once from the old navy-and-coral palette and then
survived an entire rebrand, because nothing on this site compares a pixel to a
token. The browser tab and the header logo were different colours from each
other on all 13 pages.

The geometry is the same M and ascending tick as `favicon.svg`, kept here as
coordinates rather than parsed out of the SVG, so the two can be diffed by eye
and neither silently drifts. Drawn at 16x and downsampled, which is well past
the point where the miter joins matter at 48px.

Run from the project root:  python assets/logo/build_icons.py
"""
import io
import os

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

# css/tokens.css. Change them there, then rerun this. Gate check 31 fails the
# build if any of these stops being a token.
INK = (0x13, 0x16, 0x1C)
RED = (0xD8, 0x23, 0x2A)
PAPER = (0xF0, 0xF1, 0xF3)

SS = 16                       # supersample
BOX = 64                      # the SVG viewBox
M = [(14, 54), (14, 18), (32, 42), (50, 18), (50, 54)]   # stroke-width 8
TICK = [(53, 14), (60.5, 4)]                             # stroke-width 7


def monogram(px, bg=None):
    """The mark at px square. bg=None leaves it transparent."""
    n = px * SS
    im = Image.new("RGBA", (n, n), (bg + (255,)) if bg else (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    k = n / BOX

    def scale(pts):
        return [(x * k, y * k) for x, y in pts]

    # joint="curve" rounds the two peaks of the M. At 48px and below that is
    # under half a pixel against the SVG's miter, and it survives downsampling
    # better than a hand-built miter would.
    d.line(scale(M), fill=INK + (255,), width=round(8 * k), joint="curve")
    d.line(scale(TICK), fill=RED + (255,), width=round(7 * k))
    return im.resize((px, px), Image.LANCZOS)


def main():
    # apple-touch-icon: opaque, on paper, with the mark inset the way iOS
    # expects rather than bleeding to the corners it will round off anyway.
    touch = Image.new("RGBA", (180, 180), PAPER + (255,))
    mark = monogram(132)
    touch.alpha_composite(mark, (24, 24))
    p = os.path.join(ROOT, "apple-touch-icon.png")
    touch.convert("RGB").save(p, "PNG", optimize=True)
    print("  apple-touch-icon.png  180x180  %5d bytes" % os.path.getsize(p))

    # favicon.ico: 3 sizes in one file, transparent, so it sits on whatever
    # colour the browser chrome happens to be.
    sizes = [16, 32, 48]
    frames = [monogram(s) for s in sizes]
    p = os.path.join(ROOT, "favicon.ico")
    frames[-1].save(p, "ICO", sizes=[(s, s) for s in sizes],
                    append_images=frames[:-1])
    print("  favicon.ico           %-8s %5d bytes"
          % ("/".join(str(s) for s in sizes), os.path.getsize(p)))

    # and prove the SVG the browser actually prefers agrees with these
    svg = io.open(os.path.join(ROOT, "favicon.svg"), encoding="utf-8").read()
    for name, want in (("ink", "#13161C"), ("red", "#D8232A"), ("paper", "#F0F1F3")):
        assert want in svg, f"favicon.svg has no {name} {want}: recolour it too"
    print("  favicon.svg agrees on all 3 tokens")


if __name__ == "__main__":
    main()
