# **DTG RAHP Toolkit — Resource Guide**

**Risk, Analysis and Harms Prevention (RAHP) Task Force · Decentralised Trust Graph Working Group** Working Draft · March 2026

## **Overview**

This repository contains the first deliverables of the DTG RAHP Task Force: a set of interconnected analysis tools designed to guide the development of the DTG Credential Specification towards safer, more equitable outcomes. The toolkit is built around Verifiable Trust Communities (VTCs) and their bootstrapping lifecycle.

The tools are intended to be used together. Personas and user stories frame who is affected. The risk register identifies what could go wrong and how severely. The mini-website makes the cross-references navigable. An AI tool can then be applied to a target specification using these materials as structured prompts, producing a gap analysis, harm-cluster summary, and prioritised recommendations. An example of that output is provided in DTG\_RAHP\_Priority\_Requirements\_for\_Standards\_Development.docx.

## **Repository Contents**

| File | Description |
| ----- | ----- |
| DTG\_RAHP\_User\_Stories\_Framework\_v3.xlsx | Personas, user stories, scenarios, EPICs, trust metrics, and cross-reference pivots |
| DTG\_RAHP\_Risk\_Register\_v4.xlsx | Risk register, controls catalogue, guardrails register, assurance tests, and pivot matrices |
| index.html | Mini-website: persona explorer (start here) |
| matrix.html | Mini-website: cross-reference matrix (user stories × metrics, etc.) |
| risks.html | Mini-website: risk register and metrics reference |
| DTG\_RAHP\_Priority\_Requirements\_for\_Standards\_Development.docx | Example output: AI-assisted specification review and priority recommendations |

## **Tool 1 — User Stories Framework (DTG\_RAHP\_User\_Stories\_Framework\_v3.xlsx)**

**What it is.** A structured catalogue of who participates in DTG trust communities, what they need, and how their goals and vulnerabilities connect to measurable outcomes.

**Sheets at a glance:**

| Sheet | Contents |
| ----- | ----- |
| User Stories | 13 user stories (US-01–US-13) covering legitimate users, machine agents, and bad actors across all VTC phases |
| Scenarios | 13 narrative scenarios (SC-01–SC-12) showing how user stories play out under both normal and adversarial conditions |
| EPICs | 14 capability clusters (EPIC-1–EPIC-14) grouping related user stories into feature areas such as bootstrapping, revocation, and AI agent lifecycle |
| Trust Metrics | 18 metrics (M-01–M-18) that personas want to increase, or that bad actors want to suppress. These are the shared interoperability layer between the two workbooks |
| Key Terms & Sources | Definitions for all domain terminology and external sources cited in evidence paragraphs |
| Pivot sheets (×3) | US × Metrics, Scenarios × Metrics, EPICs × Metrics — binary cross-reference matrices for traceability |

**How to use it.** Start with the personas (D1–D6 legitimate users, M1–M2 machine agents, B1–B3 bad actors). Each persona has linked user stories, scenarios, EPICs, and metric IDs. When reviewing a specification, ask: does this section address the needs of D3 (New Member Seeking Inclusion) without enabling B1 (Sybil Network Operator)? The metric IDs provide the shared language for that comparison.

## **Tool 2 — Risk & Harm Register (DTG\_RAHP\_Risk\_Register\_v4.xlsx)**

**What it is.** A comprehensive catalogue of risks, mitigations, phase gates, and test criteria for DTG/VTC systems. Risk scores are calculated as Severity × Likelihood (H=3, M=2, L=1), giving a 1–9 scale. The register currently covers 37 risks, 58 controls, 20 guardrails, and 19 assurance tests.

**Sheets at a glance:**

| Sheet | Contents |
| ----- | ----- |
| Analysis & Conclusions | Executive summary, harm clusters, priority rankings, and spec gap analysis |
| Risk & Harm Register | All risks (RK-xx), with category, VTC phase, severity, likelihood, score, and linked metric IDs |
| Controls Catalogue | 58 controls (CT-xx): continuous risk-reducing measures, each linked to risks and metrics. Note: controls are distinct from guardrails |
| Guardrails Register | 20 guardrails (GR-xx): non-negotiable binary phase-gate pre-conditions. Failure must block phase progression |
| Assurance Tests | 19 tests (AT-xx): binary pass/fail evidence that a specific guardrail is met |
| Pivot matrices (×3) | Risk × Controls, Control Coverage, Risk × Use Case — for gap analysis |
| Trust Metrics / Metrics × Personas | Mirrors the User Stories workbook; metric IDs are the linking mechanism between the two files |

**How to use it.** The three layers — controls, guardrails, assurance tests — form a deliberate hierarchy. Controls reduce probability. Guardrails are absolute gates. Assurance tests are evidence. Do not conflate them. Blue-formatted cells indicate additions sourced from the DTG Credential Specification v0.3 review, distinguishing RAHP-original content from spec-derived additions.

## 

## **Tool 3 — HTML Reference Site (index.html, matrix.html, risks.html)**

**What it is.** A self-contained, three-page static website providing a navigable, audience-appropriate view of the persona, metric, and risk data. The files contain no external dependencies and can be hosted on GitHub Pages or shared directly.

**Pages at a glance:**

| Page | Primary audience | Contents |
| ----- | ----- | ----- |
| index.html — Personas | Everyone; start here | 11 persona cards with photos, quotes, concerns, linked user stories, scenarios, EPICs, and metrics. Mouseover tooltips on all IDs |
| matrix.html — Cross-Reference Matrix | Specification authors, analysts | User stories, scenarios, and EPICs mapped to all 18 metrics. Clickable metric headers highlight the full column |
| risks.html — Risks & Metrics | Standards developers, assurance teams | Full risk register sortable by score, category, severity, and likelihood. Metrics reference with hover descriptions |

**How to use it.** Navigate to index.html first. Click any persona card to open a detailed panel. Use the matrix to identify which metrics are most densely referenced by a given EPIC or scenario. Use the risk register to sort by score and identify the immediate standards action set (score 9 \= High × High).

## **Tool 4 — AI-Assisted Specification Review (example workflow)**

**What it is.** The toolkit is designed to be used as structured prompting material for an AI tool such as Claude. The example output (DTG\_RAHP\_Priority\_Requirements\_for\_Standards\_Development.docx) demonstrates the result of applying all three tools to DTG Credential Specification v0.3.

**How to replicate the workflow:**

1. Open a conversation with an AI GPT and provide the Risk Register and User Stories Framework as context.  
2. Upload the target specification.  
3. Ask the AI to: (a) identify which risks the spec addresses, partially addresses, or leaves unaddressed; (b) map spec sections to relevant personas and user stories; (c) flag new risks introduced by specific design choices; and (d) rank gaps by risk score and produce prioritised normative recommendations.  
4. The RAHP identifier scheme (RK-xx, CT-xx, GR-xx, AT-xx, M-xx, US-xx, SC-xx, EPIC-xx) provides stable anchors the AI can reference precisely.

The example output demonstrates that this process surfaced four new risks, updated four existing risk descriptions, and added eight controls, one guardrail, and one assurance test — material that was subsequently incorporated into v4 of the register.

## **Identifier Scheme**

All identifiers are stable across tools and updates:

| Prefix | Type |
| ----- | ----- |
| RK-xx | Risk |
| CT-xx | Control |
| GR-xx | Guardrail |
| AT-xx | Assurance Test |
| M-xx | Trust Metric |
| US-xx | User Story |
| SC-xx | Scenario |
| EPIC-xx | EPIC / capability cluster |

Metric IDs (M-xx) are the shared reference standard linking the two workbooks. The HTML site does not require the workbooks to be open — all IDs are cross-referenced via tooltips.

## **Conceptual Distinctions**

Three terms are frequently confused and should not be:

**Controls (CT-xx)** are continuous risk-reducing measures. They lower the probability or impact of a risk but do not gate phase progression. Most are normative candidates for the specification.

**Guardrails (GR-xx)** are binary phase-gate pre-conditions. They must be satisfied before a VTC can progress to the next bootstrapping phase. Failure is a hard stop, not a risk-acceptance opportunity.

**Assurance Tests (AT-xx)** are the evidence that a guardrail has been met. Each test is binary (pass/fail) and linked to a specific guardrail. They are the audit criterion for conformance claims.

## **Version History**

| Version | Date | Changes |
| ----- | ----- | ----- |
| User Stories Framework v3 | March 2026 | Three pivot sheets added; metric IDs replace persona columns as cross-reference standard |
| Risk Register v4 | March 2026 | DTG Credential Spec v0.3 review: 4 new risks (RK-SC03, RK-SC04, RK-CR04, RK-G05), 8 new controls, 1 new guardrail, 1 new assurance test; 4 risk descriptions updated; 1 risk likelihood downgraded |
| HTML site | March 2026 | Initial release: index, matrix, risks pages; base64-embedded persona photos; sortable risk register |

*Maintained by the DTG RAHP Task Force. For questions, open an issue or post in the DTGWG GitHub Discussions.*

