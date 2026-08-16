#!/usr/bin/env python3
"""Render combined RAHP + security review synthesis reports."""
from __future__ import annotations
import argparse, pathlib, re, sys
from typing import Any
try: import yaml
except ImportError: sys.exit("render_combined_reviews.py requires PyYAML")

ROOT=pathlib.Path(__file__).resolve().parent.parent

def load(p):
    with p.open(encoding="utf-8") as fh:return yaml.safe_load(fh) or {}

def cell(v):
    if v is None:return "—"
    return re.sub(r"\s+"," ",str(v).strip()).replace("|","\\|") or "—"

def resolve(base:pathlib.Path,rel:str)->pathlib.Path:
    return (base/rel).resolve()

def overlap_detail(rf,sf):
    rahp=sf.get("rahp") or {}
    groups={
      "risks": set(rf.get("risks") or []) & set(rahp.get("risks") or []),
      "guardrails": set(rf.get("guardrails") or []) & set(rahp.get("guardrails") or []),
      "controls": set(rf.get("controls") or []) & set(rahp.get("controls") or []),
      "assurance_tests": set(rf.get("assurance_tests") or []) & set(rahp.get("assurance_tests") or []),
    }
    score=5*len(groups["risks"])+3*len(groups["guardrails"])+2*len(groups["controls"])+len(groups["assurance_tests"])
    shared=sorted(set().union(*groups.values()))
    return score,shared,groups

def strongest_pairs(rfs,sfs):
    pairs=[]
    for rf in rfs:
        candidates=[]
        for sf in sfs:
            score,shared,groups=overlap_detail(rf,sf)
            # A shared risk is inherently meaningful. Without one, require a
            # stronger combination than a single widely reused control/test.
            meaningful=bool(groups["risks"]) or score>=7
            if meaningful: candidates.append((score,sf,shared))
        candidates.sort(key=lambda x:(-x[0],str(x[1].get("id") or "")))
        for score,sf,shared in candidates[:2]: pairs.append((rf,sf,shared,score))
    return pairs

def render(path):
    c=(load(path).get("review") or {})
    rp=resolve(path.parent,str(c.get("rahp_review") or ""))
    sp=resolve(path.parent,str(c.get("security_review") or ""))
    rr=(load(rp).get("review") or {}); sr=(load(sp).get("review") or {})
    rfs=rr.get("findings") or []; sfs=sr.get("findings") or []
    pairs=strongest_pairs(rfs,sfs)
    target=c.get("target") or {}; against=c.get("reviewed_against") or {}
    lines=[f"# {cell(c.get('title'))}","",
      "> Generated from the linked RAHP pressure-test and security-hardening YAML records. This report is a cross-lens synthesis, not a third independent test.","",
      "## Review metadata","",
      "| Field | Value |","|---|---|",
      f"| Combined review | `{cell(c.get('id'))}` |",
      f"| Status | {cell(c.get('status'))} |",
      f"| Reviewed on | {cell(c.get('reviewed_on'))} |",
      f"| Target | `{cell(target.get('repository'))}` |",
      f"| Version | {cell(target.get('version'))} |",
      f"| Commit | `{cell(target.get('commit'))}` |",
      f"| RAHP review | `{cell(rr.get('id'))}` — {len(rfs)} finding(s) |",
      f"| Security review | `{cell(sr.get('id'))}` — {len(sfs)} finding(s) |",
      f"| RAHP version | `{cell(against.get('rahp_version'))}` |",
      f"| Engine contract | `{cell(against.get('engine_contract'))}` |",
      f"| Engine/method revalidated on | {cell(against.get('revalidated_on'))} |","",
      "## How to read the combined view","",
      "The RAHP lens asks what harms, governance failures, assurance gaps, and affected-party consequences remain. The security lens asks how an adversary or compromised component can violate a security property. The synthesis below uses shared canonical RAHP context as a heuristic, weighted toward shared risks and guardrails. It shows only the strongest connections and does not imply that paired findings are identical.","",
      "## Strongest cross-lens connections",""]
    if not pairs:
        lines += ["No cross-lens overlaps are recorded yet. This is normal for an in-progress scaffold or where the two lenses identify genuinely distinct concerns.",""]
    else:
        lines += ["| RAHP finding | Security finding | Shared RAHP context |","|---|---|---|"]
        for rf,sf,shared,score in pairs:
            lines.append(f"| `{cell(rf.get('id'))}` — {cell(rf.get('title'))} | `{cell(sf.get('id'))}` — {cell(sf.get('title'))} | {', '.join(f'`{x}`' for x in shared)} |")
        lines += [""]
    lines += ["## RAHP-only findings",""]
    sec_linked={rf.get("id") for rf,sf,sh,score in pairs}
    lone=[f for f in rfs if f.get("id") not in sec_linked]
    lines += ([f"- `{cell(f.get('id'))}` — {cell(f.get('title'))}" for f in lone] or ["None."]) + [""]
    lines += ["## Security-only findings",""]
    r_linked={sf.get("id") for rf,sf,sh,score in pairs}
    lone=[f for f in sfs if f.get("id") not in r_linked]
    lines += ([f"- `{cell(f.get('id'))}` — {cell(f.get('title'))}" for f in lone] or ["None."]) + [""]
    notes=c.get("notes") or []
    if notes: lines += ["## Reviewer synthesis notes",""]+[f"- {cell(n)}" for n in notes]+[""]
    return "\n".join(lines).rstrip()+"\n"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--slug"); a=ap.parse_args()
    files=sorted(ROOT.glob("examples/combined/**/combined-review.yaml"))
    if a.slug: files=[p for p in files if p.parent.name==a.slug]
    stale=[]
    for y in files:
        out=y.with_name("COMBINED_REVIEW.md")
        try: expected=render(y)
        except Exception as e: print(f"ERROR {y.relative_to(ROOT)}: {e}"); stale.append(y); continue
        current=out.read_text(encoding="utf-8") if out.exists() else ""
        if current!=expected:
            if a.check: print(f"STALE {out.relative_to(ROOT)} — run: python3 tools/render_combined_reviews.py"); stale.append(out)
            else: out.write_text(expected,encoding="utf-8"); print(f"[write] {out.relative_to(ROOT)}")
        else: print(f"[ok] {out.relative_to(ROOT)}")
    if stale:return 1
    print(f"Combined-review Markdown {'current' if a.check else 'rendered'}: {len(files)} review file(s).")
    return 0
if __name__=="__main__": raise SystemExit(main())
