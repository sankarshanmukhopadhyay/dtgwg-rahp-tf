---
layout: default
title: "AI-assisted process"
nav_order: 12
has_toc: true
---
# AI-assisted RAHP — a worked example

**RAHP Toolkit · CC-BY 4.0 · originally developed April 2026; generalized for portable use in v0.6**

---

## What this document is

A short, practical walkthrough of how a capable general-purpose AI assistant can be used to accelerate specific steps in the RAHP workflow. It covers five tasks that practitioners have found AI assistance genuinely useful for, with example prompts, the toolkit components each task uses, and honest notes about what requires human judgement regardless.

This is deliberately not a comprehensive methodology. Different practitioners will work differently, different AI tools have different strengths, and this area is evolving quickly. Treat this as a starting point, not a prescription.

---

## Ground rules before you start

**AI assists — it does not decide.** An assistant can draft, synthesise, cross-reference, and suggest. It cannot score risk severity, validate that a guardrail is actually met, make governance decisions, or tell you who is missing from your participant map. Every output needs human review before it goes into the toolkit.

**Provide context explicitly.** The assistant does not have access to your working documents unless you paste them in. The prompts below assume you paste the relevant toolkit artefacts — or the relevant sections — directly into the conversation. Work in a single session where possible so the assistant retains the context.

**Check sources.** When the assistant cites threat intelligence or regulatory context for persona narratives, verify the sources. It will sometimes produce plausible-sounding but inaccurate citations. The RAHP toolkit's sourcing standard is: every empirical claim in a persona narrative should link to a verifiable source.

**Version your outputs.** Paste the assistant's outputs into your working documents and apply your normal version control and provenance tagging. The AI session itself is not a record — the committed artefact is.

---

## Task 1 — Drafting an extreme user profile from interview notes

**Workflow stage:** Phase B (extreme user and bad-actor identification)

**When to use this:** You have conducted or reviewed qualitative fieldwork with a participant type and need to structure the output as an extreme user profile suitable for Phase C persona synthesis.

**Toolkit components used:**
- Phase B extreme user template (from the workflow reference)
- Existing persona set (for context on what is already covered)

**Input to the assistant:** Paste your raw notes or a summary of the engagement. Include: who you spoke with or whose perspective you reviewed, the context they operate in, what they said about their needs and fears, and what made their situation distinct from the mainstream case.

**Example prompt:**

```
I am developing an extreme user profile for the RAHP toolkit. Here are my notes 
from a review of community feedback from participants in a civic technology VTC 
operating in a jurisdiction with restricted internet freedom.

[paste notes]

Using this material, draft an extreme user profile in the following format:
- Name and type (anonymised or composite)
- Context (jurisdiction, technical environment, social position)
- Primary objectives (what they need the system to provide)
- Specific vulnerabilities (what aspects of the VTC architecture could harm them 
  that would not affect a mainstream user)
- Key design implications (what this profile suggests the standard must address)

Be specific and grounded in the notes. Do not generalise beyond what the notes 
support. Flag anything where you are extrapolating rather than reporting.
```

**Expected output:** A structured extreme user profile draft, 200–350 words, with a flags section noting where the assistant has extrapolated. This feeds directly into Phase C persona synthesis.

**Human review required:** Check that the profile accurately represents the source material. Assess whether the design implications are correctly derived. Add sourcing notes before committing.

---

## Task 2 — Synthesising a persona narrative from multiple sources

**Workflow stage:** Phase C (persona synthesis)

**When to use this:** You have an extreme user profile, relevant threat intelligence, and notes from the raw participant map, and need to synthesise them into a full RAHP-format persona narrative.

**Toolkit components used:**
- Existing persona set — paste D1, D3, D5 as format and tone references
- Phase B extreme user profile (output from Task 1)
- Phase A raw participant map extract

**Input to the assistant:** Paste the extreme user profile from Task 1, the relevant section of the raw participant map, and two or three existing RAHP personas as format references.

**Example prompt:**

```
I need to draft a new RAHP persona in the style of the existing DTG personas. 
Here are three existing personas for reference:

[paste Daniel Wright D1, Ahmed Khan D3, and Sophie Dubois D5]

Here is the extreme user profile I want to develop into a full persona:

[paste output from Task 1]

Draft a full persona narrative following the same structure as the examples: 
name, age, location, opening quote, goals and motivations, risk context 
(pain points), inclusion/exclusion factors, key use cases, and a short insights 
section with at least two sourced references to documented real-world precedents.

The insights section should cite published sources — if you are uncertain whether 
a source is accurate, say so and I will verify. Do not invent citations.
```

**Expected output:** A full persona narrative draft in RAHP format, ready for review. The insights section will contain draft citation notes that need verification before the persona is committed.

**Human review required:** Verify all citations. Assess whether the persona's objectives and vulnerabilities are analytically distinct from existing personas — a new persona that duplicates an existing one adds noise rather than analytical value. Confirm the opening quote feels authentic to the person type rather than generically constructed.

---

## Task 3 — Cross-referencing a design decision against the risk register

**Workflow stage:** Stage 2 (Drafting), Station 2 (Risk assessment)

**When to use this:** A spec author or working group member has proposed a design choice and wants to quickly identify which existing risks are affected before bringing it to the group.

**Toolkit components used:**
- Risk Register v4 — paste the full RK-xx list with identifiers, titles, categories, and short descriptions
- The design proposal, described precisely

**Input to the assistant:** Paste the risk register and describe the design choice clearly.

**Example prompt:**

```
Here is the RAHP risk register for a decentralised trust community system:

[paste RK-xx list with titles and descriptions]

A spec author has proposed the following design change:

"Revocation status should be published as a publicly readable bitstring status 
list, with each member's position in the list derived deterministically from 
their DID."

For each risk in the register, assess:
1. Does this design choice increase the severity or likelihood of this risk? 
   If so, briefly explain how.
2. Does it decrease the severity or likelihood? If so, how.
3. Does it have no meaningful effect?

Present your assessment as a table:
Risk ID | Direction (increase / decrease / neutral) | Brief rationale

Flag any risks where you are uncertain and note why.
```

**Expected output:** A structured table of all 35 risks with direction and rationale. Likely flags include RK-PV01 (M-DID linkability) and RK-HX03 (reputational harm from public revocation) as increases. The table is a rapid first-pass for working group discussion, not a final assessment.

**Human review required:** Risk scoring (severity × likelihood) is a human judgement, not derivable from description alone. The table identifies which risks to discuss — the group scores any changes. New risks surfaced by the design choice that are not in the existing register need to be identified by a human reading the assistant's rationale column.

---

## Task 4 — Drafting a user story from an objectives map

**Workflow stage:** Stage 2 (Drafting)

**When to use this:** You have a validated objectives map for a persona and need to draft user stories in the standard RAHP format for a specific lifecycle phase.

**Toolkit components used:**
- Objectives map (Phase D output)
- Existing user stories — paste US-01 to US-03 as format references
- Relevant risk register entries for the persona

**Input to the assistant:** Paste the objectives map, format reference user stories, and the most relevant risk register entries.

**Example prompt:**

```
Here are three example user stories from the RAHP User Stories Framework, 
showing the required format:

[paste US-01, US-02, US-03]

Here is the objectives map for persona D3 (Ahmed Khan, new member seeking 
inclusion), covering Phase 3 and Phase 4 of the VTC bootstrapping lifecycle:

[paste objectives map extract for D3]

Here are the risk register entries most relevant to D3:

[paste RK-ID02, RK-HX01, RK-HX02, RK-SC01]

Draft two user stories for D3 covering:
1. Phase 3: applying for membership through the web-of-trust threshold process
2. Phase 4: completing identity verification without disclosing more than the 
   minimum necessary

Each user story should follow the format: "As [persona], I need [capability] 
so that [objective]. The story must address [specific risk] by [mechanism]." 
Include acceptance criteria as a short bulleted list.
```

**Expected output:** Two user story drafts in RAHP format with acceptance criteria. These feed directly into the User Stories Framework as candidate additions, subject to working group review.

**Human review required:** Check that the acceptance criteria are specific and testable — the assistant will sometimes produce acceptance criteria that are aspirational rather than verifiable. Check that the risk linkage is accurate. Working group review required before committing.

---

## Task 5 — Identifying gaps in persona coverage

**Workflow stage:** Phase D (context validation) and Stage 5 (Maintenance — periodic extreme user review)

**When to use this:** You want to check whether the current persona set has adequate coverage across lifecycle phases and harm categories, or whether a new working context surfaces participant types not currently represented.

**Toolkit components used:**
- Full persona set — paste all 11 persona summaries (D1–D6, M1–M2, B1–B3)
- Risk Register harm categories
- Lifecycle phase map
- Description of any new working context if checking for a different system

**Input to the assistant:** Paste the full persona set with brief summaries, the harm category list, the lifecycle phases, and (optionally) a description of the new system context.

**Example prompt:**

```
Here is the RAHP persona set:

[paste all 11 personas: D1–D6, M1–M2, B1–B3 with brief summaries]

Here are the eight risk categories in the RAHP risk register:
Identity · Credential · Governance · AI Agent · Privacy · External · 
Human Experience · Systemic

Here are the VTC bootstrapping lifecycle phases:
Phase 1 (Genesis) · Phase 2 (Anchor Seeding) · Phase 3 (Member Admission) · 
Phase 4 (Open Membership) · Revocation & Expiration

Produce a coverage matrix: for each combination of lifecycle phase and risk 
category, identify which persona(s) have their primary risk exposure there. 
Where a cell has no persona, flag it as a potential gap.

Then assess: given that this toolkit is intended to be generalisable beyond 
the DTG context, what participant types are most conspicuously absent? 
Consider: non-human actors beyond M1 and M2, participants in the Global South, 
participants with low digital literacy, participants in regulated industries 
(healthcare, finance) where credential misuse has distinct legal consequences.
```

**Expected output:** A coverage matrix (lifecycle phases × risk categories) with gap cells flagged, plus a short prose section identifying the three to five most analytically significant absent participant types. Useful both for Phase D validation and the periodic extreme user review in Stage 5 maintenance.

**Human review required:** The coverage matrix is a mechanical mapping task that the assistant does reliably. The gap assessment is more analytical and requires human judgement about which gaps matter most for the specific system being governed. the assistant's suggestions about absent participant types are starting points for a conversation, not conclusions.

---

## What not to use the assistant for

**Risk scoring.** Severity and likelihood scores require contextual judgement about the specific system, deployment environment, and threat actors. the assistant will produce numbers if asked, but they are not reliable. Score risks in the working group, not with an AI.

**Guardrail verification.** An assurance test result — pass or fail — is an evidential claim about an operational system. the assistant cannot observe your system. AT-xx results are human-verified or tooling-verified, not AI-assessed.

**Governance decisions.** Which risks to formally accept, which design choices to adopt, which personas are representative — these are working group decisions with accountability behind them. the assistant can prepare the material for those decisions, not make them.

**Fieldwork.** the assistant cannot tell you who is missing from your participant map. It cannot substitute for direct engagement with harm-exposed communities. It can help you structure what you learn from that engagement, but not replace it.

**Source verification.** Always verify citations that the assistant provides in persona insights sections. The practical workflow: ask the assistant to flag uncertain citations explicitly (the prompts above do this), then verify before committing.

---

## Contributing improvements to this document

This is a first draft, written in April 2026, based on practical experience developing the RAHP v1 toolkit. It will need updating as both the toolkit and AI tooling evolve.

If you have found a useful prompt pattern not covered here, or found that one of these prompts produces poor results in practice, please open an issue or pull request on the RAHP Toolkit repository. The feedback loop between practitioners and the toolkit is one of the most important things we are trying to build. This document is part of that loop.

---

*RAHP Toolkit · CC-BY 4.0 · portable guidance*
