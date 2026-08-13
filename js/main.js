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

    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        for (var i = 0; i < entries.length; i++) {
          if (entries[i].isIntersecting) {
            entries[i].target.classList.add("in-view");
            io.unobserve(entries[i].target);
          }
        }
      }, { threshold: 0.15, rootMargin: "0px 0px -10% 0px" });
      document.querySelectorAll("[data-reveal]").forEach(function (el) {
        io.observe(el);
      });
    } else {
      document.querySelectorAll("[data-reveal]").forEach(function (el) {
        el.classList.add("in-view");
      });
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

  /* hairline under the header after 24px */
  var head = document.querySelector(".site-head");
  if (head) {
    var ticking = false;
    var onScroll = function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        head.classList.toggle("scrolled", window.scrollY > 24);
        ticking = false;
      });
    };
    window.addEventListener("scroll", onScroll, { passive: true });
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
     request happens because somebody pressed a button. */
  var audit = document.getElementById("audit");
  var af = document.getElementById("audit-form");

  /* the fragment should survive the redirect; this is the belt for when it
     does not, which is why the redirect carries both */
  if (audit && /[?&]sent=1(&|$)/.test(window.location.search)) {
    audit.classList.add("is-sent");
  }

  if (af && audit && window.fetch && window.FormData && af.checkValidity) {
    af.setAttribute("novalidate", "novalidate");

    var doneEl = document.getElementById("sent");
    var say = document.getElementById("af-say");
    var send = document.getElementById("af-send");
    var sendText = document.getElementById("af-send-text");
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
        say.textContent = "That did not send. Use the email or the WhatsApp " +
          "link below and we will pick it up from there.";
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
      sendText.textContent = "Sending";
      /* disabling the button drops focus to the body, so this live region is
         the only thing telling a screen reader that anything happened */
      say.classList.remove("is-err");
      say.textContent = "Sending your details.";

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
