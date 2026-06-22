// data.js — loads campaign config + entity data.
//
// window.CAMPAIGN is set synchronously at startup (so scripts loaded after
// this file — state.js, dashboard.js, etc. — can read it immediately without
// waiting for the async fetch). campaign.json is then fetched to override any
// of those defaults, letting a repo fork configure the app by editing only
// campaign.json rather than touching JS files.
//
// Exposes:
//   window.CAMPAIGN                  campaign configuration object
//   window.ENTITIES                  merged array of all entity objects
//   window.App.isDM()                is DM mode currently on?
//   window.App.setDM(on)             set DM mode, fires `dm:changed`
//   window.App.toggleDM()            flip DM mode
//   window.App.isVisible(entity)     should this entity show right now?
//   window.App.byId(id)              look up an entity by id (or undefined)
//
// Events dispatched on `document`:
//   entities:ready  { entities }     data finished loading
//   dm:changed      { on }           DM mode toggled

(function () {
  // ── Campaign config ────────────────────────────────────────────────────────
  // Synchronous defaults — scripts that load immediately after data.js (state.js,
  // dashboard.js) can read window.CAMPAIGN without waiting for a fetch.
  window.CAMPAIGN = {
    id:           'fail-academy',
    name:         'FAIL Academy',
    subtitle:     'Faculty of Arms, Inquiry & Lore',
    mapImage:     'assets/FUCKS_map.png',
    rootLocation: 'campus_root',
    storageKey:   'fail-academy.v1',
  };

  function applyConfig(cfg) {
    Object.assign(window.CAMPAIGN, cfg);
    document.title = window.CAMPAIGN.name + ' — Campaign Dossier';
    const h1  = document.querySelector('#topbar h1');
    const sub = document.querySelector('#topbar .subtitle');
    if (h1)  h1.textContent  = window.CAMPAIGN.name;
    if (sub) sub.textContent = window.CAMPAIGN.subtitle;
  }

  // Fetch campaign.json to override defaults (non-fatal if missing).
  fetch('campaign.json')
    .then((r) => (r.ok ? r.json() : {}))
    .then((cfg) => applyConfig(cfg))
    .catch(() => applyConfig({}));

  // ── Entity loading ─────────────────────────────────────────────────────────
  window.ENTITIES = [];
  let byIdMap = new Map();

  window.App = {
    isDM() {
      return document.body.classList.contains('dm-on');
    },
    setDM(on) {
      document.body.classList.toggle('dm-on', !!on);
      document.dispatchEvent(
        new CustomEvent('dm:changed', { detail: { on: !!on } })
      );
    },
    toggleDM() {
      this.setDM(!this.isDM());
    },
    isVisible(entity) {
      return entity.visibility !== 'dm-only' || this.isDM();
    },
    byId(id) {
      return byIdMap.get(id);
    },
  };

  function announce(entities) {
    window.ENTITIES = entities;
    byIdMap = new Map(entities.map((e) => [e.id, e]));
    document.dispatchEvent(
      new CustomEvent('entities:ready', { detail: { entities } })
    );
    console.info(`[data] Loaded ${entities.length} entit(ies).`);
  }

  function fail(err) {
    console.error(
      '[data] Could not load entity data.\n' +
        'If you opened index.html by double-clicking, your browser may be ' +
        'blocking local file access. Run the bundled server instead ' +
        '(start-map.bat) and open http://localhost:8000/.\n' +
        'Original error:',
      err
    );
    const banner = document.getElementById('load-error');
    if (banner) banner.hidden = false;
  }

  // Load the manifest, then every file it lists. A missing/broken individual
  // file is skipped (logged) rather than failing the whole load.
  fetch('data/index.json')
    .then((res) => {
      if (!res.ok) throw new Error(`index.json HTTP ${res.status}`);
      return res.json();
    })
    .then((files) => {
      if (!Array.isArray(files)) throw new Error('index.json is not an array');
      return Promise.all(
        files.map((fn) =>
          fetch(`data/${fn}`)
            .then((r) => {
              if (!r.ok) throw new Error(`HTTP ${r.status}`);
              return r.json();
            })
            .then((arr) => {
              if (!Array.isArray(arr)) throw new Error('not an array');
              return arr;
            })
            .catch((e) => {
              console.warn(`[data] Skipped data/${fn}:`, e.message);
              return [];
            })
        )
      );
    })
    .then((groups) => announce(groups.flat()))
    .catch(fail);
})();
