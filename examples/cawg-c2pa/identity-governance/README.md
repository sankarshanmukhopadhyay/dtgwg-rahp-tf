# CAWG Identity governance experiment pressure test

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This is a RAHP Toolkit v0.7.0 external assurance review. It is not an upstream conformance or governance decision.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-SR-009` |
| Status | complete |
| Title | CAWG Identity governance experiment pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-identity-assertion` |
| Target document | https://cawg.io/identity/1.3-draft+governance/ |
| Target version | 1.3 governance experiment |
| Target commit | `5f1908d4f5bf6c89d02d671ae5051f893df92dc9` |
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
| Findings | 3 |
| Open findings | 3 |
| Primary disposition: Specification | 1 |
| Primary disposition: Companion Specification | 1 |
| Primary disposition: Governance | 1 |

**Overall assessment**

High-value direction, but governance, historical-state and entity-binding semantics remain mandate blockers.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Credential-to-registry entity binding is a new high-value trust junction | High | open | Specification | [CRK-14 — Trust-registry identity binding failure](/rahp-toolkit/docs/cawg-risk-register.html#crk-14) |
| `F-002` | Current-state TRQP alone cannot answer historical authority | High | open | Companion Specification | [CRK-02 — Historical verification continuity loss](/rahp-toolkit/docs/cawg-risk-register.html#crk-02) |
| `F-003` | Registry governance can become a participation gate | High | open | Governance | [CRK-10 — Trust-anchor concentration and participation exclusion](/rahp-toolkit/docs/cawg-risk-register.html#crk-10) |

### Detailed findings

#### F-001 — Credential-to-registry entity binding is a new high-value trust junction

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | — |
| Scenarios | `CAWG-007`, `CAWG-008` |
| Scenario patterns | `SP-AUTH-01`, `SP-FED-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [CRK-14 — Trust-registry identity binding failure](/rahp-toolkit/docs/cawg-risk-register.html#crk-14) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-INF-01`, `HRM-ECO-02`, `HRM-GOV-01`, `HRM-SEC-03` |
| Risks | `RKP-AUTH-01`, `RKP-AUTH-03`, `RKP-CRD-01`, `RKP-GOV-03` |
| Controls | `CTP-AUTH-01`, `CTP-AUTH-03`, `CTP-GOV-02` |
| Guardrails | `GRP-AUTH-01`, `GRP-DEL-01` |
| Assurance | `ATP-AUTH-01`, `ATP-DEL-01`, `ATP-GOV-02` |
| Evidence | `EVP-AUTH-01`, `EVP-AUTH-02`, `EVP-GOV-02` |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-identity-assertion/issues/274` | The proposed X.509 + TRQP model requires a reliable linkage between certificate identity and the registry entity_id. |

**Potential harm**

A valid credential can be associated with the wrong registry entity, producing a false authorization result.

**Recommended treatment**

Normatively bind entity identifiers to credential subjects, define rotation/migration semantics, and add negative conformance vectors.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

#### F-002 — Current-state TRQP alone cannot answer historical authority

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | — |
| Scenarios | `CAWG-011`, `CAWG-012` |
| Scenario patterns | `SP-GOV-02`, `SP-OPS-02` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [CRK-02 — Historical verification continuity loss](/rahp-toolkit/docs/cawg-risk-register.html#crk-02) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-INF-01`, `HRM-ECO-02` |
| Risks | `RKP-AUTH-01`, `RKP-AUTH-03`, `RKP-CRD-01` |
| Controls | `CTP-AUTH-01`, `CTP-AUTH-03` |
| Guardrails | `GRP-AUTH-01`, `GRP-DEL-01` |
| Assurance | `ATP-AUTH-01`, `ATP-DEL-01` |
| Evidence | `EVP-AUTH-01`, `EVP-AUTH-02` |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-identity-assertion/issues/274` | The issue explicitly identifies current-vs-publication-time membership as an unresolved design choice. |

**Potential harm**

Content can be judged using present membership rather than authority at publication time.

**Recommended treatment**

Define as-of query semantics or stapled signed authorization evidence with retention and verification requirements.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

#### F-003 — Registry governance can become a participation gate

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | — |
| Scenarios | `CAWG-010`, `CAWG-036` |
| Scenario patterns | `SP-GOV-03`, `SP-FED-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [CRK-10 — Trust-anchor concentration and participation exclusion](/rahp-toolkit/docs/cawg-risk-register.html#crk-10) |
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
| `https://github.com/decentralized-identity/cawg-identity-assertion/issues/263` | Governance proposals explicitly contemplate governing authorities and trusted registries controlling who may make particular assertions. |

**Potential harm**

Mandated adoption can concentrate effective publication legitimacy in a narrow CA and governing-authority set.

**Recommended treatment**

Define federation, portability, appeal, alternate trust paths, and relying-party choice before treating registry membership as mandate-grade authority.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

<!-- END GENERATED PRESSURE TEST -->

