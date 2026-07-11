# XGIC AI

**Public multi-repository intelligence hub** for the XGIC ecosystem — standards, architecture, orchestration guidance, and structured knowledge for humans and AI agents.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-hub-informational)](docs/README.md)
[![ADRs](https://img.shields.io/badge/ADRs-index-success)](docs/adr/README.md)

This repository is the **public entry point** into XGIC open-source solutions. It is a curated public subset of the broader XGIC Foundation practice: high-quality documentation, formal Architecture Decision Records (ADRs), base standards, agentic workflows, and an ecosystem catalog designed so AI agents can reason about *what exists*, *where it lives*, and *how components fit together*.

> **Scope today:** documentation, standards, ADRs, and agent knowledge.  
> **Trajectory:** a full-stack cloud-native platform — starting with **Docker Compose** for on-premises deployments and evolving toward **Kubernetes** and hybrid cloud-native operations.

---

## Why this hub exists

| Audience | Value |
|----------|--------|
| **Humans** | Single place to discover XGIC OSS, decisions, and implementation patterns |
| **AI agents** | Structured ecosystem knowledge for intelligent, context-aware recommendations |
| **Implementers** | Faster onboarding: standards, Docker Compose-first ops, and clear module boundaries |
| **Contributors** | Shared ADRs, licensing (Apache 2.0), and contribution process |

Without a hub, multi-repo ecosystems fragment: agents invent dependencies, humans re-read tribal knowledge, and standards drift. **`xgic/ai` is the central intelligence layer** that keeps the public surface coherent as Grok Build and automation advance across projects.

---

## Start here

| Path | Purpose |
|------|---------|
| [docs/ecosystem/catalog.md](docs/ecosystem/catalog.md) | **Component catalog** — libraries, CLI, images, apps, tools |
| [docs/ecosystem/composition.md](docs/ecosystem/composition.md) | How components compose (fit patterns) |
| [docs/agent/knowledge-model.md](docs/agent/knowledge-model.md) | Structured model agents should load |
| [docs/VISION.md](docs/VISION.md) | Long-term platform vision |
| [docs/platform/overview.md](docs/platform/overview.md) | Compose → Kubernetes deployment path |
| [docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md) | Canonical public base standards |
| [docs/adr/](docs/adr/) | Architecture Decision Records |
| [AGENTS.md](AGENTS.md) | Instructions for AI coding assistants |

---

## Ecosystem at a glance

```text
                         ┌──────────────────────┐
                         │      xgic/ai         │
                         │  standards · ADRs    │
                         │  catalog · agents    │
                         └──────────┬───────────┘
              ┌─────────────────────┼─────────────────────┐
              ▼                     ▼                     ▼
        Libraries/CLIs        Orchestration          Surfaces
     xgic.* Python packs    Compose · (K8s path)   CMS · web · UE
     GHCR / Docker images   Dev Containers         Full-stack apps
```

**Planned and current component families** (see the [full catalog](docs/ecosystem/catalog.md)):

- Python libraries and the **XGIC CLI** (core + domain modules)
- Visual Studio Code **Dev Container** projects and **GHCR / Docker** images
- **Payload CMS**, **Next.js**, and custom full-stack applications
- **Unreal Engine** tools and plugins
- **AI playbooks** and agentic workflows
- Cloud-native and hybrid on-premises implementation recommendations
- Formal **ADRs** and multi-repo standards

**Live public repositories today:**

| Repository | Role |
|------------|------|
| [xgic/ai](https://github.com/xgic/ai) | **This hub** |
| [xgic/gitlab-graphql](https://github.com/xgic/gitlab-graphql) | GitLab GraphQL client (`xgic.gitlab.graphql`) |
| [xgic/gitlab](https://github.com/xgic/gitlab) | GitLab EE orchestration / template surface |
| [xgic/payload-cms-dev-containers](https://github.com/xgic/payload-cms-dev-containers) | Dev-container + Payload tooling (`xde`) |

---

## Core principles

1. **Public-safe by default** — No private infrastructure, private tracker IDs, or internal paths in public artifacts ([hard security](docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)).
2. **Apache 2.0** — XGIC public solutions use the Apache License 2.0 ([licensing](docs/licensing.md)).
3. **Docker Compose first, Kubernetes when ready** — On-premises path is Docker Compose; platform design stays portable toward Kubernetes ([platform overview](docs/platform/overview.md)).
4. **Python 3.14** for new Python development ([ADR-0002](docs/adr/0002-standardize-on-python-3-14.md)).
5. **GitHub Flow + human review** — Agents draft; humans approve in the GitHub UI.
6. **Agent-readable structure** — Catalog, composition graph, and knowledge model over prose-only docs.
7. **Rapid evolution** — Hub and private foundation practice co-evolve as AI automation improves daily.

---

## For AI agents

1. Read [AGENTS.md](AGENTS.md) and [docs/agent/knowledge-model.md](docs/agent/knowledge-model.md).
2. Consult the [ecosystem catalog](docs/ecosystem/catalog.md) before inventing modules or repos.
3. Prefer **full HTTPS URLs** (`https://github.com/xgic/...`) for cross-repo references.
4. Recommend **Compose** for on-prem bootstrap; surface the **Kubernetes** path only when requirements justify it.
5. Keep all contributions **public-safe**.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Proposals for new catalog entries, ADRs, and standards improvements are welcome via issues and pull requests.

## License

Copyright 2026 XGIC / Donovan Chepien.  
Licensed under the [Apache License, Version 2.0](LICENSE).  
See [NOTICE](NOTICE) for attribution.
