// state.js — persistent campaign state via localStorage.
//
// Shape (key determined by campaign.json → storageKey, e.g. "lost-mine.v1"):
//   { revealed: { "<id>": true }, notes: { "<id>": "..." },
//     baselineSeeded: { "<id>": true },
//     currentLocationId: string|null, partyLocationId: string|null,
//     timeOfDay: "dawn"|"day"|"dusk"|"night" }
//
// `baselineSeeded` tracks which campaign.json → baselineRevealed ids have
// already been applied, so baseline seeding stays one-shot per id.
//
// Two locations are tracked, and they are deliberately separate:
//   currentLocationId — what the dashboard is LOOKING at (null = home view)
//   partyLocationId   — where the party IS. Falls back to campaign.json's
//                       authored `partyLocation` in a browser that never set one.
// The DM can look away from the party (peek at another location) and snap back.
//
// Extends window.App (already created by data.js) with:
//   App.isRevealed(id)        → boolean
//   App.setRevealed(id, bool) → persist + fire campaign:changed
//   App.getNote(id)           → string (empty string if none)
//   App.setNote(id, text)     → persist (no event — notes are DM-private)
//   App.getCurrentLocationId()→ string|null
//   App.setCurrentLocation(id)→ persist + fire location:changed
//   App.getPartyLocationId()  → string|null (runtime value, else authored default)
//   App.getPartyLocation()    → the party's location entity, or null
//   App.setPartyLocation(id)  → move the party AND the view; fires party:changed
//                               then location:changed
//   App.getTimeOfDay()        → "dawn"|"day"|"dusk"|"night"
//   App.setTimeOfDay(t)       → persist + fire time:changed

(function () {
  // Reads from window.CAMPAIGN (set synchronously by data.js before this runs).
  // To use a different key for a new campaign, update campaign.json's storageKey.
  const KEY = window.CAMPAIGN.storageKey;

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; }
    catch { return {}; }
  }

  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(_state)); }
    catch (e) { console.warn('[state] localStorage write failed:', e); }
    if (window.GitHubState) window.GitHubState.sync(_state);
  }

  const _state = load();
  if (!_state.revealed)           _state.revealed           = {};
  if (!_state.notes)              _state.notes              = {};
  if (!_state.baselineSeeded)     _state.baselineSeeded     = {};
  if (!('currentLocationId' in _state)) _state.currentLocationId = null;
  if (!('partyLocationId' in _state))   _state.partyLocationId   = null;
  if (!_state.timeOfDay)          _state.timeOfDay          = 'day';


  Object.assign(window.App, {
    // ── Baseline knowledge ────────────────────────────────────────────────
    // campaign.json may list `baselineRevealed`: entities the party knows from
    // the campaign's first moment rather than by discovering them. (Five-year
    // students already know their own faculty, the campus, and the local
    // geography — that isn't a session reveal, it's the starting state.)
    //
    // Called by data.js once campaign.json has actually been fetched and
    // merged — NOT at script load, because window.CAMPAIGN only holds sync
    // defaults at that point and would silently have no baseline list.
    //
    // Additive and idempotent. Each id is applied at most once and remembered
    // in `baselineSeeded`, so:
    //   • a DM who deliberately un-reveals a baseline entity keeps that choice,
    //   • ids added to campaign.json later are still applied on next load,
    //   • re-running this never clobbers session-earned reveals.
    seedBaselineKnowledge() {
      const baseline = window.CAMPAIGN && window.CAMPAIGN.baselineRevealed;
      if (!Array.isArray(baseline) || !baseline.length) return 0;
      let added = 0;
      for (const id of baseline) {
        if (!id || _state.baselineSeeded[id]) continue;
        _state.baselineSeeded[id] = true;
        if (!_state.revealed[id]) { _state.revealed[id] = true; added++; }
      }
      if (added) {
        save();
        // One event for the whole batch — menu.js/dashboard re-render on this,
        // which matters when seeding resolves after the first render.
        //
        // Only fire once entities exist. campaign.json and data/*.json are
        // fetched in parallel, so seeding can land first; re-rendering against
        // an empty entity map throws (dashboard resolves currentLocationId by
        // id). When entities arrive later they trigger their own render, which
        // already reflects the seeded state — so skipping the event is safe.
        if (Array.isArray(window.ENTITIES) && window.ENTITIES.length) {
          document.dispatchEvent(
            new CustomEvent('campaign:changed', { detail: { baselineSeeded: added } })
          );
        }
      }
      return added;
    },

    isRevealed(id) {
      return !!_state.revealed[id];
    },
    setRevealed(id, bool) {
      if (bool) _state.revealed[id] = true;
      else      delete _state.revealed[id];
      save();
      document.dispatchEvent(
        new CustomEvent('campaign:changed', { detail: { id, revealed: !!bool } })
      );
    },
    getNote(id) {
      return _state.notes[id] || '';
    },
    setNote(id, text) {
      const t = (text || '').trim();
      if (t) _state.notes[id] = t;
      else   delete _state.notes[id];
      save();
    },

    getCurrentLocationId() {
      return _state.currentLocationId || null;
    },
    setCurrentLocation(id) {
      _state.currentLocationId = id || null;
      save();
      document.dispatchEvent(new CustomEvent('location:changed', { detail: { id: _state.currentLocationId } }));
    },
    clearLocation() {
      this.setCurrentLocation(null);
    },

    getPartyLocationId() {
      return _state.partyLocationId
        || (window.CAMPAIGN && window.CAMPAIGN.partyLocation)
        || null;
    },
    // Resolved entity. A stored id that no longer resolves (entity renamed or
    // removed since) falls through to the authored default rather than
    // leaving the party nowhere.
    getPartyLocation() {
      const authored = window.CAMPAIGN && window.CAMPAIGN.partyLocation;
      for (const id of [_state.partyLocationId, authored]) {
        const e = id && this.byId(id);
        if (e && e.type === 'location') return e;
      }
      return null;
    },
    // The view follows the party: the reason to say where the party is, is to
    // look at it. To look elsewhere without moving them, use setCurrentLocation.
    setPartyLocation(id) {
      if (!id) return;
      _state.partyLocationId   = id;
      _state.currentLocationId = id;
      save();
      document.dispatchEvent(new CustomEvent('party:changed',    { detail: { id } }));
      document.dispatchEvent(new CustomEvent('location:changed', { detail: { id } }));
    },

    getTimeOfDay() {
      return _state.timeOfDay || 'day';
    },
    setTimeOfDay(t) {
      _state.timeOfDay = t;
      save();
      document.dispatchEvent(new CustomEvent('time:changed', { detail: { time: t } }));
    },
  });

  // isVisible() in data.js: DM sees all; player sees only visibility:"player" AND isRevealed().
  // The reveal toggle in the modal and the session complete flow set these flags.
})();
