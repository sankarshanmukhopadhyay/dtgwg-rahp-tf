#!/usr/bin/env python3
from pathlib import Path
import sys, re, yaml
ROOT=Path(__file__).resolve().parent.parent
patdoc=yaml.safe_load((ROOT/'method/scenario-patterns.yaml').read_text()) or {}
patterns={p['id'] for p in patdoc.get('patterns',[])}
errors=[]; corpora=0; scenarios=0
if not patterns: errors.append('method/scenario-patterns.yaml defines no patterns')
for path in sorted((ROOT/'corpora').glob('*.yaml')):
    corpora+=1; doc=yaml.safe_load(path.read_text()) or {}; c=doc.get('corpus') or {}
    for f in ('id','title','source_repository','source_path','adapter_version','description','scenarios'):
        if not c.get(f): errors.append(f'{path.relative_to(ROOT)}: corpus.{f} is required')
    seen=set()
    for s in c.get('scenarios') or []:
        scenarios+=1; sid=str(s.get('id') or '')
        if not sid: errors.append(f'{path.relative_to(ROOT)}: scenario id required'); continue
        if sid in seen: errors.append(f'{path.relative_to(ROOT)}: duplicate scenario id {sid}')
        seen.add(sid)
        for f in ('title','domain','primary_goal','primary_pressure','priority','scenario_patterns'):
            if not s.get(f): errors.append(f'{path.relative_to(ROOT)}:{sid}: {f} is required')
        refs=s.get('scenario_patterns') or []
        if not isinstance(refs,list): errors.append(f'{path.relative_to(ROOT)}:{sid}: scenario_patterns must be a list'); continue
        for ref in refs:
            if ref not in patterns: errors.append(f'{path.relative_to(ROOT)}:{sid}: unknown scenario pattern {ref}')
if corpora==0: errors.append('no corpora/*.yaml files found')
if errors:
    for e in errors: print('ERROR',e)
    print(f'Scenario corpus validation failed: {len(errors)} error(s).'); raise SystemExit(1)
print(f'Scenario corpus validation clean: {corpora} corpus/corpora, {scenarios} scenarios, {len(patterns)} portable patterns.')
