#!/usr/bin/env python3
"""Validate implementation/documentation synchronization for declared v1.5 capabilities."""
from __future__ import annotations

from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "method" / "capability-documentation.yaml"
ROADMAP = ROOT / "ROADMAP.md"


def main() -> int:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    errors: list[str] = []
    ids: list[str] = []

    if data.get("development_target") != "1.5.0":
        errors.append("capability documentation registry must target v1.5.0")

    for capability in data.get("capabilities") or []:
        cid = capability.get("id")
        if not cid:
            errors.append("capability without id")
            continue
        if cid in ids:
            errors.append(f"duplicate capability id: {cid}")
        ids.append(cid)

        for field in ("schemas", "tools", "tests"):
            for rel in capability.get(field) or []:
                if not (ROOT / rel).is_file():
                    errors.append(f"{cid}: missing {field[:-1]} path {rel}")

        doc_rel = capability.get("documentation")
        if not doc_rel or not (ROOT / doc_rel).is_file():
            errors.append(f"{cid}: missing documentation path {doc_rel!r}")
            continue
        text = (ROOT / doc_rel).read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{cid}: documentation is not a rendered Pages source: {doc_rel}")
        lower = text.lower()
        for term in capability.get("required_terms") or []:
            if str(term).lower() not in lower:
                errors.append(f"{cid}: documentation {doc_rel} missing required semantic term {term!r}")

    roadmap = ROADMAP.read_text(encoding="utf-8")
    required_headings = [
        "Durable assessment and finding lineage",
        "Governed remediation and retest",
        "Assurance graph and impact analysis",
        "Evidence provenance and assurance freshness",
        "Executable authority and policy gates",
    ]
    for heading in required_headings:
        if heading not in roadmap:
            errors.append(f"ROADMAP.md missing v1.5 capability heading: {heading}")

    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(f"PASS capability documentation sync: {len(ids)} v1.5 capabilities have implementation, test and rendered-documentation coverage.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
