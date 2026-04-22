[README.md](https://github.com/user-attachments/files/26967001/README.md)
# DTG RAHP Toolkit

**Risk Assessment & Harms Prevention Task Force · Decentralised Trust Graph Working Group**  
Working Draft · April 2026 · CC-BY 4.0

---

The RAHP Toolkit is a set of interconnected analysis tools for embedding human harm prevention into the design of decentralised trust systems from the outset. It was developed by the DTGWG Risk Assessment & Harms Prevention Task Force, using the DTG Credential Specification as the reference implementation context — but the methodology is designed to be generalisable to any open standards working group or task force working on systems that affect people.

The core argument: a standard designed without systematically asking who gets hurt if this is wrong will produce a system that fails the people most exposed to its failures. The toolkit provides the structured method for asking that question and turning the answers into requirements that standards bodies can act on.

---

## Repository contents

| File | Description |
|---|---|
| `DTG_RAHP_User_Stories_Framework_v3.xlsx` | Personas, user stories, scenarios, EPICs, trust metrics, and cross-reference pivots |
| `DTG_RAHP_Risk_Register_v4.xlsx` | Risk register, controls catalogue, guardrails register, assurance tests, and pivot matrices |
| `index.html` | Mini-website: persona explorer (start here) |
| `matrix.html` | Mini-website: cross-reference matrix (user stories × metrics) |
| `risks.html` | Mini-website: risk register and metrics reference |
| `RAHP_Workflow_Reference.html` | Interactive workflow reference: the toolkit against the standards development lifecycle |
| `RAHP_AI_Assisted_Process.md` | Practical guide to using Claude (or any AI assistant) with the toolkit |
| `DTG_RAHP_Priority_Requirements_for_Standards_Development.docx` | Example output: AI-assisted spec review and priority recommendations |

---

## Where to start

**If you are new to the toolkit:** open `index.html` in a browser. The persona cards are the entry point — click any one to see which risks threaten that participant, which metrics signal those risks, and which user stories and scenarios they appear in. Everything else in the toolkit connects through the persona identifiers.

**If you are reviewing a specification:** open `risks.html`. Sort the risk register by score (High × High = 9) to identify the immediate action set. Use the metric IDs (M-xx) to cross-reference against the User Stories Framework.

**If you are running a working group session:** read `RAHP_Workflow_Reference.html`. It maps the toolkit against the five stages of the standards development lifecycle and shows what the toolkit provides at each stage, what it receives back, and where the gaps are.

**If you want to use an AI assistant to accelerate the work:** read `RAHP_AI_Assisted_Process.md`. It gives five worked examples with prompts, inputs, expected outputs, and explicit notes on what requires human judgement.

---

## The toolkit at a glance

### Tool 1 — User Stories Framework (`DTG_RAHP_User_Stories_Framework_v3.xlsx`)

A structured catalogue of who participates in DTG trust communities, what they need, and how their goals and vulnerabilities connect to measurable outcomes.

| Sheet | Contents |
|---|---|
| User Stories | 13 user stories (US-01–US-13) across legitimate users, machine agents, and bad actors |
| Scenarios | 13 narrative scenarios (SC-01–SC-12) under normal and adversarial conditions |
| EPICs | 14 capability clusters (EPIC-1–EPIC-14): bootstrapping, revocation, AI agent lifecycle, etc. |
| Trust Metrics | 18 metrics (M-01–M-18) — the shared reference standard linking both workbooks |
| Key Terms & Sources | Domain terminology definitions and external sources cited in evidence paragraphs |
| Pivot sheets (×3) | US × Metrics, Scenarios × Metrics, EPICs × Metrics — binary cross-reference matrices |

**How to use it.** Start with the personas (D1–D6 legitimate users, M1–M2 machine agents, B1–B3 bad actors). Each persona has linked user stories, scenarios, EPICs, and metric IDs. When reviewing a specification, ask: does this section address the needs of D3 (new member seeking inclusion) without enabling B1 (Sybil network operator)? The metric IDs provide the shared language for that comparison.

### Tool 2 — Risk & Harm Register (`DTG_RAHP_Risk_Register_v4.xlsx`)

A comprehensive catalogue of risks, mitigations, phase gates, and test criteria for DTG/VTC systems. Risk scores are calculated as Severity × Likelihood (H=3, M=2, L=1), giving a 1–9 scale. The register currently covers 37 risks, 58 controls, 20 guardrails, and 19 assurance tests.

| Sheet | Contents |
|---|---|
| Analysis & Conclusions | Executive summary, harm clusters, priority rankings, spec gap analysis |
| Risk & Harm Register | All risks (RK-xx) with category, VTC phase, severity, likelihood, score, and linked metric IDs |
| Controls Catalogue | 58 controls (CT-xx): continuous risk-reducing measures linked to risks and metrics |
| Guardrails Register | 20 guardrails (GR-xx): non-negotiable binary phase-gate pre-conditions |
| Assurance Tests | 19 tests (AT-xx): binary pass/fail evidence that a specific guardrail is met |
| Pivot matrices (×3) | Risk × Controls, Control Coverage, Risk × Use Case |
| Trust Metrics / Metrics × Personas | Mirrors the User Stories workbook; metric IDs are the linking mechanism |

**How to use it.** The three layers — controls, guardrails, assurance tests — form a deliberate hierarchy. Controls reduce probability. Guardrails are absolute gates. Assurance tests are evidence. Do not conflate them. Blue-formatted cells indicate additions sourced from the DTG Credential Specification v0.3 review, distinguishing RAHP-original content from spec-derived additions.

### Tool 3 — HTML Reference Site (`index.html`, `matrix.html`, `risks.html`)

A self-contained three-page static website providing a navigable view of the persona, metric, and risk data. No external dependencies. Can be hosted on GitHub Pages or shared directly as files.

| Page | Primary audience | Contents |
|---|---|---|
| `index.html` — Personas | Everyone; start here | 11 persona cards with quotes, concerns, linked user stories, scenarios, EPICs, and metrics. Mouseover tooltips on all IDs |
| `matrix.html` — Cross-Reference Matrix | Specification authors, analysts | User stories, scenarios, and EPICs mapped to all 18 metrics. Clickable metric headers highlight full columns |
| `risks.html` — Risks & Metrics | Standards developers, assurance teams | Full risk register sortable by score, category, severity, and likelihood. Metrics reference with hover descriptions |

### Tool 4 — Workflow Reference (`RAHP_Workflow_Reference.html`)

An interactive reference showing how the toolkit is used across all five stages of the standards development lifecycle: scoping, drafting, review and harmonisation, publication, and maintenance.

Each stage is documented with what the toolkit provides, what activities it supports, what it receives back as contributions, and where the known gaps are. The workflow is built around the principle that people and implementation context drive everything — the Context stage (scoping) is the generative engine from which all downstream artefacts derive their analytical grounding.

Open the file in a browser. Use the numbered tabs to navigate between stages. Collapsible sections within each stage allow you to drill into specific phases without losing the overall structure. Gap callouts are shown in amber throughout.

**Governing discipline.** The workflow applies the inclusive by design principles developed through the Sovrin and ToIP Human Experience Working Group work: design for the margins (extreme users define requirements, not middle cases); no-one left behind; harm prevention as a first-class design input from the outset.

### Tool 5 — AI-Assisted Process Guide (`RAHP_AI_Assisted_Process.md`)

A practical guide to using Claude (or any capable AI assistant) alongside the toolkit. Covers five tasks:

1. Drafting an extreme user profile from interview notes (Phase B)
2. Synthesising a persona narrative from multiple sources (Phase C)
3. Cross-referencing a design decision against the risk register (Stage 2)
4. Drafting a user story from an objectives map (Stage 2)
5. Identifying gaps in persona coverage (Phase D and maintenance)

Each task includes: the workflow stage it belongs to, the toolkit components used, the input required, an example prompt, the expected output, and explicit notes on what requires human judgement. A "what not to use Claude for" section covers risk scoring, guardrail verification, governance decisions, fieldwork, and source verification.

---

## Identifier scheme

All identifiers are stable across tools and updates. The metric IDs (M-xx) are the shared reference standard linking the two workbooks and the HTML site.

| Prefix | Type | Count |
|---|---|---|
| `RK-xx` | Risk | 37 |
| `CT-xx` | Control | 58 |
| `GR-xx` | Guardrail | 20 |
| `AT-xx` | Assurance test | 19 |
| `M-xx` | Trust metric | 18 |
| `US-xx` | User story | 13 |
| `SC-xx` | Scenario | 13 |
| `EPIC-xx` | EPIC / capability cluster | 14 |
| `D-series` | Legitimate user persona | D1–D6 |
| `M-series` | Machine agent persona | M1–M2 |
| `B-series` | Bad actor persona | B1–B3 |

---

## Three conceptual distinctions that matter

These terms are frequently conflated and should not be:

**Controls (CT-xx)** are continuous risk-reducing measures. They lower the probability or impact of a risk but do not gate phase progression. Most are normative candidates for the specification.

**Guardrails (GR-xx)** are binary phase-gate pre-conditions. They must be satisfied before a VTC can progress to the next bootstrapping phase. Failure is a hard stop, not a risk-acceptance opportunity.

**Assurance Tests (AT-xx)** are the evidence that a guardrail has been met. Each test is binary (pass/fail) and linked to a specific guardrail. They are the audit criterion for conformance claims.

---

## Known gaps

The toolkit is a v1 design-time artefact. Several capabilities needed for runtime governance are not yet specified:

- **Formal risk acceptance workflow** — no defined process for who accepts a risk, under what authority, with what documentation
- **Operational monitoring process** — trust metrics are defined as measurement instruments; the process that uses them at runtime is not
- **Harm triage and response** — point controls exist (GR-08, CT-44, CT-38) but no orchestrated harm response process
- **Contribution and integration governance** — the feedback loop from practitioners back into the toolkit is under development; practitioner trials are planned before it is specified
- **Vulnerability catalogue** — vulnerabilities are currently embedded in risk descriptions rather than catalogued separately

These are acknowledged as the primary development priorities for v2. If you encounter a gap not listed here, please open an issue.

---

## Version history

| Artefact | Version | Date | Changes |
|---|---|---|---|
| User Stories Framework | v3 | March 2026 | Three pivot sheets added; metric IDs replace persona columns as cross-reference standard |
| Risk Register | v4 | March 2026 | DTG Credential Spec v0.3 review: 4 new risks, 8 new controls, 1 new guardrail, 1 new assurance test; 4 risk descriptions updated; 1 risk likelihood downgraded |
| HTML reference site | v1 | March 2026 | Initial release: index, matrix, risks pages |
| Workflow Reference | v1 | April 2026 | Initial release: five-stage lifecycle workflow with gap annotations |
| AI-Assisted Process guide | v1 | April 2026 | Initial release: five worked examples with prompts and human-review notes |

---

## Contributing

The toolkit improves through use. If you apply it to a specification review and surface new risks, refine existing scores, or identify participant types not currently represented in the persona set, please contribute those findings back:

- Open an **issue** to report a gap, propose a new risk, or flag an inaccuracy
- Open a **pull request** with proposed artefact changes, following the provenance tagging convention (note the source that triggered the change)
- Post in **DTGWG GitHub Discussions** for broader questions about methodology or application context

The AI-assisted process guide (`RAHP_AI_Assisted_Process.md`) is particularly intended as a living document — if you have found prompt patterns that work well, or found that the worked examples produce poor results in practice, additions and corrections are explicitly welcomed.

---

*Maintained by the Risk Assessment & Harms Prevention Task Force, DTGWG.*  
*For questions, open an issue or post in DTGWG GitHub Discussions.*  
*CC-BY 4.0 — reuse with attribution.*
