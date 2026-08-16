# CAWG Identity Assertion pressure test

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This worked review is part of the RAHP v0.6.0 CAWG/C2PA external-deployment proof. It is an independent assessment and does not represent CAWG, DIF or C2PA consensus.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-SR-001` |
| Status | complete |
| Title | CAWG Identity Assertion pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-identity-assertion` |
| Target document | https://cawg.io/identity/1.3-draft/ |
| Target version | 1.3 WG-approved draft |
| Target commit | `8a9c4925df7e8ccbcabce9d754fc27739e11dc12` |
| Target source paths | — |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v0.8.0` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-16 |
| Engine/method revalidated on | 2026-08-16 |
| Original RAHP version | `v0.6.0` |
| Revalidation scope | method-and-engine-only; target revision and substantive findings unchanged |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/pressure-testing-a-spec.md` |
| Rule | Treat cryptographic validity, identity, authority, consent, provenance and relying-party trust as distinct propositions; route remediation to the narrowest effective control plane. |

### Review scope

**Included**

- Credential-backed named-actor identity, validation status, role semantics, trust and lifecycle boundaries.

**Excluded**

- Implementation-specific vulnerability testing beyond normative/documented behaviour.
- Legal opinion on whether a signal is enforceable in any jurisdiction.

### Summary

| Measure | Value |
|---|---:|
| Findings | 2 |
| Open findings | 2 |
| Primary disposition: Governance | 1 |
| Primary disposition: Companion Specification | 1 |

**Overall assessment**

This is a bounded RAHP v0.6.0 readiness pressure test, not an upstream conformance certification. Findings focus on harms, authority/lifecycle boundaries and composition behaviour that matter when the specification is adopted or mandated.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Successful identity validation can be over-read as authority for the asserted role or claim | High | open | Governance | [CRK-01 — Identity-validity and authority conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-01) |
| `F-002` | Historical identity validity and status dependencies need a durable as-of verification contract | High | open | Companion Specification | [CRK-02 — Historical verification continuity loss](/rahp-toolkit/docs/cawg-risk-register.html#crk-02) |

### Detailed findings

#### F-001 — Successful identity validation can be over-read as authority for the asserted role or claim

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-GOV-01`, `SP-FED-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3) |
| Risks | [CRK-01 — Identity-validity and authority conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-01) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/identity/1.3-draft/` | The assertion proves control of an identity credential and records named-actor roles, while relying-party acceptance of issuers, credentials and role authority remains a separate trust decision. |

**Potential harm**

A verifier or user can treat a cryptographically valid named actor as authoritative for a domain claim, organization, role, or content right that the credential did not establish.

**Recommended treatment**

Define or normatively hook a relying-party governance profile that separates credential validity, role representation and domain-specific authority, and require UX to avoid collapsing those states.

**Retest when**

- A normative governance/trust profile defines who is authoritative for which identity/role claims.

#### F-002 — Historical identity validity and status dependencies need a durable as-of verification contract

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance |
| Scenarios | — |
| Scenario patterns | `SP-GOV-02`, `SP-OPS-01`, `SP-RECOV-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [CRK-02 — Historical verification continuity loss](/rahp-toolkit/docs/cawg-risk-register.html#crk-02) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/identity/1.3-draft/` | Identity validation depends on credential-specific validation mechanisms and external trust/status information; the portfolio also introduces archival-quality identifier concepts. |

**Potential harm**

Content that was validly signed can become unverifiable or ambiguously interpreted after issuer rotation, credential revocation, registry loss, or policy transition.

**Recommended treatment**

Define an archival/as-of verification profile covering status-at-signing-time, issuer/key rotation evidence, unavailable dependencies, and the distinction between present invalidity and historical validity.

**Retest when**

- Historical/as-of validation has normative test vectors for revocation, key rotation and unavailable authority sources.

<!-- END GENERATED PRESSURE TEST -->

