#!/usr/bin/env python3
"""Validate the v0.5 portability contract against a non-DTG instance fixture."""
from __future__ import annotations
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FIXTURE = ROOT / "examples" / "portable-instance" / "data"


def main():
    cmd = [
        sys.executable,
        str(ROOT / "tools" / "validate.py"),
        "--data", str(FIXTURE),
        "--readme", str(FIXTURE.parent / "README.md"),
        "--strict",
        "--summary",
    ]
    run = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if run.stdout:
        print(run.stdout.strip())
    if run.returncode:
        if run.stderr:
            print(run.stderr.strip(), file=sys.stderr)
        print("Portability validation: FAIL", file=sys.stderr)
        return run.returncode

    required = [
        ROOT / "method" / "lifecycle.yaml",
        ROOT / "method" / "vocabularies.yaml",
        ROOT / "method" / "schema" / "rahp.schema.json",
        ROOT / "tools" / "validate.py",
    ]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
    if missing:
        print("Portability validation: FAIL — missing portable method assets: " + ", ".join(missing), file=sys.stderr)
        return 1

    print("Portability validation: PASS")
    print("  synthetic external instance validates without DTG data or root README coupling")
    print("  note: this proves mechanical portability, not independent Working Group adoption")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
