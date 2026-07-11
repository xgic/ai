# Architecture Decision Records (ADRs)

ADRs capture **multi-repository** decisions that public XGIC projects and AI agents should share.

## Index

| ADR | Title | Status |
|-----|-------|--------|
| [0001](0001-xgic-gitlab-architecture-and-repository-naming.md) | GitLab architecture, repository naming, phased CLI | Accepted |
| [0002](0002-standardize-on-python-3-14.md) | Standardize new Python development on Python 3.14 | Accepted |
| [0003](0003-docker-compose-first-kubernetes-ready.md) | Docker Compose-first deployments, Kubernetes-ready architecture | Accepted |
| [0004](0004-apache-2-0-for-public-solutions.md) | Apache 2.0 for XGIC public solutions | Accepted |

## When to write an ADR here

- The decision affects **more than one** public repository, or
- Other repos need a stable public citation target, or
- The decision defines a portfolio convention (naming, runtime, licensing, deployment path)

Product-specific decisions belong in the product repository’s own `docs/adr/` (or equivalent).

## ADR format

1. **Status** — Proposed / Accepted / Superseded  
2. **Date**  
3. **Context**  
4. **Decision**  
5. **Consequences**  
6. **References** — related ADRs, hub docs, public URLs only  

## Process

1. Open an issue on this repository.  
2. Add `docs/adr/NNNN-short-title.md` and update this index in the same PR.  
3. Human review and merge.  
4. Downstream repos adopt via normal PRs, linking the hub ADR.  

## Public-safety

ADRs must not include private hosts, private tracker IDs, private repositories, internal paths, or anything that violates information security best practices and XGIC cybersecurity standards.
