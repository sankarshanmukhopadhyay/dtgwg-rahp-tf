#!/usr/bin/env python3
"""Validate deployment-owned selected-issue watch registries."""
from __future__ import annotations

from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRIES = [
    ROOT / "instances/cawg/watch/issues.yaml",
    ROOT / "instances/dtg/watch/issues.yaml",
]

errors = []
total = 0

for path in REGISTRIES:
    data = yaml.safe_load(path.read_text())
    instance = data.get("instance")
    if data.get("version") != 1:
        errors.append(f"{path.relative_to(ROOT)}: version must be 1")
    if not instance:
        errors.append(f"{path.relative_to(ROOT)}: instance is required")
        continue
    labels = data.get("labels") or ["assessment-required", f"{instance}-instance"]
    if "assessment-required" not in labels or f"{instance}-instance" not in labels:
        errors.append(f"{path.relative_to(ROOT)}: labels must include assessment-required and {instance}-instance")
    default_repo = data.get("repository") or data.get("default_repository")
    seen = set()
    issues = data.get("issues") or []
    if not issues:
        errors.append(f"{path.relative_to(ROOT)}: at least one selected issue is required")
    for item in issues:
        total += 1
        repo = item.get("repository") or default_repo
        number = item.get("number")
        key = f"{repo}#{number}"
        if not repo:
            errors.append(f"{path.relative_to(ROOT)}: issue #{number} has no repository")
        if not isinstance(number, int) or number <= 0:
            errors.append(f"{path.relative_to(ROOT)}: invalid issue number {number!r}")
        if key in seen:
            errors.append(f"{path.relative_to(ROOT)}: duplicate selected issue {key}")
        seen.add(key)
        if not item.get("theme"):
            errors.append(f"{path.relative_to(ROOT)}: {key} has no theme")
        if not item.get("affected_reviews"):
            errors.append(f"{path.relative_to(ROOT)}: {key} has no affected_reviews mapping")

if errors:
    for error in errors:
        print("ERROR", error)
    print(f"Issue-watch registry validation failed: {len(errors)} error(s).")
    raise SystemExit(1)

print(f"Issue-watch registry validation clean: {len(REGISTRIES)} deployment registries, {total} selected issue(s).")
