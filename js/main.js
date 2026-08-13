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
     Enhancement only. With this file blocked the form still works: it is a
     native POST and Web3Forms returns the visitor to /start/#sent, where the
     :target rule in main.css reveals the confirmation on its own. Everything
     below exists so nobody has to leave the page. */
  var af = document.getElementById("audit-form");
  if (af && window.fetch && window.FormData) {
    var section = document.getElementById("audit");
    var done = document.getElementById("sent");
    var fail = document.getElementById("af-fail");
    var send = document.getElementById("af-send");
    var label = send ? send.innerHTML : "";

    var mark = function () {
      /* aria-invalid per field, which no other form in this workspace sets */
      var fields = af.querySelectorAll("input[required]");
      for (var i = 0; i < fields.length; i++) {
        fields[i].setAttribute("aria-invalid", fields[i].checkValidity() ? "false" : "true");
      }
    };

    af.addEventListener("submit", function (e) {
      e.preventDefault();
      if (fail) fail.hidden = true;

      /* honeypot: a bot filled the field no human can see. Look sent, do
         nothing, and never tell it why. */
      var bot = af.querySelector('[name="botcheck"]');
      if (bot && bot.checked) {
        if (section) section.classList.add("is-sent");
        return;
      }

      af.classList.add("was-validated");
      mark();
      if (!af.checkValidity()) {
        var bad = af.querySelector("input:invalid");
        if (bad) bad.focus();
        return;
      }

      if (send) { send.disabled = true; send.textContent = "Sending"; }
      fetch(af.action, { method: "POST", body: new FormData(af) })
        .then(function (r) { return r.json(); })
        .then(function (json) {
          if (!json || !json.success) throw new Error("rejected");
          if (section) section.classList.add("is-sent");
          if (done) done.focus();
        })
        .catch(function () {
          /* Never a dead button and never an alert(): the panel names the
             two other ways to reach us. */
          if (fail) { fail.hidden = false; fail.focus(); }
          if (send) { send.disabled = false; send.innerHTML = label; }
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
