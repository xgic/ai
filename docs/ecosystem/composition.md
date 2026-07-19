# Ecosystem composition guide

How XGIC public components **should fit together**. Agents use this to make context-aware recommendations; humans use it to avoid architecture drift.

## Dependency direction (preferred)

```text
Applications / templates
        │  consume
        ▼
Orchestrators (Docker Compose today · K8s later)
        │  use
        ▼
CLI modules  ──►  libraries (xgic.*)
        │
        ▼
Images (GHCR) · official vendor images
        │
        ▼
Host / cluster runtime
```

**Rules of thumb**

1. **Libraries** have no dependency on CLIs or app repos.  
2. **CLI modules** depend on libraries, not on specific application repos.  
3. **Dev-container / `*-dev` repos** produce images; **template repos** consume them.  
4. **This hub (`xgic/ai`)** is documentation-only: no runtime dependency from product code.  
5. **Applications** may depend on libraries and images; they should not re-implement catalogued library logic.

---

## Recommended compositions

| Goal | Prefer | Avoid |
|------|--------|--------|
| Talk to GitLab GraphQL from Python | `lib.gitlab.graphql` | Ad-hoc raw GraphQL clients in each app |
| Local GitLab EE lab | `orch.gitlab` + `img.xgic-gitlab` + official `gitlab/gitlab-ee` / Postgres / Redis | Custom GitLab EE image forks; building the orchestrator inside the template repo |
| Payload contributor environment | `dc.payload` + modular XGIC CLI from PyPI | One-off Dockerfiles without shared tooling |
| New Python package | `xgic.*` namespace + Python 3.14 + Apache 2.0 | Random top-level package names |
| On-prem deploy | Docker Compose first ([platform/docker-compose.md](../platform/docker-compose.md)) | Jumping to K8s without requirements |
| Cloud HA / multi-cluster | K8s path with portable contracts | Rewriting app logic for the orchestrator |
| Multi-repo policy | Link `https://github.com/xgic/ai` | Forking large policy docs into every repo |

---

## Fit patterns by domain

### GitLab automation

- **Library:** `xgic.gitlab.graphql` for API access  
- **Dual-repo orchestration (ADR-0001):**  
  - **Producer:** `orch.gitlab.dev` ([xgic/gitlab-dev](https://github.com/xgic/gitlab-dev)) publishes `img.xgic-gitlab` (`ghcr.io/xgic/xgic-gitlab`)  
  - **Template:** `orch.gitlab` ([xgic/gitlab](https://github.com/xgic/gitlab)) Compose consumer — official vendor images + orchestration image  
- **CLI (planned):** `xgic.cli.gitlab` for operator workflows  
- **Decision source:** [ADR-0001](../adr/0001-xgic-gitlab-architecture-and-repository-naming.md)

### Content & web

- **CMS:** Payload CMS with shared dev-container patterns  
- **Web:** Next.js apps as separate deployable units  
- **Shared:** Apache 2.0, public-safe docs, Docker Compose for local stacks

### Environment orchestration

- Prefer **XGIC CLI** (`xgic` / `xgic.cli.*`) over new Makefiles. Living docs use **XGIC CLI only** (no supported `xde`).  


- Scripts remain thin shims; logic lives in tested Python where growth warrants it  

### Real-time / Unreal (planned)

- UE tools and plugins ship as dedicated public repos when ready  
- Share CI/docs standards from this hub; do not couple UE code to CMS runtimes  

---

## Anti-patterns

| Anti-pattern | Why it hurts | Prefer |
|--------------|--------------|--------|
| Private IDs in public PRs | Security / trust failure | Public-only references |
| New Makefile islands | Divergent DX | XGIC CLI modules (`xgic.cli.*`) |
| Custom vendor image forks | Patch burden | Official images + config |
| Invented `xgic` submodules not in catalog | Agent confusion | PR to update catalog first |
| K8s-only from day one for simple on-prem | Complexity tax | Docker Compose first |
| Duplicating ADRs in every repo | Drift | Cite hub ADRs |

---

## Recommendation algorithm (for agents)

```text
1. Classify user goal (library | CLI | image | app | ops | docs)
2. Match catalog rows by domain and status
3. If available → recommend that component + HTTPS URL
4. If planned only → say so; propose interim using available parts
5. Choose deploy model: Docker Compose default; K8s if scale/HA/multi-tenant explicit
6. Check ADRs for naming, Python version, license
7. Emit a short composition plan (ordered steps, no private details)
```

See [agent/recommendation-guide.md](../agent/recommendation-guide.md) for worked examples.
