#!/usr/bin/env python3
"""Publish RAHP change-monitor events as deduplicated GitHub issues."""
from __future__ import annotations
import argparse, json, os, urllib.error, urllib.parse, urllib.request
from pathlib import Path


def request(method: str, url: str, token: str, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "rahp-assessment-issue-publisher/0.6",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read().decode()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        raise RuntimeError(f"GitHub API {method} {url} failed: {e.code} {body}") from e


def ensure_label(repo: str, label: str, token: str):
    encoded = urllib.parse.quote(label, safe="")
    url = f"https://api.github.com/repos/{repo}/labels/{encoded}"
    try:
        request("GET", url, token)
        return
    except RuntimeError as exc:
        if " 404 " not in str(exc):
            raise
    palette = {"assessment-required": "d73a4a", "cawg-instance": "1d76db", "dtg-instance": "5319e7"}
    request("POST", f"https://api.github.com/repos/{repo}/labels", token,
            {"name": label, "color": palette.get(label, "6f42c1"), "description": "RAHP automated assessment workflow"})


def existing_titles(repo: str, token: str) -> set[str]:
    titles = set()
    page = 1
    while page <= 5:
        items = request("GET", f"https://api.github.com/repos/{repo}/issues?state=all&per_page=100&page={page}", token)
        if not items:
            break
        titles.update(i.get("title", "") for i in items if "pull_request" not in i)
        if len(items) < 100:
            break
        page += 1
    return titles


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--events", type=Path, required=True)
    ap.add_argument("--repository", required=True)
    args = ap.parse_args()
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN or GH_TOKEN is required")
    events = json.loads(args.events.read_text()) if args.events.exists() else []
    if not events:
        print("no assessment issues to publish")
        return 0
    known = existing_titles(args.repository, token)
    created = 0
    for event in events:
        title = event["title"]
        if title in known:
            print(f"[dedupe] {title}")
            continue
        labels = event.get("labels") or ["assessment-required"]
        for label in labels:
            ensure_label(args.repository, label, token)
        issue = request("POST", f"https://api.github.com/repos/{args.repository}/issues", token,
                        {"title": title, "body": event["body"], "labels": labels})
        print(f"[created] #{issue.get('number')} {title}")
        known.add(title); created += 1
    print(f"created {created} issue(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
