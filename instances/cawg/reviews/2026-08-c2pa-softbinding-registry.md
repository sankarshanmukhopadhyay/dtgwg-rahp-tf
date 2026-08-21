---
title: "CAWG/C2PA review: softbinding algorithm registry update"
parent: CAWG RAHP review record
nav_order: 30
layout: default
nav_exclude: true
---

# CAWG/C2PA review: softbinding algorithm registry update

**Assessment ID:** `CAWG-AR-2026-003`  
**Assessment key:** `cawg:repository:c2pa-org/specifications`  
**Mode:** RAHP + security triage  
**Status:** dispositioned  
**Disposition:** no-material-assurance-impact  
**Reviewed revision:** `9c58c8c27044e44e8601f6ab13f1bcac1376eb1f`

## Scope

This review covers the single-commit change window
`7e3a99c25ffbe6a81ff66faab03c237c00ccc321` →
`9c58c8c27044e44e8601f6ab13f1bcac1376eb1f` and dispositions RAHP toolkit
issue **#28**.

The only material file changed is
`supplemental-ui/softbinding-alg-list/softbinding-algorithm-list.json`.

## Change assessment

The revision adds four registered soft-binding algorithm entries:

- `me.reconize.videoseal.1` — image/video watermark;
- `io.diker.sigi.v1` — image watermark;
- `com.adobe.hiermark.A` — audio watermark; and
- `com.adobe.flowmark.A` — video watermark.

It also normalises JSON punctuation around the preceding entry.

The change does **not** modify C2PA manifest semantics, signature validation,
trust-list processing, claim generation, assertion verification, revocation,
identity binding, or CAWG identity-governance requirements. It expands a
supplemental registry of soft-binding mechanisms that implementations may
recognise.

## Assurance boundary

Registry presence is **not** treated as proof that an algorithm is secure,
robust, interoperable, privacy-preserving or suitable for a particular relying
context. The entry establishes an identifier and descriptive metadata; algorithm
security and deployment assurance remain properties of the registered mechanism
and the relying implementation/profile.

Accordingly:

- no new authority or delegation surface is introduced;
- no existing RAHP control is weakened;
- no CAWG identity-assurance claim should inherit trust merely from registry
  membership; and
- a future change that makes a registered soft-binding algorithm normative or
  required by a conformance profile must trigger a new review.

## Assurance disposition

**No material assurance impact.** The delta is additive registry metadata and
does not alter the security or governance semantics currently assessed by the
CAWG/C2PA RAHP instance.

This record closes RAHP toolkit issue **#28** for revision
`9c58c8c27044e44e8601f6ab13f1bcac1376eb1f`.

## Sources

- <https://github.com/c2pa-org/specifications/commit/9c58c8c27044e44e8601f6ab13f1bcac1376eb1f>
- <https://github.com/c2pa-org/specifications/blob/9c58c8c27044e44e8601f6ab13f1bcac1376eb1f/supplemental-ui/softbinding-alg-list/softbinding-algorithm-list.json>
