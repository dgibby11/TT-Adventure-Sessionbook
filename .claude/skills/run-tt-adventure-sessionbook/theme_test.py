import sys, os
sys.path.insert(0, r'c:\Users\dgibb\TT-Adventure-Sessionbook\.claude\skills\run-tt-adventure-sessionbook')
import driver
from playwright.sync_api import sync_playwright
SHOT = driver.SCREEN_DIR; os.makedirs(SHOT, exist_ok=True)
fails=[]
def chk(l,c):
    print(('  PASS  ' if c else '  FAIL  ')+l)
    if not c: fails.append(l)

def px(p, sel, prop='background-color'):
    return p.eval_on_selector(sel, "e=>getComputedStyle(e)[%s]" % repr(prop))

with driver.static_server(8810):
    with sync_playwright() as pw:
        b=pw.chromium.launch(channel='chrome'); p=b.new_page(viewport=driver.VIEWPORT)
        errs=[]
        p.on('console', lambda m: errs.append(m.text) if m.type=='error' else None)
        p.on('pageerror', lambda e: errs.append('PAGEERR '+str(e)))
        p.goto('http://localhost:8810/index.html?campaign=fail-academy')
        driver.wait_for_dashboard(p)
        driver.dm_login(p,'Smuckers')
        p.wait_for_timeout(300)

        seen={}
        for tid,label in zip(('default','artificer','barbarian','bard','blood-hunter','cleric','druid','fighter','monk','paladin','pugilist','ranger','rogue','sorcerer','warlock','wizard'), ['Default','Artificer','Barbarian','Bard','Blood Hunter','Cleric','Druid','Fighter','Monk','Paladin','Pugilist','Ranger','Rogue','Sorcerer','Warlock','Wizard']):
            p.click('#settings-btn'); p.wait_for_timeout(200)
            p.select_option('#settings-theme', tid)
            p.click('#settings-save'); p.wait_for_timeout(400)
            attr = p.evaluate("document.documentElement.getAttribute('data-theme')")
            chk(f'{label}: data-theme = {attr!r}', attr == (None if tid=='default' else tid))
            seen[tid] = (px(p,'#dashboard'), px(p,'.dash-quad'), px(p,'body','color'))
            chk(f'{label}: still in DM mode after theme swap',
                p.evaluate("document.body.classList.contains('dm-on')"))
            p.screenshot(path=os.path.join(SHOT, f'theme_{tid}.png'))

        chk('all %d themes render distinct dashboard grounds' % len(seen),
            len({v[0] for v in seen.values()}) == len(seen))
        for t,(ground,quad,ink) in seen.items():
            print(f'      {t:13} ground={ground:22} quad={quad:22} ink={ink}')

        # guard rail: ground vs quad must not converge
        def lum(c):
            n=[int(x) for x in c.strip('rgba() ').split(',')[:3]]
            return 0.2126*n[0]+0.7152*n[1]+0.0722*n[2]
        for t,(ground,quad,_) in seen.items():
            d=abs(lum(ground)-lum(quad))
            chk(f'{t}: ground/quad luminance gap = {d:.0f} (>25 required)', d > 25)

        # instant swap must not reload: prove by marking the window
        p.evaluate("window.__notReloaded = true")
        p.click('#settings-btn'); p.wait_for_timeout(150)
        p.select_option('#settings-theme','blood-hunter'); p.click('#settings-save'); p.wait_for_timeout(300)
        chk('theme swap did NOT reload the page', p.evaluate("window.__notReloaded === true"))

        # DM mode persists across a real reload
        p.reload(); driver.wait_for_dashboard(p); p.wait_for_timeout(400)
        chk('DM mode survives reload', p.evaluate("document.body.classList.contains('dm-on')"))
        chk('theme survives reload (no flash-back)',
            p.evaluate("document.documentElement.getAttribute('data-theme')")=='blood-hunter')
        chk('no console/page errors %s'%errs, not errs)
        b.close()
print('\nRESULT:', 'PASS' if not fails else 'FAIL -> '+'; '.join(fails))
