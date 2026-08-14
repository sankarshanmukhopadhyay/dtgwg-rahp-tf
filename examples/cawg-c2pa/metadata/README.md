# CAWG Metadata Assertion pressure test

This worked review is part of the RAHP v0.6.0 CAWG/C2PA external-deployment proof. It is an independent assessment and does not represent CAWG, DIF or C2PA consensus.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-SR-002` |
| Status | complete |
| Title | CAWG Metadata Assertion pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-metadata-assertion` |
| Target document | https://cawg.io/metadata/1.2-draft/ |
| Target version | 1.2 draft |
| Target commit | `64069e062b6dfa1105844a773fdfd80a69356b72` |
| Target source paths | — |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v0.6.0` |
| RAHP corpus date | 2026-08-14 |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/pressure-testing-a-spec.md` |
| Rule | Treat cryptographic validity, identity, authority, consent, provenance and relying-party trust as distinct propositions; route remediation to the narrowest effective control plane. |

### Review scope

**Included**

- Metadata integrity, namespace semantics, identity-backed attestations and relying-party interpretation.

**Excluded**

- Implementation-specific vulnerability testing beyond normative/documented behaviour.
- Legal opinion on whether a signal is enforceable in any jurisdiction.

### Summary

| Measure | Value |
|---|---:|
| Findings | 2 |
| Open findings | 2 |
| Primary disposition: Implementation Guidance | 1 |
| Primary disposition: Governance | 1 |

**Overall assessment**

This is a bounded RAHP v0.6.0 readiness pressure test, not an upstream conformance certification. Findings focus on harms, authority/lifecycle boundaries and composition behaviour that matter when the specification is adopted or mandated.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Tamper-evident metadata can be mistaken for factually authoritative metadata | High | open | Implementation Guidance | [CRK-03 — Integrity and factual truth conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-03) |
| `F-002` | Namespace and authority conflicts lack a general precedence model | Medium | open | Governance | [CRK-04 — Conflicting authoritative assertions](/rahp-toolkit/docs/cawg-risk-register.html#crk-04) |

### Detailed findings

#### F-001 — Tamper-evident metadata can be mistaken for factually authoritative metadata

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-INTEROP-01`, `SP-COMP-01` |
| Personas | — |
| Risks | [CRK-03 — Integrity and factual truth conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-03) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/metadata/1.2-draft/` | The metadata assertion binds broad external metadata to a C2PA Manifest, including use cases where the manifest signer does not attest to the accuracy of gathered metadata. |

**Potential harm**

Consumers can display or automate on authenticated metadata as if authenticity of packaging implied truth, provenance authority, copyright ownership, or professional status.

**Recommended treatment**

Require implementations and UX profiles to distinguish integrity/authorship from factual authority, and define when an identity-backed attestation or external authority is required for high-impact metadata fields.

**Retest when**

- Conformance guidance includes negative tests where metadata integrity succeeds but authority/truth is intentionally unestablished.

#### F-002 — Namespace and authority conflicts lack a general precedence model

| Field | Value |
|---|---|
| Severity | Medium |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-FED-01`, `SP-INTEROP-01` |
| Personas | — |
| Risks | [CRK-04 — Conflicting authoritative assertions](/rahp-toolkit/docs/cawg-risk-register.html#crk-04) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/metadata/1.2-draft/` | The assertion intentionally permits metadata from multiple external standards and namespaces, enabling overlapping semantic claims from different authorities. |

**Potential harm**

Two valid metadata assertions can encode conflicting claims, leaving platforms to invent precedence rules and creating inconsistent treatment across implementations.

**Recommended treatment**

Define a conflict-handling profile that identifies authoritative sources by metadata domain, preserves disagreement rather than silently choosing a value, and exposes unresolved conflicts to relying parties.

**Retest when**

- Cross-implementation tests cover contradictory valid metadata from different namespaces/actors.

<!-- END GENERATED PRESSURE TEST -->

