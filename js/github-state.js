// github-state.js — GitHub API state sync.
//
// Persists campaign-state.json to the GitHub repo so DM notes and revealed
// flags survive across machines. Requires a fine-grained personal access
// token with Contents: read+write on this repo, stored in localStorage.
//
// The token is NEVER committed to the repo. It lives only in the browser's
// localStorage on each machine the DM uses.
//
// Exposes window.GitHubState:
//   .sync(state)       debounced write — called by state.js on every save
//   .load()            fetch remote state and merge into localStorage
//   .promptToken()     show token entry UI
//   .getToken()        current token (empty string if none)

(function () {
  const TOKEN_KEY   = (window.CAMPAIGN?.id || 'campaign') + '.github-token';
  const DEBOUNCE_MS = 2500;

  let _syncTimer = null;
  let _currentSha = null;  // SHA of campaign-state.json, required for updates

  // ── Token ─────────────────────────────────────────────────────────────────

  function getToken() {
    return localStorage.getItem(TOKEN_KEY) || '';
  }

  function saveToken(token) {
    const t = (token || '').trim();
    if (t) localStorage.setItem(TOKEN_KEY, t);
    else   localStorage.removeItem(TOKEN_KEY);
  }

  // ── GitHub API helpers ────────────────────────────────────────────────────

  function apiUrl() {
    const { owner, repo, stateFile } = window.CAMPAIGN.github;
    return `https://api.github.com/repos/${owner}/${repo}/contents/${stateFile}`;
  }

  function authHeaders() {
    return {
      'Authorization':        `Bearer ${getToken()}`,
      'Accept':               'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
    };
  }

  // btoa() breaks on non-Latin characters in notes; encode via URI escaping.
  function toBase64(str) {
    return btoa(unescape(encodeURIComponent(str)));
  }

  function fromBase64(str) {
    return decodeURIComponent(escape(atob(str.replace(/\n/g, ''))));
  }

  async function fetchRemote() {
    const res = await fetch(apiUrl(), { headers: authHeaders() });
    if (res.status === 404) return null;           // file doesn't exist yet
    if (!res.ok) throw new Error(`GitHub ${res.status}`);
    const data = await res.json();
    _currentSha = data.sha;
    return JSON.parse(fromBase64(data.content));
  }

  async function pushRemote(state) {
    const body = {
      message: `Campaign state — ${new Date().toISOString().slice(0, 10)}`,
      content: toBase64(JSON.stringify(state, null, 2)),
    };
    if (_currentSha) body.sha = _currentSha;

    const res = await fetch(apiUrl(), {
      method:  'PUT',
      headers: { ...authHeaders(), 'Content-Type': 'application/json' },
      body:    JSON.stringify(body),
    });
    if (!res.ok) throw new Error(`GitHub ${res.status}`);
    const data = await res.json();
    _currentSha = data.content.sha;
  }

  // ── Status UI ─────────────────────────────────────────────────────────────

  const LABELS = {
    idle:      '⛓ GitHub',
    'no-token':'⛓ Link GitHub',
    syncing:   '↻ Syncing…',
    synced:    '✓ Synced',
    error:     '✗ Sync error',
  };

  function setStatus(s) {
    const btn = document.getElementById('github-sync-btn');
    if (!btn) return;
    btn.textContent     = LABELS[s] || LABELS.idle;
    btn.dataset.status  = s;
  }

  // ── Core sync ─────────────────────────────────────────────────────────────

  // Debounced write — called on every localStorage save (state.js).
  function sync(state) {
    const cfg = window.CAMPAIGN?.github;
    if (!getToken() || !cfg?.owner) return;

    clearTimeout(_syncTimer);
    setStatus('syncing');

    _syncTimer = setTimeout(async () => {
      try {
        // Refresh SHA if we lost it (page reload between saves).
        if (!_currentSha) await fetchRemote();
        await pushRemote(state);
        setStatus('synced');
      } catch (e) {
        console.error('[github-state] Push failed:', e);
        setStatus('error');
      }
    }, DEBOUNCE_MS);
  }

  // Pull remote state and merge into localStorage, then re-render.
  // revealed + notes: remote wins (authoritative campaign record).
  // timeOfDay + currentLocationId: local wins (ephemeral UI state).
  async function load() {
    const cfg = window.CAMPAIGN?.github;
    if (!getToken() || !cfg?.owner) { setStatus('no-token'); return; }

    setStatus('syncing');
    try {
      const remote = await fetchRemote();
      if (remote) {
        const KEY   = window.CAMPAIGN.storageKey;
        const local = JSON.parse(localStorage.getItem(KEY) || '{}');
        const merged = {
          revealed:          { ...local.revealed,  ...remote.revealed  },
          notes:             { ...local.notes,     ...remote.notes     },
          timeOfDay:         local.timeOfDay         || remote.timeOfDay         || 'day',
          currentLocationId: local.currentLocationId || null,
        };
        localStorage.setItem(KEY, JSON.stringify(merged));
        document.dispatchEvent(new CustomEvent('campaign:changed', { detail: { source: 'github-sync' } }));
      }
      setStatus('synced');
    } catch (e) {
      console.error('[github-state] Load failed:', e);
      setStatus('error');
    }
  }

  // ── Token prompt ──────────────────────────────────────────────────────────

  function promptToken() {
    const existing = getToken();
    const msg = existing
      ? 'Update GitHub Personal Access Token (leave blank to disconnect):'
      : 'Enter GitHub Personal Access Token to enable cross-machine sync:';
    const token = prompt(msg, existing);
    if (token === null) return;   // cancelled
    saveToken(token);
    if (getToken()) load();
    else setStatus('no-token');
  }

  // ── Wiring ────────────────────────────────────────────────────────────────

  window.GitHubState = { sync, load, promptToken, getToken };

  document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('github-sync-btn');
    if (!btn) return;

    btn.addEventListener('click', () => {
      if (!getToken()) {
        promptToken();
      } else {
        const reenter = confirm(
          'GitHub sync is active.\n\nOK — re-enter token\nCancel — force sync now'
        );
        if (reenter) promptToken();
        else load();
      }
    });

    // Keep button visibility in sync with DM mode.
    document.addEventListener('dm:changed', ({ detail }) => {
      btn.hidden = !detail.on;
      if (detail.on) setStatus(getToken() ? 'idle' : 'no-token');
    });

    // Pull remote state on startup (only matters if a token is stored).
    load();
  });
})();
