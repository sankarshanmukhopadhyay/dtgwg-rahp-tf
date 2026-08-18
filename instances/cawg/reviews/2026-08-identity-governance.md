---
title: "CAWG review: Identity Assertion governance experiment"
layout: default
nav_exclude: true
---

# CAWG review: Identity Assertion governance experiment

**Assessment ID:** `CAWG-AR-2026-002`  
**Assessment key:** `cawg:repository:decentralized-identity/cawg-identity-assertion@governance`  
**Target:** `governance`  
**Status:** dispositioned  
**Disposition:** no-material-assurance-impact  
**Reviewed revision:** `5a2795bd752da9e60ef04536ec6eb44167c929eb`

The change from `5f1908d4f5bf6c89d02d671ae5051f893df92dc9` adds exploratory notes for a
TRQP-based trust-registry validation path. The changed text contains explicit `TO DO` markers,
including an unresolved `context` vocabulary, validation procedure, caching guidance and
possible stapling behaviour.

These notes are assurance-relevant because they could eventually introduce a new external
authority-resolution dependency, but they are not yet a stable normative contract.

## Watch conditions

Before this experiment can be treated as assurance-closed, a future review must establish:

- what proposition a successful TRQP response proves and what it does not prove;
- authority and recognition scope, context and temporal semantics;
- freshness/cache requirements and status withdrawal behaviour;
- provenance/evidence retained for later audit;
- failure/downgrade behaviour when the trust registry is unavailable; and
- whether stapled responses preserve current authority and anti-replay properties.

**Disposition:** no blocking finding against the experiment because the text is deliberately
unfinished. Keep it under the branch-specific assessment identity and reassess when the TODOs
become normative requirements.

Source: <https://github.com/decentralized-identity/cawg-identity-assertion/commit/5a2795bd752da9e60ef04536ec6eb44167c929eb>
