"""Emit the MINARANK service pages from content.py through shell.py.

Run from the project root:  python .build/gen_pages.py
Writes only when bytes change, so a second run reports nothing and produces
no git diff. Run gen_sitemap.py after this, always last.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell  # noqa: E402
from content import SERVICES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
EM_DASH = chr(0x2014)

# Figure plates, in the one drawing grammar. Zero numerals inside any figure.
REG = ('<path class="pl-reg" d="M0 -8 V-3 M-8 0 H-3 M160 -8 V-3 M168 0 H163 '
       'M0 168 V163 M-8 160 H-3 M160 168 V163 M168 160 H163" fill="none" '
       'stroke="#E4E1D9" stroke-width="1"/>')
FRAME = ('<rect class="pl-frame" x="0.5" y="0.5" width="159" height="159" '
         'fill="none" stroke="#E4E1D9" stroke-width="1"/>')

FIGS = {
    "ladder": f'''{REG}
              {FRAME}
              <path fill="none" stroke="#E4E1D9" stroke-width="1" d="M8 24 H152 M8 40 H152 M8 56 H152 M8 72 H152 M8 88 H152 M8 104 H152 M8 120 H152 M8 136 H152 M8 152 H152 M8 8.5 H152"/>
              <rect x="8" y="92" width="44" height="12" fill="none" stroke="#5B5F7A" stroke-width="1.5"/>
              <path class="pl-subject" pathLength="1" fill="none" stroke="#1B1F3B" stroke-width="2" d="M8 152 H36 V136 H60 V120 H84 V104 H108 V88 H122 V72 H134 V56 H142 V40 H148 V24"/>
              <path class="pl-coral" fill="none" stroke="#FF6B4A" stroke-width="2" d="M142 20 H146 V16 H150 V12 H154"/>''',

    "instrument": f'''{REG}
              <path fill="none" stroke="#E4E1D9" stroke-width="1" d="M20 28 V148 M32 28 V148 M44 28 V148 M56 28 V148 M68 28 V148 M80 28 V148 M92 28 V148 M104 28 V148 M116 28 V148 M128 28 V148 M140 28 V148"/>
              <rect x="8" y="8" width="144" height="144" fill="none" stroke="#1B1F3B" stroke-width="2"/>
              <path fill="none" stroke="#1B1F3B" stroke-width="2" d="M8 24 H152"/>
              <rect x="13" y="13" width="3" height="3" fill="#1B1F3B"/><rect x="19" y="13" width="3" height="3" fill="#1B1F3B"/><rect x="25" y="13" width="3" height="3" fill="#1B1F3B"/>
              <rect x="20" y="40" width="68" height="48" fill="#1B1F3B"/>
              <path fill="none" stroke="#5B5F7A" stroke-width="1.5" stroke-dasharray="4 4" d="M10 104 H150"/>
              <rect class="pl-coral-fill" x="132" y="32" width="8" height="8" fill="#FF6B4A"/>''',

    "citation": f'''{REG}
              {FRAME}
              <rect x="8" y="8" width="144" height="64" rx="8" fill="none" stroke="#5B5F7A" stroke-width="1.5"/>
              <rect x="22" y="22" width="100" height="5" fill="#E4E1D9"/>
              <rect x="22" y="34" width="116" height="5" fill="#E4E1D9"/>
              <rect x="22" y="46" width="84" height="5" fill="#E4E1D9"/>
              <path class="pl-subject" pathLength="1" fill="none" stroke="#1B1F3B" stroke-width="2" d="M24 72 V92 H62 V112 H100 V126"/>
              <rect x="100" y="126" width="44" height="18" fill="none" stroke="#1B1F3B" stroke-width="2"/>
              <path class="pl-coral" fill="none" stroke="#FF6B4A" stroke-width="2" d="M140 122 H144 V118 H148 V114 H152"/>''',

    "crossover": f'''{REG}
              {FRAME}
              <path fill="none" stroke="#5B5F7A" stroke-width="1.5" stroke-dasharray="5 4" d="M8 84 H56 V80 H104 V76 H152"/>
              <path class="pl-subject" pathLength="1" fill="none" stroke="#1B1F3B" stroke-width="2" d="M8 140 H36 V124 H62 V104 H86 V72 H110 V50 H134 V28 H152"/>
              <rect class="pl-coral-fill" x="84" y="78" width="4" height="4" fill="#FF6B4A"/>''',
}


def jsonld(svc):
    url = shell.SITE + "/" + svc["slug"] + "/"
    graph = [
        {
            "@type": "Service",
            "@id": url + "#service",
            "name": svc.get("schema_name", svc["nav"]),
            "serviceType": svc.get("schema_name", svc["nav"]),
            "description": svc["description"],
            "url": url,
            "provider": {"@id": shell.SITE + "/#org"},
            "areaServed": ["AL", "IT", "Worldwide"],
            "availableLanguage": ["en", "it", "sq"],
        },
        {
            "@type": "FAQPage",
            "@id": url + "#faq",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                for q, a in svc["faq"]
            ],
        },
        {
            "@type": "BreadcrumbList",
            "@id": url + "#crumbs",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": shell.SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": svc["nav"], "item": url},
            ],
        },
    ]
    body = {"@context": "https://schema.org", "@graph": graph}
    return json.dumps(body, indent=2, ensure_ascii=False)


def strip_tags(s):
    out, depth = [], 0
    for ch in s:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif depth == 0:
            out.append(ch)
    return "".join(out)


def render(svc):
    url = "/" + svc["slug"] + "/"
    page = {
        "url": url,
        "title": svc["title"] + " " + shell.DOT + " minarank",
        "description": svc["description"],
        "og_desc": svc.get("og_desc", svc["description"]),
        "jsonld": jsonld(svc),
    }
    parts = [shell.head(page), shell.header()]
    a = parts.append

    a('\n  <main id="main">\n    <div class="wrap">\n')
    a('      <header class="page-head">\n')
    a(shell.crumbs(svc["nav"]) + "\n")
    a(f'        <p class="eyebrow">Service {svc["n"]}</p>\n')
    a(f'        <h1 class="page-title">{svc["h1"]}</h1>\n')
    a(f'        <p class="standfirst">{svc["standfirst"]}</p>\n')
    a('      </header>\n\n')

    a('      <p class="finding">\n        <span class="finding-label">The finding</span>\n')
    a(f'        {svc["finding"]}\n      </p>\n\n')

    a('      <div class="grid">\n        <div class="prose">\n\n')

    for heading, blocks in svc["sections"]:
        a(f'          <h2>{heading}</h2>\n')
        for b in blocks:
            a(f'          {b}\n')
        a("\n")

    a('          <h2>What we do</h2>\n          <ol class="ledger">\n')
    for i, item in enumerate(svc["ledger"], 1):
        title, body = item[0], item[1]
        is_last = len(item) > 2 and item[2]
        a('            <li>\n')
        a(f'              <span class="ledger-n">{i:02d}</span>\n')
        a('              <div>\n')
        a(f'                <h3>{title}</h3>\n')
        a(f'                <p>{body}</p>\n')
        if is_last:
            a(f'                <p class="payoff">{shell.TICK}\n')
            a(f'                  {svc["payoff"]}</p>\n')
        a('              </div>\n            </li>\n')
    a('          </ol>\n\n')

    a('          <section class="exclusions">\n            <h2>What we do not do</h2>\n            <ul>\n')
    for x in svc["exclusions"]:
        a(f'              <li>{x}</li>\n')
    a('            </ul>\n          </section>\n\n')

    a('          <section class="faq">\n            <h2>Questions worth asking</h2>\n')
    for q, ans in svc["faq"]:
        a('            <div class="faq-item">\n')
        a(f'              <h3 class="faq-q">{q}</h3>\n')
        a(f'              <p class="faq-a">{ans}</p>\n')
        a('            </div>\n')
    a('          </section>\n\n        </div>\n\n')

    a('        <aside class="side" aria-label="At a glance">\n')
    a('          <figure class="fig fig-lead">\n')
    a('            <svg viewBox="-10 -10 180 180" aria-hidden="true">\n              ')
    a(FIGS[svc["fig"]] + "\n            </svg>\n")
    a(f'            <figcaption class="fig-cap">{svc["fig_cap"]}</figcaption>\n')
    a('          </figure>\n\n')
    note_h, note_b = svc["side_note"]
    a(f'          <div class="side-block">\n            <p class="side-h">{note_h}</p>\n')
    a(f'            <p>{note_b}</p>\n          </div>\n\n')
    a('          <div class="side-block">\n            <p class="side-h">Related</p>\n')
    a('            <ul class="side-list">\n')
    for href, label in svc["related"]:
        a(f'              <li><a href="{href}">{label}</a></li>\n')
    a('            </ul>\n          </div>\n        </aside>\n      </div>\n')

    a(shell.tail(svc["tail"]))
    a('\n    </div>\n  </main>\n')
    a(shell.footer())
    return "".join(parts)


def write(path, content):
    assert EM_DASH not in content, "em-dash in " + path
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    old = None
    if os.path.exists(full):
        old = io.open(full, encoding="utf-8", newline="").read()
    if old == content:
        print("unchanged", path)
        return False
    io.open(full, "w", encoding="utf-8", newline=NL).write(content)
    print("wrote    ", path, len(content), "bytes")
    return True


if __name__ == "__main__":
    changed = 0
    for svc in SERVICES:
        if write(os.path.join(svc["slug"], "index.html"), render(svc)):
            changed += 1
    print(f"{changed} page(s) changed of {len(SERVICES)}")
