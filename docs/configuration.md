---
layout: default
title: "Configuration-driven adoption"
nav_order: 3
has_toc: true
---
# Configuration-driven adoption

RAHP uses a YAML file as the boundary between the portable engine contract and a deployment. The independent DTG and CAWG/C2PA deployments prove this configuration boundary, while v0.8 makes the execution/result contract language-neutral. An adopter does **not** need to copy the DTG instance, import DTG issues, use DTG corpora, or connect to the DTG Portfolio Monitor.

## Minimal configuration

```yaml
version: 1
profile:
  id: my-wg
  title: My Working Group
assessment:
  default_mode: combined
repositories:
  - id: my-spec
    repository: my-org/my-spec
    branch: main
    context:
      title: My Specification
      type: specification
    scope:
      include: ["spec/**", "schemas/**", "docs/**"]
    reviews: [rahp, security, combined]
```

Validate and inspect it:

```bash
python3 tools/rahp.py config-validate --config rahp.yaml
python3 tools/rahp.py targets --config rahp.yaml
```

Scaffold a selected review:

```bash
python3 tools/rahp.py review --config rahp.yaml --target my-spec --mode rahp
python3 tools/rahp.py review --config rahp.yaml --target my-spec --mode security
python3 tools/rahp.py review --config rahp.yaml --target my-spec --mode combined
```

Or use the profile default across every configured repository:

```bash
python3 tools/rahp.py review --config rahp.yaml --all
```

A review must resolve a full commit SHA for provenance. Pin `commit`, point `local_path` at a Git checkout, or allow the CLI to resolve the configured branch online. `prepare` can also checkout configured remote targets under `build/targets/`:

```bash
python3 tools/rahp.py prepare --config rahp.yaml --all
```

## Configuration model

| Field | Purpose |
|---|---|
| `profile` | Names the adopter/deployment; it does not alter RAHP semantics. |
| `assessment.default_mode` | Chooses `rahp`, `security`, or `combined` when a command does not override it. |
| `repositories[]` | Declares target repositories. One profile may contain one or many. |
| `context` | Supplies human-readable purpose, type, ownership, and other adopter-defined context. |
| `scope.include/exclude` | Documents which target paths are in or out of assessment scope. |
| `reviews` | Restricts which review modes are allowed for a target. |
| `extensions` | Carries deployment-specific integrations without making them core dependencies. |

The canonical schema is [`method/schema/rahp-config.schema.json`](../method/schema/rahp-config.schema.json).

## DTG is an exemplar

[`profiles/dtg/rahp.yaml`](../profiles/dtg/rahp.yaml) demonstrates the engine across DTG ZKP, Credential Specification, and Trust Tasks repositories. Its `extensions.portfolio_registry` entry is explicitly optional. The DTG corpora, canonical `data/`, Task Force actions, `RP-001`, and other governance records remain useful evidence for that deployment, but a different Working Group does not load or run them merely to use RAHP.

## What the engine does not do

Configuration makes target resolution and workflow orchestration portable; it does not automate judgement. RAHP can resolve revisions, prepare repositories, scaffold review records, validate records, and render evidence. A human or AI-assisted reviewer remains responsible for examining target material, determining whether a finding is defensible, recording evidence, and proposing disposition.


## Review retention

v0.8 supports optional deployment retention settings under `assessment.retention`:

```yaml
assessment:
  default_mode: combined
  retention:
    workspace_directory: .rahp
    ephemeral_days: 14
    referenced_days: 365
    allow_sensitive_git_evidence: false
```

These values refine the portable defaults in `method/evidence-retention.yaml`. Working review scaffolds are not durable evidence simply because they exist; use [Review evidence and retention](evidence-retention.md) to decide what is promoted or referenced.
