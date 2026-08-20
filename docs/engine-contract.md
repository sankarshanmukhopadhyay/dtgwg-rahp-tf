---
layout: default
title: "Engine contract"
nav_order: 1
has_toc: true
parent: Implement RAHP
---
# RAHP engine contract

The stable v1 engine boundary is language-neutral. The candidate v1.2 capability extends it additively so a conforming implementation can represent evidence classification, residual assurance evaluation, governed remediation, and evidence-based retesting without making Python or TypeScript behaviour normative.

The v1.2 lifecycle is:

```text
source → observation → trigger → assessment → evidence → evaluation
       → finding → disposition → remediation → retest → baseline
```

A detector signal is not automatically a finding. Evidence must be classified, relevant controls and assurance tests credited, and the residual state recorded. A result with zero findings is not equivalent to assured when unresolved assurance gaps, review-required propositions, or unassessed propositions remain.

The normalized result remains schema version `1`. The extension adds optional `assurance_summary`, `evaluations`, `remediations`, and `retests` fields, preserving existing v1.1 result compatibility.

Normative portable surfaces are `method/engine-contract.yaml`, the schemas under `method/schema/`, retention policy, mappings, and shared conformance fixtures. Reference implementations may use richer internal logic but must preserve normalized proposition, evidence, reasoning, and lifecycle semantics.
