---
layout: default
title: "Assessment claims"
nav_order: 4
has_toc: true
parent: Adopt RAHP
---
# Claiming an assessment used RAHP

RAHP v0.5 introduced a portable template for the statement; v0.8 retains it as a method claim rather than an implementation-language claim:

> **This specification or system was assessed using RAHP.**

That is intentionally narrower than saying a target *conforms to RAHP*.

The template is [`method/conformance-claim-template.yaml`](../method/conformance-claim-template.yaml).

A useful claim pins the RAHP method version and commit, the adopter instance, the
target commit, assessment modes, corpora, canonical findings, evidence manifest,
governance authority, accepted risks and unresolved actions.

This gives another Working Group a reproducible way to report **how an assessment
was performed** without inheriting DTG-specific normative content or implying that
RAHP itself certifies the target.
