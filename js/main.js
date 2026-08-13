/* MINARANK · hero orchestration, scroll reveals, standings rail. Zero deps.
   The finished page is the CSS default; this file only adds choreography.
   If it never runs, the site still looks complete. */
(function () {
  "use strict";

  var docEl = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  /* QA hook: ?static renders the finished page with zero choreography,
     identical to the no-JS experience. */
  if (/[?&]static\b/.test(window.location.search)) reduce = true;

  if (!reduce) {
    docEl.classList.add("js");

    /* hero: arm, play, then strip the machinery so hover/glissando and the
       exit parallax own the letters. Coral lands at 1350ms; 1900ms covers
       the full sequence including the summit stamp. */
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

    /* scroll reveals: play once, let go */
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        for (var i = 0; i < entries.length; i++) {
          if (entries[i].isIntersecting) {
            entries[i].target.classList.add("in-view");
            io.unobserve(entries[i].target);
          }
        }
      }, { threshold: 0.2, rootMargin: "0px 0px -10% 0px" });
      document.querySelectorAll("[data-reveal]").forEach(function (el) {
        io.observe(el);
      });
    } else {
      document.querySelectorAll("[data-reveal]").forEach(function (el) {
        el.classList.add("in-view");
      });
    }

    /* standings rail fallback for engines without scroll-driven animations */
    var rail = document.querySelector(".rail");
    if (rail && !(window.CSS && CSS.supports("animation-timeline: scroll()"))) {
      rail.classList.add("rail-fallback");
      var railN = rail.querySelector(".rail-n");
      var railTicking = false;
      var onRail = function () {
        if (railTicking) return;
        railTicking = true;
        requestAnimationFrame(function () {
          var max = document.documentElement.scrollHeight - window.innerHeight;
          var p = max > 0 ? Math.min(1, window.scrollY / max) : 0;
          var n = Math.max(1, 10 - Math.floor(p * 9.0001));
          /* quantized so the fallback snaps in the same 9 steps as the
             native steps(9, end) path */
          rail.style.setProperty("--p",
            (Math.floor(Math.min(p, 0.9999) * 9) / 9).toFixed(4));
          if (railN) railN.textContent = (n < 10 ? "0" : "") + n;
          rail.classList.toggle("rail-top", p > 0.9);
          railTicking = false;
        });
      };
      window.addEventListener("scroll", onRail, { passive: true });
      onRail();
    }
  }

  /* nav state: mark the current section (homepage) or the current page.
     data-spy links observe their section; path links match the URL. */
  var here = window.location.pathname.replace(/index\.html$/, "");
  document.querySelectorAll(".head-nav a[href^='/']").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href.length > 1 && href.indexOf("#") === -1 && here.indexOf(href) === 0) {
      a.setAttribute("aria-current", "true");
    }
  });

  var spyLinks = document.querySelectorAll(".head-nav a[data-spy]");
  if (spyLinks.length && "IntersectionObserver" in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        spyLinks.forEach(function (a) {
          a.setAttribute("aria-current",
            a.getAttribute("data-spy") === e.target.id ? "true" : "false");
        });
      });
    }, { rootMargin: "-30% 0px -55% 0px" });
    ["services", "method", "proof"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) spy.observe(el);
    });
  }

  /* header hairline after 24px of scroll */
  var head = document.querySelector(".site-head");
  if (head) {
    var ticking = false;
    var onScroll = function () {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(function () {
          head.classList.toggle("scrolled", window.scrollY > 24);
          ticking = false;
        });
      }
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }
})();
