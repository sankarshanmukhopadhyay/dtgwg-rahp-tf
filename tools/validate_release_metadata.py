#!/usr/bin/env python3
"""Validate current release surfaces agree with package/release metadata."""
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
package = json.loads((ROOT / 'package.json').read_text())
version = package['version']
tag = f'v{version}'
errors = []

checks = [
    ('README release banner', ROOT / 'README.md', rf'Release {re.escape(tag)}\b'),
    ('README current release link', ROOT / 'README.md', rf'\[{re.escape(tag)} release notes\]\(docs/releases/{re.escape(tag)}\.md\)'),
    ('release notes', ROOT / 'docs' / 'releases' / f'{tag}.md', None),
    ('CHANGELOG current release', ROOT / 'CHANGELOG.md', rf'^## {re.escape(tag)}\b'),
    ('ROADMAP current release', ROOT / 'ROADMAP.md', rf'^## {re.escape(tag)}\b'),
]
for label, path, pattern in checks:
    if not path.exists():
        errors.append(f'{label}: missing {path.relative_to(ROOT)}')
        continue
    if pattern and not re.search(pattern, path.read_text(), re.M):
        errors.append(f'{label}: expected {tag}')

portable = ROOT / 'examples' / 'portable-instance' / 'data' / 'instance.yaml'
if portable.exists() and f'toolkit_version: {tag}' not in portable.read_text():
    errors.append(f'portable instance fixture: expected toolkit_version: {tag}')

if errors:
    for error in errors:
        print(f'ERROR: {error}')
    sys.exit(1)
print(f'PASS release metadata: {tag}')
