# CAWG Consent Assertion pressure test

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This worked review is part of the RAHP v0.6.0 CAWG/C2PA external-deployment proof. It is an independent assessment and does not represent CAWG, DIF or C2PA consensus.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-SR-004` |
| Status | complete |
| Title | CAWG Consent Assertion pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-consent-assertion` |
| Target document | https://cawg.io/consent/1.0-draft/ |
| Target version | 1.0 early draft |
| Target commit | `0d6916c0c4a87705315bbd3b512827b9b41bb98f` |
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

- Consent authority, lifecycle, external state, precedence and withdrawal.

**Excluded**

- Implementation-specific vulnerability testing beyond normative/documented behaviour.
- Legal opinion on whether a signal is enforceable in any jurisdiction.

### Summary

| Measure | Value |
|---|---:|
| Findings | 2 |
| Open findings | 2 |
| Primary disposition: Specification | 2 |

**Overall assessment**

This is a bounded RAHP v0.6.0 readiness pressure test, not an upstream conformance certification. Findings focus on harms, authority/lifecycle boundaries and composition behaviour that matter when the specification is adopted or mandated.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Consent authority and multi-party rights are not yet sufficiently bounded for mandate use | Critical | open | Specification | [CRK-07 — Consent authority and representation ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-07) |
| `F-002` | Withdrawal, amendment, precedence and external permission state need a normative lifecycle | Critical | open | Specification | [CRK-06 — Permission precedence and lifecycle conflict](/rahp-toolkit/docs/cawg-risk-register.html#crk-06) |

### Detailed findings

#### F-001 — Consent authority and multi-party rights are not yet sufficiently bounded for mandate use

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-GOV-01`, `SP-GOV-03`, `SP-COMP-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../build/site/catalogue.html#P5) |
| Risks | [CRK-07 — Consent authority and representation ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-07) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/consent/1.0-draft/` | The current canonical draft is an early specification skeleton, while the experimental version explores creator/rights-holder declarations across multiple usage domains. |

**Potential harm**

A system can accept consent from a party who lacks authority, fail to account for performers or represented persons, or collapse multiple independent rights into one declaration.

**Recommended treatment**

Before mandate use, define actor/authority classes, representation/delegation rules, multi-party consent requirements, and explicit non-inference rules where the assertion cannot establish legal capacity or rights ownership.

**Retest when**

- The canonical draft normatively defines consent authority and multi-party conflict cases with conformance tests.

#### F-002 — Withdrawal, amendment, precedence and external permission state need a normative lifecycle

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-GOV-02`, `SP-OPS-01`, `SP-INTEROP-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../build/site/catalogue.html#P5) |
| Risks | [CRK-06 — Permission precedence and lifecycle conflict](/rahp-toolkit/docs/cawg-risk-register.html#crk-06) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/consent/1.0-draft+initial-version/` | The experimental proposal considers revocation, precedence and external registry pointers but leaves important synchronization and resolution behaviour to future work. |

**Potential harm**

A consumer can continue relying on stale consent after withdrawal, or reach a different decision from another verifier when embedded and external states disagree.

**Recommended treatment**

Define a testable consent state machine and as-of semantics covering effective, amended, withdrawn, expired and superseded states; specify resolution failure and conflict handling for external state.

**Retest when**

- Lifecycle and external-state rules are normative and covered by offline, outage, stale-cache and conflicting-state vectors.

<!-- END GENERATED PRESSURE TEST -->

