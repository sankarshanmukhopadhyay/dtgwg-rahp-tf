---
layout: default
title: "Scenario corpora"
nav_order: 5
has_toc: true
---
# Scenario corpora

Scenario corpora connect domain-specific use cases to portable RAHP pressure-test patterns.

## DTG ZKP reference corpus

[`corpora/dtg-zkp.yaml`](../corpora/dtg-zkp.yaml) is the first reference adapter. It maps 30 DTG ZKP implementation-guide use cases to portable RAHP scenario patterns without taking ownership of the `UC-*` identifiers.

| Coverage area | Representative source scenarios | Portable RAHP patterns |
|---|---|---|
| Privacy and correlation | UC-002, UC-023, UC-024 | `SP-PRIV-01`, `SP-PRIV-02` |
| Recovery and controller compromise | UC-005, UC-021 | `SP-RECOV-01`, `SP-AUTH-01` |
| Agent delegation | UC-009, UC-010, UC-011 | `SP-AGENT-01`, `SP-AGENT-02` |
| Governance and lifecycle | UC-012, UC-013, UC-027 | `SP-GOV-01`…`03` |
| Offline and resilience | UC-014, UC-018, UC-028 | `SP-OPS-01`…`03` |
| Inclusion | UC-017, UC-020 | `SP-INCL-01`, `SP-INCL-02` |
| Cryptographic migration | UC-026 | `SP-CRYPTO-01` |
| Interoperability | UC-030 | `SP-INTEROP-01` |

## Adding another corpus

1. Keep scenario identifiers and normative meaning owned by the source project.
2. Create an adapter under `corpora/`.
3. Record source repository and path.
4. Map every imported scenario to at least one portable pattern.
5. Run `python3 tools/validate_scenario_corpora.py`.
6. Use scenario IDs and pattern IDs in pressure-test findings where they materially contributed to the finding.

{: .warning }
An adapter is a review aid, not a normative fork. If the source scenario meaning changes, update the adapter and re-run affected reviews.
