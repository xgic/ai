# XGIC Python Namespace Convention (Public Summary)

## Audience

High-level orientation for public consumers and AI agents. Internal-only registry details are intentionally omitted; this file is the **public** registry summary cited by other XGIC repositories.

## Purpose

This document defines the Python namespace convention for XGIC libraries and CLIs so components integrate without import conflicts and remain easy to discover.

## Python Libraries and CLIs (summary)

| Name | Type | Namespace | GitHub | Priority | Dependencies | Status (high-level) |
|------|------|-----------|--------|----------|--------------|---------------------|
| GitLab GraphQL Client | Library | `xgic.gitlab.graphql` | [xgic/gitlab-graphql](https://github.com/xgic/gitlab-graphql) | 1 | — | Available — GraphQL client for Work Items, hierarchy, auth, pagination |
| Core CLI | CLI / framework | `xgic.cli` | [xgic/cli](https://github.com/xgic/cli) | 2 | — | Available — thin core (framework, env detect, output); entrypoint `xgic` |
| Dev Container CLI | CLI module | `xgic.cli.dev` | [xgic/dev-cli](https://github.com/xgic/dev-cli) | 2 | Core CLI | Available — Docker Compose lifecycle + library (`xgic up`/`down`/`check`/…) |
| GitLab CLI | CLI module | `xgic.cli.gitlab` | [xgic/gitlab-cli](https://github.com/xgic/gitlab-cli) | 2 | Core CLI, GraphQL client | Planned — backup/restore and GitLab ops |
| AIS CLI | CLI module | `xgic.cli.ais` | [xgic/ais-cli](https://github.com/xgic/ais-cli) | 3 | Core CLI | Planned — automation-oriented AIS features (public surface only) |
| Payload CMS CLI | CLI module | `xgic.cli.payload` | [xgic/payload-cms-cli](https://github.com/xgic/payload-cms-cli) | 4 | Core CLI, Dev CLI | Available — project ensure/create helpers (subcommands later; transitional **`xde`** until cutover) |

### Naming note (xde → XGIC CLI)

| Phase | Living docs | In-repo names |
|-------|-------------|---------------|
| **Pre-cutover** | May introduce the tool as **`xde` (current CLI; successor brand: XGIC CLI)**; use **`xde`** for real commands/packages | `xde` remains |
| **Post-cutover** | Living docs and guidelines use **only XGIC CLI** / `xgic.cli.*`. **No `xde`** except minimal historical notes in completed artifacts | Code and packages use XGIC CLI only—**no** `xde` compatibility alias |

See the [ecosystem catalog](ecosystem/catalog.md) section **XGIC CLI and modules**.

## Namespace rules

1. Top-level package root is **`xgic`**.
2. Libraries use domain paths (e.g. `xgic.gitlab.graphql`).
3. CLI modules live under **`xgic.cli.*`**.
4. Prefer small, importable libraries over ad-hoc scripts.
5. New modules register here (public summary) when the corresponding public repository is announced or published.

## Publishing to PyPI

Public distributions under this registry **must** follow the hub release standard:

**[python-package-release.md](python-package-release.md)** — RC on TestPyPI with clean-env smoke, final on PyPI via OIDC Trusted Publishing (`pypa/gh-action-pypi-publish`), `uv` for build and install verification, dependency-order publish for modular stacks.

## Related ADRs

- [ADR-0001: GitLab architecture and repository naming](adr/0001-xgic-gitlab-architecture-and-repository-naming.md)
- [ADR-0002: Standardize on Python 3.14](adr/0002-standardize-on-python-3-14.md)

## Registration process (public)

1. Define namespace and planned public GitHub repository name.
2. Implement against Python 3.14 baseline (ADR-0002) and OO design norms.
3. License as Apache-2.0 (ADR-0004); set package SPDX/metadata accordingly.
4. Add or update rows in this document **and** [ecosystem/catalog.md](ecosystem/catalog.md).
5. Do not embed private coordination IDs or private repository paths in public documentation.
6. When publishing to PyPI, follow **[python-package-release.md](python-package-release.md)** (TestPyPI RC + smoke, then PyPI via OIDC Trusted Publishing; `uv` build/smoke).

## Publishing to PyPI

Public distributions under this registry **must** use the hub release standard:

**[python-package-release.md](python-package-release.md)** — clean-env install matrix; RC on TestPyPI with smoke; final on PyPI via OIDC Trusted Publishing (`pypa/gh-action-pypi-publish`); `uv` for build and install verification; dependency-order publish for modular stacks.
