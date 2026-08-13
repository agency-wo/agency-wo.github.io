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
})();
