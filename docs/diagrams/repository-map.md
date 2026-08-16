# Repository map

```mermaid
flowchart TB
  U[Adopter / Standards WG / Reviewer] --> P[profiles/<id>/ · target configuration]
  M[method/ · portable lifecycle, vocabularies, schemas] --> T[tools/ · orchestration, validation, monitoring, build]
  P --> T
  I[instances/<id>/ · deployment state, reviews, optional local vocabulary] --> T
  D[data/ · bundled DTG exemplar catalogue] --> T
  C[corpora/ · optional scenario adapters] --> T
  X[context/ · JSON-LD semantics] --> T
  T --> W[.rahp/ · ignored run workspace]
  T --> B[build/ · reproducible generated projections]
  T --> E[examples/ · deliberately promoted worked assessments]
  M --> DOC[docs/ · portable guidance and deployment documentation]
  P --> DOC
  I --> DOC
  A[archive/ · historical provenance only] -. not current authority .-> DOC
```

## Authority boundaries

- Edit `method/` only when changing **portable RAHP semantics**.
- Edit `profiles/<id>/` when changing a deployment's configured target repositories, branches, scope or allowed review modes.
- Edit `instances/<id>/` for deployment-owned state, reviews and local assurance vocabulary.
- Root `data/` is the **bundled DTG exemplar catalogue retained for compatibility**; it is not the universal RAHP data model that every adopter must inherit.
- `corpora/` contains optional domain adapters. A deployment may use none, some, or its own.
- Treat `.rahp/` as disposable run-local workspace; do not commit it.
- Never hand-edit reproducible files under `build/`.
- Promote material into `examples/` only when it is intentionally maintained as an exemplar.
- Treat `archive/` as historical provenance, not current RAHP authority.

The v0.8 architecture is therefore **one language-neutral method/engine contract, many conforming implementations and independently governed deployments**, with Git retaining assurance state rather than run exhaust.
