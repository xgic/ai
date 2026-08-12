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

### Universal (every public repo)

| Badge | When | Pattern |
|-------|------|---------|
| **License** | Always | Static Apache-2.0 → `LICENSE` |
| **CI** | When Actions exist | `https://github.com/xgic/<repo>/actions/workflows/<file>.yml/badge.svg` |

### By repository type (required sets)

Choose the set that matches the repo’s **primary deliverable**. Do not invent one-off badge layouts.

#### Image producers (`*-dev` that publish GHCR)

**Required (in roughly this order after License):**

| Badge | Purpose | Example |
|-------|---------|---------|
| **Docker image** | Signals “this repo produces a container image” | `[![Docker](https://img.shields.io/badge/Docker-image-blue?logo=docker&logoColor=white)](https://docs.docker.com/)` |
| **GHCR** | Links to the published package page | `[![GHCR](https://img.shields.io/badge/GHCR-<package>--name-blue?logo=github)](https://github.com/users/xgic/packages/container/package/<package-name>)` |
| **Release** | Semver / release discovery | `[![Release](https://img.shields.io/github/v/release/xgic/<repo>)](https://github.com/xgic/<repo>/releases)` |
| **CI** | Build/publish health | Workflow badge (above) |

**Optional on producers:**

| Badge | When to add |
|-------|-------------|
| **Docker Compose** | Producer **ships first-class Compose** used to develop or smoke the image (e.g. [payload-cms-dev](https://github.com/xgic/payload-cms-dev)). |
| Product / runtime (Payload, Python, …) | When it clarifies the stack without crowding the first row |

**Do not** replace the **Docker image** badge with **Docker Compose** on a pure image producer. Compose-first operator experience lives on the **clean template** repo ([ADR-0001](adr/0001-xgic-gitlab-architecture-and-repository-naming.md)).

**Reference producers:**

- [payload-cms-dev](https://github.com/xgic/payload-cms-dev) — image + Compose + GHCR + Release (Compose is first-class in the producer)  
- [gitlab-dev](https://github.com/xgic/gitlab-dev) — image + GHCR + Release (Compose stack lives on [gitlab](https://github.com/xgic/gitlab))

#### Clean templates (consume published image / Compose stack)

**Required:** License, **Docker Compose** (operator surface), **Release** of the **producer** (or image pin badge) when the template pins a published image, CI if present.

**Optional:** Product badge (e.g. GitLab EE, Payload CMS), GHCR link to the **consumed** package.

**Example Compose badge:**

```markdown
[![Docker Compose](https://img.shields.io/badge/Docker-Compose-blue?logo=docker&logoColor=white)](https://docs.docker.com/compose/)
```

#### PyPI libraries / CLI modules

**Required when published:** License, **PyPI**, **Python versions** (or static Python 3.14+), **Release**, CI.

```markdown
[![PyPI](https://img.shields.io/pypi/v/<dist>.svg)](https://pypi.org/project/<dist>/)
[![Python](https://img.shields.io/pypi/pyversions/<dist>.svg)](https://pypi.org/project/<dist>/)
[![Release](https://img.shields.io/github/v/release/xgic/<repo>)](https://github.com/xgic/<repo>/releases)
```

Until the first PyPI release, omit PyPI version badges (they 404 or show “not found”); keep License + CI + static Python if useful.

#### Standards / docs hubs (e.g. `xgic/ai`)

License + docs/ADR/style static badges as needed. Prefer **working** static badges over decorative ones.

### GHCR badge rules

- Link target: `https://github.com/users/xgic/packages/container/package/<package-name>`  
  (user-owned packages under the `xgic` account use `/users/xgic/…`, not `/orgs/xgic/…`).
- Label message is the **package name** (e.g. `payload-cms-dev`, `xgic-gitlab`), not necessarily the repo name.
- Pair GHCR with **Release** for version signal (native GHCR version badges are often unreliable).
- In shields **path-style** badges, encode a hyphen in the message as **double hyphen** (`payload--cms--dev`, `xgic--gitlab`). Prefer `static/v1?label=…&message=…` when multi-hyphen path parsing is fragile.

### Broken badge prevention

**Avoid broken static badge paths:** multi-hyphen messages without encoding (e.g. `badge/docs-style-guide-informational`) parse incorrectly and return **404**. Prefer:

```markdown
[![Style](https://img.shields.io/static/v1?label=docs&message=style%20guide&color=informational)](docs/documentation-style.md)
```

or encode hyphens per [Shields static badge docs](https://shields.io/badges).

Before opening a README PR: open each badge URL in a browser or `curl -I` and confirm **200** (or an intentional “no releases yet” release badge, not a shields parse 404).

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
- [ ] **Badge set matches repo type** (image producer / template / PyPI module / hub)  
- [ ] Image producers include **Docker image + GHCR + Release + CI** (Compose only if first-class on producer)  
- [ ] Badges resolve (no shields 404); GHCR package URL matches the published package name  
- [ ] Full HTTPS links to sibling `xgic/*` repos  
- [ ] AGENTS.md / catalog / BASE-STANDARDS linked  
- [ ] Public-safe scan clean  

---

## Related

- [BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)  
- [community-health.md](community-health.md)  
- [documentation-style.md](documentation-style.md)  
