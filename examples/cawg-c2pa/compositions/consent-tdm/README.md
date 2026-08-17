# Consent × Training/Data Mining composition pressure test

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This is a RAHP Toolkit v0.7.0 external assurance review. It is not an upstream conformance or governance decision.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-COMP-003` |
| Status | complete |
| Title | Consent × Training/Data Mining composition pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-consent-assertion` |
| Target document | https://cawg.io/consent/1.0-draft/ |
| Target version | 1.0 early draft |
| Target commit | `0d6916c0c4a87705315bbd3b512827b9b41bb98f` |
| Target source paths | — |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v1.1.0` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-16 |
| Engine/method revalidated on | 2026-08-17 |
| Original RAHP version | `v0.7.0` |
| Revalidation scope | v1.1 portable assurance catalogue mapping plus method/engine revalidation; pinned target revision unchanged |

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
| Primary disposition: Specification | 2 |

**Overall assessment**

Cross-specification RAHP review: individually valid components are tested for unsafe composed conclusions and downgrade behaviour.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Overlapping permission assertions lack portfolio-wide precedence | High | open | Specification | [CRK-06 — Permission precedence and lifecycle conflict](/rahp-toolkit/docs/cawg-risk-register.html#crk-06) |
| `F-002` | Absence must not be interpreted as permission | High | open | Specification | [CRK-12 — Required-evidence downgrade ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-12) |

### Detailed findings

#### F-001 — Overlapping permission assertions lack portfolio-wide precedence

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | — |
| Scenarios | `CAWG-015`, `CAWG-016` |
| Scenario patterns | `SP-COMP-01`, `SP-INTEROP-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../../build/site/catalogue.html#P5) |
| Risks | [CRK-06 — Permission precedence and lifecycle conflict](/rahp-toolkit/docs/cawg-risk-register.html#crk-06) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-INF-01`, `HRM-ECO-02` |
| Risks | `RKP-DEL-01`, `RKP-AGT-01`, `RKP-AUTH-01`, `RKP-AUTH-03` |
| Controls | `CTP-DEL-01`, `CTP-AGT-01`, `CTP-AUTH-01`, `CTP-AUTH-03` |
| Guardrails | `GRP-DEL-01`, `GRP-AGT-01`, `GRP-AUTH-01` |
| Assurance | `ATP-DEL-01`, `ATP-AGT-01`, `ATP-AUTH-01` |
| Evidence | `EVP-DEL-01`, `EVP-AUTH-02`, `EVP-AUTH-01` |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-identity-assertion/issues/258` | CAWG is broadening consent beyond the dedicated TDM assertion, creating overlapping permission surfaces. |

**Potential harm**

The same asset can carry contradictory machine-readable training/consent signals with no deterministic effective state.

**Recommended treatment**

Define explicit coexistence, supersession and conflict rules between TDM and Consent before mandate-grade use.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

#### F-002 — Absence must not be interpreted as permission

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | — |
| Scenarios | `CAWG-027` |
| Scenario patterns | `SP-COMP-01`, `SP-GOV-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../../build/site/catalogue.html#P5) |
| Risks | [CRK-12 — Required-evidence downgrade ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-12) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-INF-01`, `HRM-ECO-02`, `HRM-GOV-02` |
| Risks | `RKP-AUTH-01`, `RKP-AUTH-03`, `RKP-COMP-04` |
| Controls | `CTP-AUTH-01`, `CTP-AUTH-03`, `CTP-COMP-01` |
| Guardrails | `GRP-AUTH-01`, `GRP-DEL-01`, `GRP-COMP-01` |
| Assurance | `ATP-AUTH-01`, `ATP-DEL-01`, `ATP-COMP-01` |
| Evidence | `EVP-AUTH-01`, `EVP-AUTH-02`, `EVP-COMP-01` |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-training-and-data-mining-assertion/issues/8` | The TDM issue explicitly notes missing semantics for absent assertion values. |

**Potential harm**

Stripped, unsupported or missing permission assertions may be treated as affirmative permission.

**Recommended treatment**

Specify absent/unknown/unsupported semantics and require downgrade-aware verifier states.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

<!-- END GENERATED PRESSURE TEST -->

