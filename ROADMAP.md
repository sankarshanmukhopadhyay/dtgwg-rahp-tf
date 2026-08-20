---
layout: default
title: "Roadmap"
nav_order: 6
has_toc: true
parent: Reference
---
# RAHP Toolkit Roadmap

This roadmap records the current portable RAHP direction. Historical pre-v1.2 roadmap material is preserved under `archive/pre-v1.2/` for provenance and is not current authority.

## v1.2.0 — Evidence-Driven Assurance (complete)

v1.2.0 moves RAHP from signal-centric review to an evidence-driven assurance lifecycle while preserving the stable v1 compatibility boundary.

Delivered:

- typed assurance evaluations with `assured`, `controlled`, `finding`, `assurance-gap`, `review-required`, `not-assessed` and `not-applicable` residual states;
- first-class control credit and evidence classification by context and authority;
- explicit zero-finding semantics so unresolved assurance gaps cannot be rendered as a pass;
- additive normalized-result support for assurance summaries, evaluations, remediations and retests;
- DRARM-to-portable-assurance mappings where semantic equivalence exists, with explicit non-mappings otherwise;
- governed remediation manifests that separate ownership/routing from publication authority;
- evidence-based retest records and resolved/residual/regression transitions;
- Python and TypeScript reference implementation/conformance coverage.

Status: **stable release baseline**. See [v1.2.0 release notes](docs/releases/v1.2.0.md).

---

## v1.1.0 — Portable Assurance Knowledge Model (complete)

v1.1.0 introduced the portable method-level assurance catalogue for reusable harms, risks, controls, guardrails, assurance propositions and evidence contracts while preserving deployment independence.

Delivered:

- the portable `HRM/RKP/CTP/GRP/ATP/EVP` knowledge model;
- catalogue schema and machine validation;
- catalogue-aware pressure-test, security-review and scenario validation;
- a governed simple-English glossary;
- guardrail applicability and coverage semantics;
- generated portable catalogue and assurance graph views;
- maintained DTG, CAWG/C2PA, A2A and cross-specification examples.

Status: **complete**. See [v1.1.0 release notes](docs/releases/v1.1.0.md).

---

## v1.0.0 — Stable Method and Implementation Conformance (complete)

v1.0.0 froze the stable v1 boundaries:

```text
rahp-engine-contract-v1
normalized result schema version 1
rahp-evidence-retention-v1
```

It also established explicit compatibility/versioning rules, Python/TypeScript reference conformance, documentation IA validation and deployment independence.

Status: **stable compatibility baseline**. See [v1.0.0 release notes](docs/releases/v1.0.0.md).

---

# Next priorities

## v1.3 — Assurance operations and remediation evidence

The next minor release should operationalize the v1.2 assurance model without weakening its authority boundaries.

Candidate scope:

1. **Assessment-to-remediation correlation**
   - generate durable remediation manifests from dispositioned RAHP findings;
   - correlate upstream work items back to immutable assessment/finding IDs;
   - keep external publication separately authorized.

2. **Retest automation**
   - run a retest against a new target revision;
   - compare residual assurance states;
   - emit machine-readable `resolved`, `residual` or `regression` evidence;
   - never auto-close external issues solely because a detector no longer fires.

3. **Assurance evidence requirements**
   - make missing tests, metrics, fixtures and operational evidence executable work products;
   - support profile-specific evidence obligations without coupling core RAHP to a portfolio.

4. **Signal-to-noise qualification**
   - measure observations, triggers, findings, suppressed signals and publication candidates across maintained portfolios;
   - use the evidence to calibrate thresholds and controlled publication policies.

5. **Generated assurance views**
   - render residual-state summaries, credited controls, missing evidence, remediation state and retest history in GitHub Pages.

Release gate: **machine-verifiable evidence that the operational lifecycle preserves the v1.2 distinction between signal, finding, assurance gap, remediation authority and closure evidence.**

## Future major-version boundary

A v2 release is required for breaking changes to the stable method or normalized-result compatibility boundary. Candidate v2 topics may include a redesigned result schema, new mandatory lifecycle stages, or removal/renaming of published identifiers. These are not v1.x changes.

## Explicit non-goals

The roadmap does not make these default RAHP behaviours:

- automatic filing into arbitrary upstream repositories;
- treating observation permission as publication authority;
- equating detector absence with assurance;
- coupling the portable method to DTG, CAWG/C2PA, OpenVTC, ARPA or any other deployment;
- requiring a third implementation language without demonstrated adopter need.

## Historical roadmap

The full pre-v1.2 roadmap, including early DTG migration history, v0.x architecture decisions and the original governed finding-to-issue design, is retained at `archive/pre-v1.2/ROADMAP-pre-v1.2.txt`.
