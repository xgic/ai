# XGIC documentation style (public summary)

**Status:** Living public pointer  
**Date:** 2026-07-19  

This page is the **public** documentation-style summary for open-source repositories. Broader portfolio style rules that are not public-safe stay out of public surfaces.

## Headings

- ATX style (`#` … `####`); one H1; do not skip levels  
- **Sentence case** only: first word + proper nouns / product names; acronyms stay uppercase  
  - Prefer `## Getting started`, `## Docker Compose lifecycle`  
  - Avoid Title Case for ordinary words (`## Getting Started`)  

## Terminology

| Topic | Use | Avoid |
|-------|-----|--------|
| Compose product | **Docker Compose** | Bare “Compose” |
| GitLab edition | **GitLab Enterprise Edition** or **GitLab EE** | Bare “EE” |
| Our GitLab ops CLI | **XGIC GitLab CLI**, `xgic-gitlab-cli`, `xgic/gitlab-cli` | Bare `gitlab-cli` (confusion with official **`glab`**) |
| GraphQL library | **XGIC GitLab GraphQL Client**, `xgic-gitlab-graphql` | Ambiguous short names |

## Source formatting

- Soft-wrap **new/edited** prose at ~80–100 characters for diffs  
- Do not wrap URLs, headings, tables, or fenced code  
- Language-tagged fenced code blocks; descriptive link text; image alt text  
- Prefer Mermaid for diagrams  

## Public README headers

On **substantial** updates to a public OSS `README.md`, place a functional badge row directly under the H1:

- Shields.io `flat` or `flat-square`; about **4–10** badges  
- Typical set: license, CI status, PyPI or GitHub Release version, Python (or primary runtime)  
- Clickable destinations; meaningful alt text; blank line before the description  
- Prefer pure Markdown; no decorative badge spam  

Private or confidential projects use a different profile (no misleading public OSS badges). Details live in the private portfolio style guide; public repos follow this public summary and [BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md).

Reference package READMEs (after updates): [xgic/cli](https://github.com/xgic/cli), [xgic/gitlab-graphql](https://github.com/xgic/gitlab-graphql).

## Application

- Apply on **new and edited** files; no required mass rewrite of history  
- Public content remains **public-safe** only ([BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md))  
- Labels remain mandatory ([community-health.md](community-health.md))  

### Public GitHub hygiene (mandatory)

Public issues, pull requests, Discussions, and comments must **never** include:

- Private hosts or URLs  
- Private tracker paths, IDs, or private hub/repository names  
- Private local filesystem paths as required documentation  
- Restated portfolio hard-security rules (those belong only in dedicated rule documents such as [BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md) and root `AGENTS.md`)  

Cross-repository links on public GitHub use full `https://github.com/xgic/...` URLs only. When work is coordinated privately, **omit** that coordination from public project artifacts entirely—do not substitute a phrase that names private systems.

## Related

- [community-health.md](community-health.md)  
- [BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)  
- [python-package-release.md](python-package-release.md)  

