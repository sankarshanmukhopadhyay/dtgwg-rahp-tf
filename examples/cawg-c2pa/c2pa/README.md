# C2PA Technical Specification pressure test for CAWG dependency

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This worked review is part of the RAHP v0.6.0 CAWG/C2PA external-deployment proof. It is an independent assessment and does not represent CAWG, DIF or C2PA consensus.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-SR-008` |
| Status | complete |
| Title | C2PA Technical Specification pressure test for CAWG dependency |
| Reviewed on | 2026-08-14 |
| Target repository | `c2pa-org/specifications` |
| Target document | https://spec.c2pa.org/specifications/specifications/2.4/index.html |
| Target version | 2.4 / tracked main |
| Target commit | `b1703dc0a0420088d3f8b0e5fb11866d0fe931cb` |
| Target source paths | — |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v0.8.0` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-16 |
| Engine/method revalidated on | 2026-08-16 |
| Original RAHP version | `v0.6.0` |
| Revalidation scope | method-and-engine-only; target revision and substantive findings unchanged |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/pressure-testing-a-spec.md` |
| Rule | Treat cryptographic validity, identity, authority, consent, provenance and relying-party trust as distinct propositions; route remediation to the narrowest effective control plane. |

### Review scope

**Included**

- C2PA as the integrity/provenance substrate consumed by CAWG assertions; relying-party and composition boundaries.

**Excluded**

- Implementation-specific vulnerability testing beyond normative/documented behaviour.
- Legal opinion on whether a signal is enforceable in any jurisdiction.

### Summary

| Measure | Value |
|---|---:|
| Findings | 2 |
| Open findings | 2 |
| Primary disposition: Governance | 1 |
| Primary disposition: Implementation Guidance | 1 |

**Overall assessment**

This is a bounded RAHP v0.6.0 readiness pressure test, not an upstream conformance certification. Findings focus on harms, authority/lifecycle boundaries and composition behaviour that matter when the specification is adopted or mandated.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | A valid C2PA manifest is a provenance/integrity result, not a complete relying-party trust decision | High | open | Governance | [CRK-01 — Identity-validity and authority conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-01) |
| `F-002` | Optional assertion loss can create downgrade ambiguity unless relying parties know what evidence was required | High | open | Implementation Guidance | [CRK-12 — Required-evidence downgrade ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-12) |

### Detailed findings

#### F-001 — A valid C2PA manifest is a provenance/integrity result, not a complete relying-party trust decision

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-COMP-01`, `SP-INTEROP-01` |
| Personas | [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P4 — Intermediary / Platform Operator](../../../build/site/catalogue.html#P4) |
| Risks | [CRK-01 — Identity-validity and authority conflation](/rahp-toolkit/docs/cawg-risk-register.html#crk-01) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://spec.c2pa.org/specifications/specifications/2.4/index.html` | C2PA defines signed manifests, assertions and validation machinery; higher-layer assertion semantics and relying-party trust policy are supplied by applications, assertion specifications and governance. |

**Potential harm**

Organizations can mandate C2PA and then overstate what successful validation proves about identity, factual truth, rights, consent or authority.

**Recommended treatment**

Mandate profiles should define decision semantics above C2PA validation, including which CAWG assertions and trust policies are required for each claimed outcome.

**Retest when**

- A conformance profile distinguishes C2PA structural/cryptographic validation from higher-layer identity, authority, consent and truth decisions.

#### F-002 — Optional assertion loss can create downgrade ambiguity unless relying parties know what evidence was required

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | — |
| Scenarios | — |
| Scenario patterns | `SP-COMP-01`, `SP-INTEROP-01` |
| Personas | [P2 — Producer / Originating Actor](../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../build/site/catalogue.html#P3), [P4 — Intermediary / Platform Operator](../../../build/site/catalogue.html#P4) |
| Risks | [CRK-12 — Required-evidence downgrade ambiguity](/rahp-toolkit/docs/cawg-risk-register.html#crk-12) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://spec.c2pa.org/specifications/specifications/2.4/index.html` | C2PA supports extensible assertions and provenance chains; applications may encounter assets whose manifests or optional higher-layer assertions differ across transformations and distribution paths. |

**Potential harm**

A consumer can accept an asset with fewer assurance assertions than the producer or policy expected, particularly when identity, consent or endorsement evidence is absent rather than cryptographically invalid.

**Recommended treatment**

Define deployment-level required-assertion policies and downgrade detection: validators should distinguish absent, unsupported, stripped/expected and invalid evidence where the workflow provides enough context to know what was required.

**Retest when**

- CAWG/C2PA composition tests cover removal or absence of required Identity, Consent, Metadata and Endorsement assertions.

<!-- END GENERATED PRESSURE TEST -->

