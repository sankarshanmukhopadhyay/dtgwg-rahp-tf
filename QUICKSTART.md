---
layout: default
title: "Quick start"
nav_order: 21
has_toc: true
---
# RAHP Quickstart

Use this path when you want useful output before learning every artefact type.

1. **Choose a target.** Record the specification/system, version or commit, and review scope.
2. **Choose 3–6 personas.** Start with who has decision power, who bears harm, and edge cases.
3. **Reuse existing risks.** Search `data/risks.yaml` before inventing new hypotheses.
4. **Pressure-test 5–15 hypotheses.** Ask what fails, who is harmed, what harmful inference remains possible, and what can remain technically valid while governance-invalid.
5. **Map controls only where needed.** Use guardrails for hard stops and assurance tests for evidence.
6. **Route each finding.** Decide the correct control plane using `docs/governance-boundaries.md`.
7. **Publish recommendations.** Make each action traceable to evidence and status.
8. **Render, validate and repeat.** Treat `pressure-test.yaml` as canonical, render its Markdown view into the sibling README, and use the generated Reference catalogue so every RAHP citation resolves to its definition and context. Re-run the review when the target specification changes.

```bash
pip install -r requirements.txt
python3 tools/validate.py
python3 tools/render_pressure_tests.py
python3 tools/validate_pressure_tests.py
python3 tools/build.py
python3 tools/validate_reference_links.py
```

For the complete process, see [ADOPTION.md](ADOPTION.md) and [docs/pressure-testing-a-spec.md](docs/pressure-testing-a-spec.md).


Worked pressure tests: [`examples/dtg-credential-spec/`](examples/dtg-credential-spec/README.md) and [`examples/trust-tasks-spec/`](examples/trust-tasks-spec/README.md).


## Using an AI agent

An AI coding or repository agent can perform the repeatable mechanics above, select relevant scenario corpora, draft evidence-backed candidate findings, render the outputs, and run the validators. Keep final scoring, risk acceptance, assurance claims, and governance dispositions under accountable human review. See [Use an AI agent to run a pressure test](docs/using-an-ai-agent.md) for the prompt contract and end-to-end workflow.


## Security-hardening reviews

The coordinated Trust Tasks / DTG Credentials adversarial reviews are under [`examples/security-hardening/`](examples/security-hardening/README.md). Canonical findings are YAML; rendered reports are generated and checked:

```bash
python3 tools/render_security_reviews.py
python3 tools/validate_security_reviews.py
```

## Unified review modes

The toolkit now exposes one review entry point:

```bash
python3 tools/review.py --help
```

A reviewer can scaffold and run a **RAHP pressure test**, a **security-hardening review**, or a **combined review** that preserves both analytical lenses and generates a cross-lens synthesis. See [`docs/review-modes.md`](docs/review-modes.md).

`tools/review.py` is an orchestration tool, not a static vulnerability scanner: the findings must be produced from examination of the target specification or document, while the repository tooling handles canonical records, rendering, validation, reference resolution, and combined reporting.

