#!/usr/bin/env python3
"""Validate worked RAHP specification pressure-test records.

Checks every examples/**/pressure-test.yaml against the canonical DTG RAHP
instance. This complements tools/validate.py: the main validator checks the RAHP
corpus; this validator checks review records that consume that corpus.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("validate_pressure_tests.py requires PyYAML: pip install -r requirements.txt")

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
VOCAB = ROOT / "method" / "vocabularies.yaml"


def load_yaml(path: pathlib.Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def ids(filename: str) -> set[str]:
    doc = load_yaml(DATA / filename)
    return {str(r.get("id")) for r in doc.get("records", []) if r.get("id")}


def dispositions() -> set[str]:
    doc = load_yaml(VOCAB)
    return set(doc.get("finding_disposition", {}).get("values", []))


def main() -> int:
    known = {
        "risks": ids("risks.yaml"),
        "controls": ids("controls.yaml"),
        "guardrails": ids("guardrails.yaml"),
        "assurance_tests": ids("assurance-tests.yaml"),
    }
    allowed_dispositions = dispositions()
    allowed_status = {"in-progress", "complete", "open", "monitoring", "resolved", "superseded"}
    allowed_severity = {"Low", "Medium", "High", "Critical"}

    files = sorted(ROOT.glob("examples/**/pressure-test.yaml"))
    if not files:
        print("ERROR no examples/**/pressure-test.yaml files found")
        return 1

    errors: list[str] = []
    findings_seen = 0

    for path in files:
        rel = path.relative_to(ROOT)
        doc = load_yaml(path)
        review = doc.get("review")
        if not isinstance(review, dict):
            errors.append(f"{rel}: missing review mapping")
            continue

        for field in ("id", "status", "title", "reviewed_on", "target", "reviewed_against"):
            if not review.get(field):
                errors.append(f"{rel}: review.{field} is required")

        if review.get("status") not in allowed_status:
            errors.append(f"{rel}: review.status={review.get('status')!r} is not permitted")

        target = review.get("target") or {}
        for field in ("repository", "version", "commit"):
            if not target.get(field):
                errors.append(f"{rel}: review.target.{field} is required")
        commit = str(target.get("commit") or "")
        if commit and not re.fullmatch(r"[0-9a-fA-F]{40}", commit):
            errors.append(f"{rel}: review.target.commit must be a full 40-character commit SHA")

        against = review.get("reviewed_against") or {}
        if not against.get("rahp_version"):
            errors.append(f"{rel}: review.reviewed_against.rahp_version is required")

        if "findings" not in review:
            errors.append(f"{rel}: review.findings is required")
            findings = []
        else:
            findings = review.get("findings")
        if not isinstance(findings, list):
            errors.append(f"{rel}: review.findings must be a list")
            continue
        if not findings and review.get("status") != "in-progress":
            errors.append(f"{rel}: completed/non-draft review.findings must be non-empty")
            continue

        local_ids: set[str] = set()
        for finding in findings:
            findings_seen += 1
            fid = str(finding.get("id") or "")
            prefix = f"{rel}:{fid or '<no-id>'}"
            if not re.fullmatch(r"F-[0-9]{3}", fid):
                errors.append(f"{prefix}: id must match F-000")
            if fid in local_ids:
                errors.append(f"{prefix}: duplicate finding id")
            local_ids.add(fid)

            for field in ("title", "status", "severity", "primary_disposition", "risks", "evidence", "harm", "recommendation", "retest_when"):
                if not finding.get(field):
                    errors.append(f"{prefix}: {field} is required")

            if finding.get("status") not in allowed_status:
                errors.append(f"{prefix}: status={finding.get('status')!r} is not permitted")
            if finding.get("severity") not in allowed_severity:
                errors.append(f"{prefix}: severity={finding.get('severity')!r} is not permitted")

            primary = finding.get("primary_disposition")
            if primary not in allowed_dispositions:
                errors.append(f"{prefix}: primary_disposition={primary!r} is not in method/vocabularies.yaml")
            for d in finding.get("secondary_dispositions") or []:
                if d not in allowed_dispositions:
                    errors.append(f"{prefix}: secondary disposition {d!r} is not permitted")

            for field, valid in known.items():
                refs = finding.get(field) or []
                if not isinstance(refs, list):
                    errors.append(f"{prefix}: {field} must be a list")
                    continue
                for ref in refs:
                    if ref not in valid:
                        errors.append(f"{prefix}: {field} reference {ref!r} does not resolve")

            evidence = finding.get("evidence") or []
            if not isinstance(evidence, list):
                errors.append(f"{prefix}: evidence must be a list")
            else:
                for n, ev in enumerate(evidence, 1):
                    if not isinstance(ev, dict) or not ev.get("source") or not ev.get("observation"):
                        errors.append(f"{prefix}: evidence[{n}] requires source and observation")

        summary = review.get("summary") or {}
        if "finding_count" in summary and summary.get("finding_count") != len(findings):
            errors.append(f"{rel}: summary.finding_count={summary.get('finding_count')} but {len(findings)} findings are recorded")
        if "open_count" in summary:
            actual_open = sum(1 for f in findings if f.get("status") == "open")
            if summary.get("open_count") != actual_open:
                errors.append(f"{rel}: summary.open_count={summary.get('open_count')} but {actual_open} findings are open")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"\nPressure-test validation failed: {len(errors)} error(s) across {len(files)} review file(s).")
        return 1

    renderer = ROOT / "tools" / "render_pressure_tests.py"
    rendered = subprocess.run([sys.executable, str(renderer), "--check"], cwd=ROOT, text=True)
    if rendered.returncode != 0:
        print("\nPressure-test validation failed: generated Markdown is missing or stale.")
        return 1

    print(f"Pressure-test validation clean: {len(files)} review file(s), {findings_seen} finding(s), all references resolved, Markdown current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
