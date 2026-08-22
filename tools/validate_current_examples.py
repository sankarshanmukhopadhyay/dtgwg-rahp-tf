#!/usr/bin/env python3
"""Validate that maintained canonical examples use the current RAHP release."""
from __future__ import annotations

import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "examples" / "current-baselines.yaml"
RESIDUAL_STATES = {
    "assured", "controlled", "finding", "assurance-gap",
    "review-required", "not-assessed", "not-applicable",
}


def main() -> int:
    errors: list[str] = []
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    current_version = (registry.get("current_rahp_release") or {}).get("version")
    if not current_version:
        errors.append("examples/current-baselines.yaml does not declare current_rahp_release.version")

    examples = registry.get("maintained_examples") or []
    for entry in examples:
        eid = entry.get("id") or "<unknown>"
        rel = entry.get("detailed_record")
        if not rel:
            errors.append(f"{eid}: missing detailed_record")
            continue
        path = ROOT / rel
        if not path.exists():
            errors.append(f"{eid}: canonical detailed record does not exist: {rel}")
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        review = doc.get("review") or {}
        reviewed_against = review.get("reviewed_against") or {}
        if reviewed_against.get("rahp_version") != current_version:
            errors.append(
                f"{eid}: canonical record uses {reviewed_against.get('rahp_version')!r}; "
                f"current release is {current_version!r}"
            )
        lineage = review.get("lineage") or {}
        prior = lineage.get("prior_record")
        if not lineage.get("prior_rahp_version") or not prior:
            errors.append(f"{eid}: canonical record must declare prior_rahp_version and prior_record")
        elif not (path.parent / prior).exists():
            errors.append(f"{eid}: historical provenance pointer does not exist: {path.parent / prior}")
        assurance = review.get("assurance") or {}
        state = assurance.get("residual_state")
        if state not in RESIDUAL_STATES:
            errors.append(f"{eid}: invalid or missing assurance.residual_state: {state!r}")
        delta = assurance.get("assurance_delta") or {}
        if not delta.get("disposition") or not isinstance(delta.get("finding_lineage"), dict):
            errors.append(f"{eid}: canonical record must carry assurance_delta disposition and finding_lineage")
        baseline = entry.get("current_baseline") or {}
        if baseline.get("rahp_version") != current_version:
            errors.append(f"{eid}: registry current_baseline does not match current release")
        if baseline.get("residual_state") != state:
            errors.append(
                f"{eid}: registry residual_state {baseline.get('residual_state')!r} "
                f"does not match canonical record {state!r}"
            )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS canonical examples: {len(examples)} maintained records use {current_version} with explicit lineage, history pointers and assurance posture.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
