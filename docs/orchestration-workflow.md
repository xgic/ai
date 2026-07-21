# Orchestration workflow (public)

Practical workflow for humans and AI agents working on XGIC public GitHub repositories, including this hub.

## Core principles (deployments)

- **Deployment quality (every environment):** lab, staging, production, and hybrid/cloud deploys must be **idempotent**, **reliable**, and **reproducible**. Full policy: [BASE-STANDARDS — Deployment quality attributes](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md#deployment-quality-attributes-mandatory--every-environment). Docker Compose defaults: [platform/docker-compose.md](platform/docker-compose.md).

## Branching

- Default branch: **`main`** (always releasable / publishable documentation or software)
- One issue → one short-lived branch
- Branch names include the issue number: `1-enhance-public-hub`, `feat/12-short-description`
- Delete the feature branch after the PR merges

## Local loop

1. Sync `main`
2. Create branch from `main`
3. Implement + verify (docs read-through, tests/lint when code exists)
4. Commit with Conventional Commits
5. Push branch and open a PR
6. Human review in GitHub UI → merge

## Agent loop (Grok Build–style)

1. **Startup**: status, remotes, open issues/PRs, read `AGENTS.md`
2. **Plan**: confirm scope stays public-safe
3. **Draft**: complete issue/PR bodies before creating remote artifacts when required by project policy
4. **Implement** on a dedicated issue branch
5. **Scan**: hard-security / leakage check
6. **Pause** for human review and merge

## Linking conventions

| Context | Form |
|---------|------|
| Same public repo | `#12`, `Closes #12` |
| Other public GitHub repo | Full URL: `https://github.com/xgic/<repo>/pull/18` |
| Multi-repo standards | Link `https://github.com/xgic/ai` docs paths |

## Documentation updates

When behavior or process changes:

- Update the owning repo’s docs in the **same PR** when possible
- Promote cross-cutting decisions into this hub (ADR or base standards) rather than leaving them only in chat

## Environment orchestration

For dev containers and related tooling:

- Prefer **XGIC CLI** modules (`xgic` / `xgic.cli.*`) over new Makefiles
- Keep scripts small; put logic in tested libraries when growth warrants it

## Related

- [Base standards](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)
- [Grok playbooks](grok-playbooks.md)
