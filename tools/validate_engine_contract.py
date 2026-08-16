#!/usr/bin/env python3
"""Validate the v0.8 engine contract, retention policy and conformance fixtures."""
from __future__ import annotations
import json, pathlib, sys
try:
    import yaml, jsonschema
except ImportError:
    sys.exit('requires PyYAML and jsonschema')
ROOT=pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'tools'))
from engine_contract import validate_result, load_result, retention_plan

def fail(msg): print('ERROR:',msg); return 1

def main():
    errors=0
    contract=yaml.safe_load((ROOT/'method/engine-contract.yaml').read_text())
    stages=contract.get('execution_model',{}).get('stages') or []
    expected=['source','observation','trigger','assessment','finding','disposition','baseline']
    if stages!=expected: errors+=fail(f'engine stages must be {expected}, got {stages}')
    ops={x.get('id') for x in contract.get('operations') or []}
    required={'validate-profile','observe-source','correlate-trigger','scaffold-assessment','validate-assessment','normalize-result','plan-retention','promote-disposition'}
    if not required<=ops: errors+=fail('engine contract missing operations: '+', '.join(sorted(required-ops)))
    policy=yaml.safe_load((ROOT/'method/evidence-retention.yaml').read_text())
    classes=policy.get('classes') or {}
    if set(classes)!={'ephemeral','referenced','durable','exemplar'}: errors+=fail('retention classes must be ephemeral/referenced/durable/exemplar')
    if classes.get('ephemeral',{}).get('repository')!='forbidden': errors+=fail('ephemeral evidence must be forbidden from repository')
    fixtures=sorted((ROOT/'tests/conformance/engine').glob('*/result.json'))
    if not fixtures: errors+=fail('no engine conformance fixtures')
    for result_path in fixtures:
        exp=yaml.safe_load((result_path.parent/'expected.yaml').read_text())
        actual=validate_result(result_path,quiet=True)
        if actual != bool(exp['valid']): errors+=fail(f'{result_path.parent.name}: expected valid={exp["valid"]}, got {actual}')
        if actual and 'retention' in exp:
            plan=retention_plan(load_result(result_path)); got=sorted({a['class'] for a in plan['actions'] if a['action']=='commit'})
            want=sorted(exp['retention'].get('repository_classes') or [])
            if got!=want: errors+=fail(f'{result_path.parent.name}: retention repository classes {got}, expected {want}')
    durable=sorted(ROOT.glob('instances/*/reviews/*.result.json'))
    for result_path in durable:
        if not validate_result(result_path,quiet=True): errors+=fail(f'durable normalized result invalid: {result_path.relative_to(ROOT)}')
    if errors: print(f'Engine contract validation failed: {errors} error(s)'); return 1
    print(f'Engine contract valid: {len(fixtures)} conformance fixtures; {len(durable)} durable normalized result(s); retention policy valid')
    return 0
if __name__=='__main__': raise SystemExit(main())
