---
layout: default
title: Personas and actor roles
nav_order: 3
has_toc: true
parent: Learn RAHP
---

# Personas and actor roles

RAHP uses personas as analytical instruments for identifying who benefits, who bears harm, who exercises power, and where an assurance boundary sits. The catalogue now distinguishes **portable role personas** from deployment-specific characters and machine/adversarial actors.

## Persona families

| Namespace | Purpose |
|---|---|
| `Pxx` | Portable roles that recur across protocols and deployments |
| `Mxx` | Machine-agent behaviour profiles |
| `Bxx` | Adversarial actor profiles |
| `Dxx` | Historical DTG/VTC deployment personas |
| `ECxx` | Historical DTG edge-case personas |

The `Pxx` family should be the default starting point when pressure-testing a new specification. A deployment-specific persona should be added only when the local context materially changes goals, harms, power, inclusion, or assurance requirements.

## Portable role personas

### P1 — Principal / Rights-Bearing Party

The human or organization whose rights, assets, authority, consent, or interests are affected. This includes creators, rights holders, represented persons, delegating principals, and consent-giving parties.

### P2 — Producer / Originating Actor

The actor that originates content, metadata, signed assertions, requests, or other evidence. A producer can create authentic evidence without necessarily being authoritative for every property asserted.

### P3 — Relying Party / Verifier

The actor that consumes evidence and makes a trust, policy, routing, authorization, or presentation decision. This role is where cryptographic validity can be incorrectly converted into broader trust.

### P4 — Intermediary / Platform Operator

A publisher, platform, gateway, distributor, transformer, host, or callback service. Intermediaries can preserve, strip, reinterpret, route, or present evidence and therefore form an independent trust boundary.

### P5 — Delegated Service / Agent Operator

The operator of a service or agent acting for another party. This role is especially important for delegated AI and agentic systems because capability, credential possession, and technical reach must not be confused with authority.

### P6 — Registry / Discovery / Trust-Service Operator

The operator of a registry, directory, discovery service, status service, trust list, or related infrastructure. This role can determine discoverability, current status, historical state, and practical ecosystem participation.

## Role personas are not fictional demographic profiles

The original DTG personas intentionally include names, locations, circumstances, and lived-experience context. Those remain useful for analysing inclusion and harms within that deployment.

Portable roles are different. Their purpose is to expose **institutional and technical power relationships** across specifications. They therefore focus on:

- authority boundary;
- evidence produced or consumed;
- decisions made;
- harms borne;
- risks introduced to others;
- lifecycle involvement; and
- accountability obligations.

Demographic details should only be added when they materially change the assurance question.

## Persona analytical-richness contract

Portable does **not** mean skeletal. A portable persona must be rich enough to drive a repeatable harms and assurance analysis without inventing a fictional demographic profile. `method/persona-quality.yaml` defines the executable minimum for each persona family covered by a quality profile.

For `portable_role`, every persona must currently include:

- at least four goals and five material risk contexts;
- an institutional `context` describing operating context, authority position, and dependencies;
- at least three explicit `power_and_decisions` statements;
- at least three `harms_and_externalities` statements, covering harms borne or imposed through the role;
- at least three inclusion drivers and three exclusion risks;
- at least three concrete `pressure_test_situations`;
- at least two meaningful lifecycle stages rather than `Cross-domain` alone; and
- at least one evidence source grounding the represented failure, governance, privacy, security, or assurance pattern.

The JSON Schema continues to define what a valid persona record *can contain*. The quality profile separately defines whether that record is sufficiently developed to serve as a RAHP analytical instrument. This separation keeps the base model extensible while preventing valid-but-anaemic personas from entering the portable corpus.

Run the quality gate directly with:

```bash
python3 tools/validate_persona_quality.py
```

The standard validation and Pages workflows run the same gate in CI.

## Machine actors and institutional roles are complementary

`M1` and `M2` describe benign and malign machine-agent behaviour. They do not replace the accountable institutional role around that machine.

For example, an A2A workflow may involve:

`P1 Principal → P3 Relying/Client Party → M1 Agent → P5 Remote Agent Operator → P5 Downstream Service`

The machine may be technically benign while its operator has excessive authority, weak governance, or incomplete delegation evidence. Keeping both role types visible prevents "the agent did it" from becoming an accountability dead end.

## Applying personas to a pressure test

For each finding:

1. identify the party whose rights or authority are affected;
2. identify who produced the evidence or request;
3. identify who relies on it to make a decision;
4. identify any intermediary that transforms, routes, stores, or presents it;
5. identify delegated operators or services;
6. identify registry, discovery, or status infrastructure;
7. inspect each selected persona's `power_and_decisions` and `harms_and_externalities`;
8. exercise at least one relevant `pressure_test_situations` vector or explain why the finding needs a different situation; and
9. add machine or adversarial personas where their behaviour materially changes the finding.

Do not populate personas mechanically. Include a persona only when that role changes the harm, power relationship, decision, or assurance obligation.

## Worked examples

The C2PA/CAWG worked assessments now use the portable roles to distinguish creators and rights-bearing parties, assertion producers, relying parties, platforms, delegated processors, and trust-service operators.

The A2A assessment additionally combines portable roles with `M1`/`M2` to make the distinction between **machine behaviour** and **institutional authority/accountability** explicit.
