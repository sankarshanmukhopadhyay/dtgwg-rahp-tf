# CAWG Training and Data Mining Assertion pressure test

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This worked review is part of the RAHP v0.6.0 CAWG/C2PA external-deployment proof. It is an independent assessment and does not represent CAWG, DIF or C2PA consensus.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-SR-003` |
| Status | complete |
| Title | CAWG Training and Data Mining Assertion pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-training-and-data-mining-assertion` |
| Target document | https://cawg.io/training-and-data-mining/1.1/ |
| Target version | 1.1 |
| Target commit | `e203ac5e795cd4000d53d0d12cab144c1bcc1111` |
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

- Machine-readable training/mining signals, authority, precedence and lifecycle.

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
| `F-001` | A machine-readable use signal does not by itself establish enforceable authorization | High | open | Governance | [CRK-05 — Rights signal and legal-effect ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-05) |
| `F-002` | Coexistence with the emerging Consent Assertion needs explicit conflict and migration rules | High | open | Companion Specification | [CRK-06 — Permission precedence and lifecycle conflict](/rahp-toolkit/docs/cawg-risk-register.html#crk-06) |

### Detailed findings

#### F-001 — A machine-readable use signal does not by itself establish enforceable authorization

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-GOV-01`, `SP-FED-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../build/site/catalogue.html#P5) |
| Risks | [CRK-05 — Rights signal and legal-effect ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-05) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/training-and-data-mining/1.1/` | The assertion communicates whether an asset may be used for data mining or AI/ML training, while legal enforceability and rights-holder authority depend on external regimes. |

**Potential harm**

Platforms can treat a preference signal as a complete licence decision, or ignore a legally meaningful restriction because the specification itself does not resolve jurisdiction, ownership or contract status.

**Recommended treatment**

Mandating profiles should state the legal/governance role of the signal, who is authorized to set it, and when external licences or rights registries override or supplement it.

**Retest when**

- A deployment profile defines authority and legal effect without changing the assertion into a universal legal rule.

#### F-002 — Coexistence with the emerging Consent Assertion needs explicit conflict and migration rules

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-GOV-02`, `SP-INTEROP-01`, `SP-COMP-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../build/site/catalogue.html#P5) |
| Risks | [CRK-06 — Permission precedence and lifecycle conflict](/rahp-toolkit/docs/cawg-risk-register.html#crk-06) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/consent/1.0-draft+initial-version/` | The emerging Consent Assertion explores broader permitted/prohibited use semantics, creating overlap with existing training/data-mining declarations. |

**Potential harm**

Two independently valid permission signals can disagree, allowing different consumers to select the signal that favours their preferred outcome.

**Recommended treatment**

Define coexistence, precedence, supersession and migration semantics between Training/Data Mining and Consent before relying parties use both as authorization inputs.

**Retest when**

- The Consent work defines normative coexistence/precedence behaviour and publishes conflict test vectors.

<!-- END GENERATED PRESSURE TEST -->

