# Agent recommendation guide

Worked guidance for producing **intelligent, context-aware recommendations** across the XGIC public ecosystem.

## Output shape (recommended)

When advising a human or planning agent work, emit:

```markdown
## Goal
…

## Recommended components
| Catalog ID | Why | Status | Link |
|------------|-----|--------|------|

## Composition
Ordered steps (bootstrap → integrate → verify)

## Deployment
Docker Compose | Kubernetes | Hybrid — with rationale

## Standards / ADRs to follow
…

## Out of scope / unknown
What is not public yet (use planned catalog rows; do not invent private systems)
```

## Scenario examples

### A. “Automate GitLab Work Items from Python”

| Step | Action |
|------|--------|
| Match | `lib.gitlab.graphql` (`available`) |
| Link | https://github.com/xgic/gitlab-graphql |
| Composition | Library only unless operator UX needed → then experimental `cli.gitlab` (`xgic gitlab …`) |
| Deploy | N/A for library; if full GitLab stack needed → `orch.gitlab` + `img.xgic-gitlab` + Docker Compose |
| ADRs | 0001 naming/images, 0002 Python, 0004 license, 0005 modular CLI |

### B. “Stand up Payload CMS for local development”

| Step | Action |
|------|--------|
| Match | `dc.payload` / payload-cms-dev-containers |
| Link | https://github.com/xgic/payload-cms-dev-containers |
| Composition | Dev Container + Docker Compose services; prefer modular XGIC CLI over new Makefiles |
| Deploy | Docker Compose first |
| Avoid | Custom forked DB images if official Postgres works |

### C. “We need production HA in the cloud”

| Step | Action |
|------|--------|
| Start | Confirm app contracts are 12-factor / portable |
| Path | Document Docker Compose parity → introduce K8s manifests/Helm later in product repos |
| Hub | Cite [platform/kubernetes.md](../platform/kubernetes.md) and ADR-0003 |
| Avoid | Blocking on-prem users on K8s-only tooling |

### D. “Add a new XGIC Python CLI module”

| Step | Action |
|------|--------|
| Namespace | `xgic.cli.<domain>` per namespace convention |
| Status | If not in catalog → PR to `xgic/ai` catalog first or same change set |
| Depends | Core CLI (`available`, [xgic/cli](https://github.com/xgic/cli)) + domain libraries |
| License | Apache-2.0 |
| Python | `>=3.14` |

### E. “What is XGIC?” (onboarding)

1. Point to hub README + VISION  
2. Show catalog families  
3. List available repos with HTTPS links  
4. Explain Docker Compose-first ops and public-safe rules  

## Quality bar

| Check | Pass criteria |
|-------|----------------|
| Grounded | Every component cited appears in catalog or ADR |
| Linked | Full HTTPS URLs for other public repos |
| Safe | No private hosts/IDs/paths |
| Ordered | Clear sequence; blockers explicit |
| Honest | Planned vs available distinguished |

## Related

- [knowledge-model.md](knowledge-model.md)
- [composition.md](../ecosystem/composition.md)
- [catalog.md](../ecosystem/catalog.md)
