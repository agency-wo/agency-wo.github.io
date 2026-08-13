"""Emit 404.html. One document, English, at the root.

NOT folded into gen_docs.py, whose PAGES is multiplied by i18n.LANGS. GitHub
Pages serves exactly one 404 per origin, so this one answers /it/anything and
/sq/anything too. That is the platform's constraint and not something to paper
over with a language sniffer: a visitor who is lost gets English chrome and a
working way back, which beats a blank page in the right language.

It was hand-authored and carried no header, footer or band, so anyone who
landed here from a bad link had one link out of a site with 5 services and 4
case studies. Gate check 7 used to skip it by name; that exemption is gone,
which is the point of generating it.

Run from the project root:  python .build/gen_404.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell  # noqa: E402
from gen_pages import write  # noqa: E402

NL = chr(10)
LANG = "en"


def render():
    c = shell.ch(LANG)
    # Ten ruled results with nothing on any of them. The copy already says the
    # page never ranked, and .serp draws exactly that: this is the sentence
    # rather than a decoration beside it.
    #
    # .serp is reused verbatim. It needs a positioned ancestor and nothing
    # else, so the hero's rules are untouched and cannot regress. aria-hidden
    # goes on .serp itself here, because unlike the hero the heading beside it
    # is real text rather than an image of one.
    rules = "".join(f'<i data-n="{i + 1}"></i>' for i in range(10))

    page = {"url": "/404.html",
            "title": f"{c.ERR_TITLE} {shell.DOT} {shell.BRAND}",
            "description": c.ERR_SAY,
            "noindex": True}

    body = f'''
      <div class="err-box">
        <span class="serp" aria-hidden="true">{rules}</span>
        <h1>40<span>4</span></h1>
      </div>
      <p>{c.ERR_SAY}
        <a href="{shell.localise("/", LANG)}">{c.ERR_BACK}</a>.</p>
'''
    return (shell.head(page, LANG) + shell.header(LANG) +
            '\n  <main class="err" id="main">\n' + body + '  </main>\n' +
            shell.footer(LANG, None, c.ERR_BAND_H, c.ERR_BAND_NOTE))


if __name__ == "__main__":
    html = render()
    # The band is not optional. Check 27 skips only a page with no band at all,
    # so a band without its actions is an outright finding rather than a quiet
    # omission, and a lost visitor is exactly who should be offered the audit.
    assert 'class="band-actions"' in html, "the 404 lost its band CTA"
    assert "canonical" not in html, "a 404 must not claim a canonical"
    assert "ld+json" not in html, "a 404 must not carry structured data"
    write("404.html", html)
