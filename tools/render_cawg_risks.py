#!/usr/bin/env python3
from pathlib import Path
import yaml, sys
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'instances/cawg/data/risks.yaml'
OUT = ROOT / 'docs/cawg-risk-register.md'
d = yaml.safe_load(SRC.read_text())
lines = [
    '---',
    'title: CAWG/C2PA assessment risk register',
    'parent: Deployments & examples',
    'nav_order: 7',
    '---',
    '# CAWG/C2PA assessment risk register',
    '',
    "This register belongs to the **external CAWG/C2PA RAHP instance**. The `CRK-*` records are RAHP assessment vocabulary, not CAWG, DIF or C2PA normative terms. Keeping them under `instances/cawg/data/` prevents an external deployment from silently inheriting the DTG instance's `RK-*` catalogue.",
    '',
    '| ID | Risk | Assessment meaning |',
    '|---|---|---|',
]
for r in d['records']:
    rid = r['id']
    desc = ' '.join(str(r.get('description', '')).split())
    lines.append(f'| <a id="{rid.lower()}"></a>`{rid}` | {r["title"]} | {desc} |')
lines += [
    '',
    'The worked reviews at [`examples/cawg-c2pa/`](../examples/cawg-c2pa/README.md) provide the evidence, harm path, treatment and retest trigger for each use of these risks.',
    '',
]
text = '\n'.join(lines)
if '--check' in sys.argv:
    if not OUT.exists() or OUT.read_text() != text:
        print('STALE docs/cawg-risk-register.md')
        raise SystemExit(1)
    print(f'CAWG risk-register Markdown current: {len(d["records"])} risk(s).')
    raise SystemExit(0)
OUT.write_text(text)
print(f'[write] docs/cawg-risk-register.md ({len(d["records"])} risks)')
