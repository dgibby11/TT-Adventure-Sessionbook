// resources.js — Resources dropdown + reference modal.
//
// Phase 1: dropdown toggle (Spells, Gods, Monsters-soon).
// Phase 2: resource modal — fetches content/references/<resource>.html,
//          displays in scrollable parchment overlay, caches after first load.
// Phase 3: live search + class filter (spells) + alignment/domain filters +
//          column sorting (gods) + result count.

(function () {
  const LABELS = { spells: 'Spells', gods: 'Gods', monsters: 'Monsters' };

  const wrap = document.getElementById('resources-wrap');
  const btn  = document.getElementById('resources-btn');
  const menu = document.getElementById('resources-menu');

  // ── Dropdown ──────────────────────────────────────────────────────────────
  function openMenu() {
    menu.hidden = false;
    btn.setAttribute('aria-expanded', 'true');
  }

  function closeMenu() {
    menu.hidden = true;
    btn.setAttribute('aria-expanded', 'false');
  }

  btn.addEventListener('click', () => {
    if (menu.hidden) openMenu(); else closeMenu();
  });

  document.addEventListener('click', (e) => {
    if (!wrap.contains(e.target)) closeMenu();
  });

  menu.addEventListener('click', (e) => {
    const item = e.target.closest('[data-resource]');
    if (!item) return;
    closeMenu();
    openResourceModal(item.dataset.resource);
  });

  // ── Resource modal ─────────────────────────────────────────────────────────
  let overlay, modalEl, titleEl, searchInput, classFilter, countEl, bodyEl, searchRow;
  let currentResource = null;
  let filterTimer     = null;
  let dynamicFilters  = {}; // extra filter elements added per-resource, keyed by name
  let godsSort        = { col: -1, dir: 1 };
  let monstersSort    = { col:  0, dir: 1 }; // default: Name asc
  const cache           = {};
  let monsterIndex      = [];   // lightweight list data (name/type/cr/source)
  let allMonsters       = null; // full stat block data, null until first detail click
  let monstersLoaded    = false;
  let monstersFullLoading = false;
  let pendingDetailIdx  = -1;
  let detailPanel       = null;

  function build() {
    overlay = document.createElement('div');
    overlay.id = 'resource-overlay';
    overlay.hidden = true;
    overlay.innerHTML = `
      <div id="resource-modal" role="dialog" aria-modal="true" aria-labelledby="resource-modal-title">
        <header id="resource-modal-header">
          <h2 id="resource-modal-title"></h2>
          <button id="resource-modal-close" type="button" aria-label="Close">&times;</button>
        </header>
        <div id="resource-search-bar">
          <div id="resource-search-row">
            <input type="search" id="resource-search-input"
              placeholder="Search…" autocomplete="off" disabled />
            <select id="resource-class-filter" hidden aria-label="Filter by class"></select>
          </div>
          <span id="resource-filter-count"></span>
        </div>
        <div id="resource-modal-body"></div>
      </div>`;
    document.body.appendChild(overlay);

    modalEl     = overlay.querySelector('#resource-modal');
    titleEl     = overlay.querySelector('#resource-modal-title');
    searchInput = overlay.querySelector('#resource-search-input');
    classFilter = overlay.querySelector('#resource-class-filter');
    countEl     = overlay.querySelector('#resource-filter-count');
    bodyEl      = overlay.querySelector('#resource-modal-body');
    searchRow   = overlay.querySelector('#resource-search-row');

    overlay.querySelector('#resource-modal-close').addEventListener('click', closeModal);
    overlay.addEventListener('click', (e) => { if (e.target === overlay) closeModal(); });

    searchInput.addEventListener('input', () => {
      clearTimeout(filterTimer);
      filterTimer = setTimeout(applyFilter, 150);
    });

    classFilter.addEventListener('change', applyFilter);
  }

  function closeModal() {
    if (!overlay) return;
    overlay.hidden = true;
    bodyEl.scrollTop = 0;
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && overlay && !overlay.hidden) {
      e.stopImmediatePropagation();
      const lb = document.getElementById('monster-token-lightbox');
      if (lb && !lb.hidden)               { lb.hidden = true; }
      else if (detailPanel && !detailPanel.hidden) { closeMonsterDetail(); }
      else { closeModal(); }
    }
  }, true);

  // ── Open ──────────────────────────────────────────────────────────────────
  function openResourceModal(resource) {
    if (!overlay) build();

    currentResource = resource;
    titleEl.textContent = LABELS[resource] || resource;
    overlay.hidden = false;
    overlay.querySelector('#resource-modal-close').focus();

    // Reset all filter state
    searchInput.value    = '';
    searchInput.disabled = true;
    classFilter.hidden   = true;
    classFilter.innerHTML = '';
    countEl.textContent  = '';
    godsSort     = { col: -1, dir: 1 };
    monstersSort = { col:  0, dir: 1 };

    // Remove any per-resource dynamic filters from previous open
    Object.values(dynamicFilters).forEach((el) => el.remove());
    dynamicFilters = {};
    detailPanel = null;
    modalEl.classList.remove('monster-detail-open');

    if (resource === 'monsters') {
      loadMonsters();
      return;
    }

    if (cache[resource]) {
      bodyEl.innerHTML = cache[resource];
      bodyEl.scrollTop = 0;
      afterLoad(resource);
      return;
    }

    bodyEl.innerHTML = '<p class="resource-status">Loading…</p>';
    bodyEl.scrollTop = 0;

    const base = window.CAMPAIGN_BASE ? window.CAMPAIGN_BASE + '/' : '';
    fetch(base + 'content/references/' + resource + '.html')
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.text();
      })
      .then((html) => {
        cache[resource] = html;
        if (!overlay.hidden && currentResource === resource) {
          bodyEl.innerHTML = html;
          bodyEl.scrollTop = 0;
          afterLoad(resource);
        }
      })
      .catch((err) => {
        bodyEl.innerHTML = `<p class="resource-status resource-error">Could not load ${resource}.<br><small>${err}</small></p>`;
        console.error('[resources] load failed:', resource, err);
      });
  }

  function afterLoad(resource) {
    searchInput.disabled = false;
    if (resource === 'spells') {
      searchInput.placeholder = 'Search by name…';
      buildClassFilter();
      buildSpellExtraFilters();
    } else if (resource === 'gods') {
      searchInput.placeholder = 'Search…';
      buildGodsFilters();
      buildGodsSort();
    } else if (resource === 'monsters') {
      searchInput.placeholder = 'Search by name…';
      buildMonsterFilters();
      buildMonstersSort();
    }
    searchInput.focus();
  }

  // ── Class filter (spells) ─────────────────────────────────────────────────
  function buildClassFilter() {
    const classes = new Set();
    bodyEl.querySelectorAll('dl.spell-stats dt').forEach((dt) => {
      if (dt.textContent.trim() === 'Classes') {
        const dd = dt.nextElementSibling;
        if (dd) dd.textContent.split(',').forEach((c) => {
          const t = c.trim(); if (t) classes.add(t);
        });
      }
    });
    classFilter.innerHTML = '<option value="">All classes</option>';
    [...classes].sort().forEach((cls) => {
      const opt = document.createElement('option');
      opt.value = cls; opt.textContent = cls;
      classFilter.appendChild(opt);
    });
    classFilter.hidden = false;
  }

  // ── Level + Source + Ritual filters (spells) ──────────────────────────────
  // Source groups: which sourcebook a spell came from, bucketed by publisher type.
  // Only groups/sources actually present in the loaded content are shown.
  const SOURCE_GROUPS = [
    ['Official Sourcebooks', [
      '5e Core Rules', "Player's Handbook", '2024 Player\'s Handbook',
      'Xanathar\'s Guide to Everything', 'Fizban\'s Treasury of Dragons',
    ]],
    ['3rd-Party / OGL', [
      'Kobold Press Compilation', 'Deep Magic 5e', 'Deep Magic Extended',
      'Tome of Heroes', 'Warlock Archives', 'Level Up Advanced 5e',
    ]],
    ['Homebrew / Other', ['Open5e Original Content']],
  ];

  function buildSpellExtraFilters() {
    // Level
    const levels = [];
    bodyEl.querySelectorAll('.spell-level-heading').forEach((h) => levels.push(h.textContent.trim()));
    const levelSel = makeSelect('All levels', levels);
    levelSel.setAttribute('aria-label', 'Filter by spell level');
    levelSel.addEventListener('change', applyFilter);
    searchRow.appendChild(levelSel);
    dynamicFilters.level = levelSel;

    // Source — grouped by publisher type, normalizing away the "(unconfirmed)" suffix
    const presentSources = new Set();
    bodyEl.querySelectorAll('.spell-entry').forEach((entry) => {
      const src = getSpellField(entry, 'Source').replace(/\s*\(unconfirmed\)\s*$/, '');
      if (src) presentSources.add(src);
    });

    const sourceSel = document.createElement('select');
    sourceSel.className = 'resource-extra-filter';
    sourceSel.setAttribute('aria-label', 'Filter by source');
    sourceSel.innerHTML = '<option value="">All sources</option>';
    SOURCE_GROUPS.forEach(([label, sources]) => {
      const present = sources.filter((s) => presentSources.has(s));
      if (!present.length) return;
      const grp = document.createElement('optgroup');
      grp.label = label;
      grp.appendChild(new Option(`— All ${label} —`, 'group:' + label));
      present.forEach((s) => grp.appendChild(new Option(s, s)));
      sourceSel.appendChild(grp);
    });
    sourceSel.addEventListener('change', applyFilter);
    searchRow.appendChild(sourceSel);
    dynamicFilters.source = sourceSel;

    // Ritual toggle
    const ritualLabel = document.createElement('label');
    ritualLabel.className = 'resource-ritual-toggle';
    ritualLabel.innerHTML = '<input type="checkbox" /> Ritual only';
    ritualLabel.querySelector('input').addEventListener('change', applyFilter);
    searchRow.appendChild(ritualLabel);
    dynamicFilters.ritual = ritualLabel;
  }

  // ── Alignment + Domain filters (gods) ─────────────────────────────────────
  const ALIGNMENT_LABELS = {
    LG: 'Lawful Good', NG: 'Neutral Good', CG: 'Chaotic Good',
    LN: 'Lawful Neutral', N: 'True Neutral', CN: 'Chaotic Neutral',
    LE: 'Lawful Evil', NE: 'Neutral Evil', CE: 'Chaotic Evil',
  };

  // Splits a 2-letter alignment code into its law/good axis letters.
  // True Neutral ("N") is neutral on both axes.
  function alignmentAxes(code) {
    if (code === 'N') return { law: 'N', good: 'N' };
    return { law: code[0], good: code[1] };
  }

  function buildGodsFilters() {
    const presentAlignments = new Set();
    const domains = new Set();
    bodyEl.querySelectorAll('.gods-table tbody tr').forEach((row) => {
      const cells = row.querySelectorAll('td');
      if (cells[2]) presentAlignments.add(cells[2].textContent.trim());
      if (cells[3]) cells[3].textContent.split(',').forEach((d) => {
        const t = d.trim(); if (t) domains.add(t);
      });
    });

    const alignSel = document.createElement('select');
    alignSel.className = 'resource-extra-filter';
    alignSel.setAttribute('aria-label', 'Filter by alignment');
    alignSel.innerHTML = '<option value="">All alignments</option>';

    const lawGroup = document.createElement('optgroup');
    lawGroup.label = 'Law axis';
    [['law:L', 'Any Lawful'], ['law:N', 'Any Neutral (Law axis)'], ['law:C', 'Any Chaotic']]
      .forEach(([val, label]) => lawGroup.appendChild(new Option(label, val)));
    alignSel.appendChild(lawGroup);

    const goodGroup = document.createElement('optgroup');
    goodGroup.label = 'Morality axis';
    [['good:G', 'Any Good'], ['good:N', 'Any Neutral (Morality axis)'], ['good:E', 'Any Evil']]
      .forEach(([val, label]) => goodGroup.appendChild(new Option(label, val)));
    alignSel.appendChild(goodGroup);

    const exactGroup = document.createElement('optgroup');
    exactGroup.label = 'Exact';
    Object.keys(ALIGNMENT_LABELS)
      .filter((code) => presentAlignments.has(code))
      .forEach((code) => exactGroup.appendChild(new Option(ALIGNMENT_LABELS[code], 'exact:' + code)));
    alignSel.appendChild(exactGroup);

    const domSel = makeSelect('All domains', [...domains].sort());
    domSel.setAttribute('aria-label', 'Filter by domain');

    alignSel.addEventListener('change', applyFilter);
    domSel.addEventListener('change',   applyFilter);

    searchRow.appendChild(alignSel);
    searchRow.appendChild(domSel);
    dynamicFilters.alignment = alignSel;
    dynamicFilters.domain    = domSel;
  }

  function makeSelect(placeholder, options) {
    const sel = document.createElement('select');
    sel.className = 'resource-extra-filter';
    sel.innerHTML = `<option value="">${placeholder}</option>`;
    options.forEach((val) => {
      const opt = document.createElement('option');
      opt.value = val; opt.textContent = val;
      sel.appendChild(opt);
    });
    return sel;
  }

  // ── Column sorting (gods) ─────────────────────────────────────────────────
  function buildGodsSort() {
    bodyEl.querySelectorAll('.gods-table th').forEach((th, i) => {
      th.classList.add('gods-th-sortable');
      th.addEventListener('click', () => sortGodsBy(i));
    });
  }

  function sortGodsBy(colIndex) {
    godsSort.dir = (godsSort.col === colIndex) ? godsSort.dir * -1 : 1;
    godsSort.col = colIndex;

    const tbody = bodyEl.querySelector('.gods-table tbody');
    const rows  = [...tbody.querySelectorAll('tr')];
    rows.sort((a, b) => {
      const aVal = (a.querySelectorAll('td')[colIndex]?.textContent || '').trim();
      const bVal = (b.querySelectorAll('td')[colIndex]?.textContent || '').trim();
      return aVal.localeCompare(bVal) * godsSort.dir;
    });
    rows.forEach((r) => tbody.appendChild(r));

    // Update sort indicators on headers
    bodyEl.querySelectorAll('.gods-table th').forEach((th, i) => {
      th.removeAttribute('data-sort');
      if (i === colIndex) th.setAttribute('data-sort', godsSort.dir === 1 ? 'asc' : 'desc');
    });

    // Re-apply active filters so hidden rows stay hidden after re-order
    applyFilter();
  }

  // ── Filtering ──────────────────────────────────────────────────────────────
  function applyFilter() {
    const query = searchInput.value.toLowerCase().trim();

    if (currentResource === 'spells') {
      const cls        = classFilter.hidden ? '' : classFilter.value;
      const level       = dynamicFilters.level  ? dynamicFilters.level.value  : '';
      const source      = dynamicFilters.source ? dynamicFilters.source.value : '';
      const ritualOnly  = dynamicFilters.ritual
        ? dynamicFilters.ritual.querySelector('input').checked : false;
      filterSpells(query, cls, level, source, ritualOnly);
    } else if (currentResource === 'gods') {
      const alignVal  = dynamicFilters.alignment ? dynamicFilters.alignment.value : '';
      const domainVal = dynamicFilters.domain    ? dynamicFilters.domain.value    : '';
      filterGods(query, alignVal, domainVal);
    } else if (currentResource === 'monsters') {
      const typeVal = dynamicFilters.monType ? dynamicFilters.monType.value : '';
      const sizeVal = dynamicFilters.monSize ? dynamicFilters.monSize.value : '';
      const crFrom  = dynamicFilters.crFrom  ? dynamicFilters.crFrom.value  : '';
      const crTo    = dynamicFilters.crTo    ? dynamicFilters.crTo.value    : '';
      const srcVal  = dynamicFilters.monSrc  ? dynamicFilters.monSrc.value  : '';
      filterMonsters(query, typeVal, sizeVal, crFrom, crTo, srcVal);
    }
  }

  function filterSpells(query, cls, level, source, ritualOnly) {
    let total = 0, visible = 0;
    bodyEl.querySelectorAll('.spell-entry').forEach((entry) => {
      total++;
      const name        = (entry.querySelector('h3.spell-name')?.textContent || '').toLowerCase();
      const nameMatch    = !query  || name.includes(query);
      const clsMatch     = !cls    || getSpellField(entry, 'Classes').includes(cls);
      const levelMatch   = !level  ||
        entry.closest('.spell-level-group')?.querySelector('.spell-level-heading')?.textContent.trim() === level;
      const entrySource  = getSpellField(entry, 'Source').replace(/\s*\(unconfirmed\)\s*$/, '');
      const sourceMatch  = matchesSourceFilter(entrySource, source);
      const ritualMatch  = !ritualOnly || getSpellField(entry, 'Ritual') === 'Yes';
      const show         = nameMatch && clsMatch && levelMatch && sourceMatch && ritualMatch;
      entry.hidden       = !show;
      if (show) visible++;
    });
    bodyEl.querySelectorAll('.spell-level-group').forEach((group) => {
      group.hidden = !group.querySelector('.spell-entry:not([hidden])');
    });
    const active = query || cls || level || source || ritualOnly;
    countEl.textContent = active ? `${visible} of ${total} spells` : '';
  }

  function filterGods(query, alignVal, domainVal) {
    let total = 0, visible = 0;
    bodyEl.querySelectorAll('.gods-table tbody tr').forEach((row) => {
      total++;
      const cells      = row.querySelectorAll('td');
      const alignment  = cells[2]?.textContent.trim() || '';
      const domains    = cells[3]?.textContent || '';
      const textMatch  = !query     || row.textContent.toLowerCase().includes(query);
      const alignMatch = matchesAlignmentFilter(alignment, alignVal);
      const domMatch   = !domainVal || domains.split(',').some((d) => d.trim() === domainVal);
      const show       = textMatch && alignMatch && domMatch;
      row.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    const active = query || alignVal || domainVal;
    countEl.textContent = active ? `${visible} of ${total} gods` : '';
  }

  // alignVal is one of: '' (any), 'law:L'/'law:N'/'law:C', 'good:G'/'good:N'/'good:E',
  // or 'exact:LG' etc. — see buildGodsFilters().
  function matchesAlignmentFilter(code, alignVal) {
    if (!alignVal) return true;
    const [axis, val] = alignVal.split(':');
    if (axis === 'exact') return code === val;
    const axes = alignmentAxes(code);
    if (axis === 'law')  return axes.law  === val;
    if (axis === 'good') return axes.good === val;
    return true;
  }

  // source is either '' (any), an exact source name, or 'group:<group label>'
  // (matches any source belonging to that publisher-type group) — see SOURCE_GROUPS.
  function matchesSourceFilter(entrySource, source) {
    if (!source) return true;
    if (source.startsWith('group:')) {
      const groupLabel = source.slice('group:'.length);
      const group = SOURCE_GROUPS.find(([label]) => label === groupLabel);
      return group ? group[1].includes(entrySource) : false;
    }
    return entrySource === source;
  }

  function getSpellField(entry, fieldName) {
    const dts = entry.querySelectorAll('dl.spell-stats dt');
    for (const dt of dts) {
      if (dt.textContent.trim() === fieldName) return (dt.nextElementSibling?.textContent || '').trim();
    }
    return '';
  }

  // ── Monster resource (shared data — not campaign-specific) ───────────────

  const MONSTER_ADVENTURE_SOURCES = new Set(['cos', 'lmop', 'dip', 'bgdia', 'pabtso']);

  function monCrDisplay(cr) {
    if (cr === undefined || cr === null) return '–';
    return typeof cr === 'object' ? (cr.cr || '–') : cr;
  }

  function monCrNumeric(cr) {
    const s = (typeof cr === 'object' ? cr.cr : cr) || '0';
    if (s === '1/8') return 0.125;
    if (s === '1/4') return 0.25;
    if (s === '1/2') return 0.5;
    const n = parseFloat(s);
    return isNaN(n) ? -1 : n;
  }

  function monTypeDisplay(type) {
    if (!type) return '';
    if (typeof type === 'string') return type.split('/').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join('/');
    if (type.swarmSize) return 'Swarm';
    if (Array.isArray(type.choose)) return type.choose.map(s => s.charAt(0).toUpperCase() + s.slice(1)).join('/');
    return monTypeDisplay(type.type || '');
  }

  // Phase 1: fetch lightweight index (~122 KB) → render list immediately.
  // Phase 2: fetch full stat blocks (6 MB) on first detail click, cached.
  function loadMonsters() {
    if (monstersLoaded) {
      buildMonsterList();
      afterLoad('monsters');
      return;
    }
    bodyEl.innerHTML = '<p class="resource-status">Loading monsters…</p>';
    bodyEl.scrollTop = 0;
    fetch('shared/data/monsters-index.json')
      .then((r) => { if (!r.ok) throw new Error(`HTTP ${r.status}`); return r.json(); })
      .then((data) => {
        monsterIndex   = data;
        monstersLoaded = true;
        if (!overlay.hidden && currentResource === 'monsters') {
          buildMonsterList();
          afterLoad('monsters');
        }
      })
      .catch((err) => {
        bodyEl.innerHTML = `<p class="resource-status resource-error">Could not load monsters.<br><small>${err}</small></p>`;
        console.error('[resources] monsters index load failed:', err);
      });
  }

  function buildMonsterList() {
    const rows = monsterIndex.map((m, idx) => {
      const cr   = monCrDisplay(m.cr);
      const type = monTypeDisplay(m.type);
      const size = monSizeDisplay(m.size);
      return `<tr data-midx="${idx}"><td>${m.name}</td><td class="mn-cr">${cr}</td><td class="mn-type">${type}</td><td class="mn-size">${size}</td><td class="mn-src">${m.source}</td></tr>`;
    }).join('');

    bodyEl.innerHTML = `
      <table class="monsters-table">
        <thead><tr><th>Name</th><th>CR</th><th>Type</th><th>Size</th><th>Source</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>`;

    bodyEl.querySelector('.monsters-table tbody').addEventListener('click', (e) => {
      const tr = e.target.closest('tr');
      if (!tr) return;
      openMonsterDetail(parseInt(tr.dataset.midx, 10));
    });

    detailPanel = document.createElement('div');
    detailPanel.id = 'monster-detail-panel';
    detailPanel.hidden = true;
    detailPanel.innerHTML = `<button class="monster-detail-back" type="button">← Monsters</button><div id="monster-detail-body"></div>`;
    detailPanel.querySelector('.monster-detail-back').addEventListener('click', closeMonsterDetail);
    bodyEl.appendChild(detailPanel);
  }

  const CR_VALUES = ['0','1/8','1/4','1/2','1','2','3','4','5','6','7','8','9','10',
    '11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'];

  const SIZE_OPTIONS = [['T','Tiny'],['S','Small'],['M','Medium'],['L','Large'],['H','Huge'],['G','Gargantuan']];
  const SIZE_MAP     = Object.fromEntries(SIZE_OPTIONS);
  const SIZE_RANK    = {T:0,S:1,M:2,L:3,H:4,G:5};

  function monSizeDisplay(size) {
    if (!size) return '';
    return size.split('').map(c => SIZE_MAP[c] || c).join('/');
  }

  function buildMonsterFilters() {
    // CR range: two selects with a dash separator, wrapped so they remove together
    const crWrap = document.createElement('span');
    crWrap.className = 'cr-range-wrap';

    const crFromSel = document.createElement('select');
    crFromSel.className = 'resource-extra-filter';
    crFromSel.setAttribute('aria-label', 'CR minimum');
    crFromSel.innerHTML = '<option value="">CR min</option>' +
      CR_VALUES.map(v => `<option value="${v}">${v}</option>`).join('');

    const crDash = document.createElement('span');
    crDash.className = 'cr-range-dash';
    crDash.textContent = '–';

    const crToSel = document.createElement('select');
    crToSel.className = 'resource-extra-filter';
    crToSel.setAttribute('aria-label', 'CR maximum');
    crToSel.innerHTML = '<option value="">CR max</option>' +
      CR_VALUES.map(v => `<option value="${v}">${v}</option>`).join('');

    crFromSel.addEventListener('change', () => {
      const fNum = crFromSel.value ? monCrNumeric(crFromSel.value) : -Infinity;
      const tNum = crToSel.value   ? monCrNumeric(crToSel.value)   :  Infinity;
      if (fNum > tNum) crToSel.value = '';
      applyFilter();
    });
    crToSel.addEventListener('change', () => {
      const fNum = crFromSel.value ? monCrNumeric(crFromSel.value) : -Infinity;
      const tNum = crToSel.value   ? monCrNumeric(crToSel.value)   :  Infinity;
      if (fNum > tNum) crFromSel.value = '';
      applyFilter();
    });

    crWrap.appendChild(crFromSel);
    crWrap.appendChild(crDash);
    crWrap.appendChild(crToSel);
    searchRow.appendChild(crWrap);
    dynamicFilters.crWrap = crWrap;
    dynamicFilters.crFrom = crFromSel;
    dynamicFilters.crTo   = crToSel;

    const types = new Set();
    monsterIndex.forEach((m) => { const t = monTypeDisplay(m.type); if (t) types.add(t); });
    const typeSel = makeSelect('All types', [...types].sort());
    typeSel.setAttribute('aria-label', 'Filter by monster type');
    typeSel.addEventListener('change', applyFilter);
    searchRow.appendChild(typeSel);
    dynamicFilters.monType = typeSel;

    const sizeSel = document.createElement('select');
    sizeSel.className = 'resource-extra-filter';
    sizeSel.setAttribute('aria-label', 'Filter by size');
    sizeSel.innerHTML = '<option value="">All sizes</option>' +
      SIZE_OPTIONS.map(([code, label]) => `<option value="${code}">${label}</option>`).join('');
    sizeSel.addEventListener('change', applyFilter);
    searchRow.appendChild(sizeSel);
    dynamicFilters.monSize = sizeSel;

    const srcSel = makeSelect('All sources', ['Core Books', 'Adventures']);
    srcSel.setAttribute('aria-label', 'Filter by source type');
    srcSel.addEventListener('change', applyFilter);
    searchRow.appendChild(srcSel);
    dynamicFilters.monSrc = srcSel;
  }

  function buildMonstersSort() {
    bodyEl.querySelectorAll('.monsters-table th').forEach((th, i) => {
      th.classList.add('monsters-th-sortable');
      if (i === monstersSort.col) th.setAttribute('data-sort', monstersSort.dir === 1 ? 'asc' : 'desc');
      th.addEventListener('click', () => sortMonstersBy(i));
    });
  }

  function sortMonstersBy(colIndex) {
    monstersSort.dir = (monstersSort.col === colIndex) ? monstersSort.dir * -1 : 1;
    monstersSort.col = colIndex;

    const tbody = bodyEl.querySelector('.monsters-table tbody');
    if (!tbody) return;
    const rows = [...tbody.querySelectorAll('tr')];

    rows.sort((a, b) => {
      const am = monsterIndex[parseInt(a.dataset.midx, 10)];
      const bm = monsterIndex[parseInt(b.dataset.midx, 10)];
      let cmp = 0;
      switch (colIndex) {
        case 0: cmp = am.name.localeCompare(bm.name); break;
        case 1: cmp = monCrNumeric(am.cr) - monCrNumeric(bm.cr); break;
        case 2: cmp = monTypeDisplay(am.type).localeCompare(monTypeDisplay(bm.type)); break;
        case 3: cmp = (SIZE_RANK[am.size?.[0]] ?? 99) - (SIZE_RANK[bm.size?.[0]] ?? 99); break;
        case 4: cmp = am.source.localeCompare(bm.source); break;
      }
      return cmp * monstersSort.dir;
    });

    rows.forEach((r) => tbody.appendChild(r));

    bodyEl.querySelectorAll('.monsters-table th').forEach((th, i) => {
      th.removeAttribute('data-sort');
      if (i === colIndex) th.setAttribute('data-sort', monstersSort.dir === 1 ? 'asc' : 'desc');
    });

    applyFilter();
  }

  function safeMonsterFilename(name) {
    return name.replace(/[\\/:*?"<>|]/g, '_');
  }

  function openTokenLightbox(src, name) {
    let lb = document.getElementById('monster-token-lightbox');
    if (!lb) {
      lb = document.createElement('div');
      lb.id = 'monster-token-lightbox';
      lb.hidden = true;
      lb.innerHTML = '<img alt="">';
      lb.addEventListener('click', () => { lb.hidden = true; });
      document.body.appendChild(lb);
    }
    lb.querySelector('img').src = src;
    lb.querySelector('img').alt = name;
    lb.hidden = false;
  }

  function renderMonsterStatBlock(m, bodyEl) {
    bodyEl.innerHTML = window.MonsterRenderer.buildStatBlock(m);
    // Token image: floated right inside the stat block; removed silently if not found locally
    const sbInner = bodyEl.querySelector('.sb-inner');
    if (sbInner) {
      const img = document.createElement('img');
      img.className = 'monster-token-img';
      img.alt = m.name;
      img.src = `shared/img/monsters/${m.source}/${safeMonsterFilename(m.name)}.webp`;
      img.onerror = () => img.remove();
      img.addEventListener('click', (e) => { e.stopPropagation(); openTokenLightbox(img.src, m.name); });
      sbInner.insertBefore(img, sbInner.firstChild);
    }
  }

  function openMonsterDetail(idx) {
    if (!detailPanel) return;
    pendingDetailIdx = idx; // track most recent click for when full data arrives
    detailPanel.hidden = false;
    modalEl.classList.add('monster-detail-open');
    const body = detailPanel.querySelector('#monster-detail-body');
    if (!body) return;

    if (allMonsters) {
      const m = allMonsters[idx];
      if (m && window.MonsterRenderer) {
        renderMonsterStatBlock(m, body);
        detailPanel.scrollTop = 0; // after DOM write to avoid forced reflow
      }
      return;
    }

    body.innerHTML = '<p class="resource-status" style="padding:1.5rem;text-align:center">Loading stat block…</p>';
    detailPanel.scrollTop = 0;
    if (monstersFullLoading) return; // fetch already in flight; will render via pendingDetailIdx

    monstersFullLoading = true;
    fetch('shared/data/monsters-raw.json')
      .then((r) => { if (!r.ok) throw new Error(`HTTP ${r.status}`); return r.json(); })
      .then((data) => {
        allMonsters = data;
        monstersFullLoading = false;
        if (detailPanel && !detailPanel.hidden && window.MonsterRenderer) {
          const m = allMonsters[pendingDetailIdx];
          const liveBody = detailPanel.querySelector('#monster-detail-body');
          if (m && liveBody) {
            renderMonsterStatBlock(m, liveBody);
            detailPanel.scrollTop = 0;
          }
        }
      })
      .catch((err) => {
        monstersFullLoading = false;
        if (detailPanel && !detailPanel.hidden) {
          const liveBody = detailPanel.querySelector('#monster-detail-body');
          if (liveBody) liveBody.innerHTML = `<p class="resource-status resource-error">Could not load stat block.<br><small>${err}</small></p>`;
        }
        console.error('[resources] monsters full load failed:', err);
      });
  }

  function closeMonsterDetail() {
    modalEl.classList.remove('monster-detail-open');
    if (detailPanel) {
      detailPanel.hidden = true;
      detailPanel.scrollTop = 0;
    }
  }

  function filterMonsters(query, typeVal, sizeVal, crFrom, crTo, srcVal) {
    let total = 0, visible = 0;
    const fromNum = crFrom ? monCrNumeric(crFrom) : -Infinity;
    const toNum   = crTo   ? monCrNumeric(crTo)   :  Infinity;
    bodyEl.querySelectorAll('.monsters-table tbody tr').forEach((tr) => {
      total++;
      const m         = monsterIndex[parseInt(tr.dataset.midx, 10)];
      const nameMatch = !query   || m.name.toLowerCase().includes(query);
      const typeMatch = !typeVal || monTypeDisplay(m.type) === typeVal;
      const sizeMatch = !sizeVal || (m.size || '').includes(sizeVal);
      const crNum     = monCrNumeric(m.cr);
      const crMatch   = crNum >= fromNum && crNum <= toNum;
      const isAdv     = MONSTER_ADVENTURE_SOURCES.has((m.source || '').toLowerCase());
      const srcMatch  = !srcVal  || (srcVal === 'Adventures' ? isAdv : !isAdv);
      const show = nameMatch && typeMatch && sizeMatch && crMatch && srcMatch;
      tr.hidden = !show;
      if (show) visible++;
    });
    const active = query || typeVal || sizeVal || crFrom || crTo || srcVal;
    countEl.textContent = active ? `${visible} of ${total} monsters` : '';
  }

  window.openResourceModal = openResourceModal;
})();
