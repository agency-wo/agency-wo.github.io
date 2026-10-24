"""Encode the client screenshots from _source/plates into assets/plates.

RUN BY HAND, like make_photos.py. **Not a build dependency**: it imports PIL, and
shell.image_size() exists precisely so the build never has to. Run it when a client
rebuilds their site, commit what it writes, and the build only ever reads the WebP
that comes out.

    python .build/make_plates.py            encode anything missing or stale
    python .build/make_plates.py --force    re-encode everything

Two rungs per plate, <slug>.webp and <slug>-720.webp, paired by shell.with_720().

CAPTURING THE MASTERS
---------------------
There is no node in this project, so the shoot runs from another project's
playwright-core (see .index/code.md for which, and never name it in this repo).
The recipe, which cost three failed runs to establish:

    viewport 1440x1000, deviceScaleFactor 2  ->  a 2880x2000 master
    launch with channel "msedge"

Four traps, every one of them silent:

1. **A bare chromium.launch() finds no browser on this machine.** It prints the
   install banner and exits. channel "msedge" works.
2. **Reveal-on-scroll ships opacity:0.** Two of the six sites animate their hero in
   on an IntersectionObserver, so a shot taken before it fires captures an invisible
   hero that looks like a blank page. Force opacity, transform and visibility on
   .reveal, [data-reveal], .entrance and the [class*="fade"] family.
3. **style-src 'self' blocks addStyleTag.** Three of the six ship a strict CSP, and
   Playwright's addStyleTag throws on them. CSSOM is NOT blocked by CSP, so set the
   properties with el.style.setProperty(prop, value, "important") inside evaluate()
   instead of injecting a <style>.
4. **A consent banner covers the hero.** watch.al opens with one. Click the accept
   control, then hide any fixed or sticky element over 60px tall whose id, class or
   text matches cookie/consent/gdpr; a sticky header is shorter than that and
   survives, which is what you want since the nav belongs in the picture.

Afterwards LOOK AT EVERY MASTER before writing alt text. The alt is a factual claim
about a client's homepage and it goes stale exactly when the client rebuilds: on
2026-10-24 the Census plate was still described as "a sunset photograph of the
Durres pier" months after that photograph had been replaced by a map.
"""
import os
import sys

from PIL import Image                                   # not a build dependency

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "_source", "plates")
OUT = os.path.join(ROOT, "assets", "plates")

SMALL = 720
QUALITY = 82

# slug -> (width of the top rung, how much of the 2000px master to keep)
#
# All six keep the whole frame, which at 900 wide is exactly 900x625, the ratio
# every plate in the grid has. They show the hero and the top edge of whatever
# follows it, which is what a browser shows.
#
# Iglisi was briefly (1120, 1460), cropped to its hero band and wider, for the one
# day it sat in the homepage hero instead of the grid. It is back in the grid with
# the other five, and a grid of six wants one ratio, so it is back to the same
# frame as the rest.
PLATES = {
    "iglisi-home": (900, None),
    "victoria-home": (900, None),
    "bruna-home": (900, None),
    "proaffy-home": (900, None),
    "census-properties-home": (900, None),
    "vila-flamuri-home": (900, None),
}


def encode(im, dst_path, width):
    w, h = im.size
    if width < w:
        im = im.resize((width, round(h * width / w)), Image.LANCZOS)
    im.save(dst_path, "WEBP", quality=QUALITY, method=6)
    return im.size


def main(argv):
    force = "--force" in argv
    if not os.path.isdir(SRC):
        print("no %s" % SRC)
        return 1
    os.makedirs(OUT, exist_ok=True)

    missing = [s for s in PLATES if not os.path.exists(os.path.join(SRC, s + ".png"))]
    if missing:
        print("no master for: %s" % ", ".join(sorted(missing)))
        return 1

    for slug in sorted(PLATES):
        width, keep = PLATES[slug]
        src = os.path.join(SRC, slug + ".png")
        wide = os.path.join(OUT, slug + ".webp")
        small = os.path.join(OUT, "%s-720.webp" % slug)
        if (not force and os.path.exists(wide)
                and os.path.getmtime(wide) >= os.path.getmtime(src)):
            print("  %-24s up to date" % slug)
            continue
        im = Image.open(src).convert("RGB")
        if keep:
            im = im.crop((0, 0, im.width, keep))
        a = encode(im.copy(), wide, width)
        b = encode(im.copy(), small, SMALL)
        print("  %-24s %dx%d %d KB  +  %dx%d %d KB"
              % (slug, a[0], a[1], os.path.getsize(wide) // 1024,
                 b[0], b[1], os.path.getsize(small) // 1024))
    print("\nDeclare these sizes in clients.py: check 8 fails when the declared "
          "ratio and the file disagree.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
