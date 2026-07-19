# XGIC documentation style (public summary)

**Status:** Living public pointer  
**Date:** 2026-07-18  

Full portfolio style rules for Markdown (including private coordination docs) live in the private XGIC Foundation style guide. This page is the **public-safe** summary for open-source repositories.

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

## Application

- Apply on **new and edited** files; no required mass rewrite of history  
- Public content remains **public-safe** only ([BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md))  
- Labels remain mandatory ([community-health.md](community-health.md))  

### Public GitHub hygiene (mandatory)

Public issues, pull requests, Discussions, and comments must **never** include:

- Private GitLab hosts or URLs  
- Private tracker paths or IDs from private coordination systems  
- Private local filesystem paths as required documentation  

Cross-repository links on public GitHub use full `https://github.com/xgic/...` URLs only. When private coordination exists, use only a high-level phrase such as: “Private portfolio coordination is tracked only in the private XGIC Foundation (org members only).” Do not link or number private work items from public surfaces.

## Related

- [community-health.md](community-health.md)  
- [BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)  
- [python-package-release.md](python-package-release.md)  
