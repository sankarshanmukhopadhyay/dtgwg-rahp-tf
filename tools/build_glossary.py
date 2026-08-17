#!/usr/bin/env python3
from __future__ import annotations
import json, pathlib, yaml
ROOT=pathlib.Path(__file__).resolve().parent.parent
TERM_DIR=ROOT/'method/glossary/terms'
def load_terms():
    return [yaml.safe_load(p.read_text(encoding='utf-8')) for p in sorted(TERM_DIR.glob('*.yaml'))]
def build_outputs():
    terms=load_terms(); out=ROOT/'build'; out.mkdir(exist_ok=True)
    bundle={'glossary_version':'1.0.0','language':'en','writing_style':'simple English','terms':terms}
    (out/'glossary.json').write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    jsonld={'@context':{'rahp':'https://sankarshanmukhopadhyay.github.io/rahp-toolkit/glossary/','term':'rahp:term','definition':'rahp:definition','seeAlso':'rahp:seeAlso'},'@graph':[{'@id':'rahp:'+t['slug'],'@type':'rahp:GlossaryTerm','term':t['term'],'definition':t['definition'],'seeAlso':['rahp:'+x for x in t.get('see_also') or []]} for t in terms]}
    (out/'glossary.jsonld').write_text(json.dumps(jsonld,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    md=['# RAHP glossary','','RAHP terms in simple English. The authoritative source is `method/glossary/terms/`.','']
    for t in sorted(terms,key=lambda x:x['term'].lower()):
        md += [f"## {t['term']}",'',t['definition'],'']
        if t.get('plain_example'): md += [f"**Example:** {t['plain_example']}",'']
        if t.get('see_also'): md += ['**See also:** '+', '.join(t['see_also']),'']
    (out/'glossary.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    docs=['---','layout: default','title: "Glossary"','parent: Reference','nav_order: 3','has_toc: true','---','# RAHP glossary','','RAHP terms in simple English. The structured YAML files under `method/glossary/terms/` are authoritative. This page is generated from them.','']
    for t in sorted(terms,key=lambda x:x['term'].lower()):
        docs += [f"## {t['term']}",'',t['definition'],'']
        if t.get('plain_example'): docs += [f"**Example:** {t['plain_example']}",'']
        if t.get('see_also'): docs += ['**See also:** '+', '.join(f'`{x}`' for x in t['see_also']),'']
    (ROOT/'docs/glossary.md').write_text('\n'.join(docs)+'\n',encoding='utf-8')
    return terms

def main():
    terms=build_outputs(); print(f'Built glossary: {len(terms)} terms')
if __name__=='__main__': main()
