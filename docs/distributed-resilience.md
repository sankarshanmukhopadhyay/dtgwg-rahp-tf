---
layout: default
title: "Distributed resilience and amplification"
nav_order: 8
has_toc: true
parent: Run assessments
---
# Distributed Resilience and Amplification Risk Model (DRARM)

DRARM is RAHP's portable catalogue for failure modes where a distributed system amplifies load, retries, concurrency, queue pressure, duplicate effects, dependency failures or recovery work. It is deliberately independent of DTG, OpenVTC, CAWG/C2PA or any one protocol stack.

The core catalogue lives at [`method/resilience/catalogue.yaml`](../method/resilience/catalogue.yaml). Static evidence signals live separately in [`method/resilience/detectors.yaml`](../method/resilience/detectors.yaml). This separation is intentional: the risk model is normative method data; detectors are replaceable evidence adapters.

## What DRARM can assess

DRARM profiles classify a target as an `implementation`, `specification`, `architecture`, `deployment`, `composed-system` or `mixed` target. The same catalogue can therefore be applied to source code, protocol text, repository bundles, architecture documents and cross-component systems without importing ecosystem-specific semantics into the model.

The baseline catalogue covers retry storms, reconnect herds, startup stampedes, retry multiplication, unbounded queues, destructive overflow, fan-out amplification, poison-message redelivery, head-of-line blocking, timeout amplification, cascading and partial dependency failures, cache stampedes, duplicate effects after lost acknowledgement, backpressure collapse, restart loops, malformed-input work amplification, recursive resolution, feedback loops, broadcast amplification, scheduler synchronization, recovery replay surge, lease-renewal herds, circuit-breaker recovery herds, observability amplification, metric cardinality explosion, unbounded task creation, unbounded pagination, Retry-After non-compliance and noisy-neighbour amplification.

## Execution boundary

DRARM follows RAHP's existing lifecycle:

```text
source → observation → trigger → assessment → finding → disposition → baseline
```

A detector match is an **observation**, not automatically a finding. The reference adapter distinguishes:

- `finding`: a high-confidence hazardous construct was directly observed, such as an unbounded asynchronous channel;
- `review-required`: a resilience-sensitive construct was observed but the necessary control or assurance evidence needs confirmation;
- no emitted item: no selected detector produced a material signal. This does not prove absence of the risk.

This avoids converting missing keywords into false architectural claims.

## Run against a local repository or extracted bundle

```bash
python3 tools/rahp.py resilience \
  --path ../target-repository \
  --repository owner/repository \
  --revision <tag-or-commit>
```

Or call the adapter directly:

```bash
python3 tools/resilience_assess.py \
  --target ../target-repository \
  --profile profiles/resilience/default.yaml \
  --repository owner/repository \
  --revision <tag-or-commit>
```

The default outputs are:

```text
build/resilience/result.json
build/resilience/report.md
build/resilience/issue-events.json
```

The result validates against [`method/schema/resilience-result.schema.json`](../method/schema/resilience-result.schema.json).

## One-click GitHub Action

Run **Run distributed resilience assessment** from Actions. Supply either:

1. `target_repository` plus `target_ref` for a GitHub repository, release tag or commit; or
2. `source_url` for a single rendered/raw specification document.

Choose the target type and profile. The workflow validates DRARM, resolves the exact target revision, runs the assessment, uploads the complete evidence bundle and, when the profile publication threshold is met, creates or coalesces a durable RAHP issue.

The RAHP issue includes for every emitted item:

- risk ID, severity and confidence;
- observed source locations;
- required controls;
- assurance evidence that should exist;
- the correct upstream control plane;
- the configured upstream repository;
- a suggested upstream issue title; and
- a ready-to-file upstream issue body.

DRARM does **not** directly file upstream by default. The default `recommend-only` policy preserves the governance boundary between automated assessment and exercising issue-filing authority in another project.

## Profiles, not forks

A profile maps target context without changing the generic model. The default profile is [`profiles/resilience/default.yaml`](../profiles/resilience/default.yaml). The OpenVTC Cypress example is [`examples/resilience/openvtc-cypress/profile.yaml`](../examples/resilience/openvtc-cypress/profile.yaml).

```yaml
version: 1
profile:
  id: my-system
  title: My system resilience profile
target:
  type: mixed
  include: ['**/*']
  exclude: ['vendor/**', 'build/**']
thresholds:
  publish: findings-and-review-gaps
upstream:
  repository: my-org/my-system
  filing_policy: recommend-only
```

Profile validation is governed by [`method/schema/resilience-profile.schema.json`](../method/schema/resilience-profile.schema.json).

## Publication thresholds

`thresholds.publish` controls which assessment states may create a durable RAHP issue:

| Value | Durable issue trigger |
|---|---|
| `high-confidence` | High-confidence `finding` only |
| `all-findings` | Any `finding` |
| `findings-and-review-gaps` | Findings and review-required evidence gaps |

A profile may use the third mode for an assurance review or a tagged-release examination where unresolved evidence gaps are themselves meaningful work items. Generic automated monitoring should normally prefer `high-confidence` to avoid issue noise.

## Assurance levels

DRARM uses five cumulative assurance levels:

| Level | Evidence expectation |
|---|---|
| `DR-A1` | Behaviour/control is documented. |
| `DR-A2` | Control is evidenced in normative text or implementation. |
| `DR-A3` | Automated conformance test exists. |
| `DR-A4` | Behaviour is measured under induced failure/load. |
| `DR-A5` | Fleet-scale/adversarial behaviour is demonstrated within declared bounds. |

A design statement alone should therefore not be treated as equivalent to load-tested resilience.

## Evidence discipline

Each catalogue risk declares `evidence_required`. Examples include retry policy, fleet recovery tests, queue-capacity tests, lost-ack tests, poison-message tests and resource measurements. A complete disposition should attach or reference those artifacts rather than close a finding only because implementation text appears plausible.

For failures that span layers, the preferred evidence is a **failure-domain ownership map** showing which layer may retry, acknowledge, deduplicate, shed load, quarantine work and enter terminal failure for each failure class.

## Upstream filing governance

The upstream payload is a recommendation artifact. Before filing it upstream, the assessor should verify:

1. the source location and revision are still current;
2. the detector has not misclassified the construct;
3. an equivalent control is not implemented elsewhere;
4. the proposed control plane belongs to that upstream project;
5. the issue does not disclose sensitive deployment or security information; and
6. the upstream project has not already recorded the same problem.

This makes automated issue preparation machine-repeatable without confusing RAHP's assessment authority with an upstream maintainer's disposition authority.

## OpenVTC Cypress as a reference target

The OpenVTC profile is intentionally only a mapping layer. DRARM remains usable if that profile is deleted. To assess Cypress from the GitHub Action, use:

```text
target_repository: OpenVTC/openvtc
target_ref: Cypress
target_type: mixed
profile_path: examples/resilience/openvtc-cypress/profile.yaml
upstream_repository: OpenVTC/openvtc  # recommendation metadata only; never an automated issue destination
```

This produces a revision-pinned RAHP assessment and upstream-ready recommendations without making OpenVTC concepts part of the portable catalogue.

## Extending DRARM

Add a risk only when it describes a reusable amplification/failure pattern rather than an ecosystem-specific defect. Every risk must declare a trigger, failure mechanism, controls, assurance evidence, upstream control plane, retest condition and at least one detector/evidence adapter. Ecosystem-specific terminology belongs in profiles, corpora or worked assessments.


### Issue-publication boundary

DRARM may identify an upstream repository that owns a remediation, but that field is recommendation metadata only. All automated DRARM/RAHP issue creation is confined to `sankarshanmukhopadhyay/rahp-toolkit`. A RAHP issue may contain an upstream-ready title, body, evidence, and retest checklist; creating an issue in the assessed repository requires an explicit human action outside RAHP automation.
