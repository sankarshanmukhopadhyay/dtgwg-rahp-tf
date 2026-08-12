# DTG RAHP Toolkit

**Risk Assessment & Harms Prevention Task Force · Decentralised Trust Graph Working Group**  
Working Draft · toolkit v0.3-dev · CC-BY 4.0

RAHP is a repeatable assurance method for pressure-testing standards against risks and human harms, tracing findings to controls and evidence, and feeding actionable changes back into specification development. This repository contains both the **portable RAHP method** and a **DTG-specific worked instance**.

## What do you want to do?

| Goal | Start here |
|---|---|
| Review a specification for risks and harms | [Pressure-testing a specification](docs/pressure-testing-a-spec.md) |
| Understand the RAHP method | [How RAHP works](docs/how-rahp-works.md) |
| Explore the DTG instance | [DTG instance](docs/index.md#explore-the-dtg-instance) |
| Adopt RAHP for another Working Group | [Adoption guide](ADOPTION.md) |
| Make a small first assessment | [Minimum viable RAHP](examples/minimal-instance/README.md) |
| Contribute risks, controls, or evidence | [Contributing](CONTRIBUTING.md) |
| Understand where a remediation belongs | [Governance boundaries](docs/governance-boundaries.md) |

## Operating model

```mermaid
flowchart TB
  A[Standards WG / Spec Author] --> M
  subgraph M[Portable RAHP Method]
    L[Lifecycle]
    V[Controlled vocabularies]
    S[Schemas and invariants]
  end
  M --> I
  subgraph I[RAHP Instance]
    P[Personas] --> U[User Stories]
    P --> SC[Scenarios]
    U --> R[Risks]
    SC --> R
    R --> H[Harms]
    R --> C[Controls]
    R --> G[Guardrails]
    G --> T[Assurance Tests]
    C --> ME[Metrics]
    R --> REC[Recommendations]
  end
  I --> X[Target Specification]
  M --> TOOLS[Validator and build system]
  I --> TOOLS
  TOOLS --> OUT[Generated site · JSON/JSON-LD · coverage views · action set]
```

The mental model is simple: **people and contexts surface scenarios; scenarios surface risks; risks drive controls and guardrails; guardrails become testable; findings feed back into specification development.**

## Repository architecture

| Path | Authority and editability |
|---|---|
| `method/` | Portable RAHP mechanics: lifecycle, controlled vocabularies, schemas. Change deliberately because adopters inherit it. |
| `data/` | Canonical DTG RAHP instance. This is the source of truth for risks, controls, personas, scenarios and related records. |
| `tools/` | Validation and build automation. Produces machine-verifiable evidence and generated views. |
| `context/` | JSON-LD context used by generated linked-data outputs. |
| `docs/` | Guided narrative for understanding and applying RAHP. |
| `examples/` | Worked pressure tests and minimum viable adoption patterns. |
| `build/` | Generated output. Do not hand-edit. |
| `archive/` | Historical source artefacts and old generated views retained for provenance. Do not edit. |

See the [full repository map](docs/diagrams/repository-map.md) and [artefact relationship model](docs/diagrams/artefact-relationships.md).

## Quick start

```bash
pip install -r requirements.txt
python3 tools/validate.py
python3 tools/build.py
open build/site/index.html
```

`tools/validate.py` checks schema conformance, vocabularies, identifiers, references, symmetry, invariants, orphans and README counts. A clean exit is the minimum evidence that the instance is internally coherent.

## What is in the DTG instance

| Prefix | Type | Count |
|---|---|---|
| `RK-xx` | Risk | 43 risks |
| `CT-xx` | Control | 66 controls |
| `GR-xx` | Guardrail | 21 guardrails |
| `AT-xx` | Assurance test | 21 assurance tests |
| `M-xx` | Trust metric | 37 metrics |
| `US-xx` | User story | 36 user stories |
| `SC-xx` | Scenario | 33 scenarios |
| `EPIC-xx` | Capability cluster | 21 EPICs |
| `D/M/B/EC` | Persona | 16 personas |
| `REC-x` | Standards recommendation | 9 recommendations |
| `RA-xxx` | Risk acceptance | 3 risk acceptances (all `pending`) |
| `GP-xxx` | Governance precedent | 3 governance precedents |

These counts are checked by `tools/validate.py` and cannot silently drift.

## Three distinctions that matter

**Controls (`CT-xx`)** continuously reduce likelihood or impact. **Guardrails (`GR-xx`)** are hard-stop preconditions before progression. **Assurance tests (`AT-xx`)** are binary evidence that a guardrail has been satisfied.

`Critical` severity is not simply “very High”. It identifies a risk whose non-zero incidence is unacceptable. Critical risks carry no numeric score, must be gated by a guardrail, and may not be risk-accepted.

## Pressure-testing specifications

RAHP is more than a risk register. A specification review should create a traceable chain from target/version → affected personas/scenarios → triggered risks → controls/guardrails/evidence → finding disposition → standards action. Start with [the pressure-testing workflow](docs/pressure-testing-a-spec.md), then compare the [worked DTG Credential Specification example](examples/dtg-credential-spec/README.md) and the [Trust Tasks Framework example](examples/trust-tasks-spec/README.md). The two examples show both direct specification findings and findings deliberately routed to companion specifications, governance, runtime controls, and operational policy. The reusable starter is [`examples/pressure-test-template.yaml`](examples/pressure-test-template.yaml), and `python3 tools/validate_pressure_tests.py` checks review records against the canonical RAHP corpus.

A finding does **not** imply that every mitigation belongs in the reviewed specification. RAHP explicitly routes findings to the correct control plane: core specification, companion specification, governance, implementation guidance, runtime control, operational policy, formal risk acceptance, or no action when already addressed/out of scope.

## Known method gaps

Known gaps remain machine-readable in `method/lifecycle.yaml`. The blocking gaps include the absence of a formal risk-acceptance authority model (`GAP-3.1`) and contribution/integration governance (`GAP-5.1`). They are visible rather than hidden because assurance requires knowing not only what is controlled, but also where authority and enforcement remain undefined.

## Generated site

The generated site remains the drill-down evidence surface. Its database-oriented pages are generated from canonical YAML; the human entry point is now the guided documentation in this repository. Run `python3 tools/build.py` after canonical data changes.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: edit canonical sources, preserve provenance, validate before review, and never hand-edit generated outputs.

---

*Maintained by the Risk Assessment & Harms Prevention Task Force, DTGWG.*  
*CC-BY 4.0 — reuse with attribution.*
