# CAWG/C2PA RAHP pressure-test portfolio

RAHP v0.6.0 uses CAWG/C2PA as its first substantial external deployment proof. The eight worked reviews below are intentionally bounded: they identify mandate-readiness and composition risks without claiming upstream governance authority.

| Review | Primary pressure |
|---|---|
| [Identity Assertion](identity/) | identity vs authority; historical validation |
| [Metadata Assertion](metadata/) | integrity vs truth; conflicting authority |
| [Training & Data Mining](training-data-mining/) | signal vs authorization; consent coexistence |
| [Consent Assertion](consent/) | authority, lifecycle, precedence, external state |
| [Endorsement Assertion](endorsement/) | bounded delegation and revocation |
| [Organizational Identity Profile](organizational-identity/) | trust anchors and organizational role lifecycle |
| [UX Guidance](ux-guidance/) | misleading trust inference and accessibility |
| [C2PA Technical Specification](c2pa/) | substrate vs trust decision; downgrade/required evidence |

## Portfolio-level conclusion

The CAWG/C2PA stack is strongest when treated as layered evidence: C2PA provides integrity/provenance machinery; CAWG assertions add identity, metadata, use signals and authorization-like semantics; deployment governance determines which issuers and actors are authoritative for which decisions. The pressure tests therefore recommend against using a single “valid/verified” state as a mandate boundary. Mandate-grade profiles need explicit trust, lifecycle, conflict, accessibility and required-assertion policy.

The instance monitor under `instances/cawg/` tracks upstream repository/branch changes and raises `assessment-required` issues when configured material paths change.
