---
layout: default
title: "Scenario corpora browser"
nav_order: 6
parent: "Scenario corpora"
has_toc: true
---
# Scenario corpora browser

These are the currently packaged scenario adapters. Each **Browse** link opens a themed, human-readable projection; each **YAML** link preserves the canonical machine-readable source.

| Corpus | Browse | Canonical YAML |
|---|---|---|
| DTG ZKP | [Rendered corpus](dtg-zkp/) | [YAML](dtg-zkp.yaml) |
| Trust Tasks | [Rendered corpus](trust-tasks/) | [YAML](trust-tasks.yaml) |
| DTG Credential Spec | [Rendered corpus](credential-spec/) | [YAML](credential-spec.yaml) |
| Trust Tasks × CredSpec | [Rendered composed corpus](trust-tasks-credspec-composed/) | [YAML](trust-tasks-credspec-composed.yaml) |
| CAWG/C2PA | [Rendered corpus](cawg/) | [YAML](cawg.yaml) |

The clean rendered routes are deliberate. Files ending in `.yaml` remain machine-readable and should not be replaced with HTML, because browsers and static hosts may serve them with a YAML/text MIME type. GitHub Pages therefore exposes the reader view on a sibling directory route such as `/corpora/dtg-zkp/`.

For ownership, adaptation rules, and scenario semantics, return to [Scenario corpora](../docs/scenario-corpora.md). For source drift, immutable pins, the DTG portfolio registry relationship, and review workflows, see [Corpus synchronization and provenance](../docs/corpus-synchronization.md).
