#!/usr/bin/env python3
"""Validate the portable RAHP v1.1 assurance catalogue.

The catalogue is method-level reusable vocabulary, not deployment state. This validator
checks schema shape, namespace uniqueness, cross-catalogue references, guardrail/test/evidence
coverage and control side-effect references.
"""
from __future__ import annotations
import json, pathlib, sys
from collections import defaultdict
try:
    import yaml
except ImportError:
    sys.exit('validate_catalogue.py requires PyYAML: pip install -r requirements.txt')
try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit('validate_catalogue.py requires jsonschema: pip install -r requirements.txt')

ROOT=pathlib.Path(__file__).resolve().parent.parent
CAT=ROOT/'method'/'catalogue'
SCHEMA=json.loads((ROOT/'method'/'schema'/'catalogue.schema.json').read_text(encoding='utf-8'))
FILES={
    'harm_pattern':'harm-patterns.yaml',
    'risk_pattern':'risk-patterns.yaml',
    'control_pattern':'control-patterns.yaml',
    'guardrail_pattern':'guardrail-patterns.yaml',
    'assurance_pattern':'assurance-patterns.yaml',
    'evidence_pattern':'evidence-patterns.yaml',
}

def load(path):
    with path.open(encoding='utf-8') as fh:return yaml.safe_load(fh) or {}

def main():
    errors=[]; warnings=[]; records={}; all_ids={}; duplicate=[]
    for kind,fn in FILES.items():
        path=CAT/fn
        if not path.exists(): errors.append(f'{path.relative_to(ROOT)} missing'); continue
        doc=load(path)
        if str(doc.get('catalogue_version'))!='1.1.0': errors.append(f'{path.relative_to(ROOT)}: catalogue_version must be 1.1.0')
        if doc.get('record_type')!=kind: errors.append(f'{path.relative_to(ROOT)}: record_type must be {kind}')
        recs=doc.get('records') or []
        if not isinstance(recs,list): errors.append(f'{path.relative_to(ROOT)}: records must be a list'); continue
        records[kind]={}
        validator=Draft202012Validator({'$schema': SCHEMA['$schema'], '$defs': SCHEMA['$defs'], '$ref': f'#/$defs/{kind}'})
        for i,rec in enumerate(recs,1):
            rid=str(rec.get('id') or '')
            for e in sorted(validator.iter_errors(rec),key=lambda x:list(x.path)):
                loc='.'.join(str(x) for x in e.path)
                errors.append(f'{path.relative_to(ROOT)}:{rid or i}{":"+loc if loc else ""}: {e.message}')
            if not rid: continue
            if rid in all_ids: duplicate.append(rid)
            all_ids[rid]=kind; records[kind][rid]=rec
    for rid in duplicate: errors.append(f'duplicate portable catalogue id: {rid}')

    refs={
      'risk_pattern': [('harm_patterns','harm_pattern'),('related_patterns','risk_pattern')],
      'control_pattern':[('risk_patterns','risk_pattern'),('evidence_patterns','evidence_pattern'),('introduces_or_amplifies_risks','risk_pattern')],
      'guardrail_pattern':[('risk_patterns','risk_pattern'),('control_patterns','control_pattern')],
      'assurance_pattern':[('control_patterns','control_pattern'),('guardrail_patterns','guardrail_pattern'),('evidence_patterns','evidence_pattern')],
    }
    inbound=defaultdict(int)
    for kind,pairs in refs.items():
        for rid,rec in records.get(kind,{}).items():
            for field,target_kind in pairs:
                for ref in rec.get(field) or []:
                    if ref not in records.get(target_kind,{}): errors.append(f'{kind}/{rid}.{field}: {ref} does not resolve to {target_kind}')
                    else: inbound[ref]+=1

    # Assurance invariants
    tests_by_control=defaultdict(list); tests_by_guard=defaultdict(list); tests_by_evidence=defaultdict(list)
    for tid,t in records.get('assurance_pattern',{}).items():
        for x in t.get('control_patterns') or []: tests_by_control[x].append(tid)
        for x in t.get('guardrail_patterns') or []: tests_by_guard[x].append(tid)
        for x in t.get('evidence_patterns') or []: tests_by_evidence[x].append(tid)
    for gid,g in records.get('guardrail_pattern',{}).items():
        if g.get('evidence_required') and not tests_by_guard.get(gid): errors.append(f'guardrail_pattern/{gid}: evidence_required but no assurance pattern tests it')
        if g.get('override_permitted') and not g.get('override_authority'): errors.append(f'guardrail_pattern/{gid}: override permitted but override_authority missing')
    for cid,c in records.get('control_pattern',{}).items():
        if not tests_by_control.get(cid): warnings.append(f'control_pattern/{cid}: no assurance pattern currently tests this control')
        if c.get('introduces_or_amplifies_risks') and 'CTP-RISK-01' != cid and not c.get('evidence_patterns'):
            warnings.append(f'control_pattern/{cid}: declares side-effect risks but no evidence pattern')
    for rid,r in records.get('risk_pattern',{}).items():
        if not r.get('harm_patterns'): errors.append(f'risk_pattern/{rid}: risk must link at least one harm pattern')
        controls=[cid for cid,c in records.get('control_pattern',{}).items() if rid in (c.get('risk_patterns') or [])]
        guards=[gid for gid,g in records.get('guardrail_pattern',{}).items() if rid in (g.get('risk_patterns') or [])]
        if not controls: warnings.append(f'risk_pattern/{rid}: no portable control pattern')
        req=r.get('guardrail_requirement') or {}
        status=req.get('status')
        if status == 'required' and not guards:
            errors.append(f'risk_pattern/{rid}: guardrail_requirement is required but no portable guardrail maps to this risk')
        if status == 'control_sufficient' and guards:
            warnings.append(f'risk_pattern/{rid}: marked control_sufficient but a portable guardrail also maps to it')
        if status == 'conditional' and not req.get('condition'):
            errors.append(f'risk_pattern/{rid}: conditional guardrail requirement must state the condition')

    counts={k:len(v) for k,v in records.items()}
    if errors:
        for e in errors: print('ERROR',e)
    for w in warnings: print('WARN ',w)
    print('Portable catalogue counts: '+', '.join(f'{k}={v}' for k,v in counts.items()))
    if errors:
        print(f'Catalogue validation failed: {len(errors)} error(s), {len(warnings)} warning(s).'); return 1
    print(f'Catalogue validation clean: {sum(counts.values())} portable pattern(s), {len(warnings)} warning(s).')
    return 0
if __name__=='__main__': raise SystemExit(main())
