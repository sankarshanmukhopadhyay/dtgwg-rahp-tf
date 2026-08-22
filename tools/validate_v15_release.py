#!/usr/bin/env python3
"""Validate the RAHP v1.5 release-candidate qualification contract."""
from __future__ import annotations
import json, sys
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from assurance_posture import build_posture

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "method" / "v1.5-release-qualification.yaml"


def main() -> int:
    q = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    status = yaml.safe_load((ROOT / "PROJECT-STATUS.yaml").read_text(encoding="utf-8"))
    registry = yaml.safe_load((ROOT / "method" / "capability-documentation.yaml").read_text(encoding="utf-8"))
    errors: list[str] = []

    if status.get("development_target") != "1.5.0":
        errors.append("PROJECT-STATUS development_target must remain 1.5.0")
    if status.get("qualification_status") not in {"candidate", "cut-ready"}:
        errors.append("PROJECT-STATUS qualification_status must be candidate or cut-ready")
    if status.get("stable_release") != "1.2.0" or status.get("release_status") != "unreleased":
        errors.append("qualification PR must not mark v1.5.0 released before the release-cut commit")

    compat = status.get("compatibility") or {}
    for key, expected in (q.get("stable_compatibility") or {}).items():
        if compat.get(key) != expected:
            errors.append(f"stable compatibility mismatch for {key}: {compat.get(key)!r} != {expected!r}")

    registered = {c.get("id") for c in registry.get("capabilities", [])}
    for cap in q.get("required_capabilities", []):
        if cap not in registered:
            errors.append(f"required capability not registered/documented: {cap}")

    for label, rel in (q.get("required_evidence") or {}).items():
        if not (ROOT / rel).exists():
            errors.append(f"required evidence missing ({label}): {rel}")
    release_prep = ROOT / "docs" / "releases" / "v1.5.0-preparation.md"
    if not release_prep.exists():
        errors.append("synchronized v1.5.0 release-preparation content is missing")

    forbidden = [x.lower() for x in q.get("forbidden_core_dependencies", [])]
    for rel in q.get("portable_paths", []):
        path = ROOT / rel
        if not path.exists():
            errors.append(f"portable contract missing: {rel}")
            continue
        text = path.read_text(encoding="utf-8").lower()
        for token in forbidden:
            if token in text:
                errors.append(f"portable contract {rel} contains deployment-specific dependency token {token!r}")

    demonstrations = q.get("demonstrations") or []
    kinds = [d.get("kind") for d in demonstrations]
    if kinds.count("deployment-neutral") < 1:
        errors.append("qualification requires at least one deployment-neutral demonstration")
    if kinds.count("project-specific") < 2:
        errors.append("qualification requires at least two independent project-specific demonstrations")
    demo_ids = [d.get("id") for d in demonstrations]
    if len(demo_ids) != len(set(demo_ids)):
        errors.append("demonstration IDs must be unique")
    for demo in demonstrations:
        if not str(demo.get("command", "")).startswith("python3 "):
            errors.append(f"demonstration {demo.get('id')} lacks an executable validation command")

    source = yaml.safe_load((ROOT / "examples" / "assurance-lineage" / "generic-posture-input.yaml").read_text(encoding="utf-8"))
    expected = json.loads((ROOT / "examples" / "assurance-lineage" / "generic-posture-result.json").read_text(encoding="utf-8"))
    actual = build_posture(source, expected["generated_at"])
    if actual != expected:
        errors.append("generic assurance posture output differs from committed conformance evidence")
    schema = json.loads((ROOT / "method" / "schema" / "assurance-posture.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for err in validator.iter_errors(actual):
        loc = ".".join(str(x) for x in err.absolute_path) or "(record)"
        errors.append(f"assurance posture schema {loc}: {err.message}")
    if "score" in actual.get("summary", {}):
        errors.append("portable posture must not expose a synthetic assurance score")

    naming = status.get("release_naming", {})
    if naming.get("selection") != "random-at-release-time":
        errors.append("West Bengal butterfly naming must remain random-at-release-time")
    if (q.get("release_cut") or {}).get("butterfly_name_selection") != "random-at-release-time":
        errors.append("release qualification manifest must defer butterfly selection until release time")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS v1.5 qualification: capability completeness, compatibility, portability, demonstrations, posture evidence, documentation and release-cut policy satisfied.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
