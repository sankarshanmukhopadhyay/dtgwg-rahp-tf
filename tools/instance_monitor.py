#!/usr/bin/env python3
"""Portable repository-change monitor for a RAHP deployment instance.

Unlike the DTG portfolio adapter, this tool does not discover repositories from a
DTG registry. It reads a normal RAHP profile, tracks repository@branch heads, and
emits assessment-required events when material paths change. This makes change
tracking reusable by external deployments such as CAWG/C2PA.
"""
from __future__ import annotations
import argparse, fnmatch, json, os, pathlib, urllib.request
from datetime import datetime, timezone
from typing import Any
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent


def load_yaml(path: pathlib.Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def api_json(url: str) -> Any:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "rahp-instance-monitor/0.6"}
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def head_sha(repo: str, branch: str) -> str:
    return api_json(f"https://api.github.com/repos/{repo}/commits/{branch}")["sha"]


def compare(repo: str, base: str, head: str) -> dict[str, Any]:
    return api_json(f"https://api.github.com/repos/{repo}/compare/{base}...{head}")


def material_paths(target: dict[str, Any], cfg: dict[str, Any]) -> list[str]:
    scoped = (target.get("scope") or {}).get("include") or []
    default = ((cfg.get("assessment") or {}).get("materiality") or {}).get("always_material_paths") or []
    return list(dict.fromkeys([*scoped, *default]))


def classify(target: dict[str, Any], files: list[dict[str, Any]], cfg: dict[str, Any]) -> tuple[bool, list[str]]:
    patterns = material_paths(target, cfg)
    matched = []
    for f in files:
        name = f.get("filename", "")
        if any(fnmatch.fnmatch(name, pat) for pat in patterns):
            matched.append(name)
    return bool(matched), sorted(set(matched))


def state_key(target: dict[str, Any]) -> str:
    return f"{target['repository']}@{target.get('branch', 'main')}"


def event_body(instance: dict[str, Any], target: dict[str, Any], old: str, new: str,
               comparison: dict[str, Any], matched: list[str]) -> str:
    repo = target["repository"]
    branch = target.get("branch", "main")
    commits = comparison.get("commits") or []
    lines = [
        "## RAHP assessment trigger", "",
        f"The **{instance.get('title', instance.get('id', 'RAHP'))}** change monitor detected a material change requiring review.", "",
        "| Field | Value |", "|---|---|",
        f"| Target | `{target.get('id')}` |",
        f"| Repository | `{repo}` |",
        f"| Branch | `{branch}` |",
        f"| Previous observed revision | `{old}` |",
        f"| Current observed revision | `{new}` |",
        f"| Commit count in comparison | {len(commits)} |", "",
        "### Material files changed", "",
    ]
    lines += [f"- `{p}`" for p in matched] or ["- Comparison could not identify a configured material path; conservative review requested."]
    lines += ["", "### Review action", "",
              "1. Inspect the upstream diff and determine whether semantics, assurance assumptions, security properties, governance dependencies, or interoperability behaviour changed.",
              "2. Re-run the target RAHP/security/combined review as appropriate.",
              "3. Update the relevant assessment artefact and close this issue only when the new revision has been dispositioned.",
              "", "### Governance boundary", "",
              "This issue records work for this RAHP deployment. It does **not** imply that RAHP owns, governs, or can change the upstream specification. Proposed remediation must be routed to the appropriate upstream specification, companion specification, governance body, implementation guidance, runtime control, or operational policy.", ""]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", choices=["sync", "check"])
    ap.add_argument("--config", type=pathlib.Path, required=True, help="instance configuration YAML")
    ap.add_argument("--initialize", action="store_true", help="record current heads without emitting review events")
    args = ap.parse_args()

    cfg = load_yaml(args.config)
    instance = cfg.get("instance") or {}
    profile_path = ROOT / instance["profile"]
    profile = load_yaml(profile_path)
    targets = profile.get("repositories") or []

    generated = ROOT / cfg["generated"]["manifest"]
    generated.parent.mkdir(parents=True, exist_ok=True)
    generated.write_text(yaml.safe_dump(profile, sort_keys=False), encoding="utf-8")
    print(f"loaded {len(targets)} target(s) for {instance.get('id')}")
    if args.command == "sync":
        return 0

    state_path = ROOT / cfg["state"]["file"]
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state = json.loads(state_path.read_text()) if state_path.exists() else {"version": 1, "targets": {}}
    state.setdefault("targets", {})
    events: list[dict[str, Any]] = []

    for target in targets:
        repo = target["repository"]
        branch = target.get("branch", "main")
        key = state_key(target)
        new = head_sha(repo, branch)
        old = (state["targets"].get(key) or {}).get("sha")
        if not old or args.initialize:
            state["targets"][key] = {"sha": new, "observed_at": datetime.now(timezone.utc).isoformat()}
            continue
        if old == new:
            continue
        try:
            comp = compare(repo, old, new)
            material, matched = classify(target, comp.get("files") or [], cfg)
        except Exception as exc:
            material, matched = True, []
            comp = {"commits": []}
            print(f"warning: comparison failed for {key}: {exc}")
        if material:
            events.append({
                "instance": instance.get("id"),
                "target_id": target.get("id"),
                "repository": repo,
                "branch": branch,
                "old": old,
                "new": new,
                "title": f"[RAHP review required] {target.get('id')}: {old[:7]} → {new[:7]}",
                "body": event_body(instance, target, old, new, comp, matched),
                "labels": ((cfg.get("assessment") or {}).get("issue") or {}).get("labels") or ["assessment-required"],
            })
        state["targets"][key] = {"sha": new, "observed_at": datetime.now(timezone.utc).isoformat()}

    state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    events_path = ROOT / cfg["generated"]["events"]
    events_path.parent.mkdir(parents=True, exist_ok=True)
    events_path.write_text(json.dumps(events, indent=2) + "\n", encoding="utf-8")
    print(f"material review event(s): {len(events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
