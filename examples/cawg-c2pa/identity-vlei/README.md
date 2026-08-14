# CAWG Identity vLEI experiment pressure test

This is a RAHP Toolkit v0.7.0 external assurance review. It is not an upstream conformance or governance decision.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-SR-011` |
| Status | complete |
| Title | CAWG Identity vLEI experiment pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-identity-assertion` |
| Target document | https://cawg.io/identity/1.3-draft+vlei/ |
| Target version | 1.3 vLEI experiment |
| Target commit | `1fbff9683fb692667a81206274d4b24d17078c0b` |
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
| Findings | 3 |
| Open findings | 3 |
| Primary disposition: Specification | 1 |
| Primary disposition: Companion Specification | 1 |
| Primary disposition: Implementation Guidance | 1 |

**Overall assessment**

The vLEI branch provides a strong organizational credential path but archival KERI evidence and cross-lane interpretation remain central assurance questions.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Role credentials need durable as-of validation | High | open | Specification | [CRK-21 — Timestamp or status evidence insufficiency](/rahp-toolkit/docs/cawg-risk-register.html#crk-21) |
| `F-002` | KERI dependency retention becomes part of content durability | High | open | Companion Specification | [CRK-02 — Historical verification continuity loss](/rahp-toolkit/docs/cawg-risk-register.html#crk-02) |
| `F-003` | Multiple identity trust lanes need explicit equivalence boundaries | High | open | Implementation Guidance | [CRK-20 — Alternative trust-method inconsistency](/rahp-toolkit/docs/cawg-risk-register.html#crk-20) |

### Detailed findings

#### F-001 — Role credentials need durable as-of validation

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | — |
| Scenarios | `CAWG-033`, `CAWG-034` |
| Scenario patterns | `SP-GOV-02`, `SP-RECOV-01` |
| Personas | — |
| Risks | [CRK-21 — Timestamp or status evidence insufficiency](/rahp-toolkit/docs/cawg-risk-register.html#crk-21) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-identity-assertion/commits/1fbff9683fb692667a81206274d4b24d17078c0b` | The branch contains an explicit TODO about archival-quality validation material and issuer signatures over historical validity. |

**Potential harm**

A later-revoked OOR/ECR credential can make historically legitimate content ambiguous, or current verification can misstate historical authority.

**Recommended treatment**

Specify archival evidence for role credential status at signing time, including issuer/key lifecycle and retained validation material.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

#### F-002 — KERI dependency retention becomes part of content durability

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | — |
| Scenarios | `CAWG-034` |
| Scenario patterns | `SP-OPS-01`, `SP-RECOV-01` |
| Personas | — |
| Risks | [CRK-02 — Historical verification continuity loss](/rahp-toolkit/docs/cawg-risk-register.html#crk-02) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/identity/1.3-draft+vlei/` | vLEI verification relies on KERI key-state and credential chains whose long-term availability is distinct from the asset itself. |

**Potential harm**

Long-lived media can outlive accessible KEL/key-state evidence needed to validate the signer and delegation chain.

**Recommended treatment**

Define minimum retained KERI evidence, resolver-independent verification requirements, and failure semantics when historical KEL material is unavailable.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

#### F-003 — Multiple identity trust lanes need explicit equivalence boundaries

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | — |
| Scenarios | `CAWG-006`, `CAWG-028` |
| Scenario patterns | `SP-INTEROP-01`, `SP-COMP-01` |
| Personas | — |
| Risks | [CRK-20 — Alternative trust-method inconsistency](/rahp-toolkit/docs/cawg-risk-register.html#crk-20) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-identity-assertion/issues/274` | CAWG discussions describe X.509, vLEI and W3C credential lanes with materially different trust roots and governance. |

**Potential harm**

Relying parties may render vLEI, X.509 and VC-backed assertions as equivalent even though their assurance, governance and lifecycle semantics differ.

**Recommended treatment**

Require trust-lane-specific result codes/metadata and prohibit UX from collapsing mechanisms into an undifferentiated verified identity state.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

<!-- END GENERATED PRESSURE TEST -->

