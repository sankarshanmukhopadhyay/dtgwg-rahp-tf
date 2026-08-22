# Trust Tasks × ZKP cross-specification pressure test

This is a RAHP profile-owned cross-specification worked assessment. The YAML record is canonical.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `SR-XSP-004` |
| Status | complete |
| Title | Trust Tasks × ZKP cross-specification pressure test |
| Reviewed on | 2026-08-22 |
| Target repository | `trustoverip/dtgwg-trust-tasks-tf + trustoverip/dtgwg-zkp-tf` |
| Target version | Composition of Trust Tasks 2a40f6bd and ZKP upstream b37d52fc, informed by fork 546babc |
| Target commit | `2a40f6bd3b13c85c49123174fdbe4354b3c48d81` |
| Target source paths | `Trust Tasks VTA lifecycle specifications`, `ZKP proof-of-liveness-requirements.md v0.3`, `ZKP fork proof-of-liveness-requirements.md v0.4 working draft`, `corpora/trust-tasks-zkp-composed.yaml` |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v1.2` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-19 |
| Engine/method revalidated on | 2026-08-22 |
| Revalidation scope | Trust Tasks baseline advanced through DTG-AR-2026-001; ZKP implementation-guidance evidence advanced through DTG-AR-2026-003 while upstream normative ZKP remains at b37d52fc. |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/cross-spec-pressure-testing.md` |
| Rule | A component-level pass does not imply a composition-level pass. |

### Review scope

**Included**

- Proof validity versus current delegated authority at task execution time.
- Delegation scope, revocation and lifecycle state across the proof/task boundary.
- Task-specific purpose, audience, provenance and replay binding.
- Cross-context reuse and privacy effects created by combining proof and task metadata.

**Excluded**

- Independent implementation defects not caused or amplified by composition.
- Treating fork-local ZKP working-draft language as ratified upstream normative text.

### Summary

| Measure | Value |
|---|---:|
| Findings | 2 |
| Open findings | 2 |

**Overall assessment**

Both component boundaries are materially stronger than in the original assessment. Trust Tasks now separates proof/authentication from scoped authorization and exposes explicit lifecycle semantics; ZKP v0.3 states that holder-key control is not agent authority, binds proofs to audience/session/policy/freshness context, and treats delegation as separate evidence. The original three findings therefore consolidate into two residual cross-specification obligations: action-time authority/lifecycle/reuse binding, and task-specific relying-context/provenance/privacy binding. These are companion-profile obligations rather than evidence of a new defect in either component specification.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Action-time authority, lifecycle and reuse binding remains a cross-specification assurance gap | Critical | open | Companion Specification | [RK-G01 — Genesis Policy Capture](../../../build/site/catalogue.html#RK-G01) |
| `F-002` | Task-specific relying context, provenance and privacy binding remains incomplete | High | open | Companion Specification | [RK-G01 — Genesis Policy Capture](../../../build/site/catalogue.html#RK-G01) |

### Detailed findings

#### F-001 — Action-time authority, lifecycle and reuse binding remains a cross-specification assurance gap

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Implementation Guidance |
| Scenarios | `XSP-TZ-001`, `XSP-TZ-002`, `XSP-TZ-004` |
| Scenario patterns | `SP-AUTH-01`, `SP-COMP-01`, `SP-DEL-01`, `SP-GOV-01` |
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
| `instances/dtg/reviews/2026-08-trust-tasks.md` | Trust Tasks through 2a40f6bd explicitly separates proof from role/scope authorization and strengthens lifecycle semantics, but does not define a universal cross-system delegation or mandate model. |
| `https://github.com/trustoverip/dtgwg-zkp-tf/blob/b37d52fca4ab64ef759d4952b13757f3b23cb20b/proof-of-liveness-requirements.md` | ZKP v0.3 explicitly states key control is not agent authority and models agent authorization as separate delegation evidence with scope, duration and revocation. |
| `instances/dtg/reviews/2026-08-zkp-fork.md` | Fork-local v0.4 implementation guidance further strengthens freshness, revocation and assurance boundaries but intentionally does not define a delegation protocol. |
| `corpora/trust-tasks-zkp-composed.yaml#xsp-tz-004` | The composed scenario preserves the failure case where delegated authority changes after proof generation but before consequential task execution. |

**Potential harm**

A ZK proof can be cryptographically valid and fresh for its presentation transcript while the principal's mandate for the consequential Trust Task is revoked, expired, out of scope or otherwise no longer effective. Treating proof freshness as mandate freshness can therefore authorize an action neither component independently permits.

**Recommended treatment**

Define a Trust Tasks × ZKP companion contract that binds the proof request to the consequential task and requires a separate action-time delegated-authority decision covering principal, delegate, task/action, scope, constraints, validity interval and revocation state. The execution boundary must re-evaluate mandate state immediately before the side effect and must not infer authority from proof validity, holder binding or liveness/personhood predicates.

**Retest when**

- A companion profile defines a machine-verifiable delegation/mandate reference and its binding to the Trust Task and ZKP transcript.
- Negative tests prove that valid proof plus revoked, expired or out-of-scope delegation fails before consequential execution.
- Replay or retry tests prove that a proof/task pair cannot repeat a one-time side effect outside the declared execution semantics.

#### F-002 — Task-specific relying context, provenance and privacy binding remains incomplete

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
| `https://github.com/trustoverip/dtgwg-zkp-tf/blob/b37d52fca4ab64ef759d4952b13757f3b23cb20b/proof-of-liveness-requirements.md` | ZKP v0.3 requires transcript binding to protocol/profile, verifier or audience, challenge, session, requested predicates, policy version and expiry boundary, and defines context-dependent unlinkability rather than universal unlinkability. |
| `instances/dtg/reviews/2026-08-trust-tasks.md` | Trust Tasks now exposes explicit task and lifecycle semantics, but the specifications do not jointly define which task provenance and outcome facts must be committed into a privacy-preserving proof transcript. |
| `corpora/trust-tasks-zkp-composed.yaml#xsp-tz-003` | A valid proof can still be reused at the composition seam if the relying party cannot establish that its purpose, task instance, audience and side-effect context are the ones the prover authorized. |

**Potential harm**

A proof generated for a legitimate purpose can be replayed or semantically upgraded into another Trust Task, while raw task identifiers, lifecycle metadata or retained evidence can also create correlation channels that defeat the intended ZKP privacy boundary.

**Recommended treatment**

Define the minimum task-specific commitment carried into the ZKP transcript or companion evidence: task type/action, purpose, audience, task-instance or privacy-preserving task commitment, relevant policy/version, freshness boundary and outcome-evidence semantics. Require disclosure minimization so task correlation handles are not exposed merely to prove provenance, and keep proof verification, task completion and authorization as separate machine-readable outcomes.

**Retest when**

- A composition profile specifies the canonical task-context commitment and the verifier-visible semantics it establishes and does not establish.
- Cross-task and cross-audience negative vectors reject proof reuse outside the authorized task/purpose boundary.
- Privacy vectors demonstrate that provenance can be established without leaking an unnecessary durable cross-context correlator.

<!-- END GENERATED PRESSURE TEST -->

