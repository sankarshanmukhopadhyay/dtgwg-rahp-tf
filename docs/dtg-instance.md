---
title: DTG RAHP instance
nav_order: 69
---

# DTG RAHP instance

The repository serves two purposes without coupling them:

1. **Portable toolkit:** `method/`, `tools/rahp.py`, schemas, validators and generic configuration examples can be used by any adopter.
2. **DTG deployment:** `instances/dtg/` applies that toolkit operationally to the DTG ecosystem.

## Portfolio scope

The DTG deployment reads `config/repositories.yaml` from `sankarshanmukhopadhyay/dtg-portfolio-monitor`.
It then discovers repositories owned by the configured fork owner and includes a fork only when
GitHub reports that its parent is one of those portfolio repositories. This avoids maintaining a
second hand-written list and allows new monitored repositories and new relevant forks to enter the
DTG assessment perimeter automatically.

`instances/dtg/generated/repositories.yaml` is a generated, auditable snapshot of that resolved perimeter.

## Change-to-review flow

```mermaid
flowchart LR
  PM[DTG Portfolio Monitor registry] --> D[Discover targets]
  F[Relevant forks] --> D
  D --> H[Resolve current heads]
  H --> C{Changed since last observation?}
  C -- no --> S[Retain state]
  C -- yes --> M{Material paths changed?}
  M -- no --> S
  M -- yes --> I[File assessment-required issue]
  I --> R[RAHP / security / combined review]
  R --> A[Store durable artefacts under instances/dtg/reviews]
  A --> X[Close queue issue with reviewed SHA]
```

The automation does not claim that a changed repository contains a defect. It creates an
**assessment queue record** when changed files intersect the portfolio's material paths.

## Workflows

- `dtg-portfolio-review.yml`: scheduled and manual DTG discovery/change review queue.
- `configured-review.yml`: generic on-demand RAHP runner for any YAML profile.
- Existing validation, corpus and Pages workflows remain independent.

For the first deployment run, use `initialize=true`. This records current heads without opening
issues for the entire existing portfolio. Subsequent runs compare from that baseline.
