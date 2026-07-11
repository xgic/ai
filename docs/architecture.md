# Public multi-repository architecture

High-level mental model for humans and AI agents working across XGIC public GitHub repositories.

## Hub role

**`xgic/ai`** is the **public intelligence layer**:

- ADRs spanning multiple public repositories  
- Ecosystem catalog and composition rules  
- Agent knowledge model and playbooks  
- Canonical public base standards  
- Platform path: Docker Compose → Kubernetes  

Individual product repositories remain the source of truth for **code**, CI, and product-specific docs. They should **link** here for shared multi-repo policy.

This hub is a **public subset** of broader foundation practice. Private coordination details are intentionally absent.

## Layered architecture

```text
┌──────────────────────────────────────────────────────────────┐
│  Intelligence   xgic/ai — standards · ADRs · catalog · agents│
└────────────────────────────┬─────────────────────────────────┘
                             │ guides
┌────────────────────────────┼─────────────────────────────────┐
│  Experience     Apps · CMS · Next.js · Unreal tools (planned)│
└────────────────────────────┬─────────────────────────────────┘
                             │
┌────────────────────────────┼─────────────────────────────────┐
│  Control        XGIC CLI modules · playbooks · automation    │
└────────────────────────────┬─────────────────────────────────┘
                             │
┌────────────────────────────┼─────────────────────────────────┐
│  Capability     Python libraries (xgic.*)                    │
└────────────────────────────┬─────────────────────────────────┘
                             │
┌────────────────────────────┼─────────────────────────────────┐
│  Runtime        Docker Compose (default) · Kubernetes (scale)│
│                 GHCR/Docker images · official vendor images  │
│                 Dev Containers for contributors              │
└──────────────────────────────────────────────────────────────┘
```

## Design invariants

1. **Public-only content** in public repositories (hard security).  
2. **Apache 2.0** for public solutions ([ADR-0004](adr/0004-apache-2-0-for-public-solutions.md)).  
3. **Official vendor images** for third-party services when orchestrating them.  
4. **Python 3.14** minimum for *new* Python development ([ADR-0002](adr/0002-standardize-on-python-3-14.md)).  
5. **OO design + Pydantic** for structured configuration where Python is used.  
6. **Shared CLI / xde direction** — no new Makefiles in new or modernized repos.  
7. **Docker Compose default; Kubernetes-ready contracts** ([ADR-0003](adr/0003-docker-compose-first-kubernetes-ready.md)).  
8. **GitHub Flow + human review** on every public repository.  
9. **Catalog-driven discovery** — agents consult the ecosystem catalog before inventing modules.

## Current public surfaces

| Surface | Responsibility |
|---------|----------------|
| **Intelligence hub** (`xgic/ai`) | Cross-cutting decisions, catalog, agent knowledge |
| **Libraries** | Versioned Python packages under `xgic.*` |
| **Orchestrators / templates** | End-user Compose/config experiences |
| **Dev-container / image producers** | Contributor environments and image pipelines (`*-dev` when applicable) |

## Agent mental model

1. Read the target repo’s `AGENTS.md` and local docs.  
2. Load this hub’s [knowledge model](agent/knowledge-model.md) and [catalog](ecosystem/catalog.md).  
3. Keep changes scoped unless the task updates the hub.  
4. Never invent private infrastructure; use `planned` catalog rows when something is not public yet.

## Related

- [VISION.md](VISION.md)
- [Ecosystem catalog](ecosystem/catalog.md)
- [Composition](ecosystem/composition.md)
- [Platform overview](platform/overview.md)
- [Base standards](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)
