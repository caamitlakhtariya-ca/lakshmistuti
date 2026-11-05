/* Scroll-driven motion for the landing pages. Progressive enhancement: without JS or with reduced motion everything stays visible. */
(function () {
  var d = document, root = d.documentElement;
  var calm = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var clamp = function (x) { return Math.max(0, Math.min(1, x)); };
  var ease = function (x) { return x * x * (3 - 2 * x); };

  /* reveal on scroll */
  var rv = [].slice.call(d.querySelectorAll(".rv"));
  if (calm || !("IntersectionObserver" in window)) { rv.forEach(function (e) { e.classList.add("in"); }); }
  else {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    rv.forEach(function (e) { io.observe(e); });
  }

  /* hymn tabs */
  var tabs = [].slice.call(d.querySelectorAll(".tabs .tb")), panels = [].slice.call(d.querySelectorAll(".tpanels .tp"));
  function pick(i, focus) {
    tabs.forEach(function (t, k) { var on = k === i; t.classList.toggle("on", on); t.setAttribute("aria-selected", on); t.tabIndex = on ? 0 : -1; if (on && focus) t.focus(); });
    panels.forEach(function (p, k) { p.hidden = k !== i; });
  }
  if (tabs.length) {
    pick(0);
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { pick(i); });
      t.addEventListener("keydown", function (e) {
        if (e.key === "ArrowRight" || e.key === "ArrowLeft") { pick((i + (e.key === "ArrowRight" ? 1 : tabs.length - 1)) % tabs.length, true); e.preventDefault(); }
      });
    });
    if (location.hash === "#kanakadhara") pick(1);
  }

  if (calm) return;

  /* scroll progress: bloom hero + trail line */
  var bloom = d.querySelector(".bloom"), caps = [].slice.call(d.querySelectorAll(".caps span")), cta = d.querySelector(".bcta");
  var trail = d.querySelector(".trail"), ticking = false;
  function frame() {
    ticking = false;
    var vh = window.innerHeight;
    if (bloom) {
      var r = bloom.getBoundingClientRect(), span = r.height - vh;
      var p = clamp(-r.top / (span > 0 ? span : 1));
      bloom.style.setProperty("--p", p.toFixed(3));
      bloom.style.setProperty("--o1", ease(clamp((p - 0.04) / 0.5)).toFixed(3));
      bloom.style.setProperty("--o2", ease(clamp((p - 0.16) / 0.5)).toFixed(3));
      bloom.style.setProperty("--o3", ease(clamp((p - 0.28) / 0.5)).toFixed(3));
      var ci = p < 0.3 ? 0 : p < 0.62 ? 1 : 2;
      caps.forEach(function (c, i) { c.classList.toggle("on", i === ci); });
      if (cta) cta.classList.toggle("on", p > 0.72);
    }
    if (trail) {
      var t = trail.getBoundingClientRect();
      trail.style.setProperty("--lp", clamp((vh * 0.65 - t.top) / t.height).toFixed(3));
    }
  }
  function req() { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }
  window.addEventListener("scroll", req, { passive: true });
  window.addEventListener("resize", req);
  frame();
})();

/* Aarti page: diya, active step. Ashtalakshmi page: petal wheel. Runs even with reduced motion (no animation needed). */
(function () {
  var d = document;
  var calm = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var box = d.getElementById("diyab"), btn = d.getElementById("dbtn"), note = d.getElementById("dn");
  if (box && btn) {
    btn.addEventListener("click", function () {
      var lit = box.classList.toggle("lit");
      btn.setAttribute("aria-pressed", lit);
      btn.textContent = lit ? "Put out the diya" : "Light the diya";
      note.textContent = lit ? "The lamp is lit. Take a quiet moment of gratitude, then begin the aarti." : "Tap to light a lamp. A quiet moment before the aarti is part of the worship.";
    });
  }
  var steps = [].slice.call(d.querySelectorAll("ol.steps li"));
  if (steps.length && "IntersectionObserver" in window && !calm) {
    var so = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { steps.forEach(function (s) { s.classList.toggle("on", s === e.target); }); } });
    }, { rootMargin: "-42% 0px -48% 0px" });
    steps.forEach(function (s) { so.observe(s); });
  }
  var petals = [].slice.call(d.querySelectorAll(".awheel .ap"));
  if (petals.length) {
    var data = JSON.parse(d.getElementById("aw-data").textContent);
    var n = d.getElementById("aw-n"), dv = d.getElementById("aw-d"), sb = d.getElementById("aw-s"), ln = d.getElementById("aw-l");
    function show(i) {
      petals.forEach(function (p, k) { p.classList.toggle("sel", k === i); });
      n.textContent = data[i][0]; dv.textContent = data[i][1]; sb.textContent = data[i][2]; ln.setAttribute("href", "#f" + (i + 1));
    }
    petals.forEach(function (p, i) {
      p.addEventListener("mouseenter", function () { show(i); });
      p.addEventListener("focus", function () { show(i); });
      p.addEventListener("click", function () { show(i); });
    });
    show(0);
    var w = d.querySelector(".aw-svg");
    if (w && !w.classList.contains("in") && "IntersectionObserver" in window && !calm) {
      /* .rv already adds .in on scroll; nothing more needed */
    }
  }
})();
