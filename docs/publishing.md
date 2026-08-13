---
layout: default
title: "Publishing the RAHP site"
nav_order: 90
has_toc: true
---
# Publishing the RAHP site

RAHP documentation is rendered with **Just the Docs** and deployed to **GitHub Pages** by `.github/workflows/pages.yml`.

## Deployment pipeline

```mermaid
flowchart LR
  PUSH[Push to main] --> VALIDATE[Validate RAHP + scenario corpora]
  VALIDATE --> BUILD[Rebuild generated evidence]
  BUILD --> JTD[Build Jekyll / Just the Docs]
  JTD --> ARTIFACT[Upload Pages artifact]
  ARTIFACT --> DEPLOY[Deploy to github-pages environment]
```

The workflow also runs manually with `workflow_dispatch`. Structured YAML/JSON artefacts are rendered by `_plugins/structured_data_pages.rb` at their original Pages paths, while canonical machine-readable source remains in GitHub. See [GitHub Pages coverage](pages-coverage.md).

## One-time repository setting

GitHub requires a Pages publishing source to be enabled for custom Actions workflows. In **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**. After that, pushes to `main` deploy automatically.

The workflow uses GitHub's supported Pages actions (`configure-pages`, `upload-pages-artifact`, and `deploy-pages`) and the `github-pages` deployment environment. No PAT or `gh-pages` branch is required.

## Local validation

```bash
pip install -r requirements.txt
python3 tools/validate.py
python3 tools/validate_scenario_corpora.py
python3 tools/validate_pressure_tests.py
python3 tools/build.py
bundle install
bundle exec jekyll build
```

The generated site is written to `_site/`.
