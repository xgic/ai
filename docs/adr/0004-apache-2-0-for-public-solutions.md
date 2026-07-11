# ADR-0004: Apache License 2.0 for XGIC public solutions

**Status**: Accepted  
**Date**: 2026-07-11  
**Scope**: All public XGIC GitHub solutions and this hub unless an ADR carves out an exception

---

## Context

XGIC public repositories must share a clear, enterprise-friendly open-source license so clients, contributors, and AI agents do not guess terms per repository. Documentation hubs, libraries, CLIs, and application samples should align.

---

## Decision

1. **Apache License, Version 2.0** is the default license for XGIC public solutions under `github.com/xgic`.  
2. Repositories include a root `LICENSE` file with the Apache-2.0 text and a `NOTICE` file when required for attribution.  
3. Package metadata (e.g. PyPI classifiers / SPDX `Apache-2.0`) matches the repository license.  
4. Exceptions require a documented ADR and explicit README notice.  
5. Third-party dependencies retain their own licenses; consumers document them in the usual way.

---

## Consequences

**Positive**

- Predictable legal posture for adoption  
- Patent grant clarity relative to many permissive licenses  
- Simpler agent and template defaults  

**Trade-offs**

- Contributors must follow Apache-2.0 contribution terms  
- Mixing strong copyleft dependencies needs careful review  

---

## References

- [licensing.md](../licensing.md)
- [LICENSE](../../LICENSE)
- [NOTICE](../../NOTICE)
- https://www.apache.org/licenses/LICENSE-2.0
