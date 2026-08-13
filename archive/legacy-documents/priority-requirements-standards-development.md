---
layout: default
title: "DTG RAHP #U2014 Priority Requirements for Standards Development — historical document"
nav_exclude: true
has_toc: true
---

# DTG RAHP #U2014 Priority Requirements for Standards Development

> **Historical artefact.** This is a reading projection of a retained RAHP document. It is preserved for provenance and is not a current canonical RAHP source.

[Download the original document](priority-requirements-standards-development.docx){: .btn .btn-primary }

## Risk Assessment & Harms Prevention: Priority Requirements for DTG Standards Development

Working Draft · RAHP Task Force · March 2026
Derived from: VTC Bootstrapping Draft v3, Personas Analysis, DTG Credential Spec v0.3 review, DTGWG GitHub discussions

Document for internal review

### Overview

The RAHP risk and harm register currently identifies 35 risks across 10 categories — 20 High severity, 11 Medium, and 4 that are both High severity and High likelihood (the immediate action set). Against those risks the analysis defines 56 controls (CT), 18 guardrails (GR), and 18 assurance tests (AT). This note summarises which of those items carry the highest priority for inclusion as normative requirements in the DTG credential specification, and flags the four new risks introduced by the v0.3 spec review.

Risk categories with 100% High severity: AI Agents (4/4), Systemic (3/3).

### Five Critical Harm Clusters

Before listing controls, it is worth naming what the controls are protecting against. The register groups into five harm clusters:

### Priority Guardrails (Phase Gates)

Ranked by number of High-severity risks addressed. A guardrail is a binary pass/fail pre-condition — failure must block phase progression, not merely trigger risk-reduction.

GR-06 has the highest single-guardrail risk coverage in the dataset. Without it, GDPR compliance, social exclusion, and surveillance risks are simultaneously unmitigated.

### Priority Controls (Normative Candidates)

Ranked by High-severity risks addressed.

### Priority Assurance Tests

The assurance tests with the highest risk coverage, each providing binary pass/fail evidence that a guardrail is met:

### Eight Priority Recommendations

#### REC-1 · NORMATIVE — Uniqueness enforcement as phase-gate

GR-07 + CT-08 must become normative MUST requirements before Phase 4 opens. The specification should define at minimum three acceptable mechanisms (ZKP personhood proof, trusted IDVP quorum, social recovery) and require governing bodies to select and document one. This is the single gap with the highest combined control coverage across trust-graph integrity, AI-mediated fraud, and the open issues cluster — and it is completely absent from spec v0.3.

#### REC-2 · NORMATIVE — AI agent governance as first-class specification area

All four AI Agent risks are High severity. The spec must include a dedicated chapter covering: CT-30 (delegation scope constraints) as MUST; CT-32 (operator VMC liveness check) as MUST; GR-14 (non-human actor detection) as a Phase 4 pre-condition; CT-51 (non-human DID designation) as MUST. This is a gap in every existing VC/DID standard.

#### REC-3 · NORMATIVE — Privacy-preserving revocation

GR-09 + CT-24 address 8 risks. Revocation status must not be publicly linked to real-world identity by default. Privacy-preserving revocation status mechanisms (e.g. W3C Status List 2021 with ZKP) must be normative MUST, not optional. CT-26 (VTC-scoped revocation) must also be normative — cross-VTC contamination is a human rights risk arising from the architecture itself.

#### REC-4 · NORMATIVE — Non-discriminatory admission and alternative identity proofing

RK-ID02 (Social Graph Privilege Exclusion) and RK-HX02 (Discriminatory Vouching) are both High severity and High likelihood — the most urgent combination in the dataset. The spec must require: (a) published non-discriminatory admission criteria (CT-10); (b) at least one admission pathway not requiring government-issued ID (CT-11); (c) a documented appeals process (GR-08). These are simultaneously legal requirements in most jurisdictions.

#### REC-5 · NORMATIVE — Multi-party registry write authorisation

CT-45 + GR-10 address trust graph capture, state coercion, and registry manipulation together. Multi-party / threshold write authorisation must be a normative MUST in the DTG trust registry specification, with minimum thresholds defined (e.g. 2-of-3 for small VTCs) and tamper-evident audit trails required for all writes.

#### REC-6 · RECOMMENDED — Formal threat model as standards deliverable

GR-16 + CT-48. The DTGWG should publish the threat model as a standalone deliverable normatively referenced by the credential specification, so implementations can demonstrate conformance against it. Assurance test AT-16 defines the pass criterion.

#### REC-7 · RECOMMENDED — UX design principles as normative annex

RK-NM01 is High severity and High likelihood. The DTGWG itself identifies UX as "the single hardest problem." CT-20 (sovereign wallet UX design principles) and CT-21 (non-technical user onboarding testing) should be a normative annex, not left to implementations — poor UX creates security failures, not just usability problems.

#### REC-8 · PROCESS — Mandatory open issues resolution before Phase 4

GR-17. The four bootstrapping open issues (uniqueness, trust task protocols, expiration/revocation, DID document storage) must each have a documented mitigation or signed risk-acceptance with a review date before any implementation claims Phase 4 conformance. AT-17 provides the governance audit criterion.

### Spec v0.3 Gap Summary

The March 2026 DTG Credential Specification review introduced four new risks and identified the following gaps:

What spec v0.3 gets right: R-DID MUST per-relationship (§5.2) reduces RK-ID05 likelihood. Bilateral VRC signatures partially implement GR-04. Witness Credential (§7.3) partially counters RK-AI04. Format-agnostic ZKP supports algorithm agility.

New risks introduced by spec v0.3 design choices:

RK-SC03 — VRC core schema allows rich data embedding with no normative constraint to use annotation credentials (§5.2), undermining ZKP selective disclosure

RK-SC04 — M-DID bootstrapping exception has no normative migration trigger, making the R-DID privacy guarantee contingent on a transition that may never happen

RK-CR04 — VEC endorsement structure is open-ended, enabling coordinated reputation inflation by bad actors (§7.2)

RK-G05 — No normative governance pre-condition for credential compliance; a governanceless VTC can claim spec conformance (§9)

Critical gaps before Implementer's Draft: R1 (non-human participant governance §10), R2 (uniqueness enforcement levels), R3 (revocation placeholder with normative hook), R4 (VIC role embedding).

High-priority this draft cycle: R5 (JSON-LD context as resolvable artefact), R6 (VRC data minimisation clause), R7 (R-DID migration trigger as MUST), R8 (governance conformance class).

### High-Priority Risk Shortlist (score 9 or 6)

Score = Severity × Likelihood (H=3, M=2, L=1). The four score-9 risks are the immediate standards action set.

Full risk register, controls catalogue, and cross-reference matrices: [DTG RAHP Risk Register v4] and [DTG RAHP User Stories Framework v3] Interactive reference: index.html / matrix.html / risks.html (DTG RAHP HTML package) See ShareDrive

## Table 1

| # | Harm cluster | Risks affected | Nature |
|---|---|---|---|
| C1 | Trust graph integrity / identity fraud | 9 High | Sybil proliferation, AI-mediated synthetic identities, anchor collusion, registry manipulation. Existential: if the graph cannot be trusted, DTG fails. |
| C2 | Human rights — revocation, exclusion, surveillance | 6 High | Unjust revocation without due process, discriminatory vouching, reputational harm from public revocation, state surveillance via membership linkability. Structural features of the architecture, not edge cases. |
| C3 | Governance failure / capture | 7 High | Genesis policy capture, governance transition failure, CIB in governance. Most dangerous during bootstrapping when power is maximally concentrated and oversight does not yet exist. |
| C4 | Privacy / data protection | 5 Medium–High | Schema over-disclosure, M-DID linkability, ZKP failures, chilling effect. Legal exposure under GDPR and eIDAS 2.0 if unaddressed normatively. |
| C5 | AI-specific attack surface | 4 High | Agent scope creep, stale agent after operator revocation, AI-mediated Sybil at scale, LLM-powered anchor social engineering. No existing VC/DID standard addresses this. |

## Table 2

| Rank | Guardrail | High risks | Total risks | Phase gate |
|---|---|---|---|---|
| 1 | GR-06 Privacy-Preserving Proofing Option | 5 | 8 | Pre–Phase 4 |
| 2 | GR-09 Privacy-Preserving Revocation Disclosure | 3 | 8 | Revocation |
| 3 | GR-07 Uniqueness Enforcement Mechanism | 4 | 5 | Pre–Phase 4 |
| 4 | GR-10 Multi-Party Registry Write Authorisation | 3 | 4 | All phases |
| 5 | GR-14 Non-Human Actor Detection | 3 | 3 | Pre–Phase 4 |
| 6 | GR-03 Trust Anchor Diversity Policy | 3 | 3 | Pre–Phase 2 |
| 7 | GR-08 Revocation Due Process | 2 | 4 | Revocation |
| 8 | GR-12 Agent Delegation Scope Constraint | 2 | 2 | Agent lifecycle |

## Table 3

| Rank | Control | Type | High risks | Normative case |
|---|---|---|---|---|
| 1 | CT-08 Uniqueness Enforcement Mechanism | Technical | 3 | Single highest-coverage technical control. Addresses Sybil, AI-mediated fraud, and the open issues cluster. Completely absent from spec v0.3. |
| 2 | CT-34 Behavioural Anomaly Detection for Non-Human Actors | Technical | 3 | Required before Phase 4 opens (GR-14 underpins). Addresses AI-mediated Sybil generation and social engineering. |
| 3 | CT-45 Multi-Party Registry Write Authorisation | Technical | 3 | Protects the trust registry from single-actor attacks. State coercion and graph capture both depend on unilateral write access. |
| 4 | CT-04 Trust Anchor Diversity Policy | Governance | 3 | Required before Phase 2. Addresses anchor collusion, discriminatory vouching, and systemic capture simultaneously. |
| 5 | CT-09 Vouching Pattern Anomaly Detection | Technical | 2 | Complements CT-08. Detects coordinated Sybil vouching rings before they pass admission thresholds. |
| 6 | CT-15 Pseudonymous Per-VTC M-DID Design | Technical | 2 | Foundational privacy. Prevents cross-community profiling. Should be normative design requirement in the credential spec. |
| 7 | CT-24 Privacy-Preserving Revocation Disclosure | Technical | 2 | Protects members from public identity exposure during revocation. Addresses RK-CR01 and RK-HX03 together. |
| 8 | CT-30 Cryptographic Delegation Scope Constraints | Technical | 2 | Required for safe AI agent participation. No existing standard addresses this. |
| 9 | CT-32 Agent Liveness Check on Operator VMC | Technical | 2 | Prevents stale agent access after operator revocation. Normative MUST for agent credential lifecycle. |
| 10 | CT-10 Non-Discriminatory Admission Criteria | Governance | 2 | Equality law and human rights requirement. Must be a normative MUST in the VTC governance framework specification. |

## Table 4

| AT | Linked guardrail | Risks covered | Test type |
|---|---|---|---|
| AT-06 | GR-06 | RK-ID02, RK-ID05, RK-SC01, RK-NM01, RK-CY01, RK-EX03, RK-HX01, RK-HX02 | End-to-end flow test + UX accessibility review |
| AT-07 | GR-07 | RK-ID01, RK-CY01, RK-AI03, RK-SY01, RK-SY03 | Governance audit — uniqueness mechanism documented or risk-accepted |
| AT-09 | GR-09 | RK-ID03, RK-ID05, RK-SC01, RK-CR01, RK-CR03, RK-EX03, RK-HX01, RK-HX03 | Privacy audit |
| AT-10 | GR-10 | RK-ID04, RK-EX01, RK-EX02, RK-SY01 | Automated test on registry API |
| AT-14 | GR-14 | RK-AI03, RK-AI04, RK-SY01 | Load test + false-positive measurement |
| AT-03 | GR-03 | RK-G03, RK-HX02, RK-SY01 | Governance audit + VTA metric report |
| AT-12 | GR-12 | RK-AI01, RK-AI02 | Automated test + SLA measurement |

## Table 5

| Risk | Name | Score | Addresses |
|---|---|---|---|
| RK-ID01 | Sybil Identity Proliferation | 9 | GR-07, GR-04, CT-08, CT-09, AT-04, AT-07 |
| RK-ID02 | Social Graph Privilege Exclusion | 9 | GR-06, CT-10, CT-11, AT-06 |
| RK-NM01 | Personal Network Manager UX Failure | 9 | GR-06, CT-20, CT-21, AT-06 |
| RK-SY03 | Open Issues Left Unresolved at Scale | 9 | GR-07, GR-17, CT-47, CT-48, AT-07, AT-17 |
| RK-G03 | Anchor Homogeneity / Collusion Cluster | 6 | GR-03, GR-11, CT-04, CT-05, AT-03, AT-11 |
| RK-G04 | Governance Bandwidth Exhaustion | 6 | GR-08, GR-15, CT-06, CT-07, AT-08, AT-15 |
| RK-SC04 | M-DID Bootstrapping Exception | 6 | GR-18, CT-50, AT-18 |
| RK-G05 | Governanceless VTC | 6 | GR-01, GR-02, CT-56, AT-01, AT-02 |
