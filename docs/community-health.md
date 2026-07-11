# Community health standard (XGIC public repositories)

**Canonical public standard** for GitHub issue templates, Discussions, and repository-local community health files.  
Coordinating issue: https://github.com/xgic/ai/issues/5

## Single rules

| Topic | Rule |
|-------|------|
| Contributing guide | **Always** root `CONTRIBUTING.md` (`https://github.com/xgic/<REPO>/blob/main/CONTRIBUTING.md`). Do not use `.github/CONTRIBUTING.md`. |
| Issue forms | Prefer **YAML Issue Forms** under `.github/ISSUE_TEMPLATE/`. |
| Blank issues | `blank_issues_enabled: false` in `config.yml`. |
| Contact links | Only real, existing URLs. Contributing → root `CONTRIBUTING.md`. Discussions → only after Discussions is enabled. |
| Discussions | Enable on public / soon-to-be-public repos; pin a professional welcome post; questions/ideas in Discussions; bugs/features in Issues. |
| Multi-repo policy | **Link** [xgic/ai](https://github.com/xgic/ai) (BASE-STANDARDS, ADRs, catalog). Do **not** fork large hub policy into product repos. |
| License | Apache-2.0 for XGIC public solutions ([ADR-0004](adr/0004-apache-2-0-for-public-solutions.md)). |
| Cross-repo refs | Full HTTPS URLs (e.g. `https://github.com/xgic/ai/issues/5`). Never bare `#N` for another repository. |

## Repository-local (required) vs hub (link only)

**Local (each public repo):** root `CONTRIBUTING.md`, `SECURITY.md` when ready, `.github` issue forms, `LICENSE`/`NOTICE` as applicable. Product-specific build/test/PR steps live here.

**Hub only (link):** multi-repo BASE-STANDARDS, ADRs, ecosystem catalog, agent knowledge model, platform vision.

## Recommended `config.yml`

```yaml
blank_issues_enabled: false
contact_links:
  - name: Contributing Guidelines
    url: https://github.com/xgic/<REPO>/blob/main/CONTRIBUTING.md
    about: Please read our contribution guidelines before opening an issue.
  - name: Discussions
    # Add only after Discussions is enabled for this repository
    url: https://github.com/xgic/<REPO>/discussions
    about: Ask questions and share ideas here (not for bugs or tracked feature work).
```

## Minimum issue forms

At least:

- Bug report (YAML form)
- Feature request (YAML form)

Hub may add domain-specific forms (e.g. documentation/standards).

## GitHub Flow

- Dedicated branch named with the tracking issue number
- PR to `main` with human review in the GitHub UI
- Conventional Commits
- Public-safe content only

## Related

- [BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)
- [AGENTS.md](../AGENTS.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
