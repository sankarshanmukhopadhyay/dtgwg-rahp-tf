---
layout: default
title: "DTG RAHP Risk Register v4 — historical workbook"
nav_exclude: true
has_toc: true
---

# DTG RAHP Risk Register v4

> **Historical artefact.** This is a reading projection of a retained RAHP workbook. It is preserved for provenance and is not a current canonical RAHP source.

[Download the original workbook](DTG_RAHP_Risk_Register_v4.xlsx){: .btn .btn-primary }

## Analysis & Conclusions

| DTG RAHP – Risk & Harm Register v3  \|  Harms Prevention Analysis & Conclusion... | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 |
|---|---|---|---|---|---|---|---|
| Working Draft · DTG Credentials Task Force · Derived from: VTC Bootstrapping ... |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| 1.  Headline Risk Statistics |  |  |  |  |  |  |  |
| Total risks identified | 35 across 10 RAHP risk categories (31 original + 4 new from DTG Credential Sp... |  |  |  |  |  |  |
| High severity risks | 20 of 31  (64%) |  |  |  |  |  |  |
| Medium severity risks | 11 of 31 |  |  |  |  |  |  |
| High severity AND high likelihood (priority action) | 4 risks — these are the immediate standards-development priorities |  |  |  |  |  |  |
| Controls defined | 56 controls (CT-01–CT-56) — 8 new controls added from DTG Credential Spec v0.... |  |  |  |  |  |  |
| Guardrails defined | 18 guardrails (GR-01–GR-18) — GR-18 (R-DID Migration Phase Gate) added from s... |  |  |  |  |  |  |
| Assurance tests defined | 18 assurance tests (AT-01–AT-18) — AT-18 (R-DID migration verification) added... |  |  |  |  |  |  |
| Risk categories with 100% High severity | AI Agents (4/4 High), Systemic (3/3 High) |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| 2.  The Five Most Critical Harm Types |  |  |  |  |  |  |  |
| C1. Trust Graph Integrity / Identity Fraud (combined) |  |  |  |  |  |  |  |
| Affects 9 High-severity risks across Identity, AI Agents, and Systemic catego... |  |  |  |  |  |  |  |
| C2. Human Rights Violations — Revocation, Exclusion, Surveillance |  |  |  |  |  |  |  |
| Affects 6 High-severity risks (RK-CR01, RK-HX02, RK-HX03, RK-EX01, RK-ID02, R... |  |  |  |  |  |  |  |
| C3. Governance Failure / Capture |  |  |  |  |  |  |  |
| Affects 7 High-severity risks across Governance, Identity, and Systemic. Gene... |  |  |  |  |  |  |  |
| C4. Privacy / Data Protection |  |  |  |  |  |  |  |
| Affects 5 risks (Medium–High). Over-disclosure in credential schemas, M-DID l... |  |  |  |  |  |  |  |
| C5. AI-Specific Attack Surface |  |  |  |  |  |  |  |
| All 4 AI Agent risks are rated High severity. The DTG architecture has no cur... |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| 3.  Top Guardrails by High-Risk Coverage (Most Important Phase Gates for Stan... |  |  |  |  |  |  |  |
| Rank | Guardrail ID | Guardrail Name | High Risks Addressed | Total Risks | Why It Matters for Standards | Category | Linked ATs |
| 1 | GR-06 | Privacy-Preserving Proofing Option | 8 | 8 | Highest risk coverage of any single guardrail (8 risks, 5 High). This is the ... | Human Experience / Technology | AT-06 |
| 2 | GR-09 | Privacy-Preserving Revocation Disclosure | 6 | 8 | Second-highest coverage (8 risks). Controls revocation-related privacy, cross... | Technology / Governance | AT-09 |
| 3 | GR-07 | Uniqueness Enforcement Mechanism | 4 | 5 | Blocks the Sybil / AI-mediated identity fraud cluster (5 risks, 4 High). The ... | Technology / Governance | AT-07 |
| 4 | GR-10 | Multi-Party Registry Write Authorisation | 3 | 4 | Protects against registry manipulation, state coercion, and trust graph captu... | Technology / Governance | AT-10 |
| 5 | GR-14 | Non-Human Actor Detection | 3 | 3 | Addresses the entire AI-mediated attack cluster (3 risks, all High). Currentl... | Technology / Governance | AT-14 |
| 6 | GR-03 | Trust Anchor Diversity Policy | 3 | 3 | Addresses anchor collusion, discriminatory vouching, and systemic graph captu... | Governance / Human Experience | AT-03 |
| 7 | GR-08 | Revocation Due Process | 2 | 4 | Addresses 4 risks across the revocation lifecycle (2 High, 2 Medium). Without... | Governance / Human Experience | AT-08 |
| 8 | GR-12 | Agent Delegation Scope Constraint | 2 | 2 | Addresses both AI agent High risks. No current DTG specification covers agent... | Technology / Governance | AT-12 |
|  |  |  |  |  |  |  |  |
| 4.  Top Controls by High-Risk Coverage (Priority Implementation Candidates fo... |  |  |  |  |  |  |  |
| Rank | Control ID | Control Name | Type | High Risks | Rationale for Standards Priority | × | × |
| 1 | CT-08 | Uniqueness Enforcement Mechanism | Technical | 3 | The single most important technical control. Addresses Sybil proliferation, A... |  |  |
| 2 | CT-34 | Behavioural Anomaly Detection for Non-Human Actors | Technical | 3 | Required before Phase 4 opens (per GR-14). Addresses AI-mediated Sybil genera... |  |  |
| 3 | CT-45 | Multi-Party Registry Write Authorisation | Technical | 3 | Protects the entire trust registry from single-point-of-failure attacks. A no... |  |  |
| 4 | CT-04 | Trust Anchor Diversity Policy | Governance | 3 | Required before Phase 2 opens. Simultaneously addresses anchor collusion, dis... |  |  |
| 5 | CT-09 | Vouching Pattern Anomaly Detection | Technical | 2 | Complements uniqueness enforcement. Detects coordinated Sybil vouching rings ... |  |  |
| 6 | CT-15 | Pseudonymous Per-VTC M-DID Design | Technical | 2 | Foundational privacy protection. Prevents cross-community profiling and reduc... |  |  |
| 7 | CT-24 | Privacy-Preserving Revocation Disclosure | Technical | 2 | Protects members from public identity exposure during revocation. Addresses b... |  |  |
| 8 | CT-30 | Cryptographic Delegation Scope Constraints | Technical | 2 | Required for safe AI agent participation in VTCs. No current standard address... |  |  |
| 9 | CT-32 | Agent Liveness Check on Operator VMC | Technical | 2 | Prevents stale agent access after operator revocation. A normative MUST for a... |  |  |
| 10 | CT-10 | Non-Discriminatory Admission Criteria | Governance | 2 | Equality law and human rights requirement simultaneously. Must be a normative... |  |  |
|  |  |  |  |  |  |  |  |
| 5.  Conclusions — Priority Requirements for DTG Credential Standards |  |  |  |  |  |  |  |
| REC-1  NORMATIVE: Uniqueness Enforcement as Phase-Gate |  |  |  |  |  |  |  |
| GR-07 and CT-08 must become normative MUST requirements in the DTG credential... |  |  |  |  |  |  |  |
| REC-2  NORMATIVE: AI Agent Governance as First-Class Specification Area |  |  |  |  |  |  |  |
| All four AI Agent risks are rated High severity. The DTG credential specifica... |  |  |  |  |  |  |  |
| REC-3  NORMATIVE: Privacy-Preserving Revocation as Core Specification Require... |  |  |  |  |  |  |  |
| GR-09 (Privacy-Preserving Revocation Disclosure) and CT-24 address 8 risks in... |  |  |  |  |  |  |  |
| REC-4  NORMATIVE: Non-Discriminatory Admission and Alternative Identity Proofing |  |  |  |  |  |  |  |
| RK-ID02 (Social Graph Privilege Exclusion) and RK-HX02 (Discriminatory Vouchi... |  |  |  |  |  |  |  |
| REC-5  NORMATIVE: Multi-Party Registry Write Authorisation |  |  |  |  |  |  |  |
| CT-45 and GR-10 address trust graph capture, state coercion, and registry man... |  |  |  |  |  |  |  |
| REC-6  RECOMMENDED: Formal Threat Model as Standards Deliverable |  |  |  |  |  |  |  |
| GR-16 and CT-48 require a formal threat model. The DTGWG should publish this ... |  |  |  |  |  |  |  |
| REC-7  RECOMMENDED: UX Design Principles as Normative Standards Annex |  |  |  |  |  |  |  |
| RK-NM01 is rated High severity and High likelihood — and the DTGWG itself ack... |  |  |  |  |  |  |  |
| REC-8  PROCESS: Mandatory Open Issues Resolution Before Phase 4 |  |  |  |  |  |  |  |
| GR-17 requires the four bootstrapping open issues to be formally resolved or ... |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| 6.  Key Findings from DTG Credential Specification v0.3 Review (March 2026) |  |  |  |  |  |  |  |
| 6a. What the spec gets right (reducing existing risks) |  |  |  |  |  |  |  |
| The R-DID MUST per-relationship (§5.2) reduces RK-ID05 likelihood from Medium... |  |  |  |  |  |  |  |
| 6b. New risks introduced by spec design choices |  |  |  |  |  |  |  |
| RK-SC03 (VRC Over-Disclosure): No normative requirement to use annotation cre... |  |  |  |  |  |  |  |
| 6c. Highest-priority gaps remaining after spec v0.3 |  |  |  |  |  |  |  |
| 1. Uniqueness enforcement (GR-07, CT-08) — completely absent from spec. 2. Re... |  |  |  |  |  |  |  |
| 6d. Spec commentary recommendation status |  |  |  |  |  |  |  |
| Critical (before Implementer's Draft): R1 (Non-Human §10), R2 (Uniqueness lev... |  |  |  |  |  |  |  |

## Risk & Harm Register

| DTG RAHP – Risk & Harm Register v4  \|  Affected Personas replaced by Affected... |
|---|

## Controls Catalogue

| DTG RAHP – Controls Catalogue  \|  CT-01–CT-48  \|  Risk-reducing measures (NOT... | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 |
|---|---|---|---|---|---|---|---|
| Control Types: Technical · Governance · Procedural · UX · Legal  \|  Standards... |  |  |  |  |  |  |  |
| Control ID | Control Name | Type | Description | Linked Guardrail<br>(if underpins one) | Linked Risk IDs | Standards<br>Relevance | Priority Rationale |
| CT-01 | Version-Controlled Public Genesis Policy | Procedural | All Phase 1 bootstrapping policies must be committed to a public, version-con... | GR-01 | RK-G01 | High |  |
| CT-02 | Independent Governance Review at Genesis | Governance | An independent review of bootstrap policies by parties other than the initiat... | — | RK-G01 | High |  |
| CT-03 | Governance Transition Milestones | Governance | Explicit milestones for transitioning initiator authority to the governing bo... | GR-02 | RK-G02 | High |  |
| CT-04 | Trust Anchor Diversity Policy | Governance | A minimum diversity standard for trust anchors — geographic, organisational, ... | GR-03 | RK-G03, RK-SY01 | High |  |
| CT-05 | Anchor Clustering Metric Monitoring | Technical | The VTA tracks an anchor clustering metric (e.g. organisational or jurisdicti... | — | RK-G03 | Medium |  |
| CT-06 | Governance Capacity Planning | Procedural | The governing body must conduct annual capacity planning for admission, appea... | — | RK-G04 | Medium |  |
| CT-07 | Complaint / Appeals Rate-Limiting | Technical | The VTA or governance portal enforces rate-limiting on complaint and appeal s... | GR-15 | RK-G04, RK-SY02 | High |  |
| CT-08 | Uniqueness Enforcement Mechanism | Technical | A documented uniqueness enforcement mechanism must be in place before Phase 4... | GR-07 | RK-ID01, RK-AI03, RK-SY03 | High |  |
| CT-09 | Vouching Pattern Anomaly Detection | Technical | The VTA or a monitoring layer analyses vouching patterns for statistical anom... | — | RK-ID01, RK-SY01 | High |  |
| CT-10 | Non-Discriminatory Admission Criteria | Governance | Admission criteria must be published, non-discriminatory, and reviewed agains... | GR-06 | RK-ID02, RK-HX02 | High |  |
| CT-11 | Alternative Identity Proofing Paths | Procedural | At least one admission pathway must not require conventional government-issue... | GR-06 | RK-ID02 | High |  |
| CT-12 | IDVP Security Approval Criteria | Governance | IDVPs must meet documented security and operational standards — including bre... | GR-05 | RK-ID03 | High |  |
| CT-13 | IDVP Deregistration Handling Protocol | Procedural | The governing body must define how member VMCs issued via a deregistered IDVP... | — | RK-ID03 | High |  |
| CT-14 | DID Document Integrity Verification | Technical | The VTA must verify DID document integrity cryptographically before accepting... | GR-10 | RK-ID04 | High |  |
| CT-15 | Pseudonymous Per-VTC M-DID Design | Technical | Personal network managers should generate a distinct M-DID per VTC, and regis... | GR-09 | RK-ID05, RK-HX01 | High |  |
| CT-16 | Minimum-Necessary IDVC Attribute Set | Governance | A defined minimum-necessary IDVC attribute set must be published before Phase... | GR-06 | RK-SC01 | High |  |
| CT-17 | Data Minimisation Audit | Procedural | An annual data minimisation audit of all credential schemas (VRC, VMC, IDVC) ... | — | RK-SC01 | Medium |  |
| CT-18 | Normative Credential Schema Publication | Technical | Normative credential schemas for VRC, VMC, and IDVC must be published before ... | GR-01 | RK-SC02 | High |  |
| CT-19 | Conformance Test Suite | Technical | A conformance test suite for VTA and personal network manager implementations... | — | RK-SC02 | High |  |
| CT-20 | Sovereign Wallet UX Design Principles | UX | UX design principles for sovereign wallets must be defined, addressing task-b... | GR-06 | RK-NM01 | High |  |
| CT-21 | Non-Technical User Onboarding Testing | UX | Structured user testing with non-technical participants must be conducted bef... | — | RK-NM01 | Medium |  |
| CT-22 | Key Recovery Mechanism | Technical | A key recovery mechanism — e.g. social recovery quorum, hardware backup — mus... | — | RK-NM02 | High |  |
| CT-23 | Mandatory Pre-Revocation Notice | Governance | No VMC shall be revoked without prior written notice to the member, including... | GR-08 | RK-CR01 | High |  |
| CT-24 | Privacy-Preserving Revocation Disclosure | Technical | Revocation status must not be publicly linked to a member's real-world identi... | GR-09 | RK-CR01, RK-HX03 | High |  |
| CT-25 | Credential Renewal Workflow | Technical | A defined credential renewal workflow — including advance expiry notification... | — | RK-CR02 | Medium |  |
| CT-26 | VTC-Scoped Revocation | Technical | Revocation must be explicitly scoped to the issuing VTC only. Cross-VTC revoc... | GR-09 | RK-CR03 | High |  |
| CT-27 | Audited ZKP Library Requirement | Technical | Only ZKP implementations that have undergone formal security review or are fr... | GR-06 | RK-CY01 | High |  |
| CT-28 | ZKP Conformance Testing | Technical | A conformance test suite for ZKP implementations must be developed as part of... | GR-07 | RK-CY01 | High |  |
| CT-29 | Algorithm Agility and Migration Pathway | Technical | VTC credential schemas must be designed for algorithm agility. A quantum-read... | GR-16, GR-17 | RK-CY02 | Medium |  |
| CT-30 | Cryptographic Delegation Scope Constraints | Technical | AI agent delegation credentials must cryptographically encode explicit capabi... | GR-12 | RK-AI01 | High |  |
| CT-31 | Short-Lived Agent Credentials | Technical | AI agent delegation credentials should be short-lived (recommended: maximum 2... | GR-13 | RK-AI01 | High |  |
| CT-32 | Agent Liveness Check on Operator VMC | Technical | Before executing any delegated credential operation, an AI agent must verify ... | GR-12 | RK-AI02 | High |  |
| CT-33 | Non-Human Activity Rate-Limiting | Technical | The VTA and governance portal must enforce rate-limiting on admission request... | GR-14 | RK-AI03, RK-AI04 | High |  |
| CT-34 | Behavioural Anomaly Detection for Non-Human Actors | Technical | A behavioural anomaly detection layer must be deployed before Phase 4 to iden... | GR-14 | RK-AI03, RK-SY01 | High |  |
| CT-35 | Anchor Awareness of AI Social Engineering | Procedural | Community trust anchors must receive training on AI-powered social engineerin... | — | RK-AI04 | Medium |  |
| CT-36 | Out-of-Band Verification for High-Stakes Vouching | Procedural | For Phase 2 trust anchor admission and Phase 3 high-trust vouching, anchors s... | — | RK-AI04 | Medium |  |
| CT-37 | Jurisdictional Diversity of Key Parties | Governance | The governing body must document the jurisdictional distribution of trust anc... | GR-11 | RK-EX01 | High |  |
| CT-38 | Legal Coercion Response Protocol | Procedural | A documented legal coercion response protocol must be in place for trust anch... | — | RK-EX01 | High |  |
| CT-39 | Distributed Registry Architecture | Technical | The VTC trust registry must be deployed with geographic redundancy and a defi... | GR-10 | RK-EX02 | Medium |  |
| CT-40 | Legal Review of Credential Schemas | Legal | A legal review of all credential schemas and trust registry designs against a... | GR-06 | RK-EX03 | High |  |
| CT-41 | Open Issues Regulatory Risk Acceptance | Governance | Each of the four VTC Bootstrapping Draft open issues must have an explicit re... | GR-17 | RK-EX03 | High |  |
| CT-42 | Anonymous Membership Option | Technical | For VTCs operating in politically sensitive contexts, an anonymous membership... | GR-09 | RK-HX01 | Medium |  |
| CT-43 | Governing Body Accountability for Systematic Exclusion | Governance | The governing body must track admission denial rates by demographic proxy whe... | — | RK-HX02 | Medium |  |
| CT-44 | Remediation Pathway After Overturned Revocation | Governance | Where a revocation is overturned on appeal, a documented remediation pathway ... | — | RK-HX03 | Medium |  |
| CT-45 | Multi-Party Registry Write Authorisation | Technical | Trust registry writes must require multi-party or threshold authorisation (e.... | GR-10 | RK-SY01, RK-EX01 | High |  |
| CT-46 | Coordinated Behaviour Detection in Governance | Technical | The complaints and appeals workflow must include coordinated behaviour detect... | GR-15 | RK-SY02 | Medium |  |
| CT-47 | Formal Open Issues Mitigation Plan | Governance | Each of the four VTC Bootstrapping Draft open issues must have a formal mitig... | GR-17 | RK-SY03 | High |  |
| CT-48 | Threat Model Maintenance | Governance | A formal VTC threat model must be published, reviewed, and updated at least a... | GR-16 | RK-SY03, RK-CY02 | High |  |
| CT-49 | VRC Data Minimisation Clause | Technical | The VRC `credentialSubject` SHOULD contain only the minimum claims necessary ... | GR-06 | RK-SC03, RK-HX01, RK-ID05 | High |  |
| CT-50 | M-DID to R-DID Migration Trigger | Governance | VTC implementations MUST define and publish a normative trigger for migration... | GR-18 | RK-SC04, RK-ID05, RK-HX01 | High |  |
| CT-51 | Non-Human DID Designation in DID Document | Technical | Agent DIDs MUST be designated as non-human in the DID Document using a define... | GR-12 | RK-AI01, RK-AI03 | High |  |
| CT-52 | Agent Delegation Credential Requirement | Technical | An AI agent operating on behalf of a human VTC member MUST hold a delegation ... | GR-12 | RK-AI01, RK-AI02 | High |  |
| CT-53 | VIC Role Embedding (membershipRole field) | Technical | The VIC `credentialSubject` SHOULD include a `membershipRole` field specifyin... | GR-01 | RK-G01, RK-SC02 | High |  |
| CT-54 | VWC Requirement for High-Stakes Anchor Admission | Technical | For Phase 2 trust anchor admission, VTC governance SHOULD require that VRCs u... | GR-14 | RK-AI04, RK-ID01 | High |  |
| CT-55 | VEC Issuer Co-Membership Requirement | Governance | VTC implementations SHOULD require that Endorsement Credential (VEC per spec ... | GR-03 | RK-CR04, RK-SY02 | Medium |  |
| CT-56 | VTC Governance Conformance Class | Governance | A VTC claiming DTG credential specification compliance MUST publish a version... | GR-01 | RK-G05, RK-G01, RK-G02 | High |  |

## Guardrails Register

| DTG RAHP – Guardrails Register  \|  GR-01–GR-17  \|  Non-negotiable phase-gate pre-conditions (distinct from controls) | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 |
|---|---|---|---|---|---|---|---|---|
| A Guardrail is a binary pass/fail pre-condition that must be satisfied before a phase opens or a capability is activated. Failure to meet a guardrail must block progress, not merely trigger risk-reduction. |  |  |  |  |  |  |  |  |
| Guardrail ID | Guardrail Name | Category | Description / Requirement | Applies to Phase | Owner | Risks Addressed | Underpinning Controls | Assurance Test |
| GR-01 | Genesis Policy Documentation | Governance | All Phase 1 bootstrapping policies must be version-controlled, publicly readable, and committed to an auditable record before the initiator issues any Phase 2 invitations. Hard-coded policy changes require documented governance approval. | Phase 1 (all subsequent phases) | Initiator / Governing Body | RK-G01, RK-SC02, RK-NM02 | CT-01, CT-18 | AT-01 |
| GR-02 | Time-Bounded Initiator Authority | Governance | Initiator authority must be explicitly time-bounded or role-transitioned under documented governance rules. The VTA PEP must enforce the initiator count limit and refuse Phase 2 actions after authority expiry. | Phase 1–2 | VTA PEP / Governing Body | RK-G01, RK-G02 | CT-03 | AT-02 |
| GR-03 | Trust Anchor Diversity Policy | Governance / Human Experience | A minimum diversity standard for trust anchors must be defined and documented before Phase 2 seeding. The VTA must enforce the anchor count limit. Homogeneous anchor clusters constitute a policy violation. | Phase 2 | Governing Body | RK-G03, RK-HX02, RK-SY01 | CT-04, CT-05 | AT-03 |
| GR-04 | Reciprocal VRC Requirement | Technology / Governance | No VMC shall be issued to a trust anchor or member without a verified reciprocal VRC exchange. The VTA PEP must reject VMC issuance where only a unilateral VRC exists. | Phase 2–4 | VTA PEP | RK-ID01 | CT-08 | AT-04 |
| GR-05 | IDVP Registry Standing | Technology / Governance | IDVCs are only valid for VTC admission if issued by an IDVP whose DID is listed in the VTC trust registry with the role of identity verification provider at the time of presentation. | Phase 4 | VTA PEP / Governing Body | RK-ID03 | CT-12 | AT-05 |
| GR-06 | Privacy-Preserving Proofing Option | Human Experience / Technology | At least one privacy-preserving alternative to raw IDVC disclosure (ZKP, selective disclosure) must be available for Phase 4 admission. No applicant should be required to disclose more data than strictly necessary. | Phase 4 | VTA PEP / DPO | RK-ID02, RK-ID05, RK-SC01, RK-NM01, RK-CY01, RK-EX03, RK-HX01, RK-HX02 | CT-10, CT-11, CT-15, CT-16, CT-20, CT-27, CT-40 | AT-06 |
| GR-07 | Uniqueness Enforcement Mechanism | Technology / Governance | The VTC must define and document its uniqueness enforcement mechanism before Phase 4 opens. Absence of a uniqueness mechanism at scale is an open issue and constitutes a known risk that must be risk-accepted or mitigated. | Phase 4 (open issue) | Governing Body / Security | RK-ID01, RK-CY01, RK-AI03, RK-SY01, RK-SY03 | CT-08, CT-28 | AT-07 |
| GR-08 | Revocation Due Process | Governance / Human Experience | No VMC shall be revoked without prior notice to the member, a documented rationale, and access to a formal appeals process with defined timelines. Revocation criteria must be published in the governance framework. | Revocation | Governing Body / VTA | RK-G04, RK-CR01, RK-CR02, RK-HX03 | CT-23, CT-25 | AT-08 |
| GR-09 | Privacy-Preserving Revocation Disclosure | Technology / Governance | Revocation status must not be publicly linked to member real-world identity by default. ZKP-based or status-list approaches should be used. Cross-VTC contamination must be explicitly scoped and documented. | Revocation | VTA PEP / DPO | RK-ID03, RK-ID05, RK-SC01, RK-CR01, RK-CR03, RK-EX03, RK-HX01, RK-HX03 | CT-15, CT-24, CT-26, CT-42 | AT-09 |
| GR-10 | Multi-Party Registry Write Authorisation | Technology / Governance | Trust registry writes must require multi-party or threshold authorisation. No single actor shall have unilateral write access. All registry writes must be logged in a tamper-evident audit trail. | All phases | Registry Operator / Governing Body | RK-ID04, RK-EX01, RK-EX02, RK-SY01 | CT-14, CT-45 | AT-10 |
| GR-11 | Jurisdictional Diversity for Key Parties | Governance | The VTC governance framework must document the jurisdictional distribution of trust anchors and IDVPs, and assess the risk of any single jurisdiction having coercive legal leverage over a controlling majority of key parties. | Phase 2–4 (ongoing) | Governing Body | RK-G03, RK-EX01 | CT-37 | AT-11 |
| GR-12 | Agent Delegation Scope Constraint | Technology / Governance | AI agents operating on behalf of VTC members must hold cryptographically scoped delegation credentials with explicit capability constraints. Operator revocation of a VMC must propagate to agent credential invalidation within an agreed latency SLA. | Agent Lifecycle | VTA PEP / Operator | RK-AI01, RK-AI02 | CT-30, CT-31, CT-32 | AT-12 |
| GR-13 | Agent Audit Logging | Technology / Governance | All credential operations performed by an AI agent must be logged with sufficient detail to distinguish them from human operations, including agent DID, delegation credential reference, timestamp, and action type. | Agent Lifecycle | VTA / Operator | RK-AI01 | CT-31 | AT-13 |
| GR-14 | Non-Human Actor Detection | Technology / Governance | Rate-limiting and behavioural anomaly detection for non-human activity patterns must be in place before Phase 4 opens. Governance rules must explicitly address agent-mediated attacks. | Phase 4 + Agent Lifecycle | Security / Governing Body | RK-AI03, RK-AI04, RK-SY01 | CT-33, CT-34 | AT-14 |
| GR-15 | Complaint and Appeals Rate-Limiting | Governance / Human Experience | The complaints and appeals process must include rate-limiting controls to prevent bad-faith flooding, without suppressing legitimate grievances. Anti-retaliation protections for legitimate complainants must be documented. | Governance Operations | Governing Body | RK-G04, RK-SY02 | CT-07, CT-46 | AT-15 |
| GR-16 | Formal Threat Model Publication | Governance | A formal VTC threat model covering Sybil attacks, state coercion, anchor collusion, AI-mediated attacks, registry manipulation, and CIB must be published and reviewed before Phase 4 opens and at least annually thereafter. | Pre-Phase 4 / Ongoing | Security / Governing Body | RK-CY02, RK-EX02, RK-SY02 | CT-48 | AT-16 |
| GR-17 | Open Issues Risk Acceptance | Governance | The four open issues from the VTC Bootstrapping Draft — uniqueness, trust task protocols, expiration/revocation, DID document storage — must each be either mitigated or formally risk-accepted by the governing body before Phase 4 opens. | Phase 4 (pre-condition) | Governing Body | RK-CY02, RK-EX03, RK-SY03 | CT-41, CT-47 | AT-17 |
| GR-18 | R-DID Migration Phase Gate | Technology / Governance | Before Phase 4 opens (or before the VTC exceeds a governance-defined membership threshold, whichever comes first), the VTC MUST complete migration from M-DID-based to R-DID-based VRC edges, or formally risk-accept the residual linkability exposure with a documented rationale and review date. The migration trigger MUST be recorded in the trust registry. New VRCs issued after the trigger MUST use R-DIDs. This guardrail converts the spec's §5.2 privacy RECOMMENDATION ('migration recommended post-bootstrapping') into a binding phase gate, closing the residual window identified in RK-SC04. **Source:** DTG Credential Spec v0.3 §5.2 Privacy Considerations. | Pre-Phase 4 | VTA PEP / Governing Body | RK-SC04, RK-ID05, RK-HX01 | CT-50 | AT-18 |

## Assurance Tests

| DTG RAHP – Assurance Tests  \|  AT-01–AT-17  \|  Binary pass/fail evidence that each Guardrail is met | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 |
|---|---|---|---|---|---|---|
| AT ID | Linked Guardrail | Pass Criterion | Verification Method | Test Type | Risks Covered | Notes |
| AT-01 | GR-01 | Genesis policy artefact exists, is version-controlled, and was committed before any Phase 2 invitation was issued | Verify via audit trail timestamp comparison — automated | Governance | RK-G01, RK-SC02, RK-NM02 |  |
| AT-02 | GR-02 | VTA PEP rejects Phase 2 invitation attempts after documented initiator authority expiry | Automated test on VTA PEP | Technology | RK-G01, RK-G02 |  |
| AT-03 | GR-03 | Anchor diversity metric (geographic / organisational spread) meets documented policy floor at end of Phase 2 | Manual governance audit + VTA metric report | Governance | RK-G03, RK-HX02, RK-SY01 |  |
| AT-04 | GR-04 | VMC issuance fails when only one-directional VRC exists | VTA PEP automated rejection test | Technology | RK-ID01 |  |
| AT-05 | GR-05 | IDVP DID not in trust registry with correct role → VTA rejects IDVC presentation | Automated test | Technology | RK-ID03 |  |
| AT-06 | GR-06 | At least one ZKP / selective disclosure path is available and functional in Phase 4 UX | End-to-end flow test + UX accessibility review | Technology / UX | RK-ID02, RK-ID05, RK-SC01, RK-NM01, RK-CY01, RK-EX03, RK-HX01, RK-HX02 |  |
| AT-07 | GR-07 | Uniqueness enforcement mechanism is documented; if none exists, risk acceptance is signed and dated | Governance audit — manual | Governance | RK-ID01, RK-CY01, RK-AI03, RK-SY01, RK-SY03 |  |
| AT-08 | GR-08 | Revocation notice delivered to member within SLA; appeals path accessible within 24 hours | Governance audit + SLA measurement test | Governance | RK-G04, RK-CR01, RK-CR02, RK-HX03 |  |
| AT-09 | GR-09 | Default revocation status disclosure does not expose member real-world identity | Privacy audit — manual | Governance / Privacy | RK-ID03, RK-ID05, RK-SC01, RK-CR01, RK-CR03, RK-EX03, RK-HX01, RK-HX03 |  |
| AT-10 | GR-10 | Registry write with single-party authorisation rejected | Automated test on registry API | Technology | RK-ID04, RK-EX01, RK-EX02, RK-SY01 |  |
| AT-11 | GR-11 | Jurisdictional distribution of key parties documented; coercion risk assessment signed by governing body | Governance audit — manual | Governance | RK-G03, RK-EX01 |  |
| AT-12 | GR-12 | Agent exceeding capability constraints rejected by VTA PEP; operator VMC revocation propagates to agent within SLA | Automated test + SLA measurement | Technology | RK-AI01, RK-AI02 |  |
| AT-13 | GR-13 | Agent credential operations visible in operator audit log with all required fields | Log completeness automated test | Technology | RK-AI01 |  |
| AT-14 | GR-14 | Rate-limiting triggers on high-frequency non-human credential presentation; legitimate agent traffic not false-positively blocked | Load test + false-positive measurement | Technology | RK-AI03, RK-AI04, RK-SY01 |  |
| AT-15 | GR-15 | Complaint rate-limiting active; legitimate single-member complaint receives response within SLA | Governance audit + SLA measurement | Governance | RK-G04, RK-SY02 |  |
| AT-16 | GR-16 | Published threat model exists, is dated within 12 months, and covers all six listed threat categories | Governance audit — manual | Governance | RK-CY02, RK-EX02, RK-SY02 |  |
| AT-17 | GR-17 | All four open issues have documented mitigations or risk acceptances signed by governing body with review dates | Governance audit — manual | Governance | RK-CY02, RK-EX03, RK-SY03 |  |
| AT-18 | GR-18 | VTC trust registry records a migration trigger date for R-DID adoption; all VRCs issued after that date use R-DIDs (not M-DIDs); OR a formal risk acceptance document is signed by the governing body with rationale and review date, committed to the version-controlled governance record before Phase 4 opens | Governance audit of trust registry migration flag + sample VRC inspection | Governance / Technology | RK-SC04, RK-ID05 | Source: DTG Credential Spec v0.3 §5.2 Privacy Considerations |

## Pivot Risk x Controls

| DTG RAHP – Pivot: Risk × Guardrails (GR) and Controls (CT)  \|  Read across a ... |
|---|

## Control Coverage

| DTG RAHP – Control Coverage Ranking  \|  Controls and Guardrails ranked by number of High-severity risks addressed  \|  Use this to prioritise what goes into the standard | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 |
|---|---|---|---|---|---|---|---|
| Interpretation: Controls / Guardrails with the highest High-risk coverage give the greatest harms-prevention return per standards requirement. These are the priority candidates for normative MUST/SHOULD clauses. |  |  |  |  |  |  |  |
| Rank | ID | Name | Type | Category | High Risks<br>Addressed | Total Risks<br>Addressed | Risks Addressed (IDs) |
| 1 | GR-07 | Uniqueness Enforcement Mechanism | Guardrail | Technology / Governance | 5 | 5 | RK-ID01, RK-CY01, RK-AI03, RK-SY01, RK-SY03 |
| 2 | GR-06 | Privacy-Preserving Proofing Option | Guardrail | Human Experience / Technology | 4 | 8 | RK-ID02, RK-ID05, RK-SC01, RK-NM01, RK-CY01, RK-EX03, RK-HX01, RK-HX02 |
| 3 | GR-09 | Privacy-Preserving Revocation Disclosure | Guardrail | Technology / Governance | 3 | 8 | RK-ID03, RK-ID05, RK-SC01, RK-CR01, RK-CR03, RK-EX03, RK-HX01, RK-HX03 |
| 4 | GR-10 | Multi-Party Registry Write Authorisation | Guardrail | Technology / Governance | 3 | 4 | RK-ID04, RK-EX01, RK-EX02, RK-SY01 |
| 5 | GR-03 | Trust Anchor Diversity Policy | Guardrail | Governance / Human Experience | 3 | 3 | RK-G03, RK-HX02, RK-SY01 |
| 6 | GR-14 | Non-Human Actor Detection | Guardrail | Technology / Governance | 3 | 3 | RK-AI03, RK-AI04, RK-SY01 |
| 7 | CT-08 | Uniqueness Enforcement Mechanism | Control | Technical | 3 | 3 | RK-ID01, RK-AI03, RK-SY03 |
| 8 | GR-08 | Revocation Due Process | Guardrail | Governance / Human Experience | 2 | 4 | RK-G04, RK-CR01, RK-CR02, RK-HX03 |
| 9 | GR-02 | Time-Bounded Initiator Authority | Guardrail | Governance | 2 | 2 | RK-G01, RK-G02 |
| 10 | GR-11 | Jurisdictional Diversity for Key Parties | Guardrail | Governance | 2 | 2 | RK-G03, RK-EX01 |
| 11 | GR-12 | Agent Delegation Scope Constraint | Guardrail | Technology / Governance | 2 | 2 | RK-AI01, RK-AI02 |
| 12 | CT-04 | Trust Anchor Diversity Policy | Control | Governance | 2 | 2 | RK-G03, RK-SY01 |
| 13 | CT-09 | Vouching Pattern Anomaly Detection | Control | Technical | 2 | 2 | RK-ID01, RK-SY01 |
| 14 | CT-10 | Non-Discriminatory Admission Criteria | Control | Governance | 2 | 2 | RK-ID02, RK-HX02 |
| 15 | CT-24 | Privacy-Preserving Revocation Disclosure | Control | Technical | 2 | 2 | RK-CR01, RK-HX03 |
| 16 | CT-33 | Non-Human Activity Rate-Limiting | Control | Technical | 2 | 2 | RK-AI03, RK-AI04 |
| 17 | CT-34 | Behavioural Anomaly Detection for Non-Human Actors | Control | Technical | 2 | 2 | RK-AI03, RK-SY01 |
| 18 | CT-45 | Multi-Party Registry Write Authorisation | Control | Technical | 2 | 2 | RK-SY01, RK-EX01 |
| 19 | GR-01 | Genesis Policy Documentation | Guardrail | Governance | 1 | 3 | RK-G01, RK-SC02, RK-NM02 |
| 20 | GR-16 | Formal Threat Model Publication | Guardrail | Governance | 1 | 3 | RK-CY02, RK-EX02, RK-SY02 |
| 21 | GR-17 | Open Issues Risk Acceptance | Guardrail | Governance | 1 | 3 | RK-CY02, RK-EX03, RK-SY03 |
| 22 | GR-15 | Complaint and Appeals Rate-Limiting | Guardrail | Governance / Human Experience | 1 | 2 | RK-G04, RK-SY02 |
| 23 | CT-07 | Complaint / Appeals Rate-Limiting | Control | Technical | 1 | 2 | RK-G04, RK-SY02 |
| 24 | CT-48 | Threat Model Maintenance | Control | Governance | 1 | 2 | RK-SY03, RK-CY02 |
| 25 | GR-04 | Reciprocal VRC Requirement | Guardrail | Technology / Governance | 1 | 1 | RK-ID01 |
| 26 | GR-05 | IDVP Registry Standing | Guardrail | Technology / Governance | 1 | 1 | RK-ID03 |
| 27 | GR-13 | Agent Audit Logging | Guardrail | Technology / Governance | 1 | 1 | RK-AI01 |
| 28 | CT-01 | Version-Controlled Public Genesis Policy | Control | Procedural | 1 | 1 | RK-G01 |
| 29 | CT-02 | Independent Governance Review at Genesis | Control | Governance | 1 | 1 | RK-G01 |
| 30 | CT-03 | Governance Transition Milestones | Control | Governance | 1 | 1 | RK-G02 |
| 31 | CT-05 | Anchor Clustering Metric Monitoring | Control | Technical | 1 | 1 | RK-G03 |
| 32 | CT-11 | Alternative Identity Proofing Paths | Control | Procedural | 1 | 1 | RK-ID02 |
| 33 | CT-12 | IDVP Security Approval Criteria | Control | Governance | 1 | 1 | RK-ID03 |
| 34 | CT-13 | IDVP Deregistration Handling Protocol | Control | Procedural | 1 | 1 | RK-ID03 |
| 35 | CT-14 | DID Document Integrity Verification | Control | Technical | 1 | 1 | RK-ID04 |
| 36 | CT-20 | Sovereign Wallet UX Design Principles | Control | UX | 1 | 1 | RK-NM01 |
| 37 | CT-21 | Non-Technical User Onboarding Testing | Control | UX | 1 | 1 | RK-NM01 |
| 38 | CT-23 | Mandatory Pre-Revocation Notice | Control | Governance | 1 | 1 | RK-CR01 |
| 39 | CT-27 | Audited ZKP Library Requirement | Control | Technical | 1 | 1 | RK-CY01 |
| 40 | CT-28 | ZKP Conformance Testing | Control | Technical | 1 | 1 | RK-CY01 |
| 41 | CT-30 | Cryptographic Delegation Scope Constraints | Control | Technical | 1 | 1 | RK-AI01 |
| 42 | CT-31 | Short-Lived Agent Credentials | Control | Technical | 1 | 1 | RK-AI01 |
| 43 | CT-32 | Agent Liveness Check on Operator VMC | Control | Technical | 1 | 1 | RK-AI02 |
| 44 | CT-35 | Anchor Awareness of AI Social Engineering | Control | Procedural | 1 | 1 | RK-AI04 |
| 45 | CT-36 | Out-of-Band Verification for High-Stakes Vouching | Control | Procedural | 1 | 1 | RK-AI04 |
| 46 | CT-37 | Jurisdictional Diversity of Key Parties | Control | Governance | 1 | 1 | RK-EX01 |
| 47 | CT-38 | Legal Coercion Response Protocol | Control | Procedural | 1 | 1 | RK-EX01 |
| 48 | CT-43 | Governing Body Accountability for Systematic Exclusion | Control | Governance | 1 | 1 | RK-HX02 |
| 49 | CT-44 | Remediation Pathway After Overturned Revocation | Control | Governance | 1 | 1 | RK-HX03 |
| 50 | CT-46 | Coordinated Behaviour Detection in Governance | Control | Technical | 1 | 1 | RK-SY02 |
| 51 | CT-47 | Formal Open Issues Mitigation Plan | Control | Governance | 1 | 1 | RK-SY03 |
| 52 | CT-15 | Pseudonymous Per-VTC M-DID Design | Control | Technical | 0 | 2 | RK-ID05, RK-HX01 |
| 53 | CT-06 | Governance Capacity Planning | Control | Procedural | 0 | 1 | RK-G04 |
| 54 | CT-16 | Minimum-Necessary IDVC Attribute Set | Control | Governance | 0 | 1 | RK-SC01 |
| 55 | CT-17 | Data Minimisation Audit | Control | Procedural | 0 | 1 | RK-SC01 |
| 56 | CT-18 | Normative Credential Schema Publication | Control | Technical | 0 | 1 | RK-SC02 |
| 57 | CT-19 | Conformance Test Suite | Control | Technical | 0 | 1 | RK-SC02 |
| 58 | CT-22 | Key Recovery Mechanism | Control | Technical | 0 | 1 | RK-NM02 |
| 59 | CT-25 | Credential Renewal Workflow | Control | Technical | 0 | 1 | RK-CR02 |
| 60 | CT-26 | VTC-Scoped Revocation | Control | Technical | 0 | 1 | RK-CR03 |
| 61 | CT-29 | Algorithm Agility and Migration Pathway | Control | Technical | 0 | 1 | RK-CY02 |
| 62 | CT-39 | Distributed Registry Architecture | Control | Technical | 0 | 1 | RK-EX02 |
| 63 | CT-40 | Legal Review of Credential Schemas | Control | Legal | 0 | 1 | RK-EX03 |
| 64 | CT-41 | Open Issues Regulatory Risk Acceptance | Control | Governance | 0 | 1 | RK-EX03 |
| 65 | CT-42 | Anonymous Membership Option | Control | Technical | 0 | 1 | RK-HX01 |

## Risk x Use Case

| DTG RAHP – Risk × Use Case  \|  Which risks arise in which User Stories and Scenarios | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 | Column 10 | Column 11 | Column 12 | Column 13 | Column 14 | Column 15 | Column 16 | Column 17 | Column 18 | Column 19 | Column 20 | Column 21 | Column 22 | Column 23 | Column 24 | Column 25 | Column 26 | Column 27 | Column 28 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Risk ID | Risk Name | Cat | Sev | US-01 | US-02 | US-03 | US-04 | US-05 | US-06 | US-07 | US-08 | US-09 | US-10 | US-11 | US-12 | SC-01 | SC-02 | SC-03 | SC-04 | SC-05 | SC-06 | SC-07 | SC-08 | SC-09 | SC-10 | SC-11 | SC-12 |
| RK-AI01 | Agent Credential Scope Creep | AI Agents | High |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  |
| RK-AI02 | Stale Agent After Operator Revocation | AI Agents | High |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| RK-AI03 | AI-Mediated Sybil Generation at Scale | AI Agents | High |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  | ● |  |  |  | ● |  |
| RK-AI04 | LLM-Powered Social Engineering of Anchors | AI Agents | High |  |  | ● |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |
| RK-CR01 | Credential Revocation Without Due Process | Credentials | High |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| RK-CY01 | ZKP Implementation Failure | Cryptography | High |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| RK-EX01 | State-Level Coercion of Anchors / IDVPs | External | High |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  | ● |  |  |  |
| RK-G01 | Genesis Policy Capture | Governance | High | ● |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |
| RK-G02 | Governance Transition Failure | Governance | High | ● | ● |  |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |
| RK-G03 | Anchor Homogeneity / Collusion Cluster | Governance | High |  | ● | ● |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  | ● |  |  |  |
| RK-HX02 | Discriminatory Vouching Practices | Human Experience | High |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| RK-HX03 | Reputational Harm from Public Revocation | Human Experience | High |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| RK-ID01 | Sybil Identity Proliferation | Identity | High |  |  |  |  |  |  | ● |  |  | ● |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |
| RK-ID02 | Social Graph Privilege Exclusion | Identity | High |  |  |  | ● |  |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |
| RK-ID03 | IDVP Breach / Cascading Invalidation | Identity | High |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| RK-ID04 | DID Document Manipulation | Identity | High |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| RK-NM01 | Personal Network Manager UX Failure | Network Managers | High | ● | ● | ● | ● |  |  |  |  |  |  |  |  | ● | ● | ● | ● |  |  |  |  |  |  |  |  |
| RK-SY01 | Trust Graph Capture by Coordinated Actor | Systemic | High |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  | ● |  |  |  | ● |  |
| RK-SY02 | Coordinated Inauthentic Behaviour (CIB) in Governance | Systemic | High |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  | ● |
| RK-SY03 | Open Issues Left Unresolved at Scale | Systemic | High |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |
| RK-CR02 | Stale Credential / Expiry Without Renewal Path | Credentials | Medium |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| RK-CR03 | Revocation Cascade / Cross-VTC Contamination | Credentials | Medium |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| RK-CY02 | Quantum / Algorithm Obsolescence | Cryptography | Medium |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| RK-EX02 | Registry Censorship / Denial of Service | External | Medium |  |  |  |  |  |  | ● |  |  |  | ● |  |  |  |  |  |  |  |  | ● | ● |  |  |  |
| RK-EX03 | Legal / Regulatory Framework Conflict | External | Medium | ● |  |  |  | ● |  |  |  |  |  |  |  | ● |  |  | ● |  |  |  |  |  |  |  |  |
| RK-G04 | Governance Bandwidth Exhaustion | Governance | Medium |  |  |  |  |  | ● |  |  |  |  |  | ● |  |  |  |  |  | ● |  |  |  |  |  | ● |
| RK-HX01 | Chilling Effect on Community Participation | Human Experience | Medium |  |  |  | ● |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |
| RK-ID05 | M-DID Linkability Across VTCs | Identity | Medium |  |  |  | ● |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |
| RK-NM02 | Key Loss / Recovery Failure | Network Managers | Medium |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |
| RK-SC01 | Over-Disclosure in IDVC Schema | Schemas | Medium |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| RK-SC02 | Credential Schema Ambiguity | Schemas | Medium | ● |  |  |  | ● |  | ● |  |  |  |  |  | ● |  |  | ● |  |  |  |  |  |  |  |  |
| RK-SC03 | VRC Over-Disclosure — Rich Data in Core Edge | Schemas | Medium |  |  |  | ● |  | ● |  |  |  |  |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |
| RK-SC04 | M-DID Bootstrapping Exception Undermines R-DID Privacy | Schemas | Medium |  |  |  | ● |  | ● |  |  |  |  | ● |  | ● | ● |  |  |  |  |  |  | ● |  |  |  |
| RK-CR04 | Endorsement Credential (VEC) Manipulation | Credentials | Medium |  |  | ● |  |  |  |  |  |  | ● |  | ● |  |  |  |  |  |  | ● |  |  |  |  | ● |
| RK-G05 | Governanceless VTC Claiming Credential Compliance | Governance | Medium | ● |  |  | ● |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |

## Trust Metrics

| DTG RAHP – Trust & Confidence Metrics  \|  Metrics personas want to increase (or bad actors want to suppress) | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 |
|---|---|---|---|---|---|
| Metric ID | Metric Name | Category | Description | Personas Who WANT This Metric | Personas Who DISLIKE This Metric |
| M-01 | Anchor Diversity Index | Governance | Measures the geographic, organisational, and cultural spread of trust anchors across the trust graph. A higher score indicates greater decentralisation and resilience to collusion. | D1, D2, D3, D5, D6 | B1, B2 |
| M-02 | Time to Revocation Notice (SLA) | Governance | The elapsed time between a revocation decision and formal notification to the affected member. Lower is better for due process compliance. | D5, D6 | B2, B3 |
| M-03 | VRC Reciprocity Rate | Identity | Proportion of VMC issuances where a valid reciprocal VRC exchange was confirmed. A low rate indicates PEP enforcement failures. | D1, D2, D4, D6 | B1 |
| M-04 | IDVC Issuer Verification Rate | Identity | Proportion of Phase 4 admissions where the IDVP DID was verified against the trust registry before VMC issuance. Should be 100%. | D4, D6 | B1 |
| M-05 | Anomaly Detection Hit Rate (Vouching Patterns) | Security | Rate at which coordinated or anomalous vouching patterns are flagged by the VTA analytics engine. Higher is better for Sybil resistance. | D6, D2 | B1, B3 |
| M-06 | Registry Write Authorisation Failure Rate | Security | Rate at which single-party registry write attempts are rejected. Should be 100% — any successful single-party write is a governance failure. | D6, D1 | B1, B2 |
| M-07 | Appeals Process Response Time | Human Experience | Median time from appeal submission to formal response from the governing body. Lower indicates a more effective due process mechanism. | D3, D5 | B2, B3 |
| M-08 | Agent Credential Scope Violation Rate | AI Agents | Rate at which AI agents attempt operations outside their delegated credential scope. Any non-zero rate indicates a governance or enforcement failure. | M1, D6 | M2, B1 |
| M-09 | ZKP / Selective Disclosure Uptake Rate | Privacy | Proportion of Phase 4 applicants using privacy-preserving proofing options rather than raw IDVC disclosure. Higher indicates better privacy protection. | D3, D4, D5 | B2 |
| M-10 | Jurisdictional Concentration of Key Parties | Governance | Proportion of trust anchors and IDVPs located within a single legal jurisdiction. Lower is better — high concentration indicates coercion risk. | D1, D6 | B2 |
| M-11 | Bad-Faith Appeals Rate | Governance | Proportion of appeal submissions subsequently determined to be coordinated or bad-faith. Rate-limiting and CIB detection should suppress this. | D5, D6 | B3 |
| M-12 | Member Admission Denial Rate | Human Experience | Proportion of well-formed membership applications that are denied. A high rate may indicate discriminatory gatekeeping; a very low rate may indicate weak admission enforcement. | D3 | B1 |
| M-13 | Credential Expiry-to-Renewal Latency | Lifecycle | Time between credential expiry notification and successful renewal. Relevant for both human members and AI agents. Longer latency increases operational disruption. | D5, M1 | M2 |
| M-14 | Sybil Cluster Detection Rate | Security | Rate at which coordinated multi-M-DID registration attempts are identified and blocked. A primary uniqueness enforcement metric. | D6, D1, D2 | B1 |
| M-15 | DID Document Integrity Verification Rate | Cryptography | Proportion of DID document resolutions where the VTA confirms document integrity before relying on the resolved content. Should be 100%. | D6, D4 | B1, B2 |
| M-16 | Governance Body Response Time to Security Findings | Governance | Elapsed time from submission of a security researcher's findings to formal governance acknowledgement and response. Lower supports responsible disclosure and trust. | D6 | B1, B2 |
| M-17 | Cross-VTC Revocation Contamination Rate | Lifecycle | Rate at which a revocation in one VTC propagates (intentionally or accidentally) to unrelated VTCs where the member holds credentials. Should be governed and scoped. | D5, D3 | B2 |
| M-18 | Rate-Limiting Trigger Accuracy (AI / Non-Human) | AI Agents | Proportion of rate-limiting events that correctly target non-human or adversarial activity, avoiding false positives on legitimate benign agents. | M1, D6 | M2, B1 |
|  |  |  |  |  |  |
| LEGEND |  |  |  |  |  |
| Green = Personas who want this metric to be high / visible |  |  |  |  |  |
| Red = Personas (typically bad actors) who dislike this metric or want it suppressed |  |  |  |  |  |

## Metrics x Personas

| DTG RAHP – Metrics × Personas Pivot  \|  ✓ = Wants metric \| ✗ = Dislikes / wants suppressed \| (blank) = Not directly applicable | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 | Column 10 | Column 11 | Column 12 | Column 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Metric ID | Metric Name | D1 | D2 | D3 | D4 | D5 | D6 | M1 | M2 | B1 | B2 | B3 |
| M-01 | Anchor Diversity Index [Governance] | ✓ | ✓ | ✓ |  | ✓ | ✓ |  |  | ✗ | ✗ |  |
| M-02 | Time to Revocation Notice (SLA) [Governance] |  |  |  |  | ✓ | ✓ |  |  |  | ✗ | ✗ |
| M-03 | VRC Reciprocity Rate [Identity] | ✓ | ✓ |  | ✓ |  | ✓ |  |  | ✗ |  |  |
| M-04 | IDVC Issuer Verification Rate [Identity] |  |  |  | ✓ |  | ✓ |  |  | ✗ |  |  |
| M-05 | Anomaly Detection Hit Rate (Vouching Patterns) [Security] |  | ✓ |  |  |  | ✓ |  |  | ✗ |  | ✗ |
| M-06 | Registry Write Authorisation Failure Rate [Security] | ✓ |  |  |  |  | ✓ |  |  | ✗ | ✗ |  |
| M-07 | Appeals Process Response Time [Human Experience] |  |  | ✓ |  | ✓ |  |  |  |  | ✗ | ✗ |
| M-08 | Agent Credential Scope Violation Rate [AI Agents] |  |  |  |  |  | ✓ | ✓ | ✗ | ✗ |  |  |
| M-09 | ZKP / Selective Disclosure Uptake Rate [Privacy] |  |  | ✓ | ✓ | ✓ |  |  |  |  | ✗ |  |
| M-10 | Jurisdictional Concentration of Key Parties [Governance] | ✓ |  |  |  |  | ✓ |  |  |  | ✗ |  |
| M-11 | Bad-Faith Appeals Rate [Governance] |  |  |  |  | ✓ | ✓ |  |  |  |  | ✗ |
| M-12 | Member Admission Denial Rate [Human Experience] |  |  | ✓ |  |  |  |  |  | ✗ |  |  |
| M-13 | Credential Expiry-to-Renewal Latency [Lifecycle] |  |  |  |  | ✓ |  | ✓ | ✗ |  |  |  |
| M-14 | Sybil Cluster Detection Rate [Security] | ✓ | ✓ |  |  |  | ✓ |  |  | ✗ |  |  |
| M-15 | DID Document Integrity Verification Rate [Cryptography] |  |  |  | ✓ |  | ✓ |  |  | ✗ | ✗ |  |
| M-16 | Governance Body Response Time to Security Findings [Governance] |  |  |  |  |  | ✓ |  |  | ✗ | ✗ |  |
| M-17 | Cross-VTC Revocation Contamination Rate [Lifecycle] |  |  | ✓ |  | ✓ |  |  |  |  | ✗ |  |
| M-18 | Rate-Limiting Trigger Accuracy (AI / Non-Human) [AI Agents] |  |  |  |  |  | ✓ | ✓ | ✗ | ✗ |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| Persona → | Full Name | Daniel Wright – Initiator | Laila Hassan – Trust Anchor | Ahmed Khan – New Member | Elena Rossi – IDVP | Sophie Dubois – Revocation Subject | Tomasz Kowalski – Security Researcher | Aether – Benign AI Agent | Phantom – Malign AI Agent | Viktor – Sybil Operator | State Security Directorate | The Collective – Disruptor |

## Risk x Metrics (Pivot)

| DTG RAHP – Risk × Metrics Pivot  \|  Read across to see metrics triggered by a risk  \|  Read down to see all risks a metric helps measure | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 | Column 10 | Column 11 | Column 12 | Column 13 | Column 14 | Column 15 | Column 16 | Column 17 | Column 18 | Column 19 | Column 20 | Column 21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Risk ID | Risk Name | Sev | M-01 | M-02 | M-03 | M-04 | M-05 | M-06 | M-07 | M-08 | M-09 | M-10 | M-11 | M-12 | M-13 | M-14 | M-15 | M-16 | M-17 | M-18 |
| → Metric | Short Name |  | Anchor Diversity Index | Time to Revocation Notice (SLA) | VRC Reciprocity Rate | IDVC Issuer Verification Rate | Anomaly Detection Hit Rate (Vouching) | Registry Write Auth Failure Rate | Appeals Process Response Time | Agent Credential Scope Violation Rate | ZKP / Selective Disclosure Uptake | Jurisdictional Concentration | Bad-Faith Appeals Rate | Member Admission Denial Rate | Credential Expiry-to-Renewal Latency | Sybil Cluster Detection Rate | DID Document Integrity Verification Rate | Governance Response Time to Security Findings | Cross-VTC Revocation Contamination Rate | Rate-Limiting Trigger Accuracy (AI/NHI) |
| RK-G01 | Genesis Policy Capture | H | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| RK-G02 | Governance Transition Failure | H | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| RK-G03 | Anchor Homogeneity / Collusion Cluster | H | ● |  |  |  | ● |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| RK-G04 | Governance Bandwidth Exhaustion | M |  |  |  |  |  |  | ● |  |  |  | ● |  |  |  |  |  |  |  |
| RK-ID01 | Sybil Identity Proliferation | H |  |  | ● |  | ● |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| RK-ID02 | Social Graph Privilege Exclusion | H |  |  |  |  |  |  |  |  | ● |  |  | ● |  |  |  |  |  |  |
| RK-ID03 | IDVP Breach / Cascading Invalidation | H |  |  |  | ● |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |
| RK-ID04 | DID Document Manipulation | H |  |  |  |  |  | ● |  |  |  |  |  |  |  |  | ● |  |  |  |
| RK-ID05 | M-DID Linkability Across VTCs | M |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  | ● |  |
| RK-SC01 | Over-Disclosure in IDVC Schema | M |  |  |  | ● |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| RK-SC02 | Credential Schema Ambiguity | M |  |  |  | ● |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |
| RK-NM01 | Personal Network Manager UX Failure | H |  |  | ● |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| RK-NM02 | Key Loss / Recovery Failure | M |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |
| RK-CR01 | Credential Revocation Without Due Process | H |  | ● |  |  |  |  | ● |  | ● |  |  |  |  |  |  |  |  |  |
| RK-CR02 | Stale Credential / Expiry Without Renewal Path | M |  | ● |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |
| RK-CR03 | Revocation Cascade / Cross-VTC Contamination | M |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  | ● |  |
| RK-CY01 | ZKP Implementation Failure | H |  |  |  |  |  |  |  |  | ● |  |  |  |  |  | ● |  |  |  |
| RK-CY02 | Quantum / Algorithm Obsolescence | M |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  |  |
| RK-AI01 | Agent Credential Scope Creep | H |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  | ● |
| RK-AI02 | Stale Agent After Operator Revocation | H |  |  |  |  |  |  |  | ● |  |  |  |  | ● |  |  |  |  |  |
| RK-AI03 | AI-Mediated Sybil Generation at Scale | H |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  | ● |
| RK-AI04 | LLM-Powered Social Engineering of Anchors | H |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| RK-EX01 | State-Level Coercion of Anchors / IDVPs | H |  |  |  |  |  | ● |  |  |  | ● |  |  |  |  |  |  |  |  |
| RK-EX02 | Registry Censorship / Denial of Service | M |  |  |  |  |  | ● |  |  |  |  |  |  |  |  | ● |  |  |  |
| RK-EX03 | Legal / Regulatory Framework Conflict | M |  |  |  | ● |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| RK-HX01 | Chilling Effect on Community Participation | M |  |  |  |  |  |  |  |  | ● |  |  | ● |  |  |  |  |  |  |
| RK-HX02 | Discriminatory Vouching Practices | H |  |  |  |  | ● |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| RK-HX03 | Reputational Harm from Public Revocation | H |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |
| RK-SY01 | Trust Graph Capture by Coordinated Actor | H | ● |  |  |  | ● |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| RK-SY02 | Coordinated Inauthentic Behaviour (CIB) in Governance | H |  |  |  |  | ● |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| RK-SY03 | Open Issues Left Unresolved at Scale | H |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  | ● |  |  |
| RK-SC03 | VRC Over-Disclosure — Rich Data in Core Edge | M |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| RK-SC04 | M-DID Bootstrapping Exception Undermines R-DID Privacy | M |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  | ● |  |
| RK-CR04 | Endorsement Credential (VEC) Manipulation | M |  |  |  |  | ● |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| RK-G05 | Governanceless VTC Claiming Credential Compliance | M | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |

## Metric Detail

| DTG RAHP – Metric Detail  \|  For each metric: risks it measures, personas who want it, personas who dislike it | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 |
|---|---|---|---|---|---|
| Metric ID | Metric Name | Category | Risks Measured | Personas Who WANT This High | Personas Who DISLIKE This |
| M-01 | Anchor Diversity Index | Governance | RK-G01, RK-G02, RK-G03, RK-G05, RK-SY01 | D1: Daniel Wright – Initiator<br>D2: Laila Hassan – Trust Anchor<br>D3: Ahmed Khan – New Member<br>D5: Sophie Dubois – Revocation Subject<br>D6: Tomasz Kowalski – Researcher | B1: Viktor – Sybil Operator<br>B2: State Security Directorate |
| M-02 | Time to Revocation Notice (SLA) | Governance | RK-CR01, RK-CR02, RK-HX03 | D5: Sophie Dubois – Revocation Subject<br>D6: Tomasz Kowalski – Researcher | B2: State Security Directorate<br>B3: The Collective – Disruptor |
| M-03 | VRC Reciprocity Rate | Identity | RK-ID01, RK-NM01 | D1: Daniel Wright – Initiator<br>D2: Laila Hassan – Trust Anchor<br>D4: Elena Rossi – IDVP<br>D6: Tomasz Kowalski – Researcher | B1: Viktor – Sybil Operator |
| M-04 | IDVC Issuer Verification Rate | Identity | RK-ID03, RK-SC01, RK-SC02, RK-EX03 | D4: Elena Rossi – IDVP<br>D6: Tomasz Kowalski – Researcher | B1: Viktor – Sybil Operator |
| M-05 | Anomaly Detection Hit Rate (Vouching) | Security | RK-G03, RK-ID01, RK-CR04, RK-AI04, RK-HX02, RK-SY01, RK-SY02 | D6: Tomasz Kowalski – Researcher<br>D2: Laila Hassan – Trust Anchor | B1: Viktor – Sybil Operator<br>B3: The Collective – Disruptor |
| M-06 | Registry Write Auth Failure Rate | Security | RK-ID04, RK-EX01, RK-EX02 | D6: Tomasz Kowalski – Researcher<br>D1: Daniel Wright – Initiator | B1: Viktor – Sybil Operator<br>B2: State Security Directorate |
| M-07 | Appeals Process Response Time | Human Experience | RK-G04, RK-CR01 | D3: Ahmed Khan – New Member<br>D5: Sophie Dubois – Revocation Subject | B2: State Security Directorate<br>B3: The Collective – Disruptor |
| M-08 | Agent Credential Scope Violation Rate | AI Agents | RK-AI01, RK-AI02 | M1: Aether – Benign AI Agent<br>D6: Tomasz Kowalski – Researcher | M2: Phantom – Malign AI Agent<br>B1: Viktor – Sybil Operator |
| M-09 | ZKP / Selective Disclosure Uptake | Privacy | RK-ID02, RK-ID05, RK-SC01, RK-SC03, RK-SC04, RK-CR01, RK-CR03, RK-CY01, RK-EX03, RK-HX01 | D3: Ahmed Khan – New Member<br>D4: Elena Rossi – IDVP<br>D5: Sophie Dubois – Revocation Subject | B2: State Security Directorate |
| M-10 | Jurisdictional Concentration | Governance | RK-G03, RK-EX01 | D1: Daniel Wright – Initiator<br>D6: Tomasz Kowalski – Researcher | B2: State Security Directorate |
| M-11 | Bad-Faith Appeals Rate | Governance | RK-G04, RK-SY02 | D5: Sophie Dubois – Revocation Subject<br>D6: Tomasz Kowalski – Researcher | B3: The Collective – Disruptor |
| M-12 | Member Admission Denial Rate | Human Experience | RK-ID02, RK-NM01, RK-HX01, RK-HX02 | D3: Ahmed Khan – New Member | B1: Viktor – Sybil Operator |
| M-13 | Credential Expiry-to-Renewal Latency | Lifecycle | RK-ID03, RK-NM02, RK-CR02, RK-AI02 | D5: Sophie Dubois – Revocation Subject<br>M1: Aether – Benign AI Agent | M2: Phantom – Malign AI Agent |
| M-14 | Sybil Cluster Detection Rate | Security | RK-ID01, RK-CR04, RK-AI03, RK-SY01, RK-SY03 | D6: Tomasz Kowalski – Researcher<br>D1: Daniel Wright – Initiator<br>D2: Laila Hassan – Trust Anchor | B1: Viktor – Sybil Operator |
| M-15 | DID Document Integrity Verification Rate | Cryptography | RK-ID04, RK-SC02, RK-CY01, RK-CY02, RK-EX02 | D6: Tomasz Kowalski – Researcher<br>D4: Elena Rossi – IDVP | B1: Viktor – Sybil Operator<br>B2: State Security Directorate |
| M-16 | Governance Response Time to Security Findings | Governance | RK-G01, RK-G02, RK-G05, RK-CY02, RK-SY03 | D6: Tomasz Kowalski – Researcher | B1: Viktor – Sybil Operator<br>B2: State Security Directorate |
| M-17 | Cross-VTC Revocation Contamination Rate | Lifecycle | RK-ID05, RK-SC04, RK-CR03, RK-HX03 | D5: Sophie Dubois – Revocation Subject<br>D3: Ahmed Khan – New Member | B2: State Security Directorate |
| M-18 | Rate-Limiting Trigger Accuracy (AI/NHI) | AI Agents | RK-AI01, RK-AI03, RK-AI04 | M1: Aether – Benign AI Agent<br>D6: Tomasz Kowalski – Researcher | M2: Phantom – Malign AI Agent<br>B1: Viktor – Sybil Operator |
