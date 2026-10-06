#!/usr/bin/env python3
"""
tools/test.py --DnDAcademy data integrity tests.

Run manually:   python tools/test.py
Auto-runs from: start-map.bat (before the server starts)

Exit code 0 = all checks passed (warnings are OK).
Exit code 1 = one or more FAIL checks --fix when possible, server still starts.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent  # project root

REQUIRED_FIELDS = ['id', 'name', 'type', 'contentType', 'visibility']
CROSSLINK_RE    = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
# <div class="session-prompt" data-location="<location id>"> — a Session Runner
# beat that moves the party (and the dashboard) to that location.
DATA_LOCATION_RE = re.compile(r'data-location\s*=\s*"([^"]*)"')


def main():
    passes   = []
    failures = []
    warnings = []

    # ── Registry ──────────────────────────────────────────────────────────────
    index_path = ROOT / 'campaigns' / 'index.json'
    try:
        registry = json.loads(index_path.read_text(encoding='utf-8'))
    except Exception as e:
        failures.append(f'campaigns/index.json: parse error --{e}')
        report(passes, failures, warnings)
        return

    passes.append('campaigns/index.json parsed OK')

    # ── Per-campaign ──────────────────────────────────────────────────────────
    for entry in registry:
        check_campaign(ROOT, entry.get('id', '<unknown>'), passes, failures, warnings)

    report(passes, failures, warnings)


def check_campaign(root, cid, passes, failures, warnings):
    base = root / 'campaigns' / cid
    tag  = f'[{cid}]'

    # campaign.json --dmPassHash required
    cfg      = {}
    cfg_path = base / 'campaign.json'
    if not cfg_path.exists():
        warnings.append(f'{tag} campaign.json not found --dmPassHash not verified')
    else:
        try:
            cfg = json.loads(cfg_path.read_text(encoding='utf-8'))
            if cfg.get('dmPassHash', ''):
                passes.append(f'{tag} campaign.json: dmPassHash set')
            else:
                failures.append(f'{tag} campaign.json: dmPassHash is empty --DM view unprotected')
        except Exception as e:
            cfg = {}
            failures.append(f'{tag} campaign.json: parse error --{e}')

    # data/index.json
    data_dir = base / 'data'
    idx_path = data_dir / 'index.json'
    if not idx_path.exists():
        failures.append(f'{tag} data/index.json: not found')
        return
    try:
        file_list = json.loads(idx_path.read_text(encoding='utf-8'))
    except Exception as e:
        failures.append(f'{tag} data/index.json: parse error --{e}')
        return
    if not isinstance(file_list, list):
        failures.append(f'{tag} data/index.json: expected a JSON array')
        return

    # Load all entity files
    all_entities = []   # list of (filename, entity_dict)
    id_count     = {}   # id ->occurrence count

    for fn in file_list:
        fpath = data_dir / fn
        if not fpath.exists():
            failures.append(f'{tag} data/{fn}: file not found')
            continue
        try:
            entities = json.loads(fpath.read_text(encoding='utf-8'))
        except Exception as e:
            failures.append(f'{tag} data/{fn}: parse error --{e}')
            continue
        if not isinstance(entities, list):
            failures.append(f'{tag} data/{fn}: not a JSON array')
            continue
        passes.append(f'{tag} data/{fn}: {len(entities)} entities loaded')
        for ent in entities:
            all_entities.append((fn, ent))
            eid = ent.get('id')
            if eid:
                id_count[eid] = id_count.get(eid, 0) + 1

    all_ids = set(id_count)

    # Duplicate IDs
    dupes = sorted(eid for eid, n in id_count.items() if n > 1)
    if dupes:
        for d in dupes:
            failures.append(f'{tag} duplicate id: "{d}"')
    else:
        passes.append(f'{tag} ids: {len(all_ids)} unique across all files')

    # campaign.json location references. A typo here silently drops a region
    # from the dashboard's home view or leaves the party nowhere, so these FAIL.
    loc_ids = {ent.get('id') for _, ent in all_entities if ent.get('type') == 'location'}

    if 'regions' in cfg:
        regions = cfg['regions']
        if not isinstance(regions, list):
            failures.append(f'{tag} campaign.json: regions must be an array')
        else:
            bad = []
            for r in regions:
                rid = r if isinstance(r, str) else (r.get('id') if isinstance(r, dict) else None)
                if rid not in loc_ids:
                    bad.append(str(rid))
            if bad:
                for rid in bad:
                    failures.append(f'{tag} campaign.json: regions hub "{rid}" is not a location entity')
            else:
                passes.append(f'{tag} campaign.json: {len(regions)} region hubs resolve')

    party = cfg.get('partyLocation')
    if party:
        if party in loc_ids:
            passes.append(f'{tag} campaign.json: partyLocation resolves')
        else:
            failures.append(f'{tag} campaign.json: partyLocation "{party}" is not a location entity')

    # Per-entity checks
    schema_errors  = 0
    missing_files  = 0
    broken_related = []
    broken_links   = []
    start_locs     = 0     # sessions that declare a startLocation
    broken_starts  = []
    data_locs      = 0     # data-location attributes found in content
    broken_data_locs = []

    for fn, ent in all_entities:
        eid = ent.get('id', f'<no id in {fn}>')

        # Required fields
        missing = [f for f in REQUIRED_FIELDS if f not in ent]
        if missing:
            failures.append(f'{tag} {eid}: missing required fields --{", ".join(missing)}')
            schema_errors += 1

        # related[] references resolve within this campaign
        for ref in ent.get('related', []):
            if ref not in all_ids:
                broken_related.append(f'{eid} ->"{ref}"')

        # startLocation is where the Session Runner puts the party on launch
        start = ent.get('startLocation')
        if start:
            start_locs += 1
            if start not in loc_ids:
                broken_starts.append(f'{eid} ->"{start}"')

        # image contentType requires contentFile
        cf = ent.get('contentFile', '')
        ct = ent.get('contentType', '')
        if ct == 'image' and not cf:
            failures.append(f'{tag} {eid}: contentType "image" requires contentFile')
            schema_errors += 1

        # contentFile exists on disk (skip inline/generated entities)
        if cf and ct not in ('inline',):
            cf_path = base / cf
            if not cf_path.exists():
                failures.append(f'{tag} {eid}: contentFile missing --{cf}')
                missing_files += 1
            elif cf.endswith('.html'):
                # Check [[id]] and [[id|label]] cross-links inside HTML
                try:
                    html = cf_path.read_text(encoding='utf-8')
                    for m in CROSSLINK_RE.finditer(html):
                        ref_id = m.group(1).strip()
                        if ref_id not in all_ids:
                            broken_links.append(f'{eid} ->[[{ref_id}]]')
                    for m in DATA_LOCATION_RE.finditer(html):
                        data_locs += 1
                        ref_id = m.group(1).strip()
                        if ref_id not in loc_ids:
                            broken_data_locs.append(f'{eid} ->data-location="{ref_id}"')
                except Exception:
                    pass

    if schema_errors == 0:
        passes.append(f'{tag} schema: all entities have required fields')
    if missing_files == 0:
        passes.append(f'{tag} contentFile: all content files exist on disk')

    # Broken related[] ->warning (shows as "no link" in UI, not a crash)
    if broken_related:
        for br in broken_related:
            warnings.append(f'{tag} related[]: unresolved --{br}')
    else:
        passes.append(f'{tag} related[]: all references resolve')

    # Broken [[links]] ->warning (UI shows them as broken, by design)
    if broken_links:
        for bl in broken_links:
            warnings.append(f'{tag} [[links]]: unresolved --{bl}')
    else:
        passes.append(f'{tag} [[links]]: all cross-links resolve')

    # Broken location references ->warning (the Runner ignores a bad
    # startLocation and draws a bad data-location chip struck through)
    if broken_starts:
        for bs in broken_starts:
            warnings.append(f'{tag} startLocation: not a location --{bs}')
    elif start_locs:
        passes.append(f'{tag} startLocation: all {start_locs} resolve to locations')

    if broken_data_locs:
        for bd in broken_data_locs:
            warnings.append(f'{tag} data-location: not a location --{bd}')
    elif data_locs:
        passes.append(f'{tag} data-location: all {data_locs} resolve to locations')


def report(passes, failures, warnings):
    total = len(passes) + len(failures) + len(warnings)
    width = 59

    print()
    print('-- DnDAcademy Data Tests ' + '-' * (width - 25))

    if failures:
        print()
        for msg in failures:
            print(f'  FAIL  {msg}')
    if warnings:
        print()
        for msg in warnings:
            print(f'  WARN  {msg}')
    if not failures and not warnings:
        print(f'  All {total} checks passed.')
    else:
        print()

    summary = f'  {len(passes)}/{total} passed'
    if failures:
        summary += f'   {len(failures)} FAILED'
    if warnings:
        summary += f'   {len(warnings)} warnings'
    print(summary)
    print('-' * width)
    print()

    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()
