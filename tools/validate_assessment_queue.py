#!/usr/bin/env python3
"""Validate deployment-owned durable assessment queue/disposition state."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text())
    if data.get("version") != 1:
        errors.append(f"{path}: unsupported version {data.get('version')!r}")
    seen_ids: set[str] = set()
    seen_keys: set[str] = set()
    issue_entries: dict[int, list[dict]] = {}
    for entry in data.get("dispositions") or []:
        aid = entry.get("assessment_id")
        key = entry.get("assessment_key")
        review = entry.get("review")
        rev = entry.get("reviewed_revision")
        disposition = entry.get("disposition")
        if not aid or aid in seen_ids:
            errors.append(f"{path}: missing or duplicate assessment_id {aid!r}")
        else:
            seen_ids.add(aid)
        if not key or key in seen_keys:
            errors.append(f"{path}: missing or duplicate assessment_key {key!r}")
        else:
            seen_keys.add(key)
        if disposition not in {"no-material-assurance-impact", "findings-raised", "remediation-requested", "risk-accepted", "superseded"}:
            errors.append(f"{path}: {aid}: unsupported disposition {disposition!r}")
        if not rev or len(rev) < 7:
            errors.append(f"{path}: {aid}: reviewed_revision missing or too short")
        if not review:
            errors.append(f"{path}: {aid}: review path missing")
        else:
            review_path = ROOT / review
            if not review_path.exists():
                errors.append(f"{path}: {aid}: review does not exist: {review}")
            else:
                text = review_path.read_text()
                for expected in (aid, key, rev, disposition):
                    if expected not in text:
                        errors.append(f"{path}: {aid}: review does not contain {expected!r}")
        for number in entry.get("rahp_issues") or []:
            if not isinstance(number, int) or number <= 0:
                errors.append(f"{path}: {aid}: invalid RAHP issue number {number!r}")
            issue_entries.setdefault(number, []).append(entry)
    for number, entries in sorted(issue_entries.items()):
        if len(entries) <= 1:
            continue
        if not all(bool(entry.get("legacy_coalesced_issue")) for entry in entries):
            keys = ", ".join(str(entry.get("assessment_key")) for entry in entries)
            errors.append(
                f"{path}: RAHP issue #{number} is dispositioned by multiple assessments "
                f"without legacy_coalesced_issue=true on every entry: {keys}"
            )

    for entry in data.get("open_generated_assessments") or []:
        if not isinstance(entry, dict) or not entry.get("assessment_key"):
            errors.append(f"{path}: open_generated_assessments entries require assessment_key")
    return errors


def main() -> int:
    paths = sorted((ROOT / "instances").glob("*/state/assessment-queue.json"))
    if not paths:
        print("Assessment-queue validation clean: no deployment queue state present.")
        return 0
    errors: list[str] = []
    for path in paths:
        errors.extend(validate(path))
    if errors:
        print("Assessment-queue validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"Assessment-queue validation clean: {len(paths)} deployment queue state file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
