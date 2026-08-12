#!/usr/bin/env python3
"""Validate the generated RAHP reference catalogue and deep links.

Ensures every canonical RAHP record has a stable catalogue anchor and every
catalogue deep-link emitted into generated review Markdown resolves to a known ID.
Run after tools/build.py.
"""
from __future__ import annotations

import pathlib
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("validate_reference_links.py requires PyYAML: pip install -r requirements.txt")

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOGUE = ROOT / "build" / "site" / "catalogue.html"


def load_yaml(path: pathlib.Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def canonical_ids() -> set[str]:
    instance = load_yaml(ROOT / "data" / "instance.yaml")
    result: set[str] = set()
    for spec in (instance.get("namespaces") or {}).values():
        path = ROOT / "data" / spec["file"]
        doc = load_yaml(path) if path.exists() else {}
        for rec in doc.get("records") or []:
            if rec.get("id"):
                result.add(str(rec["id"]))
    return result


def main() -> int:
    known = canonical_ids()
    if not CATALOGUE.exists():
        print("ERROR build/site/catalogue.html is missing — run python3 tools/build.py")
        return 1

    html = CATALOGUE.read_text(encoding="utf-8")
    anchors = set(re.findall(r'\bid="([A-Za-z0-9_-]+)"', html))
    missing = sorted(known - anchors)
    errors: list[str] = []
    if missing:
        errors.append(f"catalogue is missing {len(missing)} canonical anchor(s): {', '.join(missing[:20])}")

    link_re = re.compile(r'\]\((?:\.\./)+build/site/catalogue\.html#([A-Za-z0-9_-]+)\)')
    links_checked = 0
    review_files = sorted(set(ROOT.glob("examples/**/*.md")))
    for readme in review_files:
        text = readme.read_text(encoding="utf-8")
        for rid in link_re.findall(text):
            links_checked += 1
            if rid not in known:
                errors.append(f"{readme.relative_to(ROOT)} links unknown RAHP id {rid}")
            elif rid not in anchors:
                errors.append(f"{readme.relative_to(ROOT)} links {rid}, but catalogue anchor is missing")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"\nRAHP reference-link validation failed: {len(errors)} error(s).")
        return 1

    print(f"RAHP reference links clean: {len(known)} catalogue anchors, {links_checked} generated review links checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
