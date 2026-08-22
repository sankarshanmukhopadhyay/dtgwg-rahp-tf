---
layout: default
title: "Changelog"
nav_order: 7
has_toc: true
parent: Reference
---
# Changelog

This file records current release-level changes. The complete pre-v1.2 changelog, including accumulated historical `Unreleased` sections, is preserved at `archive/pre-v1.2/CHANGELOG-pre-v1.2.txt`.

## Unreleased — v1.5.0 release qualification candidate

### Added

- Durable assessment identity and finding lineage independent of individual assessment runs and issue trackers.
- Governed remediation obligations, acceptance criteria, closure evidence and executable retest lineage.
- Portable assurance graph with explicit impact-propagation semantics and deterministic reassessment selection.
- Evidence provenance manifests, conservative assurance freshness and machine-readable assurance deltas.
- Scoped executable authority with suspension, revocation and expiry state.
- Three-valued policy gates with `PASS`, `FAIL` and `INDETERMINATE` outcomes.
- Portable assurance posture for actionable operational/portfolio views without a synthetic assurance score.
- Machine-readable v1.5 capability/documentation registry and synchronization validation.
- Machine-readable v1.5 release qualification manifest and validator.
- Deployment-neutral conformance fixtures plus maintained deployment demonstrations.
- Release runbook and synchronized v1.5.0 preparation content.

### Changed

- The v1.5 lifecycle now connects target change → impact → freshness → reassessment/retest → assurance delta → remediation → policy gate → authority verification → operational posture.
- Portfolio presentation keeps assurance conclusion, freshness, remediation, gate and authority state separate rather than collapsing them into a percentage.
- Documentation synchronization is now a CI-enforced property across implemented v1.5 capabilities.
- The release boundary is explicitly evidence-based: the final release-cut commit should contain only version/release metadata, random butterfly-name selection and publication mechanics, not new method semantics.

### Compatibility

The stable v1 compatibility boundaries remain unchanged throughout qualification:

```text
rahp-engine-contract-v1
normalized result schema version 1
rahp-evidence-retention-v1
```

v1.2.0 remains the stable published release until v1.5.0 is actually tagged and published.

### Governance

- Policy evaluation never creates authority.
- Repository permissions are not automatically governance authority.
- Stale/retest-required assurance is not automatically a finding.
- Detector absence does not establish closure.
- Work-item deletion does not destroy canonical assurance lineage.
- Project-specific deployments remain demonstrations rather than portable-core dependencies.

See [v1.5.0 release preparation](docs/releases/v1.5.0-preparation.md) and the [v1.5 release runbook](docs/v1.5-release-runbook.md).

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

- Added the portable assurance knowledge model and catalogue.
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

Detailed v0.x and early v1 release notes remain under [`docs/releases/`](docs/releases/). The full pre-v1.2 changelog is retained for provenance at `archive/pre-v1.2/CHANGELOG-pre-v1.2.txt`.
