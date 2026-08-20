---
layout: default
title: "Changelog"
nav_order: 7
has_toc: true
parent: Reference
---
# Changelog

This file records current release-level changes. The complete pre-v1.2 changelog, including accumulated historical `Unreleased` sections, is preserved at `archive/pre-v1.2/CHANGELOG-pre-v1.2.md`.

## v1.2.0 — 2026-08-20

### Added

- Evidence-driven assurance evaluation with seven residual states: `assured`, `controlled`, `finding`, `assurance-gap`, `review-required`, `not-assessed` and `not-applicable`.
- Typed evidence classification by repository/context surface and authority weight.
- First-class control credit so risk signals can be evaluated against controls and assurance evidence before a residual conclusion is assigned.
- `method/schema/assurance-evaluation.schema.json`.
- `method/schema/remediation-manifest.schema.json`.
- `method/schema/retest.schema.json`.
- `method/mappings/resilience-to-assurance.yaml` for semantically valid DRARM-to-portable-pattern mappings.
- Python assurance evaluation and CLI support.
- TypeScript schema/core/CLI support for assurance summaries, residual inference and retest outcomes.
- Cross-implementation conformance fixtures for confirmed findings, assurance gaps, controlled targets, remediation manifests and retest transitions.
- Documentation for assurance evaluation, evidence classification, result interpretation and remediation/retest lifecycle.

### Changed

- Detector output is explicitly a signal rather than an automatic finding.
- Normalized result schema version `1` gains optional assurance summaries, evaluations, remediations and retests while preserving v1.1 result validity.
- `rahp-engine-contract-v1` gains additive assurance-evaluation/remediation/retest operations without changing its stable contract identifier.
- Zero-finding semantics now prevent unresolved `assurance-gap`, `review-required` or `not-assessed` states from being represented as `no-material-assurance-impact`.
- DRARM is integrated as a specialized signal provider into the portable assurance graph where semantic equivalence exists; unmatched rules remain explicitly unmapped.
- Remediation ownership/routing is machine-readable while external publication authority remains separately governed.
- Root README and roadmap are aligned to the evidence-driven v1.2 lifecycle.
- TypeScript workspace, package and lockfile metadata advance to `1.2.0`.
- `method/versioning.yaml` advances the declared stable release to `v1.2.0`.

### Compatibility

The stable v1 boundaries remain unchanged:

```text
rahp-engine-contract-v1
normalized result schema version 1
rahp-evidence-retention-v1
```

v1.2.0 is an additive minor release. Existing v1.1 normalized results remain valid.

### Governance

- A remediation manifest can identify an owning repository/control plane but does not grant authority to publish externally.
- Observation, assessment and publication remain distinct capabilities.
- Evidence-based retesting is the closure mechanism; detector absence alone is not proof of resolution.

See [v1.2.0 release notes](docs/releases/v1.2.0.md).

## v1.1.0 — 2026-08-17

- Added the portable 149-pattern `HRM/RKP/CTP/GRP/ATP/EVP` assurance catalogue.
- Added catalogue validation, catalogue-aware review mappings and portable scenario stress patterns.
- Added the governed simple-English glossary and explicit guardrail applicability semantics.
- Expanded maintained DTG, CAWG/C2PA, A2A and cross-specification examples.
- Added generated portable catalogue and assurance graph views.
- Preserved `rahp-engine-contract-v1`, normalized result schema version `1` and `rahp-evidence-retention-v1`.

See [v1.1.0 release notes](docs/releases/v1.1.0.md).

## v1.0.0

- Established the stable v1 method/versioning boundary.
- Added Python/TypeScript differential conformance.
- Formalized evidence retention and normalized-result compatibility.
- Added documentation information-architecture validation.

See [v1.0.0 release notes](docs/releases/v1.0.0.md).

## Historical releases

Detailed v0.x and early v1 release notes remain under [`docs/releases/`](docs/releases/). The full pre-v1.2 changelog is retained for provenance under `archive/pre-v1.2/`.
