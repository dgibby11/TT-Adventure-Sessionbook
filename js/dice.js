// dice.js — Dice roller dropdown in the topbar.
//
// Clicking #dice-btn opens the panel. Select a die type, set a count, hit Roll.
// A large die SVG animates (shake + tumble), then snaps to the result with a
// gold glow. For multi-die rolls the total is shown large. History stacks below.

(function () {
  // ── SVG templates ────────────────────────────────────────────────────────────
  // font-size in SVG viewBox units (0–50 space) — scales with render size.
  function fsize(v) {
    const n = String(v).length;
    return n >= 4 ? 9 : n === 3 ? 11 : n === 2 ? 14 : 17;
  }

  const SHAPES = {
    4:   (v) => `<svg viewBox="0 0 50 50" class="die-svg"><polygon points="25,3 48,46 2,46"/><text x="25" y="33" font-size="${fsize(v)}" dominant-baseline="central">${v}</text></svg>`,
    6:   (v) => `<svg viewBox="0 0 50 50" class="die-svg"><rect x="2" y="2" width="46" height="46" rx="5"/><text x="25" y="25" font-size="${fsize(v)}" dominant-baseline="central">${v}</text></svg>`,
    8:   (v) => `<svg viewBox="0 0 50 50" class="die-svg"><polygon points="25,2 48,25 25,48 2,25"/><text x="25" y="25" font-size="${fsize(v)}" dominant-baseline="central">${v}</text></svg>`,
    10:  (v) => `<svg viewBox="0 0 50 50" class="die-svg"><polygon points="25,1 47,17 39,43 11,43 3,17"/><text x="25" y="25" font-size="${fsize(v)}" dominant-baseline="central">${v}</text></svg>`,
    12:  (v) => `<svg viewBox="0 0 50 50" class="die-svg"><polygon points="25,2 45,14 45,36 25,48 5,36 5,14"/><text x="25" y="25" font-size="${fsize(v)}" dominant-baseline="central">${v}</text></svg>`,
    20:  (v) => `<svg viewBox="0 0 50 50" class="die-svg"><polygon points="15,2 35,2 48,15 48,35 35,48 15,48 2,35 2,15"/><text x="25" y="25" font-size="${fsize(v)}" dominant-baseline="central">${v}</text></svg>`,
    100: (v) => `<svg viewBox="0 0 50 50" class="die-svg"><circle cx="25" cy="25" r="22"/><text x="25" y="25" font-size="${fsize(v)}" dominant-baseline="central">${v}</text></svg>`,
  };

  // Stage variant: same shapes but with the stage CSS class for large rendering
  function stageShape(sides, v) {
    const svg = SHAPES[sides](v);
    return svg.replace('class="die-svg"', 'class="die-svg die-svg-stage"');
  }

  const DICE = [4, 6, 8, 10, 12, 20, 100];

  let panel, stageEl, resultArea, numInput, activeLabel, rollBtn;
  let activeDie = 20;
  let rolling   = false;

  // ── Roll logic ───────────────────────────────────────────────────────────────
  function randInt(sides) { return Math.floor(Math.random() * sides) + 1; }

  function doRoll() {
    if (rolling) return;
    rolling = true;
    rollBtn.disabled = true;

    const n      = Math.max(1, Math.min(20, parseInt(numInput.value, 10) || 1));
    const values = Array.from({ length: n }, () => randInt(activeDie));
    const total  = values.reduce((s, v) => s + v, 0);
    const label  = (n > 1 ? n + '×' : '') + (activeDie === 100 ? 'd%' : 'd' + activeDie);

    // ── Stage: start throw animation ─────────────────────────────────────────
    // Show the die (no value yet — just the shape, question mark)
    stageEl.innerHTML = '<div class="dice-throw-wrap">' + stageShape(activeDie, '?') + '</div>';
    const wrap = stageEl.querySelector('.dice-throw-wrap');
    // Force reflow so the animation restarts
    void wrap.offsetWidth;
    wrap.classList.add('dice-throwing');

    // ── After throw: reveal result ────────────────────────────────────────────
    setTimeout(() => {
      wrap.classList.remove('dice-throwing');

      const isD20Multi = (activeDie === 20 && n > 1);

      if (n === 1) {
        // Single die: show die shape with the value + glow
        wrap.innerHTML = stageShape(activeDie, total);
        wrap.classList.add('dice-landed');
      } else if (isD20Multi) {
        // d20 multi-roll (advantage / disadvantage): show each die individually
        wrap.innerHTML =
          `<div class="dice-stage-multi">${values.map(v => stageShape(20, v)).join('')}</div>` +
          `<div class="dice-stage-multi-label">${label}</div>`;
        wrap.classList.add('dice-landed');
      } else {
        // Multiple non-d20 dice: show big total + label
        wrap.innerHTML = `
          <div class="dice-stage-total">
            <span class="dice-stage-total-num">${total}</span>
            <span class="dice-stage-total-label">${label}</span>
          </div>`;
        wrap.classList.add('dice-landed-multi');
      }

      // ── Add to history ───────────────────────────────────────────────────
      const row = document.createElement('div');
      row.className = 'dice-result-row new-entry';

      const diceEl = document.createElement('div');
      diceEl.className = 'dice-result-dice';

      for (const v of values) {
        const span = document.createElement('span');
        span.className = 'dice-result-die';
        span.innerHTML = SHAPES[activeDie](v);
        diceEl.appendChild(span);
      }
      if (n > 1 && activeDie !== 20) {
        const tot = document.createElement('span');
        tot.className = 'dice-result-total';
        tot.textContent = '= ' + total;
        diceEl.appendChild(tot);
      }
      row.appendChild(diceEl);
      resultArea.insertBefore(row, resultArea.firstChild);
      while (resultArea.children.length > 12) resultArea.removeChild(resultArea.lastChild);

      // Remove animation class after it finishes so re-roll can restart it
      setTimeout(() => { row.classList.remove('new-entry'); }, 300);

      rolling = false;
      rollBtn.disabled = false;
    }, 680);
  }

  // ── Build panel ──────────────────────────────────────────────────────────────
  function setActive(sides) {
    activeDie = sides;
    activeLabel.textContent = sides === 100 ? 'd%' : 'd' + sides;
    panel.querySelectorAll('.die-btn').forEach((b) =>
      b.classList.toggle('die-btn-active', +b.dataset.sides === sides));

    // Update stage if a result is already showing
    if (!rolling && stageEl.querySelector('.dice-landed')) {
      // Just reset stage to blank when die type changes
      stageEl.innerHTML = '';
    }
  }

  function buildPanel() {
    panel = document.createElement('div');
    panel.id = 'dice-panel';
    panel.hidden = true;

    // ── Die selector ──────────────────────────────────────────────────────────
    const selector = document.createElement('div');
    selector.id = 'dice-selector';
    for (const d of DICE) {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'die-btn' + (d === activeDie ? ' die-btn-active' : '');
      btn.dataset.sides = d;
      btn.title = d === 100 ? 'd100' : 'd' + d;
      btn.innerHTML = SHAPES[d](d === 100 ? 'd%' : 'd' + d);
      btn.addEventListener('click', () => {
        if (+btn.dataset.sides === activeDie) {
          numInput.value = Math.min(20, parseInt(numInput.value, 10) + 1);
        } else {
          numInput.value = 1;
          setActive(d);
        }
      });
      selector.appendChild(btn);
    }

    // ── Stage ─────────────────────────────────────────────────────────────────
    stageEl = document.createElement('div');
    stageEl.id = 'dice-stage';

    // ── Controls ──────────────────────────────────────────────────────────────
    const controls = document.createElement('div');
    controls.id = 'dice-controls';

    numInput = document.createElement('input');
    numInput.type = 'number';
    numInput.id = 'dice-num';
    numInput.min = 1; numInput.max = 20; numInput.value = 1;
    numInput.setAttribute('aria-label', 'Number of dice');

    activeLabel = document.createElement('span');
    activeLabel.className = 'dice-active-label';
    activeLabel.textContent = 'd20';

    rollBtn = document.createElement('button');
    rollBtn.type = 'button';
    rollBtn.id = 'dice-roll-btn';
    rollBtn.textContent = 'Roll';
    rollBtn.addEventListener('click', doRoll);

    numInput.addEventListener('keydown', (e) => { if (e.key === 'Enter') doRoll(); });

    const clearBtn = document.createElement('button');
    clearBtn.type = 'button';
    clearBtn.id = 'dice-clear-btn';
    clearBtn.textContent = 'Clear';
    clearBtn.addEventListener('click', () => {
      resultArea.innerHTML = '';
      stageEl.innerHTML = '';
    });

    controls.appendChild(numInput);
    controls.appendChild(activeLabel);
    controls.appendChild(rollBtn);
    controls.appendChild(clearBtn);

    resultArea = document.createElement('div');
    resultArea.id = 'dice-result-area';

    panel.appendChild(selector);
    panel.appendChild(stageEl);
    panel.appendChild(controls);
    panel.appendChild(resultArea);

    const wrap = document.getElementById('dice-wrap');
    (wrap || document.body).appendChild(panel);
  }

  // ── Toggle ───────────────────────────────────────────────────────────────────
  function openPanel() {
    if (!panel) buildPanel();
    panel.hidden = !panel.hidden;
    if (!panel.hidden) numInput && numInput.focus();
  }

  // ── Wire ─────────────────────────────────────────────────────────────────────
  function wire() {
    const btn = document.getElementById('dice-btn');
    if (!btn) return;
    btn.addEventListener('click', (e) => { e.stopPropagation(); openPanel(); });

    document.addEventListener('click', (e) => {
      if (panel && !panel.hidden) {
        const wrap = document.getElementById('dice-wrap');
        if (wrap && !wrap.contains(e.target)) panel.hidden = true;
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && panel && !panel.hidden) panel.hidden = true;
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', wire);
  else wire();
})();
