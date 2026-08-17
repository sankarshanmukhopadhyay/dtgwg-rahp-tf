# Trust Tasks Framework combined RAHP + security review

> Generated from the linked RAHP pressure-test and security-hardening YAML records. This report is a cross-lens synthesis, not a third independent test.

## Review metadata

| Field | Value |
|---|---|
| Combined review | `COMB-TT-001` |
| Status | complete |
| Reviewed on | 2026-08-12 |
| Target | `trustoverip/dtgwg-trust-tasks-tf` |
| Version | Editor's Draft 0.3 (2026-08-07) |
| Commit | `fbe196a8a17ba3f99d0657a64be5ac58621023a1` |
| RAHP review | `SR-002` — 8 finding(s) |
| Security review | `SEC-TT-001` — 13 finding(s) |
| RAHP version | `v1.1.0` |
| Engine contract | `rahp-engine-contract-v1` |
| Engine/method revalidated on | 2026-08-17 |

## How to read the combined view

The RAHP lens asks what harms, governance failures, assurance gaps, and affected-party consequences remain. The security lens asks how an adversary or compromised component can violate a security property. The synthesis below uses shared canonical RAHP context as a heuristic, weighted toward shared risks and guardrails. It shows only the strongest connections and does not imply that paired findings are identical.

## Strongest cross-lens connections

| RAHP finding | Security finding | Shared RAHP context |
|---|---|---|
| `F-001` — Repeat execution of mutating or destructive tasks is not normatively prevented | `SEC-TT-001` — Duplicate execution remains possible for state-changing Trust Tasks | `AT-12`, `CT-19`, `CT-30`, `CT-48`, `GR-12`, `GR-16`, `RK-AI01`, `RK-SC02` |
| `F-001` — Repeat execution of mutating or destructive tasks is not normatively prevented | `SEC-TT-005` — Security-critical extension semantics can be ignored across ecosystem boundaries | `AT-12`, `CT-19`, `CT-30`, `GR-12`, `GR-16`, `RK-AI01`, `RK-SC02` |
| `F-002` — High-impact Trust Tasks can remain valid without a bounded freshness window | `SEC-TT-002` — High-impact requests can be authentic but stale | `AT-12`, `AT-17`, `CT-25`, `CT-31`, `CT-32`, `GR-12`, `GR-17`, `RK-AI02`, `RK-CR02` |
| `F-002` — High-impact Trust Tasks can remain valid without a bounded freshness window | `SEC-TT-010` — Revoked consent devices can remain effective for in-flight approvals | `AT-12`, `CT-31`, `CT-32`, `GR-12`, `RK-AI02`, `RK-CR02` |
| `F-003` — Producer identity is not portable evidence of authority, delegation or mandate | `SEC-TT-002` — High-impact requests can be authentic but stale | `AT-12`, `CT-31`, `CT-32`, `GR-12`, `RK-AI02` |
| `F-003` — Producer identity is not portable evidence of authority, delegation or mandate | `SEC-TT-009` — Delegated execution is fail-open unless deployments opt into policy enforcement | `AT-12`, `CT-30`, `CT-52`, `GR-12`, `RK-AI01` |
| `F-004` — Mutable draft specifications undermine reproducible validation of retained Trust Task evidence | `SEC-TT-006` — Mutable draft specifications weaken reproducible security validation | `AT-16`, `AT-17`, `CT-18`, `CT-47`, `CT-48`, `GR-16`, `GR-17`, `RK-SC02`, `RK-SY03` |
| `F-004` — Mutable draft specifications undermine reproducible validation of retained Trust Task evidence | `SEC-TT-013` — Parser and validation resource limits are advisory for network-facing consumers | `AT-16`, `AT-17`, `CT-19`, `CT-48`, `GR-16`, `GR-17`, `RK-SY03` |
| `F-005` — Runtime registry resolution can become an availability and semantic-integrity dependency | `SEC-TT-001` — Duplicate execution remains possible for state-changing Trust Tasks | `AT-16`, `CT-19`, `CT-48`, `GR-16`, `RK-SC02` |
| `F-005` — Runtime registry resolution can become an availability and semantic-integrity dependency | `SEC-TT-005` — Security-critical extension semantics can be ignored across ecosystem boundaries | `AT-16`, `CT-18`, `CT-19`, `GR-16`, `RK-SC02` |
| `F-006` — Capability discovery does not negotiate the security profile needed to execute a supported task | `SEC-TT-008` — Capability discovery does not fully negotiate a mutually secure execution profile | `AT-16`, `CT-19`, `CT-27`, `CT-29`, `GR-16`, `RK-CY01`, `RK-SC02` |
| `F-006` — Capability discovery does not negotiate the security profile needed to execute a supported task | `SEC-TT-003` — Transport-based proof omission can create security-profile downgrade ambiguity | `AT-16`, `CT-19`, `CT-29`, `GR-16`, `RK-CY01`, `RK-SC02` |
| `F-007` — Destructive and actsAsSubject classifications do not establish a minimum human-approval floor | `SEC-TT-009` — Delegated execution is fail-open unless deployments opt into policy enforcement | `AT-12`, `AT-19`, `CT-30`, `CT-52`, `CT-58`, `GR-12`, `GR-19`, `RK-AI01`, `RK-HX04` |
| `F-007` — Destructive and actsAsSubject classifications do not establish a minimum human-approval floor | `SEC-TT-001` — Duplicate execution remains possible for state-changing Trust Tasks | `AT-12`, `CT-30`, `GR-12`, `RK-AI01` |
| `F-008` — Supported decision-making and legal representation have no framework-level binding point | `SEC-TT-009` — Delegated execution is fail-open unless deployments opt into policy enforcement | `AT-19`, `CT-58`, `GR-19`, `RK-HX04` |

## RAHP-only findings

None.

## Security-only findings

- `SEC-TT-004` — VID scheme agility can produce authorization-equivalence confusion
- `SEC-TT-007` — Dynamic registry resolution remains an availability and semantic-integrity dependency
- `SEC-TT-011` — Consent anti-fatigue controls do not bound distinct-payload prompt floods
- `SEC-TT-012` — Bearer ceremony receipts create durable correlation and disclosure risk
