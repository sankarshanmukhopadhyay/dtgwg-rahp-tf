#!/usr/bin/env python3
from pathlib import Path
import sys, re, yaml
ROOT=Path(__file__).resolve().parent.parent
patdoc=yaml.safe_load((ROOT/'method/scenario-patterns.yaml').read_text()) or {}
patterns={p['id'] for p in patdoc.get('patterns',[])}
errors=[]; corpora=0; scenarios=0
manifest_path=ROOT/'corpora/sources.yaml'
manifest=yaml.safe_load(manifest_path.read_text()) if manifest_path.exists() else {}
manifest_sources={x.get('corpus_id'):x for x in (manifest or {}).get('sources',[]) if isinstance(x,dict)}
if not manifest_sources: errors.append('corpora/sources.yaml defines no corpus sources')
if not patterns: errors.append('method/scenario-patterns.yaml defines no patterns')
for path in sorted((ROOT/'corpora').glob('*.yaml')):
    if path.name == 'sources.yaml':
        continue
    corpora+=1; doc=yaml.safe_load(path.read_text()) or {}; c=doc.get('corpus') or {}
    for f in ('id','title','adapter_version','description','scenarios'):
        if not c.get(f): errors.append(f'{path.relative_to(ROOT)}: corpus.{f} is required')
    cid=c.get('id')
    source_cfg=manifest_sources.get(cid)
    if not source_cfg: errors.append(f'{path.relative_to(ROOT)}: corpus id {cid} missing from corpora/sources.yaml')
    elif source_cfg.get('corpus_file') != str(path.relative_to(ROOT)):
        errors.append(f'{path.relative_to(ROOT)}: sources.yaml corpus_file mismatch for {cid}')
    if source_cfg and source_cfg.get('update_mode') == 'derived':
        if not c.get('depends_on'): errors.append(f'{path.relative_to(ROOT)}: derived corpus requires corpus.depends_on')
        dep_ids={d.get('corpus_id') for d in (c.get('depends_on') or []) if isinstance(d,dict)}
        for dep in source_cfg.get('dependencies') or []:
            if dep not in dep_ids: errors.append(f'{path.relative_to(ROOT)}: missing declared dependency {dep}')
    else:
        for f in ('source_repository','source_path','source_commit'):
            if not c.get(f): errors.append(f'{path.relative_to(ROOT)}: corpus.{f} is required')
        if source_cfg:
            src=source_cfg.get('source') or {}
            for f in ('repository','portfolio_repository','relationship_to_portfolio','paths'):
                if not src.get(f): errors.append(f'{path.relative_to(ROOT)}: sources.yaml source.{f} is required')
            if src.get('repository') and c.get('source_repository') != src.get('repository'):
                errors.append(f'{path.relative_to(ROOT)}: source_repository differs from corpora/sources.yaml')
    seen=set()
    for s in c.get('scenarios') or []:
        scenarios+=1; sid=str(s.get('id') or '')
        if not sid: errors.append(f'{path.relative_to(ROOT)}: scenario id required'); continue
        if sid in seen: errors.append(f'{path.relative_to(ROOT)}: duplicate scenario id {sid}')
        seen.add(sid)
        for f in ('title','domain','primary_goal','primary_pressure','priority','scenario_patterns'):
            if not s.get(f): errors.append(f'{path.relative_to(ROOT)}:{sid}: {f} is required')
        refs=s.get('scenario_patterns') or []
        if not isinstance(refs,list): errors.append(f'{path.relative_to(ROOT)}:{sid}: scenario_patterns must be a list'); continue
        for ref in refs:
            if ref not in patterns: errors.append(f'{path.relative_to(ROOT)}:{sid}: unknown scenario pattern {ref}')
if corpora==0: errors.append('no corpora/*.yaml files found')
for cid,item in manifest_sources.items():
    cf=ROOT/str(item.get('corpus_file',''))
    if not cf.exists(): errors.append(f'corpora/sources.yaml: {cid} references missing {item.get("corpus_file")}')
if errors:
    for e in errors: print('ERROR',e)
    print(f'Scenario corpus validation failed: {len(errors)} error(s).'); raise SystemExit(1)
print(f'Scenario corpus validation clean: {corpora} corpus/corpora, {scenarios} scenarios, {len(patterns)} portable patterns.')
