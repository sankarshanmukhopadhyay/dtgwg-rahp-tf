#!/usr/bin/env python3
"""Validate canonical RAHP security-hardening review records."""
from __future__ import annotations
import pathlib,re,subprocess,sys
from portable_catalogue import validate_block
try:
    import yaml
except ImportError:
    sys.exit('validate_security_reviews.py requires PyYAML: pip install -r requirements.txt')
ROOT=pathlib.Path(__file__).resolve().parent.parent

def load(p):
    with p.open(encoding='utf-8') as f:return yaml.safe_load(f) or {}
def ids(fn):
    vals=set()
    for path in [ROOT/'data'/fn, *sorted((ROOT/'instances').glob(f'*/data/{fn}'))]:
        if path.exists(): vals.update(str(r.get('id')) for r in load(path).get('records') or [] if r.get('id'))
    return vals
def vocab(name):
    v=load(ROOT/'method'/'vocabularies.yaml').get(name,{}).get('values',[])
    return {str(x.get('value')) if isinstance(x,dict) else str(x) for x in v}

def main():
    errors=[]
    known={'risks':ids('risks.yaml'),'controls':ids('controls.yaml'),'guardrails':ids('guardrails.yaml'),'assurance_tests':ids('assurance-tests.yaml')}
    external_records=load(ROOT/'data'/'external-standards.yaml').get('records') or []
    external={}
    for i,r in enumerate(external_records,1):
        rid=str(r.get('id') or '')
        if not rid:
            errors.append(f'data/external-standards.yaml: records[{i}] id required')
            continue
        if rid in external: errors.append(f'data/external-standards.yaml: duplicate id {rid}')
        external[rid]=r
        for k in ['organization','title','version','status','published','url','scope']:
            if not r.get(k): errors.append(f'data/external-standards.yaml:{rid}: {k} required')
        if r.get('url') and not str(r.get('url')).startswith('https://'):
            errors.append(f'data/external-standards.yaml:{rid}: url must use https')
    relationships=vocab('external_alignment_relationship')
    planes=vocab('security_control_plane'); exploit=vocab('security_exploitability'); impacts=vocab('security_impact'); detect=vocab('security_detectability'); prop=vocab('security_propagation')
    sev={'Low','Medium','High','Critical'}; statuses={'in-progress','complete','open','monitoring','resolved','superseded'}
    total=0; alignment_total=0; files=sorted(ROOT.glob('examples/security-hardening/**/findings.yaml'))
    if len(files)<3: errors.append(f'expected at least 3 security review files, found {len(files)}')
    for path in files:
        rel=path.relative_to(ROOT); r=load(path).get('review')
        if not isinstance(r,dict): errors.append(f'{rel}: missing review mapping'); continue
        for k in ['id','status','title','reviewed_on','target','reviewed_against','summary']:
            if not r.get(k): errors.append(f'{rel}: review.{k} required')
        if 'findings' not in r or not isinstance(r.get('findings'),list):
            errors.append(f'{rel}: review.findings must be a list')
        t=r.get('target') or {}; commit=str(t.get('commit') or '')
        if not re.fullmatch(r'[0-9a-fA-F]{40}',commit): errors.append(f'{rel}: target.commit must be full 40-character SHA')
        if t.get('secondary_commit') and not re.fullmatch(r'[0-9a-fA-F]{40}',str(t['secondary_commit'])): errors.append(f'{rel}: target.secondary_commit must be full SHA')
        fs=r.get('findings') or []; seen=set()
        if not fs and r.get('status')!='in-progress':
            errors.append(f'{rel}: completed/non-draft review.findings must be non-empty')
        for f in fs:
            total+=1; fid=str(f.get('id') or ''); p=f'{rel}:{fid or "<no-id>"}'
            if not re.fullmatch(r'SEC-(TT|CR|X|CW)-[0-9]{3}',fid): errors.append(f'{p}: invalid id')
            if fid in seen: errors.append(f'{p}: duplicate id')
            seen.add(fid)
            req=['title','status','severity','exploitability','impact','detectability','propagation','primary_control_plane','attack_surface','preconditions','security_properties','evidence','attack','existing_mitigations','residual_gap','recommendation','verification','rahp','external_alignment']
            for k in req:
                if not f.get(k): errors.append(f'{p}: {k} required')
            if f.get('status') not in statuses: errors.append(f'{p}: invalid status')
            if f.get('severity') not in sev: errors.append(f'{p}: invalid severity')
            if f.get('exploitability') not in exploit: errors.append(f'{p}: invalid exploitability')
            if f.get('impact') not in impacts: errors.append(f'{p}: invalid impact')
            if f.get('detectability') not in detect: errors.append(f'{p}: invalid detectability')
            if f.get('propagation') not in prop: errors.append(f'{p}: invalid propagation')
            if f.get('primary_control_plane') not in planes: errors.append(f'{p}: invalid primary control plane')
            for x in f.get('secondary_control_planes') or []:
                if x not in planes: errors.append(f'{p}: invalid secondary control plane {x}')
            for i,e in enumerate(f.get('evidence') or [],1):
                if not isinstance(e,dict) or not e.get('source') or not e.get('observation'): errors.append(f'{p}: evidence[{i}] requires source and observation')
            alignment_total += len(f.get('external_alignment') or [])
            for i,a in enumerate(f.get('external_alignment') or [],1):
                if not isinstance(a,dict):
                    errors.append(f'{p}: external_alignment[{i}] must be a mapping'); continue
                ref=str(a.get('ref') or '')
                if ref not in external: errors.append(f'{p}: external_alignment[{i}] ref {ref!r} does not resolve')
                if a.get('relationship') not in relationships: errors.append(f'{p}: external_alignment[{i}] invalid relationship {a.get("relationship")!r}')
                if not a.get('rationale'): errors.append(f'{p}: external_alignment[{i}] rationale required')
                if a.get('url') and not str(a.get('url')).startswith('https://'): errors.append(f'{p}: external_alignment[{i}] url must use https')
            rahp=f.get('rahp') or {}
            validate_block(rahp.get('portable_assurance'), p, errors, required=True)
            for kind,valid in known.items():
                refs=rahp.get(kind) or []
                if not isinstance(refs,list): errors.append(f'{p}: rahp.{kind} must be list'); continue
                for x in refs:
                    if x not in valid: errors.append(f'{p}: rahp.{kind} reference {x!r} does not resolve')
        s=r.get('summary') or {}
        if s.get('finding_count')!=len(fs): errors.append(f'{rel}: summary.finding_count mismatch')
        if s.get('open_count')!=sum(1 for f in fs if f.get('status')=='open'): errors.append(f'{rel}: summary.open_count mismatch')
    if errors:
        for e in errors: print('ERROR',e)
        print(f'\nSecurity-review validation failed: {len(errors)} error(s).'); return 1
    rr=subprocess.run([sys.executable,str(ROOT/'tools'/'render_security_reviews.py'),'--check'],cwd=ROOT)
    if rr.returncode:return rr.returncode
    print(f'Security-review validation clean: {len(files)} review file(s), {total} finding(s), {alignment_total} external alignment(s), RAHP and external-standard references resolved, Markdown current.')
    return 0
if __name__=='__main__':raise SystemExit(main())
