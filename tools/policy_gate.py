#!/usr/bin/env python3
"""Portable RAHP policy gate evaluation with PASS/FAIL/INDETERMINATE semantics."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

MISSING = object()


def load_document(path: str) -> dict[str, Any]:
    value = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected object: {path}")
    return value


def get_path(document: dict[str, Any], path: str):
    value: Any = document
    for part in path.split("."):
        if not isinstance(value, dict) or part not in value:
            return MISSING
        value = value[part]
    return value


def evaluate_condition(document: dict[str, Any], condition: dict[str, Any]) -> tuple[bool | None, str]:
    value = get_path(document, condition["path"])
    operator = condition["operator"]
    expected = condition.get("value", MISSING)

    if operator == "exists":
        return value is not MISSING, "evaluated"
    if operator == "not-exists":
        return value is MISSING, "evaluated"
    if value is MISSING:
        return None, "missing-input"
    if expected is MISSING:
        return None, "missing-policy-value"
    if operator == "equals":
        return value == expected, "evaluated"
    if operator == "not-equals":
        return value != expected, "evaluated"
    if operator == "in":
        if not isinstance(expected, list):
            return None, "invalid-policy-value"
        return value in expected, "evaluated"
    if operator == "not-in":
        if not isinstance(expected, list):
            return None, "invalid-policy-value"
        return value not in expected, "evaluated"
    return None, "unsupported-operator"


def evaluate_policy(policy: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
    rule_results = []
    indeterminate = False
    failed = False

    for rule in policy.get("rules") or []:
        condition_results = []
        unknown = False
        for condition in rule.get("conditions") or []:
            result, reason = evaluate_condition(context, condition)
            condition_results.append({"condition": condition, "result": result, "reason": reason})
            if result is None:
                unknown = True

        bools = [item["result"] for item in condition_results if item["result"] is not None]
        all_true = bool(condition_results) and not unknown and all(bools)
        any_false = any(item["result"] is False for item in condition_results)

        if rule.get("effect") == "deny":
            triggered = all_true
            rule_indeterminate = unknown and not any_false
            if triggered:
                failed = True
        else:  # require
            triggered = all_true
            rule_indeterminate = unknown and not any_false
            if not triggered and not rule_indeterminate:
                failed = True

        if rule_indeterminate:
            indeterminate = True

        rule_results.append({
            "id": rule.get("id"),
            "effect": rule.get("effect"),
            "satisfied": triggered if rule.get("effect") == "require" else not triggered,
            "triggered": triggered,
            "indeterminate": rule_indeterminate,
            "message": rule.get("message"),
            "conditions": condition_results,
        })

    if failed:
        outcome = "FAIL"
    elif indeterminate:
        outcome = "INDETERMINATE"
    else:
        outcome = "PASS"

    return {
        "policy_id": policy.get("policy_id"),
        "outcome": outcome,
        "rules": rule_results,
        "authority_required": policy.get("authority_required"),
        "notes": [
            "Gate outcome is policy evaluation evidence; it does not create governance authority.",
            "INDETERMINATE preserves missing or non-evaluable inputs rather than converting uncertainty into PASS.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate a portable RAHP policy gate")
    parser.add_argument("--policy", required=True)
    parser.add_argument("--context", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = evaluate_policy(load_document(args.policy), load_document(args.context))
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(result["outcome"])
    return {"PASS": 0, "FAIL": 1, "INDETERMINATE": 2}[result["outcome"]]


if __name__ == "__main__":
    raise SystemExit(main())
