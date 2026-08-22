---
layout: default
title: "Roadmap"
nav_order: 6
has_toc: true
parent: Reference
---
# RAHP Toolkit Roadmap

This roadmap records the current portable RAHP direction. Historical pre-v1.2 roadmap material is preserved under `archive/pre-v1.2/` and is not current authority.

## v1.2.0 — Evidence-Driven Assurance (stable baseline)

Status: **stable public release**.

v1.2 established typed assurance conclusions, first-class control credit, evidence classification, explicit zero-finding semantics, governed remediation/retest records, DRARM mappings, and Python/TypeScript conformance while preserving:

```text
rahp-engine-contract-v1
normalized result schema version 1
rahp-evidence-retention-v1
```

See [v1.2.0 release notes](docs/releases/v1.2.0.md).

## Next release

### v1.5.0 — Continuous Governed Assurance

Status: **release qualification candidate**. No v1.3.x or v1.4.x releases are planned.

v1.5 turns evidence-driven point-in-time assessment into durable, continuously governed assurance while preserving the v1 compatibility boundary and deployment independence.

### Portability invariant

Every v1.5 capability is defined first as a portable method, schema, engine or conformance contract. DTG, OpenVTC, ARPA, CAWG/C2PA and other deployments may demonstrate or stress-test those capabilities but do not define core semantics or become core dependencies.

A completely unrelated specification, repository, implementation, service, dataset, governance process or composed system must be able to use the same core contracts.

## Implemented v1.5 workstreams

1. **Durable assessment and finding lineage — implemented**
   - stable assessment identity is independent of run identity and work-item trackers;
   - finding evolution supports introduced, unchanged, reclassified, consolidated, split, superseded, resolved and regressed transitions.

2. **Governed remediation and retest — implemented**
   - remediation obligations carry acceptance criteria, retest triggers and closure evidence;
   - detector absence is not closure;
   - risk acceptance and closure remain separate authority-bearing actions.

3. **Assurance graph and impact analysis — implemented**
   - portable dependency graph with explicit impact-propagation semantics;
   - deterministic affected-assessment and retest candidate selection;
   - graph reachability is selection evidence, not an assurance conclusion.

4. **Evidence provenance, freshness and delta — implemented**
   - machine-readable evidence source, revision, producer, integrity and authority metadata;
   - current, potentially-stale, stale, retest-required, superseded and indeterminate freshness;
   - machine-readable assurance deltas and regression/resolution semantics.

5. **Executable authority and policy gates — implemented**
   - independently scoped observe, assess, disposition, remediate, publish, accept-risk, close and reopen authority;
   - suspension, revocation and expiry are executable states;
   - policy gates return PASS, FAIL or INDETERMINATE without minting authority.

6. **Portfolio and deployment presentation — implemented**
   - portable assurance posture separates conclusion, freshness, remediation, gate and authority state;
   - actionable counts expose stale/retest work, evidence gaps, blockers and changed assessments;
   - no synthetic assurance percentage is produced.

7. **Release qualification — implemented as a machine-verifiable candidate gate**
   - `method/v1.5-release-qualification.yaml` defines required capabilities, compatibility boundaries, neutral evidence, portability constraints and cut policy;
   - `tools/validate_v15_release.py` validates capability completeness, portability, deterministic posture evidence and naming policy;
   - CI runs the qualification validator alongside the full repository suite;
   - capability/documentation synchronization remains an executable gate.

## v1.5 end-to-end lifecycle

```text
material target change
        ↓
impact selection
        ↓
freshness evaluation
        ↓
evidence retained / weakened / invalidated
        ↓
assessment or retest
        ↓
assurance delta
        ↓
residual obligation + remediation
        ↓
policy gate: PASS | FAIL | INDETERMINATE
        ↓
independent authority verification
        ↓
governed disposition/publication
        ↓
portable assurance posture
```

The lifecycle preserves uncertainty and authority boundaries at every step.

## Release qualification evidence

v1.5.0 is cut-ready only when all of the following are green together:

- deployment-neutral lineage, remediation/retest, impact, freshness/delta, authority/gate and posture fixtures;
- Python/TypeScript stable-engine conformance;
- v1.2 compatibility metadata;
- documentation synchronization and information-architecture validation;
- generated-evidence freshness and reference-link validation;
- Just the Docs build and rendered Pages coverage;
- project-specific deployment validations without making those deployments core dependencies;
- `python3 tools/validate_v15_release.py`.

See [Assurance posture](docs/assurance-posture.md) and the [v1.5 release runbook](docs/v1.5-release-runbook.md).

## Final release-cut boundary

Once qualification passes, the final v1.5.0 release change should be deliberately mechanical. It will select the West Bengal butterfly release name at random, update version/release metadata, finalize v1.5.0 release notes, rerun the gates, tag the exact commit and publish the GitHub release.

No new method semantics should enter through the release-cut commit. Any semantic change requires a separate PR and renewed qualification.

## Future major-version boundary

A v2 release is required for breaking changes to the stable method or normalized-result compatibility boundary.

## Explicit non-goals

RAHP does not make these default behaviours:

- automatic filing into arbitrary upstream repositories;
- treating repository permissions as governance authority;
- treating a policy-gate PASS as delegation, publication authority or risk acceptance;
- equating detector absence with assurance;
- coupling portable core to a maintained deployment;
- using a universal assurance score to hide materially different states.

## Historical roadmap

The full pre-v1.2 roadmap is retained at `archive/pre-v1.2/ROADMAP-pre-v1.2.txt`.
