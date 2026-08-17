#!/usr/bin/env python3
from __future__ import annotations
import json, pathlib, re, sys
import yaml
from jsonschema import Draft202012Validator
ROOT=pathlib.Path(__file__).resolve().parent.parent
SCHEMA=json.loads((ROOT/'method/schema/glossary-term.schema.json').read_text())
TERM_DIR=ROOT/'method/glossary/terms'
SIMPLE_WORD_RE=re.compile(r'\b(?:hereinafter|thereof|wherein|pursuant|notwithstanding|aforementioned)\b',re.I)
def main():
    errors=[]; warnings=[]; docs={}
    validator=Draft202012Validator(SCHEMA)
    for p in sorted(TERM_DIR.glob('*.yaml')):
        d=yaml.safe_load(p.read_text(encoding='utf-8')) or {}
        for e in validator.iter_errors(d): errors.append(f'{p.relative_to(ROOT)}: {e.message}')
        slug=d.get('slug','')
        if slug and p.stem!=slug: errors.append(f'{p.relative_to(ROOT)}: filename must match slug {slug}')
        if slug in docs: errors.append(f'duplicate glossary slug: {slug}')
        docs[slug]=d
        definition=str(d.get('definition') or '')
        if len(definition.split())>45: warnings.append(f'{slug}: definition is longer than 45 words; simplify if possible')
        if SIMPLE_WORD_RE.search(definition): errors.append(f'{slug}: definition uses avoidable legal/formal language')
    for slug,d in docs.items():
        for ref in (d.get('see_also') or [])+(d.get('do_not_confuse_with') or []):
            if ref not in docs: errors.append(f'{slug}: glossary reference {ref} does not resolve')
    if len(docs)<40: errors.append(f'glossary must contain at least 40 core terms; found {len(docs)}')
    for e in errors: print('ERROR',e)
    for w in warnings: print('WARN ',w)
    if errors: print(f'Glossary validation failed: {len(errors)} error(s), {len(warnings)} warning(s).'); return 1
    print(f'Glossary validation clean: {len(docs)} term(s), {len(warnings)} warning(s).')
    return 0
if __name__=='__main__': raise SystemExit(main())
