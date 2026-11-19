"""Browser checks for routes, assets, controls, dialogs, and responsive layouts.
Requires the optional tools/requirements.txt dependencies, Chromium, and a static
server. Start one on port 8000, then run: python tools/retest.py"""
import os
import sys
from playwright.sync_api import sync_playwright
BASE = os.environ.get("PORTFOLIO_BASE_URL", "http://127.0.0.1:8000").rstrip("/") + "/"
EXE = os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE")
passed = failed = 0
def check(name, ok, extra=""):
    global passed, failed
    if ok: passed += 1; print("PASS", name)
    else: failed += 1; print("FAIL", name, extra)

with sync_playwright() as p:
    launch_options = {"args": ["--no-sandbox"]}
    if EXE:
        launch_options["executable_path"] = EXE
    b = p.chromium.launch(**launch_options)
    for w, h, tag in [(1440, 900, "desktop"), (768, 1024, "tablet"), (390, 844, "mobile")]:
        errs = []
        neterrs = []
        ctx = b.new_context(viewport={"width": w, "height": h}); pg = ctx.new_page()
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("requestfailed", lambda r: neterrs.append(f"{r.url}: {r.failure}"))
        pg.on("response", lambda r: neterrs.append(f"{r.status} {r.url}") if r.status >= 400 and r.url.startswith(BASE) else None)
        pg.goto(BASE, wait_until="networkidle"); pg.wait_for_timeout(2600)
        check(f"{tag}: 5 doors", pg.locator(".door").count() == 5)
        check(f"{tag}: name in hero", "Ayush Kumar" in pg.locator("h1").inner_text())
        check(f"{tag}: ability rows 9", pg.evaluate("document.getElementById('abilityDlg').showModal(); document.querySelectorAll('.ability-row').length") == 9)
        pg.locator("#abilityDlg [data-close]").click()
        check(f"{tag}: ability dialog closes", not pg.locator("#abilityDlg").evaluate("el => el.open"))
        check(f"{tag}: Onest font loads", pg.evaluate("document.fonts.check('16px Onest')"))
        check(f"{tag}: home images load", pg.evaluate("[...document.images].every(img => img.complete && img.naturalWidth > 0)"))
        check(f"{tag}: home has no horizontal overflow", pg.evaluate("document.documentElement.scrollWidth <= document.documentElement.clientWidth"))
        for i, route in enumerate(["web-developer/", "app-developer/", "ui-ux-designer/", "graphic-designer/", "photographer/"]):
            pg.evaluate("document.getElementById('doorWall').scrollLeft=0")
            d = pg.locator(".door").nth(i)
            d.scroll_into_view_if_needed(); pg.wait_for_timeout(200)
            d.click(); pg.wait_for_timeout(1400)
            check(f"{tag}: door {i+1} -> {route}", route in pg.url, pg.url)
            check(f"{tag}: door {i+1} back button", pg.locator("[data-back]").count() >= 1)
            pg.locator("[data-back]").first.click(); pg.wait_for_timeout(800)
            check(f"{tag}: door {i+1} back returns #work", "#work" in pg.url, pg.url)
        pg.goto(BASE, wait_until="networkidle"); pg.wait_for_timeout(2600)
        if w >= 1024:
            check(f"{tag}: pill nav >=7", pg.evaluate("document.querySelectorAll('.pillnav a, .pillnav button').length>=7"))
            pg.evaluate("document.getElementById('menuDlg').showModal()")
            check(f"{tag}: menu 8 items", pg.evaluate("document.querySelectorAll('#menuDlg .cta [data-goto]').length===8"))
            pg.locator("#menuDlg [data-close]").click()
        else:
            pg.locator('[data-open="menuDlg"]').first.click(); pg.wait_for_timeout(300)
            check(f"{tag}: menu 8 items", pg.evaluate("document.querySelectorAll('#menuDlg .cta [data-goto]').length===8"))
            pg.locator("#menuDlg [data-close]").click()
        pg.locator('[data-open="contactDlg"]:visible').first.click(); pg.wait_for_timeout(300)
        check(f"{tag}: contact opens + title", pg.evaluate("document.getElementById('contactDlg').open && document.querySelector('#contactDlg h2').textContent.includes('Tell me what you need built')"))
        pg.keyboard.press("Escape")
        check(f"{tag}: Escape closes contact", not pg.locator("#contactDlg").evaluate("el => el.open"))
        pg.locator('[data-open="contactDlg"]:visible').first.click()
        pg.locator('#contactForm [name="name"]').fill("Portfolio test")
        pg.locator('#contactForm [name="email"]').fill("test@example.com")
        pg.locator('#contactForm [name="phone"]').fill("0000000000")
        pg.locator('#contactForm [name="message"]').fill("Automated validation only")
        pg.locator('#contactForm [type="submit"]').click()
        check(f"{tag}: contact does not fake sending", "sending is not connected" in pg.locator("#formNote").inner_text().lower())
        pg.locator('#contactDlg [data-close]').click()
        pg.evaluate("window.scrollTo(0, document.body.scrollHeight)"); pg.wait_for_timeout(400)
        pg.locator("[data-top]").first.click(); pg.wait_for_timeout(700)
        check(f"{tag}: back-to-top", pg.evaluate("window.scrollY") < 200)
        for route in ["", "web-developer/", "app-developer/", "ui-ux-designer/", "graphic-designer/", "photographer/"]:
            r = pg.goto(BASE + route, wait_until="networkidle")
            check(f"{tag}: direct {route or '/'} returns 200", r.status == 200)
            check(f"{tag}: {route or '/'} has no horizontal overflow", pg.evaluate("document.documentElement.scrollWidth <= document.documentElement.clientWidth"))
            check(f"{tag}: {route or '/'} images load", pg.evaluate("[...document.images].every(img => img.complete && img.naturalWidth > 0)"))
            check(f"{tag}: {route or '/'} Onest font loads", pg.evaluate("document.fonts.check('16px Onest')"))
            check(f"{tag}: {route or '/'} fragment links resolve", pg.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].every(a => a.getAttribute('href') === '#' || !!document.getElementById(decodeURIComponent(a.hash.slice(1))))"))
            if route == "web-developer/":
                check(f"{tag}: web 5 real cards", pg.locator(".proj-card").count() == 5 and all(x in pg.content() for x in ["JAN AWAAZ", "BREAK THE INTERNET", "AIMT COLLEGE", "EXAM DESK", "TVESE AI"]))
        pg.locator(".photo-slot").first.click()
        check(f"{tag}: photo slot click feedback", "No photograph added" in pg.locator("#wallHint").inner_text())
        pg.locator(".photo-slot").nth(1).focus(); pg.keyboard.press("Enter")
        check(f"{tag}: photo slot keyboard feedback", "No photograph added" in pg.locator("#wallHint").inner_text())
        before_pan = pg.locator("#wallInner").get_attribute("style")
        pg.locator("#photoWall").focus(); pg.keyboard.press("ArrowLeft")
        check(f"{tag}: photo wall arrow-key pan", before_pan != pg.locator("#wallInner").get_attribute("style"))
        wall_box = pg.locator("#photoWall").bounding_box()
        before_drag = pg.locator("#wallInner").get_attribute("style")
        drag_x = wall_box["x"] + wall_box["width"] - 30
        drag_y = wall_box["y"] + 70
        pg.mouse.move(drag_x, drag_y); pg.mouse.down()
        pg.mouse.move(drag_x - 40, drag_y - 30, steps=3); pg.mouse.up()
        check(f"{tag}: photo wall pointer drag", before_drag != pg.locator("#wallInner").get_attribute("style"))
        check(f"{tag}: no console errors", len(errs) == 0, "; ".join(errs)[:200])
        check(f"{tag}: no failed or HTTP error requests", len(neterrs) == 0, "; ".join(neterrs)[:200])
        ctx.close()
    b.close()
print(f"\nSUMMARY {passed}/{passed+failed} passed")
sys.exit(1 if failed else 0)
