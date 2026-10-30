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

# slug -> (width of the top rung, how tall a window of the 2000px master, how far
# down that window starts)
#
# ONE RATIO for all six, because a grid of six wants one, but the window is placed
# per site because the sites do not agree on where their hero ends. Measured off
# the masters on 2026-10-24, as the row where the page's background changes:
#
#     iglisi 1468   census ~1519   bruna 1560   proaffy 1628
#     victoria: its two buttons reach 1708      vila flamuri 1767
#
# The whole frame was shipped at first, and Iglisi's plate was 27% white: its
# hero ends at 1472 of 2000 and the rest is the top of the next section. 1700
# cut that to 14% on the argument that it would read as the page continuing.
# It does not. It reads as a broken screenshot, which is what the owner called
# it on 2026-10-30, and it was never only Iglisi: at 1700 the window also
# landed inside a flat gap on ProAffy (8%) and Census (3%).
#
# 1450 is MEASURED, not guessed: the tallest window where the last 12 rows of
# all six masters carry real variation. The gaps that forced it down are
# iglisi 1472-1810, census 1654-1873, proaffy 1585-1836 and vila 1458-1636,
# and every value between 1460 and 1940 falls inside at least one of them.
#
# The cost is the one the 1700 note named: Victoria's clay CTA buttons sit at
# 1708 and are now outside the frame. That trade is deliberate. A plate missing
# a button still reads as the client's site; a plate with a blank seventh at
# the bottom reads as our mistake, and it was on three of the six.
#
# Re-measure with scratch pick_window.py when a client rebuilds, rather than
# nudging this number until the one plate you are looking at stops being white.
WINDOW = 1450
# The offsets stop the cut slicing a line of text in half, which 1450 at
# offset 0 did to Victoria: the bottom of the plate took the top 40% of
# "Elegance greke e luksit" and half-letters read as a rendering fault, not as
# a crop. They are 2 to 62 rows, so 1 to 31 CSS pixels off the top of a nav.
#
# Found by measuring the LEFT 52% only, with scratch pick_offsets2.py. A test
# over the full width finds nothing on 4 of the 6, because those heroes carry
# a photograph running the whole height and no row is ever flat. Cutting
# through the photograph is fine and always was. Cutting through the words is
# the thing that looks broken, and the words are in the left column on all six.
#
# Only Victoria takes one. The measurement offers an offset for all six, but
# it cannot tell "quiet between two lines of text" from "quiet because this is
# the dead band", and applying all six made Iglisi worse: 32 rows down put its
# bottom 10 rows PAST the hero, and sliced the gold announcement bar off the
# top to pay for it. At offset 0 the other five already end on content with no
# dead rows, so they keep their full nav. Look at the plate before trusting
# the number; the number cannot see.
PLATES = {
    "iglisi-home": (900, WINDOW, 0),
    # Was 20, to pull Victoria's buttons at 1708 inside a 1700 window, which
    # the window no longer reaches. 29 is the text-clearance offset: at 0 the
    # cut takes the top 40% of "Elegance greke e kuruar" and half-letters read
    # as a rendering fault rather than as a crop.
    "victoria-home": (900, WINDOW, 29),
    "bruna-home": (900, WINDOW, 0),
    "proaffy-home": (900, WINDOW, 0),
    "census-properties-home": (900, WINDOW, 0),
    "vila-flamuri-home": (900, WINDOW, 0),
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
        width, keep, top = PLATES[slug]
        src = os.path.join(SRC, slug + ".png")
        wide = os.path.join(OUT, slug + ".webp")
        small = os.path.join(OUT, "%s-720.webp" % slug)
        if (not force and os.path.exists(wide)
                and os.path.getmtime(wide) >= os.path.getmtime(src)):
            print("  %-24s up to date" % slug)
            continue
        im = Image.open(src).convert("RGB")
        if keep:
            if top + keep > im.height:
                print("  %-24s window %d..%d runs past the %dpx master"
                      % (slug, top, top + keep, im.height))
                return 1
            im = im.crop((0, top, im.width, top + keep))
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
