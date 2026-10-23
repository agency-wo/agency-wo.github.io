"""Encode the section photographs from _source/photos into assets/photos.

RUN BY HAND, like trace_proof.py. **Not a build dependency**: it imports PIL,
and shell.image_size() exists precisely so the build never has to. Run it when
an original changes, commit what it writes, and the build only ever reads the
WebP that comes out.

    python .build/make_photos.py            encode anything missing or stale
    python .build/make_photos.py --force    re-encode everything

Two rungs per image, which is the convention assets/plates already uses:
<slug>.webp at WIDE and <slug>-720.webp, paired by shell.with_720(). The
originals are 1672 wide, so WIDE is 1440: a real downscale rather than an
upscale that would cost bytes and buy nothing.
"""
import io
import os
import sys

from PIL import Image                                   # not a build dependency

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "_source", "photos")
OUT = os.path.join(ROOT, "assets", "photos")

WIDE = 1440
SMALL = 720
QUALITY = 82

# original filename -> slug. The generator titles are not filenames anybody
# would choose, and the slug is what the markup and the alt text live beside.
PHOTOS = {
    "Misty Adriatic Town by the Sea.png": "town-dawn",
    "Quiet Workshop Café Opening onto Stone Square.png": "shop-before-opening",
    "Red Pin on a Coastal City Map.png": "map-pin",
    "Serene Coastal Library Study.png": "library-study",
    "Quiet Café Table by the Window.png": "cafe-table",
    "Blueprints and Shavings on a Workbench.png": "workbench-paper",
    "Monochrome Concrete Stairway to Sky.png": "concrete-stairway",
    "Serene Mediterranean Workspace by the Water.png": "desk-by-window",
}


def encode(src_path, dst_path, width):
    im = Image.open(src_path).convert("RGB")
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

    missing = [f for f in PHOTOS if not os.path.exists(os.path.join(SRC, f))]
    if missing:
        print("MISSING originals, nothing written:")
        for f in missing:
            print("  %s" % f)
        return 1

    total_in = total_out = 0
    for fname, slug in sorted(PHOTOS.items(), key=lambda kv: kv[1]):
        src = os.path.join(SRC, fname)
        total_in += os.path.getsize(src)
        for width, suffix in ((WIDE, ""), (SMALL, "-720")):
            dst = os.path.join(OUT, "%s%s.webp" % (slug, suffix))
            if not force and os.path.exists(dst) \
                    and os.path.getmtime(dst) >= os.path.getmtime(src):
                total_out += os.path.getsize(dst)
                print("  unchanged  %s%s.webp" % (slug, suffix))
                continue
            w, h = encode(src, dst, width)
            total_out += os.path.getsize(dst)
            print("  wrote      %-28s %dx%-4d %6.1f KB"
                  % ("%s%s.webp" % (slug, suffix), w, h,
                     os.path.getsize(dst) / 1024))
    print()
    print("  originals %.1f MB  ->  served %.1f KB across %d files (%.1f%%)"
          % (total_in / 1048576, total_out / 1024, len(PHOTOS) * 2,
             100.0 * total_out / total_in))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
