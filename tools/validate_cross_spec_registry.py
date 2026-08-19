#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parent.parent
REG=ROOT/'instances/dtg/cross-spec-tests.yaml'

def main()->int:
    d=yaml.safe_load(REG.read_text(encoding='utf-8')) or {}; errors=[]; seen=set()
    comps=d.get('compositions',[])
    if not isinstance(comps,list) or not comps: errors.append('compositions must be a non-empty list')
    for i,c in enumerate(comps):
        cid=c.get('id'); p=f'compositions[{i}]'
        if not cid or cid in seen: errors.append(f'{p}.id must be present and unique')
        seen.add(cid)
        parts=c.get('components',[])
        if not isinstance(parts,list) or len(parts)!=2: errors.append(f'{p}.components must contain exactly two repositories')
        for part in parts:
            if '/' not in str(part.get('repository','')): errors.append(f'{p} has invalid repository')
        if c.get('runnable'):
            for key in ('corpus_id','assessment'):
                if not c.get(key): errors.append(f'{p}.{key} required when runnable')
            if c.get('assessment') and not (ROOT/c['assessment']).exists(): errors.append(f"{p}.assessment does not exist: {c['assessment']}")
    if errors:
        print('\n'.join(f'ERROR: {e}' for e in errors),file=sys.stderr); return 1
    print(f'cross-spec registry valid: {len(comps)} declared, {sum(bool(c.get("runnable")) for c in comps)} runnable')
    return 0
if __name__=='__main__': raise SystemExit(main())
