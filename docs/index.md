# RAHP documentation

RAHP has three primary paths:

## Understand

Start with [Concepts](concepts.md) and [How RAHP works](how-rahp-works.md) to understand people and power, risks and harms, controls and guardrails, and assurance evidence.

## Apply

Use [Pressure-testing a specification](pressure-testing-a-spec.md), then [Interpreting results](interpreting-results.md) and [Governance boundaries](governance-boundaries.md). A complete worked review is available under `examples/dtg-credential-spec/`, with a reusable starter at `examples/pressure-test-template.yaml`.

## Explore the DTG instance

Canonical records live under `data/`. Generated risk, control, matrix, lifecycle, normative and governance views are built under `build/site/` with `python3 tools/build.py`.

The generated site is a drill-down evidence surface; the guided documentation is the entry point.
