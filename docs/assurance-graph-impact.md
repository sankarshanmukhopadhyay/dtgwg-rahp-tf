---
layout: default
title: "Assurance graph and impact analysis"
nav_order: 9
has_toc: true
parent: Operate assurance
---
# Assurance graph and impact analysis

RAHP v1.5 development introduces a portable assurance graph for connecting targets, requirements, evidence, risks, harms, controls, guardrails, tests, assessments, findings, remediations and authorities without coupling the method to any particular repository, standards community or deployment.

The graph is not a universal ontology and does not make an assurance conclusion by itself. It records enough machine-readable dependency structure to answer a narrower operational question:

> If this governed target or assurance object changes, which assurance records may need to be reconsidered?

## Portable graph contract

`method/schema/assurance-graph.schema.json` defines nodes and typed edges. Each edge carries an explicit `impact_propagation` value:

- `source-to-target`
- `target-to-source`
- `both`
- `none`

Impact direction is therefore evidence carried by the graph, not an assumption hard-coded into the engine. Two deployments may use the same relationship type with different propagation semantics when their governance or dependency structure genuinely differs.

This is important for portability: RAHP does not assume that a repository, specification, implementation, dataset or operational service has the dependency layout of DTG, OpenVTC, ARPA, CAWG/C2PA or any other maintained example.

## Impact analysis

`tools/impact.py` performs deterministic reachability from one or more changed node identifiers.

```bash
python3 tools/impact.py \
  --graph examples/assurance-lineage/generic-assurance-graph.yaml \
  --changed-node target:payments-api \
  --json
```

The result records:

- changed nodes;
- every affected node and its shortest graph distance;
- the edge path (`via`) that explains why it was selected;
- affected stable assessment identities;
- assessments selected as `retest_required`; and
- changed node identifiers that could not be resolved.

`method/schema/impact-analysis.schema.json` defines the portable result contract.

## Governance boundary

Impact is **selection evidence**, not a finding and not a closure decision.

```text
material change
  → graph impact selection
  → affected assessment candidates
  → evidence review / reassessment
  → governed residual conclusion
```

A selected assessment is a candidate for retest. RAHP must not infer from graph reachability alone that a target is unsafe, that a finding exists, that a remediation failed, or that an upstream issue must be opened.

Likewise, absence from an incomplete graph is not evidence of non-impact. Deployments are responsible for the scope and quality of their graph data and should preserve uncertainty when relevant dependencies are not represented.

## Deployment-neutral conformance fixture

The canonical fixture uses the fictional Example Payments API Specification. A change to the target propagates through an authorization requirement, implementation control, assurance test and evidence into the stable assessment identity. The graph also retains downstream finding and remediation dependencies.

This demonstrates the portable contract without making any real project vocabulary part of core conformance.

Project-specific graph profiles MAY then map DTG, OpenVTC, ARPA, CAWG/C2PA or other projects into these node and edge contracts as real-world demonstrations.

## Validation

```bash
python3 tools/validate_assurance_graph.py
python3 -m unittest tests.test_assurance_graph_impact
```

The validator checks graph schema conformance, node uniqueness, edge reference integrity, impact-result conformance, deterministic target-change propagation and explicit treatment of unresolved changed nodes.
