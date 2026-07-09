# ADR-0001: XGIC GitLab Architecture, Repository Naming, and Phased CLI Introduction

**Status**: Accepted  
**Date**: 2026-07-02  
**Scope**: Public high-level summary for multi-repository consumers and AI agents

---

## Context

XGIC is building a production-grade orchestration solution for GitLab Enterprise Edition. Development concerns (VS Code dev containers, build pipelines, image optimization) must be cleanly separated from the end-user experience (simple configuration, GitHub Template usage, minimal cognitive load).

Simultaneously, XGIC is evolving toward a unified `xgic` CLI framework. Publishing high-quality, versioned Python packages takes time and must not block delivery of a working GitLab orchestrator.

This ADR records the key architectural decisions for Phase 1 delivery and a sustainable foundation for Phase 2 and future XGIC open-source projects.

---

## Decision 1: Use Official, Unaltered Docker Images Only

**Decision**: All service containers (GitLab EE, PostgreSQL, Redis) **must** use the official, unaltered images published by their respective vendors (`gitlab/gitlab-ee`, `postgres`, `redis`).

**Rationale**:
- Lower support and security-patching burden versus custom images.
- Cleaner licensing posture for the orchestration layer.
- Straightforward upgrade paths using vendor tooling.
- Alignment with vendor-tested “golden” configurations.

**Consequences**:
- Orchestrator images focus on orchestration (Compose or future platforms), not forking vendor images.
- Future Kubernetes / cloud modules consume the same official images.

---

## Decision 2: Two-Repository Model (`-dev` + Template)

**Decision**:
- Repositories whose primary purpose is a **VS Code development container and build system** that produces optimized GHCR/Docker Hub images **must** use the `-dev` suffix (e.g. `xgic/gitlab-dev`).
- A separate, clean **reference / template repository** (e.g. `xgic/gitlab`) consumes the produced image and serves as the GitHub Template for end users.

**Rationale**:
- Separation of contributor tooling from end-user configuration experience.
- Professional, approachable template repos for “Use this template”.
- Consistent pattern across XGIC OSS projects.

**Consequences**:
- `*-dev` repos hold dev containers, build pipelines, and image production.
- Clean template repos reference GHCR images and provide schema/examples.
- Future XGIC OSS image-producer repos follow the same naming.

---

## Decision 3: Phased Introduction of the XGIC CLI

**Decision**:
- **Phase 1**: Deliver working orchestrator image and essential operations (e.g. backup-oriented workflows) **without** requiring the full unified XGIC CLI package set.
- **Phase 2**: Introduce the modular `xgic` CLI (core + domain modules) after Python packages are published to GitHub and/or PyPI.

**Rationale**:
- Speed to value for operational needs without blocking on full packaging.
- Lower risk surface during repository restructure and first GHCR releases.
- GraphQL client and related libraries stabilize first as foundations for CLI modules.

**Consequences**:
- Phase 1 may use focused entry points inside orchestrator images.
- Phase 2 adopts namespaces such as `xgic.cli.*` and related libraries per the public namespace convention (see `docs/xgic-python-namespace-convention.md` in this repository).

---

## Decision 4: Object-Oriented Python + Modern Standards

**Decision**:
All new or refactored XGIC Python core logic uses **object-oriented design** (Pydantic models, service classes, clear separation of concerns). New development targets **Python 3.14** (see ADR-0002).

**Rationale**:
- Maintainability, testability, and long-horizon consistency.
- Alignment with modern typing and packaging practices.

**Consequences**:
- OO style for CLI modules and libraries; minimal-dependency preference where practical.

---

## Decision 5: Configuration Experience (JSON Schema Primary + Optional Textual)

**Decision**:
Primary configuration is **schema-validated JSON** (Pydantic-generated schemas for editor IntelliSense). Optional Textual-based guided setup may be provided.

**Rationale**:
- Power users edit JSON with validation and autocompletion.
- Guided UI lowers barrier for less JSON-centric users.

---

## Summary Principles

1. Official vendor images only for application services.
2. `-dev` vs clean template repository naming.
3. Phased CLI: operational value first, full modular CLI after packaging maturity.
4. OO Python + Python 3.14 for new work (ADR-0002).
5. JSON schema configuration primary; optional guided UI.

## References

- [ADR-0002: Standardize New Python Development on Python 3.14](./0002-standardize-on-python-3-14.md)
- [XGIC Python Namespace Convention (public summary)](../xgic-python-namespace-convention.md)
- Official GitLab EE, PostgreSQL, and Redis container documentation
