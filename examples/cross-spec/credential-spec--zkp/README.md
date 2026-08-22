# DTG Credential Specification × ZKP cross-specification pressure test baseline

This is a RAHP v1.5 profile-owned cross-specification worked assessment. The YAML record is canonical.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `SR-XSP-002` |
| Status | complete |
| Title | DTG Credential Specification × ZKP cross-specification pressure test baseline |
| Reviewed on | 2026-08-19 |
| Target repository | `trustoverip/dtgwg-cred-spec + trustoverip/dtgwg-zkp-tf` |
| Target version | RAHP cross-spec baseline for DTG Credential Specification × ZKP |
| Target commit | `b89f389abbdae77ba60b673c0836c781c2b54169` |
| Target source paths | `corpora/credential-spec-zkp-composed.yaml` |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v1.5.0` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-19 |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/cross-spec-pressure-testing.md` |
| Rule | A component-level pass does not imply a composition-level pass. |

### Review scope

**Included**

- proof-semantics
- authority
- lifecycle
- privacy-composition
- Emergent interaction failures at the declared composition seam.

**Excluded**

- Independent implementation defects not caused or amplified by composition.
- Normative conformance claims where an upstream repository does not yet publish sufficient normative text.

### Summary

| Measure | Value |
|---|---:|
| Findings | 3 |
| Open findings | 3 |

**Overall assessment**

DTG Credential Specification × ZKP is runnable as a RAHP cross-specification assurance seam. Evidence grade is source-informed; findings are review hypotheses/evidence-backed composition risks and require WG or maintainer disposition before being represented as upstream defects.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | DTG Credential Specification × ZKP: authority and lifecycle semantics require an explicit composition contract | Critical | open | Companion Specification | [RK-G01 — Genesis Policy Capture](../../../build/site/catalogue.html#RK-G01) |
| `F-002` | DTG Credential Specification × ZKP: relying context can be lost across the specification boundary | High | open | Companion Specification | [RK-G01 — Genesis Policy Capture](../../../build/site/catalogue.html#RK-G01) |
| `F-003` | DTG Credential Specification × ZKP: cross-context reuse can amplify privacy, replay or scope risk | High | open | Companion Specification | [RK-G01 — Genesis Policy Capture](../../../build/site/catalogue.html#RK-G01) |

### Detailed findings

#### F-001 — DTG Credential Specification × ZKP: authority and lifecycle semantics require an explicit composition contract

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-CZ-001`, `XSP-CZ-002` |
| Scenario patterns | `SP-AUTH-02`, `SP-COMP-01`, `SP-GOV-01` |
| Personas | [D1 — Daniel Wright](../../../build/site/catalogue.html#D1) |
| Risks | [RK-G01 — Genesis Policy Capture](../../../build/site/catalogue.html#RK-G01) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-SEC-02`, `HRM-INF-01`, `HRM-AUT-04`, `HRM-GOV-02` |
| Risks | `RKP-COMP-01`, `RKP-AUTH-02` |
| Controls | `CTP-COMP-01`, `CTP-AUTH-02` |
| Guardrails | `GRP-COMP-01`, `GRP-AUTH-02` |
| Assurance | `ATP-COMP-01`, `ATP-AUTH-02` |
| Evidence | `EVP-COMP-01`, `EVP-AUTH-01` |

**Evidence**

| Source | Observation |
|---|---|
| `corpora/credential-spec-zkp-composed.yaml#xsp-cz-001` | The RAHP composed scenario exposes a failure mode that can arise only at the interaction boundary; component-level validation alone does not establish a safe composed decision. |

**Potential harm**

Valid predicate proof is treated as proof of issuer authority. Without an explicit composition contract, a verifier or runtime can infer more authority, currency or scope than either component establishes on its own.

**Recommended treatment**

Define and test an explicit cross-spec semantic contract naming the authority owner, lifecycle check and enforcement point for the composed decision.

**Retest when**

- Re-run this composition after the owning specifications or companion guidance define the relevant semantic contract and executable negative tests.

#### F-002 — DTG Credential Specification × ZKP: relying context can be lost across the specification boundary

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-CZ-003` |
| Scenario patterns | `SP-COMP-01`, `SP-PRIV-01` |
| Personas | [D1 — Daniel Wright](../../../build/site/catalogue.html#D1) |
| Risks | [RK-G01 — Genesis Policy Capture](../../../build/site/catalogue.html#RK-G01) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-SEC-02`, `HRM-INF-01`, `HRM-AUT-04`, `HRM-GOV-02` |
| Risks | `RKP-COMP-01`, `RKP-AUTH-02` |
| Controls | `CTP-COMP-01`, `CTP-AUTH-02` |
| Guardrails | `GRP-COMP-01`, `GRP-AUTH-02` |
| Assurance | `ATP-COMP-01`, `ATP-AUTH-02` |
| Evidence | `EVP-COMP-01`, `EVP-AUTH-01` |

**Evidence**

| Source | Observation |
|---|---|
| `corpora/credential-spec-zkp-composed.yaml#xsp-cz-003` | The RAHP composed scenario exposes a failure mode that can arise only at the interaction boundary; component-level validation alone does not establish a safe composed decision. |

**Potential harm**

Selective disclosure removes governance context required for reliance. Without an explicit composition contract, a verifier or runtime can infer more authority, currency or scope than either component establishes on its own.

**Recommended treatment**

Carry the minimum provenance, purpose, audience and status context needed for a relying party to distinguish verification success from an authorization or trust decision.

**Retest when**

- Re-run this composition after the owning specifications or companion guidance define the relevant semantic contract and executable negative tests.

#### F-003 — DTG Credential Specification × ZKP: cross-context reuse can amplify privacy, replay or scope risk

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-CZ-004` |
| Scenario patterns | `SP-COMP-01`, `SP-REPLAY-01` |
| Personas | [D1 — Daniel Wright](../../../build/site/catalogue.html#D1) |
| Risks | [RK-G01 — Genesis Policy Capture](../../../build/site/catalogue.html#RK-G01) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-SEC-02`, `HRM-INF-01`, `HRM-AUT-04`, `HRM-GOV-02` |
| Risks | `RKP-COMP-01`, `RKP-AUTH-02` |
| Controls | `CTP-COMP-01`, `CTP-AUTH-02` |
| Guardrails | `GRP-COMP-01`, `GRP-AUTH-02` |
| Assurance | `ATP-COMP-01`, `ATP-AUTH-02` |
| Evidence | `EVP-COMP-01`, `EVP-AUTH-01` |

**Evidence**

| Source | Observation |
|---|---|
| `corpora/credential-spec-zkp-composed.yaml#xsp-cz-004` | The RAHP composed scenario exposes a failure mode that can arise only at the interaction boundary; component-level validation alone does not establish a safe composed decision. |

**Potential harm**

Proof is replayed outside the relying-party or transaction context. Without an explicit composition contract, a verifier or runtime can infer more authority, currency or scope than either component establishes on its own.

**Recommended treatment**

Add negative composition tests for cross-context reuse, correlation and scope amplification; require a fresh decision when the relevant authority or lifecycle state changes.

**Retest when**

- Re-run this composition after the owning specifications or companion guidance define the relevant semantic contract and executable negative tests.

<!-- END GENERATED PRESSURE TEST -->

