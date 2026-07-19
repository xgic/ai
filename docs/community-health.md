# Community health standard (XGIC public repositories)

**Canonical public standard** for GitHub issue templates, Discussions, labels, and repository-local community health files.  
Coordinating issue: https://github.com/xgic/ai/issues/5

## Single rules

| Topic | Rule |
|-------|------|
| Contributing guide | **Always** root `CONTRIBUTING.md` (`https://github.com/xgic/<REPO>/blob/main/CONTRIBUTING.md`). Do not use `.github/CONTRIBUTING.md`. |
| Issue forms | Prefer **YAML Issue Forms** under `.github/ISSUE_TEMPLATE/`. |
| Blank issues | `blank_issues_enabled: false` in `config.yml`. |
| Contact links | Only real, existing URLs. Contributing → root `CONTRIBUTING.md`. Discussions → only after Discussions is enabled. |
| Discussions | Enable on public / soon-to-be-public repos; pin a professional welcome post; questions/ideas in Discussions; bugs/features in Issues. |
| **Labels (required)** | **Every** GitHub and GitLab project artifact that supports labels must carry **proper, consistent labels** (see [Labels](#labels-required)). This includes issues, pull requests / merge requests, and **GitHub Discussion welcome posts**. |
| **Markdown style** | New/edited public Markdown follows [documentation-style.md](documentation-style.md): **sentence-case** headings; **Docker Compose** and **GitLab EE** full names; soft prose wrap for new content. |
| Multi-repo policy | **Link** [xgic/ai](https://github.com/xgic/ai) (BASE-STANDARDS, ADRs, catalog). Do **not** fork large hub policy into product repos. |
| License | Apache-2.0 for XGIC public solutions ([ADR-0004](adr/0004-apache-2-0-for-public-solutions.md)). |
| Cross-repo refs | Full HTTPS URLs (e.g. `https://github.com/xgic/ai/issues/5`). Never bare `#N` for another repository. |

## Labels (required)

Labels are mandatory for discoverability, triage, and agent/human automation. Unlabeled artifacts are incomplete.

### GitHub (issues, pull requests, Discussions)

**Create** these labels on every public XGIC GitHub repository if missing (names are exact):

| Label | Color (suggested) | Use |
|-------|-------------------|-----|
| `bug` | `d73a4a` | Defects |
| `enhancement` | `a2eeef` | Features / improvements |
| `documentation` | `0075ca` | Docs-only work |
| `standards` | `5319e7` | Standards / policy / community health |
| `chore` | `fef2c0` | Maintenance, templates, hygiene |
| `welcome` | `0e8a16` | **Welcome / onboarding Discussion posts** |
| `question` | `d876e3` | Questions (prefer Discussions when enabled) |

Optional but recommended when useful: `good first issue`, `help wanted`, priority-style labels (`priority:high`, etc.) if the repo adopts them consistently.

#### Minimum labels by artifact type

| Artifact | Required labels |
|----------|-----------------|
| Bug issue | `bug` (plus area labels if the repo defines them) |
| Feature / enhancement issue | `enhancement` |
| Documentation issue | `documentation` |
| Standards / community-health issue | `standards` (and `documentation` when docs-only) |
| Pull request | Same semantic labels as the work (e.g. `documentation`, `bug`, `chore`, `standards`) |
| **Welcome Discussion post** | **`welcome`** and **`documentation`** (add `standards` when the post also defines org process) |
| Other Discussions | At least one of: `question`, `enhancement`, `documentation`, `standards` (as appropriate) |

YAML issue forms should set default labels via the form `labels:` field where possible.

### GitLab (issues, merge requests, and related)

Private and public GitLab projects must use the project’s standard label taxonomy consistently (examples used across XGIC orchestration):

| Category | Examples |
|----------|----------|
| Type | `type:docs`, `type:bug`, `type:feature`, `chore`, `type:standards` |
| Priority | `priority:high`, `priority:medium`, `priority:low` |
| Process | `grok`, `review:human-ui`, area labels (`area:wiki`, etc.) as defined |

**Rules:**

- Every new issue and merge request receives **type** (or equivalent) and **priority** when known, before or at creation.
- Do not leave MRs/issues unlabeled after human review completes.
- Prefer the same names already used in that GitLab project; extend the taxonomy deliberately rather than inventing one-off labels per issue.

### Enforcement

- Agents and humans: refuse to treat an artifact as “complete” until required labels are applied.
- Welcome Discussion posts are created or updated **with** `welcome` + `documentation` labels in the same change set when the API allows; otherwise apply labels immediately after create.
- Coordinating issues (e.g. multi-repo standards) use `standards` (and `documentation` / `enhancement` as appropriate).

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

- Bug report (YAML form) — default label `bug`
- Feature request (YAML form) — default label `enhancement`

Hub may add domain-specific forms (e.g. documentation/standards) with default `documentation` / `standards` labels.

## Welcome Discussion template (required structure)

Welcome posts must include:

1. Repo-specific purpose  
2. **Where to post** (Discussions vs Issues)  
3. **Start here** links (root CONTRIBUTING, hub standards as applicable)  
4. **Public safety**  
5. **License** pointer  
6. **Labels:** `welcome` + `documentation` (and `standards` when appropriate)  

## GitHub Flow

- Dedicated branch named with the tracking issue number  
- PR to `main` with human review in the GitHub UI  
- Conventional Commits  
- Public-safe content only  
- PR labels applied before merge  

## Related

- [BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)
- [AGENTS.md](../AGENTS.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
