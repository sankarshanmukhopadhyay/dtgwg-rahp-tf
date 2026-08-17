---
layout: default
title: "Add a toolkit capability"
nav_order: 2
has_toc: true
parent: Implement RAHP
---
# Add a toolkit capability

Use this workflow for new executable behaviour: CLI commands, validators, renderers, monitors, publication helpers, configuration features, Python tooling or TypeScript implementation features.

A capability is complete only when another adopter can **discover it, configure it, run it, test it and understand the evidence it produces**.

## Step 1 — Define the user-visible capability before writing code

Write a short capability statement:

> Given **input X**, RAHP performs **behaviour Y**, produces **evidence Z**, and does **not** exercise authority beyond **boundary B**.

Then identify:

- intended user/operator;
- inputs and configuration;
- output/evidence artefacts;
- failure behaviour;
- whether it reads external state, writes external state, or both;
- whether it changes the portable method or only implements existing semantics.

This prevents implementation convenience from becoming accidental governance.

## Step 2 — Classify the change against the stable engine boundary

Ask whether the capability changes any stable v1 contract:

- normalized result schema;
- engine contract semantics;
- evidence-retention contract;
- configuration schema relied upon by other implementations.

If **no**, keep the capability additive and preserve the v1 boundary.

If **yes**, update the relevant schema/contract intentionally and include migration/conformance impact. Do not silently change a stable contract through a CLI feature.

Useful references:

- `method/engine-contract.yaml`
- `method/schema/rahp-result.schema.json`
- `method/evidence-retention.yaml`
- [Engine contract](engine-contract.md)
- [Conformance](conformance.md)

## Step 3 — Choose the implementation surface

Use the narrowest appropriate layer:

| Capability type | Primary location |
|---|---|
| Python orchestration/CLI | `tools/rahp.py` or a focused module under `tools/` |
| Validator | `tools/validate_*.py` plus integration into the appropriate aggregate validation path |
| Renderer/build output | `tools/render_*.py`, `tools/build.py`, or Pages projection code |
| Monitoring/queue behaviour | focused monitor under `tools/`, deployment/profile configuration, durable state under `instances/` where applicable |
| TypeScript reference implementation | `packages/*` with cross-implementation conformance where relevant |
| New portable semantics | `method/` and schemas first; implementation second |

Avoid putting deployment-specific assumptions into `tools/` when they belong in a profile or instance adapter.

## Step 4 — Define the configuration contract

If the capability is configurable, extend an existing schema or add a schema before relying on free-form YAML.

For example, profile-driven behaviour should remain representable through the established configuration boundary rather than hard-coded repository names.

Validate configuration at entry points and fail with an actionable error that identifies the invalid field or missing requirement.

## Step 5 — Implement authority and side-effect boundaries explicitly

For every capability that can change external state, answer:

1. **Who invoked it?**
2. **What scope was delegated to it?**
3. **What external resource may it change?**
4. **Can the action be dry-run or previewed?**
5. **What prevents an unreviewed finding from becoming an automatic governance action?**
6. **What evidence records the attempted and completed action?**
7. **How is the capability disabled, revoked or bounded?**

Monitoring and assessment capabilities should prefer **detect → record → review** over automatically mutating an external specification repository unless explicit publication authority is configured.

## Step 6 — Make outputs machine-verifiable

Prefer structured output over prose-only output. If the capability produces durable assurance state, define:

- stable identifiers;
- schema or validated shape;
- source/target revision;
- timestamps where meaningful;
- status/disposition;
- evidence/provenance references;
- retest/retry conditions where applicable.

A log line is useful for debugging but is not automatically durable assurance evidence.

## Step 7 — Add tests before wiring the capability into CI

Add tests at the lowest layer that can prove the behaviour:

- unit/regression tests under `tests/` for Python behaviour;
- TypeScript tests/conformance fixtures under the existing workspace structure;
- validator fixtures for both valid and invalid cases;
- projection/link tests for documentation/build behaviour.

At minimum include:

1. a success case;
2. a failure/rejection case;
3. a boundary case proving the capability does **not** exceed its authority or scope.

A validator that has never been shown to reject an invalid fixture is weak evidence.

## Step 8 — Expose the capability through the supported interface

If it is a CLI capability, add it to the established command surface rather than requiring callers to import internal functions.

For `tools/rahp.py`, ensure help text explains the input, mode and output:

```bash
python3 tools/rahp.py --help
python3 tools/rahp.py <command> --help
```

If it is a library/API capability, export it through the appropriate package boundary and keep implementation-private helpers private.

## Step 9 — Add validation and CI coverage

Run the narrow tests first, then the repository suite:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 tools/validate.py
python3 tools/build.py
python3 tools/validate_reference_links.py
```

For TypeScript or engine-boundary changes:

```bash
npm run build:ts
npm run conformance
```

If the capability introduces a new validator that protects a repository invariant, wire it into `.github/workflows/validate.yml` or the most relevant dedicated workflow. Do not rely on contributors remembering a command that CI never runs.

## Step 10 — Add a worked example or fixture

Show the capability operating on a bounded example. The example should demonstrate:

- configuration/input;
- command or invocation;
- generated output/evidence;
- expected failure mode where useful.

Do not use a production deployment as the only documentation of a new capability.

## Step 11 — Document discovery and operation

Update the documentation where an adopter would naturally look. Depending on the capability this may include:

- `README.md` for high-level discoverability;
- `QUICKSTART.md` for a core workflow;
- `docs/configuration.md` for configuration;
- `docs/operate.md` for recurring/monitoring behaviour;
- `docs/implement.md` or a dedicated page for implementation capabilities;
- release notes and `CHANGELOG.md` for shipped behaviour.

Document **what evidence is produced** and **what the capability does not authorize**, not only the command syntax.

## Step 12 — Submit the PR with implementation evidence

The PR should include:

1. capability statement;
2. authority/scope boundary;
3. canonical files changed;
4. schema/configuration impact;
5. test cases added;
6. validator/CI integration;
7. example invocation and output;
8. compatibility/migration impact;
9. documentation updated.

## Done when

- [ ] the capability has a bounded user-visible contract;
- [ ] stable engine/method compatibility has been classified explicitly;
- [ ] configuration is schema-backed where appropriate;
- [ ] external side effects have explicit authority and evidence boundaries;
- [ ] success, rejection and boundary cases are tested;
- [ ] CI protects the new invariant when applicable;
- [ ] a worked example/fixture exists;
- [ ] documentation explains how to run and interpret the capability;
- [ ] full relevant validation/conformance is green.
