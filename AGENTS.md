# AI Agent Instructions — XGIC AI (Public Hub)

**Primary context file for AI coding assistants (especially Grok Build) in this repository.**

Read this file before significant work. This hub is **public-facing**: every commit, issue, and PR must remain free of private coordination details.

---

## Mission

Provide a single, durable public source of truth for:

- Multi-repo architecture decisions (ADRs)
- Python namespace and package orientation
- Public base standards for orchestrated XGIC GitHub repositories
- Agent-friendly workflows and playbooks

Private strategy, private repository inventories, and full-fidelity internal coordination are **out of scope** here and must never be introduced into this repository.

---

## Hard security (absolute)

**Never** place any of the following in this repository (files, issues, PRs, commits, comments, or agent output intended for commit):

- Private repository names, paths, hostnames, or internal URLs
- Private issue / merge-request identifiers or cross-project refs from private trackers
- Internal workspace paths, session IDs, or private plan locations
- Credentials, tokens, or environment secrets

Allowed:

- High-level, abstract wording when necessary (e.g. “private coordination is handled separately”)
- Full HTTPS links to **public** GitHub artifacts (`https://github.com/xgic/...`)
- Same-repo short refs (`#N`) for issues/PRs **in this public repository only**

Violations are security incidents: stop, sanitize, and correct before merge.

---

## Collaboration principles

- **Positive, constructive, professional** tone. Forward-looking documentation.
- **GitHub Flow**: work on short-lived branches named with the issue number (e.g. `1-enhance-public-hub`).
- **Human review gate**: agents prepare complete drafts; humans review and approve in the GitHub UI before merge to `main`. Agents never approve or merge their own PRs.
- **Conventional Commits**: `type(scope): subject` plus a body explaining *what* and *why*.
- **Atomic changes**: include relevant doc updates in the same commit when they are part of the change.
- **Rule text lives in standards docs** (this file, `docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md`). Do not restate full rule procedures in issue/PR templates.

---

## Session startup checklist

1. `git status -sb` and confirm branch / remote
2. Read this file, `README.md`, and the docs index
3. List open issues/PRs: `gh issue list`, `gh pr list`
4. Confirm the change is **public-safe** (hard security scan)
5. Prefer linking other public repos with full `https://github.com/xgic/...` URLs

---

## What to edit where

| Change type | Primary location |
|-------------|------------------|
| Multi-repo standards | `docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md` |
| Architecture overview | `docs/architecture.md` |
| Workflow / GitHub Flow | `docs/orchestration-workflow.md` |
| Agent playbooks | `docs/grok-playbooks.md` |
| Python packages map | `docs/xgic-python-namespace-convention.md` |
| Architecture decisions | `docs/adr/` (new ADR + index update) |
| Hub orientation | `README.md`, this file, `CONTRIBUTING.md` |

Downstream public repositories should **link** here rather than copy large policy blocks, then adopt changes via their normal PR process.

---

## Status reports (optional, local only)

If generating a Grok Build session status report for work on this hub:

- Session ID: `XGIC AI`
- Write only under `.xgic/grok-build/` (gitignored; never commit)
- Use `docs/templates/status-report-template.md` as the structure

---

## References

- [Base standards](docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)
- [Architecture](docs/architecture.md)
- [Orchestration workflow](docs/orchestration-workflow.md)
- [Grok playbooks](docs/grok-playbooks.md)
- [ADR index](docs/adr/README.md)
