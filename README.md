# Ayush Kumar — Portfolio

A static portfolio (HTML, CSS, vanilla JavaScript — no build step, no backend)
recreating the reference site's experience from the Phase 1 investigation:
preloader, hero with cycling roles, five coloured doors, story section,
contact dialog, footer, and five category pages with their own structures.
**No original owner's projects, artwork, photographs, biography, or copy are
used.** Category and story content areas are intentionally empty until
Ayush provides his own work.

## Quick start

```bash
cd ayush-portfolio
python3 -m http.server 8000
# open http://localhost:8000/
```

Any static server works. Opening `index.html` directly from disk also works
for the home page and category folders, except the Netlify-style aliases
below, which need a server or Netlify.

## Structure

- `index.html` — home: preloader, hero, five doors, story section, footer
- `styles.css`, `app.js` — shared styles and behaviour
- `content.js` — **the only file you normally edit**: identity, social links,
  contact email, skills, story, and project arrays (all empty by default)
- `web-developer/`, `app-developer/`, `ui-ux-designer/`, `graphic-designer/`,
  `photographer/` — one real folder per category route, so direct URLs work
- `images/ayush-portrait.jpg` — hero portrait slot (see below)
- `tools/make-portrait.py` — dark monochrome portrait converter
- `tools/gen_categories.py` — regenerates the five category pages
- `netlify.toml` — Netlify redirects for reference-style URLs

## Routes (all working)

| Route | Page |
|---|---|
| `/` → preloader → home | Hero, doors, story |
| `/web-developer/` | Web project-card structure, empty |
| `/app-developer/` | App-card structure, empty |
| `/ui-ux-designer/` | Text-led case-study structure, empty |
| `/graphic-designer/` | Scroll-line gallery structure, empty |
| `/photographer/` | Dark floating-photo wall, empty slots |
| `/home`, `/work`, `/my-story` | Netlify aliases to the home page sections |

## The five doors

Order and colours (measured from the reference): Web #22304a,
App #4a3540, UI/UX #7a8670, Graphic #a4552c, Photographer #262523.
Tall arched doors (aspect ratio 1 / 2.25, 250px × 563px at 1440px) in a
horizontally scrollable row — four fit at 1440px, the fifth is off-screen
until the row is scrolled. Hover: the hovered door goes solid, the others
fade to faint outlines, a "Click to enter" tooltip follows the cursor,
and the door sits slightly ajar. Click: the door swings open on its left
hinge, a white interior is revealed, the screen fades white, and the
category page loads. Every category page has "Back to the doors" back
to the door wall.

Font: Onest (SIL Open Font License, self-hosted in `fonts/`), matching
the reference's typeface. Background #E8E4E0, ink #1A1818.

See `AUDIT.md` for the full final audit, difference report
(CRITICAL / MAJOR / MINOR), and test results (60/60 after fixes).

## Your photograph — applied

Your photograph (uploaded 3 Nov 2026) is now the hero portrait at
`images/ayush-portrait.jpg`, converted with `tools/make-portrait.py`:
800×1000, true grayscale, darker cinematic tone, higher contrast, soft
vignette. **Face, hairstyle, and features are untouched — only colour
grading, brightness, and contrast were changed.** No fake person and no
one else's photograph is used anywhere on the site.

To replace it with a different photograph later, run:
`python3 tools/make-portrait.py your-new-photo.jpg`

## Contact email — also not invented

`CONTACT_EMAIL` in `content.js` is intentionally empty. The contact form
validates and then says plainly that sending is not connected yet, rather
than faking a sent message. Set the email you provide, and the form will
open the visitor's email app addressed to you. GitHub and LinkedIn links
in the footer and contact dialog are live:

- GitHub: https://github.com/ayushsingh841434a-lgtm
- LinkedIn: https://www.linkedin.com/in/ayush-singh-5b2853404/

## Adding your content later

Edit only `content.js` first (arrays are empty by design), then replace the
slot markup in the relevant category page with your real entries. Empty
arrays render honest empty states and never break layout or navigation.
Do not copy anyone else's projects, artwork, or photographs into these
slots — add only work you own.

## Interactions — all wired, none decorative

Preloader counter, live local clock, menu dialog, dark-mode pull cord
(persisted in localStorage), hero role flip, door hover/open, horizontal
door scrolling, category navigation, back-to-doors, back-to-top, contact
dialog + validation, ability-card dialog, graphic scroll-line strips,
photography wall (drag, wheel, arrow keys, Enter on a slot). Keyboard
focus and `prefers-reduced-motion` are handled.

## Deployment

**Netlify (recommended, matches the reference hosting pattern):**
drag the `ayush-portfolio` folder into Netlify Drop, or connect a repo
with publish directory `ayush-portfolio`. `netlify.toml` already maps
`/home`, `/work`, and `/my-story`.

**GitHub Pages / Vercel / any static host:** publish the folder as-is.
No environment variables, no database, no build command.

## Remaining differences from the reference (honest list)

1. **Photograph:** your uploaded photograph, applied in dark monochrome
   (see above). Verified visually: face and hairstyle preserved.
2. **Exact colours/fonts/timings:** the reference's exact hex values, font
   family, and animation durations could not be verified in Phase 1
   (no DevTools source access), so this build uses close, evidence-based
   approximations: beige ground, near-black text, bold sans-serif, and
   the five observed door colours. It does not claim pixel-identical
   values it cannot prove.
3. **Menu includes Photography as item 08.** The reference menu as
   observed listed seven items and omitted Photography (reachable there
   only by door/footer). Including it is a deliberate completeness fix;
   remove that one button if you want the omission reproduced exactly.
4. **Contact sending:** not connected until you provide an email (above).
5. **Legal page:** the reference footer links to a legal page whose
   content was not inspected; this build notes it as "add when ready"
   instead of inventing legal text.
6. **Mobile 390 px:** Phase 1 could not verify the reference at exactly
   390 px, so mobile layout here is a new, tested responsive choice
   (stacked hero/footer, swipeable door row), not a claimed copy.
7. **Content:** all category, story, and skill areas are empty by your
   instruction — that is intentional, not missing work.
8. **No analytics:** the reference asks for Google Analytics consent.
   This build includes no tracking at all, by default. Add it only if
   you want it, with your own consent banner.
