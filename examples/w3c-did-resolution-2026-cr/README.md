# W3C DID Resolution v1 — RAHP pressure test

This maintained example dispositions RAHP toolkit issue **#6** against the dated W3C
Candidate Recommendation Snapshot of **6 August 2026**.

## Disposition

- **Core DID Resolution:** conditionally acceptable as evidence-retrieval infrastructure.
- **DID URL dereferencing:** separate high-risk assurance object; not inherited from the core disposition.
- **Primary boundary:** successful resolution or cryptographic verification does **not** by itself establish authorization, legitimacy, governance status or relying-party fitness.

The canonical machine-readable record is [`pressure-test.yaml`](pressure-test.yaml). Re-run the
assessment when the dated CR is superseded by a materially changed specification snapshot.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `SR-006` |
| Status | complete |
| Title | W3C DID Resolution v1 Candidate Recommendation pressure test |
| Reviewed on | 2026-08-18 |
| Target repository | `w3c/did-resolution` |
| Target document | https://www.w3.org/TR/2026/CR-did-resolution-1.0-20260806/ |
| Target version | Candidate Recommendation Snapshot 06 August 2026 |
| Target commit | `13bd245a54d84a11d16ce6a04da70e8cd8dac4ba` |
| Target source paths | `§4 DID Resolution`, `§5-6 DID URL Dereferencing`, `§8 DID Resolution Architectures`, `§9 DID Resolution Result`, `§11 Errors`, `§12 Bindings`, `§13 Security Considerations`, `§14 Privacy Considerations` |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v1.1.0` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-18 |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/pressure-testing-a-spec.md` |
| Rule | Separate evidence retrieval from authority and trust decisions; prefer existing portable patterns before adding catalogue objects. |

### Review scope

**Included**

- core DID resolution semantics
- local, remote, proxied, verifiable and unverifiable resolution
- cache, freshness, version and deactivation semantics
- resolver and DID-method proof boundaries
- privacy of resolution activity
- DID URL dereferencing security boundary

**Excluded**

- assurance properties specific to any one DID method
- cryptographic review of individual verification suites
- downstream authorization policy not claimed by DID Resolution

### Summary

| Measure | Value |
|---|---:|
| Findings | 6 |
| Open findings | 6 |

**Overall assessment**

Core DID Resolution is conditionally acceptable as evidence-retrieval infrastructure. The Candidate Recommendation identifies many relevant security and privacy risks, but important assurance boundaries remain dependent on relying-party policy, deployment controls and method- specific semantics. DID URL dereferencing receives a separate, less mature disposition because it adds resource selection and network retrieval to the core resolution boundary.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Resolution success can be over-interpreted as authority or trust | Critical | open | Implementation Guidance | [CRK-01 — Identity-validity and authority conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-01), [CRK-14 — Trust-registry identity binding failure](/rahp-toolkit/docs/cawg-risk-register.html#crk-14) |
| `F-002` | Cached valid state can become stale authority state | High | open | Operational Policy | [CRK-09 — Stale delegated or organizational authority](/rahp-toolkit/docs/cawg-risk-register.html#crk-09), [CRK-21 — Timestamp or status evidence insufficiency](/rahp-toolkit/docs/cawg-risk-register.html#crk-21) |
| `F-003` | Remote resolution can create correlation and surveillance evidence | High | open | Governance | [CRK-19 — Selective-disclosure correlation leakage](/rahp-toolkit/docs/cawg-risk-register.html#crk-19) |
| `F-004` | Responsibility and redress are fragmented across the resolution chain | High | open | Governance | [CRK-15 — Registry and governing-authority availability dependency](/rahp-toolkit/docs/cawg-risk-register.html#crk-15) |
| `F-005` | Resolver proof can be mistaken for method or current-state proof | High | open | Implementation Guidance | [CRK-12 — Required-evidence downgrade ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-12) |
| `F-006` | DID URL dereferencing materially expands the attack and privacy surface | Critical | open | Specification | [CRK-22 — Unsafe external-resource resolution](/rahp-toolkit/docs/cawg-risk-register.html#crk-22) |

### Detailed findings

#### F-001 — Resolution success can be over-interpreted as authority or trust

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | Specification, Governance |
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
| Harms | `HRM-INF-01`, `HRM-SEC-02`, `HRM-AUT-04` |
| Risks | `RKP-DISC-01`, `RKP-CRD-01`, `RKP-AUTH-01` |
| Controls | `CTP-DISC-01`, `CTP-AUTH-01` |
| Guardrails | `GRP-AUTH-01` |
| Assurance | `ATP-AUTH-01` |
| Evidence | `EVP-AUTH-01` |

**Evidence**

| Source | Observation |
|---|---|
| `DID Resolution core result semantics` | A successful or verifiable result can establish resolution/verification evidence without establishing authorization, legal authority, governance status, endorsement or relying-purpose fitness. |

**Potential harm**

A downstream verifier can promote technical identifier control into an unsupported consequential trust decision.

**Recommended treatment**

Make the non-inference contract explicit in relying-party profiles and machine-verifiable assurance tests; do not treat successful resolution as authorization.

**Retest when**

- resolution result semantics or relying-party guidance materially changes

#### F-002 — Cached valid state can become stale authority state

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Operational Policy |
| Secondary dispositions | Implementation Guidance |
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
| Risks | `RKP-DISC-02`, `RKP-AUTH-02`, `RKP-CRD-02`, `RKP-COMP-02`, `RKP-OPS-01` |
| Controls | `CTP-DISC-02`, `CTP-AUTH-02` |
| Guardrails | `GRP-AUTH-02`, `GRP-OPS-02` |
| Assurance | `ATP-AUTH-01` |
| Evidence | `EVP-AUTH-01`, `EVP-OPS-01` |

**Evidence**

| Source | Observation |
|---|---|
| `caching, versioning and DID document metadata` | Version/deactivation metadata exists, but consequential reliance still requires a policy for observation time, cache state, acceptable age and failure to obtain current authoritative state. |

**Potential harm**

Rotated, compromised or deactivated verification material may continue to satisfy later verification from stale cache state.

**Recommended treatment**

Bind consequential reliance to an explicit freshness contract including source, observation time, version, cache state and acceptable maximum age.

**Retest when**

- normative freshness/cache assurance requirements are added

#### F-003 — Remote resolution can create correlation and surveillance evidence

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | Operational Policy |
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
| Harms | `HRM-PRV-02`, `HRM-PRV-03`, `HRM-PRV-04`, `HRM-PRV-05` |
| Risks | `RKP-PRV-01`, `RKP-PRV-02`, `RKP-PRV-03` |
| Controls | `CTP-PRV-01`, `CTP-PRV-02` |
| Guardrails | `GRP-PRV-01`, `GRP-PRV-02` |
| Assurance | — |
| Evidence | — |

**Evidence**

| Source | Observation |
|---|---|
| `remote/proxied resolver architecture and privacy considerations` | The fact and sequence of DID lookups can reveal sensitive relationships even when DID Document contents are public. |

**Potential harm**

Resolver logs and telemetry can reconstruct interaction graphs or sensitive institutional/social relationships.

**Recommended treatment**

Require deployment-specific logging, retention, telemetry, secondary-use and resolver-selection controls; prefer local/privacy-preserving resolution where feasible.

**Retest when**

- privacy requirements for network resolution materially strengthen

#### F-004 — Responsibility and redress are fragmented across the resolution chain

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
| `method, resolver, proxy and binding architectures` | A harmful outcome can span application, resolver, proxy, DID method and registry components even where each claims local correctness. |

**Potential harm**

Affected parties may be unable to identify the responsible component, governing authority or correction path after stale/incorrect resolution contributes to harm.

**Recommended treatment**

Maintain an assurance responsibility map and sufficient provenance to reconstruct the resolution path and identify remediation ownership.

**Retest when**

- standardized responsibility/provenance evidence is defined

#### F-005 — Resolver proof can be mistaken for method or current-state proof

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | Specification |
| Scenarios | — |
| Scenario patterns | — |
| Personas | — |
| Risks | [CRK-12 — Required-evidence downgrade ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-12) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Portable v1.1 assurance patterns**

| Layer | Patterns |
|---|---|
| Harms | `HRM-INF-01` |
| Risks | `RKP-DISC-01`, `RKP-AUTH-01` |
| Controls | `CTP-DISC-01` |
| Guardrails | `GRP-AUTH-01` |
| Assurance | — |
| Evidence | — |

**Evidence**

| Source | Observation |
|---|---|
| `resolver-added versus method-level proof semantics` | A resolver signature can establish resolver provenance without proving that the underlying method state is authoritative, independently verified or current. |

**Potential harm**

Additional cryptographic evidence can create false confidence by silently promoting a weaker provenance claim into a stronger trust claim.

**Recommended treatment**

Expose proof class/assurance semantics so applications can distinguish resolver provenance, method verification, registry verification, historical verification and current-state assurance.

**Retest when**

- proof metadata gains explicit assurance semantics

#### F-006 — DID URL dereferencing materially expands the attack and privacy surface

| Field | Value |
|---|---|
| Severity | Critical |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | Implementation Guidance, Runtime Control |
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
| Harms | `HRM-INF-01`, `HRM-PRV-02`, `HRM-SEC-02` |
| Risks | `RKP-OPS-01`, `RKP-COMP-02`, `RKP-PRV-02` |
| Controls | `CTP-OPS-02`, `CTP-PRV-02` |
| Guardrails | `GRP-OPS-02`, `GRP-PRV-02` |
| Assurance | `ATP-OPS-02` |
| Evidence | `EVP-OPS-01` |

**Evidence**

| Source | Observation |
|---|---|
| `DID URL dereferencing sections and security considerations` | Dereferencing adds resource selection, service endpoint interpretation, URL construction and potentially new network requests; the CR also marks dereferencing as a feature at risk. |

**Potential harm**

A resolver/dereferencer can cross from identifier-state retrieval into SSRF-like access, redirect/loop exhaustion, parser differentials, path/query ambiguity or privacy leakage.

**Recommended treatment**

Maintain a separate assurance disposition and combined security test suite for dereferencing; a positive core-resolution assessment must not imply dereferencing approval.

**Retest when**

- dereferencing architecture stabilizes or feature-at-risk status changes

<!-- END GENERATED PRESSURE TEST -->

