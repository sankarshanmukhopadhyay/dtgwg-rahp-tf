# RAHP worked examples

Worked examples demonstrate the portable RAHP method against independently governed targets. They are evidence and regression assets; they do not define portable RAHP semantics.

## Current maintained baseline

`examples/current-baselines.yaml` is the machine-readable authority for the **current maintained example baseline**. From RAHP v1.5.0 onward, it records:

- the RAHP release used for the current baseline;
- target and companion revision pins;
- evidence freshness;
- normalized residual posture;
- prior assessment baseline;
- assurance delta and finding lineage.

Detailed `pressure-test.yaml` records may intentionally preserve the RAHP version under which the original assessment was produced. Do not rewrite those historical provenance fields merely because a newer toolkit release exists. The current-baseline registry links the historical record to the current v1.5 disposition.

## Baseline lifecycle

```text
historical assessment
  -> evidence freshness evaluation
  -> v1.5 reassessment/revalidation
  -> explicit assurance delta
  -> current residual posture
  -> governed disposition or further review
```

A finding may remain unchanged across toolkit releases. Rebaselining does not imply remediation. Likewise, zero findings does not imply `assured`; unresolved evidence gaps or review obligations remain visible in current posture.

## Maintained examples

The v1.5 registry currently maintains examples spanning independent ecosystems:

- CAWG/C2PA portfolio composition;
- DTG Trust Tasks x Credential Specification;
- DTG Credential Specification x ZKP;
- DTG Trust Tasks x ZKP.

OpenVTC and ARPA assessments remain in the reassessment queue where refreshed target/runtime evidence is required before a current v1.5 disposition can be asserted safely.

## Validation

The v1.5 release qualification validator checks the registry for:

- RAHP v1.5.0 current-baseline declaration;
- immutable historical-record policy;
- valid detailed-record links;
- normalized residual states;
- prior-baseline lineage;
- explicit assurance deltas;
- a minimum set of independent maintained examples.

Run:

```bash
python3 tools/validate_v15_release.py
```

Deployment-specific example semantics must remain outside the portable method and engine contract.
