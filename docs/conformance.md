---
layout: default
title: "Implementation conformance"
parent: "Implement RAHP"
nav_order: 2
has_toc: true
---
# Implementation conformance

RAHP v1.0 separates **method authority** from implementation convenience. A conforming implementation follows the stable v1 contract and produces equivalent decisions for the shared fixtures; it does not become normative merely because it ships in this repository.

## Stable v1 boundary

The normative implementation boundary is:

- `method/engine-contract.yaml` (`rahp-engine-contract-v1`)
- `method/schema/rahp-result.schema.json` (result schema version `1`)
- `method/evidence-retention.yaml` (`rahp-evidence-retention-v1`)
- `method/versioning.yaml` (compatibility rules)
- `tests/conformance/` (shared behavioral fixtures)

Python and TypeScript are reference implementations. The CI differential gate requires them to agree on normalized-result validity, evidence-retention planning, configured target enumeration, and trigger correlation fixtures.

## What conformance does not mean

Conformance does not certify the quality of a substantive risk judgement, make an AI reviewer accountable for a decision, or confer governance authority. Those remain assessment and deployment responsibilities.

## Compatibility promise

RAHP v1 follows semantic versioning for the toolkit. Breaking method changes require a new major release. A breaking engine contract or normalized-result format requires a new contract/schema identifier rather than silently changing v1 behavior. Published catalogue identifiers are not reused after retirement.

See [Engine contract](engine-contract.md), [TypeScript Reference SDK](typescript-sdk.md), and [Review evidence and retention](evidence-retention.md).
