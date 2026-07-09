# ADR-0002: Standardize New Python Development on Python 3.14

**Status**: Accepted  
**Date**: 2026-07-02  
**Scope**: Public high-level summary for multi-repository consumers and AI agents

---

## Context

To maximize long-term productivity, consistency, and maintainability across Python work, XGIC standardizes new development on the current latest stable Python release, **3.14**.

Python 3.14 delivers meaningful advancements, including:
- Template string literals (t-strings) for safer composable interpolation (PEP 750).
- Deferred evaluation of annotations and `annotationlib` (PEPs 649/749).
- Multiple interpreters support in the standard library (PEP 734).
- Continued free-threading and JIT-related improvements (PEPs 703/744).
- Standard-library zstd and pathlib enhancements, plus many performance and DX improvements.

For projects that prefer minimal third-party dependencies, a richer stdlib and modern language features reduce technical debt.

---

## Decision

All **new** Python programming at XGIC—including open-source libraries, CLIs, and client-facing solutions—shall standardize on **Python 3.14**.

Specifically:
- New projects declare `requires-python = ">=3.14"` in `pyproject.toml` (or a pinned patch at inception when required).
- Containerized environments use the official image **`python:3.14.6-slim`** (or the current latest patch in the 3.14 series, pinned for reproducibility).
- Supporting environment orchestration prefers the **XGIC CLI standard** (no new Makefiles in new or modernized repos).

**Existing projects** remain unaffected unless explicitly migrated under separate review.

---

## Consequences

**Positive**:
- Consistent runtime behavior across new projects and environments.
- Access to modern language and stdlib capabilities with less boilerplate.
- Clear alignment with OO design and typing-friendly codebases.
- Easier agentic and human development against a single baseline.

**Risks and mitigations**:
- Dependency compatibility checks for third-party packages (prefer minimal deps; ecosystem support for current Python is strong).
- Pin and review patch-level container tags as part of normal security/update processes.

---

## Implementation guidance (public)

- Update `pyproject.toml` classifiers and tool configs (ruff/pyright/mypy target versions) for 3.14.
- Prefer official slim images for CI and production-like containers.
- Document the version baseline in each project’s README and AGENTS.md (public-safe wording only).

## References

- Official “What’s New in Python 3.14” documentation and related PEPs (649, 749, 734, 750, 703, 744, and others as applicable).
- Docker Official Images for the `python` family (`3.14.6-slim` / `3.14-slim`).
- [ADR-0001: GitLab architecture and repository naming](./0001-xgic-gitlab-architecture-and-repository-naming.md)
- [XGIC Python Namespace Convention (public summary)](../xgic-python-namespace-convention.md)
