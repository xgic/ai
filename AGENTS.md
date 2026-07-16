# AI Agent Instructions — XGIC AI (Public Intelligence Hub)

**Primary context file for AI coding assistants (especially Grok Build) in this repository and when reasoning about the XGIC public ecosystem.**

Read this file before significant work. This hub is **public-facing**: every commit, issue, and PR must remain free of private coordination details.

---

## Mission

Act as the **central public intelligence layer** for the XGIC ecosystem:

| Responsibility | Location |
|----------------|----------|
| Multi-repo standards | `docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md` |
| Ecosystem “what exists” | `docs/ecosystem/catalog.md` |
| Ecosystem “how it fits” | `docs/ecosystem/composition.md` |
| Agent knowledge model | `docs/agent/knowledge-model.md` |
| Platform path (Docker Compose → K8s) | `docs/platform/` |
| Formal decisions | `docs/adr/` |
| Long-term vision | `docs/VISION.md` |

Private strategy and full-fidelity internal coordination are **out of scope** and must never be introduced into this repository. This hub is a **public subset** of broader foundation practice—not a mirror of private systems.

---

## Hard security (absolute)

**Never** place any of the following in this repository (files, issues, PRs, commits, comments, or agent output intended for commit):

- Private repository names, paths, hostnames, or internal URLs
- Private issue / merge-request identifiers from private trackers
- Internal workspace paths, session store paths, or private plan locations
- Credentials, tokens, or environment secrets

**Allowed:**

- High-level abstract wording when necessary (e.g. “private coordination is handled separately”)
- Full HTTPS links to **public** GitHub artifacts (`https://github.com/xgic/...`)
- Same-repo short refs (`#N`) for issues/PRs **in this public repository only**

Violations are security incidents: stop, sanitize, and correct before merge.

---

## Agent intelligence protocol

Before recommending a library, CLI module, image, or app pattern:

1. **Load catalog** — `docs/ecosystem/catalog.md` (status: available / planned / experimental).
2. **Load composition** — `docs/ecosystem/composition.md` (allowed pairings and anti-patterns).
3. **Load knowledge model** — `docs/agent/knowledge-model.md` (entities, edges, recommendation rules).
4. **Check ADRs** — especially runtime (0002), naming (0001), platform path (0003), licensing (0004).
5. **Prefer existing modules** over inventing parallel namespaces or repos.
6. **Deployment default** — Docker Compose for on-prem; Kubernetes only when scale/HA/multi-cluster needs are explicit.
7. **License** — Apache 2.0 for XGIC public solutions; do not introduce conflicting license assumptions.

When uncertain whether a component exists publicly, say so and point to the catalog “planned” rows rather than inventing private details.

---

## Collaboration principles

- **Positive, constructive, professional** tone; forward-looking documentation.
- **GitHub Flow**: short-lived branches named with the issue number (e.g. `3-world-class-ecosystem-hub`).
- **Human review gate**: agents prepare complete drafts; humans review and approve in the GitHub UI before merge to `main`. Agents never approve or merge their own PRs.
- **Conventional Commits**: `type(scope): subject` plus a body explaining *what* and *why*.
- **Atomic changes**: include relevant doc updates in the same commit when they are part of the change.
- **Labels (mandatory):** apply proper labels to every issue, PR, and Discussion welcome post before considering the artifact complete. Welcome posts: `welcome` + `documentation`. See [docs/community-health.md](docs/community-health.md).
- **Rule text lives in standards docs** (this file, base standards). Do not restate full rule procedures in issue/PR templates.

---

## Session startup checklist

1. `git status -sb` and confirm branch / remote  
2. Read this file, `README.md`, and `docs/agent/knowledge-model.md`  
3. Skim `docs/ecosystem/catalog.md` for the domains you will touch  
4. List open issues/PRs: `gh issue list`, `gh pr list`  
5. Confirm the change is **public-safe** (hard security scan)  
6. Prefer full `https://github.com/xgic/...` URLs for cross-repo links  

---

## What to edit where

| Change type | Primary location |
|-------------|------------------|
| New/updated public component | `docs/ecosystem/catalog.md` (+ composition if fit patterns change) |
| Agent recommendation rules | `docs/agent/` |
| Multi-repo standards | `docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md` |
| Platform / ops guidance | `docs/platform/` |
| Architecture decisions | `docs/adr/` (new ADR + index) |
| Vision / roadmap framing | `docs/VISION.md` |
| Python packages map | `docs/xgic-python-namespace-convention.md` |
| Python package release (PyPI) | `docs/python-package-release.md` |
| Hub orientation | `README.md`, this file, `CONTRIBUTING.md` |

Downstream public repositories should **link** here rather than copy large policy blocks.

---

## Status reports (optional, local only)

- Session ID: `XGIC AI`  
- Write only under `.xgic/grok-build/` (gitignored; never commit)  
- Structure: `docs/templates/status-report-template.md`  

---

## References

- [Vision](docs/VISION.md)  
- [Ecosystem catalog](docs/ecosystem/catalog.md)  
- [Composition guide](docs/ecosystem/composition.md)  
- [Agent knowledge model](docs/agent/knowledge-model.md)  
- [Platform overview](docs/platform/overview.md)  
- [Base standards](docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)  
- [ADR index](docs/adr/README.md)  
