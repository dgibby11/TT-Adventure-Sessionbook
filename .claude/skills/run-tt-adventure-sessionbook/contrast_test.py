import sys, os
sys.path.insert(0, r'c:\Users\dgibb\TT-Adventure-Sessionbook\.claude\skills\run-tt-adventure-sessionbook')
import driver
from playwright.sync_api import sync_playwright

def lum(c):
    n=[int(x)/255 for x in c.strip('rgba() ').split(',')[:3]]
    n=[(v/12.92 if v<=0.03928 else ((v+0.055)/1.055)**2.4) for v in n]
    return 0.2126*n[0]+0.7152*n[1]+0.0722*n[2]
def ratio(a,b):
    l1,l2=sorted([lum(a),lum(b)],reverse=True)
    return (l1+0.05)/(l2+0.05)

fails=[]
with driver.static_server(8822):
    with sync_playwright() as pw:
        b=pw.chromium.launch(channel='chrome')
        for tid in ('default','artificer','barbarian','bard','blood-hunter','cleric','druid','fighter','monk','paladin','pugilist','ranger','rogue','sorcerer','warlock','wizard'):
            p=b.new_page(viewport=driver.VIEWPORT)
            p.goto(f'http://localhost:8822/index.html?campaign=fail-academy')
            driver.wait_for_dashboard(p); driver.dm_login(p,'Smuckers')
            p.evaluate("t=>{if(t!=='default')document.documentElement.setAttribute('data-theme',t)}", tid)
            p.wait_for_timeout(250)
            p.click('#settings-btn'); p.wait_for_timeout(350)
            fg=p.eval_on_selector('#settings-save',"e=>getComputedStyle(e)['color']")
            bg=p.eval_on_selector('#settings-save',"e=>getComputedStyle(e)['background-color']")
            r=ratio(fg,bg)
            ok = r >= 4.5
            print(('  PASS  ' if ok else '  FAIL  ')+f'{tid:13} Save button contrast {r:.2f}:1  ({fg} on {bg})')
            if not ok: fails.append(tid)
            # body text on panel
            fg2=p.eval_on_selector('.dash-entity-card',"e=>getComputedStyle(e)['color']")
            bg2=p.eval_on_selector('.dash-quad',"e=>getComputedStyle(e)['background-color']")
            r2=ratio(fg2,bg2)
            ok2 = r2>=4.5
            print(('  PASS  ' if ok2 else '  FAIL  ')+f'{tid:13} card text on panel   {r2:.2f}:1')
            if not ok2: fails.append(tid+'-body')
            p.close()
        b.close()
print('\nRESULT:', 'PASS' if not fails else 'FAIL -> '+', '.join(fails))
