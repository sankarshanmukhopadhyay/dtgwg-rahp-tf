---
layout: default
title: "Evidence classification"
nav_order: 3
has_toc: true
parent: Operate assurance
---
# Evidence classification and control credit

RAHP distinguishes **retention class** from **semantic evidence class**. Retention (`ephemeral`, `referenced`, `durable`, `exemplar`) controls storage. Semantic classification controls how evidence contributes to an assurance proposition.

Evidence context identifies where the evidence comes from; evidence authority records how strongly it can support the claim. A CI workflow mentioning `retry`, for example, is `build-infrastructure` and usually incidental or supporting; normative retry semantics are `normative-spec` and `normative`; a passing lost-response test is `test` and may be `authoritative` for implementation assurance.

This enables first-class control credit. Mature targets may contain a risk signal and substantial mitigations. RAHP records controls already present, identifies what evidence remains missing, and reports the residual assurance state rather than mechanically promoting the signal to a finding.
