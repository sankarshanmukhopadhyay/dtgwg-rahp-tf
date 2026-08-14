# CAWG Organizational Identity Profile 1.1 draft pressure test

This is a RAHP Toolkit v0.7.0 external assurance review. It is not an upstream conformance or governance decision.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-SR-012` |
| Status | complete |
| Title | CAWG Organizational Identity Profile 1.1 draft pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-organizational-identity-profile` |
| Target document | https://cawg.io/organizational-identity-profile/1.1-draft/ |
| Target version | 1.1 draft |
| Target commit | `ad951176b1d428e027c3c20c48506b2b780a8f77` |
| Target source paths | — |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v0.7.0` |
| RAHP corpus date | 2026-08-14 |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/pressure-testing-a-spec.md` |
| Rule | Separate cryptographic validity, identity, authority, consent, lifecycle and relying-party trust; test both isolated and composed failure states. |

### Review scope

**Included**

- Normative and draft semantics relevant to the named composition or experiment.
- Cross-specification failure states that can remain hidden when each component is reviewed independently.

**Excluded**

- Legal opinion on enforceability in a particular jurisdiction.
- Claims that upstream CAWG, DIF, C2PA, GLEIF or W3C endorsed this RAHP assessment.

### Summary

| Measure | Value |
|---|---:|
| Findings | 2 |
| Open findings | 2 |
| Primary disposition: Companion Specification | 1 |
| Primary disposition: Governance | 1 |

**Overall assessment**

The 1.1 profile is a strong deployment surface but should pair implementation conformance with explicit authority and cross-version behavior.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Generator and validator profiles can diverge across supported C2PA versions | High | open | Companion Specification | [CRK-28 — Implementation/specification semantic collapse](/rahp-toolkit/docs/cawg-risk-register.html#crk-28) |
| `F-002` | Profile conformance still does not establish organization authority | High | open | Governance | [CRK-01 — Identity-validity and authority conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-01) |

### Detailed findings

#### F-001 — Generator and validator profiles can diverge across supported C2PA versions

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | — |
| Scenarios | `CAWG-028` |
| Scenario patterns | `SP-INTEROP-01`, `SP-COMP-01` |
| Personas | — |
| Risks | [CRK-28 — Implementation/specification semantic collapse](/rahp-toolkit/docs/cawg-risk-register.html#crk-28) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-organizational-identity-profile/commits/ad951176b1d428e027c3c20c48506b2b780a8f77` | Version 1.1 separates generator and validator requirements while spanning multiple C2PA versions. |

**Potential harm**

Content may be generated under capabilities a validator nominally conforming to the profile does not interpret identically.

**Recommended treatment**

Add paired generator/validator conformance vectors and explicit version-negotiation/failure semantics.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

#### F-002 — Profile conformance still does not establish organization authority

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | — |
| Scenarios | `CAWG-001`, `CAWG-003` |
| Scenario patterns | `SP-GOV-01`, `SP-FED-01` |
| Personas | — |
| Risks | [CRK-01 — Identity-validity and authority conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-01) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/organizational-identity-profile/1.1-draft/` | The profile standardizes implementation capabilities, while relying-party trust in an organization remains external. |

**Potential harm**

A conformant product can validate organizational identity without proving authorization for a particular domain claim.

**Recommended treatment**

Bind profile deployment to explicit trust-policy and authority semantics; expose these separately from conformance.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

<!-- END GENERATED PRESSURE TEST -->

