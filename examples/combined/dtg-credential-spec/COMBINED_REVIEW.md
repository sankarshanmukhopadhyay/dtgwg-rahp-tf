# DTG Core Credential Specification combined RAHP + security review

> Generated from the linked RAHP pressure-test and security-hardening YAML records. This report is a cross-lens synthesis, not a third independent test.

## Review metadata

| Field | Value |
|---|---|
| Combined review | `COMB-CR-001` |
| Status | complete |
| Reviewed on | 2026-08-12 |
| Target | `trustoverip/dtgwg-cred-spec` |
| Version | Working Draft 01 |
| Commit | `d19f7c9cac364fab8e50cf434513ef53fef80e37` |
| RAHP review | `SR-001` — 8 finding(s) |
| Security review | `SEC-CR-001` — 13 finding(s) |
| RAHP version | `v0.8.0` |
| Engine contract | `rahp-engine-contract-v1` |
| Engine/method revalidated on | 2026-08-16 |

## How to read the combined view

The RAHP lens asks what harms, governance failures, assurance gaps, and affected-party consequences remain. The security lens asks how an adversary or compromised component can violate a security property. The synthesis below uses shared canonical RAHP context as a heuristic, weighted toward shared risks and guardrails. It shows only the strongest connections and does not imply that paired findings are identical.

## Strongest cross-lens connections

| RAHP finding | Security finding | Shared RAHP context |
|---|---|---|
| `F-001` — The reverse VMC required for a complete membership edge is not constructible from the normative schema | `SEC-CR-001` — VMC bidirectionality is structurally inconsistent with the current schema | `CT-18`, `CT-19`, `RK-SC02` |
| `F-001` — The reverse VMC required for a complete membership edge is not constructible from the normative schema | `SEC-CR-004` — VRC completeness and relationship semantics can be over-claimed from one direction | `CT-18`, `CT-19`, `RK-SC02` |
| `F-002` — VMC membership of an agent can be misread as agent authority, capability or operator accountability | `SEC-CR-002` — Agent membership can be over-read as delegation or authority | `AT-12`, `AT-13`, `CT-30`, `CT-31`, `CT-32`, `GR-12`, `GR-13`, `RK-AI01`, `RK-AI02` |
| `F-002` — VMC membership of an agent can be misread as agent authority, capability or operator accountability | `SEC-CR-003` — Credential status and revocation behavior are not deterministic enough for high-impact verification | `CT-56`, `RK-G05` |
| `F-003` — Credential status and lifecycle semantics are too weak for consistent revocation and stale-authority handling | `SEC-CR-003` — Credential status and revocation behavior are not deterministic enough for high-impact verification | `AT-08`, `AT-09`, `CT-23`, `CT-24`, `CT-25`, `CT-26`, `GR-08`, `GR-09`, `RK-CR02`, `RK-CR03` |
| `F-003` — Credential status and lifecycle semantics are too weak for consistent revocation and stale-authority handling | `SEC-CR-002` — Agent membership can be over-read as delegation or authority | `AT-12`, `CT-32`, `GR-12`, `RK-AI02` |
| `F-004` — The M-DID bootstrapping exception has no bounded migration or retirement semantics | `SEC-CR-005` — M-DID bootstrapping creates an open-ended correlation window | `AT-18`, `CT-15`, `CT-50`, `GR-18`, `RK-ID05`, `RK-SC04` |
| `F-005` — ZKP-by-default guidance is not interoperable or conformance-testable without a proof profile | `SEC-CR-006` — ZKP presentation is encouraged without an interoperable security profile | `AT-06`, `CT-27`, `CT-28`, `GR-06`, `RK-CY01` |
| `F-005` — ZKP-by-default guidance is not interoperable or conformance-testable without a proof profile | `SEC-CR-007` — Presentation replay protection is outside the credential specification | `CT-27`, `CT-28`, `RK-CY01` |
| `F-006` — Conformance needs a sharper boundary between schema validity and governance-qualified DTG meaning | `SEC-CR-001` — VMC bidirectionality is structurally inconsistent with the current schema | `CT-18`, `CT-19`, `RK-SC02` |
| `F-006` — Conformance needs a sharper boundary between schema validity and governance-qualified DTG meaning | `SEC-CR-004` — VRC completeness and relationship semantics can be over-claimed from one direction | `CT-18`, `CT-19`, `RK-SC02` |

## RAHP-only findings

- `F-007` — Supported decision-making, guardianship and power-of-attorney relationships are not representable
- `F-008` — Organisational membership and relationship semantics are not explicit in the identifier model

## Security-only findings

- `SEC-CR-008` — Invitation single-use behavior is recommended but not interoperably enforceable
- `SEC-CR-009` — Optional VWC digest permits witness assertions that are not bound to an exact VRC
- `SEC-CR-010` — Witness method strings can be mistaken for verified liveness or proximity assurance
- `SEC-CR-011` — VEC endorsements can become stale or reputation-laundered across governance contexts
- `SEC-CR-012` — Personhood hint can be over-read as authoritative PHC status
- `SEC-CR-013` — Dual VC version support expands downgrade and proof-suite compatibility surface
