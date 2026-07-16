#!/usr/bin/env python3
"""
fetch-monster-tokens.py  —  run once from repo root:
    python tools/fetch-monster-tokens.py

Downloads monster token images from 5e.tools into
shared/img/monsters/{source}/{name}.webp.

Re-runnable: skips already-present files.
Expect ~40-60% hit rate; monsters with no token get a 404 (normal).
"""
import json
import os
import sys
import time
from urllib.parse import quote
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

BASE    = 'https://5e.tools/img/bestiary/tokens'
INDEX   = 'shared/data/monsters-index.json'
OUT_DIR = 'shared/img/monsters'
TIMEOUT = 15
DELAY   = 0.08   # ~12 req/s
HEADERS = {'User-Agent': 'monster-token-fetcher/1.0 (local-dnd-app)'}


def p(msg, **kw):
    kw['flush'] = True
    print(msg, **kw)


def safe_filename(name):
    for ch in '\\/:*?"<>|':
        name = name.replace(ch, '_')
    return name


def fetch_bytes(url):
    """Returns bytes on 200, None on 404, raises on other errors."""
    req = Request(url, headers=HEADERS)
    try:
        with urlopen(req, timeout=TIMEOUT) as r:
            return r.read()
    except HTTPError as e:
        if e.code == 404:
            return None
        raise


def main():
    if not os.path.exists(INDEX):
        sys.exit(f"Index not found: {INDEX}\nRun from the repo root directory.")

    # Quick sanity check with a known-good URL before starting the full run
    p("Verifying connection to 5e.tools… ", end='')
    test_url = f"{BASE}/XMM/{quote('Beholder.webp')}"
    try:
        data = fetch_bytes(test_url)
        if data:
            p(f"OK ({len(data):,} bytes)")
        else:
            sys.exit("FAILED — test URL returned 404. The site structure may have changed.")
    except Exception as e:
        sys.exit(f"FAILED — {e}")

    with open(INDEX, encoding='utf-8') as f:
        monsters = json.load(f)

    total = len(monsters)
    p(f"\nFetching tokens for {total} monsters…")
    p("Progress printed every 100 monsters.\n")
    downloaded = skipped = missing = errors = 0

    for i, m in enumerate(monsters, 1):
        source = m['source']
        name   = m['name']
        fname  = safe_filename(name) + '.webp'
        dest_dir  = os.path.join(OUT_DIR, source)
        dest_file = os.path.join(dest_dir, fname)

        if os.path.exists(dest_file):
            skipped += 1
        else:
            os.makedirs(dest_dir, exist_ok=True)
            url = f"{BASE}/{source}/{quote(fname)}"
            try:
                data = fetch_bytes(url)
                if data:
                    with open(dest_file, 'wb') as f:
                        f.write(data)
                    downloaded += 1
                else:
                    missing += 1
                time.sleep(DELAY)
            except (URLError, OSError) as e:
                p(f"  Error ({source}/{name}): {e}")
                errors += 1

        if i % 100 == 0 or i == total:
            p(f"  [{i:>4}/{total}]  downloaded={downloaded}  missing={missing}  errors={errors}  skipped={skipped}")

    p(f"\nDone.")
    p(f"  Downloaded  : {downloaded}")
    p(f"  Already had : {skipped}")
    p(f"  Not found   : {missing}  (no token exists — expected for many monsters)")
    p(f"  Errors      : {errors}")


if __name__ == '__main__':
    main()
