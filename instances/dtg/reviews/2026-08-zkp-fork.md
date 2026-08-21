---
title: "DTG review: ZKP fork RAHP v1.1 and executable-evidence refresh"
parent: DTG RAHP review record
nav_order: 30
layout: default
nav_exclude: true
---

# DTG review: ZKP fork RAHP v1.1 and executable-evidence refresh

**Assessment ID:** `DTG-AR-2026-003`  
**Assessment key:** `dtg:repository:sankarshanmukhopadhyay/dtgwg-zkp-tf`  
**Mode:** combined RAHP + security  
**Status:** dispositioned  
**Disposition:** no-blocking-assurance-impact  
**Assessment queue disposition:** `no-material-assurance-impact`  
**Reviewed revision:** `546babc471130af751ed3a117a0d476f5e0a7e03`

## Scope

This review now covers the previously dispositioned assurance/interoperability refresh and
advances the durable baseline through the material change window
`4034bd23f9c4421bd87d000f787cb7f2afaddf77` →
`546babc471130af751ed3a117a0d476f5e0a7e03`, dispositioning RAHP toolkit
issue **#27**.

The new window is principally a **conformance and evidence execution release**, not a new
cryptographic construction. It establishes a complete repository validation gate, semantic
fixtures, a fixture-backed harness adapter, external-evidence governance and a v0.5.0 release
evidence package.

## Material assurance changes

1. **Semantic assurance is executable.** Eleven new fixtures cover revocation timing,
   constrained-device ceilings, mediated proving, attestation-schema correlation,
   governed context and lifecycle bounds.
2. **Fixtures are evaluated rather than merely table-matched.** The harness adds a
   semantic fixture adapter that derives outcomes from repository-owned JSON.
3. **Repository validation is consolidated.** A single quality gate executes 19
   validators, harness unit tests and deterministic manifests.
4. **Execution coverage is explicit.** 27 of 96 protocol cases are executable; the
   remaining 69 are not presented as passing. They remain explicitly blocked on
   construction selection.
5. **External evidence cannot silently become normative.** The evidence register records
   licence and provenance status and prevents unverified external material from becoming
   vendored content, CI dependencies or conformance evidence.
6. **Upstream synchronisation is made more resilient.** Drift reporting is preserved even
   where issue creation is unavailable, reducing the chance that fork divergence is hidden.
7. **Generated artifacts are excluded.** Python bytecode is removed and repository
   cleanliness is part of release acceptance.

## Residual assurance states

### Construction-dependent conformance coverage

**Residual state:** `review-required`

The 69 construction-blocked cases remain outside executable cryptographic conformance.
This is correctly represented as an explicit blocker rather than a false pass.

**Owner:** ZKP construction-selection / conformance workstream.  
**Retest condition:** construction selection enables executable proof-system adapters and
those cases acquire deterministic pass/fail evidence.

### Cross-spec authority and lifecycle dependencies

**Residual state:** `assurance-gap`

Proof validity still does not establish current delegated authority, relying-party purpose
or action-time lifecycle state. These remain composition obligations with Trust Tasks,
Credential Specification and governance profiles.

**Owner:** cross-specification companion profiles.  
**Retest condition:** adopted profiles expose and test authority, purpose, audience,
freshness and revocation semantics at the composed decision boundary.

## Assurance disposition

No new blocking assurance or security defect is introduced by the reviewed window. The
delta is a **material strengthening of evidence execution, release integrity and
conformance honesty**.

The most important assurance property is that incomplete cryptographic coverage is not
rendered green: executable cases are distinguished from governed construction blockers.

This record closes RAHP toolkit issue **#27** for revision
`546babc471130af751ed3a117a0d476f5e0a7e03`.

## Sources

- <https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/compare/4034bd23f9c4421bd87d000f787cb7f2afaddf77...546babc471130af751ed3a117a0d476f5e0a7e03>
- <https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/blob/546babc471130af751ed3a117a0d476f5e0a7e03/RELEASE_NOTES_v0.5.0.md>
- <https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/blob/546babc471130af751ed3a117a0d476f5e0a7e03/conformance-harness/examples/semantic-fixture-manifest.json>
