#!/usr/bin/env python3
"""Validate DRARM catalogue, detectors, profiles and schemas."""
from __future__ import annotations
import json
import pathlib
import re
import sys
try:
    import yaml, jsonschema
except ImportError:
    sys.exit("requires PyYAML and jsonschema")
ROOT=pathlib.Path(__file__).resolve().parent.parent

def load(p):
    with p.open(encoding='utf-8') as f: return yaml.safe_load(f) or {}

def main():
    cat=load(ROOT/'method/resilience/catalogue.yaml'); det=load(ROOT/'method/resilience/detectors.yaml').get('detectors') or {}
    assert cat.get('version')==1 and cat.get('id')=='distributed-resilience-amplification'
    risks=cat.get('risks') or []; ids=[r.get('id') for r in risks]
    assert len(ids)>=30, 'DRARM must retain comprehensive baseline coverage'
    assert len(ids)==len(set(ids)), 'duplicate DRARM risk ids'
    assert all(re.fullmatch(r'RLA-\d{3}', x or '') for x in ids)
    for r in risks:
        for k in ('title','category','severity','trigger','failure','required_controls','evidence_required','upstream_control_plane','retest_when','detectors'):
            assert r.get(k), f"{r['id']} missing {k}"
        missing=[d for d in r['detectors'] if d not in det]
        assert not missing, f"{r['id']} references unknown detectors {missing}"
    ps=json.loads((ROOT/'method/schema/resilience-profile.schema.json').read_text())
    for path in list((ROOT/'profiles/resilience').glob('*.yaml')) + list((ROOT/'examples/resilience').glob('**/profile.yaml')):
        jsonschema.Draft202012Validator(ps).validate(load(path))
    print(f"DRARM valid: {len(risks)} risks, {len(det)} detectors, profiles valid")
if __name__=='__main__': main()
