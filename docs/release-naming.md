---
layout: default
title: "Release naming"
nav_order: 12
has_toc: true
parent: Reference
---
# Release naming

Beginning with v1.5.0, RAHP Toolkit releases use a butterfly species name as a human-readable release name in addition to the semantic version and Git tag.

## Naming source

The eligible names are butterfly species listed in the Wikipedia article [List of butterflies of West Bengal](https://en.wikipedia.org/wiki/List_of_butterflies_of_West_Bengal).

The list is used only as a naming source. It has no relationship to RAHP method semantics, conformance, deployment profiles or assurance conclusions.

## Selection rule

For each v1.5.x and later release:

1. select one listed butterfly species at random at release-preparation time;
2. record both the common name and scientific name when both are available;
3. use the common name as the release name unless release preparation documents a reason to use the scientific name;
4. record the source URL and selection date in the release notes; and
5. do not imply that the selected species name identifies a capability level or compatibility class.

A release name is therefore presentation metadata. Semantic versioning, method contracts and schema compatibility remain authoritative.

## Example release metadata

```yaml
release:
  version: 1.5.0
  tag: v1.5.0
  name: <randomly selected common name>
  species: <scientific name>
  naming_source: https://en.wikipedia.org/wiki/List_of_butterflies_of_West_Bengal
  selected_at: <release-preparation date>
```

The name SHOULD be selected only when the release candidate is ready to cut. Development commits and pull requests SHOULD continue to refer to the semantic development target, for example `v1.5.0`, without prematurely assigning the release name.
