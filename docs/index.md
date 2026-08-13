---
layout: default
title: "DTG instance"
nav_order: 13
has_toc: true
---
# RAHP documentation

RAHP has four primary paths:

## Understand

Start with [Concepts](concepts.md) and [How RAHP works](how-rahp-works.md) to understand people and power, risks and harms, controls and guardrails, and assurance evidence.

## Apply

Use [Pressure-testing a specification](pressure-testing-a-spec.md), then [Interpreting results](interpreting-results.md) and [Governance boundaries](governance-boundaries.md). Complete worked reviews are available under `examples/dtg-credential-spec/` and `examples/trust-tasks-spec/`. Together they demonstrate pressure testing of both a credential schema specification and a protocol/framework specification, including cross-layer finding disposition. In each example, `pressure-test.yaml` is canonical and the structured review section in `README.md` is generated with `tools/render_pressure_tests.py`. A reusable starter is available at `examples/pressure-test-template.yaml`. Generated RAHP citations resolve to `build/site/catalogue.html#<ID>`, which provides a stable, deep-linkable definition and cross-reference context for every canonical artefact.

## Delegate repeatable work to an AI agent

Use [Use an AI agent to run a pressure test](using-an-ai-agent.md) for an agent-friendly operating model, prompt contract, command path, evidence rules, and explicit human accountability checkpoints.

## Maintain synchronized corpora

Use [Corpus synchronization and provenance](corpus-synchronization.md) to understand how RAHP detects changes in related repositories, consumes DTG Portfolio Monitor scope metadata, preserves immutable source provenance, and prepares review packets without silently rewriting corpus semantics.

## Explore historical personas and earlier RAHP material

Use the [Historical Library](../archive/) to read the retained persona set, priority requirements, historical risk register, user-stories workbook, structured JSON-LD records, and earlier generated RAHP views. Archive pages are deliberately labelled as historical so useful context remains accessible without being confused with current canonical material.

## Explore the DTG instance

Canonical records live under `data/`. Generated risk, control, matrix, lifecycle, normative and governance views are built under `build/site/` with `python3 tools/build.py`.

The generated site is a drill-down evidence surface; the guided documentation is the entry point.

## Security hardening

For adversarial protocol review beyond the general risks-and-harms workflow, use [Security and hardening review workflow](security-hardening-review.md). The coordinated DTG example set covers [Trust Tasks](../examples/security-hardening/trust-tasks/SECURITY_REVIEW.md), [DTG Core Credentials](../examples/security-hardening/credential-spec/SECURITY_REVIEW.md), and [cross-spec composition](../examples/security-hardening/cross-spec/COMPOSITION_THREAT_MODEL.md).
## Review modes

Use [Review modes](review-modes.md) for the unified `tools/review.py` entry point. A checkout can scaffold a risks-and-harms RAHP review, an adversarial security-hardening review, or both together. Combined mode retains the two canonical records and generates a cross-lens synthesis rather than collapsing the methodologies into one finding type. Worked combined reports are available for the [DTG Credential Specification](../examples/combined/dtg-credential-spec/COMBINED_REVIEW.md) and [Trust Tasks](../examples/combined/trust-tasks-spec/COMBINED_REVIEW.md).

