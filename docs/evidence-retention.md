---
layout: default
title: "Review evidence and retention"
nav_order: 10
has_toc: true
---
# Review evidence and retention

A RAHP repository should not become an ever-growing archive of generated reviews,
cloned targets and run logs. v0.8 therefore adopts the rule:

> **Git preserves assurance state, not execution exhaust.**

## Four retention classes

| Class | Typical material | Stored in Git? | Default |
|---|---|---|---|
| `ephemeral` | logs, target clones, intermediate renders, draft scaffolds | **No** | 14 days |
| `referenced` | large evidence bundles, traces, screenshots, scan reports | manifest only | 365 days |
| `durable` | assessment identity, revision, findings, disposition, evidence references | **Yes** | indefinite / governance-defined |
| `exemplar` | deliberately curated worked examples and conformance fixtures | **Yes** | explicit promotion |

The portable defaults are defined in `method/evidence-retention.yaml`. Deployment
profiles may impose stricter retention where law, contract or governance requires it.

## Working reviews

New review scaffolds are written to `.rahp/reviews/` by default:

```bash
python3 tools/review.py init \
  --mode combined \
  --slug example-spec \
  --title "Example Specification" \
  --repository example/spec \
  --version main \
  --commit 0123456789012345678901234567890123456789
```

`.rahp/` is ignored by Git. This is where run-local logs, target material and draft
review artefacts belong.

A worked review should enter `examples/` only by deliberate promotion:

```bash
python3 tools/review.py promote --mode combined --slug example-spec
```

Promotion means "this is a maintained teaching/conformance example", not simply "this
run completed".

## Durable deployment records

A completed deployment assessment normally leaves only a compact record under
`instances/<deployment>/reviews/`, containing enough information to answer:

1. what was reviewed;
2. which immutable revision was reviewed;
3. why the assessment was triggered;
4. what findings were made;
5. how they were dispositioned;
6. what evidence supports that decision; and
7. what should cause a retest.

Large supporting evidence should normally live in deployment-controlled artifact
storage. Its manifest entry records a versioned/immutable URI, SHA-256, collection
time and sensitivity classification. That makes evidence independently verifiable
without committing the evidence payload itself.

## CI artifacts

CI systems may retain raw logs and review bundles for their own configured retention
window. Those artefacts are operational convenience, not the durable assurance
record. Their expiry must not erase the reviewed revision, findings or disposition.

## Why this model

Keeping every generated review in Git has three undesirable effects: repository size
grows monotonically, generated material obscures human governance decisions, and
sensitive or high-volume evidence is encouraged into a public source-control system.
The v0.8 model separates reproducible execution from governance-significant state.
