# XGIC ecosystem component catalog

**Audience:** humans and AI agents.  
**Rule:** Prefer this table over inventing modules. Update via PR when a public component is added, renamed, or retired.

**Status legend**

| Status | Meaning |
|--------|---------|
| `available` | Public repository and/or published artifact exists |
| `planned` | Intended public component; not yet fully published |
| `experimental` | Public but evolving rapidly; APIs may change |
| `reference` | Pattern documented here; implementation may live in a sibling repo |

---

## 1. Intelligence and standards

| ID | Name | Type | Status | Location | Purpose |
|----|------|------|--------|----------|---------|
| `hub.ai` | XGIC AI hub | docs / standards | `available` | [xgic/ai](https://github.com/xgic/ai) | Public multi-repo intelligence: ADRs, standards, catalog, agent knowledge |
| `std.base` | Base standards | standard | `available` | [BASE-STANDARDS…](../BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md) | Minimum process/docs for public orchestrated repos |
| `std.adr` | ADR set | decisions | `available` | [docs/adr/](../adr/) | Formal multi-repo architecture decisions |
| `std.playbooks` | AI playbooks | playbooks | `available` | [grok-playbooks.md](../grok-playbooks.md), [agent/](../agent/) | Agentic workflows and recommendation rules |

---

## 2. Python libraries

| ID | Name | Namespace | Status | Location | Purpose |
|----|------|-----------|--------|----------|---------|
| `lib.gitlab.graphql` | GitLab GraphQL client | `xgic.gitlab.graphql` | `available` | [xgic/gitlab-graphql](https://github.com/xgic/gitlab-graphql) | Auth, Work Items, hierarchy, pagination against GitLab GraphQL |
| `lib.cli.core` | Core CLI framework | `xgic.cli` | `available` | [xgic/cli](https://github.com/xgic/cli) | Thin core: framework, env detection, output helpers; entrypoint `xgic` |
| `lib.xde` | Environment orchestration library (current surface) | (via `xde` today; future `xgic.cli.*`) | `experimental` | Lives with [payload-cms-dev-containers](https://github.com/xgic/payload-cms-dev-containers) until extraction | Dev container & environment orchestration primitives |

See also: [Python namespace convention](../xgic-python-namespace-convention.md).

---

## 3. XGIC CLI and modules

**Naming (transition → complete cutover):**

| Phase | Living docs and guidelines | Code / packages |
|-------|----------------------------|-----------------|
| **Now (post B5 cutover for public template)** | Living docs use **XGIC CLI only** / `xgic.cli.*` | Modular packages + template consumer; no supported `xde` entrypoint |
| **Historical only** | Residual `xde` limited to **minimal notes** in completed artifacts (closed issues, old changelogs)—not living standards | No `xde` compatibility alias |

Full extraction and rename follow [ADR-0005](../adr/0005-modular-xgic-cli-and-retirement-of-xde.md) (thin-core first, then domain modules; console entry `xgic`; **no** long-term `xde` alias). Not a bulk rewrite of open historical issues. Do not leave dual product names after cutover.

| ID | Name | Namespace | Status | Location | Purpose |
|----|------|-----------|--------|----------|---------|
| `cli.core` | XGIC CLI core | `xgic.cli` | `available` | [xgic/cli](https://github.com/xgic/cli) | Thin entry framework + plugins (product-agnostic) |
| `cli.dev` | Dev Container CLI module | `xgic.cli.dev` | `available` | [xgic/dev-cli](https://github.com/xgic/dev-cli) | Compose lifecycle (`xgic up`/`down`/`check`/…) + library |
| `cli.gitlab` | GitLab CLI module | `xgic.cli.gitlab` | `planned` | planned `xgic/gitlab-cli` | Backup/restore and GitLab ops |
| `cli.ais` | AIS CLI module | `xgic.cli.ais` | `planned` | planned `xgic/ais-cli` | Automation-oriented features (public surface only) |
| `cli.payload` | Payload CMS CLI module | `xgic.cli.payload` | `available` | [xgic/payload-cms-cli](https://github.com/xgic/payload-cms-cli) | Payload CMS product commands (`xgic payload …`) |
| `cli.xde` | xde (retired) | — | `retired` | historical notes only | Former in-tree entrypoint; living template uses modular XGIC CLI only |

**Principle:** Domain logic in importable libraries; CLI modules are thin orchestration over libraries.

---

## 4. Dev Containers, images, and registries

| ID | Name | Type | Status | Location | Purpose |
|----|------|------|--------|----------|---------|
| `dc.payload` | Payload CMS dev containers | Dev Container project | `available` | [xgic/payload-cms-dev-containers](https://github.com/xgic/payload-cms-dev-containers) | Reproducible Payload CMS + tooling; **consumer** of modular XGIC CLI |
| `img.ghcr` | GHCR publications | container images | `planned` / partial | GitHub Container Registry under `xgic` | Published images for templates and orchestrators |
| `img.dockerhub` | Docker Hub publications | container images | `planned` | as announced per product | Optional mirror / distribution channel |
| `pattern.dev-suffix` | `*-dev` producer repos | naming pattern | `reference` | [ADR-0001](../adr/0001-xgic-gitlab-architecture-and-repository-naming.md) | Image producers use `-dev`; clean templates omit it |

**Vendor images:** Prefer official unaltered images for third-party products (GitLab EE, Postgres, Redis, etc.).

---

## 5. Orchestration and platform services

| ID | Name | Type | Status | Location | Purpose |
|----|------|------|--------|----------|---------|
| `orch.gitlab` | GitLab orchestration surface | Compose / template | `available` | [xgic/gitlab](https://github.com/xgic/gitlab) | GitLab EE-oriented orchestration / template experience |
| `orch.compose` | Docker Compose-first ops | pattern | `reference` | [platform/docker-compose.md](../platform/docker-compose.md) | Default on-prem deployment model |
| `orch.k8s` | Kubernetes path | pattern | `reference` | [platform/kubernetes.md](../platform/kubernetes.md) | Future scale-out; same contracts where possible |
| `orch.hybrid` | Hybrid on-prem / cloud | pattern | `reference` | [platform/hybrid.md](../platform/hybrid.md) | Lab/edge Compose + cloud K8s recommendations |

---

## 6. Applications and content platforms

| ID | Name | Stack | Status | Location | Purpose |
|----|------|-------|--------|----------|---------|
| `app.payload` | Payload CMS solutions | Payload CMS | `experimental` / `available` tooling | Dev-container repo + future app templates | Headless CMS and content apps |
| `app.next` | Next.js applications | Next.js | `planned` | future public app repos | Web frontends and full-stack Next apps |
| `app.fullstack` | Custom full-stack apps | polyglot | `planned` | future public app repos | Product-specific full-stack systems following hub standards |
| `app.unreal` | Unreal Engine tools & plugins | Unreal Engine | `planned` | future public UE repos | Editor tools, plugins, pipelines |

---

## 7. Cross-cutting practices

| ID | Name | Status | Location | Purpose |
|----|------|--------|----------|---------|
| `prac.agentic` | Agentic workflows | `available` | [grok-playbooks.md](../grok-playbooks.md), [agent/](../agent/) | Multi-step AI-assisted implementation |
| `prac.python314` | Python 3.14 baseline | `available` | [ADR-0002](../adr/0002-standardize-on-python-3-14.md) | New Python development standard |
| `prac.apache` | Apache 2.0 licensing | `available` | [licensing.md](../licensing.md), [ADR-0004](../adr/0004-apache-2-0-for-public-solutions.md) | Public solutions license |
| `prac.security` | Public hard security | `available` | [BASE-STANDARDS…](../BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md) | Zero private leakage in public artifacts |

---

## Catalog maintenance

1. New public component → add a row with stable `ID`, status, and HTTPS location.  
2. Rename/move → update row and leave a one-line note in PR description.  
3. Retire → set status to retired in a follow-up or remove with ADR if multi-repo impact.  
4. Do **not** list private repositories or private tracker IDs.
