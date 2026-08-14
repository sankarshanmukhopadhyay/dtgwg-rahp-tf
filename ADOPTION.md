---
layout: default
title: "Adopting RAHP"
nav_order: 20
has_toc: true
---
# Adopting RAHP

RAHP is adopted through configuration. A Working Group, developer, standards project, assurance team, or independent reviewer can use the toolkit without inheriting either bundled deployment. DTG and CAWG/C2PA are examples of the same portable contract, not parent environments that a new adopter must copy.

## 1. Checkout and install

```bash
git clone <rahp-repository>
cd rahp-toolkit
pip install -r requirements.txt
```

## 2. Create `rahp.yaml`

Start from `examples/configurations/minimal.yaml` and replace the target metadata with your own repository or repositories.

```yaml
version: 1
profile:
  id: my-project
  title: My Project
assessment:
  default_mode: combined
repositories:
  - id: specification
    repository: my-org/my-spec
    branch: main
    context:
      title: My Specification
    scope:
      include: ["spec/**", "docs/**"]
    reviews: [rahp, security, combined]
```

## 3. Validate and inspect targets

```bash
python3 tools/rahp.py config-validate --config rahp.yaml
python3 tools/rahp.py targets --config rahp.yaml
```

## 4. Prepare source material

Either pin a full `commit`, provide a Git `local_path`, or let RAHP resolve the configured remote branch. To checkout configured remotes:

```bash
python3 tools/rahp.py prepare --config rahp.yaml --all
```

## 5. Select a review lens

```bash
python3 tools/rahp.py review --config rahp.yaml --target specification --mode rahp
python3 tools/rahp.py review --config rahp.yaml --target specification --mode security
python3 tools/rahp.py review --config rahp.yaml --target specification --mode combined
```

The CLI scaffolds canonical review records with repository and commit provenance. It does not infer findings. Inspect the target, populate evidence-backed findings, then use the existing renderers and validators described in `docs/review-modes.md`.

## What you do not inherit

A new deployment does not inherit another deployment's governance or assessment state. You do not need the DTG Portfolio Monitor, DTG scenario corpora, DTG governance queue, `RP-001`, canonical DTG `data/` records, CAWG `CRK-*` risks, or CAWG/C2PA monitoring state. Adopt only the method and capabilities your deployment needs.

This separation is a core v0.6 invariant: **shared engine, independent deployment context**.

## Optional richer use

Once a project needs recurring scenarios, governed risk/control catalogues, evidence contracts, or source-drift monitoring, it can adopt those RAHP capabilities deliberately. They are not prerequisites for the first configured assessment.

See `docs/configuration.md` for the complete configuration model and `docs/portability.md` for the portability contract demonstrated by the independent DTG and CAWG/C2PA deployments.
