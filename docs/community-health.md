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

Use GitHub's own label names. Do not put scoped labels such as
`type::`, `priority::`, or `workflow::` on a public repository, and do
not invent unscoped process labels.

**Create** these type labels on every public XGIC GitHub repository if
missing. Names and colors are exact:

| Label | Color | Use |
|-------|-------|-----|
| `bug` | `d73a4a` | A defect |
| `enhancement` | `a2eeef` | A feature or improvement |
| `documentation` | `0075ca` | Product documentation only |
| `standards` | `5319e7` | Standards, policy, or community health |
| `chore` | `fef2c0` | Maintenance, templates, or hygiene |
| `welcome` | `0e8a16` | Welcome Discussion posts only |
| `question` | `d876e3` | A question. Prefer Discussions when enabled |

Every **issue** and **pull request** has **exactly one** type label,
chosen from `bug`, `enhancement`, `documentation`, `standards`, and
`chore`. Apply it in the same `gh issue create` or `gh pr create` call
that opens the artifact, then confirm it with `gh issue view` or
`gh pr view`. An artifact with no type label, or with two type labels,
is not complete.

A welcome Discussion post is the only artifact that carries two labels:
`welcome` and `documentation`. Any other Discussion carries exactly one
of `question`, `enhancement`, `documentation`, or `standards`.

Optional labels do not replace the type label. Use at most one of
`priority:high`, `priority:medium`, or `priority:low`, and only when
the scheduling difference matters. `good first issue` and `help wanted`
may be added for contributors.

YAML issue forms set that one type label in the form `labels:` field.

### Private GitLab

Private GitLab uses its own scoped taxonomy. Do not copy these GitHub
names onto private work items, and do not copy that private taxonomy
onto GitHub.

### Enforcement

- Agents and humans refuse to treat an artifact as complete until the
  one type label is present.
- Welcome Discussion posts are created with `welcome` and
  `documentation` in the same change. If the API cannot set labels at
  create, apply them before any other work.
- A standards change uses `standards` only. It does not also carry
  `documentation`.

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

- **Issue first** for bugs, features, DX, and standards (see [work-tracking-and-checklists.md](work-tracking-and-checklists.md)); then open the PR  
- Dedicated branch named with the tracking issue number  
- PR to `main` with human review in the GitHub UI; body uses `Fixes #N` / `Tracks #N`  
- Conventional Commits  
- Public-safe content only  
- Issue and PR labels (and assignee) applied; a publishing repository uses the `X.Y.Z` release milestone  
- PR labels applied before merge  

## Related

- [BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)
- [AGENTS.md](../AGENTS.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
