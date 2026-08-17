---
layout: default
title: "A2A RAHP worked assessment"
nav_exclude: true
permalink: /examples/a2a/
---
# A2A Protocol v1.0 RAHP example

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This worked example applies the portable RAHP method to the Linux Foundation Agent2Agent (A2A) Protocol rather than to a DTG or CAWG specification.

The review intentionally distinguishes **protocol security that A2A already provides** from residual **trust, authority, delegation and operational-assurance boundaries**. A signed Agent Card is not treated as a weakness; the pressure test asks what a relying agent is entitled to infer from it. Likewise, A2A's push-notification security guidance is credited and then converted into an assurance test rather than re-described as an absent control.

The example also motivated five protocol-neutral RAHP risks (`RK-AI05` through `RK-AI09`), seven controls (`CT-67` through `CT-73`), four guardrails (`GR-22` through `GR-25`) and four assurance tests (`AT-22` through `AT-25`). These are deliberately reusable for other agent protocols and multi-agent systems.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `SR-A2A-001` |
| Status | complete |
| Title | Agent2Agent (A2A) Protocol v1.0.0 RAHP pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `a2aproject/A2A` |
| Target document | https://a2a-protocol.org/v1.0.0/specification/ |
| Target version | 1.0.0 |
| Target commit | `1eb4aa03b07589d3a00ce7deab0dde679120ed30` |
| Target source paths | `docs/specification.md`, `docs/topics/agent-discovery.md`, `docs/topics/enterprise-ready.md`, `docs/topics/streaming-and-async.md`, `docs/whats-new-v1.md` |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v1.1.0` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-16 |
| Engine/method revalidated on | 2026-08-17 |
| Original RAHP version | `v0.7.0+a2a-example` |
| Revalidation scope | v1.1 portable assurance catalogue mapping plus method/engine revalidation; pinned target revision unchanged |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/pressure-testing-a-spec.md` |
| Rule | Credit controls already present in A2A v1.0; add a new RAHP risk only where the reusable catalogue lacks the cross-agent trust boundary. |

### Review scope

**Included**

- Agent discovery and Agent Card trust semantics
- Authentication and authorization boundaries
- Multi-agent delegation and downstream actions
- Secondary credentials used during tasks
- Long-running tasks, streaming and push notifications
- Observability and cross-agent accountability

**Excluded**

- Source-code audit of A2A SDK implementations
- Cryptographic review of JWS, TLS or OAuth primitives
- Governance assessment of any specific public agent registry
- Conformance testing of a particular deployed agent

### Summary

| Measure | Value |
|---|---:|
| Findings | 6 |
| Open findings | 6 |
| Primary disposition: Specification | 1 |
| Primary disposition: Implementation Guidance | 2 |
| Primary disposition: Companion Specification | 2 |
| Primary disposition: Governance | 1 |

**Overall assessment**

A2A v1.0.0 has substantial protocol security foundations, including signed Agent Cards, authorization scoping, secure transport expectations and detailed push-notification guidance. The principal RAHP gaps are not basic transport-security omissions. They are trust-semantics and delegated-authority boundaries that emerge when independently operated agents discover one another, subcontract work, obtain secondary credentials and act asynchronously.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | A signed Agent Card can still be over-read as proof of authority or trust | High | open | Specification | [RK-AI05 — Capability Advertisement Misread as Authority](../../build/site/catalogue.html#RK-AI05) |
| `F-002` | Discovery trust and freshness remain deployment-governed across well-known, registry and direct modes | High | open | Governance | [RK-AI06 — Agent Discovery Substitution or Stale Metadata](../../build/site/catalogue.html#RK-AI06) |
| `F-003` | A2A task delegation does not by itself preserve the originating principal’s authority envelope across agent hops | High | open | Companion Specification | [RK-AI07 — Delegation Context Lost Across Agent Hops](../../build/site/catalogue.html#RK-AI07), [RK-AI01 — Agent Credential Scope Creep](../../build/site/catalogue.html#RK-AI01) |
| `F-004` | Out-of-band secondary credentials need an explicit non-transitivity boundary | High | open | Companion Specification | [RK-AI09 — Secondary Credential Authority Laundering](../../build/site/catalogue.html#RK-AI09), [RK-AI01 — Agent Credential Scope Creep](../../build/site/catalogue.html#RK-AI01) |
| `F-005` | Push notification security is well identified but requires deployment-level assurance evidence | High | open | Implementation Guidance | [RK-AI08 — Asynchronous Callback Trust Failure](../../build/site/catalogue.html#RK-AI08) |
| `F-006` | Opaque execution needs portable cross-agent action provenance without exposing private reasoning | Medium | open | Implementation Guidance | [RK-AI07 — Delegation Context Lost Across Agent Hops](../../build/site/catalogue.html#RK-AI07) |

### Detailed findings

#### F-001 — A signed Agent Card can still be over-read as proof of authority or trust

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | Implementation Guidance, Governance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | [P3 — Relying Party / Verifier](../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../build/site/catalogue.html#P5), [P6 — Registry / Discovery / Trust-Service Operator](../../build/site/catalogue.html#P6), [M1 — Aether](../../build/site/catalogue.html#M1) |
| Risks | [RK-AI05 — Capability Advertisement Misread as Authority](../../build/site/catalogue.html#RK-AI05) |
| Controls | [CT-68 — Capability-to-Authority Non-Inference Rule](../../build/site/catalogue.html#CT-68) |
| Guardrails | [GR-22 — Discovery Is Not Authority](../../build/site/catalogue.html#GR-22) |
| Assurance tests | [AT-22 — Discovery and capability metadata are integrity/freshness checked and the relying policy d…](../../build/site/catalogue.html#AT-22) |

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
| `docs/topics/agent-discovery.md#the-role-of-the-agent-card` | The Agent Card advertises identity/provider information, service endpoints, capabilities, authentication requirements and skills, and clients use it to determine suitability. |
| `docs/whats-new-v1.md#enterprise-ready-features` | A2A v1.0 adds JWS plus JSON Canonicalization for Agent Card signature verification, improving integrity and authenticity of the published metadata. |

**Potential harm**

A client may correctly verify who signed an Agent Card yet incorrectly infer that the signer is authorised for the requested action, accountable to the principal, certified to a particular assurance level, or entitled to exercise every advertised skill.

**Recommended treatment**

Add an explicit semantic non-inference rule: Agent Card integrity, identity/provider metadata, skills and capabilities describe an endpoint but do not by themselves establish delegated authority, operator accountability, assurance level or permission. Require those decisions to be made by the applicable authorization and trust policy.

**Retest when**

- The specification or normative security guidance explicitly separates signed capability advertisement from authority and trust decisions.

#### F-002 — Discovery trust and freshness remain deployment-governed across well-known, registry and direct modes

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | Implementation Guidance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | [P3 — Relying Party / Verifier](../../build/site/catalogue.html#P3), [P6 — Registry / Discovery / Trust-Service Operator](../../build/site/catalogue.html#P6), [M1 — Aether](../../build/site/catalogue.html#M1) |
| Risks | [RK-AI06 — Agent Discovery Substitution or Stale Metadata](../../build/site/catalogue.html#RK-AI06) |
| Controls | [CT-67 — Agent Discovery Integrity and Freshness Verification](../../build/site/catalogue.html#CT-67) |
| Guardrails | [GR-22 — Discovery Is Not Authority](../../build/site/catalogue.html#GR-22) |
| Assurance tests | [AT-22 — Discovery and capability metadata are integrity/freshness checked and the relying policy d…](../../build/site/catalogue.html#AT-22) |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-05`, `HRM-SEC-02`, `HRM-INF-01`, `HRM-SEC-01`, `HRM-SEC-03` |
| Risks | `RKP-AUTH-02`, `RKP-DEL-03`, `RKP-DISC-01`, `RKP-DISC-02` |
| Controls | `CTP-AUTH-02`, `CTP-DEL-02`, `CTP-DISC-01`, `CTP-DISC-02` |
| Guardrails | `GRP-AUTH-02`, `GRP-AUTH-01` |
| Assurance | `ATP-AUTH-02`, `ATP-DISC-01`, `ATP-DISC-02` |
| Evidence | `EVP-AUTH-01`, `EVP-DEL-02`, `EVP-OPS-01` |

**Evidence**

| Source | Observation |
|---|---|
| `docs/topics/agent-discovery.md#discovery-strategies` | A2A describes well-known URI, curated registry and direct/private discovery strategies; it states that the current specification does not prescribe a standard API for curated registries. |
| `docs/topics/agent-discovery.md#caching-considerations` | Agent Cards are cacheable and clients may apply a reasonable default cache duration when servers provide no caching headers. |

**Potential harm**

Two conforming deployments can apply materially different trust, registry-governance and freshness assumptions. A valid but stale or incorrectly trusted card can route a task to an obsolete endpoint or preserve outdated capabilities and security requirements.

**Recommended treatment**

Document a deployment trust profile that identifies accepted discovery authorities, signature/origin validation, cache/freshness bounds, withdrawal behavior and registry governance. Keep the registry API out of core A2A if desired, but make the relying-party trust decision explicit and testable.

**Retest when**

- A reusable discovery trust profile or equivalent implementation/governance guidance defines origin, freshness and registry trust requirements.

#### F-003 — A2A task delegation does not by itself preserve the originating principal’s authority envelope across agent hops

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Implementation Guidance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | [P1 — Principal / Rights-Bearing Party](../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../build/site/catalogue.html#P5), [M1 — Aether](../../build/site/catalogue.html#M1) |
| Risks | [RK-AI07 — Delegation Context Lost Across Agent Hops](../../build/site/catalogue.html#RK-AI07), [RK-AI01 — Agent Credential Scope Creep](../../build/site/catalogue.html#RK-AI01) |
| Controls | [CT-30 — Cryptographic Delegation Scope Constraints](../../build/site/catalogue.html#CT-30), [CT-52 — Agent Delegation Credential Requirement](../../build/site/catalogue.html#CT-52), [CT-69 — End-to-End Delegation Context Propagation](../../build/site/catalogue.html#CT-69), [CT-73 — Cross-Agent Action Provenance and Correlation](../../build/site/catalogue.html#CT-73) |
| Guardrails | [GR-12 — Agent Delegation Scope Constraint](../../build/site/catalogue.html#GR-12), [GR-13 — Agent Audit Logging](../../build/site/catalogue.html#GR-13), [GR-23 — Delegation Continuity Across Agent Boundaries](../../build/site/catalogue.html#GR-23) |
| Assurance tests | [AT-12 — Agent exceeding capability constraints rejected by VTA PEP; operator VMC revocation propag…](../../build/site/catalogue.html#AT-12), [AT-13 — Agent credential operations visible in operator audit log with all required fields](../../build/site/catalogue.html#AT-13), [AT-23 — A multi-agent delegation test proves that downstream agents cannot exceed the originating …](../../build/site/catalogue.html#AT-23) |

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
| `docs/specification.md#11-key-goals-of-a2a` | A2A explicitly supports collaboration and delegation between independent agents while preserving opaque execution. |
| `docs/topics/enterprise-ready.md#authorization` | Authorization is the A2A server’s responsibility and is specific to the agent implementation, data, backend resources and enterprise policy. |

**Potential harm**

An upstream agent can be authorised to perform a bounded task while a downstream agent sees only a technically valid request. Purpose, human approval conditions, resource limits, expiry, revocation and permitted delegation depth can be lost between hops.

**Recommended treatment**

Define or normatively reference a delegation-context profile/extension that can bind an A2A task to the originating principal and a bounded authority envelope. Preserve capability, purpose, resource scope, approvals, validity, revocation and delegation depth across downstream calls without requiring disclosure of private reasoning.

**Retest when**

- A2A or a companion profile defines interoperable delegation-context propagation and negative tests for excess downstream authority.

#### F-004 — Out-of-band secondary credentials need an explicit non-transitivity boundary

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | Implementation Guidance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | [P1 — Principal / Rights-Bearing Party](../../build/site/catalogue.html#P1), [P5 — Delegated Service / Agent Operator](../../build/site/catalogue.html#P5), [M1 — Aether](../../build/site/catalogue.html#M1) |
| Risks | [RK-AI09 — Secondary Credential Authority Laundering](../../build/site/catalogue.html#RK-AI09), [RK-AI01 — Agent Credential Scope Creep](../../build/site/catalogue.html#RK-AI01) |
| Controls | [CT-30 — Cryptographic Delegation Scope Constraints](../../build/site/catalogue.html#CT-30), [CT-72 — Secondary Credential Audience Purpose and Delegation Constraint](../../build/site/catalogue.html#CT-72) |
| Guardrails | [GR-12 — Agent Delegation Scope Constraint](../../build/site/catalogue.html#GR-12), [GR-25 — Secondary Credential Non-Transitivity](../../build/site/catalogue.html#GR-25) |
| Assurance tests | [AT-25 — A downstream service rejects a secondary credential when audience, purpose, resource, life…](../../build/site/catalogue.html#AT-25) |

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
| `docs/topics/enterprise-ready.md#authentication` | When an agent needs credentials for a different system during a task, the client obtains those credentials out of band and provides them to the A2A server to continue the task. |
| `docs/topics/enterprise-ready.md#authorization` | The remote agent is responsible for enforcing authorization before sensitive backend actions and is instructed to apply least privilege. |

**Potential harm**

A secondary credential can be technically valid yet broader than the task’s delegated authority. Without audience, purpose and delegation-depth binding, credential possession can be mistaken for permission to forward, exchange or reuse it with additional downstream agents.

**Recommended treatment**

Define a companion credential/delegation profile or implementation contract requiring audience, resource, purpose, lifetime and delegation-depth restrictions for secondary credentials, with an explicit rule that credentials are non-transitive unless the principal authorised onward delegation.

**Retest when**

- Secondary-credential guidance includes task/delegation binding and negative confused-deputy or token-forwarding tests.

#### F-005 — Push notification security is well identified but requires deployment-level assurance evidence

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | — |
| Personas | [P4 — Intermediary / Platform Operator](../../build/site/catalogue.html#P4), [P5 — Delegated Service / Agent Operator](../../build/site/catalogue.html#P5), [M1 — Aether](../../build/site/catalogue.html#M1), [M2 — Phantom](../../build/site/catalogue.html#M2) |
| Risks | [RK-AI08 — Asynchronous Callback Trust Failure](../../build/site/catalogue.html#RK-AI08) |
| Controls | [CT-70 — Callback Destination Ownership and Egress Validation](../../build/site/catalogue.html#CT-70), [CT-71 — Callback Authenticity Freshness and Task Binding](../../build/site/catalogue.html#CT-71) |
| Guardrails | [GR-24 — Asynchronous Callback Trust Boundary](../../build/site/catalogue.html#GR-24) |
| Assurance tests | [AT-24 — Callback tests reject prohibited destinations, unauthenticated senders, wrong-task events,…](../../build/site/catalogue.html#AT-24) |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-PRV-01`, `HRM-PRV-05`, `HRM-AUT-04`, `HRM-SEC-02`, `HRM-ECO-02`, `HRM-SEC-03` |
| Risks | `RKP-CRD-04`, `RKP-AGT-02`, `RKP-OPS-02`, `RKP-OPS-01` |
| Controls | `CTP-AGT-02`, `CTP-OPS-02`, `CTP-OPS-01` |
| Guardrails | `GRP-AGT-01`, `GRP-OPS-01` |
| Assurance | `ATP-AGT-01`, `ATP-OPS-02`, `ATP-OPS-01` |
| Evidence | `EVP-AUTH-02`, `EVP-OPS-02`, `EVP-OPS-01` |

**Evidence**

| Source | Observation |
|---|---|
| `docs/topics/streaming-and-async.md#security-considerations-for-push-notifications` | A2A warns against blindly trusting client-supplied webhook URLs because of SSRF and DDoS risks, and recommends allowlisting, ownership verification and egress controls. |
| `docs/topics/streaming-and-async.md#client-webhook-receiver-security-when-receiving-notifications-from-a2a-server` | The guidance requires authenticating the A2A server and discusses timestamps, unique IDs and key rotation to mitigate replay and impersonation. |

**Potential harm**

An implementation can advertise push support while failing to prove that callback destinations, sender identity, task binding, freshness and replay controls work under adversarial conditions.

**Recommended treatment**

Add a deployment assurance checklist/test profile covering prohibited callback destinations, destination ownership where applicable, authenticated sender identity, task/audience binding, expiry/freshness and replay rejection. Treat this primarily as implementation assurance, not a new wire-format requirement unless testing reveals an interoperability gap.

**Retest when**

- A2A implementation/conformance guidance includes callback SSRF, authentication, task-binding, freshness and replay negative vectors.

#### F-006 — Opaque execution needs portable cross-agent action provenance without exposing private reasoning

| Field | Value |
|---|---|
| Severity | Medium |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | Governance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | [P1 — Principal / Rights-Bearing Party](../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../build/site/catalogue.html#P3), [P5 — Delegated Service / Agent Operator](../../build/site/catalogue.html#P5), [M1 — Aether](../../build/site/catalogue.html#M1) |
| Risks | [RK-AI07 — Delegation Context Lost Across Agent Hops](../../build/site/catalogue.html#RK-AI07) |
| Controls | [CT-73 — Cross-Agent Action Provenance and Correlation](../../build/site/catalogue.html#CT-73) |
| Guardrails | [GR-13 — Agent Audit Logging](../../build/site/catalogue.html#GR-13), [GR-23 — Delegation Continuity Across Agent Boundaries](../../build/site/catalogue.html#GR-23) |
| Assurance tests | [AT-23 — A multi-agent delegation test proves that downstream agents cannot exceed the originating …](../../build/site/catalogue.html#AT-23) |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-AUT-04`, `HRM-SEC-02` |
| Risks | `RKP-DEL-01`, `RKP-AGT-01` |
| Controls | `CTP-DEL-01`, `CTP-AGT-01` |
| Guardrails | `GRP-DEL-01`, `GRP-AGT-01` |
| Assurance | `ATP-DEL-01`, `ATP-AGT-01` |
| Evidence | `EVP-DEL-01`, `EVP-AUTH-02` |

**Evidence**

| Source | Observation |
|---|---|
| `docs/topics/enterprise-ready.md#tracing-observability-and-monitoring` | A2A recommends distributed tracing, comprehensive task/correlation logging and auditing of significant agent actions. |
| `docs/specification.md#12-guiding-principles` | A2A intentionally permits opaque execution so agents need not expose internal thoughts, plans, memory or tool implementations. |

**Potential harm**

A multi-agent workflow can be operationally observable yet still lack evidence showing which principal authorised which agent, what scope was active, which approval boundary applied and which downstream action produced a material effect.

**Recommended treatment**

Define a portable action-provenance profile for externally consequential events: principal or accountable operator reference, agent identity, task/context IDs, delegation reference, action category, approval checkpoint, timestamp, downstream target and outcome. Do not require model chain-of-thought or private internal reasoning.

**Retest when**

- A2A implementation guidance or an extension profile defines reconstructable cross-agent action provenance independent of private model reasoning.

<!-- END GENERATED PRESSURE TEST -->

