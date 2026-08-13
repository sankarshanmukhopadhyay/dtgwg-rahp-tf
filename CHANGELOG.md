---
layout: default
title: "Changelog"
nav_order: 24
has_toc: true
---
# Changelog

## [v0.4.0] — 2026-08-13

### Added

- `RP-*` governance rule profiles, with `RP-001` encoding the proposed ROADMAP Q3/Q4
  risk-acceptance authority and review model while remaining explicitly unratified.
- `EV-*` evidence artefacts, providing first-class contracts for evidence source,
  collector role, collection time, URI/hash, retention and sensitivity.
- Five proposed operational-monitoring contracts for `M-02`, `M-04`, `M-06`, `M-08`
  and `M-27`, each linked to an evidence contract and triage responsibility.
- Operational assurance documentation with assurance-chain, triage-state and responsibility
  diagrams.
- Deterministic normative-triage workbench generated from canonical data without
  auto-assigning standards status.
- Portable non-human actor taxonomy for autonomous agents, supervised agents, and
  automated pipelines.
- Machine-validatable delegation-scope schema and worked example, keeping delegated
  authority separate from liveness, identity, and key control.
- v0.4.0 release notes and release navigation.

### Changed

- Toolkit version is now `v0.4.0`; historical worked reviews retain the RAHP version
  against which they were originally performed.
- The canonical reference catalogue and JSON-LD build now include rule profiles and
  evidence artefacts.
- Validation now checks operational assurance consistency and reports pilot/evidence/profile
  coverage as part of the task-force work queue.
- All 31 asymmetric risk/control/guardrail references have been reconciled bidirectionally.
- `CT-51`, `CT-52`, and `CT-53` are no longer orphaned: their existing declared risk and
  guardrail relationships are now mirrored by the corresponding canonical records.

### Governance status

- `RP-001` remains `proposed`.
- The five monitoring contracts remain `pilot_proposed`.
- The 87 control/guardrail standards-status decisions remain human Task Force work.
  v0.4 provides decision support rather than inventing those decisions.


## Unreleased — scenario-driven RAHP and JTD documentation

- Added portable scenario patterns and a validated external scenario-corpus adapter model.
- Added the DTG ZKP 30-use-case corpus as the first scenario-driven RAHP reference adapter.
- Added a 16-scenario Trust Tasks corpus grounded in framework proof, identity, replay, versioning, transport, privacy and delegation semantics.
- Added a 16-scenario DTG Credential Specification corpus grounded in relationship, lifecycle, registry, privacy, task-context, interoperability and accessibility semantics.
- Added a 12-scenario RAHP-owned Trust Tasks × Credential Spec composition corpus for emergent cross-specification failure modes.
- Added scenario coverage and cross-specification pressure-testing documentation.
- Extended pressure-test findings with optional scenario, scenario-pattern and persona traceability.
- Added corpus validation to the standard validation workflow.
- Added Just the Docs configuration and an official GitHub Pages artifact build/deploy workflow using `configure-pages`, `upload-pages-artifact` and `deploy-pages`.
- Added publishing guidance and retained Mermaid rendering for the JTD site.
- Added a corpus source registry (`corpora/sources.yaml`) with explicit source, portfolio relationship, update mode and provenance policy.
- Added scheduled source-drift detection and manual corpus review-packet workflows, including live cross-checks against the DTG Portfolio Monitor repository registry.
- Added immutable-pin and composed-corpus dependency semantics without falsely rebasing legacy `archive-snapshot` corpora.
- Added corpus synchronization/provenance documentation and an AI-agent corpus-maintenance workflow.


## Unreleased

- Added unified `tools/review.py` orchestration with `rahp`, `security`, and `combined` modes; CI-safe in-progress scaffolds; generated cross-lens synthesis; and combined-review validation. — adoption architecture and specification pressure-testing workflow

- Reorganized the repository into the documented `method/`, `data/`, `tools/`, `context/`, `build/`, `docs/`, `examples/`, and `archive/` architecture.
- Reframed the README around task-oriented adoption paths and added repository, lifecycle, artefact-relationship, and disposition diagrams.
- Added first-class guidance for specification pressure testing, result interpretation, governance boundaries, and minimum viable RAHP adoption.
- Replaced the illustrative DTG Credential Specification placeholder with a substantive Working Draft 01 pressure test containing eight traceable findings and explicit re-test triggers.
- Added a second substantive worked pressure test for the Trust Tasks Framework editor's draft 0.3, covering replay/idempotency, freshness, portable delegation, draft immutability, registry dependency, capability negotiation, delegated-execution consent and supported representation.
- Added YAML-to-Markdown pressure-test rendering: `pressure-test.yaml` remains canonical, `tools/render_pressure_tests.py` maintains structured generated README sections, and validation now fails when rendered Markdown is stale.
- Added a canonical deep-linkable RAHP Reference catalogue and repository-wide generated reference links: pressure-test citations now render as ID + title hyperlinks, generated site pills resolve to stable catalogue anchors, and `tools/validate_reference_links.py` checks catalogue/link integrity.
- Added a coordinated security-hardening review programme with 38 machine-readable findings across Trust Tasks, DTG Core Credentials, and cross-spec composition; added adversarial review methodology, rendering, validation, control-plane vocabularies, and closure-test evidence.\n- Added a standards-backed security crosswalk: canonical external-source registry for NIST, W3C, and OWASP; 96 structured alignments across all 38 security findings; relationship-strength vocabulary; rendered hyperlinks/coverage summaries; and validation of external references.
- Added `tools/validate_pressure_tests.py` and `examples/pressure-test-template.yaml` so worked reviews are reproducible, commit-pinned, disposition-controlled and referentially valid against the canonical RAHP corpus.
- Retained the minimal-instance review record as the smallest adoption pattern.
- Added a controlled finding-disposition vocabulary so review findings can be routed to the correct control plane.
- Moved legacy spreadsheets/documents and historical generated outputs out of the primary navigation path while preserving provenance.
- Moved GitHub workflow/templates to `.github/` and made CI fail when committed generated evidence is stale.

All notable changes to the RAHP Toolkit. Versions are toolkit versions; the
specification version each one was assessed against is recorded in
`data/instance.yaml`.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project uses a single toolkit version rather than per-artefact versions —
the previous scheme (User Stories Framework v6, Risk Register v5, HTML site
unversioned) made it impossible to say which state of the toolkit a given
review was based on.

## [Unreleased] — v0.3-dev

### Added

- **Canonical YAML data model** under `data/`. Nine artefact types migrated from
  `DTG_RAHP_Risk_Register_v5.xlsx` and `DTG_RAHP_User_Stories_Framework_v6.xlsx`
  with no content loss: 43 risks, 66 controls, 21 guardrails, 21 assurance tests,
  37 metrics, 36 user stories, 33 scenarios, 21 EPICs, 16 personas.
- **Three new record types**, extracting content that previously existed only as
  prose inside single spreadsheet cells:
  - `data/recommendations.yaml` — REC-1 to REC-9, from the Analysis & Conclusions sheet
  - `data/risk-acceptances.yaml` — RA-001 to RA-003, all `pending` (see GAP-3.1)
  - `data/governance-precedents.yaml` — GP-001 to GP-003, all `proposed`
- **`method/` directory** separating the portable RAHP method from the DTG
  instance, so another working group can adopt the method without inheriting DTG
  content.
- **`method/lifecycle.yaml`** — the five-stage standards lifecycle converted from
  hand-maintained HTML to data, with every gap callout as a tracked record
  (`GAP-1.1` … `GAP-5.5`) carrying a severity.
- **`method/vocabularies.yaml`** — controlled vocabularies for severity,
  likelihood, standards priority, standards status, normative language, control
  type, persona type and acceptance decision.
- **`tools/validate.py`** — schema, vocabulary, identifier, referential
  integrity, symmetry, invariant, orphan and README count checks. Configuration
  is read from `data/instance.yaml`; no working-group-specific logic is
  hard-coded.
- **`tools/build.py`** — generates the HTML site, JSON-LD, a JSON bundle, derived
  cross-references and `build/normative.md` from `data/`.
- **JSON-LD context** at `context/rahp.jsonld`, giving every RAHP identifier a
  resolvable IRI under `https://trustoverip.github.io/dtgwg-rahp-tf/id/`.
- **`standards_status` and `normative_language` fields** on every control and
  guardrail. All 87 are deliberately `unassigned` — assigning them is a task force
  decision, and the importer records the gap rather than guessing.
- **`monitoring` hook** on every metric, `null` pending the v0.4 runtime layer.
- **CI workflow, issue templates, PR template, CONTRIBUTING.md, this file.**
- **Two new generated views**: a standards pipeline page showing what is awaiting
  triage, and a governance page showing acceptances and precedents.

### Changed

- **`Critical` is now a distinct severity class**, not a higher number. Critical
  risks carry no numeric score, must be gated by a guardrail, and may not be
  risk-accepted. Enforced by invariant `INV-3`. Affects `RK-EX04`.
- **Persona cross-references are now computed**, not stored. `data/personas.yaml`
  carries narrative and evidence only; links to user stories, scenarios, EPICs,
  metrics and risks are derived at build time.
- **Filenames no longer carry version numbers.** Git tags carry versions.

### Fixed

- **Metric namespace desynchronisation.** The Risk Register v5 defined M-01–M-18
  and M-31–M-37 while the User Stories Framework v6 defined M-01–M-37. The two
  workbooks disagreed about the shared identifier space they were supposed to
  share. The union is now a single file.
- **Persona cross-reference column shift.** Rows D2, D3, D5, M2 and B1 of the v6
  Persona Cross-Reference sheet had a missing Type value, shifting every
  subsequent column. Eliminated by deriving the cross-references.

### Known issues surfaced by the new validator

These are reported as warnings and are open work, not migration defects:

- **31 asymmetric cross-references** — a risk cites a guardrail that does not cite
  it back, or a guardrail cites a control that does not cite it back. Affects
  RK-SC03, RK-CR04, RK-G05, RK-HX05, RK-HX06, RK-ID06, RK-EX04, RK-EX06, RK-SC05,
  GR-03, GR-04, GR-06, GR-08, GR-12, GR-20, GR-21 among others.
- **3 orphaned controls** — CT-51, CT-52 and CT-53 are defined but referenced by
  no risk and no guardrail.
- **28 risks marked `must_address`** with no acceptance pathway available.
- **37 metrics with no runtime monitoring definition** (expected; v0.4 scope).

## Prior artefact versions

Recorded for continuity. These predate the single-version scheme.

| Artefact | Version | Date | Change |
|---|---|---|---|
| Risk Register | v5 | 2026-08 | Edge-case personas: 8 new risks (RK-HX04–06, RK-ID06, RK-EX04–06, RK-SC05), 10 new controls (CT-57–66), 3 new guardrails (GR-19–21), 3 new assurance tests (AT-19–21); `Critical` severity introduced |
| User Stories Framework | v6 | 2026-08 | EC1–EC4 edge-case personas; US-13–36, SC-13–33, EPIC-14–21, M-19–37 added |
| Workflow Reference | v1 | 2026-04 | Five-stage lifecycle with gap annotations |
| AI-Assisted Process guide | v1 | 2026-04 | Five worked examples |
| Risk Register | v4 | 2026-03 | DTG Credential Spec v0.3 review: 4 new risks, 8 new controls, 1 guardrail, 1 assurance test |
| User Stories Framework | v3 | 2026-03 | Three pivot sheets; metric IDs replace persona columns as the cross-reference standard |
| HTML reference site | v1 | 2026-03 | Initial release |
