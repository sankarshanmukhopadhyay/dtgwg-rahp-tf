---
layout: default
title: "How RAHP works"
nav_order: 2
has_toc: true
parent: Learn RAHP
---
# How RAHP works

RAHP converts affected-party analysis into standards assurance evidence.

1. Personas and contexts establish who participates and who bears consequences.
2. User stories and scenarios expose concrete decision and failure paths.
3. Risks describe failure mechanisms and harms describe consequence allocation.
4. Controls reduce likelihood or impact; guardrails prevent progression when hard preconditions fail.
5. Assurance tests and metrics produce evidence that controls are operating or guardrails are satisfied.
6. Recommendations translate findings into actionable standards or governance changes.
7. Risk acceptances and governance precedents preserve explicit decisions rather than allowing silent drift.

The validator makes structural integrity machine-verifiable. v0.8 also defines a language-neutral execution lifecycle (`source → observation → trigger → assessment → finding → disposition → baseline`) and normalized result contract. The build system turns canonical YAML into human and machine-readable evidence surfaces, while ordinary run exhaust remains outside durable Git state. See [Engine contract](engine-contract.md) and [Review evidence and retention](evidence-retention.md).

## v1.1: reusable assurance patterns

RAHP can now project a deployment finding onto a portable assurance chain: `HRM-* ← RKP-* → CTP-* → GRP-*/ATP-* → EVP-*`. The local finding remains authoritative for the reviewed deployment; the portable mapping makes recurring mechanisms comparable and testable across specifications. See [Assurance knowledge model](assurance-knowledge-model.md).
