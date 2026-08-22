#!/usr/bin/env python3
"""Validate portable RAHP assessment and finding lineage fixtures.

This validator intentionally targets deployment-neutral fixtures. Portfolio-specific
examples may adopt the same contracts, but they are not required for core validity.
"""
from __future__ import annotations

import json
import pathlib
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "method" / "schema"
FIXTURE_DIR = ROOT / "examples" / "assurance-lineage"


def load_json(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: pathlib.Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate(schema_name: str, fixture_name: str) -> list[str]:
    schema = load_json(SCHEMA_DIR / schema_name)
    instance = load_yaml(FIXTURE_DIR / fixture_name)
    validator = Draft202012Validator(schema)
    errors = []
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.absolute_path) or "(root)"
        errors.append(f"{fixture_name}: {location}: {error.message}")
    return errors


def check_cross_fixture_invariants() -> list[str]:
    assessment = load_yaml(FIXTURE_DIR / "generic-specification.yaml")
    finding = load_yaml(FIXTURE_DIR / "generic-finding-lineage.yaml")
    errors = []

    run_ids = [run["run_id"] for run in assessment["runs"]]
    if len(run_ids) != len(set(run_ids)):
        errors.append("assessment run_id values must be unique")
    if assessment.get("current_run_id") not in set(run_ids):
        errors.append("current_run_id must reference a declared run")

    for run in assessment["runs"]:
        predecessor = run.get("predecessor_run_id")
        if predecessor and predecessor not in set(run_ids):
            errors.append(f"run {run['run_id']} references unknown predecessor {predecessor}")

    if finding["assessment_id"] != assessment["assessment_id"]:
        errors.append("finding lineage must reference the fixture assessment_id")

    for revision in finding["history"]:
        if revision["run_id"] not in set(run_ids):
            errors.append(
                f"finding revision references unknown assessment run {revision['run_id']}"
            )
        for relation in ("predecessors", "successors"):
            for ref in revision.get(relation, []):
                if ref["assessment_id"] == assessment["assessment_id"] and ref["run_id"] not in set(run_ids):
                    errors.append(
                        f"{relation} reference uses unknown local run {ref['run_id']}"
                    )

    return errors


def main() -> int:
    errors = []
    errors.extend(validate("assessment-lineage.schema.json", "generic-specification.yaml"))
    errors.extend(validate("finding-lineage.schema.json", "generic-finding-lineage.yaml"))
    errors.extend(check_cross_fixture_invariants())

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Portable assurance lineage validation passed: 2 schemas, 2 generic fixtures.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
