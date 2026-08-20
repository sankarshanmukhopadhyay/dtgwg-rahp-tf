---
layout: default
title: Actor-chain delegation assurance
nav_order: 74
---
# Actor-chain delegation assurance

Actor/delegation lineage is an **attribution surface**, not an authority credential. RAHP evaluates lineage in separate planes so a chain that looks internally consistent cannot silently become permission to act.

## Required separation

| Plane | Question | Example result |
|---|---|---|
| Lineage well-formedness | Does each hop narrow scope and obey structural rules? | pass/fail |
| Evidence resolution | Can independent grant evidence be obtained and validated? | missing/unresolvable/invalid/resolvable |
| Lifecycle | Was the evidenced grant current at the relevant time? | active/expired/revoked |
| Authorization | Did relying policy permit the requested action? | permit/deny/indeterminate |
| Disclosure | Was only necessary lineage exposed? | minimized/excessive |

A pass on the first row MUST NOT imply a pass on any later row.

## Portable pressure-test questions

- Can a fabricated but monotonically narrowing chain trigger a consequential action?
- Can a forwarding actor rewrite an earlier hop without detection?
- Are missing, unresolvable, invalid, revoked/expired and denied states distinguishable in evidence?
- Is a proof/content reference domain-separated or otherwise bound to the authority context?
- Can the same assurance objective be met without disclosing every durable actor identifier?

These questions are protocol-neutral. A2A issue #2028 is one current example of the design surface; the RAHP patterns apply equally to other multi-agent, delegation, workflow, and cross-protocol systems.
