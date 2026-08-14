---
layout: default
title: "Contributing"
nav_order: 22
has_toc: true
---
# Contributing to the RAHP Toolkit

The toolkit improves through use. This document tells you where things live, how
to change them safely, and what a reviewable contribution looks like.

## The one rule

**Edit the canonical source for the layer you are changing; never hand-edit `build/`.**

RAHP has more than one authority boundary. `method/` is portable method authority. Root `data/` is the bundled DTG exemplar catalogue retained for compatibility and generated evidence. A deployment may own assessment vocabulary and state under `instances/<id>/`. Profiles under `profiles/<id>/` declare deployment targets. Generated material under `build/` is derived and must be regenerated, never edited directly.

## Repository layout

```
method/            Portable RAHP method: lifecycle, vocabulary and schemas.
  lifecycle.yaml     Five lifecycle stages, their evidence requirements, and every known gap
  vocabularies.yaml  Controlled vocabularies (severity, standards status, persona type, …)
  schema/            JSON Schema for every record type
data/              Bundled DTG exemplar catalogue; not the portable RAHP method.
  instance.yaml      Namespaces, cross-reference edges, invariants — drives the validator
  risks.yaml  controls.yaml  guardrails.yaml  assurance-tests.yaml
  metrics.yaml  user-stories.yaml  scenarios.yaml  epics.yaml  personas.yaml
  recommendations.yaml  risk-acceptances.yaml  governance-precedents.yaml
profiles/          Deployment configuration (for example dtg/ and cawg/).
instances/         Deployment-owned state, reviews and optional local vocabularies.
tools/             Portable orchestration, validation, monitoring and build tooling.
context/           JSON-LD context
build/             Generated. Do not hand-edit; regenerate after canonical changes.
```

## Setup

```bash
pip install -r requirements.txt
python3 tools/validate.py     # must exit 0 before you start
```

## Making a change

1. Edit the authoritative source for the change: `method/` for method semantics, root `data/` for the bundled DTG exemplar, `instances/<id>/data/` for deployment-local assessment vocabulary, or `profiles/<id>/` for target configuration.
2. Add a `provenance` block to every record you add or materially change:

   ```yaml
   provenance:
     source: "Target Specification v1.2 §5.2"   # what you were reading
     triggered_by: "spec-review-2026-09"        # the activity that surfaced it
     contributor: "your name or handle"
     imported: 2026-09-14
   ```

   Provenance is not bureaucracy. It is how a reader in two years works out
   whether a risk score reflects evidence or someone's Tuesday afternoon.

3. Run `python3 tools/validate.py`. Fix errors. Read the warnings — most of them
   are telling you something true.
4. Run `python3 tools/build.py` if you want to see the change in the site.
5. Open a PR using the template. Paste the validator summary line into it:

   ```
   python3 tools/validate.py --summary
   ```

## Adding each record type

**A risk** (for example bundled DTG `RK-*`, or a deployment-local namespace such as CAWG `CRK-*`) needs: a category, a lifecycle phase, a description that
says what goes wrong, a harm description that says who is hurt, severity and
likelihood, and at least one metric that would move if it happened. A risk you
cannot measure is an opinion.

**A control (`CT-xx`)** reduces probability or impact. It must link to at least
one risk, and — transitively, through that risk — reach at least one metric. The
validator enforces this: a control that reaches no metric is unmonitorable.

**A guardrail (`GR-xx`)** is a binary phase-gate pre-condition. It must have at
least one assurance test. Guardrails are hard stops, not aspirations. If you find
yourself wanting to write "should", you are describing a control.

**An assurance test (`AT-xx`)** is binary pass/fail evidence for exactly one
guardrail. State the pass criterion so precisely that two people testing
independently would agree on the result.

**A metric (`M-xx`)** is a measurement instrument. It belongs to the shared
identifier space that links every artefact — never reuse an M number.

**A persona** is an analytical instrument, not a marketing profile. Give it
realistic context, documented objectives and vulnerabilities, and cite evidence
with a resolvable URL. Do not write cross-references into `personas.yaml` — they
are computed at build time from the records that reference the persona.

**A recommendation (`REC-xx`)** proposes a change to the target specification.
Set `class` to `normative`, `recommended` or `process`, and `status` truthfully.

**A risk acceptance (`RA-xxx`)** — read the header of `data/risk-acceptances.yaml`
before adding one. There is currently no agreed acceptance authority, so every
record is `pending`. Do not invent one.

**A governance precedent (`GP-xxx`)** records *why* a decision was made inside a deployment, so a future contributor does not silently reverse it. A governance decision in one deployment does not automatically change the portable RAHP method or another deployment.

## Severity and Critical

`Critical` is not "very High". It marks a risk whose non-zero incidence is
unacceptable — legal, criminal or safeguarding consequence. Critical risks have
no numeric score, must be gated by a guardrail, and **may not be risk-accepted**.
The validator enforces this.

## Naming conventions

- Files in `data/` and `method/`: lowercase, hyphenated, `.yaml`.
- No version numbers in filenames. Git tags carry versions; `CHANGELOG.md`
  explains them. (The old `_v3`/`_v4`/`(1)` filenames are exactly what this rule
  is here to prevent.)
- Identifiers never change meaning. If a risk is superseded, retire the ID and
  record why — do not reuse it.

## Using an AI assistant

`docs/ai-assisted-process.md` covers this in detail. Two rules apply here:

- Anything an assistant drafts enters the repository through the same PR review
  as anything else. There is no fast path.
- Set `provenance.contributor` to `"<your name> (AI-assisted)"` when a record was
  substantially drafted by an assistant. This is not a warning label; it lets a
  reviewer calibrate how much independent verification the record needs. Risk
  scoring, guardrail verification and governance decisions are not assistant work.

## Contributing a specification pressure test

Use `docs/pressure-testing-a-spec.md` and place worked review material under `examples/<target>/` unless/until the Working Group decides to make review records part of canonical `data/`. Every finding should identify the target version/commit, linked RAHP risks, disposition, status, and evidence or resolution reference.

A finding is not a mandate to edit the core specification. Reviewers must identify the control plane with legitimate authority and an enforceable evidence path.

## Review expectations

A PR is ready when: `validate.py` exits 0, every new record has provenance, and
the description says what triggered the change. A PR that changes a risk score
should say what evidence moved it.
