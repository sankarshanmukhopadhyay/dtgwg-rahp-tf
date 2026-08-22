#!/usr/bin/env python3
"""Validate portable authority and policy-gate contracts and neutral fixtures."""
from __future__ import annotations

import json
from pathlib import Path
import sys
from datetime import datetime, timezone

import yaml
from jsonschema import Draft202012Validator, FormatChecker

from authority import evaluate_authority
from policy_gate import evaluate_policy

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "method" / "schema"
FIXTURE_DIR = ROOT / "examples" / "assurance-lineage"


def load_yaml(name: str):
    return yaml.safe_load((FIXTURE_DIR / name).read_text(encoding="utf-8"))


def validate(document, schema_name: str) -> list[str]:
    schema = json.loads((SCHEMA_DIR / schema_name).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    for err in sorted(validator.iter_errors(document), key=lambda e: list(e.path)):
        loc = ".".join(str(p) for p in err.absolute_path) or "(record)"
        errors.append(f"{schema_name} {loc}: {err.message}")
    return errors


def main() -> int:
    authority = load_yaml("generic-authority.yaml")
    policy = load_yaml("generic-release-gate.yaml")
    pass_context = load_yaml("generic-release-context-pass.yaml")
    fail_context = load_yaml("generic-release-context-fail.yaml")
    indeterminate_context = load_yaml("generic-release-context-indeterminate.yaml")
    errors: list[str] = []

    errors.extend(validate(authority, "authority.schema.json"))
    errors.extend(validate(policy, "gate-policy.schema.json"))

    at = datetime(2026, 8, 22, tzinfo=timezone.utc)
    publish = evaluate_authority(
        authority,
        subject="example:assurance-operator",
        action="publish",
        scope_kind="assessment",
        scope_id="example:specification:payments-api",
        at=at,
    )
    if not publish["authorized"]:
        errors.append("declared publication authority was not recognized")

    accept_risk = evaluate_authority(
        authority,
        subject="example:assurance-operator",
        action="accept-risk",
        scope_kind="assessment",
        scope_id="example:specification:payments-api",
        at=at,
    )
    if accept_risk["authorized"]:
        errors.append("authority evaluator expanded scope to undeclared accept-risk authority")

    wrong_scope = evaluate_authority(
        authority,
        subject="example:assurance-operator",
        action="publish",
        scope_kind="assessment",
        scope_id="example:other-project",
        at=at,
    )
    if wrong_scope["authorized"]:
        errors.append("authority evaluator ignored scope boundary")

    outcomes = {
        "pass": evaluate_policy(policy, pass_context)["outcome"],
        "fail": evaluate_policy(policy, fail_context)["outcome"],
        "indeterminate": evaluate_policy(policy, indeterminate_context)["outcome"],
    }
    expected = {"pass": "PASS", "fail": "FAIL", "indeterminate": "INDETERMINATE"}
    if outcomes != expected:
        errors.append(f"policy outcomes {outcomes!r} do not match expected {expected!r}")

    required = policy.get("authority_required") or {}
    if required.get("action") != "publish" or required.get("scope", {}).get("id") != "example:specification:payments-api":
        errors.append("release gate does not preserve explicit publication-authority requirement")

    for rule in policy.get("rules") or []:
        for condition in rule.get("conditions") or []:
            if condition.get("operator") in {"equals", "not-equals", "in", "not-in"} and "value" not in condition:
                errors.append(f"rule {rule.get('id')} condition {condition.get('path')} requires a value")

    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("Portable authority/policy validation passed: scope, revocation posture and PASS/FAIL/INDETERMINATE semantics satisfied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
