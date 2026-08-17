# C2PA + CAWG portfolio combined review

> Generated from the linked RAHP pressure-test and security-hardening YAML records. This report is a cross-lens synthesis, not a third independent test.

## Review metadata

| Field | Value |
|---|---|
| Combined review | `COMB-CW-002` |
| Status | complete |
| Reviewed on | 2026-08-14 |
| Target | `c2pa-org/specifications` |
| Version | 2.4 / tracked main |
| Commit | `b1703dc0a0420088d3f8b0e5fb11866d0fe931cb` |
| RAHP review | `CAWG-COMP-005` — 2 finding(s) |
| Security review | `SEC-CW-002` — 3 finding(s) |
| RAHP version | `v1.1.0` |
| Engine contract | `rahp-engine-contract-v1` |
| Engine/method revalidated on | 2026-08-17 |

## How to read the combined view

The RAHP lens asks what harms, governance failures, assurance gaps, and affected-party consequences remain. The security lens asks how an adversary or compromised component can violate a security property. The synthesis below uses shared canonical RAHP context as a heuristic, weighted toward shared risks and guardrails. It shows only the strongest connections and does not imply that paired findings are identical.

## Strongest cross-lens connections

| RAHP finding | Security finding | Shared RAHP context |
|---|---|---|
| `F-001` — All cryptographic layers can validate while the trust decision is still unjustified | `SEC-CW-005` — Single success UX can mask unperformed authority or consent checks | `CRK-28` |
| `F-002` — Optional higher-layer assertion stripping is not distinguishable from legitimate absence | `SEC-CW-004` — Optional assertion stripping can downgrade a relying-party decision | `CRK-23` |

## RAHP-only findings

None.

## Security-only findings

- `SEC-CW-006` — Conflicting valid assertions can be exploited as policy confusion

## Reviewer synthesis notes

- The principal portfolio risk is semantic downgrade: lower-layer cryptographic validity can survive removal, conflict or non-evaluation of higher-layer evidence.
