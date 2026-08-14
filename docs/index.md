---
layout: default
title: "RAHP Toolkit documentation"
nav_order: 1
has_toc: true
---
# RAHP Toolkit documentation

RAHP Toolkit is a **portable specification-assurance toolkit**. It provides a method, configuration contract, review tooling, scenario patterns, validation and evidence rendering for pressure-testing standards and technical specifications against risks, harms and adversarial failure conditions.

The repository contains deployments and examples, but **RAHP is not the DTG deployment and it is not the CAWG/C2PA deployment**. DTG is the historical origin and a bundled exemplar; CAWG/C2PA is the first substantial external deployment proving that the same method and engine can operate with independent scope, risks, state and governance.

## Start here

### Understand the portable method

Read [Concepts](concepts.md), [How RAHP works](how-rahp-works.md), and [Portability](portability.md). These pages describe the parts that belong to RAHP itself rather than to a particular deployment.

### Apply RAHP to your own target

Use [Configuration-driven adoption](configuration.md) and [Adopting RAHP](../ADOPTION.md), then follow [Pressure-testing a specification](pressure-testing-a-spec.md). The minimum path is: declare target repositories in YAML, pin review provenance, record evidence-backed findings, render, validate and re-test after change.

### Choose the analytical lens

- [RAHP pressure testing](pressure-testing-a-spec.md) focuses on people, harms, governance boundaries and assurance.
- [Security and hardening review](security-hardening-review.md) focuses on adversarial protocol and implementation failure.
- [Review modes](review-modes.md) explains `rahp`, `security`, and `combined` operation.
- [Scenario-driven pressure testing](scenario-driven-pressure-testing.md) applies reusable stress patterns and domain corpora.

### Examine independent deployments

- [CAWG/C2PA deployment](cawg-instance.md) — external portfolio, branch-aware source monitoring, instance-local risk vocabulary, 36-scenario corpus, 17 CAWG pressure-test reviews, security/combined reviews and issue-aware situational monitoring.
- [DTG exemplar deployment](dtg-instance.md) — historical origin, portfolio discovery, DTG scenario corpora, operational assurance and governance queue.

These deployments are **evidence of portability**, not prerequisites for adoption.

### Worked assessments

The [CAWG/C2PA assessment pack](../examples/cawg-c2pa/README.md) now demonstrates v0.7 scenario-driven, cross-specification and combined assurance. Earlier DTG examples remain useful regression fixtures for credential and protocol/framework reviews: [DTG Credential Specification](../examples/dtg-credential-spec/README.md) and [Trust Tasks](../examples/trust-tasks-spec/README.md).

### AI-assisted review

Use [AI-assisted RAHP](ai-assisted-process.md) and [Use an AI agent to run a pressure test](using-an-ai-agent.md). AI may prepare, synthesize and cross-reference evidence; accountable humans remain responsible for findings, risk judgements, acceptance and governance decisions.

### Evidence, governance and maintenance

- [Interpreting results](interpreting-results.md)
- [Governance boundaries](governance-boundaries.md)
- [Operational assurance](operational-assurance.md)
- [Assessment claims](conformance-claims.md)
- [Corpus synchronization and provenance](corpus-synchronization.md)
- [DTG exemplar governance action register](task-force-actions.md)
- [Roadmap](../ROADMAP.md)

## Historical material

The [Historical Library](../archive/) retains earlier personas, requirements, registers, spreadsheets and generated views. It is provenance, not the portable RAHP method and not current deployment state.
