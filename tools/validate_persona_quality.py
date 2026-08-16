#!/usr/bin/env python3
"""Validate persona analytical richness independently of base schema validity."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parent.parent


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def validate(root: Path) -> list[str]:
    config = load_yaml(root / "method" / "persona-quality.yaml")
    personas = load_yaml(root / "data" / "personas.yaml").get("records", [])
    errors: list[str] = []

    for persona in personas:
        ptype = persona.get("type")
        profile = (config.get("profiles") or {}).get(ptype)
        if not profile:
            continue
        pid = persona.get("id", "<missing-id>")
        for field in profile.get("required_fields", []):
            value = persona.get(field)
            if value is None or value == [] or value == {} or value == "":
                errors.append(f"{pid}: required richness field '{field}' is empty or missing")
        for field, minimum in (profile.get("minimum_items") or {}).items():
            value = persona.get(field)
            count = len(value) if isinstance(value, list) else 0
            if count < int(minimum):
                errors.append(f"{pid}: '{field}' has {count} item(s); minimum is {minimum}")
        context = persona.get("context") or {}
        for key in profile.get("context_required_keys", []):
            if not isinstance(context, dict) or not str(context.get(key, "")).strip():
                errors.append(f"{pid}: context.{key} is required by persona quality profile")
        phases = persona.get("lifecycle_phases") or []
        prohibited = set(profile.get("prohibited_lifecycle_only_values", []))
        if len(phases) == 1 and phases[0] in prohibited:
            errors.append(f"{pid}: lifecycle cannot be represented only as '{phases[0]}'")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"ERROR persona-quality: {error}")
        print(f"FAIL persona-quality: {len(errors)} error(s)")
        return 1
    print("PASS persona-quality: all configured persona richness profiles satisfied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
