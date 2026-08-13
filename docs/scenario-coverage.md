---
layout: default
title: "Scenario coverage"
nav_order: 7
has_toc: true
---
# Scenario coverage

This view summarizes how the current domain corpora exercise RAHP's portable scenario-pattern catalogue. Counts are **scenario-to-pattern mappings**, not safety scores.

## Corpus inventory

| Corpus | Adapter | Scenarios |
|---|---|---:|
| DTG Credential Specification scenario corpus | [`credential-spec.yaml`](../corpora/credential-spec.yaml) | 16 |
| DTG ZKP pressure-test use-case corpus | [`dtg-zkp.yaml`](../corpora/dtg-zkp.yaml) | 30 |
| Trust Tasks × Credential Spec composed scenario corpus | [`trust-tasks-credspec-composed.yaml`](../corpora/trust-tasks-credspec-composed.yaml) | 12 |
| Trust Tasks scenario corpus | [`trust-tasks.yaml`](../corpora/trust-tasks.yaml) | 16 |

## Portable-pattern coverage

| Pattern | Meaning | ZKP | Trust Tasks | CredSpec | Composed | Total |
|---|---|---:|---:|---:|---:|---:|
| `SP-AUTH-01` | Compromised controller | 3 | 3 | 2 | 2 | 10 |
| `SP-PRIV-01` | Malicious verifier | 5 | 4 | 3 | 2 | 14 |
| `SP-PRIV-02` | Cross-party collusion | 1 | 0 | 2 | 1 | 4 |
| `SP-INCL-01` | Accessibility constraint | 1 | 0 | 1 | 0 | 2 |
| `SP-INCL-02` | Resource-constrained participant | 1 | 1 | 1 | 0 | 3 |
| `SP-GOV-01` | Authority status changes | 2 | 0 | 3 | 1 | 6 |
| `SP-GOV-02` | Policy changes over time | 1 | 2 | 2 | 1 | 6 |
| `SP-GOV-03` | Appeal and redress | 1 | 0 | 0 | 1 | 2 |
| `SP-OPS-01` | Dependency unavailable | 1 | 1 | 3 | 2 | 7 |
| `SP-OPS-02` | Offline operation | 1 | 0 | 0 | 1 | 2 |
| `SP-OPS-03` | Emergency or degraded mode | 1 | 0 | 0 | 0 | 1 |
| `SP-AGENT-01` | Delegated agent exceeds mandate | 2 | 3 | 0 | 1 | 6 |
| `SP-AGENT-02` | Human intent changes after delegation | 1 | 1 | 0 | 2 | 4 |
| `SP-CRYPTO-01` | Algorithm or profile migration | 1 | 1 | 2 | 1 | 5 |
| `SP-INTEROP-01` | Cross-implementation ambiguity | 1 | 6 | 5 | 2 | 14 |
| `SP-REPLAY-01` | Replay or duplicate action | 5 | 4 | 1 | 2 | 12 |
| `SP-RECOV-01` | Recovery and continuity | 2 | 0 | 1 | 0 | 3 |
| `SP-FED-01` | Cross-domain recognition conflict | 2 | 1 | 1 | 1 | 5 |
| `SP-SCALE-01` | Scale changes observability | 1 | 2 | 0 | 0 | 3 |
| `SP-COMP-01` | Composite assurance interaction | 1 | 1 | 3 | 4 | 9 |

## Interpretation

A zero in a particular corpus does not automatically indicate a defect. It identifies a portable failure class that the corpus does not currently exercise. Reviewers should decide whether that absence is appropriate for the source specification or represents a scenario gap.

Cross-specification coverage is intentionally narrower and higher-severity: it concentrates on emergent behavior at the Trust Tasks / credential boundary rather than repeating every standalone scenario.
