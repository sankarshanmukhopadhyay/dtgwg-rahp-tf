---
layout: default
title: "Roadmap"
nav_order: 23
has_toc: true
---
# RAHP Toolkit Roadmap

## v0.8.0 — Language-neutral Engine Boundary (complete)

v0.8 turns the lifecycle established in v0.7.1 into an explicit implementation contract. The portable method now defines engine operations, a normalized result schema, implementation-neutral conformance fixtures and review-evidence retention semantics.

Status: release baseline. Python remains the current reference adapter, but its internal module structure is not normative. New review runs default to ignored `.rahp/` workspaces; durable Git state is limited to compact dispositions/evidence manifests and explicitly promoted exemplars.

Key boundary:

`method + schemas + fixtures → conforming engine → normalized result → retention/disposition`

Next candidate: **v0.9 TypeScript reference SDK**, with generated types, graph traversal and programmatic APIs implemented against this contract. Rust/WASM remains a later option when static-binary, embedding or performance requirements justify a second implementation.

---

## v0.7.1 — Assessment Queue Consolidation (complete)

v0.7.1 closes the operational gap exposed by the first live situational-assurance queue: an observation is not automatically a new assessment. Repository and selected-issue events now carry stable assessment identity, related triggers coalesce into an open repository assessment, and durable review records preserve the reviewed revision and disposition.

Status: release baseline; the initial DTG generated queue is dispositioned through two durable assessments, while unresolved upstream dependencies remain watched without being confused with independent RAHP findings.

Key execution model established for the next engine boundary:

`source → observation → trigger → assessment → finding → disposition → baseline`

---

## v0.7.0 — Composition and Situational Assurance (complete)

CAWG/C2PA now exercises scenario-driven, cross-specification, security and combined review modes with mandate-readiness evidence, while both CAWG/C2PA and DTG use deployment-owned selected-issue situational monitoring alongside repository drift.

Status: v0.7.0 release baseline; RAHP Toolkit operates independently governed DTG and CAWG/C2PA deployments, with CAWG exercising scenario, composition, security and combined assurance and both deployments exercising independent situational-assurance workflows

Supersedes: the roadmap proposal in DTGWG discussion #3 (April 2026), which it
largely adopts. Where it departs, the reasoning is stated.

---

## The problem this roadmap actually solves

The v0.2 proposal framed the problem as "everything lives in spreadsheets, Word
documents and HTML files; there is no machine-readable source of truth". That is
true but it is a description of the *mechanism*. The consequence is what matters,
and the consequence is now measurable.

Between April 2026 and August 2026 the toolkit grew from 37 risks to 43, from 58
controls to 66, from 18 metrics to 37. During that growth:

- the two workbooks **stopped agreeing about the metric namespace** — the shared
  identifier space that the entire toolkit is supposed to hang from. The Risk
  Register defined M-01–M-18 plus M-31–M-37; the User Stories Framework defined
  M-01–M-37. Twelve metrics existed in one authoritative source and not the other;
  the Risk Register's own pivot sheet had columns for metrics its own definitions
  sheet did not contain.
- **31 cross-references became asymmetric** — a risk citing a guardrail that does
  not cite it back.
- **three controls became orphaned** — CT-51, CT-52 and CT-53 are defined and
  referenced by nothing.
- the **HTML site drifted to a different risk count** from the workbooks it was
  generated from, while still describing itself as current.
- five rows of the persona cross-reference sheet **lost a column** to a missing
  cell value, silently shifting every subsequent field.

None of this was caught by review. It is not a competence problem — it is the
predictable failure mode of maintaining a graph of ~300 interlinked records by
hand across two spreadsheets, two documents and four HTML files. This roadmap's
justification is not elegance. It is that the toolkit had already begun to
contradict itself, and nobody could tell.

## Adopted from discussion #3, with amendments

| Proposal | Decision |
|---|---|
| §1 Single source of truth in YAML | **Adopted.** See Q1 below for the format decision. |
| §2 Schema validation and consistency checks | **Adopted and extended.** See "what the validator also checks". |
| §3 Repository consistency cleanup | **Adopted**, folded into v0.3 rather than run as a separate v0.2. |
| §4 Lifecycle as data | **Adopted and extended** — gaps become tracked records with severity, not prose. |
| §5 Normative candidate pathways | **Adopted** with one change: no status is auto-assigned. All 87 controls and guardrails import as `unassigned`. |
| §6 Formal risk acceptance model | **Adopted structurally, blocked substantively.** Schema exists; every record is `pending` until Q3 and Q4 are answered. |
| §7 Governance precedent records | **Adopted.** Three seeded from the v0.3 spec review. |
| §8 Runtime governance coverage | **Deferred to v0.4** as proposed, with a `monitoring: null` hook on every metric so the shape is fixed now. |
| §9 AI agent governance expansion | **Deferred to v0.4**, and see "the sequencing disagreement" below. |
| §10 Contributor experience | **Adopted**, folded into v0.3. |
| §11 v0.2 / v0.3 / v0.4 milestones | **Amended** — v0.2 and v0.3 are merged. See below. |

### Amendment 1: merge v0.2 into v0.3

The proposal put repository housekeeping in v0.2 ("no dependencies, immediate
value") and the data model in v0.3. In practice most of the v0.2 list is either
produced by the migration or made trivial by it:

- README count alignment is a validator check, not a manual task — and manual
  alignment would have drifted again within a month.
- The CHANGELOG has to be written against a data model that exists, or it
  documents artefacts that are about to be restructured.
- Filename normalisation is resolved by the naming convention, which is a
  CONTRIBUTING.md decision that only makes sense once `data/` exists.

Doing housekeeping first means doing it twice. The merged v0.3 is delivered.

### Amendment 2: separate the method from the instance

This is the substantive addition to the proposal, and it follows from the goal of
RAHP being reusable by other working groups.

The discussion treats RAHP as one repository of DTG artefacts. But the thing worth
publishing is the *method* — the persona discipline, the control/guardrail/assurance
hierarchy, the lifecycle with its evidence requirements, the invariants. The DTG
risk register is a worked example of it.

The repository therefore separates portable method from deployment state. `method/` contains the reusable semantics; `profiles/<id>/` declares targets; `instances/<id>/` may hold deployment-owned state, reviews and local assurance vocabulary. Root `data/` remains the bundled DTG exemplar catalogue for compatibility, but v0.5 and v0.6 supersede the old "fork and replace data/" adoption model. A new adopter supplies configuration and only adopts deployment data it explicitly chooses.

### Amendment 3: no auto-assigned normative status

The proposal's §5 example shows `CT-08` importing with `standards_status:
normative_candidate` and `normative_language: MUST`. The Analysis & Conclusions
sheet does support that for a handful of items. It does not support it for the
other 80.

Assigning normative status to 87 controls and guardrails is a working group
decision with standards consequences. An importer that guesses produces a file
that *looks* triaged and is not — the worst possible outcome, because nobody
re-checks a field that is already populated. Every item therefore imports as
`unassigned`, and the validator reports the count on every run: **87 awaiting
triage**. The gap is visible and countable. Closing it is task force work, and it
is the highest-value work in v0.3.

### The sequencing disagreement: AI agent governance

The proposal places AI agent expansion in v0.4, after the operational monitoring
layer. There is a case for pulling the *specification-facing* half of it forward.

All four AI agent risks are High severity. `RK-AI02` (stale agent after operator
revocation) and `RK-AI01` (scope creep) need normative provisions in the credential
specification, and the specification is being drafted now. The delegation scope
constraint schema and the non-human actor taxonomy are specification work, not
runtime work — they do not depend on the monitoring layer. The misuse detection
playbook does, and can stay in v0.4.

Recommendation: move the delegation credential scope schema and the non-human actor
classification taxonomy into v0.3 as REC-2 deliverables; leave detection and
response in v0.4.

## What the validator checks beyond the proposal

The proposal listed referential integrity, orphans, duplicate IDs and README
counts. Added:

- **Vocabulary conformance** — severity, likelihood, standards status, normative
  language, control type, persona type and acceptance decision must hold permitted
  values. Prevents `High`/`high`/`HIGH` drift, which had already begun.
- **Bidirectional symmetry** — if a risk cites a guardrail, the guardrail must cite
  the risk. This is the check that found the 31 asymmetries.
- **Method invariants**, expressed as data in `data/instance.yaml`:
  - every guardrail has an assurance test (a guardrail without a test is unverifiable)
  - every control reaches a metric (a control without a signal is unmonitorable)
  - a Critical risk is gated by a guardrail and may not be risk-accepted
  - a `must_address` risk has a guardrail or an acceptance record

  These are the toolkit's own rules from the Workflow Reference. Encoding them as
  executable checks is what turns a documented method into an enforced one.

## Milestones

### v0.3 — machine-readable model, validation, contributor readiness · **delivered**

- [x] YAML data model and `method/` vs `data/` split
- [x] Recommendations, risk acceptances, and governance precedents as records
- [x] Schema, vocabulary, identifier, reference, symmetry, invariant, orphan, and count validation
- [x] Generated HTML, JSON, JSON-LD, normative action set, and stable reference catalogue
- [x] Reproducible pressure-test records and review rendering
- [x] Security-hardening and combined-review lenses
- [x] Scenario corpora and portable scenario patterns
- [x] GitHub Pages / Just the Docs publication
- [x] AI-agent pressure-test guidance
- [x] Corpus provenance and related-repository drift detection
- [x] Historical Library published as explicitly non-canonical reference material
- [x] Resolve the 31 asymmetric cross-references
- [x] Resolve the 3 orphaned controls
- [ ] **Task force: decide canonical standards status for the 87 controls/guardrails**
- [ ] Ratify or revise GP-001 to GP-003 as precedent

v0.4 keeps the last two items visible as governance work rather than blocking the
toolkit's operational-assurance machinery.

### v0.4.0 — governed and observable assurance · **release**

The v0.4 release establishes the first operational layer without claiming that a
specific deployment or governance body has adopted the proposed operating profile.

- [x] Add `RP-*` governance rule-profile records
- [x] Encode the Q3/Q4 proposed risk-acceptance authority model as `RP-001`
- [x] Keep `RP-001` explicitly `proposed` until human ratification
- [x] Add first-class `EV-*` evidence artefact records
- [x] Add five proposed metric monitoring contracts (`M-02`, `M-04`, `M-06`, `M-08`, `M-27`)
- [x] Link pilot metrics to explicit evidence contracts
- [x] Add operational-assurance validation and generated evidence views
- [x] Add deterministic normative-triage decision support without auto-assigning status
- [x] Add state-flow and swimlane documentation for runtime triage
- [x] Add portable non-human actor classification taxonomy
- [x] Add machine-validatable delegation scope constraint schema and worked example
- [x] Publish v0.4.0 release notes and update reader navigation
- [ ] **Task force: ratify/revise `RP-001`**
- [ ] **Task force: activate or revise the five pilot monitoring contracts**
- [ ] Practitioner trial of the operational-assurance loop
- [ ] Populate real `uri`, `digest`, and `collected_at` fields from trial evidence

The distinction is deliberate: **v0.4.0 delivers the mechanism and proposed profile;
ratification and runtime evidence remain accountable human/implementation work.**

### Task Force governance queue — generated, not hidden in roadmap prose

Starting with v0.5 development, unresolved governance work is maintained as an
**itemized generated register** rather than as aggregate roadmap reminders. The
register is derived from canonical record state and published at
`build/site/task-force-actions.html`.

It currently includes every control/guardrail awaiting standards triage, proposed
rule profiles such as `RP-001`, proposed governance precedents, pending risk
acceptances, and proposed monitoring contracts. A record disappears from the queue
only when its canonical state is changed through an accountable decision.

This means the roadmap can describe **milestones**, while the generated Task Force
Action Register carries the live decision inventory.

### v0.5 — configuration-driven portable assessment · **release scope complete**

v0.5 changes the portability boundary. An adopter no longer proves portability by
copying `method/` and `tools/` into a separately governed RAHP instance. Instead, the
portable engine accepts a schema-validated YAML profile listing one or more target
repositories, their assessment context and scope, and the review modes permitted for
each target. The DTG deployment is the bundled exemplar of this engine.

- [x] Define `method/schema/rahp-config.schema.json` as the portable configuration contract
- [x] Add `tools/rahp.py` as the neutral configuration-driven CLI
- [x] Support one or many configured repository targets
- [x] Support pinned commits, local Git checkouts, and remote branch resolution
- [x] Support per-target `rahp`, `security`, and `combined` modes
- [x] Support target include/exclude scope and contextual metadata
- [x] Add `profiles/dtg/rahp.yaml` so DTG is an exemplar deployment, not an engine dependency
- [x] Keep DTG Portfolio Monitor integration optional under deployment extensions
- [x] Add non-DTG minimal, multi-repository, and security-only examples
- [x] Add a synthetic non-DTG portability fixture and CI validation
- [x] Prove the portable fixture does not require DTG corpora, governance issues, `RP-001`, or DTG instance data
- [x] Add a generic configured-review GitHub Actions workflow
- [x] Preserve existing DTG validators/renderers and evidence without a disruptive migration
- [x] Capture a substantial external specification-portfolio deployment as field evidence (CAWG/C2PA in v0.6)
- [ ] Publish a practitioner trial report with real evidence artefacts
- [ ] Populate real evidence URI/digest/timestamp fields from field use
- [ ] Ratify at least one rule profile and activate at least one monitoring profile in a deployment that chooses to use those RAHP governance features

The unchecked items are **field-evidence objectives**, not blockers to the v0.5
software portability claim. Architectural portability is proven by configuration: a
non-DTG adopter can checkout RAHP, add one YAML file, and use the review machinery
without modifying or running DTG-specific instance material.

## v0.6.0 — External deployment proof and neutral project identity

**Status: delivered.** v0.6 turns the v0.5 portability contract into evidence from a materially different specification ecosystem.

- [x] Rename/decouple the fork as `rahp-toolkit` while preserving DTG provenance.
- [x] Add a CAWG/C2PA profile using the same portable YAML configuration contract.
- [x] Track multiple branches of a repository independently where experimental specification work requires it.
- [x] Complete initial RAHP pressure tests for the principal CAWG/C2PA specification surfaces.
- [x] Add a reusable static-profile change monitor for non-DTG deployments.
- [x] File deduplicated `assessment-required` issues when material tracked paths change.
- [x] Persist observed revisions so scheduled runs advance the assessment baseline rather than repeatedly reopening the same delta.
- [x] Keep DTG discovery/portfolio metadata instance-specific and keep CAWG/C2PA governance authority upstream.

**Next field objective:** convert selected open CAWG/C2PA findings into upstream-discussion-ready evidence only after human review confirms the finding and appropriate control plane. RAHP should not automatically file findings against upstream projects.

## Open questions

Answering Q1 below unblocks nothing further; it is settled. Q2 to Q5 are live.

**Q1 — Canonical format.** *Settled: YAML authoring, JSON-LD build output.*
Contributors write YAML because the alternative is that non-engineers stop
contributing, and the personas are the part that most needs non-engineer
contribution. `tools/build.py` emits JSON-LD with resolvable identifiers under
`https://sankarshanmukhopadhyay.github.io/rahp-toolkit/id/`, so RAHP IDs can be referenced
normatively by other specifications without anyone hand-writing JSON-LD. This is
reversible: if JSON-LD authoring later becomes necessary, the YAML becomes the
derived view and nothing downstream changes.

**Q2 — Normative scope.** Proposed answer: RAHP is a methodology toolkit, and a
conformance claim is made *against the method*, not against RAHP's DTG content. A
VTC cannot claim "conformance to RAHP"; a working group can claim "this
specification was assessed using RAHP v0.3, with these guardrails and these signed
acceptances". That keeps the fuzzy human-experience edges honest — as noted in the
discussion thread — while giving the core something checkable. The normative core
is the *process obligation*: every risk is either controlled or formally accepted,
every guardrail has a test, every control has a signal.

**Q3 — Evidence thresholds for risk acceptance.** *Mechanism implemented in v0.4; governance decision remains open.*
The proposed starting profile below is now machine-readable as `RP-001`. It remains
`proposed`, not ratified:

| Risk score | Acceptance requires |
|---|---|
| Critical severity | Not acceptable. Guardrail required. |
| High × High (9) | Full working group vote, documented rationale, 6-month review |
| High severity (3–6) | Task force co-chair sign-off, 12-month review |
| Medium and below | Task force decision, recorded, 12-month review |

**Q4 — Acceptance authority.** *Mechanism implemented in v0.4; authority remains unratified.*
`RP-001` now makes the proposed authority/review cadence explicit and machine-readable.
The useful framing from the thread
is the lightweight *rule profile* a working group adopts when it picks up the
toolkit: which controls are mandatory, optional or context-dependent for its own
risk appetite; who signs. That profile belongs in `data/instance.yaml` as an
instance-level declaration, so it is machine-readable and differs legitimately
between adopters. Implemented as the v0.4 `RP-*` schema; adoption remains a human governance decision.

**Q5 — AI agents as contributors to RAHP itself.** Yes. `CONTRIBUTING.md` now
requires `provenance.contributor: "<name> (AI-assisted)"` on records substantially
drafted by an assistant — not as a warning label, but so a reviewer can calibrate
how much independent verification a record needs. Risk scoring, guardrail
verification and governance decisions remain out of scope for assistants, per the
existing AI-assisted process guide. Reviewing this with the ToIP AI & Human Trust
WG and the DIF agents work remains useful before an external v0.5 adoption claim is made.

## Relationship to the object model proposed in the thread

The five-record object model proposed in discussion #3 (risk item, control,
assurance test, decision record, evidence artefact) maps onto what is implemented
as follows:

| Proposed | Implemented |
|---|---|
| risk item | `data/risks.yaml` — plus harm type and affected personas, which the proposal omitted and which are the point of RAHP |
| control | `data/controls.yaml` — with the control/guardrail distinction preserved rather than collapsed |
| assurance test | `data/assurance-tests.yaml` |
| decision record | split into `risk-acceptances.yaml` (what was decided about a risk) and `governance-precedents.yaml` (why the toolkit is shaped as it is) |
| evidence artefact | `data/evidence-artifacts.yaml` — implemented in v0.4 as `EV-*` contracts and linked to operational pilot metrics |

The evidence artefact record (URI/hash, collector, timestamp, retention class,
sensitivity label) is implemented in v0.4 as `EV-*` contracts. v0.5 field work now
needs to populate those contracts with real assessment evidence. The three-layer
rule profile — core object rules, working-group adoption rules, runtime-readiness
rules — remains the frame for Q4 and for future independent adopters.
