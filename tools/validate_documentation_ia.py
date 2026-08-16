#!/usr/bin/env python3
"""Ensure rendered documentation has a curated navigation owner in v1."""
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
TOP={'RAHP Toolkit','Learn RAHP','Adopt RAHP','Run assessments','Operate assurance','Implement RAHP','Deployments & examples','Reference','Releases'}
PARENTS=TOP-{'RAHP Toolkit'}
errors=[]; checked=0
files=[*ROOT.glob('docs/**/*.md'),ROOT/'ADOPTION.md',ROOT/'CONTRIBUTING.md',ROOT/'ROADMAP.md',ROOT/'CHANGELOG.md']
for p in files:
    if not p.exists(): continue
    text=p.read_text(encoding='utf-8')
    if not text.startswith('---\n'): continue
    fm=text.split('---',2)[1]; checked+=1
    title=re.search(r'^title:\s*["\']?(.+?)["\']?\s*$',fm,re.M)
    parent=re.search(r'^parent:\s*["\']?(.+?)["\']?\s*$',fm,re.M)
    nav_exclude=re.search(r'^nav_exclude:\s*true\s*$',fm,re.M)
    ttl=title.group(1).strip('"\'') if title else ''
    par=parent.group(1).strip('"\'') if parent else None
    if ttl in TOP: continue
    if nav_exclude: continue
    if not par: errors.append(f'{p.relative_to(ROOT)}: no navigation parent')
    elif par not in PARENTS: errors.append(f'{p.relative_to(ROOT)}: unknown navigation parent {par!r}')
# hub existence/children
for ttl in TOP-{'RAHP Toolkit'}:
    found=False
    for p in ROOT.glob('docs/**/*.md'):
        txt=p.read_text(encoding='utf-8')
        if f'title: "{ttl}"' in txt or f'title: {ttl}\n' in txt:
            found=True
            if 'has_children: true' not in txt: errors.append(f'{p.relative_to(ROOT)}: hub must declare has_children: true')
    if not found: errors.append(f'missing navigation hub: {ttl}')
if errors:
    [print('ERROR:',e) for e in errors];sys.exit(1)
print(f'PASS documentation IA: {checked} renderable pages owned by {len(TOP)-1} curated sections')
