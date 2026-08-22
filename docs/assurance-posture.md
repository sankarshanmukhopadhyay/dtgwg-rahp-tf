---
layout: default
title: "Assurance posture"
nav_order: 12
has_toc: true
parent: Operate assurance
---
# Assurance posture

RAHP v1.5 adds a portable operational posture view that summarizes actionable assurance state without collapsing materially different evidence and governance conditions into a synthetic score.

The posture contract is deployment-neutral. It can summarize a specification, repository, implementation, service, deployment, composition or portfolio without inheriting DTG, OpenVTC, ARPA, CAWG/C2PA or other project-specific vocabulary.

## What the posture answers

A posture view answers operational questions such as:

- which assessments require action;
- which assessments are stale or require retest;
- where evidence gaps remain;
- which policy gates are blocking or indeterminate;
- where required authority is denied or indeterminate;
- which conclusions changed since a baseline; and
- which remediations remain open, in progress or waiting for retest.

It does **not** produce an assurance score or percentage. `controlled`, `assurance-gap`, `retest-required`, `FAIL`, `INDETERMINATE` and `denied` are not interchangeable states and must remain separately visible.

## Portable contract

`method/schema/assurance-posture.schema.json` defines the machine-readable posture. Each assessment record retains separate fields for:

```text
conclusion
freshness
remediation
gate
authority
changed_since_baseline
evidence_gaps
```

This separation preserves the governance model established by the earlier v1.5 tranches. For example, a policy gate may be `PASS` while publication authority is `denied`; the posture must show both facts rather than infer a publishable result.

## Generate a posture view

```bash
python3 tools/assurance_posture.py \
  --input examples/assurance-lineage/generic-posture-input.yaml \
  --generated-at 2026-08-22T00:00:00Z \
  --json
```

The deployment-neutral conformance result is pinned at `examples/assurance-lineage/generic-posture-result.json`.

## Operational semantics

`action_required` is an operational queue count. It includes adverse/uncertain conclusions and unresolved remediation work. It is not a claim that every counted item is equally severe.

`stale_or_retest` identifies assurance that should not be relied on as current without further evaluation. It does not establish that the target is unsafe or non-conformant.

`gate_blocked` and `authority_blocked` are deliberately separate. Policy evaluation does not create authority, and authority does not make a failed policy gate pass.

## Portfolio use

Portfolio dashboards SHOULD render the portable posture records and counts directly, with drill-down to the underlying assessment, evidence, remediation, gate and authority records. They SHOULD NOT invent an aggregate “assurance percentage” that obscures those states.

A portfolio is therefore a view over governed assurance evidence, not an alternative source of truth or authority.
