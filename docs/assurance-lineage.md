---
layout: default
title: "Assurance lineage"
parent: Run assessments
nav_order: 8
has_toc: true
---
# Assurance lineage

RAHP assurance lineage gives an assessment a durable identity across repeated runs, target revisions, evidence changes and work-item systems. It is a portable method contract: the model does not depend on GitHub, DTG, OpenVTC, ARPA, CAWG/C2PA, or any other deployment.

## Why lineage is needed

An assurance assessment is not the same thing as a single execution of that assessment, and neither is the same thing as an issue or ticket used to coordinate review.

```text
assessment identity
  ├─ assessment run A
  ├─ assessment run B
  └─ assessment run C

work item(s) ── track/review/remediate/retest ── assessment runs
```

This separation lets RAHP preserve assurance history when:

- a target changes and the assessment is rerun;
- findings are consolidated, split, reclassified, resolved or later regress;
- an issue tracker is changed or a work item is closed;
- multiple repositories or systems contribute evidence to one assurance conclusion;
- a deployment uses no issue tracker at all.

## Portable contracts

The initial v1.5 development contracts are:

- `method/schema/assessment-lineage.schema.json` — stable assessment identity, subject, run history, triggers, revisions and optional work-item references;
- `method/schema/finding-lineage.schema.json` — finding evolution across runs, including predecessor/successor relationships and evidence references.

Both are additive development contracts. They do not change `rahp-engine-contract-v1`, normalized result schema version `1`, or `rahp-evidence-retention-v1`.

## Assessment identity versus run identity

`assessment_id` identifies the assurance question or governed assessment surface. `run_id` identifies one execution or reassessment of it.

A run can record:

- its predecessor;
- why it was triggered;
- the target revision assessed;
- evidence grade;
- result location;
- whether it is complete, superseded or invalidated.

A deployment may use any identifier convention that satisfies the portable schema. Core RAHP does not prescribe a repository, organization or standards-community namespace.

## Work items are views, not authority

Issue trackers and review queues are useful operational surfaces, but they are not the canonical identity of an assessment or finding.

A work item therefore has an explicit relationship such as `tracks`, `reviews`, `remediates`, `retests` or `publishes`. Deleting or closing the work item must not erase assurance lineage.

Likewise, authority to create or close a local work item does not imply authority to accept risk, change an upstream specification or publish a finding externally.

## Finding transitions

The finding-lineage contract supports these transitions:

| Transition | Meaning |
|---|---|
| `introduced` | First durable appearance of the finding. |
| `unchanged` | Finding persists materially unchanged. |
| `reclassified` | Evidence changes severity, state or interpretation without changing identity. |
| `consolidated` | Multiple prior findings become one successor obligation. |
| `split` | One prior finding becomes multiple separately governed obligations. |
| `superseded` | Another finding or model replaces this record. |
| `resolved` | Required closure evidence supports resolution. |
| `regressed` | A previously resolved or controlled condition reappears. |

These transitions record evidence evolution; they do not by themselves grant risk-acceptance or publication authority.

## Generic conformance fixture

`examples/assurance-lineage/` intentionally uses a fictional payments specification and a generic tracker. This demonstrates that the portable lineage contract is usable without any RAHP-maintained deployment.

Portfolio examples may subsequently map real DTG, OpenVTC, ARPA or CAWG/C2PA assessments into the same contract. Those examples test adoption; they do not define the method.

## Validation

Run:

```bash
python3 tools/validate_assurance_lineage.py
```

The validator checks both JSON Schemas, the neutral fixtures and cross-fixture references such as `current_run_id`, predecessor runs and finding run references.

## v1.5 direction

Lineage is the foundation for later unreleased v1.5 capabilities:

```text
lineage
  → remediation correlation
  → retest transitions
  → assurance delta
  → evidence freshness
  → change-impact selection
  → authority-valid lifecycle decisions
```

These capabilities will accumulate on `main` before a v1.5.x release is cut.
