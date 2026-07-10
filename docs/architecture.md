# Public multi-repository architecture

High-level mental model for humans and AI agents working across XGIC public GitHub repositories.

## Hub role

**`xgic/ai`** is the public standards and orientation hub:

- ADRs that span multiple public repositories
- Python namespace registry (public summary)
- Canonical public base standards
- Agent playbooks and workflow guidance

Individual product repositories remain the source of truth for their **code**, CI, and product-specific docs. They should **link** here for shared multi-repo policy rather than forking large policy documents.

## Layers

```text
┌─────────────────────────────────────────────────────────────┐
│  xgic/ai  — public standards, ADRs, namespace, playbooks     │
└────────────────────────────┬────────────────────────────────┘
                             │ cited by
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
   Libraries / CLIs    Orchestrators      Dev-container producers
   (e.g. graphql)      (e.g. gitlab)      (e.g. payload-cms-…)
```

## Current public surfaces

| Surface | Responsibility |
|---------|----------------|
| **Standards hub** (`xgic/ai`) | Cross-cutting decisions and process |
| **Libraries** | Versioned Python packages under `xgic.*` |
| **Orchestrators / templates** | End-user Compose/config experiences; often consume GHCR images |
| **Dev-container / image producers** | Contributor environments and image build pipelines (`*-dev` naming when applicable) |

See [ADR-0001](adr/0001-xgic-gitlab-architecture-and-repository-naming.md) for the two-repository (`-dev` vs template) model and official-image policy.

## Design invariants

1. **Public-only content** in public repositories (hard security).
2. **Official vendor images** for application services when orchestrating third-party products.
3. **Python 3.14** minimum for *new* Python development ([ADR-0002](adr/0002-standardize-on-python-3-14.md)).
4. **OO design + Pydantic** for structured configuration and service logic where Python is used.
5. **Shared CLI direction** (`xgic.cli.*`, domain tools such as `xde`) instead of new Makefiles.
6. **GitHub Flow + human review** on every public repository.

## Agent mental model

When an agent lands in a public XGIC repository:

1. Read that repo’s `AGENTS.md` and local docs first.
2. Use **this hub** for multi-repo decisions (ADRs, namespace, base standards).
3. Keep changes scoped to the current repo unless the task explicitly updates the hub.
4. Never invent private infrastructure details; if something is not documented publicly, say so and stay at the public boundary.

## Related

- [Base standards](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)
- [Python namespace convention](xgic-python-namespace-convention.md)
- [Orchestration workflow](orchestration-workflow.md)
