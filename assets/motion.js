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
      n.textContent = data[i][0]; dv.textContent = data[i][1]; sb.textContent = data[i][2]; ln.setAttribute("href", petals[i].getAttribute("href"));
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

/* Ashtalakshmi Stotram page: scroll journey with a moving diya, and the read-one-stanza-a-day planner */
(function () {
  var d = document, calm = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var jp = d.getElementById("jpath");
  if (jp && !calm) {
    var tk = false;
    var upd = function () {
      tk = false;
      var r = jp.getBoundingClientRect(), vh = window.innerHeight;
      var lp = Math.max(0, Math.min(1, (vh * 0.55 - r.top) / r.height));
      jp.style.setProperty("--lp", lp.toFixed(3));
      var nodes = jp.querySelectorAll(".jn"), h = vh * 0.55;
      for (var i = 0; i < nodes.length; i++) { var t = nodes[i].getBoundingClientRect().top; nodes[i].classList.toggle("lit", t < h); }
    };
    addEventListener("scroll", function () { if (!tk) { tk = true; requestAnimationFrame(upd); } }, { passive: true });
    addEventListener("resize", upd); upd();
  } else if (jp) { jp.style.setProperty("--lp", "1"); [].forEach.call(jp.querySelectorAll(".jn"), function (n) { n.classList.add("lit"); }); }

  var list = d.getElementById("pdays"), bar = d.getElementById("plan-bar");
  if (list && bar) {
    var KEY = "lakshmistuti_stotram_plan", st = { start: null, done: [] };
    try { var raw = localStorage.getItem(KEY); if (raw) st = JSON.parse(raw) || st; } catch (e) {}
    var save = function () { try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) {} };
    var items = [].slice.call(list.querySelectorAll("li"));
    var msg = d.getElementById("plan-msg"), go = d.getElementById("plan-start"), rs = d.getElementById("plan-reset");
    bar.hidden = false;
    items.forEach(function (li, i) {
      var cb = d.createElement("input"); cb.type = "checkbox"; cb.className = "pchk"; cb.setAttribute("aria-label", "Mark day " + (i + 1) + " as read");
      cb.addEventListener("change", function () {
        var k = st.done.indexOf(i); if (cb.checked && k < 0) st.done.push(i); if (!cb.checked && k >= 0) st.done.splice(k, 1); save(); paint();
      });
      li.insertBefore(cb, li.firstChild);
    });
    var today = function () {
      if (!st.start) return -1;
      var a = new Date(st.start), b = new Date(); a.setHours(0, 0, 0, 0); b.setHours(0, 0, 0, 0);
      return Math.round((b - a) / 864e5);
    };
    function paint() {
      var t = today();
      items.forEach(function (li, i) {
        var on = st.done.indexOf(i) >= 0;
        li.classList.toggle("done", on); li.querySelector(".pchk").checked = on; li.classList.toggle("now", t === i);
      });
      var n = st.done.length;
      if (!st.start) msg.textContent = "Tick each day as you read it, or press Start today to follow along.";
      else if (t > 7) msg.textContent = n + " of 8 days read. The eight days are over; read any stanza again whenever you like.";
      else if (t >= 0) msg.textContent = "Today is Day " + (t + 1) + ". " + n + " of 8 read.";
      go.hidden = !!st.start; rs.hidden = !st.start && n === 0;
    }
    go.addEventListener("click", function () { st.start = new Date().toISOString(); save(); paint(); });
    rs.addEventListener("click", function () { st = { start: null, done: [] }; save(); paint(); });
    paint();
  }
})();

/* Yantra layered build, and glossary search */
(function () {
  var d = document;
  var cards = [].slice.call(d.querySelectorAll(".ylc")), layers = [].slice.call(d.querySelectorAll(".ys-svg .yl")), cap = d.getElementById("ycap");
  if (cards.length && layers.length && "IntersectionObserver" in window) {
    var names = ["Enclosure", "Circle", "Lotus petals", "Triangles", "Central point"];
    var show = function (n) {
      layers.forEach(function (g, i) { g.classList.toggle("on", i < n); g.classList.toggle("cur", i === n - 1); });
      cards.forEach(function (c, i) { c.classList.toggle("cur", i === n - 1); });
      if (cap) cap.textContent = "Layer " + n + " of " + cards.length + ": " + (names[n - 1] || "");
    };
    show(1);
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) show(+e.target.getAttribute("data-l")); });
    }, { rootMargin: "-40% 0px -45% 0px" });
    cards.forEach(function (c) { io.observe(c); });
  }
  var gl = d.getElementById("gl"), q = d.getElementById("gq");
  if (gl && q) {
    d.getElementById("gsearch").hidden = false;
    var items = [].slice.call(gl.querySelectorAll(".gi")), cnt = d.getElementById("gcount"), none = d.getElementById("gnone");
    var norm = function (t) { return t.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); };
    items.forEach(function (it) { it._n = norm(it.getAttribute("data-q") || ""); });
    var run = function () {
      var v = norm(q.value.trim()), shown = 0;
      items.forEach(function (it) { var ok = !v || it._n.indexOf(v) >= 0; it.hidden = !ok; if (ok) shown++; });
      cnt.textContent = v ? shown + " of " + items.length + " words" : items.length + " words";
      none.hidden = shown > 0;
    };
    q.addEventListener("input", run); run();
  }
})();
