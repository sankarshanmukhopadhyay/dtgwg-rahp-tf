#!/usr/bin/env python3
"""Validate TypeScript reference SDK and v1 cross-implementation equivalence."""
from __future__ import annotations
import json,pathlib,subprocess,sys,yaml
ROOT=pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'tools'))
from engine_contract import load_result,retention_plan,validate_result,correlate_trigger
from rahp import validate_config

def run(*args,capture=False):
 p=subprocess.run(args,cwd=ROOT,text=True,capture_output=capture)
 if p.returncode:
  if capture: print(p.stdout);print(p.stderr,file=sys.stderr)
  raise SystemExit(p.returncode)
 return p.stdout if capture else ''

def target_projection(items):
 return [{k:x.get(k) for k in ('id','repository','branch','commit','reviews') if x.get(k) not in (None,'')} for x in items]

def main():
 run('npm','run','build:ts');run('node','packages/cli/dist/cli.js','conformance')
 profiles=('tests/fixtures/portable-project/rahp.yaml','profiles/dtg/rahp.yaml','profiles/cawg/rahp.yaml')
 for profile in profiles:
  run('node','packages/cli/dist/cli.js','validate-profile',profile)
  py=validate_config(ROOT/profile);ts=json.loads(run('node','packages/cli/dist/cli.js','targets',profile,capture=True))
  if target_projection(py['repositories'])!=target_projection(ts): raise SystemExit(f'target enumeration mismatch: {profile}')
 fixtures=sorted((ROOT/'tests/conformance/engine').glob('*/result.json'))
 for f in fixtures:
  py=validate_result(f,quiet=True);p=subprocess.run(['node','packages/cli/dist/cli.js','validate-result',str(f)],cwd=ROOT,text=True,capture_output=True);ts=p.returncode==0
  if py!=ts: raise SystemExit(f'cross-implementation validation mismatch: {f}')
  if py:
   a=retention_plan(load_result(f));b=json.loads(run('node','packages/cli/dist/cli.js','retention-plan',str(f),capture=True))
   if a!=b: raise SystemExit(f'cross-implementation retention mismatch: {f}')
 lifecycle=sorted((ROOT/'tests/conformance/lifecycle').glob('*/input.json'))
 for f in lifecycle:
  inp=json.loads(f.read_text());py=correlate_trigger(inp['observation'],inp.get('open_assessments') or []);ts=json.loads(run('node','packages/cli/dist/cli.js','correlate-trigger',str(f),capture=True))
  if py!=ts: raise SystemExit(f'cross-implementation trigger correlation mismatch: {f}')
 graph=json.loads(run('node','packages/cli/dist/cli.js','graph-stats','build/rahp.json',capture=True))
 if graph['nodes']<100 or graph['edges']<100: raise SystemExit(f'graph projection unexpectedly small: {graph}')
 print(f'v1 implementation conformance valid: {len(fixtures)} result fixture(s), {len(lifecycle)} lifecycle fixture(s), retention equivalence, target equivalence across {len(profiles)} profiles, {graph["nodes"]} graph nodes / {graph["edges"]} edges')
if __name__=='__main__': raise SystemExit(main())
