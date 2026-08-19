---
layout: default
title: "Quick start"
nav_order: 21
has_toc: true
---
# RAHP Quickstart

Use this path when you want useful output before learning every artefact type.

1. **Choose a target.** Record the specification/system, version or commit, and review scope.
2. **Choose 3–6 personas.** Start with portable `Pxx` roles, then add machine, adversarial, or deployment-specific personas when they materially change the analysis.
3. **Reuse the deployment's existing risks.** Search the applicable risk catalogue (for example `instances/<id>/data/risks.yaml`; the bundled DTG exemplar uses `data/risks.yaml`) before inventing new hypotheses.
4. **Pressure-test 5–15 hypotheses.** Ask what fails, who is harmed, what harmful inference remains possible, and what can remain technically valid while governance-invalid.
5. **Map controls only where needed.** Use guardrails for hard stops and assurance tests for evidence.
6. **Route each finding.** Decide the correct control plane using `docs/governance-boundaries.md`.
7. **Publish recommendations.** Make each action traceable to evidence and status.
8. **Render, validate and disposition.** Keep ordinary run artefacts in the ignored `.rahp/` workspace, render and validate the canonical review record, then deliberately promote only maintained exemplars or preserve a compact deployment disposition. Re-run the review when a retest trigger or target change occurs.

```bash
pip install -r requirements.txt
python3 tools/validate.py
python3 tools/render_pressure_tests.py
python3 tools/validate_pressure_tests.py
python3 tools/build.py
python3 tools/validate_reference_links.py
```

For the complete process, see [ADOPTION.md](ADOPTION.md) and [docs/pressure-testing-a-spec.md](docs/pressure-testing-a-spec.md).


Worked pressure tests: [`examples/cawg-c2pa/`](examples/cawg-c2pa/README.md), [`examples/a2a/`](examples/a2a/README.md), [`examples/dtg-credential-spec/`](examples/dtg-credential-spec/README.md), and [`examples/trust-tasks-spec/`](examples/trust-tasks-spec/README.md). These are curated exemplars, not the default storage location for ordinary runs.


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
## Run a distributed-resilience assessment

```bash
python3 tools/rahp.py resilience \
  --path ../target-repository \
  --repository owner/repository \
  --revision <tag-or-commit>
```

Use `examples/resilience/openvtc-cypress/profile.yaml` as a worked profile example, not as a dependency.

