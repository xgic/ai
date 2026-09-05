# ADR-0007: Headless Wagtail v2 read path for static sites

**Status:** Proposed
**Date:** 2026-09-05
**Scope:** Public-safe extract of a site-level specialization of
[ADR-0006](0006-adopt-wagtail.md) for statically generated front ends
**Does not change:** ADR-0005 (modular CLI) or ADR-0006 (adopt Wagtail)

---

## Context

[ADR-0006](0006-adopt-wagtail.md) adopts Wagtail as the default CMS and
keeps three read/write options:

- Wagtail API v3 for authenticated writes and automation
- wagtail-grapple for GraphQL reads
- Legacy API v2 for simple read-only static generation

Some XGIC sites are **pure static generation** (Next.js `output: 'export'`
or equivalent). The public HTML must not call Wagtail at request time.
For those sites, v2 is the read path. v3 and GraphQL stay available to
the portfolio; they are out of scope for that public read path.

Wagtail 8 can swap `wagtailcore.Page` via `WAGTAIL_PAGE_MODEL`. That
feature is experimental. A static front end never queries the Django
ORM, so a swapped base page is unused cost.

Product StreamField and site copy belong in the **site consumer**, not
in the empty public [xgic/wagtail](https://github.com/xgic/wagtail)
template.

---

## Decision

### 1. Stock page model

Do not set `WAGTAIL_PAGE_MODEL`. Page types subclass
`wagtail.models.Page`.

Do not put StreamFields or orderables on a shared base page. Share
cross-type columns with an abstract mixin only when those columns are
in use (for example per-page SEO after that work is approved).

### 2. Public read API is v2

The static build consumes Wagtail API v2.

Mount stock endpoints `pages`, `images`, and `documents`.

A site may add thin extra JSON reads (live snippets, header/footer/site
settings) beside those viewsets. Do not mount or call v3 or GraphQL
from that site's public front end or static build.

Listings return live objects only.

### 3. Static generation

Build pages at generate time from v2 listing and detail endpoints.
Select templates with typed fetches (`?type=…`) or a small `meta.type`
map. Client components handle interactivity only.

A later publish hook rebuilds the export. The live site does not fetch
Wagtail on each request.

### 4. Concrete types in the consumer

Prefer few concrete page types. Put visual variation in StreamField
blocks. Use extra types when the route has distinct fields (for
example a service card/hero, a contact options list, or an open-source
band that queries snippets). Do not add those models to the public
empty template.

---

## Consequences

### Positive

- Default Wagtail page table and add-on compatibility
- Small, cacheable JSON for SSG
- No experimental page-swap migrations
- Empty public template stays empty

### Trade-offs

- This specialization does not use Grapple or v3 even though ADR-0006
  keeps them for the portfolio
- Mixed-type listings stay thin unless `?type=` is set

---

## References

- [ADR-0006: Adopt Wagtail as the default CMS](0006-adopt-wagtail.md)
- [xgic/wagtail](https://github.com/xgic/wagtail) (empty public template)
- [Wagtail API v2 configuration](https://docs.wagtail.org/en/stable/advanced_topics/api/v2/configuration.html)
- [Custom base page models (experimental)](https://docs.wagtail.org/en/stable/advanced_topics/customization/custom_base_page_models.html)
