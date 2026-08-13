#!/usr/bin/env python3
"""Validate combined review linkage and generated synthesis."""
from __future__ import annotations
import pathlib,re,subprocess,sys
try: import yaml
except ImportError: sys.exit("validate_combined_reviews.py requires PyYAML")
ROOT=pathlib.Path(__file__).resolve().parent.parent
def load(p):
    with p.open(encoding="utf-8") as fh:return yaml.safe_load(fh) or {}
def main():
    errors=[]; files=sorted(ROOT.glob("examples/combined/**/combined-review.yaml"))
    for p in files:
        r=load(p).get("review") or {}; rel=p.relative_to(ROOT)
        for k in ["id","status","title","reviewed_on","target","rahp_review","security_review"]:
            if not r.get(k): errors.append(f"{rel}: review.{k} required")
        t=r.get("target") or {}; commit=str(t.get("commit") or "")
        if commit and not re.fullmatch(r"[0-9a-fA-F]{40}",commit): errors.append(f"{rel}: target.commit must be full SHA")
        for kind in ["rahp_review","security_review"]:
            ref=(p.parent/str(r.get(kind) or "")).resolve()
            if not ref.exists(): errors.append(f"{rel}: {kind} does not resolve: {r.get(kind)!r}"); continue
            other=(load(ref).get("review") or {}); ot=other.get("target") or {}
            for key in ["repository","commit"]:
                if t.get(key) and ot.get(key)!=t.get(key):
                    errors.append(f"{rel}: {kind} target.{key} differs from combined target")
    if errors:
        for e in errors: print("ERROR",e)
        print(f"\nCombined-review validation failed: {len(errors)} error(s)."); return 1
    rc=subprocess.run([sys.executable,str(ROOT/"tools"/"render_combined_reviews.py"),"--check"],cwd=ROOT).returncode
    if rc:return rc
    print(f"Combined-review validation clean: {len(files)} review file(s), linked targets consistent, Markdown current.")
    return 0
if __name__=="__main__": raise SystemExit(main())
