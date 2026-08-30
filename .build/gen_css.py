# -*- coding: utf-8 -*-
"""Emit css/*.css from the commented source in .build/css/.

WHY THIS EXISTS. The homepage was 204,735 bytes against a gate that fails at
200 KB: 65 bytes of headroom, and nothing could be added to the site without
breaking the build. 52% of main.css and 57% of tokens.css were comments. That
reasoning is the most valuable thing in the stylesheet and it is why the design
is coherent, so deleting it was never an option. It simply does not need to be
sent to a browser, which cannot read it.

Source moves to .build/css/, where the rest of this site's source already lives,
and the root keeps the served file. That is the model posts.py and blog/ already
use; the stylesheet was the one thing authored in the output location.

Rule 30 says "no build step at SERVE time", and this is not one. The served file
is still static hand-written CSS on the same origin, and a visitor's request
touches nothing but a file.

RUNS FIRST. shell.stamped() appends ?v=<sha1 of the file's own bytes>, reading
the file at the ROOT. If the pages were built before this, every page would ship
a hash of the previous stylesheet and the cache would serve the old one to
everybody who had it. That is why gen_css leads rule 34's order.

THE LICENCE COMMENT STAYS. fonts.css opens by crediting Luigi Gorlero and
Collletttivo for Apfel Grotezk and Omnibus-Type for Archivo, both SIL OFL. A
site that credits its clients' work does not strip the type designers' names to
save 229 bytes.

WHAT DOES NOT CHANGE. verify.py's content checks read the SOURCE, not this
output, so check 9's banned-class scan and check 18's mark scan still see the
comments. A check that only saw the stripped file would be weaker than it is
today, and this repo does not loosen a check to make something pass. Only the
weight check reads the output, because the output is what ships.

Run from the project root:  python .build/gen_css.py
"""
import hashlib
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(HERE, "css")
OUT = os.path.join(ROOT, "css")
NL = chr(10)

# fonts.css keeps its first comment, which is the type designers' credit.
KEEP_FIRST_COMMENT = {"fonts.css"}


def strip_comments(text, keep_first=False):
    """Remove every /* */ block, optionally sparing the first.

    CSS has one comment form and it does not nest, so a non-greedy scan is
    complete. It is only unsafe when the delimiters appear inside a string or a
    url(), which was checked across all three files and does not happen; the
    assertion below keeps that true if somebody adds one.
    """
    for quoted in re.findall(r'"[^"' + NL + r']*"|\'[^\'' + NL + r']*\'', text):
        assert "/*" not in quoted and "*/" not in quoted, (
            "a comment delimiter inside a string literal: " + quoted[:40])

    spans = list(re.finditer(r"/\*.*?\*/", text, re.S))
    out, last = [], 0
    for i, m in enumerate(spans):
        out.append(text[last:m.start()])
        if keep_first and i == 0:
            out.append(m.group(0))
        last = m.end()
    out.append(text[last:])
    body = "".join(out)

    # the strip leaves ragged whitespace where a block comment used to sit
    body = NL.join(line.rstrip() for line in body.split(NL))
    body = re.sub(NL + "{3,}", NL + NL, body)
    return body.strip() + NL


def write_if_changed(path, body):
    old = io.open(path, encoding="utf-8").read() if os.path.exists(path) else None
    if old == body:
        return "unchanged"
    io.open(path, "w", encoding="utf-8", newline=NL).write(body)
    return "written"


def main():
    if not os.path.isdir(SRC):
        print("gen_css: no .build/css/ to build from")
        return 1
    total_src = total_out = 0
    for name in sorted(os.listdir(SRC)):
        if not name.endswith(".css"):
            continue
        src = io.open(os.path.join(SRC, name), encoding="utf-8").read()
        body = strip_comments(src, keep_first=name in KEEP_FIRST_COMMENT)

        # a strip that unbalanced the braces would have eaten real CSS
        assert body.count("{") == body.count("}"), name + ": unbalanced braces"

        state = write_if_changed(os.path.join(OUT, name), body)
        total_src += len(src.encode("utf-8"))
        total_out += len(body.encode("utf-8"))
        print("  %-12s %s  %6d -> %6d bytes" % (name, state, len(src), len(body)))
    saved = total_src - total_out
    print("  css %d -> %d bytes, %d saved (%.0f%% was comment)"
          % (total_src, total_out, saved, 100.0 * saved / total_src))
    return 0


if __name__ == "__main__":
    sys.exit(main())
