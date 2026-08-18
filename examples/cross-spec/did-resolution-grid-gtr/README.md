# DID Resolution × GRID/GTR cross-specification pressure test

This maintained worked example dispositions RAHP toolkit issue **#10** and tests the assurance
seam between W3C DID Resolution v1 and UN/CEFACT GRID/GTR.

The architectural contract is intentionally narrow:

```text
DID resolution
  -> technical identifier/control evidence
GRID authority state
  -> registrar authority/recognition evidence
registrar/DIA verification
  -> attributable assertion evidence
registration evidence
  -> subject/asset assertion evidence
relying-party policy
  -> trust decision
```

The composition is viable, but **not yet assurance-closed**. The canonical YAML records eight
open composition findings (two Critical, six High) and assigns each to the narrowest effective
control plane rather than treating every ecosystem dependency as a DID Resolution defect.

This example should be rerun when either the DID Resolution CR materially changes or GRID/GTR
changes authority, lifecycle, historical verification, DID/DIA binding or reliance semantics.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `XSR-003` |
| Status | complete |
| Title | W3C DID Resolution v1 × UN/CEFACT GRID/GTR cross-specification pressure test |
| Reviewed on | 2026-08-18 |
| Target repository | `w3c/did-resolution` |
| Target document | https://www.w3.org/TR/2026/CR-did-resolution-1.0-20260806/ |
| Target version | Candidate Recommendation Snapshot 06 August 2026 composed with UN/CEFACT GRID/GTR public-review material |
| Target commit | `13bd245a54d84a11d16ce6a04da70e8cd8dac4ba` |
| Target source paths | `W3C DID Resolution v1 Candidate Recommendation Snapshot 06 August 2026`, `UN/CEFACT GRID/GTR public-review working material observed August 2026` |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v1.1.0` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-18 |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/cross-spec-pressure-testing.md` |
| Rule | Preserve proposition boundaries across the composition and prohibit technical identifier control from silently becoming registrar authority or relying-party authorization. |

### Review scope

**Included**

- DID resolution as technical identifier-state and verification-material evidence
- GRID registrar authority, recognition, scope and lifecycle evidence
- temporal and historical verification across both layers
- resolver provenance, privacy and downgrade behaviour
- DID URL dereferencing where introduced into a GRID verification flow

**Excluded**

- claims that W3C or UN/CEFACT endorses this RAHP assessment
- legal opinion on any particular registrar or jurisdiction

### Summary

| Measure | Value |
|---|---:|
| Findings | 8 |
| Open findings | 8 |
| Primary disposition: Governance | 3 |
| Primary disposition: Implementation Guidance | 2 |
| Primary disposition: Operational Policy | 1 |
| Primary disposition: Specification | 1 |
| Primary disposition: Runtime Control | 1 |

**Overall assessment**

The composition is viable but not assurance-closed. DID Resolution supplies technical identifier-state and verification-material evidence; GRID must supply the legal/governance proposition of registrar authority, recognition, scope and lifecycle. Neither layer may silently substitute for the other.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Successful DID resolution can be over-read as registrar authority | Critical | open | Implementation Guidance | [CRK-01 — Identity-validity and authority conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-01), [CRK-14 — Trust-registry identity binding failure](/rahp-toolkit/docs/cawg-risk-register.html#crk-14) |
| `F-002` | GRID withdrawal or key compromise can diverge from previously issued DIA state | Critical | open | Governance | [CRK-09 — Stale delegated or organizational authority](/rahp-toolkit/docs/cawg-risk-register.html#crk-09), [CRK-21 — Timestamp or status evidence insufficiency](/rahp-toolkit/docs/cawg-risk-register.html#crk-21) |
| `F-003` | Historical and as-of authority cannot rely on current resolution alone | High | open | Governance | [CRK-02 — Historical verification continuity loss](/rahp-toolkit/docs/cawg-risk-register.html#crk-02), [CRK-21 — Timestamp or status evidence insufficiency](/rahp-toolkit/docs/cawg-risk-register.html#crk-21) |
| `F-004` | Resolver provenance and assurance downgrades can be hidden | High | open | Implementation Guidance | [CRK-12 — Required-evidence downgrade ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-12), [CRK-15 — Registry and governing-authority availability dependency](/rahp-toolkit/docs/cawg-risk-register.html#crk-15) |
| `F-005` | Resolver observation can expose sensitive GRID relationship queries | High | open | Operational Policy | [CRK-19 — Selective-disclosure correlation leakage](/rahp-toolkit/docs/cawg-risk-register.html#crk-19) |
| `F-006` | DID control can be over-read as legal-identity equivalence | High | open | Governance | [CRK-14 — Trust-registry identity binding failure](/rahp-toolkit/docs/cawg-risk-register.html#crk-14) |
| `F-007` | DID URL dereferencing adds an unnecessary attack boundary to GRID verification | High | open | Runtime Control | [CRK-22 — Unsafe external-resource resolution](/rahp-toolkit/docs/cawg-risk-register.html#crk-22) |
| `F-008` | Accountability and redress fragment across GRID, resolver and DID-method layers | High | open | Governance | [CRK-15 — Registry and governing-authority availability dependency](/rahp-toolkit/docs/cawg-risk-register.html#crk-15) |

### Detailed findings

#### F-001 — Successful DID resolution can be over-read as registrar authority

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | Governance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [CRK-01 — Identity-validity and authority conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-01), [CRK-14 — Trust-registry identity binding failure](/rahp-toolkit/docs/cawg-risk-register.html#crk-14) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-INF-01`, `HRM-SEC-02` |
| Risks | `RKP-DISC-01`, `RKP-AUTH-01` |
| Controls | `CTP-DISC-01`, `CTP-AUTH-01` |
| Guardrails | `GRP-AUTH-01` |
| Assurance | `ATP-AUTH-01` |
| Evidence | `EVP-AUTH-01` |

**Evidence**

| Source | Observation |
|---|---|
| `https://www.w3.org/TR/2026/CR-did-resolution-1.0-20260806/` | DID Resolution establishes identifier-state and verification-material evidence, not GRID registrar authority or legal/governance recognition. |

**Potential harm**

Technical DID control is promoted into legal/governance authority without checking the GRID authority record.

**Recommended treatment**

Enforce a non-inference rule: DID resolution evidence is an input to, never a substitute for, GRID authority evaluation; retain the GRID record/version and relying-policy decision trace.

**Retest when**

- GRID or DID Resolution defines a materially different authority-binding contract

#### F-002 — GRID withdrawal or key compromise can diverge from previously issued DIA state

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | Operational Policy |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [CRK-09 — Stale delegated or organizational authority](/rahp-toolkit/docs/cawg-risk-register.html#crk-09), [CRK-21 — Timestamp or status evidence insufficiency](/rahp-toolkit/docs/cawg-risk-register.html#crk-21) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-INF-01`, `HRM-SEC-02` |
| Risks | `RKP-AUTH-02`, `RKP-CRD-02`, `RKP-COMP-02` |
| Controls | `CTP-AUTH-02`, `CTP-DISC-02` |
| Guardrails | `GRP-AUTH-02` |
| Assurance | `ATP-AUTH-01` |
| Evidence | `EVP-AUTH-01` |

**Evidence**

| Source | Observation |
|---|---|
| `UN/CEFACT GRID/GTR lifecycle and historical-verification public-review material` | A previously valid technical verification path can remain cryptographically usable after registrar authority or verification material ceases to be current. |

**Potential harm**

A stale DID/DIA path may continue to verify after withdrawal, suspension, compromise or authority change.

**Recommended treatment**

Bind verification to effective-time lifecycle state, explicit current/historical status semantics and authoritative record version.

**Retest when**

- GRID lifecycle/status semantics or historical-verification rules materially change

#### F-003 — Historical and as-of authority cannot rely on current resolution alone

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | Implementation Guidance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [CRK-02 — Historical verification continuity loss](/rahp-toolkit/docs/cawg-risk-register.html#crk-02), [CRK-21 — Timestamp or status evidence insufficiency](/rahp-toolkit/docs/cawg-risk-register.html#crk-21) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-INF-01`, `HRM-GOV-02` |
| Risks | `RKP-AUTH-02`, `RKP-COMP-02` |
| Controls | `CTP-AUTH-02` |
| Guardrails | `GRP-AUTH-02` |
| Assurance | `ATP-AUTH-01` |
| Evidence | `EVP-AUTH-01`, `EVP-RED-01` |

**Evidence**

| Source | Observation |
|---|---|
| `UN/CEFACT GRID/GTR historical and as-of verification public-review material` | Current discovery state alone cannot prove whether registrar authority and verification material were valid at a prior transaction time. |

**Potential harm**

Audit, financing, insurance or dispute verification may be unable to reconstruct the applicable authority state at time T.

**Recommended treatment**

Maintain logically separate historical verification records and an explicit as-of evaluation contract carrying requested time, evaluation time, selected record/version, historical key/status and provenance.

**Retest when**

- GRID publishes normative historical/as-of verification semantics

#### F-004 — Resolver provenance and assurance downgrades can be hidden

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | Runtime Control |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [CRK-12 — Required-evidence downgrade ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-12), [CRK-15 — Registry and governing-authority availability dependency](/rahp-toolkit/docs/cawg-risk-register.html#crk-15) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-INF-01`, `HRM-SEC-02` |
| Risks | `RKP-DISC-01`, `RKP-OPS-01` |
| Controls | `CTP-DISC-01`, `CTP-OPS-02` |
| Guardrails | `GRP-OPS-02` |
| Assurance | `ATP-OPS-02` |
| Evidence | `EVP-OPS-01` |

**Evidence**

| Source | Observation |
|---|---|
| `https://www.w3.org/TR/2026/CR-did-resolution-1.0-20260806/` | Local, remote, proxied, verifiable and unverifiable resolution paths can provide materially different assurance while returning structurally usable results. |

**Potential harm**

A proxied or unverifiable resolution path is consumed as if it had the assurance of direct method verification.

**Recommended treatment**

Preserve resolution path, proof class and downgrade indicators through the GRID verification workflow; fail indeterminate rather than silently lowering assurance.

**Retest when**

- resolution provenance or verification-strength metadata becomes normative

#### F-005 — Resolver observation can expose sensitive GRID relationship queries

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Operational Policy |
| Secondary dispositions | Governance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [CRK-19 — Selective-disclosure correlation leakage](/rahp-toolkit/docs/cawg-risk-register.html#crk-19) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-PRV-02`, `HRM-PRV-03`, `HRM-PRV-04` |
| Risks | `RKP-PRV-01`, `RKP-PRV-02` |
| Controls | `CTP-PRV-01`, `CTP-PRV-02` |
| Guardrails | `GRP-PRV-01`, `GRP-PRV-02` |
| Assurance | — |
| Evidence | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://www.w3.org/TR/2026/CR-did-resolution-1.0-20260806/#privacy-considerations` | Network resolution exposes lookup activity to resolver infrastructure even when the resolved document itself is public. |

**Potential harm**

Resolver logs can reveal which registrars, entities or authority relationships a relying party is evaluating.

**Recommended treatment**

Minimize network resolution, logs, retention and secondary use; support privacy-preserving or local resolution where feasible and retain a deployment privacy policy as evidence.

**Retest when**

- resolver privacy requirements or GRID deployment architecture materially changes

#### F-006 — DID control can be over-read as legal-identity equivalence

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | Implementation Guidance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [CRK-14 — Trust-registry identity binding failure](/rahp-toolkit/docs/cawg-risk-register.html#crk-14) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-INF-01`, `HRM-SEC-02` |
| Risks | `RKP-AUTH-01` |
| Controls | `CTP-AUTH-01` |
| Guardrails | `GRP-AUTH-01` |
| Assurance | `ATP-AUTH-01` |
| Evidence | `EVP-AUTH-01` |

**Evidence**

| Source | Observation |
|---|---|
| `GRID/GTR registrar authority model composed with DID Resolution` | Control of DID verification material does not independently prove that the controller is the legal registrar or entity represented in GRID. |

**Potential harm**

A technically valid DID controller is treated as the legally/governance-recognized registrar without an independently governed binding.

**Recommended treatment**

Bind DID identifiers to GRID legal/governance records through explicit mapping provenance, effective period and governing authority evidence.

**Retest when**

- GRID publishes a normative identifier-to-registrar binding model

#### F-007 — DID URL dereferencing adds an unnecessary attack boundary to GRID verification

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Runtime Control |
| Secondary dispositions | Specification, Implementation Guidance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [CRK-22 — Unsafe external-resource resolution](/rahp-toolkit/docs/cawg-risk-register.html#crk-22) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-SEC-02`, `HRM-PRV-02` |
| Risks | `RKP-OPS-01`, `RKP-COMP-02` |
| Controls | `CTP-OPS-02` |
| Guardrails | `GRP-OPS-02` |
| Assurance | `ATP-OPS-02` |
| Evidence | `EVP-OPS-01` |

**Evidence**

| Source | Observation |
|---|---|
| `https://www.w3.org/TR/2026/CR-did-resolution-1.0-20260806/` | DID URL dereferencing adds resource selection, service endpoint interpretation, URL construction and potentially further network retrieval beyond core identifier-state resolution. |

**Potential harm**

A GRID workflow that follows DID service resources inherits SSRF-like, redirect, path/query ambiguity, loop and availability risks.

**Recommended treatment**

Use bounded dereferencing profiles only where necessary, enforce destination/resource controls, and keep core registrar-authority evaluation independent of unconstrained resource retrieval.

**Retest when**

- dereferencing architecture stabilizes or GRID adopts a normative dereferencing profile

#### F-008 — Accountability and redress fragment across GRID, resolver and DID-method layers

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | Implementation Guidance |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [CRK-15 — Registry and governing-authority availability dependency](/rahp-toolkit/docs/cawg-risk-register.html#crk-15) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-GOV-02`, `HRM-ECO-02` |
| Risks | `RKP-GOV-04` |
| Controls | `CTP-GOV-03` |
| Guardrails | `GRP-RED-01` |
| Assurance | — |
| Evidence | `EVP-RED-01` |

**Evidence**

| Source | Observation |
|---|---|
| `composed GRID, resolver, DID method and relying-party responsibility chain` | A harmful result may cross multiple independently operated and governed components even where each component behaved correctly according to its local contract. |

**Potential harm**

An affected party cannot determine who supplied stale or incorrect evidence, which authority governed the component, or who owns remediation.

**Recommended treatment**

Maintain a cross-boundary responsibility map, operator/governing-authority identity, auditable decision trace and contestation route.

**Retest when**

- cross-boundary provenance or redress contracts materially change

<!-- END GENERATED PRESSURE TEST -->

