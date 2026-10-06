// dashboard.js — Location-centric dashboard.
//
// Which view renders depends on App.getCurrentLocationId():
//   • a location id                   → that location's 4 quadrants (below)
//   • null + campaign.json `regions`  → the Regions home: one column per region
//   • null, no `regions`              → the campaign's rootLocation, as before
//
// Location view (always 2×2):
//   TL: Locations   — related locations
//   TR: People      — NPCs by category, Creatures, Factions
//   BL: Environment — atmosphere text from entity.environment + related items
//   BR: Curiosities — entity.curiosities roll-entries + Mysteries + DM Notes
//
// Data hooks on location entities (all optional):
//   environment: { architecture, activity, sensory, flora, lighting, weather }
//   curiosities: [{ roll: "Perception DC 14", detail: "…" }, …]
//
// Forward + reverse relationship lookup populates People/Environment/Curiosities
// from the entity graph automatically — no duplication needed.
//
// Regions (campaign.json → regions: ["hub_id", { id, label }, …]):
//   A region is a hub location. Every other location belongs to the region
//   whose hub is the fewest location-to-location links away. Locations no hub
//   reaches are listed under "Elsewhere" so nothing is ever unreachable.
//
// The header also carries the party marker — where the party is (state.js),
// which is separate from the location being looked at.

(function () {

  // ── Data helpers ──────────────────────────────────────────────────────────

  // Union of forward (loc.related[]) and reverse (entities that point to loc).
  function getGraph(locationId) {
    const loc = window.App.byId(locationId);
    if (!loc) return [];
    const forward = (loc.related || [])
      .map((id) => window.App.byId(id))
      .filter((e) => e && e.id !== locationId && window.App.isVisible(e));
    const seen = new Set(forward.map((e) => e.id));
    for (const e of window.ENTITIES) {
      if (e.id === locationId || seen.has(e.id) || !window.App.isVisible(e)) continue;
      if ((e.related || []).includes(locationId)) { seen.add(e.id); forward.push(e); }
    }
    return forward;
  }

  function groupBy(arr, key) {
    const out = {};
    for (const item of arr) { const k = item[key] || ''; (out[k] = out[k] || []).push(item); }
    return out;
  }

  // Pure: takes the entity list and the campaign's `regions` config, returns
  //   regions  — [{ id, hub, label }] in config order (unresolvable ids dropped)
  //   regionOf — Map(locationId → region id)
  //   orphans  — location entities no hub reaches
  // Visibility is NOT applied here, so membership is the same for DM and
  // players; callers filter what they show.
  function buildRegionModel(entities, regionsCfg) {
    const locs = entities.filter((e) => e.type === 'location');
    const byId = new Map(locs.map((e) => [e.id, e]));

    const regions = [];
    for (const r of regionsCfg || []) {
      const id  = typeof r === 'string' ? r : r && r.id;
      const hub = byId.get(id);
      if (!hub || regions.some((x) => x.id === id)) continue;
      regions.push({ id, hub, label: (r && r.label) || hub.name });
    }

    const adj = new Map(locs.map((e) => [e.id, new Set()]));
    for (const e of locs) {
      for (const ref of e.related || []) {
        if (ref === e.id || !byId.has(ref)) continue;
        adj.get(e.id).add(ref);
        adj.get(ref).add(e.id);
      }
    }

    // Breadth-first from every hub at once. Hubs are queued in config order,
    // so a location equally near two hubs goes to the earlier region.
    const regionOf = new Map();
    const queue    = [];
    for (const r of regions) { regionOf.set(r.id, r.id); queue.push(r.id); }
    for (let i = 0; i < queue.length; i++) {
      const cur = queue[i];
      for (const next of adj.get(cur)) {
        if (regionOf.has(next)) continue;
        regionOf.set(next, regionOf.get(cur));
        queue.push(next);
      }
    }

    return { regions, regionOf, orphans: locs.filter((e) => !regionOf.has(e.id)) };
  }

  // The party's location, but only if this viewer is allowed to see it.
  function visibleParty() {
    const party = window.App.getPartyLocation();
    return party && window.App.isVisible(party) ? party : null;
  }

  // ── DOM helpers ───────────────────────────────────────────────────────────

  function el(tag, cls, text) {
    const n = document.createElement(tag);
    if (cls)            n.className   = cls;
    if (text !== undefined) n.textContent = text;
    return n;
  }

  // A quadrant: header title bar + scrollable body. Returns the element;
  // content is added to .quad.body.
  function makeQuad(title, extraClass) {
    const quad  = el('div', 'dash-quad' + (extraClass ? ' ' + extraClass : ''));
    quad.header = el('div', 'dash-quad-header', title);
    quad.appendChild(quad.header);
    const body  = el('div', 'dash-quad-body');
    quad.appendChild(body);
    quad.body   = body;
    return quad;
  }

  // A labelled sub-group within a quad body.
  function makeSubSection(title) {
    const sec = el('div', 'dash-subsection');
    sec.appendChild(el('div', 'dash-subsection-title', title));
    return sec;
  }

  function makeEmpty(msg) { return el('p', 'dash-empty', msg); }

  // ── Card renderers ────────────────────────────────────────────────────────

  function makeEntityCard(entity) {
    const card = el('div', 'dash-entity-card');
    if (entity.visibility === 'dm-only') card.classList.add('dash-entity-dm');
    const link = el('a', 'dash-entity-name', entity.name);
    link.href = '#';
    link.addEventListener('click', (e) => { e.preventDefault(); window.openLocationModal(entity); });
    card.appendChild(link);
    if (entity.category) card.appendChild(el('span', 'dash-entity-cat', entity.category));
    return card;
  }

  function makeLocCard(loc) {
    const card = el('div', 'dash-loc-card');
    card.title = 'Enter ' + loc.name;
    card.dataset.loc = loc.id;
    const name = el('span', 'dash-loc-card-name', loc.name);
    card.appendChild(name);
    const party = visibleParty();
    if (party && party.id === loc.id) {
      card.classList.add('dash-loc-card-party');
      card.appendChild(el('span', 'dash-party-flag', '⚑ Party'));
    }
    if (loc.category) card.appendChild(el('span', 'dash-loc-card-cat', loc.category));
    const count = (loc.related || []).length;
    if (count) card.appendChild(el('span', 'dash-loc-card-hint', count + ' linked'));
    card.addEventListener('click', () => window.App.setCurrentLocation(loc.id));
    return card;
  }

  // ── Quadrant builders ─────────────────────────────────────────────────────

  // Preferred category order for the campus root locations quadrant.
  const LOC_CAT_ORDER = [
    'Departments',
    'Central Campus Facilities',
    'Special Facilities',
    'Underground Infrastructure',
    'Remote Field Sites',
    'Founding-Era & Lore',
    'Nearby World',
  ];

  // Location cards grouped by category, alphabetical within each. Returns
  // false if there was nothing to add.
  function appendLocationGroups(body, locs) {
    const groups = groupBy(locs, 'category');
    const keys   = [
      ...LOC_CAT_ORDER.filter((k) => groups[k]),
      ...Object.keys(groups).filter((k) => !LOC_CAT_ORDER.includes(k)).sort(),
    ];
    for (const cat of keys) {
      const sec = makeSubSection(cat || 'Locations');
      const sorted = [...groups[cat]].sort((a, b) => a.name.localeCompare(b.name));
      for (const loc of sorted) sec.appendChild(makeLocCard(loc));
      body.appendChild(sec);
    }
    return keys.length > 0;
  }

  function makeLocationsQuad(graphLocs) {
    const quad = makeQuad('Locations');
    if (!appendLocationGroups(quad.body, graphLocs)) {
      quad.body.appendChild(makeEmpty('No locations linked. Add location ids to the related[] array on this entity.'));
    }
    return quad;
  }

  function makePeopleQuad(entities) {
    const quad     = makeQuad('People & Creatures');
    const npcs     = entities.filter((e) => e.type === 'npc');
    const creatures= entities.filter((e) => e.type === 'creature');
    const factions = entities.filter((e) => e.type === 'faction');
    let any = false;

    const byName = (a, b) => a.name.localeCompare(b.name);
    if (npcs.length) {
      any = true;
      const groups = groupBy(npcs, 'category');
      for (const cat of Object.keys(groups).sort()) {
        const sec = makeSubSection(cat || 'People');
        for (const e of [...groups[cat]].sort(byName)) sec.appendChild(makeEntityCard(e));
        quad.body.appendChild(sec);
      }
    }
    if (creatures.length) {
      any = true;
      const sec = makeSubSection('Creatures');
      for (const e of [...creatures].sort(byName)) sec.appendChild(makeEntityCard(e));
      quad.body.appendChild(sec);
    }
    if (factions.length) {
      any = true;
      const sec = makeSubSection('Factions');
      for (const e of [...factions].sort(byName)) sec.appendChild(makeEntityCard(e));
      quad.body.appendChild(sec);
    }
    if (!any) quad.body.appendChild(makeEmpty('No people or creatures linked to this location.'));
    return quad;
  }

  function makeEnvironmentQuad(loc, graphItems) {
    const quad  = makeQuad('Environment', 'quad-environment');
    const env   = loc?.environment;
    const items = graphItems.filter((e) => e.type === 'item');
    let any = false;

    if (env) {
      any = true;
      const FIELDS = [
        ['architecture', 'Architecture'],
        ['activity',     'Activity'    ],
        ['sensory',      'Sensory'     ],
        ['flora',        'Flora'       ],
        ['lighting',     'Lighting'    ],
        ['weather',      'Weather'     ],
      ];
      for (const [key, label] of FIELDS) {
        if (!env[key]) continue;
        const block = el('div', 'env-block');
        block.appendChild(el('div', 'env-label', label));
        block.appendChild(el('p',   'env-text',  env[key]));
        quad.body.appendChild(block);
      }
    }

    if (items.length) {
      any = true;
      const sec = makeSubSection('Notable Objects');
      for (const e of items) sec.appendChild(makeEntityCard(e));
      quad.body.appendChild(sec);
    }

    if (!any) {
      quad.body.appendChild(makeEmpty(
        'Add an "environment" object to this location\'s JSON to describe what the party sees, hears, and smells. ' +
        'Keys: architecture · activity · sensory · flora · lighting · weather'
      ));
    }
    return quad;
  }

  function timeVisible(entry) {
    if (!entry.time || !entry.time.length) return true;
    return entry.time.includes(window.App.getTimeOfDay());
  }

  function makeCuriositiesQuad(loc, graphEntities) {
    const quad       = makeQuad('Curiosities', 'quad-curiosities');
    const allCuriosities = loc?.curiosities || [];
    const curiosities    = allCuriosities.filter(timeVisible);
    const mysteries  = graphEntities.filter((e) => e.type === 'mystery');
    const sessions   = graphEntities.filter((e) => e.type === 'session');
    let any = false;

    if (curiosities.length) {
      any = true;
      const sec = makeSubSection('Observations');
      for (const c of curiosities) {
        const row = el('div', 'curiosity-item');
        if (c.roll) row.appendChild(el('span', 'curiosity-roll', c.roll));
        row.appendChild(el('p', 'curiosity-detail', c.detail));
        sec.appendChild(row);
      }
      quad.body.appendChild(sec);
    }

    const byName = (a, b) => a.name.localeCompare(b.name);
    if (mysteries.length) {
      any = true;
      const sec = makeSubSection('Mysteries');
      for (const e of [...mysteries].sort(byName)) sec.appendChild(makeEntityCard(e));
      quad.body.appendChild(sec);
    }
    if (sessions.length) {
      any = true;
      const sec = makeSubSection('Sessions');
      for (const e of [...sessions].sort(byName)) sec.appendChild(makeEntityCard(e));
      quad.body.appendChild(sec);
    }

    if (!any) {
      quad.body.appendChild(makeEmpty(
        'Add a "curiosities" array to this location\'s JSON for perception/insight discoveries. ' +
        'Each entry: { "roll": "Perception DC 14", "detail": "…" }'
      ));
    }

    // DM notes appear at the bottom of Curiosities when a specific location is active.
    if (window.App.isDM() && loc) {
      const sec = makeSubSection('DM Notes');
      sec.classList.add('dash-notes-section');
      const ta = el('textarea', 'dash-notes-ta');
      ta.placeholder = 'Session notes for this location…';
      ta.value = window.App.getNote(loc.id);
      let timer;
      ta.addEventListener('input', () => {
        clearTimeout(timer);
        timer = setTimeout(() => window.App.setNote(loc.id, ta.value), 400);
      });
      sec.appendChild(ta);
      quad.body.appendChild(sec);
    }

    return quad;
  }

  // ── Header ────────────────────────────────────────────────────────────────

  // view: { isHome, isRoot, loc, region }
  //   isHome — the Regions home (no location selected, regions configured)
  //   isRoot — legacy: the campaign's rootLocation standing in as home
  //   region — the region `loc` belongs to, if any
  function makeHeader(view) {
    const { isHome, isRoot, loc, region } = view;
    const hdr = el('div', 'dash-location-header');

    if (!isHome && !isRoot) {
      const back = el('button', 'loc-bar-back', '← Home');
      back.addEventListener('click', () => window.App.clearLocation());
      hdr.appendChild(back);

      // One step up: from a location inside a region to that region's hub.
      if (region && region.id !== loc.id && window.App.isVisible(region.hub)) {
        const up = el('button', 'loc-bar-back loc-bar-region', '‹ ' + region.label);
        up.title = 'Up to ' + region.hub.name;
        up.addEventListener('click', () => window.App.setCurrentLocation(region.id));
        hdr.appendChild(up);
      }
    }

    const atTop = isHome || isRoot;
    hdr.appendChild(el('h2', 'dash-location-title', atTop ? window.CAMPAIGN.name : loc.name));

    const meta = el('div', 'dash-location-meta');
    meta.textContent = isHome ? 'Select a region or a location'
      : isRoot ? 'Select a location to enter it'
      : (['LOCATION', loc && loc.category].filter(Boolean).join(' · '));
    hdr.appendChild(meta);

    appendPartyControls(hdr, loc);
    hdr.appendChild(makeTimeToggle());

    if (!atTop && loc && loc.contentFile) {
      const btn = el('button', 'dash-detail-btn', 'Full Entry →');
      btn.addEventListener('click', () => window.openLocationModal(loc));
      hdr.appendChild(btn);
    }
    return hdr;
  }

  // Party marker + (DM only) the control that moves the party to this view.
  //   viewing the party's location → a static "Party is here" marker
  //   viewing anywhere else        → a button that snaps the view back to them
  function appendPartyControls(hdr, loc) {
    const party = visibleParty();
    const here  = !!(party && loc && party.id === loc.id);

    if (here) {
      hdr.appendChild(el('span', 'dash-party-chip dash-party-here', '⚑ Party is here'));
    } else if (party) {
      const jump = el('button', 'dash-party-chip dash-party-jump', '⚑ Party: ' + party.name);
      jump.title = 'Back to the party';
      jump.addEventListener('click', () => window.App.setCurrentLocation(party.id));
      hdr.appendChild(jump);
    }

    if (window.App.isDM() && loc && loc.type === 'location' && !here) {
      const set = el('button', 'dash-party-chip dash-party-set', 'Set party here');
      set.title = 'Move the party to ' + loc.name;
      set.addEventListener('click', () => window.App.setPartyLocation(loc.id));
      hdr.appendChild(set);
    }
  }

  // ── Time of day ───────────────────────────────────────────────────────────

  const TIME_SLOTS = [
    { id: 'dawn',  label: '◐ Dawn'  },
    { id: 'day',   label: '○ Day'   },
    { id: 'dusk',  label: '◑ Dusk'  },
    { id: 'night', label: '● Night' },
  ];

  function makeTimeToggle() {
    const wrap = el('div', 'loc-bar-time');
    const current = window.App.getTimeOfDay();
    for (const slot of TIME_SLOTS) {
      const btn = el('button', 'loc-time-btn' + (slot.id === current ? ' loc-time-active' : ''), slot.label);
      btn.dataset.time = slot.id;
      btn.addEventListener('click', () => {
        if (window.App.getTimeOfDay() !== slot.id) window.App.setTimeOfDay(slot.id);
      });
      wrap.appendChild(btn);
    }
    return wrap;
  }

  // ── Map widget ────────────────────────────────────────────────────────────

  function makeMapWidget(entity, skipRevealCheck) {
    if (!entity) return null;
    if (skipRevealCheck) {
      if (entity.visibility === 'dm-only' && !window.App.isDM()) return null;
    } else {
      if (!window.App.isVisible(entity)) return null;
    }
    const src  = window.CAMPAIGN_BASE + '/' + entity.contentFile;
    const wrap = el('div', 'dash-region-map');
    wrap.title = 'Click to open — ' + entity.name;
    wrap.style.cursor = 'zoom-in';
    const img = el('img');
    img.src = src;
    img.alt = entity.name;
    wrap.appendChild(img);
    wrap.addEventListener('click', () => window.openImageModal(src, entity.name));
    return wrap;
  }

  function makeRegionMap() {
    const entity = window.App.byId(window.CAMPAIGN.regionMapEntity);
    // Region map bypasses reveal — always shown if player-visible.
    return makeMapWidget(entity, true);
  }

  // For non-root locations: pick the DM map if in DM mode, else player map.
  function makeLocationMap(graph) {
    const images = graph.filter((e) => e.type === 'image');
    if (!images.length) return null;
    const entity = window.App.isDM()
      ? (images.find((e) => e.visibility === 'dm-only') || images[0])
      : images[0];
    return makeMapWidget(entity);
  }

  // ── Regions home ──────────────────────────────────────────────────────────

  // One column per region: the hub (click to enter) and the locations linked
  // straight from it. Deeper locations are reached by entering, same as any
  // other location view — this is a way in, not a flat list of everything.
  function makeRegionsHome(model) {
    const row   = el('div', 'dash-row');
    const party = visibleParty();
    const partyRegion = party ? model.regionOf.get(party.id) : null;

    for (const region of model.regions) {
      if (!window.App.isVisible(region.hub)) continue;
      const quad = makeQuad(region.label, 'quad-region');
      quad.dataset.region = region.id;
      if (partyRegion === region.id) {
        quad.classList.add('quad-region-party');
        quad.header.appendChild(el('span', 'dash-party-flag', '⚑ Party'));
      }

      const enter = makeLocCard(region.hub);
      enter.classList.add('dash-region-enter');
      enter.querySelector('.dash-loc-card-hint')?.remove();
      enter.querySelector('.dash-loc-card-cat')?.remove();
      enter.appendChild(el('span', 'dash-loc-card-hint', 'Enter →'));
      quad.body.appendChild(enter);

      const linked = getGraph(region.id).filter(
        (e) => e.type === 'location' && model.regionOf.get(e.id) === region.id
      );
      appendLocationGroups(quad.body, linked);
      row.appendChild(quad);
    }

    const orphans = model.orphans.filter((e) => window.App.isVisible(e));
    if (orphans.length) {
      const quad = makeQuad('Elsewhere', 'quad-region quad-elsewhere');
      appendLocationGroups(quad.body, orphans);
      row.appendChild(quad);
    }

    if (!row.children.length) {
      const quad = makeQuad('Regions', 'quad-region');
      quad.body.appendChild(makeEmpty('Nowhere has been discovered yet.'));
      row.appendChild(quad);
    }

    if (window.CAMPAIGN.regionMapEntity) {
      const mapEl = makeRegionMap();
      if (mapEl) row.appendChild(mapEl);
    }
    return row;
  }

  // ── Main render ───────────────────────────────────────────────────────────

  function render() {
    const dash = document.getElementById('dashboard');
    if (!dash) return;

    const ROOT       = window.CAMPAIGN.rootLocation;
    const model      = buildRegionModel(window.ENTITIES, window.CAMPAIGN.regions);
    const hasRegions = model.regions.length > 0;

    let currentId = window.App.getCurrentLocationId();
    let loc       = currentId ? window.App.byId(currentId) : null;
    // Fall back to the home view if the stored location can't be resolved —
    // entities may not have loaded yet, or a saved id may point at an entity
    // that has since been renamed or removed. Rendering a header for an
    // undefined entity throws and takes the whole dashboard down with it.
    // Likewise a location this viewer may not see: the DM can leave the view
    // on a dm-only location and then switch to Player View.
    if (!loc || !window.App.isVisible(loc)) { currentId = null; loc = null; }

    // No regions configured: the root location stands in as the home view.
    const isHome = !currentId && hasRegions;
    if (!currentId && !hasRegions) {
      currentId = ROOT;
      loc       = window.App.byId(ROOT);
    }
    const isRoot = !hasRegions && currentId === ROOT;
    const region = loc ? model.regions.find((r) => r.id === model.regionOf.get(loc.id)) : null;

    dash.innerHTML = '';
    dash.appendChild(makeHeader({ isHome, isRoot, loc, region }));

    const quads = el('div', 'dash-quadrants');

    if (isHome) {
      quads.appendChild(makeRegionsHome(model));
      dash.appendChild(quads);
      return;
    }

    const graph  = getGraph(currentId);
    const topRow = el('div', 'dash-row');
    topRow.appendChild(makeLocationsQuad(graph.filter((e) => e.type === 'location')));
    topRow.appendChild(makePeopleQuad(graph));
    quads.appendChild(topRow);

    const botRow = el('div', 'dash-row');
    botRow.appendChild(makeEnvironmentQuad(loc, graph));
    if (isRoot && window.CAMPAIGN.regionMapEntity) {
      const mapEl = makeRegionMap();
      if (mapEl) botRow.appendChild(mapEl);
    } else if (!isRoot) {
      const mapEl = makeLocationMap(graph);
      if (mapEl) botRow.appendChild(mapEl);
    }
    botRow.appendChild(makeCuriositiesQuad(loc, graph));
    quads.appendChild(botRow);

    dash.appendChild(quads);
  }

  // No listener for party:changed — moving the party always moves the view
  // too (state.js), so location:changed already covers it.
  document.addEventListener('entities:ready',   render);
  document.addEventListener('location:changed', render);
  document.addEventListener('dm:changed',       render);
  document.addEventListener('campaign:changed', render);
  document.addEventListener('time:changed',     render);

  // Test hook — exposes pure logic for tools/tests.html.
  window._dashTest = { buildRegionModel };
})();
