---
layout: default
title: "Add a specification pressure test"
nav_order: 3
has_toc: true
parent: Implement RAHP
---
# Add a specification pressure test

Use this workflow to add a new RAHP assessment of a specification, protocol, profile or other governed technical artefact.

The goal is not to manufacture findings. The goal is to leave a **reproducible evidence trail** from a pinned target revision through affected people/scenarios and risk hypotheses to dispositions, controls and retest conditions.

## Step 1 — Choose the deployment/profile context

Decide which deployment owns the assessment vocabulary and governance context.

- Reuse an existing profile under `profiles/<id>/` when the target belongs to that deployment.
- Add a new profile when a new adopter/specification family needs independent configuration.
- Do not import DTG or CAWG local risk IDs into a new deployment just to make the validator happy.

The portable catalogue may be reused across deployments; deployment-local risk hypotheses remain local.

## Step 2 — Add or confirm the target configuration

Represent the repository in the applicable YAML profile with at least:

- stable target ID;
- repository;
- branch;
- assessment context/title;
- allowed review mode(s);
- included source paths where scope should be bounded.

Validate the profile:

```bash
python3 tools/rahp.py config-validate --config profiles/<profile>/rahp.yaml
python3 tools/rahp.py targets --config profiles/<profile>/rahp.yaml
```

Use the actual profile filename present in the deployment if it differs.

## Step 3 — Pin the exact target revision

Resolve the commit you intend to assess. A durable pressure test must identify the target with a full commit SHA rather than only `main`, `latest`, or an unpinned web page.

Prepare/resolve configured targets as needed:

```bash
python3 tools/rahp.py prepare \
  --config profiles/<profile>/rahp.yaml \
  --target <target-id>
```

The eventual review record must preserve the full SHA.

## Step 4 — Scaffold the review

Create a RAHP review working record:

```bash
python3 tools/rahp.py review \
  --config profiles/<profile>/rahp.yaml \
  --target <target-id> \
  --mode rahp
```

Ordinary review work belongs under `.rahp/reviews/`. Do not start by creating a polished `examples/` directory.

If you want to inspect the command without writing files first:

```bash
python3 tools/rahp.py review \
  --config profiles/<profile>/rahp.yaml \
  --target <target-id> \
  --mode rahp \
  --dry-run
```

## Step 5 — Establish personas and scenarios before writing findings

Identify actors who:

- exercise authority or delegated power;
- rely on the specification's claims;
- bear failures or exclusion costs;
- operate registries/intermediaries;
- represent vulnerable or edge conditions;
- act as autonomous/non-human agents where relevant.

Select applicable corpus scenarios and portable scenario patterns. Validate corpus references with:

```bash
python3 tools/validate_scenario_corpora.py
```

This prevents a clause-only review from missing composition, accessibility, degraded-operation, collusion or lifecycle harms.

## Step 6 — Inspect the target and reuse existing risk hypotheses first

For each relevant requirement or omission, ask:

1. What can an implementation infer or do?
2. Who has authority to cause that action?
3. Can authority be delegated, narrowed, suspended or revoked?
4. What harmful state can remain cryptographically valid?
5. Who bears the harm or cost?
6. What control plane can actually fix the issue?
7. What evidence would show the mitigation works?

Search the deployment's existing risk catalogue before adding a new local risk. Add one only when the existing vocabulary cannot represent the failure mechanism without distorting it.

## Step 7 — Write each finding as a traceable assurance record

Each finding should identify:

- stable finding ID;
- concise title;
- status and severity;
- affected personas/scenarios;
- deployment risk IDs;
- `portable_assurance` mappings where useful;
- primary disposition/control plane;
- source evidence tied to the pinned target;
- human harm statement;
- recommendation;
- retest trigger.

Minimum shape:

```yaml
findings:
  - id: F-001
    title: Concise finding
    status: open
    severity: High
    primary_disposition: specification
    personas: [P1, P3]
    scenarios: []
    risks: [RISK-LOCAL-01]
    controls: []
    guardrails: []
    assurance_tests: []
    portable_assurance:
      harms: [HRM-...]
      risks: [RKP-...]
      controls: [CTP-...]
    evidence:
      - source: spec/body.md#relevant-section
        observation: What the pinned text permits, omits or contradicts.
    harm: Who can be harmed and how.
    recommendation: Action at the narrowest effective control plane.
    retest_when:
      - Observable source or governance change that should trigger reassessment.
```

Do not force every finding into the `specification` disposition. Governance, implementation guidance, runtime controls, companion specifications and operational policy may have more legitimate authority.

## Step 8 — Add new local risks/controls only when the review needs them

If the pressure test exposes a genuinely new deployment risk hypothesis, add it to the deployment-owned vocabulary, not directly to the portable method.

If the same mechanism appears reusable across deployments, separately follow [Extend the assurance catalogue](contributing-catalogue.md) to propose a portable `HRM/RKP/CTP/GRP/ATP/EVP` pattern.

This separation keeps **finding evidence**, **deployment governance**, and **portable method knowledge** distinct.

## Step 9 — Render and validate the working review

Run:

```bash
python3 tools/render_pressure_tests.py
python3 tools/validate_pressure_tests.py
python3 tools/validate_reference_links.py
```

The validator should prove at least:

- target commit is pinned;
- finding metadata is complete;
- controlled dispositions are valid;
- referenced risks/controls/guardrails/tests resolve;
- generated reader output is current.

Fix errors before discussing promotion to `examples/`.

## Step 10 — Decide whether the review becomes a maintained example

Most completed reviews **do not need to become examples**.

Promote to `examples/<target>/` only when the review is deliberately useful as one or more of:

- teaching material;
- method regression fixture;
- conformance/portability exemplar;
- maintained cross-specification example.

Deployment decisions and durable local state should normally live under the deployment instance, with raw working artefacts kept according to the evidence-retention policy.

If promoting an example:

1. copy the canonical review YAML into the example structure used by neighboring exemplars;
2. preserve the pinned target revision;
3. render the generated README region;
4. add human interpretation only outside generated markers;
5. add it to relevant documentation indexes.

## Step 11 — Add security or combined analysis when the target warrants it

A RAHP pressure test focuses on human harms and governance-invalid states. If adversarial exploitation materially changes the assessment, add a security review and/or combined synthesis rather than collapsing both lenses into one unstructured list.

Validate with:

```bash
python3 tools/validate_security_reviews.py
python3 tools/validate_combined_reviews.py
```

For cross-specification compositions, also follow [Cross-spec pressure testing](cross-spec-pressure-testing.md).

## Step 12 — Run the full assessment validation set

Before submission:

```bash
python3 tools/validate_pressure_tests.py
python3 tools/validate_scenario_corpora.py
python3 tools/validate_security_reviews.py
python3 tools/validate_combined_reviews.py
python3 tools/build.py
python3 tools/validate_reference_links.py
python3 tools/validate.py
```

Run only applicable security/combined validators if the contribution does not contain those review modes, but the repository-wide validators must remain green.

## Step 13 — Document what changed and what must trigger retest

Update the relevant example/deployment documentation so a future reviewer can answer:

- what was assessed;
- against which commit;
- why the review was initiated;
- which findings remain open;
- which upstream change would close or weaken each finding;
- when the assessment should be re-run.

A pressure test without a retest condition is a snapshot, not a maintained assurance artefact.

## Step 14 — Submit the PR with assessment evidence

The PR should include:

1. target repository and full SHA;
2. profile/deployment context;
3. review mode and scope;
4. finding count by severity/disposition;
5. new deployment-local catalogue records, if any;
6. new portable patterns proposed separately, if any;
7. validation results;
8. whether the review is ordinary deployment evidence or a maintained exemplar;
9. explicit retest triggers.

## Done when

- [ ] the target is represented in a valid profile;
- [ ] the assessed revision is pinned to a full SHA;
- [ ] personas and scenarios were considered before final scoring;
- [ ] existing deployment risks were reused before new ones were created;
- [ ] every finding has source evidence, harm, disposition and retest trigger;
- [ ] portable mappings are used where they clarify a reusable mechanism;
- [ ] renderers and pressure-test validation pass;
- [ ] security/combined analysis is added when warranted;
- [ ] promotion to `examples/` is deliberate rather than automatic;
- [ ] documentation makes future reassessment straightforward.
