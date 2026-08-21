# Trust Tasks × DTG Credential Specification combined composition review

> Generated from the linked RAHP pressure-test and security-hardening YAML records. This report is a cross-lens synthesis, not a third independent test.

## Review metadata

| Field | Value |
|---|---|
| Combined review | `COMB-X-001` |
| Status | monitoring |
| Reviewed on | 2026-08-22 |
| Target | `trustoverip/dtgwg-trust-tasks-tf + trustoverip/dtgwg-cred-spec` |
| Version | Mixed-baseline synthesis: RAHP at Trust Tasks 2a40f6bd / Credentials b89f389a; security at Trust Tasks fbe196a8 / Credentials d19f7c9 |
| Commit | `—` |
| RAHP review | `SR-XSP-001` — 3 finding(s) |
| Security review | `SEC-X-001` — 12 finding(s) |
| RAHP version | `v1.2` |
| Engine contract | `rahp-engine-contract-v1` |
| Engine/method revalidated on | 2026-08-22 |

## How to read the combined view

The RAHP lens asks what harms, governance failures, assurance gaps, and affected-party consequences remain. The security lens asks how an adversary or compromised component can violate a security property. The synthesis below uses shared canonical RAHP context as a heuristic, weighted toward shared risks and guardrails. It shows only the strongest connections and does not imply that paired findings are identical.

## Strongest cross-lens connections

| RAHP finding | Security finding | Shared RAHP context |
|---|---|---|
| `F-001` — Authority and lifecycle coherence remains a cross-specification assurance gap | `SEC-X-001` — Valid task authentication plus valid credential membership does not establish delegated authority | `RK-AI01` |
| `F-001` — Authority and lifecycle coherence remains a cross-specification assurance gap | `SEC-X-012` — Organisational and agent identities can satisfy syntactic roles without proving accountable human/control relationships | `RK-AI01` |

## RAHP-only findings

- `F-002` — Execution, outcome binding and replay remain incompletely composed
- `F-003` — Privacy composition and contestability remain cross-boundary governance obligations

## Security-only findings

- `SEC-X-002` — taskContext identifies a task exchange, not a ceremony completion event
- `SEC-X-003` — Durable taskContext/thread identifiers can become cross-presentation correlation handles
- `SEC-X-004` — One accepted issuance task can mint multiple durable credentials without a shared idempotency invariant
- `SEC-X-005` — Authorization and registry state can change between task approval, issuance, and later verification
- `SEC-X-006` — Agent revocation does not automatically invalidate credentials or outstanding tasks derived from its former mandate
- `SEC-X-007` — Ceremony completion evidence and credential validity can be conflated by relying applications
- `SEC-X-008` — ZKP credential proofs do not yet compose with Trust Task outcome evidence without privacy or semantic leakage
- `SEC-X-009` — Both layers depend on trust-registry semantics without a shared query/failure contract
- `SEC-X-010` — Failure and refusal states can be lost before durable credential issuance
- `SEC-X-011` — Supported decision-making and legal delegation are not consistently representable across task and credential layers

## Reviewer synthesis notes

- Portable assurance patterns provide the shared semantic bridge between the RAHP and security lenses without replacing deployment-specific findings.
- The RAHP lens is current at Trust Tasks 2a40f6bd3b13c85c49123174fdbe4354b3c48d81 and Credential Specification b89f389abbdae77ba60b673c0836c781c2b54169.
- The security lens remains source-pinned at Trust Tasks fbe196a8a17ba3f99d0657a64be5ac58621023a1 and Credential Specification d19f7c9cac364fab8e50cf434513ef53fef80e37.
- Do not interpret this mixed-baseline synthesis as evidence that the current revisions have completed combined RAHP + security review. A security rerun is the retest condition for returning this record to complete status with a common target pin.
