#!/usr/bin/env python3
"""Portable RAHP v1.2 assurance evaluation, remediation and retest helpers."""
from __future__ import annotations
import json, pathlib
from typing import Any
try:
    import jsonschema
except ImportError:
    jsonschema = None
ROOT=pathlib.Path(__file__).resolve().parent.parent
SCHEMA_DIR=ROOT/'method'/'schema'
RESIDUAL_STATES=('assured','controlled','finding','assurance-gap','review-required','not-assessed','not-applicable')

def load_json(path:pathlib.Path)->dict[str,Any]:
    value=json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(value,dict): raise ValueError(f'expected object: {path}')
    return value

def validate_document(value:dict[str,Any], schema_name:str)->list[str]:
    if jsonschema is None: raise RuntimeError('jsonschema is required')
    schema=json.loads((SCHEMA_DIR/schema_name).read_text(encoding='utf-8'))
    resolver=jsonschema.RefResolver(base_uri=(SCHEMA_DIR.as_uri()+'/'),referrer=schema)
    errors=[]
    for exc in jsonschema.Draft202012Validator(schema,resolver=resolver).iter_errors(value):
        loc='.'.join(str(x) for x in exc.absolute_path) or '<root>'
        errors.append(f'{loc}: {exc.message}')
    return errors

def summarize(evaluations:list[dict[str,Any]])->dict[str,int]:
    out={state:0 for state in RESIDUAL_STATES}
    for item in evaluations:
        state=((item.get('residual') or {}).get('status'))
        if state in out: out[state]+=1
    return out

def infer_residual(signals:list[dict[str,Any]], controls:list[dict[str,Any]], assurance:list[dict[str,Any]])->str:
    """Conservative reference inference; never converts uncertainty into a pass."""
    risk=any(x.get('type')=='risk-indicator' for x in signals)
    contradiction=any(x.get('type')=='contradictory-evidence' for x in signals)
    control_present=any(x.get('status')=='present' for x in controls)
    control_absent=any(x.get('status')=='absent' for x in controls)
    test_pass=any(x.get('status')=='pass' for x in assurance)
    test_fail=any(x.get('status')=='fail' for x in assurance)
    test_partial=any(x.get('status') in ('partial','unknown') for x in assurance)
    if contradiction or test_fail or (risk and control_absent): return 'finding'
    if risk and control_present and test_pass: return 'controlled'
    if risk and control_present and (test_partial or not assurance): return 'assurance-gap'
    if risk: return 'review-required'
    if control_present and test_pass: return 'assured'
    return 'not-assessed'

def retest_outcome(previous_status:str,current_status:str)->str:
    bad={'finding','assurance-gap','review-required'}
    good={'assured','controlled','not-applicable'}
    if previous_status in bad and current_status in good: return 'resolved'
    if previous_status in good and current_status in bad: return 'regression'
    if current_status in bad: return 'residual'
    return 'inconclusive'
