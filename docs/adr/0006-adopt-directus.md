# ADR-0006: Adopt Directus as the next production CMS candidate

**Status:** Proposed  
**Date:** 2026-09-01  
**Scope:** Public XGIC CMS tooling, image producers, templates, and
agent playbooks

---

## Context

XGIC needs a reusable headless CMS standard for many kinds of websites
and web applications. The most demanding project will use a large,
deeply hierarchical relational schema. The CMS choice is driven by that
schema complexity, development-time resource behavior, licensing, and
how cleanly the stack fits the existing producer / template / CLI
repository pattern.

The previous CMS candidate, Payload CMS 3.88 on Next.js 16.3.3, showed
development-time memory usage that exceeded acceptable limits. That
candidate never entered production. Existing Payload repositories stay
published; there is no forced migration.

Directus is selected as the **next** production candidate for its lower
idle footprint, official vendor images, and schema-first relational
modeling suited to complex, deeply hierarchical data models. A final
production verdict follows only after the three-repo plan is built and
exercised.

---

## Decision

### 1. Adopt Directus as the next production candidate

**Decision:** Adopt Directus as the next production candidate for new
XGIC work. Existing Payload repositories stay as-is for now; no forced
migration. A final production verdict follows only after the three-repo
plan is built and exercised in real development.

### 2. Preserve the three-repo structure

**Decision:** The CLI, image producer, and template remain separate
repositories.

- **CLI** — Python module under the `xgic.cli.directus` namespace that
  plugs into the shared XGIC CLI core, independently versioned and
  reusable across every site.
- **Producer** — one highly optimized VS Code Dev Container image,
  pinned and multi-arch, published to GHCR as
  `ghcr.io/xgic/directus-dev`. It installs the XGIC CLI modules,
  Postgres and Redis clients, and the full test harness: unit,
  integration, and smoke tests. The image is the stable development
  environment consumed by the template.
- **Template** — thin consumer of that pinned image. It holds only
  site-specific schema, extensions, and Docker Compose overrides, and
  is intended to spin up quickly.

This continues the producer / template split already recorded in
[ADR-0001](0001-xgic-gitlab-architecture-and-repository-naming.md) and
the modular CLI model in
[ADR-0005](0005-modular-xgic-cli-and-retirement-of-xde.md).

Do **not** bootstrap those repositories until this ADR is accepted.

### 3. Start lean; optimize from day one

**Decision:** Prefer the official `directus/directus` image with
explicit version pins. Build a custom producer image only when there is
a concrete, measured need. Optimize for low idle memory and fast cold
start from day one, and validate the empty-site footprint on a
constrained Linux test environment before any schema work begins. Use
schema-first modeling in Postgres, not code-first collections, so the
relational data model stays the source of truth.

### 4. Root-cause discipline in agent instructions

**Decision:** Shared playbooks and each repository `AGENTS.md` require
diagnosis before patching. Prefer structural fixes over workarounds.
Document recurring failure modes as rules so the same class of defect
is not patched around repeatedly. This matches the public base-standards
requirement to fix root causes rather than environment-specific
workarounds.

---

## Alternatives considered

| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| **Directus** | Schema-first relational modeling in Postgres; official images; low idle memory; strong REST, GraphQL, and realtime APIs; fits deeply hierarchical and relational data models | Newer ecosystem than Django-based options; extension model differs from code-first CMS | **Selected** as next production candidate |
| **Payload CMS 3.88** | Code-first TypeScript collections; tight Next.js integration; strong TypeScript DX | Development-time memory usage on Next.js 16.3.3 exceeded acceptable limits; never entered production | Not selected for this cycle; may be reconsidered |
| **Strapi** | Mature, widely adopted; plugin ecosystem | Significant features behind a commercial paywall; heavier runtime | Not selected — paywalled core features conflict with cost control |
| **Wagtail** | Django-based; excellent performance; very low memory footprint; mature admin | Older technology stack; less modern developer experience than Payload or Directus; weaker fit for complex application schemas | Not selected as the successor CMS; strong performer for other workloads |
| **Nuxt** | Fine-grained control over each tier; business logic separable into its own repository | High development complexity for this use case; not a CMS | Not selected as CMS; tier-separation ideas may inform architecture later |
| **Pure Next.js** | Maximum framework control; no separate CMS dependency; unified TypeScript stack | Reimplements CMS concerns (schema, admin, API) by hand; no relational data modeling out of the box | Not selected — too much custom infrastructure for the payoff |

---

## Consequences

### Positive

- Lighter development images and no Turbopack dependency in the CMS
  path.
- Schema-first relational modeling suited to complex, deeply
  hierarchical data models across many websites and applications.
- Reusable producer image and a thin template that can be instantiated
  per site.
- Same three-repo pattern already used for other XGIC products.

### Trade-offs

- A second CMS story until Payload is retired or later reconsidered.
- Shared playbook plus per-repo overrides adds a small maintenance
  surface.
- Directus remains a candidate until the three-repo plan proves it in
  practice.

### Rejected alternatives

Covered in the table above.

---

## References

- [ADR-0001: XGIC GitLab architecture and repository naming](0001-xgic-gitlab-architecture-and-repository-naming.md)
- [ADR-0003: Docker Compose-first, Kubernetes-ready](0003-docker-compose-first-kubernetes-ready.md)
- [ADR-0005: Modular XGIC CLI](0005-modular-xgic-cli-and-retirement-of-xde.md)
- [Base standards for orchestrated repos](../BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)
- [Ecosystem catalog](../ecosystem/catalog.md)
- [Grok playbooks](../grok-playbooks.md)
- Intended public repositories (not yet published): `xgic/directus-dev`,
  `xgic/directus`, `xgic/directus-cli`
- Intended image: `ghcr.io/xgic/directus-dev`
