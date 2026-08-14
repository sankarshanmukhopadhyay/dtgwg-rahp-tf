---
layout: default
title: "A2A protocol worked example"
nav_order: 16
has_toc: true
---
# A2A protocol worked example

RAHP includes a worked pressure test of the **Agent2Agent (A2A) Protocol v1.0.0** at `examples/a2a/`.

This example broadens the toolkit beyond credential, trust-task and content-authenticity specifications. It demonstrates how RAHP treats an **agent interoperability protocol** whose implementations are independently operated, potentially opaque, long-running and able to delegate work.

## What the example tests

The assessment focuses on six boundaries:

1. whether signed capability/skill metadata can be confused with authority or trust;
2. discovery origin, registry trust and metadata freshness;
3. preservation of delegated authority across multiple agent hops;
4. safe use of secondary credentials for downstream systems;
5. asynchronous callback and push-notification assurance; and
6. reconstructable action provenance without requiring disclosure of private model reasoning.

## Why new catalogue items were needed

The earlier RAHP catalogue already covered single-agent scope creep, stale authority, delegation credentials and agent audit logging. A2A exposed four additional reusable boundaries that were not represented cleanly:

| Boundary | New guardrail | Key risks |
|---|---|---|
| Discovery metadata vs authority | `GR-22` | `RK-AI05`, `RK-AI06` |
| Delegation continuity across agent hops | `GR-23` | `RK-AI07` |
| Asynchronous callback trust | `GR-24` | `RK-AI08` |
| Secondary credential non-transitivity | `GR-25` | `RK-AI09` |

These additions are **protocol-neutral**. They should be reused when reviewing MCP-mediated agents, agent registries, delegated commerce, travel agents, enterprise agent meshes, or other multi-agent systems where the same trust boundaries arise.

## Control-plane discipline

Not every finding is assigned to the A2A core specification. The review routes findings among:

- `specification` for a semantic non-inference boundary;
- `companion-specification` where interoperable delegation/credential semantics may be needed;
- `implementation-guidance` for callback assurance and provenance; and
- `governance` for discovery trust and registry policy.

This is intentional. RAHP evaluates whether the assurance obligation is covered **somewhere appropriate**, not whether every risk can be solved by adding another field to a protocol.

See the [worked assessment](../examples/a2a/README.md), [agent delegation governance](agent-delegation-governance.md), and [pressure-testing workflow](pressure-testing-a-spec.md).
