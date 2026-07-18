# XGIC platform vision

## Purpose

Describe the long-term trajectory of the XGIC public ecosystem so humans and AI agents optimize for the same future—not only the repositories that exist today.

## North star

A **secure, well-documented, AI-accelerated platform** for building and operating full-stack solutions: libraries and CLIs, containerized services, CMS and web applications, real-time/Unreal tooling, and hybrid on-premises / cloud deployments—discoverable through a single public intelligence hub (`xgic/ai`).

## Phases

### Phase 0 — Intelligence hub (now)

- Public standards, ADRs, catalog, and agent knowledge model
- Apache 2.0 licensing policy for public solutions
- GitHub Flow + human review across orchestrated public repos
- Existing OSS seeds: GraphQL client, GitLab orchestration surface, Payload/dev-container tooling

### Phase 1 — Docker Compose-first delivery

- On-premises and workstation deployments default to **Docker Compose**
- Official vendor images for third-party services where applicable ([ADR-0001](adr/0001-xgic-gitlab-architecture-and-repository-naming.md))
- Dev Containers for contributor environments; GHCR for published images
- **XGIC CLI** modules ship as versioned PyPI packages; living docs use **XGIC CLI only** (see [catalog](ecosystem/catalog.md))

### Phase 2 — Modular platform services

- Published Python packages under `xgic.*` (see [namespace convention](xgic-python-namespace-convention.md))
- Clear split between **libraries**, **CLI modules** (XGIC CLI / `xgic.cli.*`), **image producers (`*-dev`)**, and **end-user templates**
- Payload CMS + Next.js reference applications with repeatable bootstrap
- Agentic playbooks covering multi-repo implementation sequences

### Phase 3 — Cloud-native scale-out

- Same application and config contracts deploy to **Kubernetes**
- Hybrid patterns: Docker Compose on edge/on-prem lab; K8s in cloud/production clusters
- Progressive delivery, observability, and policy as code without rewriting product logic
- Platform recommendations remain documentation-first in this hub until services graduate to dedicated repos

## Design tenets

1. **Portable contracts** — Prefer Docker Compose-compatible service definitions and 12-factor config that map cleanly to K8s later.
2. **Thin orchestration** — Orchestrators configure and operate; they do not fork vendor application images.
3. **Agent ergonomics** — Structure docs for machines: catalogs, tables, explicit statuses, stable URLs.
4. **Security boundaries** — Public docs never expose private coordination; private work stays private.
5. **Daily improvement** — As Grok Build and automation advance, distill only public-safe, high-value patterns into this hub.

## Success measures

| Signal | Indicator |
|--------|-----------|
| Discoverability | New contributors/agents find the right repo in minutes |
| Correct composition | Recommendations match catalog + composition rules |
| Ops clarity | Docker Compose path documented; K8s path explicit and non-blocking |
| Coherence | ADRs cited from multiple public repos without policy forks |
| Safety | Zero private leakage incidents in public artifacts |

## Related

- [Platform overview](platform/overview.md)
- [Ecosystem catalog](ecosystem/catalog.md)
- [Agent knowledge model](agent/knowledge-model.md)
