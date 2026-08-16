import sys, os
sys.path.insert(0, r'c:\Users\dgibb\TT-Adventure-Sessionbook\.claude\skills\run-tt-adventure-sessionbook')
import driver
from playwright.sync_api import sync_playwright
fails=[]
def chk(l,c):
    print(('  PASS  ' if c else '  FAIL  ')+l)
    if not c: fails.append(l)
with driver.static_server(8850):
    with sync_playwright() as pw:
        b=pw.chromium.launch(channel='chrome')
        ctx=b.new_context(viewport=driver.VIEWPORT)
        p=ctx.new_page()
        errs=[]; p.on('console', lambda m: errs.append(m.text) if m.type=='error' else None)
        p.goto('http://localhost:8850/index.html?campaign=fail-academy')
        driver.wait_for_dashboard(p); driver.dm_login(p,'Smuckers')
        p.click('#settings-btn'); p.wait_for_timeout(350)

        link = p.locator('#settings-gallery-link')
        chk('link visible in settings modal', link.is_visible())
        chk('opens in new tab (target=_blank)', link.get_attribute('target')=='_blank')
        chk('has rel=noopener', 'noopener' in (link.get_attribute('rel') or ''))
        # positioned above the dropdown?
        ly = link.bounding_box()['y']; sy = p.locator('#settings-theme').bounding_box()['y']
        chk('sits above the dropdown (%.0f < %.0f)' % (ly, sy), ly < sy)

        # actually click it and confirm a second tab loads the gallery
        before = len(ctx.pages)
        with ctx.expect_page() as newp:
            link.click()
        np = newp.value
        np.wait_for_load_state(); np.wait_for_timeout(700)
        chk('click opened a NEW tab (%d -> %d)' % (before, len(ctx.pages)), len(ctx.pages) == before+1)
        chk('new tab is the gallery, %d cards' % np.locator('.card').count(),
            np.locator('.card').count() == 16)
        chk('original tab still on the app', 'index.html' in p.url)
        chk('settings modal still open in original tab',
            not p.evaluate("document.getElementById('settings-overlay').hidden"))
        chk('no console errors %s' % errs, not errs)
        p.screenshot(path=os.path.join(driver.SCREEN_DIR,'settings_with_link.png'))
        b.close()
print('\nRESULT:', 'PASS' if not fails else 'FAIL -> '+'; '.join(fails))
