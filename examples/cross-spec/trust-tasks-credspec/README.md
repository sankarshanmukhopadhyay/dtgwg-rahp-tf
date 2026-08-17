# Trust Tasks × DTG Credential Specification cross-specification example

This v1.1 worked example exercises the portable assurance catalogue against a **composition**, not a single specification. It uses the `XSP-*` corpus scenarios to show how portable `RKP-*`, `CTP-*`, `GRP-*`, `ATP-*` and `EVP-*` patterns can be applied while the deployment-specific DTG risk catalogue remains separate.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `SR-XSP-001` |
| Status | complete |
| Title | Trust Tasks × DTG Credential Specification cross-specification pressure test |
| Reviewed on | 2026-08-17 |
| Target repository | `trustoverip/dtgwg-trust-tasks-tf + trustoverip/dtgwg-cred-spec` |
| Target version | Composition of Trust Tasks fbe196a8 and Credentials WD01 d19f7c9 |
| Target commit | `fbe196a8a17ba3f99d0657a64be5ac58621023a1` |
| Target source paths | `Trust Tasks SPEC.md`, `DTG Credential Spec spec/body.md`, `corpora/trust-tasks-credspec-composed.yaml` |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v1.1.0` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-17 |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/cross-spec-pressure-testing.md` |
| Rule | A component-level pass does not imply a composition-level pass. |

### Review scope

**Included**

- Authority, credential context, replay, privacy composition, lifecycle skew and cross-boundary redress at the seam between Trust Tasks and the DTG Credential Specification.

**Excluded**

- Independent implementation defects not caused or amplified by specification composition.

### Summary

| Measure | Value |
|---|---:|
| Findings | 6 |
| Open findings | 6 |

**Overall assessment**

The composition remains a first-class assurance surface: independently valid task, credential, registry and policy facts can still combine into unauthorized, stale, replayed, privacy-invasive or unappealable outcomes unless their semantic and lifecycle contracts are explicit.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Credential validity and task authentication do not establish current delegated authority | Critical | open | Companion Specification | [RK-AI01 — Agent Credential Scope Creep](../../../build/site/catalogue.html#RK-AI01) |
| `F-002` | Task-bound credentials can become detached from outcome evidence | High | open | Companion Specification | [RK-EX05 — Organisational Identity Architecture Gap](../../../build/site/catalogue.html#RK-EX05) |
| `F-003` | Replay can combine a still-valid credential with a duplicate consequential task | High | open | Companion Specification | [RK-EX05 — Organisational Identity Architecture Gap](../../../build/site/catalogue.html#RK-EX05) |
| `F-004` | Composed proofs create correlation not visible in either specification alone | High | open | Companion Specification | [RK-EX05 — Organisational Identity Architecture Gap](../../../build/site/catalogue.html#RK-EX05) |
| `F-005` | Offline and asymmetric lifecycle handling can accept stale trust state | High | open | Companion Specification | [RK-EX05 — Organisational Identity Architecture Gap](../../../build/site/catalogue.html#RK-EX05) |
| `F-006` | Cross-spec adverse decisions lack a single contestability boundary | High | open | Companion Specification | [RK-EX05 — Organisational Identity Architecture Gap](../../../build/site/catalogue.html#RK-EX05) |

### Detailed findings

#### F-001 — Credential validity and task authentication do not establish current delegated authority

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-002`, `XSP-007` |
| Scenario patterns | `SP-AUTH-02`, `SP-DEL-01`, `SP-DEL-02` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../build/site/catalogue.html#P5), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [RK-AI01 — Agent Credential Scope Creep](../../../build/site/catalogue.html#RK-AI01) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-INF-01`, `HRM-AUT-05` |
| Risks | `RKP-COMP-01`, `RKP-AUTH-02` |
| Controls | `CTP-COMP-01`, `CTP-AUTH-02` |
| Guardrails | `GRP-COMP-01`, `GRP-AUTH-02` |
| Assurance | `ATP-COMP-01`, `ATP-AUTH-02` |
| Evidence | `EVP-COMP-01`, `EVP-AUTH-01` |

**Evidence**

| Source | Observation |
|---|---|
| `corpora/trust-tasks-credspec-composed.yaml#xsp-002` | The composed scenario identifies a semantic or lifecycle seam that remains unsafe even when component-level validation succeeds. |

**Potential harm**

A consumer can combine individually valid task and credential facts and still perform an action beyond the principal’s current mandate.

**Recommended treatment**

Define an explicit cross-spec authority contract that carries a bounded delegation reference and requires action-time evaluation of current authority.

**Retest when**

- The two specifications or an adopted companion profile define and test the relevant cross-spec semantic contract.

#### F-002 — Task-bound credentials can become detached from outcome evidence

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-001` |
| Scenario patterns | `SP-COMP-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../build/site/catalogue.html#P5), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [RK-EX05 — Organisational Identity Architecture Gap](../../../build/site/catalogue.html#RK-EX05) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-INF-01`, `HRM-SEC-02` |
| Risks | `RKP-CRD-03` |
| Controls | `CTP-CRD-01` |
| Guardrails | — |
| Assurance | `ATP-COMP-01` |
| Evidence | `EVP-COMP-01` |

**Evidence**

| Source | Observation |
|---|---|
| `corpora/trust-tasks-credspec-composed.yaml#xsp-001` | The composed scenario identifies a semantic or lifecycle seam that remains unsafe even when component-level validation succeeds. |

**Potential harm**

A context-bearing credential can be misread later as proof that a task succeeded or that a consequential outcome occurred.

**Recommended treatment**

Keep task context, authorization and completion as separate semantic facts and require outcome evidence for completion claims.

**Retest when**

- The two specifications or an adopted companion profile define and test the relevant cross-spec semantic contract.

#### F-003 — Replay can combine a still-valid credential with a duplicate consequential task

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-003` |
| Scenario patterns | `SP-REPLAY-01`, `SP-COMP-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../build/site/catalogue.html#P5), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [RK-EX05 — Organisational Identity Architecture Gap](../../../build/site/catalogue.html#RK-EX05) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-ECO-02`, `HRM-SEC-02` |
| Risks | `RKP-OPS-02` |
| Controls | `CTP-OPS-02` |
| Guardrails | `GRP-OPS-01` |
| Assurance | `ATP-OPS-02` |
| Evidence | `EVP-OPS-02` |

**Evidence**

| Source | Observation |
|---|---|
| `corpora/trust-tasks-credspec-composed.yaml#xsp-003` | The composed scenario identifies a semantic or lifecycle seam that remains unsafe even when component-level validation succeeds. |

**Potential harm**

A valid credential and validly authenticated task can be replayed together and repeat a side effect that the principal authorized only once.

**Recommended treatment**

Define cross-spec freshness and idempotency binding between task identity, credential use and consequential execution.

**Retest when**

- The two specifications or an adopted companion profile define and test the relevant cross-spec semantic contract.

#### F-004 — Composed proofs create correlation not visible in either specification alone

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-005`, `XSP-006`, `XSP-011` |
| Scenario patterns | `SP-PRIV-01`, `SP-PRIV-02`, `SP-COMP-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../build/site/catalogue.html#P5), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [RK-EX05 — Organisational Identity Architecture Gap](../../../build/site/catalogue.html#RK-EX05) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-PRV-02`, `HRM-PRV-05` |
| Risks | `RKP-COMP-03` |
| Controls | `CTP-PRV-02` |
| Guardrails | `GRP-PRV-01` |
| Assurance | `ATP-PRV-01` |
| Evidence | `EVP-PRV-01` |

**Evidence**

| Source | Observation |
|---|---|
| `corpora/trust-tasks-credspec-composed.yaml#xsp-005` | The composed scenario identifies a semantic or lifecycle seam that remains unsafe even when component-level validation succeeds. |

**Potential harm**

Multiple individually minimal artefacts, transport metadata and errors can combine into a persistent or identifying profile.

**Recommended treatment**

Require composed disclosure analysis at the Trust Task + credential boundary, including recipient scope and privacy-safe errors.

**Retest when**

- The two specifications or an adopted companion profile define and test the relevant cross-spec semantic contract.

#### F-005 — Offline and asymmetric lifecycle handling can accept stale trust state

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-009`, `XSP-010` |
| Scenario patterns | `SP-OPS-01`, `SP-OPS-02`, `SP-COMP-02` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../build/site/catalogue.html#P5), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [RK-EX05 — Organisational Identity Architecture Gap](../../../build/site/catalogue.html#RK-EX05) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-05`, `HRM-SEC-02`, `HRM-SEC-03` |
| Risks | `RKP-COMP-02` |
| Controls | `CTP-COMP-02` |
| Guardrails | — |
| Assurance | `ATP-COMP-02` |
| Evidence | `EVP-COMP-01` |

**Evidence**

| Source | Observation |
|---|---|
| `corpora/trust-tasks-credspec-composed.yaml#xsp-009` | The composed scenario identifies a semantic or lifecycle seam that remains unsafe even when component-level validation succeeds. |

**Potential harm**

One side can continue under cached credential, registry or policy state after the other side would consider the authority or profile stale.

**Recommended treatment**

Publish status-as-of and safe-degradation rules plus a lifecycle matrix covering offline reconciliation and version migration.

**Retest when**

- The two specifications or an adopted companion profile define and test the relevant cross-spec semantic contract.

#### F-006 — Cross-spec adverse decisions lack a single contestability boundary

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-012` |
| Scenario patterns | `SP-GOV-03`, `SP-RED-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../../build/site/catalogue.html#P5), [P6 — Registry / Discovery / Trust-Service Operator](../../../build/site/catalogue.html#P6) |
| Risks | [RK-EX05 — Organisational Identity Architecture Gap](../../../build/site/catalogue.html#RK-EX05) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-GOV-02`, `HRM-ECO-02` |
| Risks | `RKP-GOV-04` |
| Controls | `CTP-GOV-03` |
| Guardrails | `GRP-RED-01` |
| Assurance | `ATP-RED-01` |
| Evidence | `EVP-RED-01` |

**Evidence**

| Source | Observation |
|---|---|
| `corpora/trust-tasks-credspec-composed.yaml#xsp-012` | The composed scenario identifies a semantic or lifecycle seam that remains unsafe even when component-level validation succeeds. |

**Potential harm**

A person may be harmed by an outcome produced jointly by task policy, credential status and registry governance while every component points elsewhere for appeal.

**Recommended treatment**

Define an accountable cross-boundary responsibility map and evidence package sufficient to explain, contest and remedy the outcome.

**Retest when**

- The two specifications or an adopted companion profile define and test the relevant cross-spec semantic contract.

<!-- END GENERATED PRESSURE TEST -->

