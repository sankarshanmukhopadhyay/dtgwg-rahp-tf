# Repository map

```mermaid
flowchart TB
  U[Working Group / Spec Author] --> M[method/ · portable lifecycle, vocabularies, schemas]
  U --> D[data/ · canonical RAHP instance]
  M --> T[tools/ · validate and build]
  D --> T
  C[context/ · JSON-LD semantics] --> T
  T --> B[build/ · generated site, JSON/JSON-LD, derived views]
  D --> E[examples/ · applied pressure tests]
  M --> DOC[docs/ · understand and apply]
  D --> DOC
  A[archive/ · historical provenance only] -. not canonical .-> U
```

## Edit contract

- Edit `data/` for DTG facts and findings.
- Edit `method/` only for portable method changes.
- Edit `tools/` to change validation/build behaviour.
- Never hand-edit `build/`.
- Treat `archive/` as read-only provenance.
