# C2PA × CAWG portfolio stack composition pressure test

This is a RAHP Toolkit v0.7.0 external assurance review. It is not an upstream conformance or governance decision.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-COMP-005` |
| Status | complete |
| Title | C2PA × CAWG portfolio stack composition pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `c2pa-org/specifications` |
| Target document | https://spec.c2pa.org/specifications/specifications/2.4/index.html |
| Target version | 2.4 / tracked main |
| Target commit | `b1703dc0a0420088d3f8b0e5fb11866d0fe931cb` |
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
| Primary disposition: Implementation Guidance | 1 |
| Primary disposition: Companion Specification | 1 |

**Overall assessment**

Cross-specification RAHP review: individually valid components are tested for unsafe composed conclusions and downgrade behaviour.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | All cryptographic layers can validate while the trust decision is still unjustified | High | open | Implementation Guidance | [CRK-28 — Implementation/specification semantic collapse](/rahp-toolkit/docs/cawg-risk-register.html#crk-28) |
| `F-002` | Optional higher-layer assertion stripping is not distinguishable from legitimate absence | High | open | Companion Specification | [CRK-23 — Assertion stripping and downgrade](/rahp-toolkit/docs/cawg-risk-register.html#crk-23) |

### Detailed findings

#### F-001 — All cryptographic layers can validate while the trust decision is still unjustified

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | — |
| Scenarios | `CAWG-024`, `CAWG-028` |
| Scenario patterns | `SP-COMP-01`, `SP-INCL-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../../build/site/catalogue.html#P1), [P2 — Producer / Originating Actor](../../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../../build/site/catalogue.html#P3), [P4 — Intermediary / Platform Operator](../../../../build/site/catalogue.html#P4), [P6 — Registry / Discovery / Trust-Service Operator](../../../../build/site/catalogue.html#P6) |
| Risks | [CRK-28 — Implementation/specification semantic collapse](/rahp-toolkit/docs/cawg-risk-register.html#crk-28) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://cawg.io/specs/` | CAWG layers identity, metadata, permission and endorsement semantics over C2PA provenance, each with distinct trust meaning. |

**Potential harm**

A product can show a single success state even though provenance, identity, authority, consent and factual truth answer different questions.

**Recommended treatment**

Define a portfolio-level verifier result model and mandate UX separation of each independently evaluated proposition.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

#### F-002 — Optional higher-layer assertion stripping is not distinguishable from legitimate absence

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Companion Specification |
| Secondary dispositions | — |
| Scenarios | `CAWG-027` |
| Scenario patterns | `SP-COMP-01`, `SP-REPLAY-01` |
| Personas | [P2 — Producer / Originating Actor](../../../../build/site/catalogue.html#P2), [P3 — Relying Party / Verifier](../../../../build/site/catalogue.html#P3), [P4 — Intermediary / Platform Operator](../../../../build/site/catalogue.html#P4) |
| Risks | [CRK-23 — Assertion stripping and downgrade](/rahp-toolkit/docs/cawg-risk-register.html#crk-23) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://spec.c2pa.org/specifications/specifications/2.4/index.html` | C2PA provides the container/provenance substrate while CAWG gathered assertions can remain optional at the portfolio level. |

**Potential harm**

Intermediaries can remove consent, endorsement or identity evidence while preserving a valid lower-layer C2PA asset.

**Recommended treatment**

Define deployment profiles that declare expected/required assertion classes and produce explicit downgrade status when missing.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

<!-- END GENERATED PRESSURE TEST -->

