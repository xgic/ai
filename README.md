# XGIC AI

**Public multi-repository standards, architecture decision records (ADRs), and orientation hub** for XGIC open-source work on GitHub.

This repository is the shared reference for humans and AI coding assistants (including [Grok Build](https://x.ai/)) when working across XGIC’s public libraries, CLIs, dev-container producers, templates, and related OSS. It is intentionally **public-safe**: high-level standards and decisions only—no private coordination details.

## Why this hub exists

| Need | How this repo helps |
|------|---------------------|
| Shared ADRs | Single place for multi-repo architecture decisions |
| Python namespace map | Discover `xgic.*` packages and planned CLIs |
| Consistent process | Canonical public base standards for orchestrated repos |
| Agent onboarding | `AGENTS.md` + playbooks for productive sessions |
| Cross-repo links | Stable HTTPS URLs other public repos can cite |

## Quick navigation

| Document | Purpose |
|----------|---------|
| [AGENTS.md](AGENTS.md) | Instructions for AI coding assistants working in or referencing this hub |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to propose standards, ADRs, and doc improvements |
| [docs/architecture.md](docs/architecture.md) | Mental model of the public multi-repo landscape |
| [docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md) | **Canonical** public base standards for XGIC GitHub repos |
| [docs/orchestration-workflow.md](docs/orchestration-workflow.md) | GitHub Flow, commits, PRs, and agent workflows |
| [docs/grok-playbooks.md](docs/grok-playbooks.md) | Step-by-step playbooks for common AI-assisted tasks |
| [docs/xgic-python-namespace-convention.md](docs/xgic-python-namespace-convention.md) | Public Python namespace registry (summary) |
| [docs/adr/](docs/adr/) | Architecture decision records |

## Public repository map (current)

| Repository | Role |
|------------|------|
| [xgic/ai](https://github.com/xgic/ai) | **This hub** — multi-repo standards & ADRs |
| [xgic/gitlab-graphql](https://github.com/xgic/gitlab-graphql) | Python GraphQL client (`xgic.gitlab.graphql`) |
| [xgic/gitlab](https://github.com/xgic/gitlab) | GitLab EE orchestration / template surface |
| [xgic/payload-cms-dev-containers](https://github.com/xgic/payload-cms-dev-containers) | VS Code dev-container + Payload CMS tooling (`xde`) |

Additional libraries and CLI modules are planned under the [namespace convention](docs/xgic-python-namespace-convention.md).

## Core principles (summary)

1. **Hard security** — Public artifacts never expose private repository names, hosts, paths, or private tracker IDs.
2. **GitHub Flow** — Short-lived branches; merge to `main` only via reviewed pull requests.
3. **Human review** — AI agents prepare drafts; humans approve in the GitHub UI before merge to `main`.
4. **Python 3.14** for new development — see [ADR-0002](docs/adr/0002-standardize-on-python-3-14.md).
5. **XGIC CLI / xde** — Prefer shared CLI tooling; no new Makefiles in new or modernized repos.
6. **Conventional Commits** — Detailed, reviewable history.

## For AI agents

1. Read [AGENTS.md](AGENTS.md) completely before making changes here.
2. Prefer **full HTTPS URLs** when linking to other public GitHub artifacts from any tracker or doc.
3. Cite this hub from other public repos instead of duplicating multi-repo policy text.
4. Keep all contributions public-safe (see hard security rule in base standards).

## License

See [LICENSE](LICENSE).
