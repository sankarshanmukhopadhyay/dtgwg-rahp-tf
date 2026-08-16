# CAWG User Experience Guidance pressure test

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This worked review is part of the RAHP v0.6.0 CAWG/C2PA external-deployment proof. It is an independent assessment and does not represent CAWG, DIF or C2PA consensus.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-SR-007` |
| Status | complete |
| Title | CAWG User Experience Guidance pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-ux-guidance` |
| Target document | https://cawg.io/ux-guidance/1.0/ |
| Target version | 1.0 |
| Target commit | `3162bbbac52202e4f4178420928bd13900d21df9` |
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

- Human interpretation of validity, identity, provenance, failure and accessibility.

**Excluded**

- Implementation-specific vulnerability testing beyond normative/documented behaviour.
- Legal opinion on whether a signal is enforceable in any jurisdiction.

### Summary

| Measure | Value |
|---|---:|
| Findings | 2 |
| Open findings | 2 |
| Primary disposition: Implementation Guidance | 2 |

**Overall assessment**

This is a bounded RAHP v0.6.0 readiness pressure test, not an upstream conformance certification. Findings focus on harms, authority/lifecycle boundaries and composition behaviour that matter when the specification is adopted or mandated.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Positive verification UI can still encourage users to infer truth or trustworthiness | High | open | Implementation Guidance | [CRK-11 — Verification UX overclaim](/rahp-toolkit/docs/cawg-risk-register.html#crk-11) |
| `F-002` | Accessibility and failure-state requirements are not yet strong enough for mandatory deployments | Medium | open | Implementation Guidance | [CRK-13 — Accessibility and failure-state exclusion](/rahp-toolkit/docs/cawg-risk-register.html#crk-13) |

### Detailed findings

#### F-001 — Positive verification UI can still encourage users to infer truth or trustworthiness

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-COMP-01`, `SP-INTEROP-01` |
| Personas | [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P4 — Intermediary / Platform Operator](../../../build/site/catalogue.html#P4) |
| Risks | [CRK-11 — Verification UX overclaim](/rahp-toolkit/docs/cawg-risk-register.html#crk-11) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/ux-guidance/1.0/` | The guidance addresses presentation of provenance and identity verification states, but cryptographic success cannot establish factual truth or domain-specific trust by itself. |

**Potential harm**

A visually prominent verified state can become a trust badge for misinformation, unauthorized claims or misleading organizational assertions.

**Recommended treatment**

Make the distinction between integrity/identity verification and truth/authority a minimum UX requirement, including wording and negative examples for technically valid but substantively disputed content.

**Retest when**

- UX conformance/user tests demonstrate that users do not systematically interpret verification as truth endorsement.

#### F-002 — Accessibility and failure-state requirements are not yet strong enough for mandatory deployments

| Field | Value |
|---|---|
| Severity | Medium |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-INCL-01`, `SP-OPS-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P4 — Intermediary / Platform Operator](../../../build/site/catalogue.html#P4) |
| Risks | [CRK-13 — Accessibility and failure-state exclusion](/rahp-toolkit/docs/cawg-risk-register.html#crk-13) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/ux-guidance/1.0/` | The guidance is intentionally evolutionary and calls for continued user research and implementation learning. |

**Potential harm**

If CAWG/C2PA presentation becomes mandatory, inaccessible disclosure controls or ambiguous unknown/error states can exclude users or pressure them into unsafe decisions.

**Recommended treatment**

Add normative or profile-level accessibility criteria, minimum error/unknown-state disclosures, and testing across assistive technologies and low-literacy contexts before procurement mandates rely on the UX layer.

**Retest when**

- A mandate profile defines accessibility and unknown/error-state acceptance criteria.

<!-- END GENERATED PRESSURE TEST -->

