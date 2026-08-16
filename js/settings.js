// settings.js — app-level user settings (⚙ Settings modal).
//
// Deliberately NOT stored in the campaign state from state.js: that store is
// keyed per campaign (campaign.json → storageKey) and is pushed to GitHub by
// github-state.js. A theme choice belongs to the person sitting at the browser,
// not to the campaign, and should not travel between machines as campaign data.
// So settings live under their own app-wide key.
//
// Shape (localStorage key "tt.settings.v1"):
//   { theme: "default" }
//
// Extends window.Settings:
//   Settings.get(key)        → value (or the default)
//   Settings.set(key, value) → persist + apply
//   Settings.open()          → open the modal
//
// Adding a theme later: add an entry to THEMES below and a matching
// :root[data-theme="<id>"] block in css/style.css. Nothing else needs to change
// — the dropdown builds itself from this list.

(function () {
  const KEY = 'tt.settings.v1';

  // The theme roster. "default" is the palette currently defined on bare :root,
  // so it intentionally sets no data-theme attribute at all.
  const THEMES = [
    { id: 'default', name: 'Default' },
  ];

  const DEFAULTS = { theme: 'default' };

  function load() {
    try { return Object.assign({}, DEFAULTS, JSON.parse(localStorage.getItem(KEY)) || {}); }
    catch { return Object.assign({}, DEFAULTS); }
  }

  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(_settings)); }
    catch (e) { console.warn('[settings] localStorage write failed:', e); }
  }

  const _settings = load();

  // ── Apply ─────────────────────────────────────────────────────────────────

  function applyTheme(id) {
    const root = document.documentElement;
    // "default" is the bare :root palette — no attribute, so nothing overrides it.
    if (!id || id === 'default') root.removeAttribute('data-theme');
    else                         root.setAttribute('data-theme', id);
  }

  function applyAll() {
    applyTheme(_settings.theme);
  }

  // ── Modal ─────────────────────────────────────────────────────────────────

  let overlayEl = null;

  function buildModal() {
    const overlay = document.createElement('div');
    overlay.id = 'settings-overlay';
    overlay.hidden = true;
    overlay.innerHTML = `
      <div id="settings-dialog" role="dialog" aria-modal="true" aria-labelledby="settings-title">
        <header id="settings-header">
          <h2 id="settings-title">Settings</h2>
          <button id="settings-close" type="button" aria-label="Close">&times;</button>
        </header>

        <div id="settings-body">
          <div class="settings-field">
            <label for="settings-theme">Color Theme</label>
            <select id="settings-theme"></select>
            <p class="settings-hint">Additional themes will appear here as they are added.</p>
          </div>
        </div>

        <footer id="settings-footer">
          <button id="settings-cancel" type="button">Cancel</button>
          <button id="settings-save" type="button">Save</button>
        </footer>
      </div>`;
    document.body.appendChild(overlay);

    const select = overlay.querySelector('#settings-theme');
    for (const t of THEMES) {
      const opt = document.createElement('option');
      opt.value = t.id;
      opt.textContent = t.name;
      select.appendChild(opt);
    }

    overlay.querySelector('#settings-close').addEventListener('click', close);
    overlay.querySelector('#settings-cancel').addEventListener('click', close);
    overlay.querySelector('#settings-save').addEventListener('click', commit);

    // Click the scrim (but not the dialog) to dismiss, matching the other overlays.
    overlay.addEventListener('click', (e) => { if (e.target === overlay) close(); });

    return overlay;
  }

  function open() {
    if (!overlayEl) overlayEl = buildModal();
    // Seed the controls from saved state each time, so a previous Cancel doesn't
    // leave a stale selection sitting in the form.
    overlayEl.querySelector('#settings-theme').value = _settings.theme;
    overlayEl.hidden = false;
    overlayEl.querySelector('#settings-theme').focus();
  }

  function close() {
    if (overlayEl) overlayEl.hidden = true;
  }

  // Save applies and persists; Cancel just closes, discarding the selection.
  function commit() {
    _settings.theme = overlayEl.querySelector('#settings-theme').value;
    save();
    applyAll();
    close();
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && overlayEl && !overlayEl.hidden) close();
  });

  // ── Wire up ───────────────────────────────────────────────────────────────

  document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('settings-btn');
    if (btn) btn.addEventListener('click', open);
  });

  applyAll();

  window.Settings = {
    get: (k) => _settings[k],
    set: (k, v) => { _settings[k] = v; save(); applyAll(); },
    open,
    THEMES,
  };
})();
