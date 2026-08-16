#!/usr/bin/env python3
"""Validate the v0.9 TypeScript reference SDK and cross-implementation equivalence."""
from __future__ import annotations
import json,pathlib,subprocess,sys,tempfile
ROOT=pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'tools'))
from engine_contract import load_result,retention_plan,validate_result

def run(*args,capture=False):
 p=subprocess.run(args,cwd=ROOT,text=True,capture_output=capture)
 if p.returncode:
  if capture: print(p.stdout); print(p.stderr,file=sys.stderr)
  raise SystemExit(p.returncode)
 return p.stdout if capture else ''

def main():
 run('npm','run','build:ts')
 run('node','packages/cli/dist/cli.js','conformance')
 for profile in ('tests/fixtures/portable-project/rahp.yaml','profiles/dtg/rahp.yaml','profiles/cawg/rahp.yaml'):
  run('node','packages/cli/dist/cli.js','validate-profile',profile)
 fixtures=sorted((ROOT/'tests/conformance/engine').glob('*/result.json'))
 for f in fixtures:
  py=validate_result(f,quiet=True)
  p=subprocess.run(['node','packages/cli/dist/cli.js','validate-result',str(f)],cwd=ROOT,text=True,capture_output=True)
  ts=p.returncode==0
  if py!=ts: raise SystemExit(f'cross-implementation validation mismatch: {f}')
  if py:
   a=retention_plan(load_result(f)); b=json.loads(run('node','packages/cli/dist/cli.js','retention-plan',str(f),capture=True))
   if a!=b: raise SystemExit(f'cross-implementation retention mismatch: {f}')
 graph=json.loads(run('node','packages/cli/dist/cli.js','graph-stats','build/rahp.json',capture=True))
 if graph['nodes'] < 100 or graph['edges'] < 100: raise SystemExit(f'graph projection unexpectedly small: {graph}')
 print(f'TypeScript SDK valid: {len(fixtures)} shared fixture(s), retention equivalence, 3 profiles, {graph["nodes"]} graph nodes / {graph["edges"]} edges')
 return 0
if __name__=='__main__': raise SystemExit(main())
