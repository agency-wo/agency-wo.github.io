/* MINARANK. Zero dependencies.
   The finished page is the CSS default; this only adds choreography. If it
   never runs, the site still looks complete. */
(function () {
  "use strict";

  var docEl = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  /* QA hook: ?static renders the finished page with no choreography, which is
     what no-JS and reduced-motion visitors get. */
  if (/[?&]static\b/.test(window.location.search)) reduce = true;

  if (!reduce) {
    docEl.classList.add("js");

    var played = false;
    var play = function () {
      if (played) return;
      played = true;
      requestAnimationFrame(function () {
        docEl.classList.add("play");
        setTimeout(function () {
          docEl.classList.add("played");
          docEl.classList.remove("play");
        }, 1900);
      });
    };
    var cap = setTimeout(play, 800);
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(function () { clearTimeout(cap); play(); });
    }

    /* Count-up on the stat strips. THE NUMBERS ARE NEVER RE-DERIVED: the
       final frame writes the exact source string back, so after the animation
       the DOM is byte-identical to the HTML the generator emitted, separators
       and suffixes included (57.6k, the Italian 57,6k, 1%). The animation is
       theatre; the value is the record's. */
    var countUp = function (el) {
      var end = el.textContent;
      var m = end.match(/^([^0-9]*)([0-9]+(?:[.,][0-9]+)?)(.*)$/);
      if (!m) return;
      var target = parseFloat(m[2].replace(",", "."));
      var decimals = (m[2].split(/[.,]/)[1] || "").length;
      var sep = m[2].indexOf(",") !== -1 ? "," : ".";
      var t0 = null;
      var DUR = 900;
      var step = function (ts) {
        if (t0 === null) t0 = ts;
        var p = Math.min((ts - t0) / DUR, 1);
        /* the hero's own ease-out: fast start, settled ending */
        var eased = 1 - Math.pow(1 - p, 3);
        if (p < 1) {
          var v = (target * eased).toFixed(decimals).replace(".", sep);
          el.textContent = m[1] + v + m[3];
          requestAnimationFrame(step);
        } else {
          el.textContent = end;   /* the source string, exactly */
        }
      };
      requestAnimationFrame(step);
    };

    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        for (var i = 0; i < entries.length; i++) {
          if (entries[i].isIntersecting) {
            var el = entries[i].target;
            /* a group reveals its children on a small stagger. The delay is
               set through the CSSOM, which style-src does not govern; the cap
               keeps a 17-row list from taking a second to finish. The class
               lands 2 frames later so the delays are in place first; a single
               element needs no delay and reveals on the spot. */
            if (!el.hasAttribute("data-reveal-group")) {
              el.classList.add("in-view");
            } else {
              var kids = el.children;
              for (var k = 0; k < kids.length; k++) {
                kids[k].style.transitionDelay =
                  (Math.min(k, 6) * 70) + "ms";
              }
              /* two frames, so the delays land before the class flips */
              (function (g) {
                requestAnimationFrame(function () {
                  requestAnimationFrame(function () {
                    g.classList.add("in-view");
                  });
                });
              })(el);
              if (el.hasAttribute("data-count")) {
                el.querySelectorAll(".stat-n").forEach(countUp);
              }
            }
            io.unobserve(el);
          }
        }
      }, { threshold: 0.15, rootMargin: "0px 0px -10% 0px" });
      document.querySelectorAll("[data-reveal], [data-reveal-group]")
        .forEach(function (el) { io.observe(el); });
    } else {
      document.querySelectorAll("[data-reveal], [data-reveal-group]")
        .forEach(function (el) { el.classList.add("in-view"); });
    }
  }

  /* mark the current section in the nav */
  var here = window.location.pathname.replace(/index\.html$/, "");
  document.querySelectorAll(".head-nav a[href^='/']").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href.length > 1 && href.indexOf("#") === -1 && here.indexOf(href) === 0) {
      a.setAttribute("aria-current", "true");
    }
  });

  /* ---- header hairline, and the service spotlight -----------------------
     One scroll listener for both. A second listener would run a second rAF
     on every scroll event to do work that fits in the first one.

     THE SPOTLIGHT. Below 719px the 5 service doors collapse to one column and
     a phone has no hover, so the hover state main.css gives them never fires
     on the device this market reads on. This marks whichever door is nearest
     the middle of the viewport, which walks the reader through all 5 as the
     page moves. On a desktop :hover still wins, because a pointer deliberately
     on a door beats a guess made from scroll position.

     Skipped entirely when reduce is on: the doors are then exactly what CSS
     alone makes them, which is the contract at the top of this file. */
  var head = document.querySelector(".site-head");
  var doors = reduce ? [] :
    [].slice.call(document.querySelectorAll(".svc-list > li"));
  var near = null;

  var spotlight = function () {
    if (!doors.length) return;
    var mid = window.innerHeight / 2;
    /* one bounds check for the whole list before measuring 5 rects: scrolling
       anywhere else on the page costs 2 reads rather than 5.

       The test is whether the LIST intersects the viewport, so it is the
       first door's top against the bottom of the screen and the last door's
       bottom against the top of it. Reading last.top instead of first.top
       looks equivalent and is not: below 719px these 5 stack into a block
       taller than a phone, so the last door's top only comes on screen near
       the end of the list, and the spotlight sat dark for most of the scroll.
       The QA walk caught it -- it reached 1 door of 5. */
    var first = doors[0].getBoundingClientRect();
    var last = doors[doors.length - 1].getBoundingClientRect();
    var best = null;
    if (first.top < window.innerHeight && last.bottom > 0) {
      var bestGap = Infinity;
      for (var i = 0; i < doors.length; i++) {
        var r = doors[i].getBoundingClientRect();
        var gap = Math.abs((r.top + r.bottom) / 2 - mid);
        if (gap < bestGap) { bestGap = gap; best = doors[i]; }
      }
    }
    if (best === near) return;
    if (near) near.classList.remove("is-near");
    if (best) best.classList.add("is-near");
    near = best;
  };

  if (head || doors.length) {
    var ticking = false;
    var onScroll = function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        if (head) head.classList.toggle("scrolled", window.scrollY > 24);
        spotlight();
        ticking = false;
      });
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    onScroll();
  }

  /* ---- the free audit form ------------------------------------------------
     Two submit paths, one result.

     No JS: a plain POST. Native validation runs, because novalidate is set
     from HERE and never from the markup: in the markup it would let a JS-off
     visitor send an empty form. Web3Forms returns to /start/?sent=1#sent and
     the :target rule in main.css reveals the confirmation before first paint.

     JS: intercept, post the same FormData, reveal the same panel in place.

     Rule 30 holds. Nothing here runs on load except the ?sent= check, and the
     request happens because somebody pressed a button.

     EVERY SENTENCE THIS SCRIPT SAYS COMES OFF THE FORM. There are three, and
     they used to be English literals down there, so an Italian visitor read
     Italian until the button was pressed and English afterwards. They are
     data- attributes emitted by shell.form_js, not an {en,it,sq} table in
     here: script-src has no unsafe-inline so a per-language script is out, and
     a table falls back to English on a language nobody told it about, which is
     the half-translated page the gate exists to catch. If any of the three is
     missing this whole block does not run and the native POST stands, which
     works and is already in the reader's language. */
  var audit = document.getElementById("audit");
  var af = document.getElementById("audit-form");

  /* the fragment should survive the redirect; this is the belt for when it
     does not, which is why the redirect carries both */
  if (audit && /[?&]sent=1(&|$)/.test(window.location.search)) {
    audit.classList.add("is-sent");
  }

  var doneEl = document.getElementById("sent");
  var say = document.getElementById("af-say");
  var send = document.getElementById("af-send");
  var sendText = document.getElementById("af-send-text");
  /* the words, in the page's own language */
  var T_SENDING = af && af.getAttribute("data-sending");
  var T_SENDING_SAY = af && af.getAttribute("data-sending-say");
  var T_ERROR = af && af.getAttribute("data-error");

  /* Every hook and every string, tested BEFORE novalidate is set. This used to
     read `af && audit && ...`, set novalidate, and then throw on the first
     missing hook: that leaves a form which still posts natively AND has had
     its native validation taken away, so an empty submit reaches Web3Forms.
     A missing hook now costs the upgrade and nothing else. */
  if (af && audit && doneEl && say && send && sendText &&
      T_SENDING && T_SENDING_SAY && T_ERROR &&
      window.fetch && window.FormData && af.checkValidity) {
    af.setAttribute("novalidate", "novalidate");

    var sendLabel = sendText.textContent;  /* read once, never hardcoded twice */
    var sending = false;

    var mark = function () {
      var req = af.querySelectorAll("input[required]");
      for (var i = 0; i < req.length; i++) {
        req[i].setAttribute("aria-invalid",
          req[i].checkValidity() ? "false" : "true");
      }
    };

    var settle = function (ok) {
      sending = false;
      send.disabled = false;
      sendText.textContent = sendLabel;
      if (ok) {
        say.classList.remove("is-err");
        say.textContent = "";
        audit.classList.add("is-sent");
        doneEl.focus();
      } else {
        /* never a dead button and never an alert(): name the other 2 ways */
        say.classList.add("is-err");
        say.textContent = T_ERROR;
        send.focus();
      }
    };

    af.addEventListener("submit", function (e) {
      e.preventDefault();
      if (sending) return;

      /* honeypot. Look sent, say nothing, never explain why. */
      var bot = af.querySelector("[name=botcheck]");
      if (bot && bot.checked) { audit.classList.add("is-sent"); return; }

      af.classList.add("was-validated");
      mark();
      if (!af.checkValidity()) {
        /* no summary message: the focused field announces its own label and
           its own error through aria-describedby, and 2 voices is noise */
        var bad = af.querySelector("input:invalid");
        if (bad) bad.focus();
        return;
      }

      sending = true;
      send.disabled = true;
      sendText.textContent = T_SENDING;
      /* disabling the button drops focus to the body, so this live region is
         the only thing telling a screen reader that anything happened */
      say.classList.remove("is-err");
      say.textContent = T_SENDING_SAY;

      window.fetch(af.getAttribute("action"), {
        method: "POST",
        body: new FormData(af)
      }).then(function (r) {
        return r.json();
      }).then(function (json) {
        settle(!!(json && json.success));
      }).catch(function () {
        settle(false);
      });
    });

    /* clear the red the moment somebody starts fixing it */
    af.addEventListener("input", function (e) {
      if (af.classList.contains("was-validated") && e.target.checkValidity()) {
        e.target.setAttribute("aria-invalid", "false");
      }
    });
  }
})();
