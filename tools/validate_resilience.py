#!/usr/bin/env python3
"""Validate DRARM catalogue, detectors, profiles, schemas and disposition policy."""
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
    cat=load(ROOT/'method/resilience/catalogue.yaml')
    det=load(ROOT/'method/resilience/detectors.yaml').get('detectors') or {}
    assert cat.get('version')==1 and cat.get('id')=='distributed-resilience-amplification'
    risks=cat.get('risks') or []
    ids=[r.get('id') for r in risks]
    assert len(ids)>=30, 'DRARM must retain comprehensive baseline coverage'
    assert len(ids)==len(set(ids)), 'duplicate DRARM risk ids'
    assert all(re.fullmatch(r'RLA-\d{3}', x or '') for x in ids)
    for r in risks:
        for k in ('title','category','severity','trigger','failure','required_controls','evidence_required','upstream_control_plane','retest_when','detectors'):
            assert r.get(k), f"{r['id']} missing {k}"
        missing=[d for d in r['detectors'] if d not in det]
        assert not missing, f"{r['id']} references unknown detectors {missing}"

    ps=json.loads((ROOT/'method/schema/resilience-profile.schema.json').read_text())
    profile_paths=list((ROOT/'profiles/resilience').glob('*.yaml')) + list((ROOT/'examples/resilience').glob('**/profile.yaml'))
    for path in profile_paths:
        jsonschema.Draft202012Validator(ps).validate(load(path))

    policy=ROOT/'method/resilience/maintainer-feedback-disposition.md'
    assert policy.is_file(), 'maintainer-feedback disposition policy missing'
    policy_text=policy.read_text(encoding='utf-8')
    for phrase in ('review-required', 'controlled', 'deployment topology', 'Record lineage'):
        assert phrase in policy_text, f'maintainer-feedback policy missing required concept: {phrase}'

    exemplar=ROOT/'examples/resilience/openvtc-cypress/maintainer-disposition.yaml'
    assert exemplar.is_file(), 'OpenVTC maintainer-feedback disposition exemplar missing'
    ex=load(exemplar)
    assert ex.get('rahp_baseline')=='v1.5.0'
    records={r.get('id'):r for r in ex.get('records') or []}
    assert records['OVTC-RAHP-01']['transition']=='weakened'
    assert records['OVTC-RAHP-01']['severity']=='Medium'
    assert records['OVTC-RAHP-02']['transition']=='weakened'
    assert records['OVTC-RAHP-02']['current_state']=='review-required'
    assert records['OVTC-RAHP-03']['transition']=='strengthened'
    assert records['OVTC-RAHP-04']['transition']=='strengthened'
    gaps={r.get('id'):r for r in ex.get('review_gaps') or []}
    assert gaps['RLA-016']['transition']=='promoted'
    assert gaps['RLA-030']['current_state']=='review-required'

    openvtc_profile=load(ROOT/'examples/resilience/openvtc-cypress/profile.yaml')
    overrides=((openvtc_profile.get('rules') or {}).get('detector_overrides') or {})
    assert overrides.get('unbounded-channel')=='review-only', 'OpenVTC exemplar must not auto-promote unbounded-channel syntax to a finding after accepted counter-evidence'

    print(f"DRARM valid: {len(risks)} risks, {len(det)} detectors, profiles and maintainer-feedback disposition valid")


if __name__=='__main__': main()
