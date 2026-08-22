---
layout: default
title: "Remediation and retesting"
nav_order: 8
has_toc: true
parent: Operate assurance
---
# Governed remediation and evidence-based retesting

RAHP treats remediation as an assurance object rather than an unstructured recommendation. The portable `method/schema/remediation-manifest.schema.json` contract can identify a durable remediation, bind it to an assessment run and finding lineage, state requested outcomes and acceptance criteria, identify evidence required for closure, define retest triggers, and record the authority permitted to propose, approve, implement, accept risk or close the remediation.

The contract remains deployment-neutral. A remediation owner may be a specification repository, implementation project, governance process, runtime control plane, operational policy or another governed surface. DTG, OpenVTC, ARPA, CAWG/C2PA and other deployments can demonstrate the model without defining it.

Publication remains governed. A generated remediation may declare that an external work item is eligible, but this does not authorize RAHP automation to file or change an upstream repository. Observation, assessment, remediation ownership, publication, risk acceptance and closure authority remain distinct.

## Portable lifecycle

```text
assessment run
  → finding lineage
  → governed disposition
  → remediation obligation
  → acceptance criteria
  → target/control/evidence change
  → retest
  → closure evidence
  → resolved | residual | regression | inconclusive | indeterminate
  → authority-valid disposition
```

A work-item tracker is an operational view of this lifecycle, not its canonical identity.

## Acceptance criteria and closure evidence

A remediation can define explicit acceptance criteria. Retest evidence may bind to those criteria using `criterion_id`. The v1.5 development validator enforces a conservative closure rule: a `resolved` outcome requires passing evidence for every referenced acceptance criterion and cannot contain non-passing closure evidence.

`resolved` does not itself close the governance obligation. A retest may become `eligible-for-closure`; actual closure remains an authority-bearing disposition. `inconclusive` and `indeterminate` outcomes cannot be closed as successful remediation.

## Retest lineage

`method/schema/retest.schema.json` can record:

- a stable `retest_id`;
- the associated `remediation_id`;
- the assessment identity and previous/current run identities;
- previous and retested target revisions;
- acceptance criteria evaluated;
- attributable closure evidence;
- the retest outcome; and
- the disposition actor and authority basis.

This makes remediation history reconstructable even when repository issues, tickets or other coordination surfaces are later closed, moved or deleted.

## Executable retest

`tools/retest.py` evaluates an arbitrary YAML or JSON remediation/retest pair against both the portable schemas and the governed closure invariants. It can emit a machine-readable judgment suitable for CI or another assurance control plane.

```bash
python3 tools/retest.py \
  --remediation examples/assurance-lineage/generic-remediation.yaml \
  --retest examples/assurance-lineage/generic-retest.yaml \
  --json
```

The generic conformance fixtures use a fictional payments specification rather than a project-specific deployment. Repository CI additionally runs:

```bash
python3 tools/validate_remediation_retest_lineage.py
python3 -m unittest tests.test_remediation_retest_lineage
```

Project-specific deployments MAY add further acceptance rules or evidence obligations, but MUST NOT weaken the portable invariants when claiming portable RAHP conformance.
