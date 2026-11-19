# Final Audit — Ayush Kumar Portfolio vs. Reference (3 Nov 2026)

## Addendum 3 — real personal data round, same day (12:27 IST task)

Design and functionality were NOT redesigned in this round; the only
changes are real data replacing placeholders, verified in the files:

- Ability card now lists your eight technologies (HTML, CSS,
  JavaScript, C, C++, SQL, Git, GitHub) tagged "Worked with / studied"
  and DSA using Java tagged "Currently learning". No percentages,
  scores, certifications, or years of experience were added.
- Web Development page now shows your five real projects (JAN AWAAZ,
  BREAK THE INTERNET, AIMT COLLEGE, EXAM DESK, TVESE AI) with GitHub
  and live links, each live link verified HTTP 200 on 3 Nov 2026.
  Descriptions come only from your supplied BREAK THE INTERNET concept
  or from the projects' GitHub descriptions; EXAM DESK and TVESE AI
  have no published description, so those fields are explicitly left
  editable instead of invented.
- Hero now states your six interests as interests, not experience.
- Footer now names Vercel (projects) and Render (databases) exactly
  as provided, with no Render URL claimed.
- Story, contact, and the other four category galleries keep neutral
  placeholders: no email, college, degree, year, employment,
  internship, certification, award, client, or statistic was invented.
- Full per-item evidence is in `DATA_AUDIT.md` (the Personal Data
  Implementation Audit). This file remains the Original Website
  Replication Audit; its earlier findings and CLOSE MATCH status are
  unchanged by the data round.

## Addendum 2 — strict replication pass, same day (11:09–11:15 IST)

A third live inspection (desktop, public visitor, nothing submitted,
cord not pulled) settled the remaining structure questions and drove
this round of fixes:

- **Photography confirmed as a dark floating drag wall, not a filter
  grid.** No filter pills were found, so none were added. The wall
  keeps drag/wheel/arrow-key movement, with a bottom-centre "Drag in
  any direction" pill, a top-left Back pill, and a top-right
  "Photography" pill.
- **Graphic confirmed as a numbered walk-the-line sequence (01–05).**
  Groups now use the observed colours — 01 dark charcoal, 02 pale
  warm off-white, 03 dusty mauve/pink, 05 near-black; 04's colour was
  not separately confirmed, so it uses a neutral warm grey and is
  marked as unconfirmed here. Slots hang from a dashed line by tan
  pegs, are slightly tilted with white borders, and a "Scroll →"
  indicator is present. True vertical-scroll-driven horizontal
  movement is NOT reproduced: strips scroll horizontally, which is
  the same content movement with a different input mechanism.
- **Project cards alternate sides** (text left / mockup right, then
  mockup left / text right), with a mono category line, bold title,
  subtitle, description, outline tag pills, and a note line; Web and
  UI/UX use tilted desktop monitors with stands, App uses a tilted
  phone with a dark screen. Cards are neutral, editable placeholders
  marked as not real projects.
- **Story is a two-column timeline:** sticky left (about 40%) with a
  large year numeral, period label, counter, and progress line; right
  side is a dot-marked vertical timeline with period, title,
  secondary line, and dash bullets. The single placeholder entry and
  counter "01 / 01" claim nothing.
- **Ability card is a draggable 3D trading card** overlaid on the
  lower-left of the hero portrait, opening a full-screen dark dialog
  with a Close pill at top-right, a gold-bordered mauve front with
  portrait and cream stats panel, and a black/gold reverse. Stats are
  four skill-group rows with empty dot meters and "—" scores — no
  scores invented.
- **Contact title corrected to "Tell me what you need built."** with
  a "• Hire me" label, uppercase NAME / EMAIL / PHONE /
  WHAT DO YOU NEED? labels, Send message at bottom-right, and a
  reply-time note at bottom-left. Earlier visits reported two other
  titles ("Let's build something.", "Let's work together."); the
  newest, most specific inspection was followed and the conflict is
  recorded here.
- **Hero flip card** is now a cream spiral-style card with the role
  number at bottom-right ("01 / 05" … "05 / 05"); the bottom strip
  uses vertical dividers; Hire me is a solid black pill with an
  arrow; See my work is an outline pill.
- **Top bar** now reads brand left, centred pill nav, local-time pill
  right, with the dark-mode cord hanging from the top-right edge as
  a beige twisted cord with a brown wooden teardrop pull and gold
  cap, overlaying the page.
- **Door hover checklist** now appears as a titled panel with a mono
  sub-line and ticked list (matching the inspected content), above
  the door row rather than to the right of the hovered door — that
  position difference remains and is stated here.
- **Back controls:** light floating pill at bottom-left on Web/App/
  UI/UX/Graphic, top-left on Photography, plus a black circular
  back-to-top button at bottom-right on all pages. Back-to-top now
  scrolls the current page instead of jumping home.
- **Menu dialog at desktop was NOT found** on the reference at
  1919px — it shows inline navigation instead. The menu dialog in
  this build is therefore treated as the narrow-viewport control
  (full-screen dark, brand + Close at top, numbered items, local
  time + Hire me row), not a desktop feature.

Retest after this round: **61/61 passed** (1440px + 390px, zero
console errors), plus visual verification of home, ability card,
story, Web, Graphic, and Photography screenshots in `screenshots/`
(v2-* files).

Remaining honest differences after this round: content is
placeholder by instruction (no real projects, skills, timeline, or
photographs yet); Graphic vertical-scroll-driven horizontal walk is
approximated by horizontal strips; door checklist position is above
the row, not to the right of the door; animation timings and
intermediate breakpoints are close choices; Graphic section 04's
colour and the desktop menu dialog could not be verified on the
reference; reference screenshots could not be exported from this
machine, so comparison is token- and structure-based plus own-site
screenshots, not a pixel-diff pair. Status remains **CLOSE MATCH**.

## Addendum — live recheck, same day (10:33–10:38 IST)

A second live recheck of the reference (public visitor, no sign-in, no
form submitted, no dark-mode toggle) arrived after the first audit and
found five further differences, all fixed here and retested:

1. **Footer was beige; the reference footer is black.** Fixed: black
   footer with light text, CTA, Work / Navigate / Status columns, and
   Back to top (see `screenshots/footer-black.png`).
2. **Back control position.** On the reference, Back to the doors is a
   floating pill at bottom-left on Web/App/UI/UX/Graphic, and top-left
   only on Photography. Fixed to match, per page.
3. **Wide-width navigation.** At ~1920px the reference shows a centred
   pill nav and no Menu button; the Menu button appears only at
   narrower widths. Fixed: pill nav at ≥1024px, Menu button below that;
   menu dialog still available at all widths.
4. **Menu order.** Reference order is Home, Web, App, UI/UX, Graphic,
   My story, Contact (Photography omitted there). Fixed to that order,
   with Photography kept as item 08 for completeness, plus a local-time
   and Hire me row in the dialog.
5. **Door handles and hero roles.** Handles are now brass-toned
   (reference: gold nameplates/handles/keyholes), and the hero role
   card now shows the role number, e.g. "Web Developer 01/05".
6. **Preloader corners.** Added the name (top-left) and role list
   (top-right) around the counter, as on the reference.

Conflicts between the two live observations, kept as-is and disclosed:
the first visit put Back to the doors at top-left on all categories,
the recheck puts it bottom-left on four of them — the recheck (newer,
all five pages) was followed. The first visit also described doors as
slightly ajar on hover, the recheck as closed on hover with a centre
checklist overlay — the hover-ajar behaviour was kept, since it was
directly observed in the first visit and the checklist preview already
appears above the door row here. The contact-dialog title also differs
between visits ("Let's build something." vs "Let's work together."),
so the existing title was kept rather than chasing one observation.

Retest after these fixes: **61/61 passed** (the earlier 60 checks plus
the new pill-nav check), 1440px + 390px, zero console errors.

## How this audit was actually done (no claimed test is untested)

- **Reference:** inspected in the Muse live browser in Phase 1 and again
  in this audit, plus public source inspection of the reference homepage
  via its own served HTML/CSS (font, colour tokens, door geometry and
  colours below were read from that public page, not guessed). The VM's
  headless browser cannot reach the public internet (its proxy tunnel
  fails for external hosts, while the Muse browser and curl reach the
  site normally), so **no reference screenshot file could be exported
  from this VM** — that is a disclosed limitation, not a hidden gap.
  Reference screenshots therefore cannot be attached; reference facts
  below are from live-browser observation + public source tokens.
- **Own site:** tested in headless Chromium on this VM at 1440px and
  390px, with real clicks, hovers, drags, keyboard input, and console
  capture. Screenshots in `screenshots/` are from that run.
- **Identity/content guardrail:** no original owner's biography, projects,
  artwork, photographs, or achievements are used anywhere. Category,
  story, and skill areas stay empty until Ayush provides his own work.
  No email was invented.

## Reference tokens now matched (measured, not estimated)

- Font: **Onest** (self-hosted woff2, SIL OFL, in `fonts/`), weight
  100–900 in the reference; this build ships 400/700/900.
- Background **#E8E4E0**, ink **#1A1818**, muted **#857878**,
  line **#D5CDCA**, surface **#DED8D4**.
- Doors section wall **#DAD4CF** → **#E4DFDB**, floor tones
  **#C2AE98 / #A8937E** (used as a section gradient here).
- Door colours (light): Web **#22304a**, App **#4a3540**,
  UI/UX **#7a8670**, Graphic **#a4552c**, Photographer **#262523**.
- Door geometry: aspect ratio **1 / 2.25**, arched top
  (border-radius 50% of width), max width about 17.5rem. This build:
  250px × 563px at 1440px, 180px × 405px at 390px — verified in-browser.
- Door behaviour: hover fades other doors to faint outlines
  (reference: opacity 0.03 + desaturation for non-hovered doors),
  a "Click to enter" cursor badge, left-hinge swing, white interior,
  then the category page. This build reproduces that sequence with
  CSS 3D + a white fade (timings are close choices, not measured
  originals — see Minor).
- Breakpoints observed in the reference stylesheet include
  1920 / 1440 / 1024 / 640px and a mobile doors treatment under
  ~640px. This build uses 900px / 560px breakpoints as practical
  equivalents (see Minor).

## Difference report

### CRITICAL — none remaining

No missing, broken, or non-functional element was found in the final
retest. All five doors, all five routes (by door and by direct URL),
menu, contact dialog, dark-mode cord, back-to-top, and the photo wall
work. No console errors, no 404s for site assets, no broken images.

### MAJOR — fixed in this audit, then re-verified

1. **Door colours were wrong.** App was bright purple and UI/UX was
   strong green; the reference uses muted plum and sage. Fixed to the
   exact tokens above. Verified: Web computed colour
   rgb(34, 48, 74) = #22304a.
2. **Doors were short rectangles.** Reference doors are tall and
   arched (1 / 2.25). Fixed: aspect ratio + arched top + panel outline.
3. **Door labels were invisible at the arch.** White label text sat
   over the white interior where the arch curves in. Fixed: label
   padding moved below the arch curve; verified visually — "Web
   Development" is now fully readable on hover.
4. **Dimmed doors looked like pastel fills.** Reference fades others
   to faint outlines. Fixed: non-hovered doors become transparent
   with a coloured outline in the dim state.
5. **Fake-looking placeholder project cards** on Web/App/UI-UX pages
   (titled "Project title") could be mistaken for invented work.
   Fixed: removed; each page now has one honest empty-state panel
   describing its structure, with no placeholder projects.
6. **Top bar blurred text behind it** (translucent backdrop blur).
   Fixed: solid background.
7. **Portrait double-darkened** (treated image + CSS brightness 0.88).
   Fixed: CSS now only grayscales; the treated image carries the
   dark tone. Face, hairstyle, and features untouched throughout.

### MAJOR — remaining by design / by instruction (not bugs)

8. **Content is empty.** By your instruction, no projects, skills,
   timeline, or photographs are invented. Category pages therefore
   cannot visually match the reference's filled project galleries
   until you provide content. This is intentional, and the structures
   are ready for it in `content.js`.
9. **Hero portrait is rectangular, not cut-out.** The reference hero
   uses a cut-out portrait anchored on a hairline; your photograph is
   a rectangular sitting portrait, and cutting it out would alter the
   image. It is presented as a dark monochrome rectangle, matching
   the reference's tonal treatment instead.
10. **Doors mechanism differs in detail.** Reference desktop doors are
    a 4-column grid with the fifth door "secret" past the end and the
    wall sliding to reveal it; on mobile the wall is pinned and scroll
    walks along it. This build uses a horizontally scrollable row in
    both cases: 4 doors fit at 1440px, the fifth is off-screen and is
    reached by scrolling the row. The user-visible outcome (fifth door
    hidden until revealed, same order/colours/hover/open) matches;
    the internal mechanism does not.
11. **Category pages open as separate documents, not as a fixed
    full-screen overlay** over the home page. The reference opens
    category content through a door into a full-screen view with a
    "Back to the doors" control; this build navigates to the category
    folder and its "Back to the doors" returns to the door wall.
    Navigation outcome and return behaviour match; the overlay
    implementation does not.

### MINOR — remaining

- Animation durations/easings are close choices (hover 0.35s, open
  0.9s, fade 0.45s), not measured reference values; the reference's
  exact timings were not measurable with the tools available.
- Breakpoints differ (900/560 vs. reference 1024/640 family); layout
  outcomes at 1440px and 390px were verified, intermediate widths
  were not exhaustively compared.
- Menu includes Photography as item 08. The reference menu as
  observed listed seven items and omitted Photography (reachable by
  door/footer). Including it is a deliberate completeness fix.
- Scroll routing uses anchors (#work, #my-story) plus Netlify
  redirects for /home, /work, /my-story; the reference changes the
  path as sections come into view. On a plain static server, the
  anchor version is the one that works without a server rewrite.
- No analytics consent banner (reference asks for Google Analytics
  consent). This build ships no tracking by default.
- No legal page content (reference footer links to one whose content
  was not inspected); this build notes it as "add when ready" rather
  than inventing legal text.
- Reference screenshots could not be exported (see "How this audit
  was done"). Side-by-side comparison is therefore textual +
  token-based + own-site screenshots, not a pixel-diff image pair.

## Final test results (after fixes, re-run in full)

- **Total checks:** 60 (30 at 1440px + 30 at 390px)
- **Passed:** 60
- **Failed:** 0
- **Not performed:** reference screenshot export (VM cannot browse
  the public internet directly); reference animation-timing measurement;
  contact-form sending (no email provided, by design — the form
  honestly reports that sending is not connected); graphic lightbox
  and photography Enter-to-enlarge (no artwork/photographs provided
  yet, so there is nothing to enlarge).

Checks covered: home load + preloader, exactly 5 doors, door geometry
and colours, hero name + portrait load, GitHub/LinkedIn links, absence
of the original owner's name/text, every door click → correct route,
every Back-to-doors → #work, menu open (8 items), contact open,
back-to-top, all five direct routes, no console errors, mobile
390px door count and stacked hero.

## Final status

**CLOSE MATCH** — not EXACT MATCH, and not NOT READY.

The site is functionally complete, tested 60/60, and now matches the
reference on the measurable visual facts that matter most: Onest type,
#E8E4E0 / #1A1818 palette, exact door colours, tall arched door
geometry, hover-to-outline + click-to-enter + left-hinge open + white
fade, five working routes with Back to the doors, and Ayush's own
dark monochrome portrait with his GitHub/LinkedIn identity.

It is not an exact match because content is intentionally empty,
because the doors' internal grid/slide mechanism and the category
overlay implementation differ from the reference's, because animation
timings and intermediate breakpoints are close choices rather than
measured originals, and because reference screenshots could not be
exported for a pixel comparison. Those are stated limits, not hidden
ones. No "100% complete" or "perfect" claim is made.
