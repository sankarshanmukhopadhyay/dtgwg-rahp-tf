---
layout: default
title: "v1.1 HEAD qualification"
parent: Deployments & examples
nav_order: 8
has_toc: true
---
# v1.1.0 HEAD qualification

On **2026-08-17**, the maintained v1.1.0 example estate was re-qualified against the current default-branch HEAD of every live repository represented by the examples. This is a **longitudinal assurance run**: the original examples remain pinned to the revision they actually reviewed, while this run records whether current HEAD changes the findings.

## Outcome

| Target | Pinned canonical baseline | HEAD | Delta | Qualification |
|---|---|---|---:|---|
| A2A | `1eb4aa0` | `134a382` | +1 | Non-material; assessed source paths unchanged |
| C2PA Specifications | `b1703dc` | `b1703dc` | 0 | Current |
| CAWG Consent | `0d6916c` | `0d6916c` | 0 | Current |
| CAWG Endorsement | `585c7fb` | `585c7fb` | 0 | Current |
| CAWG Identity | `8a9c492` | `8a9c492` | 0 | Current canonical WG-approved baseline |
| CAWG Metadata | `64069e0` | `64069e0` | 0 | Current |
| CAWG Organizational Identity | `c862069` | `c862069` | 0 | Current ratified baseline |
| CAWG Training/Data Mining | `e203ac5` | `e203ac5` | 0 | Current |
| CAWG UX Guidance | `3162bbb` | `3162bbb` | 0 | Current |
| DTG Credential Spec | `d19f7c9` | `b89f389` | +1 | Material positive change |
| DTG Trust Tasks | `fbe196a` | `7e0d755` | +27 | Material positive change |

The table contains eleven live repositories; CAWG Identity and Organizational Identity additionally have deliberately pinned experimental/draft variants. Those variants are retained as variant evidence and are not rewritten as default-branch HEAD assessments.

## A2A

A2A advanced by one commit, changing only `docs/index.md` to repair broken links. None of the source paths cited by the RAHP assessment changed. All six findings therefore remain **unchanged**.

## Credential Specification

The Credential Specification changed only `spec/body.md`. The VWC `credentialSubject.digest` is now **REQUIRED**, with normative SHA-256/JCS computation and an explicit statement that the digest binds the VWC to the exact VRC/edge being witnessed.

This **resolves `SEC-CR-009`**, which specifically identified the optional digest as allowing witness assertions not bound to an exact VRC. The change also strengthens the cross-spec outcome-evidence story, but does not by itself resolve the broader distinction between credential validity and Trust Task completion.

## Trust Tasks

Trust Tasks moved 27 commits and is the most important result of this run. Current HEAD now includes:

- normative duplicate-execution protection for consequential tasks (`§7.2` item 11);
- a bounded executable acceptance/freshness window tied to duplicate-record retention;
- explicit separation of identity/proof validation from authorization (`§7.2` item 10);
- required declaration of authorization evidence for consequential task specifications (`§7.3` item 15);
- re-evaluation of authority, delegation, credential/key status and other required conditions immediately before irreversible effects (`§7.2` item 12);
- producer-driven `cancel`, `suspend` and `resume` task control, tied explicitly to the item-12 checkpoint;
- binding-level requirements that must justify any allowance to omit document proof;
- task digests for externally relied-upon citations; and
- explicit payload validation policy in the reference libraries, with self-contained schemas.

As a result, the original Trust Tasks RAHP findings for duplicate execution, unbounded freshness and identity-as-authority are **resolved as written**. Several security findings are also resolved or weakened. Mutable drafts, registry availability, full secure-profile discovery, human-approval floors, supported decision-making, prompt flooding, ceremony-receipt correlation and resource-limit risks remain open.

## Cross-specification result

The Trust Tasks × Credential Specification composition was reassessed because both constituents changed. The main movement is positive:

- exact Trust Task replay no longer repeats a consequential effect;
- authority must be evaluated independently of authentication and re-evaluated before irreversible effects;
- task digests and ceremony receipts provide stronger external completion/citation evidence; and
- the Credential Specification now requires the VWC digest that binds witness evidence to the exact VRC.

The composition still has residual risks around delegated-authority portability, durable correlation, later/offline lifecycle state, ZKP/outcome evidence composition, registry query/failure semantics, supported decision-making and accountable human/control relationships.

## Portable catalogue qualification

No new `HRM-*`, `RKP-*`, `CTP-*`, `GRP-*`, `ATP-*` or `EVP-*` pattern was required to express the material HEAD changes. This is useful evidence for the v1.1 model itself: the portable catalogue covered the live evolution encountered in A2A and the two DTG specifications without requiring an emergency vocabulary extension.

## Machine-readable evidence

The complete target inventory and per-finding classifications are committed in [`examples/head-qualification/qualification.yaml`](../examples/head-qualification/qualification.yaml). Run:

```bash
python3 tools/validate_head_qualification.py
```

to verify that the qualification references real curated findings and uses valid commit identifiers/classifications.
