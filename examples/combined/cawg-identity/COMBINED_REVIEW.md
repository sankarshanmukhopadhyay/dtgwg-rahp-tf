# CAWG Identity Assertion combined RAHP + security review

> Generated from the linked RAHP pressure-test and security-hardening YAML records. This report is a cross-lens synthesis, not a third independent test.

## Review metadata

| Field | Value |
|---|---|
| Combined review | `COMB-CW-001` |
| Status | complete |
| Reviewed on | 2026-08-14 |
| Target | `decentralized-identity/cawg-identity-assertion` |
| Version | 1.3 WG-approved draft |
| Commit | `8a9c4925df7e8ccbcabce9d754fc27739e11dc12` |
| RAHP review | `CAWG-SR-001` — 2 finding(s) |
| Security review | `SEC-CW-001` — 3 finding(s) |
| RAHP version | `v1.1.0` |
| Engine contract | `rahp-engine-contract-v1` |
| Engine/method revalidated on | 2026-08-17 |

## How to read the combined view

The RAHP lens asks what harms, governance failures, assurance gaps, and affected-party consequences remain. The security lens asks how an adversary or compromised component can violate a security property. The synthesis below uses shared canonical RAHP context as a heuristic, weighted toward shared risks and guardrails. It shows only the strongest connections and does not imply that paired findings are identical.

## Strongest cross-lens connections

No cross-lens overlaps are recorded yet. This is normal for an in-progress scaffold or where the two lenses identify genuinely distinct concerns.

## RAHP-only findings

- `F-001` — Successful identity validation can be over-read as authority for the asserted role or claim
- `F-002` — Historical identity validity and status dependencies need a durable as-of verification contract

## Security-only findings

- `SEC-CW-001` — External identity and registry URI resolution can become a network attack surface
- `SEC-CW-002` — Trust-registry entity binding can be substituted across issuers
- `SEC-CW-003` — Status and archival dependency loss can force insecure fallback

## Reviewer synthesis notes

- Identity validity, authority and historical status are both harms/governance and adversarial trust-boundary concerns.
