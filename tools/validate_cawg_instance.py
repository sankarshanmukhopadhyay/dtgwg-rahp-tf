#!/usr/bin/env python3
"""Validate the v0.7 CAWG/C2PA deployment integrity contract."""
from pathlib import Path
import sys,yaml,json
ROOT=Path(__file__).resolve().parents[1]
def y(path): return yaml.safe_load((ROOT/path).read_text()) or {}
errors=[]
risks={r['id'] for r in y(Path('instances/cawg/data/risks.yaml')).get('records',[]) if r.get('id')}
if len(risks)<28: errors.append(f'CAWG risk register has {len(risks)} risks; v0.7 baseline requires at least 28')
corpus=y(Path('corpora/cawg.yaml')).get('corpus') or {}; scenarios=corpus.get('scenarios') or []
if len(scenarios)<36: errors.append(f'CAWG corpus has {len(scenarios)} scenarios; v0.7 baseline requires at least 36')
scenario_ids={s.get('id') for s in scenarios}
readiness=y(Path('instances/cawg/mandate-readiness.yaml'))
if len(readiness.get('records') or [])<10: errors.append('mandate-readiness register is unexpectedly sparse')
for r in readiness.get('records') or []:
    for rid in r.get('blocking_risks') or []:
        if rid not in risks: errors.append(f"{r.get('id')}: unknown blocking risk {rid}")
watch=y(Path('instances/cawg/watch/issues.yaml'))
if len(watch.get('issues') or [])<10: errors.append('CAWG issue watch must retain at least 10 selected architecture/governance issues')
for i in watch.get('issues') or []:
    if not i.get('number') or not i.get('theme') or not i.get('affected_reviews'):
        errors.append(f"watched issue {i.get('number')}: number/theme/affected_reviews required")
reviews=list(ROOT.glob('examples/cawg-c2pa/**/pressure-test.yaml'))
if len(reviews)<17: errors.append(f'expected at least 17 CAWG pressure-test reviews, found {len(reviews)}')
sec=list(ROOT.glob('examples/security-hardening/cawg*/findings.yaml'))
if len(sec)<2: errors.append(f'expected at least 2 CAWG security reviews, found {len(sec)}')
comb=list(ROOT.glob('examples/combined/cawg*/combined-review.yaml'))
if len(comb)<2: errors.append(f'expected at least 2 CAWG combined reviews, found {len(comb)}')
if errors:
    for e in errors: print('ERROR',e)
    print(f'CAWG instance validation failed: {len(errors)} error(s).'); sys.exit(1)
print(f'CAWG instance validation clean: {len(risks)} risks, {len(scenarios)} scenarios, {len(reviews)} pressure reviews, {len(sec)} security reviews, {len(comb)} combined reviews, {len(watch.get("issues") or [])} watched issues.')
