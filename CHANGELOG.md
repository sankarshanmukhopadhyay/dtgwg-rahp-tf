## [Unreleased]

### Documentation

- Expanded contribution workflows for catalogue, capabilities and specification pressure tests.

### Generated assurance site

- Add portable catalogue and assurance-graph views under `build/site/` for the v1.1 `HRM/RKP/CTP/GRP/ATP/EVP` model.
- Relabel the existing `build/site/` risk, catalogue, normative, matrix, lifecycle, governance, assurance and Task Force views as DTG deployment surfaces.
- Preserve `catalogue.html#RK-*` deep links while distinguishing deployment-local records from portable method patterns.
- Surface catalogue coverage gaps and the current 11-repository HEAD qualification evidence in generated assurance output.

---
layout: default
title: "Changelog"
nav_order: 7
has_toc: true
parent: Reference
---
# Changelog

## Unreleased — semantic governance and guardrail closure

- Add a 56-term RAHP glossary under `method/glossary/terms/`, written in simple English and validated against `method/schema/glossary-term.schema.json`.
- Generate `build/glossary.json`, `build/glossary.md`, `docs/glossary.md` and `build/site/glossary.html` from the authoritative term records.
- Add `guardrail_requirement` to every portable risk pattern so guardrail completeness is explicit and machine-verifiable.
- Expand the portable catalogue from 139 to 149 patterns by adding 10 reusable guardrails and extending two existing guardrails to naturally related risks.
- Reduce required guardrail gaps to zero while keeping `RKP-PE-02` explicitly conditional.
- Update generated assurance coverage so it distinguishes missing required guardrails from conditional or intentionally control-only cases.

## v1.1.0 — 2026-08-17

### Added
- Portable assurance catalogue with 139 reusable harm, risk, control, guardrail, assurance and evidence patterns.
- Catalogue schema, validator and human-readable reference documentation.
- Dedicated Trust Tasks × DTG Credential Specification RAHP cross-specification exemplar and combined review.
- Portable assurance mappings across curated RAHP, security and composed-corpus examples.

### Changed
- Revalidate and rerender curated examples against v1.1.0 while preserving pinned target revisions.
- Expand scenario patterns and cross-spec documentation for authority, delegation, discovery, redress, political economy, lifecycle skew and control side effects.
- Keep `rahp-engine-contract-v1` and result schema version 1 stable; v1.1 is additive.
### Pages rendering refresh
- Preserve canonical `.yaml`, `.json` and `.jsonld` routes as machine-readable structured data instead of replacing those paths with generated HTML.
- Render structured-data reader views on clean sibling routes such as `/corpora/dtg-zkp/` and `/method/catalogue/risk-patterns/` so GitHub Pages serves them through the Just-the-Docs HTML shell.
- Add scenario-corpus and portable-assurance catalogue browser indexes, plus a `/method/catalog/` compatibility route.
- Strengthen post-Jekyll validation to require both canonical structured sources and themed human projections.
- Preserve source-directory relative-link semantics for projected Markdown: `README.md` renders as a directory index, while other Markdown files render as same-directory `.html` siblings instead of nested `.../index.html` routes.

### Qualification refresh
- Qualify all maintained live example repositories against current default-branch HEAD.
- Record longitudinal finding deltas without overwriting the original pinned evidence.
- Resolve the Trust Tasks duplicate-execution, stale-consequential-request and identity-as-authorization findings against current HEAD.
- Resolve Credential Spec `SEC-CR-009` after VWC digest becomes required.
- Reassess the Trust Tasks × Credential Specification composition and confirm no new portable-catalogue pattern is required.


## v1.0.0 — 2026-08-16

### Added
- Stable v1 compatibility and versioning contract for method, engine, normalized results and identifiers.
- Reader-journey documentation hubs for learning, adoption, assessment, operations, implementation, deployments, reference and releases.
- Documentation information-architecture validation.
- Shared lifecycle trigger-correlation fixtures and stronger Python↔TypeScript target-enumeration equivalence checks.
- Implementation-conformance guide and v1.0 release notes.

### Changed
- Current toolkit, deployment-profile, template and TypeScript package metadata advances to v1.0.0.
- The primary Just the Docs navigation is curated by reader task rather than flat page-level `nav_order`.
- v1.0 treats `rahp-engine-contract-v1`, result schema version 1 and evidence-retention policy v1 as stable compatibility boundaries.
- Correct Pages rendering for deployment and durable-review routes by requiring the Just-the-Docs layout on every front-matter Markdown page; harden Mermaid labels and make the A2A detailed assessment a rendered Pages route.
- Strengthen source and post-Jekyll validation so bare HTML fragments cannot pass as valid themed documentation pages.


## v0.9.0 — 2026-08-16

### Added
- TypeScript reference packages for schema/result validation, core profile and retention operations, catalogue graph traversal and CLI access.
- Python↔TypeScript differential conformance validation against the shared v0.8 engine fixtures.
- TypeScript SDK documentation and v0.9 release notes.

### Changed
- Current toolkit/profile/template metadata advances to v0.9.0.
- CI now builds and validates both reference implementations while preserving Python-backed operational monitoring.


## v0.8.0 — 2026-08-16

### Added
- Language-neutral RAHP engine contract covering the source → observation → trigger → assessment → finding → disposition → baseline lifecycle.
- Normalized `rahp-result` schema and implementation-neutral engine conformance fixtures.
- Reference engine-contract CLI and CI validator.
- Evidence-retention policy with `ephemeral`, `referenced`, `durable` and `exemplar` classes.
- Deployment-profile retention settings and ignored `.rahp/` working review area.

### Changed
- New review scaffolds default to `.rahp/reviews/` rather than automatically becoming committed examples.
- Curated examples now require explicit promotion from a working review.
- Clarify that Python is a reference adapter; schemas, method data, lifecycle invariants and conformance fixtures define the portable engine boundary.
- Review retention now preserves compact assurance/disposition state in Git while keeping logs, target clones, intermediate renders and large/sensitive evidence outside normal repository history.
- Revalidate all 20 committed pressure-test exemplars, 5 security-hardening reviews and 4 combined syntheses against `rahp-engine-contract-v1`, preserving original target pins and review dates while recording prior RAHP versions.
- Complete an active-documentation audit so review output locations, portability guidance, templates, Pages coverage and retention semantics consistently describe v0.8 behavior.

## v0.7.1 — 2026-08-16

### Added
- Stable assessment keys for repository-change and selected-issue observations.
- Durable DTG assessment records for the Trust Tasks and Verifiable Trust Infrastructure change windows.
- DTG assessment-queue state linking generated GitHub issues to durable review records and reviewed revisions.
- Queue-behaviour tests covering stable keys, legacy marker migration, repository correlation and trigger idempotence.

### Changed
- Rework assessment issue publication from title-based event deduplication to work-item coalescing.
- Related selected-issue events now carry a repository assessment correlation key so situational triggers can enrich an existing open repository assessment.
- Repository monitors now emit stable assessment identity independently of the current SHA or issue title.
- Advance the DTG Trust Tasks reviewed baseline through `8eb7509ffabf6cc095eec20cb7d8d0120ff59ef3`; retain `1c20e3157597952d174fa2e884609f5b938923be` as the reviewed Verifiable Trust Infrastructure baseline.
- Re-baseline selected Trust Tasks issue-watch state through the observations used for this release, including the still-open task-control/corrigibility discussion.

### Dispositioned
- RAHP toolkit issues #1, #3 and #4 through consolidated assessment `DTG-AR-2026-001`.
- RAHP toolkit issue #2 through assessment `DTG-AR-2026-002`.

## v0.7.0 — 2026-08-14

- Deepen CAWG/C2PA coverage with scenario, composition, experimental-branch, security and combined review evidence.
- Add deployment-neutral issue-aware situational monitoring: CAWG/C2PA and DTG maintain separate curated issue registries and state.
- Add CAWG mandate-readiness rendering.
- Fix Pages base-URL and structured-data coverage validation, including canonical mandate-readiness projection and assessment-pack links.

## v0.6.0 — 2026-08-14

### Added
- First substantial external RAHP deployment under `profiles/cawg/` and `instances/cawg/`, covering CAWG/C2PA specification work without inheriting DTG portfolio governance.
- Eight completed CAWG/C2PA RAHP pressure tests spanning identity, metadata, training/mining, consent, endorsement, organizational identity, UX, and C2PA substrate boundaries.
- Portable branch-aware `tools/instance_monitor.py` for static-profile change tracking and materiality detection.
- Hardened DTG and portable instance monitors so empty/uninitialised repositories do not terminate scheduled assurance monitoring; genuine API failures remain visible.
- Deduplicated GitHub assessment issue publication and unified `instance-watch.yml` scheduled/manual workflow for DTG and CAWG/C2PA deployments.
- CAWG/C2PA instance documentation and v0.6.0 release notes.

### Changed
- Project identity and Pages/JSON-LD references now use the neutral `sankarshanmukhopadhyay/rahp-toolkit` repository.
- Completed an active-documentation identity audit: navigation, adoption, contribution guidance, repository diagrams, AI-assisted guidance and pressure-test instructions now distinguish the portable toolkit from deployment-owned state.
- DTG is retained as an origin/exemplar deployment rather than encoded in the toolkit name or treated as the default adoption boundary.
- External deployment proof is now field evidence rather than an unchecked v0.5 roadmap objective.
- Pressure-test validation resolves instance-local risk catalogues such as CAWG `CRK-*` alongside the bundled DTG catalogue.
- Validation workflows now use Node 24-based `actions/checkout@v6` and `actions/setup-python@v6`; active documentation identity is checked in CI by `tools/validate_project_identity.py`.

### Removed
- Obsolete root-level release checklist and duplicate root release-note files; `docs/releases/` is the canonical release-note location.

## v0.5.0 — 2026-08-13

### Added
- Configuration-driven `tools/rahp.py` entry point for validating profiles, listing targets, preparing repositories, and scaffolding configured reviews.
- Portable `rahp-config` JSON Schema under `method/schema/`.
- DTG exemplar profile plus non-DTG minimal, multi-repository, security-only, and CI portability profiles.
- Generic configured-review GitHub Actions workflow.
- DTG instance portfolio discovery from `dtg-portfolio-monitor`, including relevant forks discovered by GitHub parent relationship.
- Scheduled/manual DTG material-change detection and detailed `assessment-required` issue queue.
- Durable DTG instance perimeter/state/review structure under `instances/dtg/`, kept separate from the portable toolkit.
- Configuration/adoption and v0.5 portability documentation.

### Changed
- Redefined portability around a YAML deployment profile rather than copying/replacing DTG instance data.
- Reframed DTG corpora, Portfolio Monitor metadata, Task Force actions and governance records as deployment-specific exemplar assets rather than core requirements.
- Made real external WG adoption a field-evidence objective rather than a blocker to the software portability claim.

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


## Development history — scenario-driven RAHP and JTD documentation (incorporated through v0.8.0)

### Portable persona layer

- Add reusable `P1`–`P6` personas for principals/rights-bearing parties, producers, relying parties, intermediaries, delegated service/agent operators, and registry/discovery/trust-service operators.
- Apply portable personas at finding level across the C2PA/CAWG and A2A worked pressure tests, while retaining machine-agent personas where behaviour is independently relevant.
- Extend persona namespace validation/import handling and document when portable roles versus DTG-specific personas should be used.
- Deepen `P1`–`P6` to parity with the established corpus through institutional context, meaningful lifecycle stages, explicit power/decision and harms/externality fields, concrete pressure-test situations, broader inclusion/exclusion analysis, and evidence grounding.
- Add `method/persona-quality.yaml` and `tools/validate_persona_quality.py` so portable-role richness is machine-verifiable in validation and Pages CI rather than relying on editorial convention.

### Agent-protocol assurance example

- Add a worked RAHP pressure test of **Agent2Agent (A2A) Protocol v1.0.0**, pinned to upstream commit `1eb4aa03b07589d3a00ce7deab0dde679120ed30`.
- Add reusable agentic risks `RK-AI05`–`RK-AI09`, controls `CT-67`–`CT-73`, guardrails `GR-22`–`GR-25`, assurance tests `AT-22`–`AT-25`, and metrics `M-38`–`M-40`.
- Add method documentation for discovery metadata vs authority, multi-agent delegation continuity, asynchronous callback trust, secondary-credential non-transitivity, and cross-agent action provenance.

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


## Development history — review orchestration and repository architecture (incorporated before v0.8.0)

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

## v0.3 development history

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
  resolvable IRI under `https://sankarshanmukhopadhyay.github.io/rahp-toolkit/id/`.
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
