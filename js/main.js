/* MINARANK — hero orchestration + scroll reveals. Zero dependencies.
   The finished page is the CSS default; this file only adds the choreography.
   If it never runs, the site still looks complete. */
(function () {
  "use strict";

  var docEl = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  /* QA hook: ?static renders the finished page with zero choreography —
     identical to the no-JS experience. */
  if (/[?&]static\b/.test(window.location.search)) reduce = true;

  if (!reduce) {
    /* .js arms the start-states, .play fires the sequence. Armed and fired
       in the same script so a failed load can never strand a hidden hero. */
    docEl.classList.add("js");

    var played = false;
    var play = function () {
      if (played) return;
      played = true;
      requestAnimationFrame(function () { docEl.classList.add("play"); });
    };
    /* wait for the display font so letters never morph mid-rise; 800ms cap */
    var cap = setTimeout(play, 800);
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(function () { clearTimeout(cap); play(); });
    }

    /* scroll reveals: play once, then let go */
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
