import sys, os
sys.path.insert(0, r'c:\Users\dgibb\TT-Adventure-Sessionbook\.claude\skills\run-tt-adventure-sessionbook')
import driver
from playwright.sync_api import sync_playwright
PORT, SHOT = 8805, driver.SCREEN_DIR
os.makedirs(SHOT, exist_ok=True)
fails = []
def chk(label, cond):
    print(('  PASS  ' if cond else '  FAIL  ') + label)
    if not cond: fails.append(label)

with driver.static_server(PORT):
    with sync_playwright() as pw:
        b = pw.chromium.launch(channel='chrome')
        p = b.new_page(viewport=driver.VIEWPORT)
        errs = []
        p.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
        p.on('pageerror', lambda e: errs.append('PAGEERROR ' + str(e)))
        p.goto(f'http://localhost:{PORT}/index.html?campaign=fail-academy')
        driver.wait_for_dashboard(p)

        chk('Settings button present', p.is_visible('#settings-btn'))
        chk('modal starts hidden', p.evaluate("!document.getElementById('settings-overlay') || document.getElementById('settings-overlay').hidden"))

        p.click('#settings-btn'); p.wait_for_timeout(300)
        chk('modal opens', p.is_visible('#settings-dialog'))
        opts = p.eval_on_selector_all('#settings-theme option', 'e=>e.map(o=>o.textContent)')
        chk('dropdown labelled "Color Theme"', 'COLOR THEME' in p.inner_text('#settings-body').upper())
        chk('theme roster  got=%s' % opts, opts == ['Default','Artificer','Barbarian','Bard','Blood Hunter','Cleric','Druid','Fighter','Monk','Paladin','Pugilist','Ranger','Rogue','Sorcerer','Warlock','Wizard'])
        p.screenshot(path=os.path.join(SHOT, 'settings_01_open.png'))

        # Cancel closes
        p.click('#settings-cancel'); p.wait_for_timeout(250)
        chk('Cancel closes modal', p.evaluate("document.getElementById('settings-overlay').hidden"))

        # Save closes + persists
        p.click('#settings-btn'); p.wait_for_timeout(250)
        p.click('#settings-save'); p.wait_for_timeout(250)
        chk('Save closes modal', p.evaluate("document.getElementById('settings-overlay').hidden"))
        stored = p.evaluate("localStorage.getItem('tt.settings.v1')")
        chk('Save persisted settings  got=%s' % stored, stored and 'default' in stored)
        chk('settings NOT written into campaign store',
            'theme' not in (p.evaluate("localStorage.getItem('fail-academy.v1')") or ''))

        # Esc closes
        p.click('#settings-btn'); p.wait_for_timeout(200)
        p.keyboard.press('Escape'); p.wait_for_timeout(250)
        chk('Esc closes modal', p.evaluate("document.getElementById('settings-overlay').hidden"))

        chk('no console/page errors  %s' % errs, not errs)
        b.close()
print('\nRESULT:', 'PASS' if not fails else 'FAIL -> ' + '; '.join(fails))
