# CAWG/C2PA assessment reviews

This directory is the operational review surface for the external CAWG/C2PA RAHP instance.
The v0.6.0 baseline and v0.7.0 expanded worked pressure tests are published under `examples/cawg-c2pa/` so they are
validated and rendered by the existing worked-review toolchain. Change-monitor issues link future
upstream revisions back to this instance and trigger re-review.

The instance is observational. A finding may recommend an upstream specification change, but the
RAHP toolkit does not claim CAWG, DIF, or C2PA governance authority.

## Branch-specific durable records

A repository can contain several independently monitored assurance targets. Durable records therefore use the branch-aware assessment identity emitted by `tools/instance_monitor.py`. A generated issue is closure-eligible only when every durable assessment associated with that issue explicitly marks it eligible for closure. This prevents a disposition on one branch from silently closing unresolved work on another branch.
