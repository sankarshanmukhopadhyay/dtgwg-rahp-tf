#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import sys

ROOT = Path(__file__).resolve().parent.parent
SITE = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / '_site'

REQUIRED_PROJECTIONS = [
    'corpora/dtg-zkp.yaml',
    'corpora/trust-tasks.yaml',
    'corpora/credential-spec.yaml',
    'corpora/trust-tasks-credspec-composed.yaml',
]
REQUIRED_DOCS = [
    'index.html',
    'docs/using-an-ai-agent.html',
    'docs/pages-coverage.html',
    'README.md',
    'QUICKSTART.md',
    'ADOPTION.md',
    'examples/dtg-credential-spec/README.md',
    'examples/security-hardening/credential-spec/SECURITY_REVIEW.md',
]

class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            href = dict(attrs).get('href')
            if href:
                self.links.append(href)

errors = []
htmls = list(SITE.rglob('*.html'))
if not htmls:
    print(f'ERROR {SITE} contains no HTML')
    raise SystemExit(1)

for required in REQUIRED_DOCS + REQUIRED_PROJECTIONS:
    target = SITE / required
    if not target.exists():
        errors.append(f'missing required Pages projection: {required}')
    elif required.endswith(('.yaml', '.yml', '.json', '.jsonld')):
        head = target.read_text(errors='ignore')[:1000].lower()
        if '<!doctype html' not in head and '<html' not in head:
            errors.append(f'structured-data path was not rendered as HTML: {required}')

for page in htmls:
    p = P()
    p.feed(page.read_text(errors='ignore'))
    for href in p.links:
        if href.startswith(('#', 'mailto:', 'javascript:')):
            continue
        u = urlparse(href)
        if u.scheme or u.netloc:
            continue
        path = unquote(u.path)
        if not path:
            continue
        if path.startswith('/dtgwg-rahp-tf/'):
            path = path[len('/dtgwg-rahp-tf/'):]
            target = SITE / path
        elif path.startswith('/'):
            continue
        else:
            target = page.parent / path
        if target.is_dir():
            target = target / 'index.html'
        if target.suffix == '':
            a = target.with_suffix('.html')
            b = target / 'index.html'
            if a.exists():
                target = a
            elif b.exists():
                target = b
        if not target.exists():
            errors.append(f'{page.relative_to(SITE)} -> {href}')

if errors:
    for e in errors[:80]:
        print('ERROR', e)
    print(f'JTD site validation failed: {len(errors)} error(s).')
    raise SystemExit(1)

print(f'JTD site validation clean: {len(htmls)} HTML page(s); required structured-data projections present.')
