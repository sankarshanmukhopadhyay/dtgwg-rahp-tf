# RAHP documentation

RAHP has three primary paths:

## Understand

Start with [Concepts](concepts.md) and [How RAHP works](how-rahp-works.md) to understand people and power, risks and harms, controls and guardrails, and assurance evidence.

## Apply

Use [Pressure-testing a specification](pressure-testing-a-spec.md), then [Interpreting results](interpreting-results.md) and [Governance boundaries](governance-boundaries.md). Complete worked reviews are available under `examples/dtg-credential-spec/` and `examples/trust-tasks-spec/`. Together they demonstrate pressure testing of both a credential schema specification and a protocol/framework specification, including cross-layer finding disposition. In each example, `pressure-test.yaml` is canonical and the structured review section in `README.md` is generated with `tools/render_pressure_tests.py`. A reusable starter is available at `examples/pressure-test-template.yaml`.

## Explore the DTG instance

Canonical records live under `data/`. Generated risk, control, matrix, lifecycle, normative and governance views are built under `build/site/` with `python3 tools/build.py`.

The generated site is a drill-down evidence surface; the guided documentation is the entry point.
