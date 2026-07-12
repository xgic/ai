# XGIC Python Namespace Convention (Public Summary)

## Audience

High-level orientation for public consumers and AI agents. Internal-only registry details are intentionally omitted; this file is the **public** registry summary cited by other XGIC repositories.

## Purpose

This document defines the Python namespace convention for XGIC libraries and CLIs so components integrate without import conflicts and remain easy to discover.

## Planned Python Libraries and CLIs (summary)

| Name | Type | Namespace | Planned GitHub | Priority | Dependencies | Status (high-level) |
|------|------|-----------|----------------|----------|--------------|---------------------|
| GitLab GraphQL Client | Library | `xgic.gitlab.graphql` | [xgic/gitlab-graphql](https://github.com/xgic/gitlab-graphql) | 1 | — | GraphQL client for Work Items, hierarchy, auth, pagination |
| Core CLI | CLI / framework | `xgic.cli` | [xgic/cli](https://github.com/xgic/cli) | 2 | — | Base framework for modular CLI |
| Dev Container CLI | CLI module | `xgic.cli.dev` | [xgic/dev-cli](https://github.com/xgic/dev-cli) | 2 | Core CLI | VS Code dev-container orchestration helpers |
| GitLab CLI | CLI module | `xgic.cli.gitlab` | [xgic/gitlab-cli](https://github.com/xgic/gitlab-cli) | 2 | Core CLI, GraphQL client | Backup/restore and GitLab ops |
| AIS CLI | CLI module | `xgic.cli.ais` | [xgic/ais-cli](https://github.com/xgic/ais-cli) | 3 | Core CLI | Automation-oriented AIS features (public surface only) |
| Payload CMS CLI | CLI module | `xgic.cli.payload` | [xgic/payload-cms-cli](https://github.com/xgic/payload-cms-cli) | 4 | Core CLI, Dev CLI | Payload CMS orchestration (today often via in-tree **`xde`**; planned under **XGIC CLI**) |

### Naming note (xde → XGIC CLI)

The current environment-orchestration CLI used with Dev Containers is **`xde`**. The planned public product brand after modular extraction is **XGIC CLI** (`xgic.cli.*`). Until extraction ships, use **`xde`** for concrete commands and packages; use **XGIC CLI** for the future public product line. See the [ecosystem catalog](ecosystem/catalog.md) section **XGIC CLI and modules**.

## Namespace rules

1. Top-level package root is **`xgic`**.
2. Libraries use domain paths (e.g. `xgic.gitlab.graphql`).
3. CLI modules live under **`xgic.cli.*`**.
4. Prefer small, importable libraries over ad-hoc scripts.
5. New modules register here (public summary) when the corresponding public repository is announced or published.

## Related ADRs

- [ADR-0001: GitLab architecture and repository naming](adr/0001-xgic-gitlab-architecture-and-repository-naming.md)
- [ADR-0002: Standardize on Python 3.14](adr/0002-standardize-on-python-3-14.md)

## Registration process (public)

1. Define namespace and planned public GitHub repository name.
2. Implement against Python 3.14 baseline (ADR-0002) and OO design norms.
3. License as Apache-2.0 (ADR-0004); set package SPDX/metadata accordingly.
4. Add or update rows in this document **and** [ecosystem/catalog.md](ecosystem/catalog.md).
5. Do not embed private coordination IDs or private repository paths in public documentation.
