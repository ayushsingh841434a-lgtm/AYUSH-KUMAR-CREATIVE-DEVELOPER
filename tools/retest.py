"""Retest for Ayush Kumar portfolio (kept in the project, not /tmp).
Covers both viewports: doors, routes, back, menu/pillnav, contact,
ability rows, web project cards, console errors. Run: python3 tools/retest.py"""
import sys
from playwright.sync_api import sync_playwright
BASE = "http://localhost:8901/"
EXE = "/home/hatch/.cache/ms-playwright/chromium-1248/chrome-linux64/chrome"
passed = failed = 0
def check(name, ok, extra=""):
    global passed, failed
    if ok: passed += 1; print("PASS", name)
    else: failed += 1; print("FAIL", name, extra)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=EXE, args=["--no-sandbox"])
    for w, h, tag in [(1440, 900, "desktop"), (390, 844, "mobile")]:
        errs = []
        ctx = b.new_context(viewport={"width": w, "height": h}); pg = ctx.new_page()
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.goto(BASE, wait_until="networkidle"); pg.wait_for_timeout(2600)
        check(f"{tag}: 5 doors", pg.locator(".door").count() == 5)
        check(f"{tag}: name in hero", "Ayush Kumar" in pg.locator("h1").inner_text())
        check(f"{tag}: ability rows 9", pg.evaluate("document.getElementById('abilityDlg').showModal(); document.querySelectorAll('.ability-row').length") == 9)
        pg.evaluate("document.getElementById('abilityDlg').close()")
        for i, route in enumerate(["web-developer/", "app-developer/", "ui-ux-designer/", "graphic-designer/", "photographer/"]):
            pg.evaluate("document.getElementById('doorWall').scrollLeft=0")
            d = pg.locator(".door").nth(i)
            d.scroll_into_view_if_needed(); pg.wait_for_timeout(200)
            d.click(); pg.wait_for_timeout(1100)
            check(f"{tag}: door {i+1} -> {route}", route in pg.url, pg.url)
            check(f"{tag}: door {i+1} back button", pg.locator("[data-back]").count() >= 1)
            pg.locator("[data-back]").first.click(); pg.wait_for_timeout(800)
            check(f"{tag}: door {i+1} back returns #work", "#work" in pg.url, pg.url)
        pg.goto(BASE, wait_until="networkidle"); pg.wait_for_timeout(2600)
        if w >= 1024:
            check(f"{tag}: pill nav >=7", pg.evaluate("document.querySelectorAll('.pillnav a, .pillnav button').length>=7"))
            pg.evaluate("document.getElementById('menuDlg').showModal()")
            check(f"{tag}: menu 8 items", pg.evaluate("document.querySelectorAll('#menuDlg .cta [data-goto]').length===8"))
            pg.evaluate("document.getElementById('menuDlg').close()")
        else:
            pg.locator('[data-open="menuDlg"]').first.click(); pg.wait_for_timeout(300)
            check(f"{tag}: menu 8 items", pg.evaluate("document.querySelectorAll('#menuDlg .cta [data-goto]').length===8"))
            pg.evaluate("document.getElementById('menuDlg').close()")
        pg.evaluate("([...document.querySelectorAll('[data-open=contactDlg]')].find(el=>el.offsetParent!==null)).click()"); pg.wait_for_timeout(300)
        check(f"{tag}: contact opens + title", pg.evaluate("document.getElementById('contactDlg').open && document.querySelector('#contactDlg h2').textContent.includes('Tell me what you need built')"))
        pg.evaluate("document.getElementById('contactDlg').close()")
        pg.evaluate("window.scrollTo(0, document.body.scrollHeight)"); pg.wait_for_timeout(400)
        pg.locator("[data-top]").first.click(); pg.wait_for_timeout(700)
        check(f"{tag}: back-to-top", pg.evaluate("window.scrollY") < 200)
        r = pg.goto(BASE + "web-developer/", wait_until="networkidle")
        check(f"{tag}: web 5 real cards", pg.locator(".proj-card").count() == 5 and all(x in pg.content() for x in ["JAN AWAAZ", "BREAK THE INTERNET", "AIMT COLLEGE", "EXAM DESK", "TVESE AI"]))
        for route in ["app-developer/", "ui-ux-designer/", "graphic-designer/", "photographer/"]:
            r = pg.goto(BASE + route, wait_until="networkidle"); check(f"{tag}: direct {route}", r.status == 200)
        check(f"{tag}: no console errors", len(errs) == 0, "; ".join(errs)[:200])
        ctx.close()
    b.close()
print(f"\nSUMMARY {passed}/{passed+failed} passed")
sys.exit(1 if failed else 0)
