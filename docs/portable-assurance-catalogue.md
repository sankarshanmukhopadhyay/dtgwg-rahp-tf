---
layout: default
title: "Portable assurance catalogue"
parent: Reference
nav_order: 2
has_toc: true
---
# Portable assurance catalogue

RAHP v1.1 adds a **method-level assurance knowledge model** that can be reused across deployments without importing DTG, CAWG/C2PA or any other deployment's governance state. The catalogue is canonical in `method/catalogue/`; this page is a human-readable index.

For direct browsing, use the [portable assurance catalogue browser](../method/catalogue/). The generated assurance site also provides a [portable catalogue view](../build/site/portable-catalogue.html) and a [coverage/HEAD-qualification view](../build/site/assurance-graph.html). It provides generated Just-the-Docs views for each YAML catalogue while preserving the YAML files themselves as the canonical machine-readable sources. The compatibility route [`/method/catalog/`](../method/catalog/) points readers to the same catalogue.

The chain is:

```text
harm ← risk → control → guardrail / assurance test → evidence
```

Portable patterns describe reusable failure and assurance semantics. Deployment records remain local and may specialize or reference these patterns.


## Harm patterns

Canonical source: [`method/catalogue/harm-patterns.yaml`](../method/catalogue/harm-patterns.yaml)

### HRM-AUT-01 — Manipulation

A person or accountable principal is steered toward an outcome through materially misleading, asymmetric or exploitative influence.

| Field | Value |
|---|---|

| Family | Autonomy |



### HRM-AUT-02 — Coercion

A person faces material penalty, loss or threat unless they accept a system action, disclosure or decision.

| Field | Value |
|---|---|

| Family | Autonomy |



### HRM-AUT-03 — Loss of meaningful choice

Nominal consent or choice exists but practical alternatives, information or timing are insufficient for meaningful agency.

| Field | Value |
|---|---|

| Family | Autonomy |



### HRM-AUT-04 — Delegation beyond informed intent

A delegated actor performs or enables an action outside the principal’s reasonably understood mandate.

| Field | Value |
|---|---|

| Family | Autonomy |



### HRM-AUT-05 — Inability to withdraw or revoke

A person cannot effectively terminate consent, delegated authority, participation or continued processing.

| Field | Value |
|---|---|

| Family | Autonomy |



### HRM-ACC-01 — Wrongful exclusion

A legitimate person or organization is denied access, participation or recognition without a justified basis.

| Field | Value |
|---|---|

| Family | Access and inclusion |



### HRM-ACC-02 — Discriminatory burden

A rule or system imposes materially higher burdens on a protected, marginalized or structurally disadvantaged group.

| Field | Value |
|---|---|

| Family | Access and inclusion |



### HRM-ACC-03 — Accessibility failure

A legitimate participant cannot complete a required interaction because accessibility needs are not supported.

| Field | Value |
|---|---|

| Family | Access and inclusion |



### HRM-ACC-04 — Infrastructure dependency exclusion

Access depends on devices, networks, identity infrastructure or services unavailable to some legitimate participants.

| Field | Value |
|---|---|

| Family | Access and inclusion |



### HRM-PRV-01 — Unnecessary disclosure

Information beyond the minimum necessary is exposed to a party or system.

| Field | Value |
|---|---|

| Family | Privacy |



### HRM-PRV-02 — Linkability and correlation

Separate interactions can be linked to construct a broader profile of a person, organization or agent.

| Field | Value |
|---|---|

| Family | Privacy |



### HRM-PRV-03 — Inference beyond disclosed facts

Observed data or metadata enables sensitive conclusions not intentionally disclosed.

| Field | Value |
|---|---|

| Family | Privacy |



### HRM-PRV-04 — Persistent surveillance

System operation enables durable observation or reconstruction of activities across time or contexts.

| Field | Value |
|---|---|

| Family | Privacy |



### HRM-PRV-05 — Secondary use and context collapse

Information collected for one purpose or audience is reused in another materially different context.

| Field | Value |
|---|---|

| Family | Privacy |



### HRM-ECO-01 — Loss of economic opportunity

A system decision prevents or materially reduces access to employment, trade, finance or other economic participation.

| Field | Value |
|---|---|

| Family | Economic |



### HRM-ECO-02 — Fraudulent or misallocated liability

A person or organization bears financial or legal consequences for an action they did not authorize or control.

| Field | Value |
|---|---|

| Family | Economic |



### HRM-GOV-01 — Arbitrary decision

A consequential decision is taken without consistent rules, sufficient reasons or accountable authority.

| Field | Value |
|---|---|

| Family | Governance and due process |



### HRM-GOV-02 — Unavailable appeal or remedy

An affected party lacks a practical path to contest, correct or obtain remedy for an adverse outcome.

| Field | Value |
|---|---|

| Family | Governance and due process |



### HRM-GOV-03 — Unaccountable or captured authority

Decision power is exercised without effective oversight, contestability or independence.

| Field | Value |
|---|---|

| Family | Governance and due process |



### HRM-SEC-01 — Impersonation and false attribution

Actions or claims are attributed to the wrong person, organization or agent.

| Field | Value |
|---|---|

| Family | Security-mediated harm |



### HRM-SEC-02 — Unauthorized consequential action

A system performs a consequential action without current, sufficient authority from the accountable principal.

| Field | Value |
|---|---|

| Family | Security-mediated harm |



### HRM-SEC-03 — Denial or disruption of participation

Security or operational failure prevents legitimate use, continuity, recovery or participation.

| Field | Value |
|---|---|

| Family | Security-mediated harm |



### HRM-INF-01 — False provenance or trust inference

A party correctly observes an artefact or signature but infers legitimacy, endorsement, authority or quality that it does not establish.

| Field | Value |
|---|---|

| Family | Information integrity |



### HRM-SAF-01 — Physical or safeguarding exposure

Digital information or system action materially increases risk of physical harm, stalking, abuse or safeguarding failure.

| Field | Value |
|---|---|

| Family | Safety |



## Risk patterns

Canonical source: [`method/catalogue/risk-patterns.yaml`](../method/catalogue/risk-patterns.yaml)

### RKP-AUTH-01 — Possession mistaken for authority

Authentication, key possession or identity proof is treated as sufficient evidence that the actor is authorized for the requested action.

| Field | Value |
|---|---|

| Family | Authority and delegation |

| Harm Patterns | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-INF-01` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-AUTH-02 — Stale authority accepted

Authority is checked at an earlier lifecycle point and not re-evaluated when a consequential action occurs.

| Field | Value |
|---|---|

| Family | Authority and delegation |

| Harm Patterns | `HRM-AUT-05`, `HRM-SEC-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-AUTH-03 — Authority scope ambiguity

Purpose, audience, resource, action, value or time bounds are insufficiently defined or inconsistently interpreted.

| Field | Value |
|---|---|

| Family | Authority and delegation |

| Harm Patterns | `HRM-AUT-04`, `HRM-ECO-02`, `HRM-SEC-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-DEL-01 — Transitive delegation expansion

A downstream delegate receives or infers broader authority than the upstream principal granted.

| Field | Value |
|---|---|

| Family | Authority and delegation |

| Harm Patterns | `HRM-AUT-04`, `HRM-SEC-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-DEL-02 — Delegation provenance loss

An execution chain cannot demonstrate which principal authorized which delegate under what scope.

| Field | Value |
|---|---|

| Family | Authority and delegation |

| Harm Patterns | `HRM-GOV-02`, `HRM-ECO-02`, `HRM-SEC-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-DEL-03 — Revocation propagation failure

Withdrawal or suspension of delegated authority does not reach all parties or enforcement points before further action.

| Field | Value |
|---|---|

| Family | Authority and delegation |

| Harm Patterns | `HRM-AUT-05`, `HRM-SEC-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-GOV-01 — Concentrated governance authority

A single actor or tightly aligned group can set, change or enforce rules without independent constraint.

| Field | Value |
|---|---|

| Family | Governance and capture |

| Harm Patterns | `HRM-GOV-01`, `HRM-GOV-03` |

| Origin | governance |

| Scope | systemic |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-GOV-02 — Governance capture or collusion

Actors expected to provide independent oversight coordinate, collude or are commonly controlled.

| Field | Value |
|---|---|

| Family | Governance and capture |

| Harm Patterns | `HRM-GOV-03`, `HRM-ACC-02` |

| Origin | governance |

| Scope | systemic |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-GOV-03 — Rule change without safe transition

Policy or governance semantics change while old artefacts or dependent implementations remain active without migration rules.

| Field | Value |
|---|---|

| Family | Governance and capture |

| Harm Patterns | `HRM-GOV-01`, `HRM-SEC-03` |

| Origin | governance |

| Scope | cross-party |

| Temporal Mode | delayed |

| Reversibility | costly |

| Observability | detectable |



### RKP-GOV-04 — Responsibility fragmentation

No single accountable path exists for an adverse outcome that spans specifications, operators or trust domains.

| Field | Value |
|---|---|

| Family | Governance and capture |

| Harm Patterns | `HRM-GOV-02`, `HRM-ECO-02` |

| Origin | governance |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-ID-01 — Identity or role misbinding

Identity layers or roles are substituted or conflated, binding a claim or action to the wrong subject, issuer, holder, operator or principal.

| Field | Value |
|---|---|

| Family | Identity and attribution |

| Harm Patterns | `HRM-SEC-01`, `HRM-INF-01` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-ID-02 — Uniqueness assumption failure

A system assumes uniqueness or one-person/one-actor semantics without a defensible mechanism or stated limitation.

| Field | Value |
|---|---|

| Family | Identity and attribution |

| Harm Patterns | `HRM-GOV-03`, `HRM-ACC-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-ID-03 — Recovery enables takeover or exclusion

Recovery is absent, inaccessible or weak enough to enable account/identity takeover.

| Field | Value |
|---|---|

| Family | Identity and attribution |

| Harm Patterns | `HRM-ACC-01`, `HRM-SEC-01`, `HRM-SEC-03` |

| Origin | operations |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-DISC-01 — Discovery interpreted as endorsement

Presence in a discovery document, registry or directory is treated as certification, endorsement or sufficient trust.

| Field | Value |
|---|---|

| Family | Discovery and trust inference |

| Harm Patterns | `HRM-INF-01`, `HRM-SEC-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-DISC-02 — Stale discovery metadata

Cached or unrefreshed discovery metadata preserves obsolete endpoints, keys, capabilities, authority or status.

| Field | Value |
|---|---|

| Family | Discovery and trust inference |

| Harm Patterns | `HRM-SEC-01`, `HRM-SEC-03`, `HRM-INF-01` |

| Origin | operations |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-DISC-03 — Registry governance ambiguity

Relying parties cannot determine who may add, remove, suspend or correct registry entries and under what authority.

| Field | Value |
|---|---|

| Family | Discovery and trust inference |

| Harm Patterns | `HRM-GOV-03`, `HRM-INF-01` |

| Origin | governance |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-CRD-01 — Credential validity interpreted as authorization

A valid credential or proof is treated as permission for an action outside the credential’s actual claim semantics.

| Field | Value |
|---|---|

| Family | Credentials and claims |

| Harm Patterns | `HRM-SEC-02`, `HRM-INF-01` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-CRD-02 — Credential status or issuer authority staleness

Credential validity or issuer authority is evaluated using stale status, registry or governance state.

| Field | Value |
|---|---|

| Family | Credentials and claims |

| Harm Patterns | `HRM-SEC-02`, `HRM-SEC-03` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-CRD-03 — Credential context detachment

A credential bound to a task, ceremony, transaction or context is later reused as a free-standing assurance claim.

| Field | Value |
|---|---|

| Family | Credentials and claims |

| Harm Patterns | `HRM-INF-01`, `HRM-SEC-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-CRD-04 — Credential audience or purpose expansion

A credential or secondary credential is forwarded, reused or presented to a broader audience or purpose than intended.

| Field | Value |
|---|---|

| Family | Credentials and claims |

| Harm Patterns | `HRM-PRV-01`, `HRM-PRV-05`, `HRM-AUT-04` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-PRV-01 — Stable identifier correlation

Persistent identifiers allow interactions across relying parties or contexts to be correlated.

| Field | Value |
|---|---|

| Family | Privacy and inference |

| Harm Patterns | `HRM-PRV-02`, `HRM-PRV-04` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-PRV-02 — Composition fingerprinting

Individually minimal proofs or metadata become identifying or sensitive when combined.

| Field | Value |
|---|---|

| Family | Privacy and inference |

| Harm Patterns | `HRM-PRV-02`, `HRM-PRV-03` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-PRV-03 — Failure channel disclosure

Errors, diagnostics or status responses reveal sensitive attributes, classifications or relationship information.

| Field | Value |
|---|---|

| Family | Privacy and inference |

| Harm Patterns | `HRM-PRV-01`, `HRM-PRV-03` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-EXC-01 — Single-path participation exclusion

A system requires one identity, device, interaction or proofing path without a viable alternative for legitimate participants.

| Field | Value |
|---|---|

| Family | Inclusion and accessibility |

| Harm Patterns | `HRM-ACC-01`, `HRM-ACC-03`, `HRM-ACC-04` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-EXC-02 — Social or institutional privilege dependency

Access depends on pre-existing social, institutional or documentation privilege that is unevenly distributed.

| Field | Value |
|---|---|

| Family | Inclusion and accessibility |

| Harm Patterns | `HRM-ACC-01`, `HRM-ACC-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-AGT-01 — Agent goal or mandate drift

An autonomous actor optimizes or continues execution in ways that depart from the principal’s current purpose or constraints.

| Field | Value |
|---|---|

| Family | Agentic systems |

| Harm Patterns | `HRM-AUT-04`, `HRM-SEC-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-AGT-02 — Secondary credential transitivity

A credential obtained for one agent/task is forwarded or treated as authority for another without explicit onward delegation.

| Field | Value |
|---|---|

| Family | Agentic systems |

| Harm Patterns | `HRM-AUT-04`, `HRM-PRV-05`, `HRM-SEC-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-AGT-03 — Opaque execution accountability gap

Opaque internal execution is combined with insufficient external action provenance to reconstruct accountability.

| Field | Value |
|---|---|

| Family | Agentic systems |

| Harm Patterns | `HRM-GOV-02`, `HRM-ECO-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-OPS-01 — Dependency unavailability or stale fallback

A required registry, status, issuer, policy or network dependency is unavailable and fallback behavior is unsafe or undefined.

| Field | Value |
|---|---|

| Family | Operational resilience |

| Harm Patterns | `HRM-SEC-03`, `HRM-INF-01` |

| Origin | operations |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-OPS-02 — Replay or duplicate side effect

A valid request, proof or task can be replayed or retried in a way that repeats an externally consequential effect.

| Field | Value |
|---|---|

| Family | Operational resilience |

| Harm Patterns | `HRM-ECO-02`, `HRM-SEC-02` |

| Origin | implementation |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-OPS-03 — Cascading invalidation

Compromise, deregistration or withdrawal of a dependency invalidates many downstream artefacts without a safe continuity path.

| Field | Value |
|---|---|

| Family | Operational resilience |

| Harm Patterns | `HRM-ACC-01`, `HRM-SEC-03` |

| Origin | operations |

| Scope | systemic |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-RED-01 — Evidence insufficient for contestability

The system cannot produce durable evidence necessary to explain, contest or remedy a consequential outcome.

| Field | Value |
|---|---|

| Family | Accountability and redress |

| Harm Patterns | `HRM-GOV-02`, `HRM-ECO-02` |

| Origin | design |

| Scope | cross-party |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-COMP-01 — Cross-spec authority mismatch

Two specifications use compatible-looking identity or authorization concepts with materially different semantics.

| Field | Value |
|---|---|

| Family | Composition |

| Harm Patterns | `HRM-AUT-04`, `HRM-SEC-02`, `HRM-INF-01` |

| Origin | design |

| Scope | systemic |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-COMP-02 — Cross-spec lifecycle mismatch

Validity, status, expiry, revocation or freshness is evaluated at different lifecycle points across dependent specifications.

| Field | Value |
|---|---|

| Family | Composition |

| Harm Patterns | `HRM-AUT-05`, `HRM-SEC-02`, `HRM-SEC-03` |

| Origin | design |

| Scope | systemic |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-COMP-03 — Cross-system linkability

Composition across protocols exposes identifiers or metadata that defeat privacy separation present in each component.

| Field | Value |
|---|---|

| Family | Composition |

| Harm Patterns | `HRM-PRV-02`, `HRM-PRV-05` |

| Origin | design |

| Scope | systemic |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-COMP-04 — Policy or evidence boundary conflict

Dependent systems disagree about which artefact establishes completion, authority, status or an auditable fact.

| Field | Value |
|---|---|

| Family | Composition |

| Harm Patterns | `HRM-GOV-02`, `HRM-INF-01` |

| Origin | design |

| Scope | systemic |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-PE-01 — Infrastructure dependency capture

A critical governance or verification dependency is controlled by an actor that can extract rents, surveil participants or change access conditions.

| Field | Value |
|---|---|

| Family | Political economy |

| Harm Patterns | `HRM-GOV-03`, `HRM-PRV-04`, `HRM-ACC-04` |

| Origin | ecosystem |

| Scope | systemic |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



### RKP-PE-02 — Failure cost externalization

Operators or intermediaries capture benefits while harmed participants bear disproportionate remediation, exclusion or liability costs.

| Field | Value |
|---|---|

| Family | Political economy |

| Harm Patterns | `HRM-ECO-01`, `HRM-ECO-02`, `HRM-GOV-02` |

| Origin | ecosystem |

| Scope | systemic |

| Temporal Mode | immediate |

| Reversibility | costly |

| Observability | detectable |



## Control patterns

Canonical source: [`method/catalogue/control-patterns.yaml`](../method/catalogue/control-patterns.yaml)

### CTP-AUTH-01 — Separate authentication from authorization

Require an explicit authorization decision independent of identity, authentication, credential validity or discovery integrity.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-AUTH-01`, `RKP-CRD-01`, `RKP-DISC-01` |

| Control Function | constrain |



### CTP-AUTH-02 — Action-time authority evaluation

Evaluate current authority, status, expiry and revocation immediately before a consequential action.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-AUTH-02`, `RKP-CRD-02`, `RKP-COMP-02` |

| Evidence Patterns | `EVP-AUTH-01` |

| Control Function | prevent |



### CTP-AUTH-03 — Machine-readable authority envelope

Represent audience, action, resource, purpose, value, time and delegation bounds in a form that can be enforced.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-AUTH-03`, `RKP-DEL-01`, `RKP-AGT-01` |

| Evidence Patterns | `EVP-AUTH-02` |

| Control Function | constrain |



### CTP-DEL-01 — Delegation chain continuity

Preserve the originating principal and bounded authority envelope across each delegation hop.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-DEL-01`, `RKP-DEL-02`, `RKP-AGT-02`, `RKP-COMP-01` |

| Evidence Patterns | `EVP-DEL-01` |

| Control Function | constrain |



### CTP-DEL-02 — Revocation propagation

Distribute revocation/suspension rapidly to every enforcement point that can exercise delegated authority.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-DEL-03`, `RKP-AUTH-02` |

| Evidence Patterns | `EVP-DEL-02` |

| Control Function | interrupt |



### CTP-GOV-01 — Independent governance checks

Separate policy creation, approval, enforcement and appeal so no single actor can unilaterally control the full lifecycle.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-GOV-01`, `RKP-GOV-02`, `RKP-DISC-03` |

| Evidence Patterns | `EVP-GOV-01` |

| Control Function | constrain |



### CTP-GOV-02 — Versioned policy transition

Publish effective dates, migration rules, compatibility constraints and rollback/retirement handling for governance changes.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-GOV-03`, `RKP-COMP-02` |

| Evidence Patterns | `EVP-GOV-02` |

| Control Function | recover |



### CTP-GOV-03 — Cross-boundary responsibility map

Assign accountable owners and redress paths for outcomes that span protocols, operators or trust domains.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-GOV-04`, `RKP-RED-01`, `RKP-COMP-04` |

| Evidence Patterns | `EVP-RED-01` |

| Control Function | remediate |



### CTP-ID-01 — Explicit role binding

Bind subject, issuer, holder, operator, principal and relying-party roles explicitly and reject role substitution.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-ID-01`, `RKP-COMP-01` |

| Control Function | prevent |



### CTP-ID-02 — Recovery with takeover resistance

Provide accessible recovery with independent checks, notification, delay or quorum protections appropriate to impact.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-ID-03` |

| Evidence Patterns | `EVP-REC-01` |

| Control Function | recover |



### CTP-DISC-01 — Discovery non-inference rule

State and enforce that discoverability, signed metadata or registry presence does not itself establish authorization, certification or endorsement.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-DISC-01`, `RKP-CRD-01` |

| Control Function | constrain |



### CTP-DISC-02 — Discovery freshness and withdrawal

Define cache bounds, refresh rules, withdrawal semantics and stale-state behavior for discovery metadata.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-DISC-02`, `RKP-OPS-01` |

| Evidence Patterns | `EVP-OPS-01` |

| Control Function | detect |



### CTP-DISC-03 — Registry governance policy

Publish admission, update, suspension, removal, correction, audit and appeal authority for registry entries.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-DISC-03`, `RKP-GOV-01` |

| Evidence Patterns | `EVP-GOV-01` |

| Control Function | govern |



### CTP-CRD-01 — Context-bound credential use

Bind credential use to intended task, transaction, audience or purpose and reject detached reuse when context is material.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-CRD-03`, `RKP-CRD-04`, `RKP-OPS-02` |

| Control Function | constrain |



### CTP-CRD-02 — Status-as-of semantics

Define which status and authority state must be evaluated and at what time for issuance, presentation and action.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-CRD-02`, `RKP-COMP-02` |

| Evidence Patterns | `EVP-AUTH-01` |

| Control Function | detect |



### CTP-PRV-01 — Pairwise or scoped identifiers

Use context-scoped identifiers and minimize stable metadata where correlation is not required.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-PRV-01`, `RKP-COMP-03` |

| Control Function | prevent |



### CTP-PRV-02 — Composition privacy analysis

Evaluate privacy and inference risks for the combined disclosure set, not only each credential or artefact independently.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-PRV-02`, `RKP-COMP-03` |

| Evidence Patterns | `EVP-PRV-01` |

| Control Function | detect |



### CTP-PRV-03 — Privacy-safe failure responses

Limit errors and diagnostics to information necessary for remediation, with sensitive detail protected or authenticated.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-PRV-03` |

| Control Function | prevent |



### CTP-EXC-01 — Alternative participation path

Provide at least one viable alternative when the primary identity, device, accessibility or connectivity path excludes legitimate participants.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-EXC-01`, `RKP-EXC-02` |

| Evidence Patterns | `EVP-INCL-01` |

| Control Function | compensate |



### CTP-AGT-01 — Principal intent checkpoint

Require step-up confirmation or reauthorization for material scope expansion, high-impact action or changed conditions.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-AGT-01`, `RKP-AUTH-03` |

| Evidence Patterns | `EVP-AUTH-02` |

| Control Function | constrain |



### CTP-AGT-02 — Secondary credential non-transitivity

Do not forward or reuse secondary credentials across agents or purposes unless onward delegation is explicitly authorized.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-AGT-02`, `RKP-CRD-04` |

| Control Function | constrain |



### CTP-AGT-03 — External action provenance

Record externally consequential actions, active delegation reference, accountable actor, target, time and outcome without requiring private chain-of-thought.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-AGT-03`, `RKP-DEL-02`, `RKP-RED-01` |

| Evidence Patterns | `EVP-AUD-01` |

| Control Function | audit |



### CTP-OPS-01 — Safe dependency degradation

Define fail-closed, defer, bounded-cache or explicit risk-accepted behavior for unavailable dependencies.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-OPS-01`, `RKP-CRD-02` |

| Evidence Patterns | `EVP-OPS-01` |

| Control Function | contain |



### CTP-OPS-02 — Idempotency and anti-replay

Bind freshness/uniqueness to consequential requests and make retries idempotent where duplicate effects are unsafe.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-OPS-02`, `RKP-CRD-03` |

| Evidence Patterns | `EVP-OPS-02` |

| Control Function | prevent |



### CTP-OPS-03 — Dependency invalidation continuity plan

Define notification, re-verification, grace, replacement and rollback behavior when a dependency is compromised or withdrawn.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-OPS-03` |

| Evidence Patterns | `EVP-GOV-02` |

| Control Function | recover |



### CTP-RED-01 — Contestability evidence package

Preserve sufficient decision, policy, identity/authority and action evidence to support explanation, appeal and remediation.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-RED-01`, `RKP-GOV-04` |

| Evidence Patterns | `EVP-RED-01`, `EVP-AUD-01` |

| Control Function | audit |



### CTP-COMP-01 — Cross-spec semantic contract

Define ownership and exact semantics of identity, authority, status, completion and evidence facts at each specification seam.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-COMP-01`, `RKP-COMP-04` |

| Evidence Patterns | `EVP-COMP-01` |

| Control Function | prevent |



### CTP-COMP-02 — Cross-spec lifecycle test matrix

Test dependent specifications across issue, authorize, present, execute, revoke, retry, migrate and appeal timing boundaries.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-COMP-02`, `RKP-OPS-02` |

| Evidence Patterns | `EVP-COMP-01` |

| Control Function | detect |



### CTP-PE-01 — Dependency governance and exit assessment

Document control, funding, surveillance capability, switching cost, shutdown authority and exit paths for critical dependencies.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-PE-01`, `RKP-PE-02` |

| Evidence Patterns | `EVP-GOV-01` |

| Control Function | govern |



### CTP-RISK-01 — Control side-effect assessment

Assess whether a mitigation introduces, amplifies or redistributes other risks and require explicit disposition of material side effects.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-EXC-02`, `RKP-PRV-01`, `RKP-PE-02` |

| Evidence Patterns | `EVP-RISK-01` |

| Control Function | detect |



### CTP-ID-03 — Explicit uniqueness assurance

Where uniqueness is required, define the population, assurance mechanism, false-positive/false-negative limits and non-uniqueness fallback explicitly.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-ID-02` |

| Evidence Patterns | `EVP-RISK-01` |

| Control Function | constrain |



## Guardrail patterns

Canonical source: [`method/catalogue/guardrail-patterns.yaml`](../method/catalogue/guardrail-patterns.yaml)

### GRP-AUTH-01 — No authority by inference

A consequential action is authorized solely from authentication, possession, credential validity, discovery metadata or registry presence.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-AUTH-01`, `RKP-CRD-01`, `RKP-DISC-01` |

| Control Patterns | `CTP-AUTH-01`, `CTP-DISC-01` |

| Protected Interest | principal agency |



### GRP-AUTH-02 — Current authority required

A consequential action proceeds when required authority, revocation or status state cannot be established at the action boundary.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-AUTH-02`, `RKP-DEL-03` |

| Control Patterns | `CTP-AUTH-02`, `CTP-DEL-02` |

| Protected Interest | principal agency |



### GRP-DEL-01 — Delegation cannot silently expand

A delegate or downstream actor receives materially broader scope than was granted by the accountable principal.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-DEL-01`, `RKP-AUTH-03` |

| Control Patterns | `CTP-AUTH-03`, `CTP-DEL-01` |

| Protected Interest | principal agency |



### GRP-GOV-01 — No unilateral irreversible governance action

One actor can make an irreversible high-impact governance decision without defined independent check or later remedy.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-GOV-01`, `RKP-GOV-02` |

| Control Patterns | `CTP-GOV-01` |

| Protected Interest | due process |



### GRP-ID-01 — No role substitution

A verifier substitutes one identity/role layer for another without an explicit binding rule.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-ID-01` |

| Control Patterns | `CTP-ID-01` |

| Protected Interest | identity integrity |



### GRP-PRV-01 — No unnecessary disclosure

A required flow discloses information not necessary for the stated decision or function.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-PRV-02`, `RKP-PRV-03` |

| Control Patterns | `CTP-PRV-02`, `CTP-PRV-03` |

| Protected Interest | privacy |



### GRP-EXC-01 — No essential-service single path

A high-impact or essential participation path has no viable alternative for foreseeable legitimate users excluded by the primary mechanism.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-EXC-01` |

| Control Patterns | `CTP-EXC-01` |

| Protected Interest | equitable access |



### GRP-AGT-01 — No agent action beyond current mandate

An autonomous agent performs a consequential action outside the current bounded mandate.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-AGT-01`, `RKP-AGT-02` |

| Control Patterns | `CTP-AGT-01`, `CTP-AGT-02` |

| Protected Interest | principal agency |



### GRP-OPS-01 — No unsafe replay

A replay or retry can repeat an externally consequential side effect without a new authorized decision.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-OPS-02` |

| Control Patterns | `CTP-OPS-02` |

| Protected Interest | transaction integrity |



### GRP-RED-01 — No consequential decision without contestability evidence

A high-impact adverse decision is made without sufficient retained evidence and an accountable appeal/remedy path.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-RED-01`, `RKP-GOV-04` |

| Control Patterns | `CTP-RED-01`, `CTP-GOV-03` |

| Protected Interest | due process |



### GRP-COMP-01 — No implicit cross-spec semantic substitution

A fact established by one specification is treated as establishing a different authority, completion, identity or status fact in another without an explicit contract.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-COMP-01`, `RKP-COMP-04` |

| Control Patterns | `CTP-COMP-01` |

| Protected Interest | composition integrity |



### GRP-PE-01 — Critical dependency must have governed exit

A critical dependency can materially change access or surveillance conditions with no documented alternative, exit or governance response.

| Field | Value |
|---|---|

| Risk Patterns | `RKP-PE-01` |

| Control Patterns | `CTP-PE-01` |

| Protected Interest | institutional autonomy |



## Assurance patterns

Canonical source: [`method/catalogue/assurance-patterns.yaml`](../method/catalogue/assurance-patterns.yaml)

### ATP-AUTH-01 — Authentication/authorization separation test

Identity or credential validity alone never authorizes a consequential action.

| Field | Value |
|---|---|

| Control Patterns | `CTP-AUTH-01` |

| Guardrail Patterns | `GRP-AUTH-01` |

| Evidence Patterns | `EVP-AUTH-01` |

| Automation Level | automated |

| Assurance Level | A3 |



### ATP-AUTH-02 — Action-time revocation test

A revoked or expired authority cannot be exercised after the effective revocation/expiry boundary.

| Field | Value |
|---|---|

| Control Patterns | `CTP-AUTH-02`, `CTP-DEL-02`, `CTP-CRD-02` |

| Guardrail Patterns | `GRP-AUTH-02` |

| Evidence Patterns | `EVP-AUTH-01` |

| Automation Level | automated |

| Assurance Level | A3 |



### ATP-DEL-01 — Delegation attenuation test

Each downstream delegation is equal to or narrower than the authority received upstream.

| Field | Value |
|---|---|

| Control Patterns | `CTP-DEL-01`, `CTP-AUTH-03` |

| Guardrail Patterns | `GRP-DEL-01` |

| Evidence Patterns | `EVP-DEL-01` |

| Automation Level | automated |

| Assurance Level | A3 |



### ATP-DEL-02 — Delegation provenance reconstruction

An auditor can reconstruct principal, delegation chain, scope and action for a consequential event.

| Field | Value |
|---|---|

| Control Patterns | `CTP-DEL-01`, `CTP-AGT-03` |

| Evidence Patterns | `EVP-DEL-01`, `EVP-AUD-01` |

| Automation Level | assisted |

| Assurance Level | A3 |



### ATP-GOV-01 — Independent governance decision test

High-impact governance changes show required independent approval and immutable decision evidence.

| Field | Value |
|---|---|

| Control Patterns | `CTP-GOV-01` |

| Guardrail Patterns | `GRP-GOV-01` |

| Evidence Patterns | `EVP-GOV-01` |

| Automation Level | assisted |

| Assurance Level | A3 |



### ATP-GOV-02 — Policy migration test

Artefacts created under prior policy versions follow documented migration, compatibility and retirement rules.

| Field | Value |
|---|---|

| Control Patterns | `CTP-GOV-02` |

| Evidence Patterns | `EVP-GOV-02` |

| Automation Level | assisted |

| Assurance Level | A3 |



### ATP-ID-01 — Role-confusion negative test

Requests with mismatched principal, subject, holder, issuer or operator roles are rejected or escalated.

| Field | Value |
|---|---|

| Control Patterns | `CTP-ID-01`, `CTP-ID-02` |

| Guardrail Patterns | `GRP-ID-01` |

| Evidence Patterns | `EVP-AUTH-01` |

| Automation Level | automated |

| Assurance Level | A3 |



### ATP-DISC-01 — Discovery non-inference test

A signed or registered discovery record without separate authorization cannot unlock a protected action.

| Field | Value |
|---|---|

| Control Patterns | `CTP-DISC-01`, `CTP-DISC-03` |

| Guardrail Patterns | `GRP-AUTH-01` |

| Evidence Patterns | `EVP-AUTH-01` |

| Automation Level | automated |

| Assurance Level | A3 |



### ATP-DISC-02 — Discovery freshness test

Withdrawn or stale discovery metadata is not used beyond the documented freshness bound.

| Field | Value |
|---|---|

| Control Patterns | `CTP-DISC-02` |

| Evidence Patterns | `EVP-OPS-01` |

| Automation Level | automated |

| Assurance Level | A3 |



### ATP-PRV-01 — Composed disclosure review

The combined disclosure set is assessed for linkability, inference and unnecessary attributes.

| Field | Value |
|---|---|

| Control Patterns | `CTP-PRV-02`, `CTP-PRV-01`, `CTP-PRV-03` |

| Guardrail Patterns | `GRP-PRV-01` |

| Evidence Patterns | `EVP-PRV-01` |

| Automation Level | assisted |

| Assurance Level | A3 |



### ATP-EXC-01 — Alternative-path usability test

Representatively affected legitimate participants can complete an alternative path without materially worse unjustified burden.

| Field | Value |
|---|---|

| Control Patterns | `CTP-EXC-01` |

| Guardrail Patterns | `GRP-EXC-01` |

| Evidence Patterns | `EVP-INCL-01` |

| Automation Level | assisted |

| Assurance Level | A3 |



### ATP-AGT-01 — Agent mandate boundary test

Agent attempts outside purpose, resource, value, time or onward-delegation scope are blocked.

| Field | Value |
|---|---|

| Control Patterns | `CTP-AGT-01`, `CTP-AGT-02` |

| Guardrail Patterns | `GRP-AGT-01` |

| Evidence Patterns | `EVP-AUTH-02` |

| Automation Level | automated |

| Assurance Level | A3 |



### ATP-OPS-01 — Dependency outage test

Loss or staleness of a dependency triggers the documented safe degradation behavior.

| Field | Value |
|---|---|

| Control Patterns | `CTP-OPS-01`, `CTP-OPS-03` |

| Evidence Patterns | `EVP-OPS-01` |

| Automation Level | assisted |

| Assurance Level | A3 |



### ATP-OPS-02 — Replay/idempotency test

Replayed or retried requests do not repeat a protected side effect without fresh authorization.

| Field | Value |
|---|---|

| Control Patterns | `CTP-OPS-02` |

| Guardrail Patterns | `GRP-OPS-01` |

| Evidence Patterns | `EVP-OPS-02` |

| Automation Level | automated |

| Assurance Level | A3 |



### ATP-RED-01 — Contestability reconstruction test

An affected party and reviewer can reconstruct the consequential decision and identify an accountable remedy path.

| Field | Value |
|---|---|

| Control Patterns | `CTP-RED-01`, `CTP-GOV-03` |

| Guardrail Patterns | `GRP-RED-01` |

| Evidence Patterns | `EVP-RED-01`, `EVP-AUD-01` |

| Automation Level | assisted |

| Assurance Level | A3 |



### ATP-COMP-01 — Cross-spec semantic seam test

Each cross-spec fact has a named owner and is not silently substituted for another semantic fact.

| Field | Value |
|---|---|

| Control Patterns | `CTP-COMP-01`, `CTP-CRD-01` |

| Guardrail Patterns | `GRP-COMP-01` |

| Evidence Patterns | `EVP-COMP-01` |

| Automation Level | assisted |

| Assurance Level | A3 |



### ATP-COMP-02 — Cross-spec lifecycle matrix test

Composition behavior is tested across issuance, authorization, execution, revocation, retry, migration and appeal boundaries.

| Field | Value |
|---|---|

| Control Patterns | `CTP-COMP-02` |

| Evidence Patterns | `EVP-COMP-01` |

| Automation Level | assisted |

| Assurance Level | A3 |



### ATP-RISK-01 — Control side-effect test

Material privacy, exclusion, autonomy or political-economy side effects of a proposed mitigation are identified and dispositioned.

| Field | Value |
|---|---|

| Control Patterns | `CTP-RISK-01`, `CTP-ID-03` |

| Evidence Patterns | `EVP-RISK-01` |

| Automation Level | assisted |

| Assurance Level | A3 |



### ATP-PE-01 — Critical dependency exit test

A critical dependency has explicit control ownership, material-change monitoring, a governed response and a viable exit or substitution path.

| Field | Value |
|---|---|

| Control Patterns | `CTP-PE-01` |

| Guardrail Patterns | `GRP-PE-01` |

| Evidence Patterns | `EVP-GOV-01` |

| Automation Level | assisted |

| Assurance Level | A3 |



## Evidence patterns

Canonical source: [`method/catalogue/evidence-patterns.yaml`](../method/catalogue/evidence-patterns.yaml)

### EVP-AUTH-01 — Authorization decision trace

Shows identity/authentication inputs separately from current authorization/status evaluation.

| Field | Value |
|---|---|

| Freshness | per consequential decision |

| Privacy Classification | internal-assurance |



### EVP-AUTH-02 — Authority envelope fixture

Shows enforceable scope, purpose, audience, value, time and delegation limits plus negative vectors.

| Field | Value |
|---|---|

| Freshness | per assessment or event |

| Privacy Classification | internal-assurance |



### EVP-DEL-01 — Delegation chain trace

Binds principal, each delegate, authority attenuation and resulting action.

| Field | Value |
|---|---|

| Freshness | per consequential action |

| Privacy Classification | internal-assurance |



### EVP-DEL-02 — Revocation propagation trace

Shows revocation effective time and observation/enforcement time at each relevant enforcement point.

| Field | Value |
|---|---|

| Freshness | per revocation event |

| Privacy Classification | internal-assurance |



### EVP-GOV-01 — Governance decision record

Shows authority, reviewers, rationale, version, effective date and approvals for a governance decision.

| Field | Value |
|---|---|

| Freshness | per governance decision |

| Privacy Classification | internal-assurance |



### EVP-GOV-02 — Policy migration record

Shows affected versions, migration rules, compatibility tests, notifications and retirement/rollback state.

| Field | Value |
|---|---|

| Freshness | per material policy release |

| Privacy Classification | internal-assurance |



### EVP-REC-01 — Recovery ceremony evidence

Shows recovery checks, approvals, notification and replacement/invalidation events without exposing unnecessary secrets.

| Field | Value |
|---|---|

| Freshness | per recovery event |

| Privacy Classification | sensitive |



### EVP-OPS-01 — Dependency freshness/outage trace

Shows dependency state, freshness age, fallback path and resulting decision.

| Field | Value |
|---|---|

| Freshness | per outage or stale-state test |

| Privacy Classification | internal-assurance |



### EVP-OPS-02 — Replay/idempotency evidence

Shows duplicate identifiers, freshness checks and side-effect suppression for replay/retry vectors.

| Field | Value |
|---|---|

| Freshness | per assessment or event |

| Privacy Classification | internal-assurance |



### EVP-PRV-01 — Disclosure composition analysis

Records disclosed fields/metadata, audiences, correlation surfaces and minimization rationale for the composed transaction.

| Field | Value |
|---|---|

| Freshness | per flow/profile revision |

| Privacy Classification | sensitive |



### EVP-INCL-01 — Inclusive-path test record

Records representative accessibility/exclusion conditions, completion outcomes and burden comparison across alternate paths.

| Field | Value |
|---|---|

| Freshness | per major interaction release |

| Privacy Classification | sensitive |



### EVP-RED-01 — Appeal and remedy record

Binds adverse outcome, explanation evidence, appeal owner, timeline, decision and remedy.

| Field | Value |
|---|---|

| Freshness | per adverse decision |

| Privacy Classification | sensitive |



### EVP-AUD-01 — Consequential action audit record

Binds accountable actor, delegation/authority reference, action category, target, time and outcome without private reasoning.

| Field | Value |
|---|---|

| Freshness | per consequential action |

| Privacy Classification | sensitive |



### EVP-COMP-01 — Cross-spec contract test matrix

Records semantic ownership, lifecycle boundary cases, expected outcomes and tested revisions for a composition.

| Field | Value |
|---|---|

| Freshness | per composed baseline |

| Privacy Classification | internal-assurance |



### EVP-RISK-01 — Control side-effect assessment

Records risks mitigated, risks introduced/amplified, affected groups and explicit disposition.

| Field | Value |
|---|---|

| Freshness | per control design change |

| Privacy Classification | internal-assurance |


