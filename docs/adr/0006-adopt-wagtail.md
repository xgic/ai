# ADR-0006: Adopt Wagtail as the default CMS

**Status:** Accepted  
**Date:** 2026-09-02  
**Accepted:** 2026-09-02  
**Scope:** Public XGIC CMS tooling, image producers, templates, and
agent playbooks

---

## Context

After evaluating multiple CMS and framework options, **Wagtail** is
selected as the default CMS for new XGIC work. It is BSD-licensed,
fully free for commercial use and client recommendations, with no
paywalls, no license keys, no collection caps, and no telemetry.
Wagtail 8.0 (released 2026-08-25) is current; the 7.4 LTS line remains
supported through November 2027.

The previous code-first candidate, Payload CMS 3.88 on Next.js 16.3.3,
showed development-time memory usage that exceeded acceptable limits.
That candidate never entered production. Existing Payload repositories
stay published; there is no forced migration.

Directus v12 was evaluated and is **not** selected: it uses a
source-available license with key enforcement, feature caps, and
paywalled capabilities — the same class of commercial restriction this
standard is designed to avoid. Strapi was evaluated and rejected for
paywalled core features.

Wagtail provides schema-first relational modeling in Postgres suited to
complex, deeply hierarchical data models, a generated admin UI,
StreamFields, and multi-site support within a single instance.

---

## Decision

### 1. Adopt Wagtail as the default CMS

**Decision:** Adopt Wagtail as the default CMS for new XGIC work. A
final production verdict follows only after the three-repo plan is
built and exercised in real development.

### 2. Multi-site within instances, separate instances by domain

**Decision:** Use Wagtail’s first-class multi-site support, but deploy
separate instances per business domain (for example the public IT
company site and the game company) to keep data and operations cleanly
separated while sharing one codebase and operational model.

### 3. Preserve the three-repo structure

**Decision:** The CLI, image producer, and template remain separate
repositories.

- **CLI** — Python module under the `xgic.cli.wagtail` namespace that
  plugs into the shared XGIC CLI core, independently versioned and
  reusable across every site.
- **Producer** — one highly optimized VS Code Dev Container image,
  pinned and multi-arch, published to GHCR as
  `ghcr.io/xgic/wagtail-dev`. It installs a preferred AI coding agent,
  the XGIC CLI modules, Postgres and Redis clients, and the full test
  harness: unit, integration, and smoke tests.
- **Template** — thin consumer of that pinned image. It holds only
  site-specific schema, extensions, and Docker Compose overrides, and
  is intended to spin up quickly.

This continues the producer / template split in
[ADR-0001](0001-xgic-gitlab-architecture-and-repository-naming.md) and
the modular CLI model in
[ADR-0005](0005-modular-xgic-cli-and-retirement-of-xde.md).

Public repositories: [xgic/wagtail-cli](https://github.com/xgic/wagtail-cli),
[xgic/wagtail-dev](https://github.com/xgic/wagtail-dev),
[xgic/wagtail](https://github.com/xgic/wagtail).
`xgic/wagtail-dev` is the GHCR **producer** for `ghcr.io/xgic/wagtail-dev`
([ADR-0001](0001-xgic-gitlab-architecture-and-repository-naming.md)).
The image is not published yet; that does not change the repo’s purpose.

### 4. Start lean; optimize from day one

**Decision:** Prefer official Python / Wagtail / Django / Postgres
images as **unaltered bases** (same rule as GitLab EE, Postgres, and
Redis in [ADR-0001](0001-xgic-gitlab-architecture-and-repository-naming.md)).
Do not fork vendor CMS images. The XGIC `*-dev` repository still
**publishes** `ghcr.io/xgic/wagtail-dev`: a pinned multi-arch Dev
Container producer image built FROM those official bases, installing
the CLI modules, an AI coding agent, DB clients, and the test harness.
“Measured need” applies to extra customization beyond that producer,
not to whether the GHCR image exists.

Optimize for low idle memory and fast cold start, and validate the
empty-site footprint on a constrained Linux test environment before
schema work. Model data in Postgres with real relational and
hierarchical structures rather than freeform documents.

### 5. API strategy: v3 for writes, Grapple for reads

**Decision:**

- **Wagtail v3 API** (Django Ninja, opt-in preview in 8.0) is the
  native read-write path for automation: authenticated create, edit,
  publish, unpublish, move, copy, revert, and revision management, with
  OpenAPI schema and bearer-token auth.
- **wagtail-grapple** is the maintained read-oriented GraphQL option
  for frontends and static generators.
- The legacy v2 API remains for simple read-only static generation.
- Low-level approval workflows remain in the source-control system;
  high-level status can be mirrored into Wagtail via the v3 API.

### 6. Frontend: hybrid Django templates plus Next.js

**Decision:** Use Django templates for content-mostly sites with
progressive enhancement (small React/TypeScript islands via Stimulus or
htmx). Use **Next.js** for sites needing heavy interactivity or pure
static generation, pulling content from Wagtail through the v3 or
Grapple APIs at build time.

### 7. Agent control and root-cause discipline

**Decision:** Root-cause rules live in a shared playbook the CLI ships,
with per-repo overrides in each AGENTS.md. Agents must diagnose before
patching and prefer fixing the root cause rather than applying
workarounds. Wagtail’s built-in AI integration (local and online
models) may be used for content generation, review, and enhancement.

---

## Alternatives considered

| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| **Wagtail** | BSD license, zero cost, no paywalls; schema-first relational modeling; StreamFields; multi-site; v3 read-write API; low memory; mature admin | Weaker native GraphQL writes than a code-first CMS | **Selected** as default CMS |
| **Directus v12** | Schema-first; official images; low idle memory; strong APIs | Source-available license with key enforcement, collection/flow/seat caps, paywalled SSO/offline/telemetry | Not selected — commercial restrictions conflict with cost-control goals |
| **Payload CMS 3.88** | Code-first TypeScript; tight Next.js integration | Development-time memory spikes; known open issues; never reached production | Not selected this cycle; frozen on standby |
| **Strapi** | Mature; plugin ecosystem | Significant features behind a commercial paywall | Not selected — paywalled core features |
| **Nuxt** | Fine-grained tier control; separable business logic | High development complexity; not a CMS | Not selected as CMS; tier-separation ideas retained |
| **Pure Next.js** | Maximum framework control; no separate CMS | Reimplements schema, admin, API by hand | Not selected — too much custom infrastructure |

---

## Consequences

### Positive

- Zero CMS licensing; safe to recommend to clients.
- No vendor lock-in, no license keys, no telemetry, no collection caps.
- Schema-first relational modeling for complex, deeply hierarchical
  data.
- Native read-write v3 API for automation; Grapple for reads.
- Reusable, optimized producer image for agent-ready development.
- Hybrid frontend supports both content sites and interactive/static
  apps.
- Existing under-structured pages can be restructured into proper
  relational models within the same CMS.

### Trade-offs

- Two instances to operate across business domains.
- GraphQL write support is not native; v3 REST is the write path.
- Some modern DX conveniences of code-first CMS ecosystems are traded
  for license freedom.
- v3 API is a preview and may change before stabilization.

---

## References

- [ADR-0001](0001-xgic-gitlab-architecture-and-repository-naming.md)
- [ADR-0003](0003-docker-compose-first-kubernetes-ready.md)
- [ADR-0005](0005-modular-xgic-cli-and-retirement-of-xde.md)
- [Base standards](../BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)
- [Ecosystem catalog](../ecosystem/catalog.md)
- Public repositories: [xgic/wagtail-cli](https://github.com/xgic/wagtail-cli),
  [xgic/wagtail-dev](https://github.com/xgic/wagtail-dev),
  [xgic/wagtail](https://github.com/xgic/wagtail)
- Intended image: `ghcr.io/xgic/wagtail-dev` (produced by `xgic/wagtail-dev`; not yet published)
