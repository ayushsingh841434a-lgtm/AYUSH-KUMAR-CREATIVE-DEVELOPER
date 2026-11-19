#!/usr/bin/env python3
"""Generate the five category pages from one shared template.
Run from ayush-portfolio/: python3 tools/gen_categories.py
The Web page includes Ayush's supplied projects; other category content stays
placeholder-only until real content is provided in content.js."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

COMMON_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Ayush Kumar</title>
<meta name="description" content="{desc}">
<link rel="icon" href="../favicon.ico">
<link rel="stylesheet" href="../styles.css">
<script>window.__ROOT__ = "../";</script>
<script src="../content.js" defer></script>
<script src="../app.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div id="transition" aria-hidden="true"></div>
<header class="topbar">
  <span class="brand">Ayush Kumar</span>
  <nav class="pillnav" aria-label="Primary">
    <a href="../index.html#home">Home</a>
    <a href="../web-developer/index.html">Web</a>
    <a href="../app-developer/index.html">App</a>
    <a href="../ui-ux-designer/index.html">UI/UX</a>
    <a href="../graphic-designer/index.html">Graphic</a>
    <a href="../index.html#my-story">My story</a>
    <button data-open="contactDlg">Contact</button>
  </nav>
  <div class="right">
    <span class="clock pill">Local time</span>
    <button class="pill menu-btn" data-open="menuDlg">Menu</button>
    <button class="cord" id="cordBtn" aria-label="Toggle dark mode" aria-pressed="false"><span class="wire"></span><span class="knob"></span><small>Dark mode (pull the cord)</small></button>
  </div>
</header>
<main class="wrap" id="main">
  <div class="backbar">
    {backbar}
    <span class="pill">{pill}</span>
  </div>
  <section class="cat-head">
    <h1>{h1}</h1>
    <p>{intro}</p>
  </section>
"""

COMMON_FOOT = """
</main>
{backfloat}
<footer class="wrap">
  <h2>Need something built? Let's make it happen.</h2>
  <p>Available for freelance work across websites, apps, interfaces, and visual content.</p>
  <div class="cta">
    <button class="btn" data-open="contactDlg">Hire me</button>
    <button class="btn secondary" data-back>Back to the doors</button>
  </div>
  <div class="foot-grid">
    <div><h3>Work</h3>
      <a href="../web-developer/index.html">Web Development</a>
      <a href="../app-developer/index.html">App Development</a>
      <a href="../ui-ux-designer/index.html">UI/UX Design</a>
      <a href="../graphic-designer/index.html">Graphic Design</a>
      <a href="../photographer/index.html">Photography</a>
    </div>
    <div><h3>Navigate</h3>
      <a href="../index.html#home">Home</a>
      <a href="../index.html#my-story">My story</a>
      <button class="pill" data-open="contactDlg">Contact</button>
    </div>
    <div><h3>Status</h3><p>Available for new work<br>Remote-first, worldwide<br>Deployments: Vercel for projects · Render for databases<br><small>Individual live links are shown only where verified.</small></p></div>
    <div><h3>Connect</h3>
      <a data-social="github" href="https://github.com/ayushsingh841434a-lgtm">GitHub</a>
      <a data-social="linkedin" href="https://www.linkedin.com/in/ayush-singh-5b2853404/">LinkedIn</a>
    </div>
  </div>
  <p class="copy">&copy; 2026 Ayush Kumar. Designed and built by Ayush Kumar. Privacy &amp; credits: add a legal page when ready. <button class="pill" data-top>Back to top &uarr;</button></p>
  <button class="back-top-circle" data-top aria-label="Back to top">&uarr;</button>
</footer>
<dialog id="menuDlg" aria-label="Menu">
  <div class="menu-head"><span>Ayush Kumar</span><button class="pill" data-close>Close</button></div>
  <h2>Menu</h2>
  <div class="cta">
    <button class="btn secondary" data-goto="home">01 Home</button>
    <button class="btn secondary" data-goto="web-developer/index.html">02 Web</button>
    <button class="btn secondary" data-goto="app-developer/index.html">03 App</button>
    <button class="btn secondary" data-goto="ui-ux-designer/index.html">04 UI/UX</button>
    <button class="btn secondary" data-goto="graphic-designer/index.html">05 Graphic</button>
    <button class="btn secondary" data-goto="story">06 My story</button>
    <button class="btn secondary" data-goto="contact">07 Contact</button>
    <button class="btn secondary" data-goto="photographer/index.html">08 Photography</button>
  </div>
  <div class="row" style="justify-content:space-between"><span class="clock">Local time</span><button class="btn" data-goto="contact">Hire me →</button></div>
</dialog>
<dialog id="contactDlg" aria-label="Contact">
  <button class="pill dlg-x" data-close aria-label="Close">Close</button>
  <p class="hire-label">• Hire me</p>
  <h2>Tell me what you need built.</h2>
  <form id="contactForm">
    <label>NAME <input name="name" placeholder="Your name" required></label>
    <label>EMAIL <input name="email" type="email" placeholder="you@company.com" required></label>
    <label>PHONE <input name="phone" placeholder="Your phone number" required></label>
    <label>WHAT DO YOU NEED? <textarea name="message" rows="4" placeholder="Describe your project — scope, timeline, budget&hellip;" required></textarea></label>
    <p class="form-note" id="formNote"></p>
    <div class="row" style="justify-content:space-between"><p class="reply-note">Reply time to be confirmed once a contact email is provided.</p><button type="submit" class="btn">Send message</button></div>
  </form>
  <p>Or connect via <a data-social="github" href="https://github.com/ayushsingh841434a-lgtm">GitHub</a> or <a data-social="linkedin" href="https://www.linkedin.com/in/ayush-singh-5b2853404/">LinkedIn</a>.</p>
</dialog>
</body>
</html>
"""

def _proj_cards(kind):
    if kind == "web":
        real = [
            ("JAN AWAAZ", "Civic-tech platform",
             "JanAwaaz is a citizen-focused civic-tech platform that helps people understand public issues, raise their voice, and find the right way forward.",
             ["TypeScript"], "https://github.com/ayushsingh841434a-lgtm/JanAwaaz", "https://jan-awaaz-beta.vercel.app"),
            ("BREAK THE INTERNET", "Educational simulator",
             "An educational infrastructure failure simulator that lets users safely break a simulated website and observe how infrastructure components fail, recover and reroute requests. Browser-based, using vanilla JavaScript, without touching real servers or requiring a backend/database for the simulation.",
             ["HTML", "CSS", "Vanilla JavaScript"], "https://github.com/ayushsingh841434a-lgtm/BREAK-THE-INTERNET-INFRASTRUCTURE-LAB", "https://brkktheint.vercel.app"),
            ("AIMT COLLEGE", "College management system",
             "College management system for AIMT with secure login, attendance, examinations, results, and role-based access.",
             ["TypeScript"], "https://github.com/ayushsingh841434a-lgtm/AIMT-College-Management-System", "https://aimt-college-management-system.vercel.app"),
            ("EXAM DESK", "Project — details to be added",
             "Description to be added: no description is published on this project's GitHub repository. The GitHub and live links below are verified; the description field is left editable rather than invented.",
             ["TypeScript"], "https://github.com/ayushsingh841434a-lgtm/EXAM-DESK", "https://exam-desk-alpha.vercel.app"),
            ("TVESE AI", "Project — details to be added",
             "Description to be added: no description is published on this project's GitHub repositories. The GitHub and live links below are verified; the description field is left editable rather than invented.",
             ["HTML"], "https://github.com/ayushsingh841434a-lgtm/TVESE-AI", "https://tvese-ai-1.vercel.app"),
        ]
        out = ['<section class="section"><h2>Projects</h2>',
               '<p class="sub">All five project names, in Web Development: each is a Vercel web deployment with a GitHub repository (verified 3 Nov 2026 — every live link below returned HTTP 200). No project is claimed to use a technology it does not, and no live link is shown for a project whose homepage could not be verified.</p>']
        for i, (name, sub, desc, tags, gh, live) in enumerate(real):
            cls = "proj-card alt" if i % 2 == 1 else "proj-card"
            tag_html = "".join(f'<span class="tag">{x}</span>' for x in tags)
            out.append(f"""<article class="{cls}"><div class="proj-text"><p class="mono">Web Development</p><h3>{name}</h3><p class="proj-sub">{sub}</p><p>{desc}</p><div class="tags">{tag_html}</div><div class="cta"><a class="btn secondary" href="{gh}">GitHub</a><a class="btn" href="{live}">Live site</a></div><p class="proj-note">Live link verified 3 Nov 2026 (HTTP 200); GitHub link from the public repository.</p></div><div class="mock monitor"><div class="screen"><span>Desktop monitor mockup — visit the live site or repository for the real project.</span></div><div class="stand"></div></div></article>""")
        out.append("</section>")
        return "\n".join(out)
    mock = "phone" if kind == "app" else "monitor"
    mock_label = "Phone mockup area — add your app screens here." if kind == "app" else "Desktop monitor mockup area — add your screen recording here."
    title = {"web": "Projects", "app": "Apps", "uiux": "Case studies"}[kind]
    cat = {"web": "Web Development", "app": "App Development", "uiux": "UI/UX Design"}[kind]
    def card(alt, n):
        cls = "proj-card alt" if alt else "proj-card"
        return f"""<article class="{cls}"><div class="proj-text"><p class="mono">{cat}</p><h3>Your project title</h3><p class="proj-sub">Your project subtitle</p><p>Editable placeholder: add your project description here in <code>projects</code> in <code>content.js</code>.</p><div class="tags"><span class="tag">Your tag</span><span class="tag">Your tag</span></div><p class="proj-note">This is a neutral placeholder, not a real project and not the original owner's work.</p></div><div class="mock {mock}"><div class="screen"><span>{mock_label}</span></div><div class="stand"></div></div></article>"""
    return f"""<section class="section"><h2>{title}</h2>
{card(False, 1)}
{card(True, 2)}</section>"""

def card_body(kind):
    return _proj_cards(kind)

PAGES = {
    "web-developer": dict(title="Web Development", desc="Five web development projects by Ayush Kumar, with project descriptions and GitHub and live-site links.",
        pill="Web Development", h1="Web Development",
        intro="Five web projects by Ayush Kumar are listed below with project descriptions, GitHub repositories, and live-site links.",
        body=card_body("web")),
    "app-developer": dict(title="App Development", desc="App development work by Ayush Kumar — apps to be added.",
        pill="App Development", h1="App Development",
        intro="App work will appear here. The app-card structure below is ready for your apps, icons, and phone recordings.",
        body=card_body("app")),
    "ui-ux-designer": dict(title="UI/UX Design", desc="UI/UX design work by Ayush Kumar — case studies to be added.",
        pill="UI/UX Design", h1="UI/UX Design",
        intro="Interface work will appear here. The case-study structure below is ready for your research, flows, and prototypes.",
        body=card_body("uiux")),
    "graphic-designer": dict(title="Graphic Design", desc="Graphic design work by Ayush Kumar — artwork to be added.",
        pill="Graphic Design", h1="Graphic Design",
        intro="Brand and campaign work will appear here. Scroll to walk each brand's line, and click a print to view it when artwork is added.",
        body="""<section class="section"><h2>Gallery</h2>
<p class="scroll-line">Scroll → <span class="progress"></span></p>
<div class="empty"><h3>No artwork added yet</h3><p>This page keeps the original scroll-line gallery structure: one line per brand group, with swipeable strips. Add artwork groups to <code>projects.graphic</code> in <code>content.js</code>.</p></div>
""" + "".join(f"""<div class="line-group g{i}"><h3>Group {i} — 0{i}</h3><div class="line"></div><div class="strip"><div class="slot">Artwork slot</div><div class="slot">Artwork slot</div><div class="slot">Artwork slot</div></div></div>""" for i in range(1, 6)) + "</section>"),
    "photographer": dict(title="Photography", desc="Photography by Ayush Kumar — photographs to be added.",
        pill="Photography", h1="Photography by Ayush",
        intro="Photographs will appear here, floating in the dark. Drag, scroll, or use arrow keys to explore the wall.",
        body="""<section class="section"><h2>Photo wall</h2>
<div class="wall" id="photoWall" aria-label="Floating photo wall — drag, scroll, or use arrow keys">
  <div class="wall-inner" id="wallInner">
    <div class="photo-slot" style="left:350px;top:240px">Photo slot 1</div>
    <div class="photo-slot" style="left:700px;top:180px">Photo slot 2</div>
    <div class="photo-slot" style="left:1050px;top:320px">Photo slot 3</div>
    <div class="photo-slot" style="left:520px;top:560px">Photo slot 4</div>
    <div class="photo-slot" style="left:900px;top:640px">Photo slot 5</div>
    <div class="photo-slot" style="left:1300px;top:560px">Photo slot 6</div>
    <div class="photo-slot" style="left:700px;top:900px">Photo slot 7</div>
    <div class="photo-slot" style="left:1150px;top:900px">Photo slot 8</div>
  </div>
  <span class="wall-hint" id="wallHint">Drag to move · Scroll · Arrow keys · Enter on a slot</span>
</div>
<div class="empty" style="margin-top:18px"><h3>No photographs added yet</h3><p>The wall, its movement, and its navigation work now with empty slots. Replace slots with your photographs in <code>projects.photo</code> when ready — no fake photographs are shown.</p></div></section>"""),
}

for slug, p in PAGES.items():
    if slug == "photographer":
        p["backbar"] = '<button class="pill" data-back>&larr; Back to the doors</button>'
        p["backfloat"] = ""
    else:
        p["backbar"] = ""
        p["backfloat"] = '<button class="pill back-float" data-back>&larr; Back to the doors</button>'
    out = ROOT / slug / "index.html"
    out.write_text(COMMON_HEAD.format(**p) + p["body"] + COMMON_FOOT.format(**p), encoding="utf-8")
    print("wrote", out)
