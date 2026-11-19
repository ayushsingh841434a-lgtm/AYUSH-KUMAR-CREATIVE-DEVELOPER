# Personal Data Implementation Audit — Ayush Kumar (3 Nov 2026)

Verification method: the actual project files in this folder were read
and searched after the data was added. GitHub data was checked against
the public GitHub API for user `ayushsingh841434a-lgtm` (repository
language and description fields), and every live homepage below was
checked by HTTP request on 3 Nov 2026 — all five returned HTTP 200.
No field below was copied from the reference owner's website.

## 1. Identity

- **Name "Ayush Kumar"** — `index.html`: page title, top-bar brand,
  hero heading ("Hi, I'm Ayush Kumar."), portrait caption, menu
  dialog brand, footer copyright, ability-card reverse face; every
  category page: top-bar brand and footer copyright.
- **Portrait** — `images/ayush-portrait.jpg` (your supplied photograph,
  dark monochrome treatment, face untouched). Used in `index.html`
  hero portrait and in the ability-card front panel.
- **GitHub** — `https://github.com/ayushsingh841434a-lgtm`:
  `index.html` footer Connect column and contact-dialog "Or connect
  via" line; every category page footer; `content.js` `social.github`.
- **LinkedIn** — `https://www.linkedin.com/in/ayush-singh-5b2853404/`:
  same places as GitHub; `content.js` `social.linkedin`.
- **Owner-name check** — searched all six site pages for the reference
  owner's name and site domain: no matches. The only percentage-like
  string in `index.html` is a layout width (`width:100%` on the story
  progress line), not a skill rating.

## 2. Skills (ability card, `index.html` — "My ability card" dialog)

Structure kept from the reference (trading-card shape, gold border,
portrait, stats panel, reverse face); content replaced with your
technologies only, and scores replaced with status tags because no
proficiency rating was provided:

- HTML, CSS, JavaScript, C, C++, SQL, Git, GitHub — each tagged
  "Worked with / studied".
- DSA using Java — tagged "Currently learning" (not presented as a
  completed skill, and with no rating, percentage, or score).
- No certifications, years of experience, or proficiency percentages
  appear anywhere. The card note states this explicitly.

The same lists live in `content.js` (`skills`, `learning`) as the
single edit point.

## 3. Projects (Web Development page, `web-developer/index.html`)

All five projects are placed in Web Development, because each has a
Vercel web deployment (its GitHub homepage field) and a GitHub
repository — that is the verified basis for the placement, not an
assumption from the name alone. Cards alternate sides, as on the
reference. No project is claimed to use a technology outside its
verified source, and no client, user count, or achievement is claimed
for any project.

| Project | Description source | Tech shown (source) | GitHub | Live site (verified 3 Nov 2026, HTTP 200) |
|---|---|---|---|---|
| JAN AWAAZ | GitHub repo description, verbatim in substance | TypeScript (repo language) | github.com/ayushsingh841434a-lgtm/JanAwaaz | jan-awaaz-beta.vercel.app |
| BREAK THE INTERNET | Your supplied concept description in this task (plus GitHub description confirming pure HTML/CSS/Vanilla JS) | HTML, CSS, Vanilla JavaScript | github.com/ayushsingh841434a-lgtm/BREAK-THE-INTERNET-INFRASTRUCTURE-LAB | brkktheint.vercel.app |
| AIMT COLLEGE | GitHub repo description | TypeScript (repo language) | github.com/ayushsingh841434a-lgtm/AIMT-College-Management-System | aimt-college-management-system.vercel.app |
| EXAM DESK | None published — field left editable, explicitly marked "Description to be added" | TypeScript (repo language) | github.com/ayushsingh841434a-lgtm/EXAM-DESK | exam-desk-alpha.vercel.app |
| TVESE AI | None published — field left editable, explicitly marked "Description to be added" | HTML (TVESE-AI1 repo language; the TVESE-AI repo itself lists no language) | github.com/ayushsingh841434a-lgtm/TVESE-AI | tvese-ai-1.vercel.app (homepage of TVESE-AI1) |

Other GitHub repositories found (e.g. Online-Book-Hub, smart, nidhi,
exam, ayush, momo-hub) were NOT added, because they were not in your
five-project list for this task.

## 4. Interests

`index.html` hero, under the introduction: "Frontend web development ·
Programming · Building websites and web applications · Learning DSA
using Java · Working with Git and GitHub · Using AI-assisted tools to
design and build websites." Presented as interests, not as employment
or qualifications.

## 5. Deployments

- Footer Status column on every page: "Deployments: Vercel for
  projects · Render for databases" plus "Individual live links are
  shown only where verified."
- All five project live links above are Vercel domains, each verified
  HTTP 200 on 3 Nov 2026. No Render database URL is displayed, because
  none was provided or verified — Render is named only as the database
  deployment platform, exactly as you stated it.
- No project is described as "live" beyond its verified link, and no
  deployment is claimed for App, UI/UX, Graphic, or Photography, whose
  galleries remain ready for future content.

## 6. What was deliberately NOT invented

Searched and confirmed absent from all site pages: any email address,
college name, degree, graduation year, employment history, internship,
certification, award, client name, user statistic, or achievement.
The story timeline stays a single neutral placeholder entry; the
contact form still states plainly that sending is not connected until
a contact email is provided (CONTACT_EMAIL in `content.js` is empty);
App, UI/UX, Graphic, and Photography keep neutral placeholder
structures, not invented work.

## 7. Where to edit later

- `content.js` — name, social links, CONTACT_EMAIL, skills, learning,
  interests, deployments, and the five web projects (same data as the
  Web page cards).
- `tools/gen_categories.py` — regenerates the five category pages
  (run `python3 tools/gen_categories.py` after editing, then retest).
