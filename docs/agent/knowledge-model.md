# Agent knowledge model

Formal model of the XGIC public ecosystem for AI agents. Prefer this structure when building context graphs, RAG indexes, or multi-step plans.

## Entity types

| Type | Description | Examples |
|------|-------------|----------|
| `Hub` | Documentation/intelligence repository | `xgic/ai` |
| `Library` | Importable package | `xgic.gitlab.graphql` |
| `CliModule` | CLI surface over libraries | `xgic.cli.gitlab` (planned) |
| `DevContainerProject` | VS Code Dev Container producer/consumer | payload-cms-dev-containers |
| `Image` | Container image artifact | GHCR images |
| `Orchestrator` | Compose/K8s stack definition surface | xgic/gitlab |
| `Application` | Product or sample app | Payload/Next.js apps |
| `Standard` | Process or technical standard | base standards, Apache 2.0 |
| `ADR` | Architecture decision record | ADR-0001… |
| `Playbook` | Stepwise agent/human procedure | grok-playbooks |
| `Pattern` | Reusable architecture pattern | Compose-first, `*-dev` naming |

## Relationship types

| Edge | Meaning |
|------|---------|
| `DOCUMENTS` | Hub/ADR documents a component or pattern |
| `IMPLEMENTS` | Repo implements a catalog component |
| `DEPENDS_ON` | Runtime or build dependency |
| `PRODUCES` | Repo produces an image or package |
| `CONSUMES` | Repo/template consumes an image or package |
| `EXTENDS` | CLI module extends core CLI |
| `CITES` | Doc/repo cites an ADR or standard |
| `DEPLOYS_WITH` | Component is typically deployed via Compose or K8s |

## Canonical graph (simplified)

```text
Hub(xgic/ai)
  DOCUMENTS → Standard(base), ADR(*), Pattern(compose-first), Catalog(*)
Library(gitlab.graphql) IMPLEMENTS ← Repo(gitlab-graphql)
Orchestrator(gitlab) CONSUMES → Image(vendor gitlab-ee, postgres, redis)
DevContainerProject(payload-cms-dev-containers) PRODUCES → local/dev images
CliModule(*) EXTENDS → CliModule(core) DEPENDS_ON → Library(*)
Application(*) DEPENDS_ON → Library(*) ; DEPLOYS_WITH → Pattern(compose|k8s)
```

## Required attributes per catalog component

Agents should treat each catalog row as having:

| Field | Required | Notes |
|-------|----------|-------|
| `id` | yes | Stable string (e.g. `lib.gitlab.graphql`) |
| `name` | yes | Human title |
| `type` | yes | Entity type |
| `status` | yes | available / planned / experimental / reference |
| `location` | yes | HTTPS URL or hub-relative path |
| `purpose` | yes | One-sentence capability |
| `namespace` | when Python | e.g. `xgic.cli.dev` |
| `interfaces` | recommended | library API, CLI, Compose service, HTTP, etc. |
| `depends_on` | recommended | Other catalog IDs |

## Invariants agents must not violate

1. **Public-safe outputs only** in public repos and public PR text.  
2. **No private tracker IDs** as close references from public GitHub.  
3. **Namespace root `xgic`** for Python packages unless an ADR says otherwise.  
4. **Python `>=3.14`** for new Python code ([ADR-0002](../adr/0002-standardize-on-python-3-14.md)).  
5. **Apache-2.0** for new public XGIC solutions ([ADR-0004](../adr/0004-apache-2-0-for-public-solutions.md)).  
6. **Compose default** for on-prem; K8s when justified ([ADR-0003](../adr/0003-compose-first-kubernetes-ready.md)).  
7. **Catalog before invention** — if missing, propose a catalog PR rather than silent new modules.

## Context pack (minimum load order)

For multi-repo XGIC tasks, load in this order:

1. `AGENTS.md` (this hub)  
2. `docs/agent/knowledge-model.md` (this file)  
3. `docs/ecosystem/catalog.md`  
4. `docs/ecosystem/composition.md`  
5. Relevant ADRs  
6. Target repository’s own `AGENTS.md` and README  

## Evolution

As new public components ship, update the catalog and, when relationships change, this model. Prefer additive rows over rewriting history. Major platform shifts get ADRs.
