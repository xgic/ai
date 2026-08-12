# README standards for public XGIC repositories

**Status:** Living  
**Audience:** Maintainers, contributors, AI agents (including Grok Build)  
**Authority:** Prefer this document in [xgic/ai](https://github.com/xgic/ai) over forked copies.

The repository **README** is the first impression for humans and the primary orientation surface for agents. Every public `xgic/*` repository should meet these bars.

---

## Goals

A strong XGIC README:

1. States **what the repo is** and **who it is for** in the first screenful.  
2. Separates **product vision/benefits** from **architecture jargon** (ADRs belong in dedicated sections).  
3. Gives a **Quick start** before long tutorials.  
4. Links **full `https://github.com/xgic/...` URLs** (and PyPI/GHCR where relevant).  
5. Stays **public-safe** ([BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)).  
6. Points agents to **AGENTS.md** and the [ecosystem catalog](ecosystem/catalog.md).

---

## Recommended structure

Adapt by repo type (library, CLI module, image producer, template). Prefer this order:

1. **Title + badges** (license, CI, PyPI/release/GHCR as applicable)  
2. **One-sentence positioning** + audience (human / AI)  
3. **Vision** or **Why this exists** (outcomes, not internal process dumps)  
4. **Quick start** (copy-pasteable; link to deeper guides)  
5. **Features / benefits** (tables welcome)  
6. **Architecture / ecosystem** (dual-repo, modules, diagrams in fenced text)  
7. **XGIC standards** (ADR and hub links—not only in the lede)  
8. **Commands / API**  
9. **Contributing + license**  

### Dual-repo products (`*-dev` + clean template)

Follow [ADR-0001](adr/0001-xgic-gitlab-architecture-and-repository-naming.md):

| Repo | README emphasis |
|------|-----------------|
| `*-dev` producer | Image/GHCR, who should **not** use it for app starts, link to template |
| Clean template | **Optimal app start**, Quick start, image pin, XGIC CLI for humans and agents |

Reference implementations:

- Producer: [payload-cms-dev](https://github.com/xgic/payload-cms-dev)  
- Template: [payload-cms](https://github.com/xgic/payload-cms)  
- CLI modules: [cli](https://github.com/xgic/cli), [dev-cli](https://github.com/xgic/dev-cli), [payload-cms-cli](https://github.com/xgic/payload-cms-cli)  

---

## Badges (shields.io)

| Use | Example pattern |
|-----|-----------------|
| License | Static Apache-2.0 badge |
| CI | `https://github.com/xgic/<repo>/actions/workflows/<file>.yml/badge.svg` |
| PyPI version | `https://img.shields.io/pypi/v/<dist>.svg` |
| GitHub release | `https://img.shields.io/github/v/release/xgic/<repo>` |
| GHCR package | Link badge to package page; pair with **release** badge for version (native GHCR version badges are often unreliable) |

**Avoid broken static badge paths:** multi-hyphen messages without encoding (e.g. `badge/docs-style-guide-informational`) parse incorrectly and return **404**. Prefer:

```markdown
[![Style](https://img.shields.io/static/v1?label=docs&message=style%20guide&color=informational)](docs/documentation-style.md)
```

or encode hyphens per [Shields static badge docs](https://shields.io/badges).

---

## Style

- Sentence case headings ([documentation-style.md](documentation-style.md))  
- Prefer **Docker Compose** (full product name) in operator prose  
- Soft-wrap new prose ~80–100 characters where practical  
- No private hosts, private tracker IDs, financial strategy, or pre-release confidential product lore  

---

## Checklist (README PR)

- [ ] First screen states purpose and audience  
- [ ] Quick start present (or justified absence for pure standards hubs)  
- [ ] Architecture / ADR links not crowding the lede  
- [ ] Badges resolve (no shields 404)  
- [ ] Full HTTPS links to sibling `xgic/*` repos  
- [ ] AGENTS.md / catalog / BASE-STANDARDS linked  
- [ ] Public-safe scan clean  

---

## Related

- [BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)  
- [community-health.md](community-health.md)  
- [documentation-style.md](documentation-style.md)  
