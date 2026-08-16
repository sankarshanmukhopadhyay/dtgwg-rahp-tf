#!/usr/bin/env python3
"""Guard the project/deployment identity boundary in active documentation."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

# Historical release notes and archive are provenance; active guidance must use the neutral project identity.
ACTIVE = [
    ROOT / 'README.md', ROOT / 'ADOPTION.md', ROOT / 'CONTRIBUTING.md', ROOT / 'ROADMAP.md', ROOT / 'index.md',
    *sorted((ROOT / 'docs').glob('*.md')),
    *sorted((ROOT / 'docs' / 'diagrams').glob('*.md')),
]

errors = []
for path in ACTIVE:
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    rel = path.relative_to(ROOT)
    if 'dtgwg-rahp-tf' in text:
        errors.append(f"{rel}: legacy repository identity 'dtgwg-rahp-tf' appears in active guidance")

required = {
    ROOT / 'README.md': ['# RAHP Toolkit', '## The v0.9 architecture', 'CAWG/C2PA', 'Bundled DTG exemplar'],
    ROOT / 'docs' / 'index.md': ['title: "RAHP Toolkit documentation"', 'RAHP is not the DTG deployment', 'CAWG/C2PA'],
    ROOT / 'ADOPTION.md': ['# Adopting RAHP', 'shared engine contract, independent deployment context'],
    ROOT / 'CONTRIBUTING.md': ['instances/<id>/', 'bundled DTG exemplar'],
    ROOT / 'docs' / 'portability.md': ['RAHP is portable by construction'],
}
for path, phrases in required.items():
    text = path.read_text(encoding='utf-8')
    for phrase in phrases:
        if phrase not in text:
            errors.append(f"{path.relative_to(ROOT)}: required identity phrase missing: {phrase!r}")

# The documentation landing page must never masquerade as a deployment page.
index = (ROOT / 'docs' / 'index.md').read_text(encoding='utf-8')
if 'title: "DTG instance"' in index:
    errors.append('docs/index.md: documentation home is incorrectly titled as the DTG instance')

if errors:
    for e in errors:
        print('ERROR', e)
    print(f"Project identity validation failed: {len(errors)} error(s).")
    sys.exit(1)
print(f"Project identity validation clean: {len(ACTIVE)} active guidance files checked.")
