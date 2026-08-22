#!/usr/bin/env python3
"""Portable RAHP authority evaluation.

The evaluator determines whether a declared authority grant covers an action and
scope. It does not create authority, mutate governance state, or infer mandate
from repository permissions.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any

import yaml


def load_document(path: str) -> dict[str, Any]:
    value = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected object: {path}")
    return value


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def scope_matches(grant_scope: dict[str, Any], requested_scope: dict[str, str]) -> bool:
    if grant_scope.get("kind") == "global":
        return True
    return (
        grant_scope.get("kind") == requested_scope.get("kind")
        and grant_scope.get("id") == requested_scope.get("id")
    )


def evaluate_authority(
    grant: dict[str, Any],
    *,
    subject: str,
    action: str,
    scope_kind: str,
    scope_id: str,
    at: datetime | None = None,
) -> dict[str, Any]:
    at = at or datetime.now(timezone.utc)
    reasons: list[str] = []

    if grant.get("subject") != subject:
        reasons.append("subject-mismatch")
    if grant.get("status") != "active":
        reasons.append(f"authority-{grant.get('status', 'unknown')}")

    valid_from = parse_time(grant.get("valid_from"))
    valid_until = parse_time(grant.get("valid_until"))
    if valid_from and at < valid_from:
        reasons.append("not-yet-valid")
    if valid_until and at > valid_until:
        reasons.append("expired-by-time")

    requested_scope = {"kind": scope_kind, "id": scope_id}
    matching_grants = [
        item for item in (grant.get("grants") or [])
        if item.get("action") == action and scope_matches(item.get("scope") or {}, requested_scope)
    ]
    if not matching_grants:
        reasons.append("no-matching-grant")

    authorized = not reasons
    return {
        "authority_id": grant.get("authority_id"),
        "subject": subject,
        "action": action,
        "scope": requested_scope,
        "authorized": authorized,
        "decision": "AUTHORIZED" if authorized else "DENIED",
        "reasons": reasons,
        "matched_grants": matching_grants if authorized else [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate a portable RAHP authority grant")
    parser.add_argument("--authority", required=True)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--action", required=True)
    parser.add_argument("--scope-kind", required=True)
    parser.add_argument("--scope-id", required=True)
    parser.add_argument("--at")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = evaluate_authority(
        load_document(args.authority),
        subject=args.subject,
        action=args.action,
        scope_kind=args.scope_kind,
        scope_id=args.scope_id,
        at=parse_time(args.at) if args.at else None,
    )
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(result["decision"])
        if result["reasons"]:
            print("Reasons: " + ", ".join(result["reasons"]))
    return 0 if result["authorized"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
