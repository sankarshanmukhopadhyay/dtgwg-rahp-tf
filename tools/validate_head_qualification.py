#!/usr/bin/env python3
"""Validate the committed v1.1 HEAD qualification record against curated example finding IDs."""
from pathlib import Path
import re, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
Q=ROOT/'examples/head-qualification/qualification.yaml'
allowed={"unchanged","weakened","resolved","strengthened","superseded","new"}
errors=[]
data=yaml.safe_load(Q.read_text())
q=data.get("qualification",{})
if q.get("status") != "complete": errors.append("qualification.status must be complete")
repos=q.get("targets",[])
if len(repos)!=11: errors.append(f"expected 11 live targets, found {len(repos)}")
seen=set()
for t in repos:
    repo=t.get("repository")
    if not repo or repo in seen: errors.append(f"duplicate/missing repository: {repo}")
    seen.add(repo)
    for fld in ("canonical_baseline","head"):
        v=t.get(fld,"")
        if not re.fullmatch(r"[0-9a-f]{40}",v): errors.append(f"{repo}: invalid {fld} {v!r}")

for path, deltas in q.get("finding_deltas",{}).items():
    p=ROOT/path
    if not p.exists():
        errors.append(f"missing referenced example {path}"); continue
    src=yaml.safe_load(p.read_text())
    review=src.get("review",src) if isinstance(src,dict) else {}
    ids={f.get("id") for f in review.get("findings",[]) if isinstance(f,dict)}
    seen_ids=set()
    for d in deltas:
        fid=d.get("finding")
        if fid not in ids: errors.append(f"{path}: unknown finding {fid}")
        if fid in seen_ids: errors.append(f"{path}: duplicate delta for {fid}")
        seen_ids.add(fid)
        if d.get("classification") not in allowed: errors.append(f"{path}/{fid}: invalid classification {d.get('classification')}")
    if seen_ids != ids:
        errors.append(f"{path}: qualification covers {len(seen_ids)}/{len(ids)} findings")

if errors:
    print("HEAD qualification validation: FAIL")
    for e in errors: print("-",e)
    sys.exit(1)
print(f"HEAD qualification validation: PASS ({len(repos)} repositories, {sum(len(v) for v in q.get('finding_deltas',{}).values())} finding deltas)")
