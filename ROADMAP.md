---
layout: default
title: "Roadmap"
nav_order: 6
has_toc: true
parent: Reference
---
# RAHP Toolkit Roadmap

This roadmap records the current portable RAHP direction. Historical pre-v1.2 roadmap material is preserved under `archive/pre-v1.2/` and is not current authority.

## v1.5.0 — Continuous Governed Assurance (stable release)

Status: **stable public release — Purple Leaf Blue (*Amblypodia anita*)**.

v1.5 turns evidence-driven point-in-time assessment into durable, continuously governed assurance while preserving the v1 compatibility boundary and deployment independence.

### Portability invariant

Every v1.5 capability is defined first as a portable method, schema, engine or conformance contract. DTG, OpenVTC, ARPA, CAWG/C2PA and other deployments may demonstrate or stress-test those capabilities but do not define core semantics or become core dependencies.

A completely unrelated specification, repository, implementation, service, dataset, governance process or composed system must be able to use the same core contracts.

### Delivered workstreams

1. **Durable assessment and finding lineage**
   - stable assessment identity independent of run identity and work-item trackers;
   - explicit finding evolution across introduced, unchanged, reclassified, consolidated, split, superseded, resolved and regressed transitions.

2. **Governed remediation and retest**
   - remediation obligations with acceptance criteria, retest triggers and closure evidence;
   - detector absence is not closure;
   - risk acceptance and closure remain separate authority-bearing actions.

3. **Assurance graph and impact analysis**
   - portable dependency graph with explicit impact-propagation semantics;
   - deterministic affected-assessment and retest candidate selection;
   - graph reachability is selection evidence, not an assurance conclusion.

4. **Evidence provenance, freshness and delta**
   - machine-readable evidence source, revision, producer, integrity and authority metadata;
   - current, potentially-stale, stale, retest-required, superseded and indeterminate freshness;
   - machine-readable assurance deltas and regression/resolution semantics.

5. **Executable authority and policy gates**
   - independently scoped observe, assess, disposition, remediate, publish, accept-risk, close and reopen authority;
   - suspension, revocation and expiry as executable states;
   - policy gates return PASS, FAIL or INDETERMINATE without minting authority.

6. **Portfolio and deployment presentation**
   - portable assurance posture separates conclusion, freshness, remediation, gate and authority state;
   - actionable counts expose stale/retest work, evidence gaps, blockers and changed assessments;
   - no synthetic assurance percentage is produced.

7. **Release qualification**
   - `method/v1.5-release-qualification.yaml` defines required capabilities, compatibility boundaries, neutral evidence, portability constraints and release policy;
   - `tools/validate_v15_release.py` validates capability completeness, portability, deterministic posture evidence and release naming policy;
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

## Compatibility

The stable v1 compatibility boundaries remain:

```text
rahp-engine-contract-v1
normalized result schema version 1
rahp-evidence-retention-v1
```

v1.5.0 is additive within that boundary. Existing v1.1 and v1.2 normalized results remain valid.

See [v1.5.0 release notes](docs/releases/v1.5.0.md), [Assurance posture](docs/assurance-posture.md), and the [v1.5 release runbook](docs/v1.5-release-runbook.md).

## v1.2.0 — Evidence-Driven Assurance

v1.2 established typed assurance conclusions, first-class control credit, evidence classification, explicit zero-finding semantics, governed remediation/retest records, DRARM mappings, and Python/TypeScript conformance.

See [v1.2.0 release notes](docs/releases/v1.2.0.md).

## Future work

Subsequent v1.5.x releases may refine implementation, adoption and operational tooling without breaking the stable v1 contracts. Each v1.5.x release receives its own randomly selected West Bengal butterfly release name at release time.

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
