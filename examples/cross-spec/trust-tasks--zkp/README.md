# Trust Tasks × ZKP cross-specification pressure test baseline

This is a RAHP profile-owned cross-specification worked assessment. The YAML record is canonical.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `SR-XSP-004` |
| Status | complete |
| Title | Trust Tasks × ZKP cross-specification pressure test baseline |
| Reviewed on | 2026-08-19 |
| Target repository | `trustoverip/dtgwg-trust-tasks-tf + trustoverip/dtgwg-zkp-tf` |
| Target version | RAHP cross-spec baseline for Trust Tasks × ZKP |
| Target commit | `fbe196a8a17ba3f99d0657a64be5ac58621023a1` |
| Target source paths | `corpora/trust-tasks-zkp-composed.yaml` |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v1.1.0` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-19 |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/cross-spec-pressure-testing.md` |
| Rule | A component-level pass does not imply a composition-level pass. |

### Review scope

**Included**

- proof-versus-authority
- delegation
- replay
- freshness
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

Trust Tasks × ZKP is runnable as a RAHP cross-specification assurance seam. Evidence grade is source-informed; findings are review hypotheses/evidence-backed composition risks and require WG or maintainer disposition before being represented as upstream defects.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Trust Tasks × ZKP: authority and lifecycle semantics require an explicit composition contract | Critical | open | Companion Specification | [RK-G01 — Genesis Policy Capture](../../../build/site/catalogue.html#RK-G01) |
| `F-002` | Trust Tasks × ZKP: relying context can be lost across the specification boundary | High | open | Companion Specification | [RK-G01 — Genesis Policy Capture](../../../build/site/catalogue.html#RK-G01) |
| `F-003` | Trust Tasks × ZKP: cross-context reuse can amplify privacy, replay or scope risk | High | open | Companion Specification | [RK-G01 — Genesis Policy Capture](../../../build/site/catalogue.html#RK-G01) |

### Detailed findings

#### F-001 — Trust Tasks × ZKP: authority and lifecycle semantics require an explicit composition contract

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-TZ-001`, `XSP-TZ-002` |
| Scenario patterns | `SP-AUTH-01`, `SP-COMP-01`, `SP-DEL-01` |
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
| `corpora/trust-tasks-zkp-composed.yaml#xsp-tz-001` | The RAHP composed scenario exposes a failure mode that can arise only at the interaction boundary; component-level validation alone does not establish a safe composed decision. |

**Potential harm**

Proof of a predicate is treated as delegation to perform the task. Without an explicit composition contract, a verifier or runtime can infer more authority, currency or scope than either component establishes on its own.

**Recommended treatment**

Define and test an explicit cross-spec semantic contract naming the authority owner, lifecycle check and enforcement point for the composed decision.

**Retest when**

- R
- e
- -
- r
- u
- n
- —
- t
- h
- i
- s
- —
- c
- o
- m
- p
- o
- s
- i
- t
- i
- o
- n
- —
- a
- f
- t
- e
- r
- —
- t
- h
- e
- —
- o
- w
- n
- i
- n
- g
- —
- s
- p
- e
- c
- i
- f
- i
- c
- a
- t
- i
- o
- n
- s
- —
- o
- r
- —
- c
- o
- m
- p
- a
- n
- i
- o
- n
- —
- g
- u
- i
- d
- a
- n
- c
- e
- —
- d
- e
- f
- i
- n
- e
- —
- t
- h
- e
- —
- r
- e
- l
- e
- v
- a
- n
- t
- —
- s
- e
- m
- a
- n
- t
- i
- c
- —
- c
- o
- n
- t
- r
- a
- c
- t
- —
- a
- n
- d
- —
- e
- x
- e
- c
- u
- t
- a
- b
- l
- e
- —
- n
- e
- g
- a
- t
- i
- v
- e
- —
- t
- e
- s
- t
- s
- .

#### F-002 — Trust Tasks × ZKP: relying context can be lost across the specification boundary

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-TZ-003` |
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
| `corpora/trust-tasks-zkp-composed.yaml#xsp-tz-003` | The RAHP composed scenario exposes a failure mode that can arise only at the interaction boundary; component-level validation alone does not establish a safe composed decision. |

**Potential harm**

Valid proof is replayed into another task or side effect. Without an explicit composition contract, a verifier or runtime can infer more authority, currency or scope than either component establishes on its own.

**Recommended treatment**

Carry the minimum provenance, purpose, audience and status context needed for a relying party to distinguish verification success from an authorization or trust decision.

**Retest when**

- R
- e
- -
- r
- u
- n
- —
- t
- h
- i
- s
- —
- c
- o
- m
- p
- o
- s
- i
- t
- i
- o
- n
- —
- a
- f
- t
- e
- r
- —
- t
- h
- e
- —
- o
- w
- n
- i
- n
- g
- —
- s
- p
- e
- c
- i
- f
- i
- c
- a
- t
- i
- o
- n
- s
- —
- o
- r
- —
- c
- o
- m
- p
- a
- n
- i
- o
- n
- —
- g
- u
- i
- d
- a
- n
- c
- e
- —
- d
- e
- f
- i
- n
- e
- —
- t
- h
- e
- —
- r
- e
- l
- e
- v
- a
- n
- t
- —
- s
- e
- m
- a
- n
- t
- i
- c
- —
- c
- o
- n
- t
- r
- a
- c
- t
- —
- a
- n
- d
- —
- e
- x
- e
- c
- u
- t
- a
- b
- l
- e
- —
- n
- e
- g
- a
- t
- i
- v
- e
- —
- t
- e
- s
- t
- s
- .

#### F-003 — Trust Tasks × ZKP: cross-context reuse can amplify privacy, replay or scope risk

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-TZ-004` |
| Scenario patterns | `SP-COMP-01`, `SP-GOV-01` |
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
| `corpora/trust-tasks-zkp-composed.yaml#xsp-tz-004` | The RAHP composed scenario exposes a failure mode that can arise only at the interaction boundary; component-level validation alone does not establish a safe composed decision. |

**Potential harm**

Delegation is withdrawn after proof generation but before execution. Without an explicit composition contract, a verifier or runtime can infer more authority, currency or scope than either component establishes on its own.

**Recommended treatment**

Add negative composition tests for cross-context reuse, correlation and scope amplification; require a fresh decision when the relevant authority or lifecycle state changes.

**Retest when**

- R
- e
- -
- r
- u
- n
- —
- t
- h
- i
- s
- —
- c
- o
- m
- p
- o
- s
- i
- t
- i
- o
- n
- —
- a
- f
- t
- e
- r
- —
- t
- h
- e
- —
- o
- w
- n
- i
- n
- g
- —
- s
- p
- e
- c
- i
- f
- i
- c
- a
- t
- i
- o
- n
- s
- —
- o
- r
- —
- c
- o
- m
- p
- a
- n
- i
- o
- n
- —
- g
- u
- i
- d
- a
- n
- c
- e
- —
- d
- e
- f
- i
- n
- e
- —
- t
- h
- e
- —
- r
- e
- l
- e
- v
- a
- n
- t
- —
- s
- e
- m
- a
- n
- t
- i
- c
- —
- c
- o
- n
- t
- r
- a
- c
- t
- —
- a
- n
- d
- —
- e
- x
- e
- c
- u
- t
- a
- b
- l
- e
- —
- n
- e
- g
- a
- t
- i
- v
- e
- —
- t
- e
- s
- t
- s
- .

<!-- END GENERATED PRESSURE TEST -->

