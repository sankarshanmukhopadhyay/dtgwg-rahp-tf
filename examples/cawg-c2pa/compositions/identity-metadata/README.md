# Identity × Metadata composition pressure test

This is a RAHP Toolkit v0.7.0 external assurance review. It is not an upstream conformance or governance decision.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-COMP-002` |
| Status | complete |
| Title | Identity × Metadata composition pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-metadata-assertion` |
| Target document | https://cawg.io/metadata/1.2-draft/ |
| Target version | 1.2 draft |
| Target commit | `64069e062b6dfa1105844a773fdfd80a69356b72` |
| Target source paths | — |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v0.7.0` |
| RAHP corpus date | 2026-08-14 |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/pressure-testing-a-spec.md` |
| Rule | Separate cryptographic validity, identity, authority, consent, lifecycle and relying-party trust; test both isolated and composed failure states. |

### Review scope

**Included**

- Normative and draft semantics relevant to the named composition or experiment.
- Cross-specification failure states that can remain hidden when each component is reviewed independently.

**Excluded**

- Legal opinion on enforceability in a particular jurisdiction.
- Claims that upstream CAWG, DIF, C2PA, GLEIF or W3C endorsed this RAHP assessment.

### Summary

| Measure | Value |
|---|---:|
| Findings | 2 |
| Open findings | 2 |
| Primary disposition: Governance | 1 |
| Primary disposition: Companion Specification | 1 |

**Overall assessment**

Cross-specification RAHP review: individually valid components are tested for unsafe composed conclusions and downgrade behaviour.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Authenticated metadata still needs property-specific authority | High | open | Governance | [CRK-03 — Integrity and factual truth conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-03) |
| `F-002` | Conflicting identity-backed metadata needs deterministic policy | High | open | Companion Specification | [CRK-04 — Conflicting authoritative assertions](/rahp-toolkit/docs/cawg-risk-register.html#crk-04) |

### Detailed findings

#### F-001 — Authenticated metadata still needs property-specific authority

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | — |
| Scenarios | `CAWG-024`, `CAWG-025` |
| Scenario patterns | `SP-GOV-01`, `SP-COMP-01` |
| Personas | — |
| Risks | [CRK-03 — Integrity and factual truth conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-03) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/metadata/1.2-draft/` | Metadata can be identity-backed without making the signer authoritative for every asserted property. |

**Potential harm**

Users may infer that identified signers make factually authoritative metadata claims.

**Recommended treatment**

Pair sensitive metadata namespaces with authority/governance semantics and distinct UX for integrity versus authoritative verification.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

#### F-002 — Conflicting identity-backed metadata needs deterministic policy

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | — |
| Scenarios | `CAWG-025` |
| Scenario patterns | `SP-FED-01`, `SP-COMP-01` |
| Personas | — |
| Risks | [CRK-04 — Conflicting authoritative assertions](/rahp-toolkit/docs/cawg-risk-register.html#crk-04) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-metadata-assertion/issues/7` | Metadata quality/attestation concerns show that authenticated assertions can carry uncertainty and competing claims. |

**Potential harm**

Different valid actors can provide incompatible provenance or rights metadata and consumers may choose arbitrarily.

**Recommended treatment**

Define precedence or multi-claim presentation semantics rather than treating later or locally preferred metadata as implicitly authoritative.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

<!-- END GENERATED PRESSURE TEST -->

