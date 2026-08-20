#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,pathlib
from assurance import load_json, validate_document, summarize, infer_residual, retest_outcome

def main():
    ap=argparse.ArgumentParser(description='RAHP v1.2 assurance lifecycle utilities'); sub=ap.add_subparsers(dest='cmd',required=True)
    p=sub.add_parser('validate-evaluation');p.add_argument('file',type=pathlib.Path)
    p=sub.add_parser('validate-remediation');p.add_argument('file',type=pathlib.Path)
    p=sub.add_parser('validate-retest');p.add_argument('file',type=pathlib.Path)
    p=sub.add_parser('summarize');p.add_argument('file',type=pathlib.Path)
    p=sub.add_parser('infer');p.add_argument('file',type=pathlib.Path)
    p=sub.add_parser('retest-outcome');p.add_argument('--previous',required=True);p.add_argument('--current',required=True)
    a=ap.parse_args()
    schemas={'validate-evaluation':'assurance-evaluation.schema.json','validate-remediation':'remediation-manifest.schema.json','validate-retest':'retest.schema.json'}
    if a.cmd in schemas:
        errs=validate_document(load_json(a.file),schemas[a.cmd]); print('VALID' if not errs else 'INVALID'); [print('  - '+e) for e in errs]; raise SystemExit(bool(errs))
    if a.cmd=='summarize': print(json.dumps(summarize(load_json(a.file).get('evaluations') or []),indent=2))
    elif a.cmd=='infer':
        v=load_json(a.file);print(infer_residual(v.get('signals') or [],v.get('control_evidence') or [],v.get('assurance_evidence') or []))
    else: print(retest_outcome(a.previous,a.current))
if __name__=='__main__':main()
