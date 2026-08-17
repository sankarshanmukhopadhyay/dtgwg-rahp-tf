# Trust Tasks Framework pressure-test example

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This directory records a **substantive RAHP pressure test of the Trust Tasks Framework**, using the same review-record model as the DTG Credential Specification example.

The purpose is not to argue that every safety concern belongs in `SPEC.md`. Trust Tasks intentionally separates document authenticity, authorization, transport, ceremony evidence, deployment policy and task-specific semantics. The pressure test preserves that architecture by routing each finding to the narrowest effective control plane.

The target revision, review scope, RAHP baseline, summary and complete finding record are rendered below directly from the canonical [`pressure-test.yaml`](pressure-test.yaml).

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `SR-002` |
| Status | complete |
| Title | Trust Tasks Framework editor's draft 0.3 pressure test |
| Reviewed on | 2026-08-12 |
| Target repository | `trustoverip/dtgwg-trust-tasks-tf` |
| Target document | https://trustoverip.github.io/dtgwg-trust-tasks-tf/SPEC.html |
| Target version | Editor's Draft 0.3 (2026-08-07) |
| Target commit | `fbe196a8a17ba3f99d0657a64be5ac58621023a1` |
| Target source paths | `SPEC.md`, `docs/design-notes/delegated-trust-task-execution.md`, `docs/design-notes/trust-ceremonies.md`, `specs/task-consent/`, `specs/trust-task-discovery/`, `specs/trust-ceremony-receipt/` |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v1.1.0` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-16 |
| Engine/method revalidated on | 2026-08-17 |
| Original RAHP version | `v0.3-dev` |
| Revalidation scope | v1.1 portable assurance catalogue mapping plus method/engine revalidation; pinned target revision unchanged |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/pressure-testing-a-spec.md` |
| Rule | Reuse existing RAHP risks before creating new risks; route each recommendation to the narrowest effective control plane. |

### Review scope

**Included**

- Trust Task document model, party identity and proof semantics
- Producer and consumer conformance requirements
- Freshness, expiry, replay and error semantics
- Specification versioning, maturity and registry resolution
- Side-effect and exposure classifications
- Discovery and capability negotiation
- Trust Ceremony envelope semantics and evidence boundary
- Delegated-execution and task-consent architecture where it tests framework assumptions

**Excluded**

- Line-by-line security audit of Rust or TypeScript implementations
- Cryptographic review of individual Data Integrity suites
- Review of every task-specific payload schema in the registry
- Review of any specific VTC governance framework

### Summary

| Measure | Value |
|---|---:|
| Findings | 8 |
| Open findings | 8 |
| Primary disposition: Specification | 4 |
| Primary disposition: Companion Specification | 2 |
| Primary disposition: Governance | 1 |
| Primary disposition: Operational Policy | 1 |

**Overall assessment**

The Trust Tasks framework has unusually strong separation between transport identity, document proof, audience binding, ceremony membership and authorization, and it explicitly treats destructive effects and delegated action as separate safety dimensions. The pressure test nevertheless finds eight open assurance gaps concentrated around repeat execution, freshness, portable authority, mutable draft semantics, registry dependence, negotiation, human approval and supported representation. Several should not be solved by enlarging the core envelope; they need explicit companion profiles or governance requirements.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Repeat execution of mutating or destructive tasks is not normatively prevented | Critical | open | Specification | [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02), [RK-AI01 — Agent Credential Scope Creep](../../build/site/catalogue.html#RK-AI01) |
| `F-002` | High-impact Trust Tasks can remain valid without a bounded freshness window | High | open | Specification | [RK-AI02 — Stale Agent After Operator Revocation](../../build/site/catalogue.html#RK-AI02), [RK-CR02 — Stale Credential / Expiry Without Renewal Path](../../build/site/catalogue.html#RK-CR02), [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02) |
| `F-003` | Producer identity is not portable evidence of authority, delegation or mandate | Critical | open | Companion Specification | [RK-AI01 — Agent Credential Scope Creep](../../build/site/catalogue.html#RK-AI01), [RK-AI02 — Stale Agent After Operator Revocation](../../build/site/catalogue.html#RK-AI02), [RK-G05 — Governanceless VTC Claiming Credential Compliance](../../build/site/catalogue.html#RK-G05) |
| `F-004` | Mutable draft specifications undermine reproducible validation of retained Trust Task evidence | High | open | Specification | [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02), [RK-SY03 — Open Issues Left Unresolved at Scale](../../build/site/catalogue.html#RK-SY03) |
| `F-005` | Runtime registry resolution can become an availability and semantic-integrity dependency | High | open | Operational Policy | [RK-EX02 — Registry Censorship / Denial of Service](../../build/site/catalogue.html#RK-EX02), [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02) |
| `F-006` | Capability discovery does not negotiate the security profile needed to execute a supported task | High | open | Companion Specification | [RK-CY01 — ZKP Implementation Failure](../../build/site/catalogue.html#RK-CY01), [RK-ID04 — DID Document Manipulation](../../build/site/catalogue.html#RK-ID04), [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02) |
| `F-007` | Destructive and actsAsSubject classifications do not establish a minimum human-approval floor | Critical | open | Governance | [RK-AI01 — Agent Credential Scope Creep](../../build/site/catalogue.html#RK-AI01), [RK-HX04 — Incapacity / Unsupported Decision-Making Exclusion](../../build/site/catalogue.html#RK-HX04) |
| `F-008` | Supported decision-making and legal representation have no framework-level binding point | High | open | Specification | [RK-HX04 — Incapacity / Unsupported Decision-Making Exclusion](../../build/site/catalogue.html#RK-HX04), [RK-HX05 — Legal Capacity Architecture Gap — LPA / Guardianship Not Representable](../../build/site/catalogue.html#RK-HX05), [RK-SC05 — Credential Schema Gap — Supported Consent and LPA Not Representable](../../build/site/catalogue.html#RK-SC05) |

### Detailed findings

#### F-001 — Repeat execution of mutating or destructive tasks is not normatively prevented

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | Runtime Control, Implementation Guidance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02), [RK-AI01 — Agent Credential Scope Creep](../../build/site/catalogue.html#RK-AI01) |
| Controls | [CT-19 — Conformance Test Suite](../../build/site/catalogue.html#CT-19), [CT-30 — Cryptographic Delegation Scope Constraints](../../build/site/catalogue.html#CT-30), [CT-48 — Threat Model Maintenance](../../build/site/catalogue.html#CT-48) |
| Guardrails | [GR-12 — Agent Delegation Scope Constraint](../../build/site/catalogue.html#GR-12), [GR-16 — Formal Threat Model Publication](../../build/site/catalogue.html#GR-16) |
| Assurance tests | [AT-12 — Agent exceeding capability constraints rejected by VTA PEP; operator VMC revocation propag…](../../build/site/catalogue.html#AT-12) |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-INF-01`, `HRM-ECO-02` |
| Risks | `RKP-AUTH-01`, `RKP-AUTH-03`, `RKP-CRD-01`, `RKP-OPS-02` |
| Controls | `CTP-AUTH-01`, `CTP-AUTH-03`, `CTP-OPS-02` |
| Guardrails | `GRP-AUTH-01`, `GRP-DEL-01`, `GRP-OPS-01` |
| Assurance | `ATP-AUTH-01`, `ATP-DEL-01`, `ATP-OPS-02` |
| Evidence | `EVP-AUTH-01`, `EVP-AUTH-02`, `EVP-OPS-02` |

**Evidence**

| Source | Observation |
|---|---|
| `SPEC.md#101-cross-recipient-replay` | Producers must mint a unique document id, but same-recipient replay protection is only a SHOULD: consumers handling assertions whose effect persists between exchanges SHOULD maintain an idempotency cache keyed on id. |
| `SPEC.md#73-specification-requirements` | Every specification declares whether execution is none, mutating or destructive, so the framework already has a machine-readable signal that could trigger a stronger replay rule for state-changing operations. |

**Potential harm**

A captured or accidentally retried Trust Task can execute the same state mutation, destructive operation or authority-bearing action more than once even though the document itself remains valid. For deletion, key rotation, credential issuance, grants or actions performed as the subject, duplicate execution can be irreversible or create authority the producer never intended to create twice.

**Recommended treatment**

Make duplicate suppression normative for mutating, destructive and actsAsSubject tasks. Define the minimum replay-key lifetime and the required duplicate disposition, and allow task-specific specifications to strengthen the rule with operation-level idempotency keys where document id alone is insufficient.

**Retest when**

- Same-recipient replay handling is mandatory for state-changing and authority-exercising tasks.

#### F-002 — High-impact Trust Tasks can remain valid without a bounded freshness window

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | Operational Policy |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-AI02 — Stale Agent After Operator Revocation](../../build/site/catalogue.html#RK-AI02), [RK-CR02 — Stale Credential / Expiry Without Renewal Path](../../build/site/catalogue.html#RK-CR02), [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02) |
| Controls | [CT-19 — Conformance Test Suite](../../build/site/catalogue.html#CT-19), [CT-25 — Credential Renewal Workflow](../../build/site/catalogue.html#CT-25), [CT-31 — Short-Lived Agent Credentials](../../build/site/catalogue.html#CT-31), [CT-32 — Agent Liveness Check on Operator VMC](../../build/site/catalogue.html#CT-32) |
| Guardrails | [GR-12 — Agent Delegation Scope Constraint](../../build/site/catalogue.html#GR-12), [GR-17 — Open Issues Risk Acceptance](../../build/site/catalogue.html#GR-17) |
| Assurance tests | [AT-12 — Agent exceeding capability constraints rejected by VTA PEP; operator VMC revocation propag…](../../build/site/catalogue.html#AT-12), [AT-17 — All four open issues have documented mitigations or risk acceptances signed by governing b…](../../build/site/catalogue.html#AT-17) |

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
| `SPEC.md#42-top-level-members` | issuedAt is a SHOULD and expiresAt is a MAY. A consumer must honor expiry only when an expiresAt value is actually present. |
| `SPEC.md#73-specification-requirements` | Side-effect and exposure classifications distinguish destructive tasks and tasks that act as the subject, but no framework requirement couples those risk classes to expiry or freshness. |

**Potential harm**

A signed or transport-authenticated instruction that changes authority or acts on a subject's behalf can remain actionable long after the human intent, operator mandate, policy state or security context that produced it has changed. Cryptographic validity alone does not establish that the request is still live.

**Recommended treatment**

Require bounded freshness for destructive and actsAsSubject tasks, either in the framework or a mandatory safety profile. At minimum define when issuedAt and expiresAt are required, maximum-age evaluation, and how a consumer responds when freshness cannot be established.

**Retest when**

- High-impact task classes have testable freshness and maximum-age requirements.

#### F-003 — Producer identity is not portable evidence of authority, delegation or mandate

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Governance, Specification |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-AI01 — Agent Credential Scope Creep](../../build/site/catalogue.html#RK-AI01), [RK-AI02 — Stale Agent After Operator Revocation](../../build/site/catalogue.html#RK-AI02), [RK-G05 — Governanceless VTC Claiming Credential Compliance](../../build/site/catalogue.html#RK-G05) |
| Controls | [CT-30 — Cryptographic Delegation Scope Constraints](../../build/site/catalogue.html#CT-30), [CT-31 — Short-Lived Agent Credentials](../../build/site/catalogue.html#CT-31), [CT-32 — Agent Liveness Check on Operator VMC](../../build/site/catalogue.html#CT-32), [CT-52 — Agent Delegation Credential Requirement](../../build/site/catalogue.html#CT-52), [CT-56 — VTC Governance Conformance Class](../../build/site/catalogue.html#CT-56) |
| Guardrails | [GR-12 — Agent Delegation Scope Constraint](../../build/site/catalogue.html#GR-12), [GR-13 — Agent Audit Logging](../../build/site/catalogue.html#GR-13) |
| Assurance tests | [AT-12 — Agent exceeding capability constraints rejected by VTA PEP; operator VMC revocation propag…](../../build/site/catalogue.html#AT-12), [AT-13 — Agent credential operations visible in operator audit log with all required fields](../../build/site/catalogue.html#AT-13) |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-AUT-05` |
| Risks | `RKP-DEL-01`, `RKP-AGT-01`, `RKP-AUTH-02`, `RKP-DEL-03` |
| Controls | `CTP-DEL-01`, `CTP-AGT-01`, `CTP-AUTH-02`, `CTP-DEL-02` |
| Guardrails | `GRP-DEL-01`, `GRP-AGT-01`, `GRP-AUTH-02` |
| Assurance | `ATP-DEL-01`, `ATP-AGT-01`, `ATP-AUTH-02` |
| Evidence | `EVP-DEL-01`, `EVP-AUTH-02`, `EVP-AUTH-01`, `EVP-DEL-02` |

**Evidence**

| Source | Observation |
|---|---|
| `SPEC.md#72-consumer-requirements` | Ceremony membership explicitly confers no authority; authorization decisions rest on issuer, proof and the consumer's own policy. |
| `SPEC.md#48-the-issuer-and-recipient-members` | issuer identifies the party responsible for the document and proof binds content to that party, but the framework does not define portable evidence that the party is authorized to request the action represented by the task. |
| `docs/design-notes/delegated-trust-task-execution.md#2-roles-and-trust` | Delegated execution deliberately makes the executor's policy authoritative and treats a relying party as untrusted, confirming that authorization is a separate layer from document authenticity. |

**Potential harm**

Implementations can correctly authenticate the same producer yet reach incompatible conclusions about whether that producer is allowed to invoke a task. In agentic or delegated execution, identity can be over-read as mandate, leaving stale or over-broad authority active after the principal's intent changes.

**Recommended treatment**

Preserve the framework's identity/authority separation, but normatively bind a companion authorization or delegation profile for portable use cases. It should identify the principal, delegate, permitted task types/actions, constraints, validity, revocation, onward delegation and the evidence a consumer must evaluate before execution.

**Retest when**

- A portable delegation/capability profile is defined and its binding to Trust Task execution is explicit.

#### F-004 — Mutable draft specifications undermine reproducible validation of retained Trust Task evidence

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | Operational Policy |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02), [RK-SY03 — Open Issues Left Unresolved at Scale](../../build/site/catalogue.html#RK-SY03) |
| Controls | [CT-18 — Normative Credential Schema Publication](../../build/site/catalogue.html#CT-18), [CT-19 — Conformance Test Suite](../../build/site/catalogue.html#CT-19), [CT-47 — Formal Open Issues Mitigation Plan](../../build/site/catalogue.html#CT-47), [CT-48 — Threat Model Maintenance](../../build/site/catalogue.html#CT-48) |
| Guardrails | [GR-16 — Formal Threat Model Publication](../../build/site/catalogue.html#GR-16), [GR-17 — Open Issues Risk Acceptance](../../build/site/catalogue.html#GR-17) |
| Assurance tests | [AT-16 — Published threat model exists, is dated within 12 months, and covers all six listed threat…](../../build/site/catalogue.html#AT-16), [AT-17 — All four open issues have documented mitigations or risk acceptances signed by governing b…](../../build/site/catalogue.html#AT-17) |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-GOV-02`, `HRM-ECO-02` |
| Risks | `RKP-RED-01` |
| Controls | `CTP-RED-01` |
| Guardrails | `GRP-RED-01` |
| Assurance | `ATP-RED-01` |
| Evidence | `EVP-RED-01` |

**Evidence**

| Source | Observation |
|---|---|
| `SPEC.md#52-compatibility-rules` | While a task specification is at draft status, breaking changes may use a MINOR increment and editorial or normalization changes are required to be made in place within the existing version. |
| `SPEC.md#53-maturity-levels` | Draft schemas and prose may change without notice, while producers are still allowed to emit documents whose type resolves to a draft specification. |

**Potential harm**

A retained document can later be evaluated against semantics or schema content different from those in force when it was produced. This weakens auditability, dispute resolution and long-lived evidence because the Type URI alone may not identify the exact normative material under which the document was created.

**Recommended treatment**

Add immutable revision pinning for emitted documents that target draft specifications, such as a content digest, immutable revision URI or registry snapshot reference. Define verification behavior when the historical draft cannot be retrieved. Candidate and standard immutability should remain the preferred production path.

**Retest when**

- Retained documents can unambiguously resolve the exact draft semantics under which they were emitted.

#### F-005 — Runtime registry resolution can become an availability and semantic-integrity dependency

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Operational Policy |
| Secondary dispositions | Specification, Implementation Guidance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-EX02 — Registry Censorship / Denial of Service](../../build/site/catalogue.html#RK-EX02), [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02) |
| Controls | [CT-18 — Normative Credential Schema Publication](../../build/site/catalogue.html#CT-18), [CT-19 — Conformance Test Suite](../../build/site/catalogue.html#CT-19), [CT-39 — Distributed Registry Architecture](../../build/site/catalogue.html#CT-39), [CT-48 — Threat Model Maintenance](../../build/site/catalogue.html#CT-48) |
| Guardrails | [GR-16 — Formal Threat Model Publication](../../build/site/catalogue.html#GR-16) |
| Assurance tests | [AT-16 — Published threat model exists, is dated within 12 months, and covers all six listed threat…](../../build/site/catalogue.html#AT-16) |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-SEC-03`, `HRM-INF-01` |
| Risks | `RKP-OPS-01` |
| Controls | `CTP-OPS-01` |
| Guardrails | — |
| Assurance | `ATP-OPS-01` |
| Evidence | `EVP-OPS-01` |

**Evidence**

| Source | Observation |
|---|---|
| `SPEC.md#72-consumer-requirements` | Consumer validation is defined in terms of obtaining the framework and payload schemas by content-negotiating registry URIs. |
| `SPEC.md#103-schema-validation-dos` | The security considerations explicitly distinguish dynamically obtained schemas from schemas authenticated and embedded at build time, but do not establish a normative caching, pinning or offline-verification baseline. |

**Potential harm**

A registry outage, routing failure, compromised mutable source or forced online dependency can prevent otherwise valid tasks from being processed or cause different consumers to validate against different material. Critical trust operations can therefore inherit a single resolution-path dependency that the transport-agnostic document model does not make obvious to deployers.

**Recommended treatment**

Publish an operational profile for authenticated schema pinning, caching and offline verification. Candidate/standard artifacts should be cacheable indefinitely by immutable digest, with explicit failure behavior when a required artifact cannot be authenticated or retrieved.

**Retest when**

- Registry-unavailable and registry-compromise scenarios have a normative or required operational profile.

#### F-006 — Capability discovery does not negotiate the security profile needed to execute a supported task

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Specification, Implementation Guidance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-CY01 — ZKP Implementation Failure](../../build/site/catalogue.html#RK-CY01), [RK-ID04 — DID Document Manipulation](../../build/site/catalogue.html#RK-ID04), [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02) |
| Controls | [CT-14 — DID Document Integrity Verification](../../build/site/catalogue.html#CT-14), [CT-19 — Conformance Test Suite](../../build/site/catalogue.html#CT-19), [CT-27 — Audited ZKP Library Requirement](../../build/site/catalogue.html#CT-27), [CT-28 — ZKP Conformance Testing](../../build/site/catalogue.html#CT-28), [CT-29 — Algorithm Agility and Migration Pathway](../../build/site/catalogue.html#CT-29) |
| Guardrails | [GR-16 — Formal Threat Model Publication](../../build/site/catalogue.html#GR-16) |
| Assurance tests | [AT-16 — Published threat model exists, is dated within 12 months, and covers all six listed threat…](../../build/site/catalogue.html#AT-16) |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-INF-01`, `HRM-ECO-02`, `HRM-SEC-01`, `HRM-SEC-03` |
| Risks | `RKP-AUTH-01`, `RKP-AUTH-03`, `RKP-DISC-01`, `RKP-DISC-02` |
| Controls | `CTP-AUTH-01`, `CTP-AUTH-03`, `CTP-DISC-01`, `CTP-DISC-02` |
| Guardrails | `GRP-AUTH-01`, `GRP-DEL-01` |
| Assurance | `ATP-AUTH-01`, `ATP-DEL-01`, `ATP-DISC-01`, `ATP-DISC-02` |
| Evidence | `EVP-AUTH-01`, `EVP-AUTH-02`, `EVP-OPS-01` |

**Evidence**

| Source | Observation |
|---|---|
| `SPEC.md#11-discovery-and-capability-negotiation` | Discovery returns supported Type URIs and is advisory. It does not negotiate supported VID methods, proof suites, transport bindings, required extensions or freshness/ authorization profiles for the advertised task. |
| `SPEC.md#47-proof` | The framework permits any appropriate W3C-registered Data Integrity suite, leaving suite choice to the parties' trust requirements. |

**Potential harm**

Two parties can discover that they support the same task and still fail at execution because they do not share a verification method, proof suite, binding or mandatory safety profile. In higher-stakes deployments this can push implementers toward silent downgrade, bespoke fallback or broad acceptance rules that reduce assurance.

**Recommended treatment**

Extend discovery through a companion capability profile that can advertise the security parameters relevant to successful execution without making the core task registry transport-specific. Include supported VID schemes, proof suites, bindings and named authorization/freshness profiles, with anti-downgrade guidance.

**Retest when**

- Parties can discover a mutually executable security profile before sending the task.

#### F-007 — Destructive and actsAsSubject classifications do not establish a minimum human-approval floor

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | Companion Specification, Runtime Control |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-AI01 — Agent Credential Scope Creep](../../build/site/catalogue.html#RK-AI01), [RK-HX04 — Incapacity / Unsupported Decision-Making Exclusion](../../build/site/catalogue.html#RK-HX04) |
| Controls | [CT-30 — Cryptographic Delegation Scope Constraints](../../build/site/catalogue.html#CT-30), [CT-52 — Agent Delegation Credential Requirement](../../build/site/catalogue.html#CT-52), [CT-58 — Accessible Trust Task Ceremony UX for Cognitive Differences](../../build/site/catalogue.html#CT-58) |
| Guardrails | [GR-12 — Agent Delegation Scope Constraint](../../build/site/catalogue.html#GR-12), [GR-19 — Supported Decision-Making and Legal Delegation Pathway](../../build/site/catalogue.html#GR-19) |
| Assurance tests | [AT-12 — Agent exceeding capability constraints rejected by VTA PEP; operator VMC revocation propag…](../../build/site/catalogue.html#AT-12), [AT-19 — For any VTC that has admitted or intends to admit participants under supported or substitu…](../../build/site/catalogue.html#AT-19) |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-INF-01`, `HRM-ECO-02`, `HRM-GOV-01`, `HRM-GOV-03` |
| Risks | `RKP-AUTH-01`, `RKP-AUTH-03`, `RKP-GOV-01` |
| Controls | `CTP-AUTH-01`, `CTP-AUTH-03`, `CTP-GOV-01` |
| Guardrails | `GRP-AUTH-01`, `GRP-DEL-01`, `GRP-GOV-01` |
| Assurance | `ATP-AUTH-01`, `ATP-DEL-01`, `ATP-GOV-01` |
| Evidence | `EVP-AUTH-01`, `EVP-AUTH-02`, `EVP-GOV-01` |

**Evidence**

| Source | Observation |
|---|---|
| `SPEC.md#73-specification-requirements` | Side-effect and exposure classifications are explicitly descriptive, not prescriptive; a specification must not derive a consent requirement from them. |
| `docs/design-notes/delegated-trust-task-execution.md#3-the-invariant` | Policy enforcement is opt-in and the boot-installed baseline allows every task, including destructive tasks. Human consent exists only where a deployment enables enforcement and authors a requireConsent policy. |

**Potential harm**

Two conforming deployments can treat the same destructive or subject-authority action very differently: one can require meaningful human approval while another can execute it automatically. For agent-mediated operation this can turn a technically conforming task vocabulary into an automation surface that exceeds the principal's expectations.

**Recommended treatment**

Keep consent policy out of generic payload schemas, but define a governance/safety profile for deployments that execute on behalf of people. The profile should establish minimum approval requirements for destructive and actsAsSubject actions, fail-safe behavior when effects cannot be rendered, and explicit exceptions for pre-authorized automation.

**Retest when**

- A named deployment profile establishes minimum approval behavior for high-impact delegated execution.

#### F-008 — Supported decision-making and legal representation have no framework-level binding point

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | Companion Specification, Governance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-HX04 — Incapacity / Unsupported Decision-Making Exclusion](../../build/site/catalogue.html#RK-HX04), [RK-HX05 — Legal Capacity Architecture Gap — LPA / Guardianship Not Representable](../../build/site/catalogue.html#RK-HX05), [RK-SC05 — Credential Schema Gap — Supported Consent and LPA Not Representable](../../build/site/catalogue.html#RK-SC05) |
| Controls | [CT-57 — Supported Decision-Making Credential Extension](../../build/site/catalogue.html#CT-57), [CT-58 — Accessible Trust Task Ceremony UX for Cognitive Differences](../../build/site/catalogue.html#CT-58), [CT-59 — LPA Delegation Credential Type](../../build/site/catalogue.html#CT-59), [CT-60 — Secondary Notification Recipient Registration](../../build/site/catalogue.html#CT-60), [CT-66 — Children's Data Processing Impact Assessment Requirement](../../build/site/catalogue.html#CT-66) |
| Guardrails | [GR-19 — Supported Decision-Making and Legal Delegation Pathway](../../build/site/catalogue.html#GR-19) |
| Assurance tests | [AT-19 — For any VTC that has admitted or intends to admit participants under supported or substitu…](../../build/site/catalogue.html#AT-19) |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-SEC-01`, `HRM-INF-01` |
| Risks | `RKP-DEL-01`, `RKP-AGT-01`, `RKP-ID-01` |
| Controls | `CTP-DEL-01`, `CTP-AGT-01`, `CTP-ID-01` |
| Guardrails | `GRP-DEL-01`, `GRP-AGT-01`, `GRP-ID-01` |
| Assurance | `ATP-DEL-01`, `ATP-AGT-01`, `ATP-ID-01` |
| Evidence | `EVP-DEL-01`, `EVP-AUTH-02`, `EVP-AUTH-01` |

**Evidence**

| Source | Observation |
|---|---|
| `SPEC.md#2-terminology` | The framework models each document bilaterally with one producer/issuer and one consumer/recipient, while additional people represented in a payload have no common framework semantics. |
| `SPEC.md#73-specification-requirements` | Specifications define parties and payloads but there is no common representation for a representative acting with or for a subject, supported consent, notification of a secondary decision-support person, or legal delegation evidence. |

**Potential harm**

Task specifications can independently invent incompatible ways to represent guardians, attorneys, supporters or co-decision-makers, or omit them entirely. People who cannot safely or legally act through a single-controller interaction can therefore be excluded from otherwise interoperable trust workflows.

**Recommended treatment**

Add an explicit extension/binding point for representation semantics and normatively reference a companion supported-decision-making/legal-delegation profile. Do not require every Trust Task to carry representation data; require specifications and deployments to avoid inferring exclusive legal capacity from issuer identity alone.

**Retest when**

- A reusable representation/delegation profile is defined and the framework states how task specifications bind to it.

<!-- END GENERATED PRESSURE TEST -->

## What the pressure test found

### 1. Unique IDs are not enough when execution has side effects

The framework correctly requires every document to have a globally unique `id`, but same-recipient duplicate suppression is only a `SHOULD`. That is too weak for a framework that already classifies tasks as `mutating`, `destructive`, or `actsAsSubject`.

The RAHP recommendation is narrow: make replay suppression mandatory for those classes, define the lifetime of the replay record, and permit task-specific operation-level idempotency where a document identifier alone is not sufficient.

### 2. High-impact instructions need freshness, not only authenticity

`issuedAt` is recommended and `expiresAt` is optional. As a result, a cryptographically valid destructive instruction can remain actionable after the human intent, mandate or policy state that produced it has expired.

The pressure test does not recommend making every read-only query short-lived. It recommends coupling a bounded freshness rule to the task classes that can destroy state or exercise the subject's authority.

### 3. Identity and authority are correctly separated, but portable delegation is still missing

One of the strongest properties of Trust Tasks is that ceremony membership explicitly **does not confer authority**. The same separation needs a portable positive path: when a producer is an agent, representative or delegated executor, what evidence proves that it is allowed to ask for this particular action?

That belongs primarily in a companion authorization/delegation profile rather than in the generic envelope. The profile should cover principal, delegate, task scope, constraints, validity, revocation and onward delegation.

### 4. Draft mutability conflicts with long-lived evidentiary use

The framework allows producers to emit against `draft` task specifications while also allowing draft schema/prose to change without notice and some changes to occur in place. A retained task can therefore outlive the exact semantics under which it was produced.

The proposed fix is not to eliminate drafts. It is to make emitted draft documents able to pin the exact revision — by content digest, immutable revision URI or equivalent registry snapshot — so later verification is reproducible.

### 5. The registry needs an offline and failure-mode profile

The consumer algorithm is described in terms of resolving framework and payload schemas by content negotiation. The security section already recognizes the difference between dynamically resolved and build-pinned schemas.

RAHP turns that observation into an operational requirement: define authenticated caching, immutable digest pinning, offline verification and fail-closed behavior when a required artifact cannot be authenticated.

### 6. “We support the same task” does not yet mean “we can execute it together”

Discovery advertises Type URIs. It does not advertise the VID methods, proof suites, transport bindings or named authorization/freshness profiles that make the task executable.

A companion capability profile can close this gap without making Trust Tasks transport-specific. Its purpose is anti-downgrade interoperability, not another mandatory envelope field.

### 7. Safety classifications do not create a human-consent baseline

The distinction between `sideEffects` and `exposure` is excellent: a signing operation may mutate no local state while still exercising the subject's authority. But the classifications are intentionally descriptive, and the delegated-execution design confirms that policy enforcement is opt-in.

That means a destructive or `actsAsSubject` task can be conformingly automated with no human approval unless deployment governance says otherwise. RAHP routes this primarily to a **governance/safety profile**, including fail-safe treatment where effects cannot be rendered.

### 8. Supported decision-making needs a reusable representation path

The bilateral document model works for protocol transport, but it does not provide shared semantics for a guardian, attorney, supporter, co-decision-maker or secondary notification person. Leaving every task specification to invent this independently will create incompatible representations and exclusion.

The recommendation is a common companion representation/delegation profile plus a framework non-inference rule: issuer identity must not be treated as proof that no legally authorized or supported representative exists.

## Positive controls observed

A pressure test should record safeguards that already work, not only gaps. The reviewed draft has several important strengths:

- a proof binds document content to the issuer and, for non-bearer use, cryptographically binds the intended recipient;
- in-band and transport-derived identities are cross-checked rather than silently overridden;
- ceremony membership explicitly confers no authority;
- destructive side effects and `actsAsSubject` exposure are modeled as separate dimensions;
- dynamically obtained schemas are recognized as a security boundary;
- discovery is advisory rather than an authorization commitment;
- the delegated-execution design binds human approval to the exact payload and state being executed.

These controls are why several findings are routed outside the core framework rather than expressed as requests for additional envelope fields.

## Reproducing the review

```bash
pip install -r requirements.txt
python3 tools/validate.py
python3 tools/render_pressure_tests.py
python3 tools/validate_pressure_tests.py
```

The pressure-test validator checks this record and the credential-spec review together. It verifies commit pinning, required finding metadata, dispositions, summary counts, and every RAHP risk/control/guardrail/assurance-test reference.

## Re-testing

Re-run SR-002 when the Trust Tasks framework changes any of the following:

- replay/idempotency requirements;
- freshness or expiry requirements;
- delegation/authorization profiles;
- draft version immutability rules;
- registry caching/pinning guidance;
- discovery/capability negotiation;
- delegated-execution consent policy; or
- supported representation semantics.

Do not overwrite the target commit while leaving the findings unchanged. Update each finding's state against the newly reviewed commit and retain the old commit as historical review evidence.

## Interpretation boundary

This review does **not** assert that the Trust Tasks core document format should absorb all governance, delegation, legal-capacity or consent semantics. In several places the current architecture is stronger precisely because it separates those concerns. RAHP's role is to make the remaining dependency explicit, assign it to a control plane, and give the project a testable condition for knowing when the risk has actually been addressed.
