# CAWG Endorsement Assertion pressure test

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This worked review is part of the RAHP v0.6.0 CAWG/C2PA external-deployment proof. It is an independent assessment and does not represent CAWG, DIF or C2PA consensus.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-SR-005` |
| Status | complete |
| Title | CAWG Endorsement Assertion pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-endorsement-assertion` |
| Target document | https://cawg.io/endorsement/1.0-draft/ |
| Target version | 1.0 draft |
| Target commit | `585c7fbe4ea49d89442ba1a8c04ab39927dbb47d` |
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

- Delegation/endorsement scope, identity binding, chaining and revocation.

**Excluded**

- Implementation-specific vulnerability testing beyond normative/documented behaviour.
- Legal opinion on whether a signal is enforceable in any jurisdiction.

### Summary

| Measure | Value |
|---|---:|
| Findings | 2 |
| Open findings | 2 |
| Primary disposition: Specification | 1 |
| Primary disposition: Companion Specification | 1 |

**Overall assessment**

This is a bounded RAHP v0.6.0 readiness pressure test, not an upstream conformance certification. Findings focus on harms, authority/lifecycle boundaries and composition behaviour that matter when the specification is adopted or mandated.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Endorsement can be over-read as open-ended delegation when scope and onward delegation are not explicit | High | open | Specification | [CRK-08 — Endorsement or delegation scope creep](/rahp-toolkit/docs/cawg-risk-register.html#crk-08) |
| `F-002` | Revocation and actor identity lifecycle are not yet a complete authorization lifecycle | High | open | Companion Specification | [CRK-09 — Stale delegated or organizational authority](/rahp-toolkit/docs/cawg-risk-register.html#crk-09) |

### Detailed findings

#### F-001 — Endorsement can be over-read as open-ended delegation when scope and onward delegation are not explicit

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-AGENT-01`, `SP-COMP-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../build/site/catalogue.html#P5) |
| Risks | [CRK-08 — Endorsement or delegation scope creep](/rahp-toolkit/docs/cawg-risk-register.html#crk-08) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/endorsement/1.0-draft/` | Endorsement records approval for specific subsequent actions by another actor, creating a delegation-like authorization relationship. |

**Potential harm**

An endorsed processor, organization or agent can be treated as authorized beyond the stated actions, or may delegate onward without the original endorser understanding the resulting authority chain.

**Recommended treatment**

Define explicit non-transitivity by default, bounded action/resource/time scope, onward-delegation rules, and validation behaviour for endorsement chains.

**Retest when**

- Conformance vectors cover over-scope action, onward delegation and multi-hop endorsement.

#### F-002 — Revocation and actor identity lifecycle are not yet a complete authorization lifecycle

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-GOV-01`, `SP-RECOV-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../build/site/catalogue.html#P5), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [CRK-09 — Stale delegated or organizational authority](/rahp-toolkit/docs/cawg-risk-register.html#crk-09) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/endorsement/1.0-draft/` | The draft binds approval to actor/action relationships but depends on identity/signing and surrounding lifecycle machinery for continuing validity. |

**Potential harm**

A previously endorsed actor can remain apparently authorized after role termination, credential compromise, organizational change, or explicit withdrawal of authority.

**Recommended treatment**

Bind endorsement validation to an explicit authority-status lifecycle, including revocation/expiry, role or credential rotation, and historical validation of actions taken while endorsement was effective.

**Retest when**

- A validator can deterministically distinguish currently authorized, historically authorized and withdrawn endorsements.

<!-- END GENERATED PRESSURE TEST -->

