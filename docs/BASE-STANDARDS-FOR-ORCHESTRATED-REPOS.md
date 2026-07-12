# Base Standards for Orchestrated Repos (Public)

**Purpose**: Canonical **public** minimum set of documentation, architecture patterns, and AI collaboration standards for XGIC repositories on GitHub.

**Authority**: This file in [`xgic/ai`](https://github.com/xgic/ai) is the preferred multi-repo citation target. Downstream public repos may keep a short local copy or pointer; prefer linking here to reduce drift.

**Audience**: Maintainers, contributors, and AI coding assistants (including Grok Build).

---

## Hard security (non-negotiable)

**Zero private leakage**: Do not place private repository names, internal hosts/URLs, private tracker IDs, private filesystem paths, credentials, or private coordination structures into any public XGIC repository (files, issues, PRs, commits, comments, or agent output destined for public artifacts).

**Public-safe references only**:

- Use full HTTPS URLs to public GitHub artifacts: `https://github.com/xgic/<repo>/...`
- Same-repo short refs (`#N`) only within that public repository
- Do **not** close or reference private trackers from public PR bodies (no private project IDs)

Violations are security incidents: correct immediately; coordinate remediation privately if needed.

---

## Mandatory human review before `main`

While AI-assisted development tools are used heavily:

- Every change lands on `main` only through a **pull request** with explicit **human** review in the GitHub UI
- Agents prepare complete drafts; agents do **not** approve or merge their own PRs
- “Code review” includes documentation, workflows, and agent instruction files

Enforcement: branch protection (required reviews, no direct pushes to `main`, linear history where practical) + this document + each repo’s `AGENTS.md`.

---

## Minimum base set (every public orchestrated repo)

1. **Hard security rule** (this document and/or local `AGENTS.md`).
2. **GitHub Flow + branch protection** on `main`.
3. **`AGENTS.md`** — collaboration principles, security boundary, session checklist, commit expectations.
4. **`CONTRIBUTING.md`** (root or `.github/CONTRIBUTING.md`) — contributor-facing process without restating entire policy volumes.
5. **`README.md`** — purpose, quick start, links to docs and this hub when multi-repo policy applies.
6. **Docs skeleton** (as applicable):
   - architecture / design overview
   - development or orchestration workflow
   - playbooks for AI-assisted tasks (optional but recommended)
7. **`.gitignore`** covering secrets, virtualenvs, IDE noise, and **`.xgic/`** (local agent status reports; never commit).
8. **Issue / PR templates** that collect useful fields **without** embedding full rule text (point to `AGENTS.md` / this document if a short pointer is needed). Follow [community-health.md](community-health.md): YAML issue forms, `blank_issues_enabled: false`, root `CONTRIBUTING.md` only, Discussions contact links only when enabled.
9. **Python 3.14** for *new* Python development ([ADR-0002](adr/0002-standardize-on-python-3-14.md)):
   - `requires-python = ">=3.14"`
   - Prefer official `python:3.14.6-slim` (or current pinned 3.14 patch) for containers
10. **Conventional Commits**, atomic changes, positive professional tone.
11. **XGIC CLI / environment orchestration** — no new Makefiles. **Pre-cutover:** in-tree **`xde`** where that is still the shipped CLI. **Post full modular migration:** living docs and guidelines refer only to **XGIC CLI** (`xgic.cli.*`); no `xde` in current standards (historical completed artifacts only). See [ecosystem catalog](ecosystem/catalog.md) naming note.
12. **Public package metadata** uses the org-facing author identity (e.g. `XGIC`), never private project names.
13. **Apache License 2.0** for public XGIC solutions ([licensing.md](licensing.md), [ADR-0004](adr/0004-apache-2-0-for-public-solutions.md)).
14. **Docker Compose-first ops docs** for on-prem; Kubernetes path documented when relevant ([ADR-0003](adr/0003-docker-compose-first-kubernetes-ready.md)).
15. **Cite this hub** for multi-repo policy and the [ecosystem catalog](ecosystem/catalog.md) rather than inventing parallel modules.

---

## Commits and pull requests

- Subject: imperative, Conventional Commit type/scope
- Body: explain motivation and impact
- Squash related tiny commits when they form one logical change (unrelated work = separate PRs)
- Prefer `Closes #N` only for **same-repo** public issues
- **Labels (mandatory):** every issue, PR/MR, and GitHub Discussion welcome post must carry proper labels. GitHub: at least the semantic set in [community-health.md](community-health.md) (`bug`, `enhancement`, `documentation`, `standards`, `chore`, `welcome`, …). Welcome Discussions require `welcome` + `documentation`. GitLab: apply project type/priority/process labels (e.g. `type:docs`, `priority:high`). Unlabeled artifacts are incomplete.

---

## AI agent usage (public repos)

- Load the target repo’s `AGENTS.md` first; use this hub for multi-repo standards
- Draft issues/PRs completely; wait for human LGTM before remote create/push/merge when policy requires it
- Run a **leakage scan** before proposing public commits (private hosts, private IDs, internal paths)
- Distill only public-safe, high-value content into the repo; keep raw session data local

---

## Bootstrap checklist (new public repo)

1. Initialize GitHub Flow + protect `main`
2. Add comprehensive `.gitignore` (include `.xgic/`)
3. Add `README.md`, `AGENTS.md`, `CONTRIBUTING.md`
4. Add docs skeleton and CI as needed
5. Link multi-repo policy to `https://github.com/xgic/ai`
6. Human review of the bootstrap PR
7. Register or update the public namespace summary when a new public Python package is introduced

---

## Related hub documents

- [Architecture](architecture.md)
- [Orchestration workflow](orchestration-workflow.md)
- [Grok playbooks](grok-playbooks.md)
- [Python namespace convention](xgic-python-namespace-convention.md)
- [ADR index](adr/README.md)
