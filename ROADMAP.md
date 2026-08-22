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

# Next release target

## v1.5.0 — Continuous Governed Assurance

RAHP will accumulate additive capability commits on `main` until the continuous governed assurance lifecycle is qualified as a coherent release. No v1.3.x or v1.4.x releases are planned. The stable public baseline remains v1.2.0 until v1.5.0 is ready.

The v1.5 programme turns evidence-driven point-in-time assessment into durable, continuously governed assurance while preserving the v1 compatibility boundary and deployment independence.

### Portability invariant

Every v1.5 capability MUST be defined first as a portable method, schema, engine or conformance contract. Project-specific deployments may demonstrate or stress-test that capability, but must not define core semantics or become core dependencies.

This means DTG, OpenVTC, ARPA, CAWG/C2PA and other maintained examples are evidence that the portable method works in materially different environments. A completely unrelated specification, repository, service, dataset or governance process must be able to use the same core contracts without inheriting those projects' vocabulary, authority structures or repository layouts.

### Development workstreams

1. **Durable assessment and finding lineage**
   - separate stable assessment identity from individual assessment runs;
   - preserve finding evolution across `introduced`, `unchanged`, `reclassified`, `consolidated`, `split`, `superseded`, `resolved` and `regressed` transitions;
   - treat issue trackers and queues as operational work-item views rather than canonical assurance identity;
   - validate the core contract using deployment-neutral fixtures.

2. **Governed remediation and retest**
   - correlate findings to remediation obligations and acceptance evidence;
   - retest against changed targets without equating detector absence with closure;
   - preserve risk-acceptance, publication and external-change authority boundaries.

3. **Assurance graph and impact analysis**
   - connect targets, requirements, evidence, risks, controls, tests, findings, remediations and governance authorities;
   - identify which assurance conclusions may be affected by a material target change;
   - keep profile-specific graph data outside the portable method contract.

4. **Evidence provenance and assurance freshness**
   - make evidence origin, revision, production mechanism, integrity and authority class machine-readable;
   - distinguish current, potentially stale, stale, superseded and retest-required assurance;
   - produce machine-readable assurance deltas between assessment runs.

5. **Executable authority and policy gates**
   - model who may observe, assess, disposition, remediate, publish, accept risk, close and reopen;
   - reject lifecycle transitions that exceed delegated authority;
   - support `PASS`, `FAIL` and `INDETERMINATE` gate outcomes so uncertainty is not silently converted into success or failure.

6. **Portfolio and deployment presentation**
   - render current assurance, changed assurance, critical residual obligations, evidence gaps, stale assessments, remediation state and retest history;
   - avoid synthetic assurance percentages that collapse materially different states;
   - ensure portfolio dashboards remain views over portable assurance records rather than an alternative source of authority.

7. **Release qualification**
   - demonstrate Python/TypeScript conformance and v1.2 result compatibility;
   - test assessment reconstruction independently from GitHub issue state;
   - prove regression detection, freshness invalidation, impact selection and unauthorized-transition rejection;
   - qualify at least one deployment-neutral fixture plus multiple independent real-world deployments.

### Current implementation status

Four v1.5 development tranches are now represented in the portable contracts:

- durable assessment and finding lineage, with deployment-neutral fixtures and stable identities independent of work-item trackers;
- governed remediation and executable retest lineage, including acceptance criteria, closure evidence and authority-aware disposition;
- assurance graph and deterministic impact analysis, with explicit edge propagation semantics and machine-readable retest candidate selection;
- evidence provenance, conservative assurance freshness and machine-readable assurance delta, including baseline-to-current evidence succession and explicit uncertainty preservation.

See [Assurance lineage](docs/assurance-lineage.md), [Remediation and retesting](docs/remediation-lifecycle.md), [Assurance graph and impact analysis](docs/assurance-graph-impact.md), and [Evidence provenance and freshness](docs/evidence-freshness-delta.md).

### v1.5 release gate

v1.5.0 is releasable when RAHP can demonstrate the following end-to-end lifecycle with machine-verifiable evidence:

```text
material target change
        ↓
affected assurance identified
        ↓
existing evidence retained, weakened or invalidated
        ↓
assessment rerun where required
        ↓
assurance delta produced
        ↓
residual obligation governed
        ↓
remediation evidence attached
        ↓
retest executed
        ↓
authority-valid disposition
        ↓
current assurance state published
```

The release must preserve:

```text
portable method
independent deployment context
authority separation
evidence provenance
stable v1 compatibility
```

## Future major-version boundary

A v2 release is required for breaking changes to the stable method or normalized-result compatibility boundary. Candidate v2 topics may include a redesigned result schema, new mandatory lifecycle stages, or removal/renaming of published identifiers. These are not v1.x changes.

## Explicit non-goals

The roadmap does not make these default RAHP behaviours:

- automatic filing into arbitrary upstream repositories;
- treating observation permission as publication authority;
- equating detector absence with assurance;
- coupling the portable method to DTG, CAWG/C2PA, OpenVTC, ARPA or any other deployment;
- requiring project-specific vocabulary, repository structure or governance roles in portable core;
- requiring a third implementation language without demonstrated adopter need.

## Historical roadmap

The full pre-v1.2 roadmap, including early DTG migration history, v0.x architecture decisions and the original governed finding-to-issue design, is retained at `archive/pre-v1.2/ROADMAP-pre-v1.2.txt`.
