#!/usr/bin/env python3
"""Validate a remediation/retest pair and emit a machine-readable closure judgment."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import yaml

from validate_remediation_retest_lineage import schema_errors, semantic_errors


def load_document(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    value = json.loads(text) if path.suffix.lower() == ".json" else yaml.safe_load(text)
    if not isinstance(value, dict):
        raise ValueError(f"expected object: {path}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate portable RAHP remediation/retest lineage")
    parser.add_argument("--remediation", required=True, type=Path)
    parser.add_argument("--retest", required=True, type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    remediation = load_document(args.remediation)
    retest = load_document(args.retest)
    errors = [f"remediation schema {e}" for e in schema_errors(remediation, "remediation-manifest.schema.json")]
    errors += [f"retest schema {e}" for e in schema_errors(retest, "retest.schema.json")]
    errors += semantic_errors(remediation, retest)

    disposition = retest.get("disposition") or {}
    result = {
        "assessment_id": retest.get("assessment_id"),
        "remediation_id": retest.get("remediation_id"),
        "retest_id": retest.get("retest_id"),
        "outcome": retest.get("outcome"),
        "disposition_status": disposition.get("status"),
        "authority_basis": disposition.get("authority_basis"),
        "valid": not errors,
        "errors": errors,
    }

    if args.as_json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"retest {result['retest_id'] or '<unidentified>'}: {'VALID' if result['valid'] else 'INVALID'}")
        print(f"outcome={result['outcome']} disposition={result['disposition_status']}")
        for error in errors:
            print(f"ERROR: {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
