#!/usr/bin/env python3
"""Validate portable evidence provenance, freshness and assurance-delta contracts."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker

from assurance_state import conclusion_transition, freshness_from_basis

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "method" / "schema"
FIXTURE_DIR = ROOT / "examples" / "assurance-lineage"


def load_yaml(name: str):
    return yaml.safe_load((FIXTURE_DIR / name).read_text(encoding="utf-8"))


def validate(doc, schema_name: str) -> list[str]:
    schema = json.loads((SCHEMA_DIR / schema_name).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    for err in sorted(validator.iter_errors(doc), key=lambda e: list(e.path)):
        location = ".".join(str(p) for p in err.absolute_path) or "(record)"
        errors.append(f"{schema_name} {location}: {err.message}")
    return errors


def main() -> int:
    evidence = load_yaml("generic-evidence-manifest.yaml")
    freshness = load_yaml("generic-assurance-freshness.yaml")
    delta = load_yaml("generic-assurance-delta.yaml")
    errors: list[str] = []

    errors.extend(validate(evidence, "evidence-manifest.schema.json"))
    errors.extend(validate(freshness, "assurance-freshness.schema.json"))
    errors.extend(validate(delta, "assurance-delta.schema.json"))

    evidence_id = evidence.get("evidence_id")
    if evidence_id not in (freshness.get("evidence_ids") or []):
        errors.append("freshness record does not reference the generic evidence manifest")

    expected_status, expected_retest = freshness_from_basis(freshness.get("basis") or [])
    if freshness.get("status") != expected_status:
        errors.append(f"freshness status {freshness.get('status')} does not match basis-derived {expected_status}")
    if bool(freshness.get("retest_required")) != expected_retest:
        errors.append("freshness retest_required does not match basis-derived state")

    conclusion = delta.get("conclusion") or {}
    expected_transition = conclusion_transition(conclusion.get("previous"), conclusion.get("current"))
    if conclusion.get("transition") != expected_transition:
        errors.append(f"delta transition {conclusion.get('transition')} does not match derived {expected_transition}")

    changed = any(
        delta.get(section, {}).get(bucket)
        for section in ("findings", "controls", "evidence")
        for bucket in ("introduced", "resolved", "changed")
    ) or conclusion.get("previous") != conclusion.get("current")
    if bool(delta.get("material_change")) != bool(changed):
        errors.append("material_change must reflect substantive finding/control/evidence/conclusion change")

    if delta.get("freshness") == "current" and freshness.get("status") in {"stale", "retest-required", "indeterminate"}:
        # These fixtures describe consecutive lifecycle moments: freshness first flags the old run,
        # while the delta records the newly completed current run. Enforce that the run identities differ.
        if freshness.get("assessment_run_id") == delta.get("current_run_id"):
            errors.append("a run cannot be both current in delta and stale/retest-required in freshness")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Portable evidence/freshness/delta validation passed: provenance, conservative freshness and transition semantics satisfied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
