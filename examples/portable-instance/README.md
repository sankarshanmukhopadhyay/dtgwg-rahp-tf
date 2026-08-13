# Synthetic portable RAHP instance

This is a **test fixture**, not evidence of adoption by another real Working Group.
Its purpose is to prove that the portable RAHP validator can operate against an
independent `data/` root without inheriting DTG records or the repository README.

| Namespace | Meaning | Count |
|---|---|---:|
| `RK` | Risks | 1 |
| `CT` | Controls | 1 |
| `GR` | Guardrails | 1 |
| `AT` | Assurance tests | 1 |
| `M` | Metrics | 1 |

Run:

```bash
python3 tools/validate.py --data examples/portable-instance/data --strict
```

Passing this fixture demonstrates **mechanical instance portability**. It does not
satisfy the v0.5 independent-adoption milestone, which requires a real external
Working Group to own its instance data and governance decisions.
