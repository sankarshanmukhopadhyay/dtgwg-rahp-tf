# OpenVTC Cypress DRARM reference profile

This directory demonstrates how an ecosystem-specific target maps into RAHP's generic Distributed Resilience and Amplification Risk Model without changing DRARM itself.

Use the **Run distributed resilience assessment** workflow with:

```text
target_repository = OpenVTC/openvtc
target_ref = Cypress
target_type = mixed
profile_path = examples/resilience/openvtc-cypress/profile.yaml
upstream_repository = OpenVTC/openvtc
```

The profile deliberately uses `findings-and-review-gaps` because a tagged-release review benefits from surfacing unresolved assurance evidence as well as directly observed hazardous constructs. The generated RAHP issue includes upstream-ready issue text but uses `recommend-only`; upstream filing remains a governed follow-on action.
