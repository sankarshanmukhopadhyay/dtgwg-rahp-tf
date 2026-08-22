#!/usr/bin/env python3
"""Validate portable remediation and retest lineage plus closure invariants."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "method" / "schema"
FIXTURE_DIR = ROOT / "examples" / "assurance-lineage"


def load_yaml(name: str):
    return yaml.safe_load((FIXTURE_DIR / name).read_text(encoding="utf-8"))


def validate(doc, schema_name: str):
    schema = json.loads((SCHEMA_DIR / schema_name).read_text(encoding="utf-8"))
    return sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(doc), key=lambda e: list(e.path))


def main() -> int:
    remediation = load_yaml("generic-remediation.yaml")
    retest = load_yaml("generic-retest.yaml")
    errors: list[str] = []

    for label, doc, schema in [
        ("remediation", remediation, "remediation-manifest.schema.json"),
        ("retest", retest, "retest.schema.json"),
    ]:
        for err in validate(doc, schema):
            loc = ".".join(str(p) for p in err.absolute_path) or "(record)"
            errors.append(f"{label} schema {loc}: {err.message}")

    if remediation.get("remediation_id") != retest.get("remediation_id"):
        errors.append("retest remediation_id does not resolve to the remediation fixture")
    if remediation.get("assessment_id") != retest.get("assessment_id"):
        errors.append("retest assessment_id does not match remediation assessment_id")
    if remediation.get("finding_id") != retest.get("previous_finding"):
        errors.append("retest previous_finding does not match remediation finding_id")
    if remediation.get("assessment_run_id") != retest.get("previous_run_id"):
        errors.append("retest previous_run_id does not match remediation assessment_run_id")

    criteria = {item["id"] for item in remediation.get("acceptance_criteria") or []}
    referenced = set(retest.get("acceptance_criteria") or [])
    if not referenced.issubset(criteria):
        errors.append("retest references acceptance criteria not defined by remediation")

    evidence_by_criterion = {}
    for evidence in retest.get("closure_evidence") or []:
        cid = evidence.get("criterion_id")
        if cid:
            evidence_by_criterion.setdefault(cid, []).append(evidence.get("result"))

    if retest.get("outcome") == "resolved":
        missing = [cid for cid in referenced if "pass" not in evidence_by_criterion.get(cid, [])]
        nonpassing = [e.get("id") for e in retest.get("closure_evidence") or [] if e.get("result") != "pass"]
        if missing:
            errors.append(f"resolved retest lacks passing evidence for: {', '.join(sorted(missing))}")
        if nonpassing:
            errors.append(f"resolved retest contains non-passing closure evidence: {', '.join(nonpassing)}")
        disposition = retest.get("disposition") or {}
        if disposition.get("status") not in {"eligible-for-closure", "closed"}:
            errors.append("resolved retest must be eligible-for-closure or closed")
        if not disposition.get("authority_basis"):
            errors.append("resolved retest requires an explicit disposition authority basis")

    if retest.get("outcome") in {"inconclusive", "indeterminate"} and (retest.get("disposition") or {}).get("status") == "closed":
        errors.append("inconclusive or indeterminate retest cannot be closed")

    close_authority = (remediation.get("authority") or {}).get("close") or []
    if (retest.get("disposition") or {}).get("status") == "closed" and not close_authority:
        errors.append("closed retest requires remediation close authority")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Portable remediation/retest lineage validation passed: governed closure evidence and authority invariants satisfied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
