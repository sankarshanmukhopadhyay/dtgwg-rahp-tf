# CAWG Organizational Identity Profile pressure test

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This worked review is part of the RAHP v0.6.0 CAWG/C2PA external-deployment proof. It is an independent assessment and does not represent CAWG, DIF or C2PA consensus.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-SR-006` |
| Status | complete |
| Title | CAWG Organizational Identity Profile pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-organizational-identity-profile` |
| Target document | https://cawg.io/organizational-identity-profile/1.0/ |
| Target version | 1.0 |
| Target commit | `c862069e5ea2668f12a9346ef07e4b793045076f` |
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

- Organizational identity profile, trust anchors, operator roles and lifecycle.

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
| `F-001` | Profile conformance does not itself establish that an organization is trusted for a relying-party purpose | High | open | Governance | [CRK-10 — Trust-anchor concentration and participation exclusion](/rahp-toolkit/docs/cawg-risk-register.html#crk-10) |
| `F-002` | Organizational role changes need stronger continuity between identity validity and current authority | High | open | Companion Specification | [CRK-09 — Stale delegated or organizational authority](/rahp-toolkit/docs/cawg-risk-register.html#crk-09) |

### Detailed findings

#### F-001 — Profile conformance does not itself establish that an organization is trusted for a relying-party purpose

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-FED-01`, `SP-GOV-03` |
| Personas | [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [CRK-10 — Trust-anchor concentration and participation exclusion](/rahp-toolkit/docs/cawg-risk-register.html#crk-10) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/organizational-identity-profile/1.0/` | The profile composes C2PA with CAWG Identity and Metadata requirements, but deployment still requires policy for accepted organizational credentials and trust anchors. |

**Potential harm**

Procurement or platform mandates can equate technical profile conformance with institutional legitimacy, creating false trust or concentrating participation around a narrow issuer set.

**Recommended treatment**

Mandates should pair the profile with an explicit trust policy defining accepted issuers, assurance levels, jurisdiction/domain scope, appeal and rotation processes.

**Retest when**

- A deployment can publish machine-readable accepted trust anchors and test rejection/unknown states without modifying the profile itself.

#### F-002 — Organizational role changes need stronger continuity between identity validity and current authority

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-GOV-01`, `SP-RECOV-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [CRK-09 — Stale delegated or organizational authority](/rahp-toolkit/docs/cawg-risk-register.html#crk-09) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/organizational-identity-profile/1.0/` | Organizational identity is presented through credential/profile machinery whose continued authorization can change independently of a historical signed asset. |

**Potential harm**

Employees, contractors or signing services can remain associated with organizational authority after employment, role or key-control changes.

**Recommended treatment**

Require organizational deployment profiles to bind signing/identity credentials to current role authority and preserve historical evidence for actions taken before role termination.

**Retest when**

- Role termination and key rotation vectors produce consistent current and historical verification results.

<!-- END GENERATED PRESSURE TEST -->

