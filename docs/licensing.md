# Licensing — Apache 2.0

## Policy

**All XGIC public solutions** (source repositories, documentation hubs, published packages, and related public artifacts under `github.com/xgic`) use the **Apache License, Version 2.0**, unless a specific public repository documents a deliberate exception (rare; requires an ADR).

This repository (`xgic/ai`) is licensed under Apache 2.0. See [LICENSE](../LICENSE) and [NOTICE](../NOTICE).

## Why Apache 2.0

- Explicit patent grant suitable for enterprise and client adoption
- Clear contribution terms for multi-repo ecosystems
- Compatible with common open-source dependency graphs
- Professional default for libraries, CLIs, images’ accompanying source, and documentation

## Agent rules

When creating or advising on new **public** XGIC repositories:

1. Include `LICENSE` (Apache-2.0 text) and a short `NOTICE` when redistribution notices apply.
2. Set package metadata / SPDX identifiers to `Apache-2.0` where tooling supports it.
3. Do not mix in copyleft assumptions without an explicit human-approved ADR.
4. Third-party dependencies retain their own licenses; document them in the consuming repo as usual.

## Related ADR

- [ADR-0004: Apache 2.0 for XGIC public solutions](adr/0004-apache-2-0-for-public-solutions.md)
