---
layout: default
title: "Remediation and retesting"
nav_order: 8
has_toc: true
parent: Operate assurance
---
# Governed remediation and evidence-based retesting

RAHP v1.2 makes remediation an assurance object rather than an unstructured recommendation. `method/schema/remediation-manifest.schema.json` records the finding, the control plane or authority that owns the requested outcome, concrete remediation outcomes, required closure evidence, and publication status.

Publication remains governed. A generated manifest may declare that an upstream issue is eligible, but it does not authorize RAHP automation to file or change an upstream repository. The authority boundary is preserved in machine-readable state.

`method/schema/retest.schema.json` binds a retest to the prior finding, prior revision, retested revision, outcome, and closure evidence. Valid outcomes are `resolved`, `residual`, `regression`, and `inconclusive`.

```text
finding → remediation manifest → governed change → retest → closure evidence → disposition
```

```bash
python3 tools/assurance_cli.py retest-outcome --previous finding --current controlled
```
