# DTG Credential Specification pressure-test example

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This directory contains a **substantive RAHP pressure test**, not an illustrative placeholder. It demonstrates how a standards review can be pinned to a precise target revision, mapped to the canonical RAHP corpus, routed to the correct control plane, and retained for later re-testing.

The target revision, review scope, RAHP baseline, summary and complete finding record are rendered below directly from the canonical [`pressure-test.yaml`](pressure-test.yaml).

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `SR-001` |
| Status | complete |
| Title | DTG Core Credential Specification Working Draft 01 pressure test |
| Reviewed on | 2026-08-12 |
| Target repository | `trustoverip/dtgwg-cred-spec` |
| Target document | https://trustoverip.github.io/dtgwg-cred-spec/ |
| Target version | Working Draft 01 |
| Target commit | `d19f7c9cac364fab8e50cf434513ef53fef80e37` |
| Target source paths | `spec/intro.md`, `spec/body.md` |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v0.8.0` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-16 |
| Engine/method revalidated on | 2026-08-16 |
| Original RAHP version | `v0.3-dev` |
| Revalidation scope | method-and-engine-only; target revision and substantive findings unchanged |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/pressure-testing-a-spec.md` |
| Rule | Reuse existing RAHP risks before creating new risks; route each recommendation to the narrowest effective control plane. |

### Review scope

**Included**

- Credential taxonomy and common credential structure
- VRC and VMC edge semantics
- VIC invitation semantics
- VPC, VWC and VEC annotation semantics
- Trust Task context binding
- Security, privacy, governance and conformance requirements

**Excluded**

- Cryptographic implementation review of any specific ZKP suite
- Review of the future DTG Core Trust Task Protocols specification
- Review of any specific VTC governance framework or registry implementation

### Summary

| Measure | Value |
|---|---:|
| Findings | 8 |
| Open findings | 8 |
| Primary disposition: Specification | 5 |
| Primary disposition: Companion Specification | 2 |
| Primary disposition: Governance | 1 |

**Overall assessment**

Working Draft 01 is materially stronger than the earlier credential draft in privacy, task-context binding, witness semantics and verifier authorization checks. The pressure test nevertheless identifies eight open assurance gaps. Two are structural schema or semantic ambiguities, three concern lifecycle/authority boundaries, and three are scope gaps that need an explicit companion-specification or governance route rather than being silently left to implementers.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | The reverse VMC required for a complete membership edge is not constructible from the normative schema | High | open | Specification | [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02) |
| `F-002` | VMC membership of an agent can be misread as agent authority, capability or operator accountability | High | open | Specification | [RK-AI01 — Agent Credential Scope Creep](../../build/site/catalogue.html#RK-AI01), [RK-AI02 — Stale Agent After Operator Revocation](../../build/site/catalogue.html#RK-AI02), [RK-G05 — Governanceless VTC Claiming Credential Compliance](../../build/site/catalogue.html#RK-G05) |
| `F-003` | Credential status and lifecycle semantics are too weak for consistent revocation and stale-authority handling | High | open | Specification | [RK-ID03 — IDVP Breach / Cascading Invalidation](../../build/site/catalogue.html#RK-ID03), [RK-CR01 — Credential Revocation Without Due Process](../../build/site/catalogue.html#RK-CR01), [RK-CR02 — Stale Credential / Expiry Without Renewal Path](../../build/site/catalogue.html#RK-CR02), [RK-CR03 — Revocation Cascade / Cross-VTC Contamination](../../build/site/catalogue.html#RK-CR03), [RK-AI02 — Stale Agent After Operator Revocation](../../build/site/catalogue.html#RK-AI02) |
| `F-004` | The M-DID bootstrapping exception has no bounded migration or retirement semantics | High | open | Specification | [RK-SC04 — M-DID Bootstrapping Exception Undermines R-DID Privacy](../../build/site/catalogue.html#RK-SC04), [RK-ID05 — M-DID Linkability Across VTCs](../../build/site/catalogue.html#RK-ID05) |
| `F-005` | ZKP-by-default guidance is not interoperable or conformance-testable without a proof profile | High | open | Companion Specification | [RK-CY01 — ZKP Implementation Failure](../../build/site/catalogue.html#RK-CY01) |
| `F-006` | Conformance needs a sharper boundary between schema validity and governance-qualified DTG meaning | High | open | Governance | [RK-G05 — Governanceless VTC Claiming Credential Compliance](../../build/site/catalogue.html#RK-G05), [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02) |
| `F-007` | Supported decision-making, guardianship and power-of-attorney relationships are not representable | High | open | Companion Specification | [RK-HX05 — Legal Capacity Architecture Gap — LPA / Guardianship Not Representable](../../build/site/catalogue.html#RK-HX05), [RK-SC05 — Credential Schema Gap — Supported Consent and LPA Not Representable](../../build/site/catalogue.html#RK-SC05) |
| `F-008` | Organisational membership and relationship semantics are not explicit in the identifier model | High | open | Specification | [RK-EX05 — Organisational Identity Architecture Gap](../../build/site/catalogue.html#RK-EX05) |

### Detailed findings

#### F-001 — The reverse VMC required for a complete membership edge is not constructible from the normative schema

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02) |
| Controls | [CT-18 — Normative Credential Schema Publication](../../build/site/catalogue.html#CT-18), [CT-19 — Conformance Test Suite](../../build/site/catalogue.html#CT-19) |
| Guardrails | [GR-01 — Genesis Policy Documentation](../../build/site/catalogue.html#GR-01) |
| Assurance tests | [AT-01 — Genesis policy artefact exists, is version-controlled, and was committed before any Phase …](../../build/site/catalogue.html#AT-01) |

**Evidence**

| Source | Observation |
|---|---|
| `spec/body.md#vmc-verifiable-membership-credential` | The specification states that two VMCs, one in each direction, form a complete DTG edge, but the normative VMC schema requires the issuer to be the VTC/VTN C-DID and the subject to be the member M-DID (or a C-DID for VTN-to-VTC membership). It does not define the member-issued acknowledgement direction. |

**Related work**

| Reference | Status | Note |
|---|---|---|
| `trustoverip/dtgwg-cred-spec#12` | open-pr | PR #12 proposes direction-qualified VMC rules and explicit consent semantics but was not merged at the reviewed commit. |

**Potential harm**

Implementations can either treat a unilateral community assertion as complete membership or invent incompatible reverse-credential structures. The former permits unconsented membership assertions; the latter breaks interoperability.

**Recommended treatment**

Define both VMC directions normatively, including issuer/subject rules, binding between the grant and acknowledgement, ordering, verifier behavior and the consent semantics of the reverse direction.

**Retest when**

- PR #12 or an equivalent VMC directionality change is merged.

#### F-002 — VMC membership of an agent can be misread as agent authority, capability or operator accountability

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | Companion Specification, Governance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-AI01 — Agent Credential Scope Creep](../../build/site/catalogue.html#RK-AI01), [RK-AI02 — Stale Agent After Operator Revocation](../../build/site/catalogue.html#RK-AI02), [RK-G05 — Governanceless VTC Claiming Credential Compliance](../../build/site/catalogue.html#RK-G05) |
| Controls | [CT-30 — Cryptographic Delegation Scope Constraints](../../build/site/catalogue.html#CT-30), [CT-31 — Short-Lived Agent Credentials](../../build/site/catalogue.html#CT-31), [CT-32 — Agent Liveness Check on Operator VMC](../../build/site/catalogue.html#CT-32), [CT-56 — VTC Governance Conformance Class](../../build/site/catalogue.html#CT-56) |
| Guardrails | [GR-12 — Agent Delegation Scope Constraint](../../build/site/catalogue.html#GR-12), [GR-13 — Agent Audit Logging](../../build/site/catalogue.html#GR-13) |
| Assurance tests | [AT-12 — Agent exceeding capability constraints rejected by VTA PEP; operator VMC revocation propag…](../../build/site/catalogue.html#AT-12), [AT-13 — Agent credential operations visible in operator audit log with all required fields](../../build/site/catalogue.html#AT-13) |

**Evidence**

| Source | Observation |
|---|---|
| `spec/body.md#vmc-verifiable-membership-credential` | The VMC subject is explicitly allowed to be a person, device or agent, while the VMC schema contains only membership semantics. |
| `spec/body.md#security-considerations` | Issuer authorization is checked, but the specification does not state that membership must not be interpreted as authority to act, delegation, operator identity, autonomy or capability. |

**Potential harm**

A verifier or higher-layer protocol can over-read a valid agent VMC as evidence that the agent is authorized to perform an action or that accountability has been established. This creates scope creep and can leave agent authority live after the operator's mandate changes.

**Recommended treatment**

Add an explicit semantic non-inference rule: a VMC may establish membership of an agent node but does not establish agenthood, operator/controller identity, accountability, delegation, autonomy, capability or current authority. Require those properties to be established by separate verifiable evidence and define the binding point to the companion agent/delegation protocol.

**Retest when**

- The VMC semantics or companion agent/delegation specification defines this boundary.

#### F-003 — Credential status and lifecycle semantics are too weak for consistent revocation and stale-authority handling

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | Companion Specification, Governance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-ID03 — IDVP Breach / Cascading Invalidation](../../build/site/catalogue.html#RK-ID03), [RK-CR01 — Credential Revocation Without Due Process](../../build/site/catalogue.html#RK-CR01), [RK-CR02 — Stale Credential / Expiry Without Renewal Path](../../build/site/catalogue.html#RK-CR02), [RK-CR03 — Revocation Cascade / Cross-VTC Contamination](../../build/site/catalogue.html#RK-CR03), [RK-AI02 — Stale Agent After Operator Revocation](../../build/site/catalogue.html#RK-AI02) |
| Controls | [CT-12 — IDVP Security Approval Criteria](../../build/site/catalogue.html#CT-12), [CT-13 — IDVP Deregistration Handling Protocol](../../build/site/catalogue.html#CT-13), [CT-23 — Mandatory Pre-Revocation Notice](../../build/site/catalogue.html#CT-23), [CT-24 — Privacy-Preserving Revocation Disclosure](../../build/site/catalogue.html#CT-24), [CT-25 — Credential Renewal Workflow](../../build/site/catalogue.html#CT-25), [CT-26 — VTC-Scoped Revocation](../../build/site/catalogue.html#CT-26), [CT-32 — Agent Liveness Check on Operator VMC](../../build/site/catalogue.html#CT-32) |
| Guardrails | [GR-05 — IDVP Registry Standing](../../build/site/catalogue.html#GR-05), [GR-08 — Revocation Due Process](../../build/site/catalogue.html#GR-08), [GR-09 — Privacy-Preserving Revocation Disclosure](../../build/site/catalogue.html#GR-09), [GR-12 — Agent Delegation Scope Constraint](../../build/site/catalogue.html#GR-12) |
| Assurance tests | [AT-05 — IDVP DID not in trust registry with correct role → VTA rejects IDVC presentation](../../build/site/catalogue.html#AT-05), [AT-08 — Revocation notice delivered to member within SLA; appeals path accessible within 24 hours](../../build/site/catalogue.html#AT-08), [AT-09 — Default revocation status disclosure does not expose member real-world identity](../../build/site/catalogue.html#AT-09), [AT-12 — Agent exceeding capability constraints rejected by VTA PEP; operator VMC revocation propag…](../../build/site/catalogue.html#AT-12) |

**Evidence**

| Source | Observation |
|---|---|
| `spec/body.md#base-structure` | The common schema defines validity dates but no required credential-status mechanism or status-reference semantics. |
| `spec/body.md#security-considerations` | Verifiers are told they should check applicable revocation status via the governing trust registry, leaving the mechanism, required availability, failure behavior and timing semantics undefined. |

**Potential harm**

Two conforming verifiers may reach different decisions about a credential after withdrawal, issuer compromise, membership termination or operator revocation. Stale credentials can remain cryptographically valid while their governing authority is no longer valid.

**Recommended treatment**

Define a normative lifecycle/status contract or a mandatory profile hook: how status is discovered, the authoritative time semantics, verifier behavior when status is unavailable, and how revocation, suspension, expiry and renewal differ. Keep due process and cross-community consequence policy in governance, but make the technical status semantics interoperable.

**Retest when**

- Credential status/lifecycle semantics are specified or normatively delegated to a named profile.

#### F-004 — The M-DID bootstrapping exception has no bounded migration or retirement semantics

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-SC04 — M-DID Bootstrapping Exception Undermines R-DID Privacy](../../build/site/catalogue.html#RK-SC04), [RK-ID05 — M-DID Linkability Across VTCs](../../build/site/catalogue.html#RK-ID05) |
| Controls | [CT-15 — Pseudonymous Per-VTC M-DID Design](../../build/site/catalogue.html#CT-15), [CT-50 — M-DID to R-DID Migration Trigger](../../build/site/catalogue.html#CT-50) |
| Guardrails | [GR-06 — Privacy-Preserving Proofing Option](../../build/site/catalogue.html#GR-06), [GR-09 — Privacy-Preserving Revocation Disclosure](../../build/site/catalogue.html#GR-09), [GR-18 — R-DID Migration Phase Gate](../../build/site/catalogue.html#GR-18) |
| Assurance tests | [AT-06 — At least one ZKP / selective disclosure path is available and functional in Phase 4 UX](../../build/site/catalogue.html#AT-06), [AT-09 — Default revocation status disclosure does not expose member real-world identity](../../build/site/catalogue.html#AT-09), [AT-18 — VTC trust registry records a migration trigger date for R-DID adoption; all VRCs issued af…](../../build/site/catalogue.html#AT-18) |

**Evidence**

| Source | Observation |
|---|---|
| `spec/body.md#vrc-verifiable-relationship-credential` | R-DIDs are recommended for privacy while M-DIDs are allowed for bootstrapping. |
| `spec/body.md#privacy-considerations` | Migration from M-DID-based to R-DID-based edges is recommended post-bootstrapping, without a trigger, deadline or verifier-visible state transition. |

**Potential harm**

The privacy-preserving path can remain optional indefinitely. Implementations may normalize M-DID reuse across relationships and VTCs, making correlation a de facto permanent property rather than a temporary bootstrap compromise.

**Recommended treatment**

Define when the bootstrap exception applies, what event ends it, whether new relationships may continue using M-DIDs after that point, and how an existing edge migrates or is re-issued without creating ambiguous duplicate relationships.

**Retest when**

- Bootstrapping and M-DID-to-R-DID migration semantics are made testable.

#### F-005 — ZKP-by-default guidance is not interoperable or conformance-testable without a proof profile

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Implementation Guidance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-CY01 — ZKP Implementation Failure](../../build/site/catalogue.html#RK-CY01) |
| Controls | [CT-27 — Audited ZKP Library Requirement](../../build/site/catalogue.html#CT-27), [CT-28 — ZKP Conformance Testing](../../build/site/catalogue.html#CT-28) |
| Guardrails | [GR-06 — Privacy-Preserving Proofing Option](../../build/site/catalogue.html#GR-06), [GR-07 — Uniqueness Enforcement Mechanism](../../build/site/catalogue.html#GR-07) |
| Assurance tests | [AT-06 — At least one ZKP / selective disclosure path is available and functional in Phase 4 UX](../../build/site/catalogue.html#AT-06), [AT-07 — Uniqueness enforcement mechanism is documented; if none exists, risk acceptance is signed …](../../build/site/catalogue.html#AT-07) |

**Evidence**

| Source | Observation |
|---|---|
| `spec/body.md#zero-knowledge-and-selective-disclosure` | The specification is intentionally format-agnostic and leaves detailed ZK protocols and registry-ZK interactions to future work. |
| `spec/body.md#privacy-considerations` | Implementations are encouraged to use ZKP presentation by default. |

**Potential harm**

Independent implementations can satisfy the prose while choosing incompatible proof systems, predicate semantics, freshness mechanisms or registry bindings. Privacy expectations can therefore diverge even when credential schemas interoperate.

**Recommended treatment**

Keep the credential specification proof-format agnostic, but normatively reference a companion ZKP/selective-disclosure profile before claiming interoperable ZKP behavior. The profile should define supported proof constructions, freshness/replay requirements, predicates, status checks and conformance vectors.

**Retest when**

- A DTG ZKP profile is normatively bound or equivalent interoperability requirements are added.

#### F-006 — Conformance needs a sharper boundary between schema validity and governance-qualified DTG meaning

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | Specification |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-G05 — Governanceless VTC Claiming Credential Compliance](../../build/site/catalogue.html#RK-G05), [RK-SC02 — Credential Schema Ambiguity](../../build/site/catalogue.html#RK-SC02) |
| Controls | [CT-18 — Normative Credential Schema Publication](../../build/site/catalogue.html#CT-18), [CT-19 — Conformance Test Suite](../../build/site/catalogue.html#CT-19), [CT-56 — VTC Governance Conformance Class](../../build/site/catalogue.html#CT-56) |
| Guardrails | [GR-01 — Genesis Policy Documentation](../../build/site/catalogue.html#GR-01), [GR-02 — Time-Bounded Initiator Authority](../../build/site/catalogue.html#GR-02) |
| Assurance tests | [AT-01 — Genesis policy artefact exists, is version-controlled, and was committed before any Phase …](../../build/site/catalogue.html#AT-01), [AT-02 — VTA PEP rejects Phase 2 invitation attempts after documented initiator authority expiry](../../build/site/catalogue.html#AT-02) |

**Evidence**

| Source | Observation |
|---|---|
| `spec/body.md#governance-considerations` | Most membership, invitation and identity-proofing policy is delegated to each VTC/VTN governance framework and trust registry. |
| `spec/body.md#conformance` | Conformance targets are defined for issuers, holders and verifiers, but no separate claim vocabulary distinguishes syntactic credential conformance from governance-qualified participation in a recognized VTC/VTN. |

**Potential harm**

A technically valid issuer can present a credential as "DTG compliant" even when the community has no legitimate governance, policy publication or recognized authority chain. Cryptographic validity can be confused with governance legitimacy.

**Recommended treatment**

Define conformance claim levels or terminology that separates schema/protocol conformance from governance-qualified trust semantics. State what evidence a verifier needs to establish that a VTC, VTN or role is recognized under the applicable governance framework and trust registry.

**Retest when**

- Conformance language explicitly separates technical validity from governance legitimacy.

#### F-007 — Supported decision-making, guardianship and power-of-attorney relationships are not representable

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Specification, Governance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-HX05 — Legal Capacity Architecture Gap — LPA / Guardianship Not Representable](../../build/site/catalogue.html#RK-HX05), [RK-SC05 — Credential Schema Gap — Supported Consent and LPA Not Representable](../../build/site/catalogue.html#RK-SC05) |
| Controls | [CT-57 — Supported Decision-Making Credential Extension](../../build/site/catalogue.html#CT-57), [CT-58 — Accessible Trust Task Ceremony UX for Cognitive Differences](../../build/site/catalogue.html#CT-58), [CT-59 — LPA Delegation Credential Type](../../build/site/catalogue.html#CT-59), [CT-60 — Secondary Notification Recipient Registration](../../build/site/catalogue.html#CT-60), [CT-66 — Children's Data Processing Impact Assessment Requirement](../../build/site/catalogue.html#CT-66) |
| Guardrails | [GR-19 — Supported Decision-Making and Legal Delegation Pathway](../../build/site/catalogue.html#GR-19) |
| Assurance tests | [AT-19 — For any VTC that has admitted or intends to admit participants under supported or substitu…](../../build/site/catalogue.html#AT-19) |

**Evidence**

| Source | Observation |
|---|---|
| `spec/body.md#base-structure` | The credential model identifies issuer and subject but has no representation/delegation semantics for a person acting with or for another person. |
| `spec/body.md#related-specifications` | Higher-layer trust-task and agent-card work is anticipated, but legal-capacity and supported-consent relationships are not assigned a concrete representation path in WD-01. |

**Potential harm**

Systems built only from the core credential types can assume that the subject is always the sole decision-maker and key controller. People using supported decision-making, an LPA or guardianship arrangement can be excluded or forced into non-standard workarounds that weaken accountability.

**Recommended treatment**

Assign representation and supported-consent semantics to a named companion specification and add a non-inference note to the core credentials: subject identity does not by itself establish legal capacity, exclusive control or absence of an authorized representative.

**Retest when**

- A concrete representation/delegation path is documented and linked from the credential specification.

#### F-008 — Organisational membership and relationship semantics are not explicit in the identifier model

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | Governance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [RK-EX05 — Organisational Identity Architecture Gap](../../build/site/catalogue.html#RK-EX05) |
| Controls | [CT-63 — Organisational Credential Type Definition](../../build/site/catalogue.html#CT-63), [CT-64 — Organisational Governance Conformance Mapping](../../build/site/catalogue.html#CT-64) |
| Guardrails | [GR-21 — Organisational Identity Governance Mapping](../../build/site/catalogue.html#GR-21) |
| Assurance tests | [AT-21 — For any regulated organisation admitted as a VTC member: (1) legal identifier and regulato…](../../build/site/catalogue.html#AT-21) |

**Evidence**

| Source | Observation |
|---|---|
| `spec/body.md#vmc-verifiable-membership-credential` | The VMC member subject is described as a person, device or agent; C-DID is reserved for VTC/VTN community membership cases. |
| `spec/body.md#vrc-verifiable-relationship-credential` | VRC issuer and subject rules are expressed in terms of R-DID or M-DID without stating how a non-community organisation participates as an organisation. |

**Potential harm**

Implementers may model organisations inconsistently as members, communities, agents or out-of-band identities. That ambiguity affects authorization, accountability, key rotation and staff/role changes.

**Recommended treatment**

State whether ordinary organisations are valid DTG entities and, if so, which DID class and credential semantics represent them. If organisational identity is intentionally out of scope, say so explicitly and identify the companion architecture required before organisational use cases can claim interoperability.

**Retest when**

- Organisational entity semantics are defined or explicitly delegated.

<!-- END GENERATED PRESSURE TEST -->

## What the pressure test found

### 1. Membership-edge directionality is a real schema contradiction

WD-01 says that a complete membership edge consists of two VMCs, one in each direction, while its normative VMC schema only defines the community-issued direction. This is not merely editorial because different implementations can make different choices about consent and edge completeness. The open upstream PR `trustoverip/dtgwg-cred-spec#12` proposes a direction-qualified member acknowledgement and therefore becomes evidence attached to F-001, not a reason to mark the finding resolved.

### 2. Membership must not silently become authority

The specification explicitly allows an agent to be the subject of a VMC. RAHP therefore tests the harmful inference that a verifier may treat that VMC as evidence of the agent's mandate. The pressure-test record recommends a semantic boundary: membership can recognize an agent node, but operator identity, accountability, delegation, autonomy, capabilities and current authority remain separately verifiable facts.

### 3. Lifecycle semantics need a technical contract even when due process remains governance

The draft has validity periods and tells verifiers to check applicable revocation through a trust registry, but it does not define a mandatory status discovery/profile contract or consistent failure semantics. RAHP separates two questions: **how a verifier determines status** belongs in interoperable technical semantics; **whether revocation was legitimate and what consequence follows** remains a governance question.

### 4. Privacy-by-default requires bounding the bootstrap exception

R-DIDs are the privacy-preserving relationship identifier, but M-DIDs remain allowed for bootstrapping and post-bootstrap migration is only recommended. Without a defined end condition or migration state, the exception can become permanent and cross-relationship correlation can become normal implementation behavior.

### 5. ZKP guidance needs a companion interoperability profile

The credential spec is right to remain proof-format agnostic, but `SHOULD`-style ZKP-by-default expectations cannot become interoperable behavior without a profile covering proof constructions, predicates, freshness/replay, status checks and test vectors. F-005 therefore routes primarily to a companion specification rather than forcing a specific cryptographic suite into the core credential schema.

### 6. Conformance should distinguish cryptographic/schema validity from governance legitimacy

The specification correctly says a cryptographically valid credential is not necessarily an authorized one. The remaining gap is claim language: an implementation should not be able to collapse "valid DTG-shaped credential" into "governance-qualified DTG trust assertion." F-006 recommends explicit conformance levels or terminology.

### 7. Legal representation and supported consent need an assigned architecture

The current issuer/subject model does not represent supported decision-making, guardianship or power-of-attorney relationships. That does not mean all legal-capacity semantics belong in this credential specification. It does mean the gap should have an explicit companion-specification route and the core model should avoid implying that subject identity proves exclusive capacity or control.

### 8. Organisational entity semantics should be explicit

The VMC text names person, device and agent members, while C-DID represents communities. An ordinary organisation is therefore easy to model inconsistently. F-008 asks the specification either to define the organisational entity path or to state that it is intentionally outside this layer and name the required companion architecture.

## Reproducing the review

Run the repository integrity validator and the pressure-test validator:

```bash
pip install -r requirements.txt
python3 tools/validate.py
python3 tools/render_pressure_tests.py
python3 tools/validate_pressure_tests.py
```

The second command validates every `examples/**/pressure-test.yaml` against the canonical RAHP identifiers and the controlled finding-disposition vocabulary. It fails if a finding cites a risk/control/guardrail/assurance test that does not exist, if a target is not pinned to a commit, or if required review metadata is missing.

## Re-testing after the specification changes

Do **not** overwrite the reviewed commit and silently keep the old findings. Re-run the review against the new target revision, then update each finding as `resolved`, `open`, `superseded` or `monitoring`, preserving upstream issue/PR references as evidence. This turns the example into a longitudinal assurance record rather than a static critique.

## Interpretation boundary

This is a RAHP pressure test, not a claim that every listed control must become normative text in `dtgwg-cred-spec`. Each finding records a primary disposition and, where necessary, secondary control planes. That is intentional: the purpose of RAHP is to expose harm pathways **and** put remediation where legitimate authority and effective enforcement actually exist.
