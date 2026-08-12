# RAHP Toolkit Roadmap

Status: draft for task force review
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

So the repository is split: `method/` is portable and contains no DTG content;
`data/` is the DTG instance. Adopting RAHP for another specification is `fork, keep
method/ and tools/, replace data/`. Without this split, "reusable methodology" means
"read our spreadsheets and infer the method", which is what it currently means.

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

### v0.3 — machine-readable model, validation, contributor readiness · **delivered as draft**

- [x] YAML data model for nine artefact types; `method/` vs `data/` split
- [x] Three new record types: recommendations, risk acceptances, governance precedents
- [x] `validate.py` with eight check classes, driven by `instance.yaml`
- [x] `build.py` producing the site, JSON-LD, JSON bundle and normative action set
- [x] JSON-LD context with resolvable identifiers
- [x] `standards_status` / `normative_language` fields, all `unassigned`
- [x] Lifecycle and gaps as data
- [x] CI, issue and PR templates, CONTRIBUTING, CHANGELOG, this roadmap
- [x] Reproducible specification pressure-test records with a reusable template and canonical-reference validator
- [ ] **Task force: triage the 87 unassigned controls and guardrails** ← the real work
- [ ] **Task force: resolve the 31 asymmetries and 3 orphaned controls**
- [ ] Ratify GP-001 to GP-003 as precedent
- [ ] Publish the site to GitHub Pages from `build/`

### v0.4 — operational governance layer

Blocked on Q3/Q4 for the acceptance half; blocked on practitioner trial input for
the monitoring half, as the proposal correctly noted.

- [ ] Risk acceptance authority model → unblocks `data/risk-acceptances.yaml` and AT-17
- [ ] `monitoring` populated for the five highest-priority metrics, with thresholds,
      triage workflow references, responsible roles and notification SLAs
- [ ] Triage workflow specifications for those five
- [ ] AI agent delegation scope constraint schema (moved from v0.4 per above, if agreed)
- [ ] Non-human actor classification taxonomy: autonomous / supervised / automated pipeline
- [ ] Operator VMC liveness check protocol
- [ ] Revocation and notification SLA structures
- [ ] Practitioner trial report

### v0.5 — reuse

- [ ] A second instance under a different working group, proving `method/` is portable
- [ ] Method documentation as a standalone deliverable
- [ ] Conformance claim template for "assessed using RAHP v0.x"

## Open questions

Answering Q1 below unblocks nothing further; it is settled. Q2 to Q5 are live.

**Q1 — Canonical format.** *Settled: YAML authoring, JSON-LD build output.*
Contributors write YAML because the alternative is that non-engineers stop
contributing, and the personas are the part that most needs non-engineer
contribution. `tools/build.py` emits JSON-LD with resolvable identifiers under
`https://trustoverip.github.io/dtgwg-rahp-tf/id/`, so RAHP IDs can be referenced
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

**Q3 — Evidence thresholds for risk acceptance.** Yes, this is a DTGWG risk
appetite decision. Proposed starting profile, for the task force to amend:

| Risk score | Acceptance requires |
|---|---|
| Critical severity | Not acceptable. Guardrail required. |
| High × High (9) | Full working group vote, documented rationale, 6-month review |
| High severity (3–6) | Task force co-chair sign-off, 12-month review |
| Medium and below | Task force decision, recorded, 12-month review |

**Q4 — Acceptance authority.** Follows from Q3. The useful framing from the thread
is the lightweight *rule profile* a working group adopts when it picks up the
toolkit: which controls are mandatory, optional or context-dependent for its own
risk appetite; who signs. That profile belongs in `data/instance.yaml` as an
instance-level declaration, so it is machine-readable and differs legitimately
between adopters. Proposed as a v0.4 schema addition.

**Q5 — AI agents as contributors to RAHP itself.** Yes. `CONTRIBUTING.md` now
requires `provenance.contributor: "<name> (AI-assisted)"` on records substantially
drafted by an assistant — not as a warning label, but so a reviewer can calibrate
how much independent verification a record needs. Risk scoring, guardrail
verification and governance decisions remain out of scope for assistants, per the
existing AI-assisted process guide. Reviewing this with the ToIP AI & Human Trust
WG and the DIF agents work, as suggested in the thread, is worth doing before v0.4.

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
| evidence artefact | **not yet implemented** — the missing piece |

The evidence artefact record (URI/hash, collector, timestamp, retention class,
sensitivity label) is the right idea and is deferred to v0.4, where it belongs
alongside the monitoring layer: an assurance test result is only meaningful if the
evidence it was based on is addressable. The three-layer rule profile — core object
rules, working-group adoption rules, runtime-readiness rules — is a good frame for
Q4 and is reflected in the instance-level rule profile proposed above.
