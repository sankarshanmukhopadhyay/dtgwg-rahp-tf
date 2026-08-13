#!/usr/bin/env python3
"""Create a review packet for one corpus; never mutates the corpus automatically."""
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parent.parent

def y(path): return yaml.safe_load(path.read_text(encoding='utf-8')) or {}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('corpus_id'); ap.add_argument('--output',default='build/corpus-review.md'); a=ap.parse_args()
    manifest=y(ROOT/'corpora/sources.yaml'); item=next((x for x in manifest.get('sources',[]) if x.get('corpus_id')==a.corpus_id),None)
    if not item: print(f'Unknown corpus id: {a.corpus_id}',file=sys.stderr); return 2
    tmp=ROOT/'build/.corpus-status.json'
    subprocess.run([sys.executable,str(ROOT/'tools/corpus_status.py'),'--json',str(tmp),'--markdown',str(ROOT/'build/.corpus-status.md')],check=False,cwd=ROOT)
    report=json.loads(tmp.read_text()) if tmp.exists() else {'results':[]}
    r=next((x for x in report.get('results',[]) if x.get('corpus_id')==a.corpus_id),{})
    c=y(ROOT/item['corpus_file']).get('corpus') or {}
    src=item.get('source') or {}
    lines=[f'# Corpus review packet: {a.corpus_id}','',
           '> This packet assists review. It does not authorize advancing `source_commit` or changing scenario semantics.','',
           '## Provenance','',f"- Corpus file: `{item['corpus_file']}`",f"- Adapter version: `{c.get('adapter_version','')}`",
           f"- Source repository: `{src.get('repository','derived')}`",f"- Tracked branch: `{src.get('branch','main')}`",
           f"- Current source pin: `{c.get('source_commit','')}`",f"- Observed HEAD: `{r.get('observed_head','unknown')}`",
           f"- Status: **{r.get('status','unknown')}**",'', '## Tracked source paths','']
    lines += [f'- `{p}`' for p in src.get('paths',[])] or ['- Derived from other corpora.']
    lines += ['', '## Relevant changed files','']
    lines += [f'- `{p}`' for p in r.get('relevant_changed_files',[])] or ['- Not available or no tracked-path change detected.']
    lines += ['', '## Reviewer checklist','',
              '- [ ] Confirm the source repository and branch are still the intended authority for this adapter.',
              '- [ ] Read changes in every relevant tracked source file; do not infer semantic equivalence from filenames alone.',
              '- [ ] Identify source scenarios added, removed, renamed, split, merged or semantically changed.',
              '- [ ] Re-evaluate affected `SP-*` mappings and cross-spec dependencies.',
              '- [ ] Update scenario-level `source_anchor` values where source structure moved.',
              '- [ ] Run `python3 tools/validate_scenario_corpora.py` and affected RAHP/security/combined reviews.',
              '- [ ] Only after semantic review, replace `source_commit` with the reviewed immutable HEAD SHA and update provenance status.',
              '', '## AI-agent handoff prompt','',
              'Ask an agent to compare the pinned source with the observed HEAD, classify only changes affecting tracked source paths, propose (not silently apply) scenario/mapping edits, cite every source location, and leave source-pin advancement for human approval.', '']
    out=ROOT/a.output; out.parent.mkdir(parents=True,exist_ok=True); out.write_text('\n'.join(lines),encoding='utf-8'); print(out.relative_to(ROOT)); return 0
if __name__=='__main__': raise SystemExit(main())
