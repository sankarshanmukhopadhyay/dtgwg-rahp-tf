#!/usr/bin/env python3
"""Validate the v0.5 configuration-driven portability contract."""
from __future__ import annotations
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG = ROOT / "tests" / "fixtures" / "portable-project" / "rahp.yaml"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(ROOT / "tools" / "rahp.py"), *args], cwd=ROOT, text=True, capture_output=True)


def main() -> int:
    checks = [
        ("configuration schema", run("config-validate", "--config", str(CONFIG))),
        ("target discovery", run("targets", "--config", str(CONFIG))),
        ("RAHP mode", run("review", "--config", str(CONFIG), "--target", "alpha-spec", "--mode", "rahp", "--offline", "--dry-run")),
        ("security mode", run("review", "--config", str(CONFIG), "--target", "alpha-spec", "--mode", "security", "--offline", "--dry-run")),
        ("combined mode", run("review", "--config", str(CONFIG), "--target", "alpha-spec", "--mode", "combined", "--offline", "--dry-run")),
    ]
    failed = False
    for label, result in checks:
        if result.returncode:
            failed = True
            print(f"[{label}] FAIL", file=sys.stderr)
            if result.stdout: print(result.stdout.strip(), file=sys.stderr)
            if result.stderr: print(result.stderr.strip(), file=sys.stderr)
        else:
            print(f"[{label}] PASS")
    required = [
        ROOT / "method" / "schema" / "rahp-config.schema.json",
        ROOT / "tools" / "rahp.py",
        ROOT / "profiles" / "dtg" / "rahp.yaml",
    ]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
    if missing:
        failed = True
        print("missing v0.5 assets: " + ", ".join(missing), file=sys.stderr)
    text = CONFIG.read_text(encoding="utf-8").lower()
    forbidden = ["trustoverip", "portfolio-monitor", "corpus-dtg", "rp-001", "dtgwg-"]
    leaked = [x for x in forbidden if x in text]
    if leaked:
        failed = True
        print("portable fixture contains deployment-specific coupling: " + ", ".join(leaked), file=sys.stderr)
    if failed:
        print("Portability validation: FAIL", file=sys.stderr)
        return 1
    print("Portability validation: PASS")
    print("  non-DTG YAML profile resolves targets and all three review modes")
    print("  no DTG corpus, portfolio registry, governance issue or DTG instance data is required")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
