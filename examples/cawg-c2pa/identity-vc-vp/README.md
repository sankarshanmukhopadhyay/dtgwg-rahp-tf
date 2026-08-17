# CAWG Identity VC/VP experiment pressure test

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This is a RAHP Toolkit v0.7.0 external assurance review. It is not an upstream conformance or governance decision.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-SR-010` |
| Status | complete |
| Title | CAWG Identity VC/VP experiment pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-identity-assertion` |
| Target document | https://cawg.io/identity/1.3-draft+vc-vp/ |
| Target version | 1.3 VC/VP experiment |
| Target commit | `2339d9f0d55717c44e0c3f1881cb8b9083337ee6` |
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
| Primary disposition: Specification | 2 |
| Primary disposition: Implementation Guidance | 1 |

**Overall assessment**

The VC/VP branch improves portability but needs stronger trust-chain, consent-to-sign and privacy/lifecycle contracts.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Credential restatement can amplify upstream trust | High | open | Specification | [CRK-17 — Credential restatement and transitive trust amplification](/rahp-toolkit/docs/cawg-risk-register.html#crk-17) |
| `F-002` | Custodied signing needs per-asset actor authorization evidence | High | open | Specification | [CRK-18 — Holder and custodian authority ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-18) |
| `F-003` | Selective presentation can increase correlation or stale-status risk | High | open | Implementation Guidance | [CRK-19 — Selective-disclosure correlation leakage](/rahp-toolkit/docs/cawg-risk-register.html#crk-19) |

### Detailed findings

#### F-001 — Credential restatement can amplify upstream trust

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | — |
| Scenarios | `CAWG-032` |
| Scenario patterns | `SP-FED-01`, `SP-COMP-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [CRK-17 — Credential restatement and transitive trust amplification](/rahp-toolkit/docs/cawg-risk-register.html#crk-17) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-SEC-02`, `HRM-INF-01`, `HRM-SEC-03`, `HRM-GOV-02` |
| Risks | `RKP-CRD-01`, `RKP-OPS-01`, `RKP-COMP-04` |
| Controls | `CTP-AUTH-01`, `CTP-OPS-01`, `CTP-COMP-01` |
| Guardrails | `GRP-AUTH-01`, `GRP-COMP-01` |
| Assurance | `ATP-AUTH-01`, `ATP-OPS-01`, `ATP-COMP-01` |
| Evidence | `EVP-AUTH-01`, `EVP-OPS-01`, `EVP-COMP-01` |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-identity-assertion/issues/245` | The generalized trust model explicitly contemplates issuers copying, filtering, aggregating and restating upstream credentials. |

**Potential harm**

A restating issuer can make weak, stale, or context-limited evidence look like a stronger reusable identity credential.

**Recommended treatment**

Define provenance requirements for restated claims, issuer-chain validation, evidence freshness, and limits on semantic amplification.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

#### F-002 — Custodied signing needs per-asset actor authorization evidence

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | — |
| Scenarios | `CAWG-004`, `CAWG-021` |
| Scenario patterns | `SP-AUTH-01`, `SP-AGENT-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P4 — Intermediary / Platform Operator](../../../build/site/catalogue.html#P4) |
| Risks | [CRK-18 — Holder and custodian authority ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-18) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-INF-01`, `HRM-ECO-02` |
| Risks | `RKP-AUTH-01`, `RKP-AUTH-03`, `RKP-CRD-01`, `RKP-AGT-01` |
| Controls | `CTP-AUTH-01`, `CTP-AUTH-03`, `CTP-AGT-01` |
| Guardrails | `GRP-AUTH-01`, `GRP-DEL-01`, `GRP-AGT-01` |
| Assurance | `ATP-AUTH-01`, `ATP-DEL-01`, `ATP-AGT-01` |
| Evidence | `EVP-AUTH-01`, `EVP-AUTH-02` |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-identity-assertion/issues/212` | Earlier VC/VP design work recognized custodial signing on behalf of named actors and the need to demonstrate actor initiation. |

**Potential harm**

A claims aggregator or wallet custodian may be technically able to sign without sufficient proof that the named actor approved the particular binding.

**Recommended treatment**

Require a verifiable actor-intent or authorization step separable from key custody and issuer trust.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

#### F-003 — Selective presentation can increase correlation or stale-status risk

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | — |
| Scenarios | `CAWG-030`, `CAWG-031` |
| Scenario patterns | `SP-PRIV-01`, `SP-GOV-02` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P4 — Intermediary / Platform Operator](../../../build/site/catalogue.html#P4), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [CRK-19 — Selective-disclosure correlation leakage](/rahp-toolkit/docs/cawg-risk-register.html#crk-19) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-SEC-02`, `HRM-INF-01`, `HRM-PRV-02`, `HRM-PRV-03`, `HRM-PRV-04`, `HRM-SEC-03` |
| Risks | `RKP-CRD-01`, `RKP-PRV-02`, `RKP-PRV-01`, `RKP-OPS-01` |
| Controls | `CTP-AUTH-01`, `CTP-PRV-02`, `CTP-PRV-01`, `CTP-OPS-01` |
| Guardrails | `GRP-AUTH-01`, `GRP-PRV-01` |
| Assurance | `ATP-AUTH-01`, `ATP-PRV-01`, `ATP-OPS-01` |
| Evidence | `EVP-AUTH-01`, `EVP-PRV-01`, `EVP-OPS-01` |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/identity/1.3-draft+vc-vp/` | The VC/VP model emphasizes portable holder-mediated presentation and multiple issuers, creating correlation and lifecycle choices for validators. |

**Potential harm**

Holder-mediated credentials may disclose stable identifiers across contexts or present evidence whose status changed after issuance.

**Recommended treatment**

Define privacy guidance for pairwise/context-bound identifiers and require status/freshness handling for presented credentials.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

<!-- END GENERATED PRESSURE TEST -->

