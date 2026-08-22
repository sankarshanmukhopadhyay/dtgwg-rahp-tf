#!/usr/bin/env python3
"""Build actionable RAHP assurance posture without synthetic assurance scores."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from datetime import datetime, timezone
import yaml

ACTION_CONCLUSIONS = {"finding", "assurance-gap", "review-required", "not-assessed"}
STALE = {"potentially-stale", "stale", "retest-required", "indeterminate"}


def load(path: str):
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    return json.loads(text) if p.suffix.lower() == ".json" else yaml.safe_load(text)


def build_posture(source: dict, generated_at: str | None = None) -> dict:
    records = source.get("records") or []
    summary = {
        "total": len(records),
        "action_required": sum(1 for r in records if r.get("conclusion") in ACTION_CONCLUSIONS or r.get("remediation") in {"open", "in-progress", "retest-pending", "indeterminate"}),
        "stale_or_retest": sum(1 for r in records if r.get("freshness") in STALE),
        "evidence_gaps": sum(int(r.get("evidence_gaps", 0)) for r in records),
        "gate_blocked": sum(1 for r in records if r.get("gate") in {"FAIL", "INDETERMINATE"}),
        "authority_blocked": sum(1 for r in records if r.get("authority") in {"denied", "indeterminate"}),
        "changed": sum(1 for r in records if r.get("changed_since_baseline") is True),
    }
    return {
        "version": 1,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "scope": source["scope"],
        "records": records,
        "summary": summary,
        "notes": [
            "Counts are operational views over portable assurance records, not an assurance score.",
            "Gate and authority posture remain distinct: PASS does not confer authority."
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--generated-at")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    result = build_posture(load(args.input), args.generated_at)
    print(json.dumps(result, indent=2) if args.json else yaml.safe_dump(result, sort_keys=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
