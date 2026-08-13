#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import sys
ROOT=Path(__file__).resolve().parent.parent; SITE=ROOT/'_site'
class P(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]
    def handle_starttag(self,tag,attrs):
        if tag=='a':
            href=dict(attrs).get('href');
            if href: self.links.append(href)
errors=[]; htmls=list(SITE.rglob('*.html'))
if not htmls: print('ERROR _site contains no HTML'); raise SystemExit(1)
for page in htmls:
    p=P(); p.feed(page.read_text(errors='ignore'))
    for href in p.links:
        if href.startswith(('#','mailto:','javascript:')): continue
        u=urlparse(href)
        if u.scheme or u.netloc: continue
        path=unquote(u.path)
        if not path: continue
        # Jekyll baseurl links are absolute within deployed site; resolve after stripping repo base.
        if path.startswith('/dtgwg-rahp-tf/'): path=path[len('/dtgwg-rahp-tf/'):]
        elif path.startswith('/'): continue
        target=(SITE/path) if path.startswith('/') is False and href.startswith('/') else (page.parent/path)
        if href.startswith('/dtgwg-rahp-tf/'): target=SITE/path
        if target.is_dir(): target=target/'index.html'
        if target.suffix=='':
            a=target.with_suffix('.html'); b=target/'index.html'
            if a.exists(): target=a
            elif b.exists(): target=b
        if not target.exists(): errors.append(f'{page.relative_to(SITE)} -> {href}')
if errors:
    for e in errors[:50]: print('ERROR broken rendered link',e)
    print(f'JTD site validation failed: {len(errors)} broken local link(s).'); raise SystemExit(1)
print(f'JTD site validation clean: {len(htmls)} HTML page(s).')
