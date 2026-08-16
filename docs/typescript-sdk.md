---
layout: default
title: "TypeScript Reference SDK"
nav_order: 2
parent: Implement RAHP
---
# TypeScript Reference SDK

RAHP v1.0 includes a second reference implementation of the v0.8 engine boundary. The TypeScript SDK is intentionally **an implementation of `rahp-engine-contract-v1`, not a second normative definition of RAHP**. Method YAML, schemas, retention rules and shared conformance fixtures remain authoritative.

## Packages

| Package | Responsibility |
|---|---|
| `@rahp/schema` | TypeScript result types and normalized-result validation |
| `@rahp/core` | Profile loading, result loading, retention planning and evidence hashing |
| `@rahp/graph` | Catalogue graph projection and relationship traversal |
| `@rahp/cli` | Command-line access to the reference SDK |

The runtime packages have no third-party dependencies. TypeScript is required only to build the source distribution.

## Build and test

```bash
npm install
npm run build:ts
npm run test:ts
python3 tools/validate_typescript_sdk.py
```

`validate_typescript_sdk.py` is the cross-implementation gate. It verifies that Python and TypeScript agree on every shared engine fixture and on the retention plan for valid results, then checks the portable profile and graph projection.

## CLI

```bash
node packages/cli/dist/cli.js describe
node packages/cli/dist/cli.js validate-profile profiles/dtg/rahp.yaml
node packages/cli/dist/cli.js targets profiles/dtg/rahp.yaml
node packages/cli/dist/cli.js validate-result instances/dtg/reviews/<assessment>.result.json
node packages/cli/dist/cli.js retention-plan <result.json>
node packages/cli/dist/cli.js graph-stats build/rahp.json
node packages/cli/dist/cli.js trace RK-AI01 build/rahp.json 2
node packages/cli/dist/cli.js conformance
```

## What the TypeScript implementation proves

The v1 release preserves the v0.9 proof that normalized result validation, evidence-retention decisions, profile enumeration and catalogue traversal can be implemented independently of Python while preserving the same portable contract.

It does **not** make TypeScript normative, retire the Python operational tooling, or require existing Actions workflows to execute assessments in TypeScript. Operational source observation and GitHub issue publication remain Python-backed in v1.0 while the portable engine boundary is exercised by both implementations.

## v1.0 direction

v1.0 should strengthen the shared fixture suite until the two implementations cover the complete portable assessment lifecycle and then stabilize the contract/versioning rules. Rust/WASM remains out of scope until an actual embedding, static-binary or performance requirement emerges.
