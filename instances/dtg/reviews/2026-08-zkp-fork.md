---
title: "DTG review: ZKP fork RAHP v1.1 and interoperability refresh"
parent: DTG RAHP review record
nav_order: 30
layout: default
nav_exclude: true
---

# DTG review: ZKP fork RAHP v1.1 and interoperability refresh

**Assessment ID:** `DTG-AR-2026-003`  
**Assessment key:** `dtg:repository:sankarshanmukhopadhyay/dtgwg-zkp-tf`  
**Mode:** combined RAHP + security  
**Status:** dispositioned  
**Disposition:** no-material-assurance-impact  
**Reviewed revision:** `a67ba80cf231a77b9608646c117f80a64d89567b`

## Scope

This review covers `9a1ae81465e1da9f5c06ccd500a70708eb2511a6` →
`a67ba80cf231a77b9608646c117f80a64d89567b` and dispositions RAHP toolkit
issue **#11**.

The change window is principally an assurance/interoperability refresh rather than a new
cryptographic primitive. It adds a machine-readable cross-specification assurance register,
requirements-to-assurance traceability, authority/evidence boundaries and new/rerun pressure
tests against the current Trust Tasks and Credential Specification baselines.

## Assessment

The revision improves the fork's assurance posture in five material ways:

1. **Cross-spec dependencies are pinned.** Pressure tests identify reviewed upstream
   revisions and explicit retest triggers rather than relying on undated narrative links.
2. **Proof remains subordinate to authority.** Trust Task × ZKP scenarios test that proof
   possession/validity cannot substitute for action authority, delegation scope or current
   lifecycle status.
3. **Effect-time re-evaluation is modeled.** New task-lifecycle scenarios ask which evidence
   must be re-evaluated when work is delayed, suspended or resumed.
4. **Witness evidence is bounded.** Witness/edge-digest scenarios test replay, correlation
   and exact relationship binding rather than treating witness participation as authority.
5. **Implementation evidence is kept non-normative.** OpenVTC implementations are tracked as
   evidence sources without being promoted into the source of specification semantics.

The cross-spec assurance register explicitly pins Trust Tasks to
`7e0d755f5b815498c861cacecee5cae49b3f14eb`, matching the newly dispositioned
Trust Tasks review in this RAHP instance.

## Residual dependencies

- Credential linkage remains sensitive to correlation and subject/controller-binding semantics.
- Delegation/current-authority semantics remain external governance dependencies.
- Exploratory VDS, Agent Names and HTX relationships are intentionally not represented as
  active bindings until the ZKP profile actually depends on them.

These are correctly represented as retest triggers rather than silently assumed closure.

## Assurance disposition

No new blocking assurance or security defect is introduced by this change window. The delta
is a **material strengthening of traceability and cross-specification assurance discipline**.

This record closes RAHP toolkit issue **#11** for revision
`a67ba80cf231a77b9608646c117f80a64d89567b`.

## Sources

- <https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/compare/9a1ae81465e1da9f5c06ccd500a70708eb2511a6...a67ba80cf231a77b9608646c117f80a64d89567b>
- <https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/blob/a67ba80cf231a77b9608646c117f80a64d89567b/docs/implementation-guide/interoperability/cross-spec-assurance-register.yaml>
