#!/usr/bin/env python3
from pathlib import Path
import yaml,sys
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'instances/cawg/mandate-readiness.yaml'; OUT=ROOT/'docs/cawg-mandate-readiness.md'
d=yaml.safe_load(SRC.read_text())
lines=['---','layout: default','title: "CAWG/C2PA mandate readiness"','nav_order: 13','has_toc: true','---','# CAWG/C2PA mandate readiness','', '> RAHP Toolkit assessment view. This is not a CAWG, DIF or C2PA conformance decision and does not assign legal effect to any assertion.','',f"Assessment date: **{d['assessment_date']}**",'', '## Portfolio view','', '| Surface | Technical | Governance | Security | Composition | Mandate readiness | Blocking risks |','|---|---|---|---|---|---|---|']
for r in d['records']:
    risks=', '.join(f'[`{x}`](cawg-risk-register.html#{x.lower()})' for x in r['blocking_risks'])
    lines.append(f"| {r['title']} | {r['technical']} | {r['governance']} | {r['security']} | {r['composition']} | **{r['mandate_readiness']}** | {risks} |")
lines += ['', '## Interpretation','', '- **Conditional** means technically usable in a bounded deployment only when the deployment supplies the missing trust/governance policy and accepts the cited residual risks.', '- **Pilot** means the surface is appropriate for controlled experimentation but should not yet be treated as a mandate baseline.', '- **Not ready** means unresolved semantics can change the meaning of a relying-party decision.', '', 'Read this table together with the [CAWG scenario corpus](../corpora/cawg.yaml), the [worked CAWG/C2PA reviews](../examples/cawg-c2pa/), and the [CAWG risk register](cawg-risk-register.html).','']
text='\n'.join(lines)
if '--check' in sys.argv:
    if not OUT.exists() or OUT.read_text()!=text: print('STALE docs/cawg-mandate-readiness.md'); raise SystemExit(1)
    print('CAWG mandate-readiness Markdown current.'); raise SystemExit(0)
OUT.write_text(text); print('[write] docs/cawg-mandate-readiness.md')
