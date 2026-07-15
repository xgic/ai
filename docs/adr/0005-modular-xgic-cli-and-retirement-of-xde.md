# ADR-0005: Modular XGIC CLI and retirement of the transitional `xde` brand

**Status**: Proposed  
**Date**: 2026-07-15  
**Scope**: Public XGIC CLI packages, environment orchestration modules, hub catalog/namespace docs, and living standards that describe the CLI brand

---

## Context

XGIC ships environment and dev-container orchestration today primarily as an in-tree CLI/library surface known as **`xde`** (for example inside the public Payload CMS Dev Containers project). That surface is valuable, but:

1. The **product brand** intended for the portfolio is **XGIC CLI**, not a permanent dual name.  
2. Shared libraries should live in **modular public packages** under the `xgic.cli` / `xgic.cli.*` namespaces, not only inside one product template repo.  
3. Living documentation already uses a **pre-cutover** bridge: introduce the tool as `xde` (current CLI; successor brand: XGIC CLI) while real commands/paths remain `xde`.  
4. Agents and humans are confused when strategy docs say one name and packages another without a clear end state.

A long-term **compatibility alias** period (`xde` entrypoint remaining supported after modular cutover) was considered and **rejected**: it prolongs dual branding and confuses catalog rows, packaging, and agent instructions.

Related hub docs: [ecosystem catalog](../ecosystem/catalog.md), [Python namespace convention](../xgic-python-namespace-convention.md), [ADR-0002](0002-standardize-on-python-3-14.md), [ADR-0004](0004-apache-2-0-for-public-solutions.md).

---

## Decision

### 1. Product brand

**XGIC CLI** is the public product brand for the modular CLI framework and domain modules after cutover.

### 2. Namespaces and repositories (target)

| Component | Namespace | Planned public repository |
|-----------|-----------|---------------------------|
| Core framework + `xgic` entry | `xgic.cli` | `xgic/cli` |
| Dev container / env orchestration | `xgic.cli.dev` | `xgic/dev-cli` |
| Payload-oriented commands | `xgic.cli.payload` | `xgic/payload-cms-cli` |
| GitLab-oriented commands | `xgic.cli.gitlab` | `xgic/gitlab-cli` |
| AIS-oriented public surface | `xgic.cli.ais` | `xgic/ais-cli` |

Libraries that are not CLI modules continue under domain packages (e.g. `xgic.gitlab.graphql` in `xgic/gitlab-graphql`).

### 3. Console entrypoint

- **After cutover:** the supported console script is **`xgic`** (plugin/subcommand architecture).  
- **After cutover:** **do not** ship a supported `xde` console script or package entrypoint as a compatibility alias.  
- **Pre-cutover:** existing `xde` entrypoints remain valid until the hard cutover for that ship path.

### 4. Extraction strategy

Prefer **thin-core first, then domain modules**:

1. Bootstrap public `xgic/cli` (scaffold + packaging + CI).  
2. Extract shared core (environment/docker/project/CLI framework) from the transitional in-tree surface into `xgic.cli`.  
3. Extract non-product-specific env/dev commands into `xgic.cli.dev`.  
4. Extract product-specific Payload commands into `xgic.cli.payload`.  
5. **Hard cutover:** remove supported `xde` surface from living docs and shipping entrypoints.  
6. Later: GitLab CLI and public-safe AIS CLI modules (do not block cutover).

Product template repositories (e.g. Payload Dev Containers) become **consumers** of modular packages, not the long-term home of the shared library.

### 5. Documentation rules

| Phase | Living docs / guidelines | Code / packages |
|-------|--------------------------|-----------------|
| **Pre-cutover** | May say `xde` (current CLI; successor brand: XGIC CLI); use `xde` for real commands/paths | `xde` remains where still shipped |
| **Post-cutover** | **XGIC CLI only** / `xgic.cli.*` — no living dual brand | No supported `xde` entrypoint or package as product surface |

Residual `xde` text after cutover is limited to **minimal historical notes** in completed artifacts (changelogs, closed issues)—not living standards.

Do **not** mass-rewrite historical closed issues solely to rename `xde`.

### 6. Licensing and quality bar

New public CLI modules follow the public bar: Apache-2.0 + `Copyright 2026 XGIC`, root `CONTRIBUTING`, community health, branch protection, **root CODEOWNERS**, Python 3.14 for new code, public-safe content only.

---

## Consequences

### Positive

- Clear single product brand after cutover  
- Modular reuse across Payload, GitLab, and future products  
- Better agent ergonomics (one entrypoint family, stable namespaces)  
- Aligns catalog, namespace registry, and packaging  

### Trade-offs

- Multi-repo extract work and short dual-maintenance until cutover  
- Callers must migrate from `xde` commands at cutover (documented map required)  
- Requires disciplined public-safe extraction and pre-public checklist per new repo  

### Rejected alternatives

| Alternative | Why rejected |
|-------------|--------------|
| Permanent dual brand (`xde` + XGIC CLI) | Ongoing agent/human confusion |
| Long-term `xde` alias after modular ship | Re-creates dual product line |
| Rename only inside one product repo | Never yields portfolio modular brand |
| Big-bang monorepo extract then maybe split | Acceptable fallback only if thin-core path is blocked |

---

## Implementation notes (public)

1. Hub ADR accepted (this document).  
2. Create `xgic/cli` with installable stub (`xgic --help` / `--version`).  
3. Port core library + tests; keep product template green on transitional entrypoint until cutover.  
4. Publish domain modules; update catalog rows from `planned` / `experimental` as they ship.  
5. Cutover PR set: entrypoints, living READMEs, catalog, namespace summary.  
6. Command migration map in hub or module READMEs for humans and agents.

---

## References

- [ecosystem/catalog.md](../ecosystem/catalog.md)  
- [xgic-python-namespace-convention.md](../xgic-python-namespace-convention.md)  
- [ADR-0001](0001-xgic-gitlab-architecture-and-repository-naming.md) (phased CLI / repo naming patterns)  
- [ADR-0002](0002-standardize-on-python-3-14.md)  
- [ADR-0004](0004-apache-2-0-for-public-solutions.md)  
- Transitional reference implementation: [payload-cms-dev-containers](https://github.com/xgic/payload-cms-dev-containers) (in-tree CLI surface until extraction)  
- Existing modular library example: [gitlab-graphql](https://github.com/xgic/gitlab-graphql)  
