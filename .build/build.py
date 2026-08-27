# -*- coding: utf-8 -*-
"""Every generator, in rule 34's order, in one command.

Rule 34 has always named the order. What it could not do is run it. The order
lived in a document and in whatever loop somebody typed that afternoon, and on
27 August 2026 the loop ran 10 of the 11. gen_launch was the omission, so
llms.txt and llms-full.txt went on describing the previous build for 5 days
while every page carried a fresh Search Console reading. Nothing failed. The
gate was green, the pages were right, and the two files written specifically
for AI assistants told them a number the site had retracted.

That is the shape of the bug this file exists to make impossible: not a wrong
step, a missing one. A loop typed by hand is correct only for as long as the
person typing it remembers all 11, and the one that gets forgotten is always
the one at the end that does not visibly change a page.

So the order stops being a thing to remember. ORDER below is the list; gate
check 52 holds it to rule 34 and to the generators actually sitting in this
directory, so a generator added without being wired in here fails the gate
rather than quietly never running.

Run from the project root:

    python .build/build.py             everything, then the gate
    python .build/build.py --no-ping   the same, minus IndexNow's 3 minutes

The exit code is the gate's, so this can stand in front of a commit.
"""
import os
import subprocess
import sys
import time

# verify.py writes straight to this terminal rather than through us, so our own
# progress has to be on the screen before it starts. Piped, a block-buffered
# stdout hands the gate's report to the reader ahead of the build it describes.
# Set once here rather than flushed at each print, because the print this gets
# added to last is the one whose absence is confusing.
sys.stdout.reconfigure(line_buffering=True)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# Rule 34, as a list rather than a sentence. gen_sitemap is last because it
# describes what the others emitted, and gen_launch is second to last for the
# same reason: both read the built HTML, so either one running early describes
# the previous build. verify is not here because it is not a generator; it runs
# after all of them and its exit code becomes ours.
ORDER = [
    "gen_pages", "gen_docs", "gen_cases", "gen_home", "gen_blog",
    "gen_glossary", "gen_term_pages", "gen_404", "gen_feed",
    "gen_launch", "gen_sitemap",
]

# Only gen_launch talks to the network, so only gen_launch is offered the flag.
# Handing it to every generator would invite one to grow a meaning for it.
TAKES_NO_PING = {"gen_launch"}


def run(mod, extra=()):
    """One generator. Its last line is its summary; on failure, all of it.

    Failure stops the build. A generator that died leaves the ones after it
    reading half a site, and gen_launch and gen_sitemap would then describe
    that half with total confidence.
    """
    argv = [sys.executable, os.path.join(HERE, mod + ".py")] + list(extra)
    t0 = time.time()
    p = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    lines = [ln for ln in (p.stdout or "").split("\n") if ln.strip()]
    if p.returncode != 0:
        print("  %-15s FAILED (exit %d)" % (mod, p.returncode))
        for ln in lines + [ln for ln in (p.stderr or "").split("\n") if ln.strip()]:
            print("      " + ln)
        sys.exit(p.returncode)
    print("  %-15s %-58s %5.1fs"
          % (mod, (lines[-1] if lines else "")[:58], time.time() - t0))


def main(argv):
    no_ping = "--no-ping" in argv
    print("build: %d generators in rule 34 order%s"
          % (len(ORDER), ", IndexNow skipped" if no_ping else ""))
    t0 = time.time()
    for mod in ORDER:
        run(mod, ["--no-ping"] if no_ping and mod in TAKES_NO_PING else ())
    print("  %-15s %5.1fs total\n" % ("", time.time() - t0))
    # Not captured: the gate's report is the point of running it, and burying
    # it behind this script's formatting would make the gate worth less.
    return subprocess.run([sys.executable, os.path.join(HERE, "verify.py")],
                          cwd=ROOT).returncode


# Guarded so verify.py can import ORDER without running a build. Check 52 does
# exactly that, and an unguarded module would make the gate rebuild the site.
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
