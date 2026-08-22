# RAHP worked examples

Worked examples demonstrate the portable RAHP method against independently governed targets. They are evidence and regression assets; they do not define portable RAHP semantics.

## Canonical maintained-example policy

From RAHP v1.5.0 onward, a **canonical maintained example** is expected to run on the current stable RAHP release.

The invariant is:

```text
canonical maintained example -> current stable RAHP v1.5.x
historical/versioned evidence -> original RAHP version preserved
```

For maintained pressure tests, the canonical `pressure-test.yaml` therefore records the current RAHP baseline directly. Older assessment provenance is not silently rewritten or discarded: each migrated example has a `history/pre-v1.5.yaml` pointer that records the original RAHP version and exact Git blob SHA, while Git history retains the full prior content.

`examples/current-baselines.yaml` is the machine-readable index for the current maintained example set. It records:

- the stable RAHP release used by canonical examples;
- target and companion revision pins;
- evidence freshness;
- normalized residual posture;
- prior assessment baseline;
- assurance delta and finding lineage.

The registry **indexes and validates current examples; it is not a substitute for updating them**.

## Baseline lifecycle

```text
historical assessment
  -> preserve exact prior blob identity
  -> evidence freshness evaluation
  -> v1.5 reassessment/revalidation
  -> canonical current pressure-test.yaml
  -> explicit assurance delta + finding lineage
  -> current residual posture + policy gate
  -> governed disposition or further review
```

A finding may remain unchanged across toolkit releases. Rebaselining does not imply remediation. Likewise, zero findings does not imply `assured`; unresolved evidence gaps or review obligations remain visible in current posture.

## Maintained examples on v1.5.0

The canonical v1.5 examples currently include:

- CAWG/C2PA portfolio composition;
- DTG Trust Tasks × Credential Specification;
- DTG Credential Specification × ZKP;
- DTG Trust Tasks × ZKP.

Each canonical record directly declares `reviewed_against.rahp_version: v1.5.0` and includes v1.5 evidence-lineage and assurance-posture fields.

OpenVTC and ARPA assessments remain in the reassessment queue where refreshed target/runtime evidence is required before a current executable assessment can be asserted safely. Their queue status does not prevent the maintained examples above from using the current toolkit baseline.

## Validation

The v1.5 release qualification validator checks that:

- the registry declares RAHP v1.5.0 as current;
- every canonical maintained example exists and itself declares RAHP v1.5.0;
- every canonical maintained example carries explicit lineage and current assurance posture;
- historical provenance pointers exist for migrated pre-v1.5 examples;
- normalized residual states are valid;
- prior-baseline lineage and assurance deltas are explicit;
- deployment-specific example semantics remain outside the portable method and engine contract.

Run:

```bash
python3 tools/validate_v15_release.py
```
