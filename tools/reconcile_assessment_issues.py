#!/usr/bin/env python3
"""Reconcile dispositioned RAHP assessment records with generated GitHub issues.

The command is conservative by design. It only treats an issue as closure-eligible when
*every* queue disposition that references that issue has a sidecar result marked
``status=dispositioned`` and explicitly lists the issue under
``closure.eligible_issues``. Default mode prints a machine-readable plan; ``--apply``
performs the GitHub close operation and posts an evidence-bearing comment.
"""
from __future__ import annotations

import argparse
import json
import os
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def result_path(review: str) -> Path:
    path = ROOT / review
    return path.with_suffix(".result.json")


def closure_candidates(queue: dict[str, Any]) -> list[dict[str, Any]]:
    by_issue: dict[int, list[dict[str, Any]]] = {}
    for disposition in queue.get("dispositions", []):
        for issue in disposition.get("rahp_issues", []):
            by_issue.setdefault(int(issue), []).append(disposition)

    candidates: list[dict[str, Any]] = []
    for issue, dispositions in sorted(by_issue.items()):
        evidence = []
        eligible = True
        for disposition in dispositions:
            rp = result_path(disposition["review"])
            if not rp.exists():
                eligible = False
                evidence.append({"assessment_id": disposition["assessment_id"], "error": "missing-result"})
                continue
            result = load_json(rp)
            closure = result.get("closure") or {}
            record = {
                "assessment_id": disposition["assessment_id"],
                "assessment_key": disposition["assessment_key"],
                "review": disposition["review"],
                "reviewed_revision": (result.get("target") or {}).get("reviewed_revision"),
                "status": result.get("status"),
                "explicitly_eligible": issue in closure.get("eligible_issues", []),
            }
            evidence.append(record)
            if result.get("status") != "dispositioned" or not record["explicitly_eligible"]:
                eligible = False
        if eligible and evidence:
            candidates.append({"issue": issue, "evidence": evidence})
    return candidates


def gh_request(method: str, url: str, token: str, payload: dict[str, Any]) -> None:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        method=method,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "rahp-assessment-reconciler/1.0",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(req, timeout=30):
        pass


def closure_comment(candidate: dict[str, Any]) -> str:
    lines = [
        "RAHP assessment reconciliation confirms that every durable assessment record associated with this generated work item is dispositioned.",
        "",
        "Evidence:",
    ]
    for item in candidate["evidence"]:
        lines.append(
            f"- `{item['assessment_id']}` — `{item['reviewed_revision']}` — `{item['review']}`"
        )
    lines += [
        "",
        "Closing this queue issue means the named revision(s) were reviewed and dispositioned. It does not assert that every upstream design dependency or residual finding is resolved.",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--queue", type=Path, required=True)
    ap.add_argument("--repository", help="GitHub repository in owner/name form")
    ap.add_argument("--apply", action="store_true", help="close eligible issues on GitHub")
    args = ap.parse_args()
    queue = load_json(args.queue)
    candidates = closure_candidates(queue)
    print(json.dumps({"closure_candidates": candidates}, indent=2))
    if not args.apply:
        return 0
    if not args.repository:
        raise SystemExit("--repository is required with --apply")
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN or GH_TOKEN is required with --apply")
    for candidate in candidates:
        number = candidate["issue"]
        base = f"https://api.github.com/repos/{args.repository}/issues/{number}"
        gh_request("POST", base + "/comments", token, {"body": closure_comment(candidate)})
        gh_request("PATCH", base, token, {"state": "closed", "state_reason": "completed"})
        print(f"closed #{number}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
