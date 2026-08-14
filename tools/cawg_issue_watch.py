#!/usr/bin/env python3
"""Compatibility entry point for the CAWG issue watch.

The implementation is deployment-neutral in tools/issue_watch.py. New workflows
should call that tool directly with the CAWG registry/state paths.
"""
from issue_watch import main

if __name__ == "__main__":
    raise SystemExit(main([
        "--registry", "instances/cawg/watch/issues.yaml",
        "--state", "instances/cawg/state/issues.json",
        "--events", "instances/cawg/state/issue-events.json",
    ]))
