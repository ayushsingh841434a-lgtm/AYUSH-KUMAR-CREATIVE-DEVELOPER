/* Shared behaviour for every page. No backend, no tracking.
   All controls do what they say; nothing pretends to send data. */
(function () {
  var S = window.SITE || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* Local clock (no timezone label, matching the reference presentation) */
  function tick() {
    var el = $(".clock"); if (!el) return;
    var d = new Date();
    var time = d.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" }).toLowerCase();
    var date = d.toLocaleDateString([], { day: "numeric", month: "long", year: "numeric" });
    el.textContent = "Local time " + time + " · " + date;
  }
  tick(); setInterval(tick, 30000);

  /* Dark mode via the pull cord — real toggle, remembered locally */
  var cord = $("#cordBtn");
  if (localStorage.getItem("ayush-dark") === "1") document.body.classList.add("dark");
  if (cord) cord.addEventListener("click", function () {
    var on = document.body.classList.toggle("dark");
    localStorage.setItem("ayush-dark", on ? "1" : "0");
    cord.setAttribute("aria-pressed", on ? "true" : "false");
  });

  /* Dialog helpers */
  function openDlg(id) { var d = document.getElementById(id); if (d && d.showModal) d.showModal(); }
  function closeDlg(btn) { var d = btn.closest("dialog"); if (d) d.close(); }
  $$("[data-open]").forEach(function (b) {
    b.addEventListener("click", function () { openDlg(b.getAttribute("data-open")); });
  });
  $$("dialog [data-close]").forEach(function (b) {
    b.addEventListener("click", function () { closeDlg(b); });
  });
  $$("dialog").forEach(function (d) {
    d.addEventListener("click", function (e) { if (e.target === d) d.close(); });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var dlg = $("dialog[open]");
    if (dlg) { e.preventDefault(); dlg.close(); }
  });

  /* Menu navigation: buttons that go to real pages/sections */
  $$("[data-goto]").forEach(function (b) {
    b.addEventListener("click", function () {
      var dest = b.getAttribute("data-goto");
      var dlg = b.closest("dialog"); if (dlg) dlg.close();
      if (dest === "contact") { openDlg("contactDlg"); return; }
      if (dest === "work") { window.location.href = window.__ROOT__ + "index.html#work"; return; }
      if (dest === "home") { window.location.href = window.__ROOT__ + "index.html#home"; return; }
      if (dest === "story") { window.location.href = window.__ROOT__ + "index.html#my-story"; return; }
      window.location.href = window.__ROOT__ + dest;
    });
  });

  /* Back to top — real scroll to the top of the current page */
  $$("[data-top]").forEach(function (b) {
    b.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });

  /* Footer social links from content.js */
  $$("[data-social]").forEach(function (a) {
    var key = a.getAttribute("data-social");
    if (S.social && S.social[key]) a.href = S.social[key];
  });

  /* Hero role flip — cycles the five real category names, with number */
  var flip = $("#roleFlip");
  if (flip && S.roleWords) {
    var i = 0, roleEl = $(".flip-role", flip), numEl = $(".flip-num", flip);
    setInterval(function () {
      i = (i + 1) % S.roleWords.length;
      if (roleEl) roleEl.textContent = S.roleWords[i];
      if (numEl) numEl.textContent = "0" + (i + 1) + " / 05";
      if (!roleEl) flip.textContent = S.roleWords[i] + " 0" + (i + 1) + "/05";
    }, 2200);
  }

  /* Ability card: drag to rotate between front and back */
  var abilityCard = $("#abilityCard");
  if (abilityCard) {
    var dragging = false, startX = 0, angle = 0;
    abilityCard.addEventListener("pointerdown", function (e) { dragging = true; startX = e.clientX; abilityCard.setPointerCapture(e.pointerId); });
    abilityCard.addEventListener("pointermove", function (e) {
      if (!dragging) return;
      angle = Math.max(-180, Math.min(180, (e.clientX - startX) * 0.6));
      abilityCard.style.transform = "rotateY(" + angle + "deg)";
    });
    ["pointerup", "pointercancel"].forEach(function (t) {
      abilityCard.addEventListener(t, function () {
        dragging = false;
        angle = Math.abs(angle) > 90 ? 180 : 0;
        abilityCard.style.transform = "rotateY(" + angle + "deg)";
      });
    });
  }

  /* Doors: hover dim + cursor tooltip + ajar + left-hinge open */
  var wall = $("#doorWall");
  if (wall) {
    var tip = $("#doorTip"), previewTitle = $("#doorPreviewTitle"), previewText = $("#doorPreviewText");
    var doors = $$(".door", wall);
    var info = {
      web: ["Web Development", "Websites & tools", ["Websites", "Web apps", "Landing pages", "Dashboards"]],
      app: ["App Development", "Apps & games", ["iOS apps", "Android apps", "App UI", "Prototypes"]],
      uiux: ["UI/UX Design", "Interfaces", ["Research", "Wireframes", "Prototypes", "Design systems"]],
      graphic: ["Graphic Design", "Brand visuals", ["Logos", "Posters", "Campaigns", "Brand visuals"]],
      photo: ["Photography", "Photography", ["Portraits", "Architecture", "Events", "Products"]]
    };
    function setPreview(key) {
      if (!previewTitle) return;
      previewTitle.textContent = info[key][0];
      var sub = $("#doorPreviewSub"); if (sub) sub.textContent = info[key][1];
      var list = $("#doorPreviewList");
      if (list) list.innerHTML = info[key][2].map(function (x) { return "<li>" + x + "</li>"; }).join("");
      if (previewText) previewText.textContent = "";
    }
    doors.forEach(function (d) {
      var key = d.getAttribute("data-door");
      d.addEventListener("mouseenter", function () {
        wall.classList.add("dim"); d.classList.add("active"); setPreview(key);
      });
      d.addEventListener("mouseleave", function () {
        wall.classList.remove("dim"); d.classList.remove("active");
        if (tip) tip.classList.remove("show");
      });
      d.addEventListener("mousemove", function (e) {
        if (!tip) return;
        tip.style.left = e.clientX + "px"; tip.style.top = e.clientY + "px";
        tip.classList.add("show");
      });
      d.addEventListener("click", function () {
        d.classList.add("opening");
        var trans = $("#transition"); if (trans) trans.classList.add("on");
        setTimeout(function () {
          window.location.href = d.getAttribute("data-href");
        }, 950);
      });
    });
    /* Keyboard: Enter/Space on a focused door also opens it (native button behaviour) */
  }

  /* Back to the doors: white fade, then home work section */
  $$("[data-back]").forEach(function (b) {
    b.addEventListener("click", function () {
      var trans = $("#transition"); if (trans) trans.classList.add("on");
      setTimeout(function () { window.location.href = window.__ROOT__ + "index.html#work"; }, 450);
    });
  });

  /* Contact form — honest: validates, then either opens mailto (if an
     email is configured in content.js) or says plainly that sending is
     not connected yet. It never fakes a sent message. */
  var form = $("#contactForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = $("#formNote");
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var data = new FormData(form);
      if (S.CONTACT_EMAIL) {
        var subject = encodeURIComponent("Portfolio enquiry from " + data.get("name"));
        var body = encodeURIComponent(data.get("message") + "\n\n— " + data.get("name") + " (" + data.get("email") + ", " + data.get("phone") + ")");
        window.location.href = "mailto:" + S.CONTACT_EMAIL + "?subject=" + subject + "&body=" + body;
        if (note) note.textContent = "Opening your email app to send this message.";
      } else {
        if (note) note.textContent = "Message checked, but sending is not connected yet: no contact email has been provided. Add CONTACT_EMAIL in content.js, or reach Ayush via GitHub / LinkedIn in the footer.";
      }
    });
  }

  /* Photography wall: drag, wheel, and arrow-key panning over empty slots.
     Enter on a focused slot reports honestly that no photograph is added yet. */
  var wallEl = $("#photoWall");
  if (wallEl) {
    var inner = $("#wallInner"), x = -300, y = -200, dragging = false, sx = 0, sy = 0;
    var pressedSlot = null, pointerStartX = 0, pointerStartY = 0;
    function apply() { inner.style.transform = "translate(" + x + "px," + y + "px)"; }
    function clamp() {
      x = Math.max(-1600, Math.min(0, x)); y = Math.max(-1000, Math.min(0, y));
    }
    apply();
    wallEl.addEventListener("pointerdown", function (e) {
      dragging = true; sx = e.clientX - x; sy = e.clientY - y;
      pressedSlot = e.target.closest(".photo-slot");
      pointerStartX = e.clientX; pointerStartY = e.clientY;
      wallEl.setPointerCapture(e.pointerId);
    });
    wallEl.addEventListener("pointermove", function (e) {
      if (!dragging) return;
      if (pressedSlot && (Math.abs(e.clientX - pointerStartX) > 4 || Math.abs(e.clientY - pointerStartY) > 4)) pressedSlot = null;
      x = e.clientX - sx; y = e.clientY - sy; clamp(); apply();
    });
    ["pointerup", "pointercancel"].forEach(function (t) {
      wallEl.addEventListener(t, function () {
        if (t === "pointerup" && pressedSlot) {
          var hint = $("#wallHint");
          if (hint) hint.textContent = "No photograph added to this slot yet — add photos in content.js when ready.";
        }
        dragging = false; pressedSlot = null;
      });
    });
    wallEl.addEventListener("wheel", function (e) { e.preventDefault(); x -= e.deltaX; y -= e.deltaY; clamp(); apply(); }, { passive: false });
    wallEl.setAttribute("tabindex", "0");
    wallEl.addEventListener("keydown", function (e) {
      var step = 80;
      if (e.key === "ArrowLeft") x += step; else if (e.key === "ArrowRight") x -= step;
      else if (e.key === "ArrowUp") y += step; else if (e.key === "ArrowDown") y -= step;
      else return;
      e.preventDefault(); clamp(); apply();
    });
    $$(".photo-slot", wallEl).forEach(function (s) {
      s.setAttribute("tabindex", "0");
      s.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
          var hint = $("#wallHint");
          if (hint) hint.textContent = "No photograph added to this slot yet — add photos in content.js when ready.";
        }
      });
      s.addEventListener("click", function () {
        var hint = $("#wallHint");
        if (hint) hint.textContent = "No photograph added to this slot yet — add photos in content.js when ready.";
      });
    });
  }

  /* Preloader: counter, then fade. Only present on the home page. */
  var pre = $("#preloader");
  if (pre) {
    var countEl = $("#preCount"), n = 1;
    var iv = setInterval(function () {
      n += 7; if (n >= 100) { n = 100; clearInterval(iv); setTimeout(function () { pre.classList.add("done"); }, 250); }
      if (countEl) countEl.textContent = String(n).padStart(3, "0");
    }, 90);
    setTimeout(function () { pre.classList.add("done"); }, 3000);
  }
})();
