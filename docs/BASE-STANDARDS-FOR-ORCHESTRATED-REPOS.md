# Base Standards for Orchestrated Repos (Public)

**Purpose**: Canonical **public** minimum set of documentation, architecture patterns, and AI collaboration standards for XGIC repositories on GitHub.

**Authority**: This file in [`xgic/ai`](https://github.com/xgic/ai) is the preferred multi-repo citation target. Downstream public repos may keep a short local copy or pointer; prefer linking here to reduce drift.

**Audience**: Maintainers, contributors, and AI coding assistants (including Grok Build).

---

## Hard security (non-negotiable)

**Zero private leakage**: Do not place private repository names, internal hosts/URLs, private tracker IDs, private filesystem paths, credentials, or private coordination structures into any public XGIC repository (files, **tests**, issues, **PR/issue/Discussion bodies and comments**, commits, package metadata, or agent output destined for public artifacts).

**Public-safe references only**:

- Use full HTTPS URLs to public GitHub artifacts: `https://github.com/xgic/<repo>/...`
- Same-repo short refs (`#N`) only within that public repository
- Do **not** name private hubs, private repository identities, private hosts, or private trackers on public surfaces—including in “safe” summary phrases
- Do **not** close or reference private trackers from public PR bodies
- Do **not** spell real private hostnames or private tracker paths—even as “forbidden examples”—on public surfaces
- When work is coordinated privately, **omit** that coordination from public artifacts entirely (no substitute phrase that names private systems)

**Configuration over hard-coding (mandatory for production code and tests):**

- Hosts, base URLs, project/namespace paths, user IDs, tokens, and similar environment-specific values must come from **configuration or environment variables** (or explicit test fixtures with **synthetic** names).
- **Unit tests** use only fictional placeholders (e.g. `example-group/example-project`, `gid://gitlab/User/1001`).
- **Integration tests** (opt-in) read live targets from env (e.g. `GITLAB_URL`, `GITLAB_TOKEN`, `GITLAB_TEST_NAMESPACE_PATH`) and must target a **dedicated non-production** instance/project—never production coordination projects.
- Do not hard-code private usernames, production project paths, or real credential material in source, tests, or docs.

**Project artifacts vs rule documents:**

- **Project artifacts** (PR/issue/Discussion bodies, release notes, commit messages meant for product history): describe the technical change only. Do **not** restate portfolio hard-security rules or name private coordination systems.
- **Rule documents** (this file, `AGENTS.md`, and linked public standards): hold the rules. Agents and humans follow them; they do not copy rule prose into every PR.

**Pre-publish checklist** (every public PR/issue body, comment, and commit message):

1. No private hosts / internal URLs  
2. No private tracker IDs, private work-item links, or private hub/repository names  
3. No private local paths  
4. No restated portfolio rules (rules live in dedicated documents only)  
5. Labels applied  
6. No financial goals, revenue targets, or private business-strategy language  
7. No pre-release product or client-confidential marketing/lore content unless that content has already been approved for public release  

**Financial and business strategy:** Public repositories must not document revenue targets, income goals, pricing strategy, commercial partnership terms, GTM pipeline numbers, or other private business strategy. Keep that class of content in private planning systems only.

**Pre-release product confidentiality:** Public repositories and public websites must not disclose pre-release product details (unreleased lore, mechanics, working titles, roadmaps, franchise plans, unreleased media, and similar) unless approved for public release through the proper human approval workflow. Until an official public product site is live and content is authorized, treat unreleased product information as confidential. Public engineering docs may describe **generic** platform capabilities only.

---

**Mandatory before `gh issue create|edit`, `gh pr create|edit`, or any public comment** (agent and human gate — do not skip):

1. Draft offline; scan for private hostnames, private DNS zones, private project paths, private tracker issue/MR numbers, and real operator identities.  
2. Replace with **fictional placeholders only** (e.g. `https://gitlab.example.com`, `group/project`, `TOKEN`).  
3. Prefer describing defects generically (“self-hosted instance missing field X”) over naming any private deployment.  
4. Re-scan the **final** body after any edit.  
5. If a leak was published: **sanitize immediately** (edit/delete), then treat as a security incident—without restating the private values on public surfaces.  

Optional helper (generic patterns only; no private host denylist in public trees): `scripts/public-safe-scan.py` in this hub (or a local copy). Prefer running it on a draft file before `gh` create/edit.

Violations are security incidents: correct immediately. Do not re-leak private names, hosts, or tracker URLs while describing the fix on public GitHub.

---

## README quality (first impression)

Every public repository **README** should meet [readme-standards.md](readme-standards.md): clear positioning for humans and AI, Quick start before long tutorials, dual-repo clarity where applicable, working badges, and public-safe full HTTPS links.

## Mandatory human review before `main`

While AI-assisted development tools are used heavily:

- Every change lands on `main` only through a **pull request** with explicit **human** review in the GitHub UI
- Agents prepare complete drafts; agents do **not** approve or merge their own PRs
- “Code review” includes documentation, workflows, and agent instruction files

Enforcement: branch protection (required reviews, no direct pushes to `main`, linear history where practical) + this document + each repo’s `AGENTS.md`.

---

## Deployment quality attributes (mandatory — every environment)

**Deployments to any environment** (contributor workstation, lab, staging, production, edge/hybrid, and cloud) **must follow current best practices**, including **idempotency**, **reliability**, and **reproducibility**. This applies to application stacks, platform services, infrastructure-as-code, container images, and CI/CD deploy paths.

| Attribute | Requirement |
|-----------|-------------|
| **Idempotency** | Re-running install, configure, or deploy converges to the same desired state without duplicate resources, partial drift, or “only works once” steps. Prefer declarative config and safe automation modules over one-shot shell. |
| **Reliability** | Safe defaults (dry-run / confirm for destructive ops); health and readiness probes where the platform provides them; explicit failure modes; restart policies; human review gates for production-affecting mutations; backups proven before cutover. |
| **Reproducibility** | Pinned image/tag and runtime versions; configuration via env/config files—not hard-coded in application code; the same documented procedure produces the same outcome across operators and machines; document version-match rules for restore/migrate when applicable. |

**Also required:**

- Prefer **configuration over hard-coding** hosts, URLs, paths, and secrets.
- Prefer **official vendor images** and thin orchestration (configure/operate; do not fork application images).
- Prefer **Docker Compose** for on-prem/lab defaults with a clear path to Kubernetes when scale requires it ([ADR-0003](adr/0003-docker-compose-first-kubernetes-ready.md)).
- Fix **root causes** rather than committing environment-specific host-file workarounds into shared automation.

**Enforcement:** Each orchestrated repo’s `AGENTS.md` and workflow docs; dry-run defaults for destructive automation; PR review for hard-coded topology and non-idempotent one-shots; human UI review before production deploys.

Public platform detail: [platform/docker-compose.md](platform/docker-compose.md), [orchestration-workflow.md](orchestration-workflow.md).

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
7. **`.gitignore`** covering secrets, virtualenvs, IDE noise, build/temp dirs, and **`.xgic/`** (local agent status reports; never commit). See **Temporary-file lifecycle** below.
8. **Issue / PR templates** that collect useful fields **without** embedding full rule text (point to `AGENTS.md` / this document if a short pointer is needed). Follow [community-health.md](community-health.md): YAML issue forms, `blank_issues_enabled: false`, root `CONTRIBUTING.md` only, Discussions contact links only when enabled.
9. **Python 3.14** for *new* Python development ([ADR-0002](adr/0002-standardize-on-python-3-14.md)):
   - `requires-python = ">=3.14"`
   - Prefer official `python:3.14.6-slim` (or current pinned 3.14 patch) for containers
9a. **Dual-mode Python development environments:**
   - **Applications / services** that match Linux container runtime or production: use a **VS Code Dev Container** (or the project’s documented Linux container workflow) as the development source of truth. Do not treat a host OS virtualenv as the primary environment for those projects.
   - **Pure Python libraries and CLI packages** with no hard Linux-only dependencies: use **`uv`** for install, lock, and local development. Open the **library repository folder** as the VS Code workspace for Python tooling so a parent multi-folder workspace does not auto-activate a nested project `.venv` in unrelated terminals.
   - Prefer gitignoring `.venv` / `.venv*`. Prefer [python-package-release.md](python-package-release.md) clean-env smoke patterns over long-lived disposable envs under multi-folder workspace roots.
   - Rationale (technical): Dev Containers reproduce CI/prod Linux dependencies; `uv` is fast and lockfile-friendly for pure packages; automatic nested-venv activation in a multi-folder parent workspace pollutes orchestration shells with the wrong environment.
10. **Conventional Commits**, atomic changes, positive professional tone.
11. **XGIC CLI / environment orchestration** — no new Makefiles. Living docs and guidelines refer only to **XGIC CLI** (`xgic` / `xgic.cli.*`); no `xde` in current standards (historical completed artifacts only). Public template is a modular CLI consumer. See [ecosystem catalog](ecosystem/catalog.md) naming note.
12. **Public package metadata** uses the org-facing author identity (e.g. `XGIC`), never private project names.
13. **Apache License 2.0** for public XGIC solutions ([licensing.md](licensing.md), [ADR-0004](adr/0004-apache-2-0-for-public-solutions.md)).
14. **Docker Compose-first ops docs** for on-prem; Kubernetes path documented when relevant ([ADR-0003](adr/0003-docker-compose-first-kubernetes-ready.md)).
15. **Cite this hub** for multi-repo policy and the [ecosystem catalog](ecosystem/catalog.md) rather than inventing parallel modules.
16. **Public Python packages (PyPI):** when a public repo publishes to PyPI, it **must** follow [python-package-release.md](python-package-release.md): clean-env install matrix on packaging PRs; RC → TestPyPI + smoke; final → PyPI via **OIDC Trusted Publishing** and **`pypa/gh-action-pypi-publish` only**; **`uv`** for build and install smoke; no long-lived PyPI tokens for routine releases; no laptop publishes for official releases.

---

## Commits and pull requests

- Subject: imperative, Conventional Commit type/scope
- Body: explain motivation and impact
- Squash related tiny commits when they form one logical change (unrelated work = separate PRs)
- Prefer `Closes #N` only for **same-repo** public issues
- **Labels (mandatory):** every issue, PR/MR, and GitHub Discussion welcome post must carry proper labels. GitHub: at least the semantic set in [community-health.md](community-health.md) (`bug`, `enhancement`, `documentation`, `standards`, `chore`, `welcome`, …). Welcome Discussions require `welcome` + `documentation`. GitLab: apply project type/priority/process labels (e.g. `type:docs`, `priority:high`). Unlabeled artifacts are incomplete.
- **Assignee (mandatory for active work):** Every issue and PR that tracks active work must have an assignee. On XGIC public repositories the default is **`@xgic`** unless the human explicitly requests unassigned (for example help-wanted). Agents set assignee at create and verify before close. See [AGENTS.md](../AGENTS.md).
- **Checklist completion before close (mandatory):** Before closing any issue or PR that contains Markdown task lists (`- [ ]` / `- [x]`), verify every required item, update the body to mark completed items `- [x]`, and do not close with unchecked required items unless a human documents an explicit waiver. Also confirm assignee is set (or explicitly waived). Reviewers (human or future AI) apply the same gate. See [AGENTS.md](../AGENTS.md).
- **Documentation style (mandatory for new/edited Markdown):** [documentation-style.md](documentation-style.md) — **sentence-case** headings; **Docker Compose** and **GitLab EE** full product names; soft prose wrap for new content; public-safe only; public OSS README badge row on substantial updates.

---

## AI agent usage (public repos)

- Load the target repo’s `AGENTS.md` first; use this hub for multi-repo standards
- Draft issues/PRs completely; wait for human LGTM before remote create/push/merge when policy requires it
- Run a **leakage scan** before proposing public commits (private hosts, private IDs, internal paths)
- **Never** run `gh issue create|edit`, `gh pr create|edit`, or post a public GitHub comment on an `xgic/*` public repo without completing the **mandatory public-safe draft gate** above
- Distill only public-safe, high-value content into the repo; keep raw session data local

---

## Temporary-file lifecycle (mandatory)

Temporary files are **runtime / agent / CI scratch** — never the product source of truth.

| Rule | Detail |
|------|--------|
| **Location** | Prefer OS temp (`TMPDIR`, system temp directories) or **explicit gitignored** project dirs such as `tmp/` and `.xgic/` outside tracked package trees |
| **Not under product layout** | Do not stage generated files under long-lived source trees (for example package `src/`, or orchestration roots that are versioned as permanent layout) as if they were source |
| **Source of truth** | Keep templates and static assets in their proper locations; generated renderings stay ephemeral |
| **`.gitignore`** | Ignore project temp dirs; add a short comment explaining why |
| **Create** | Prefer restrictive modes when secrets might land in temps; use unique or run-scoped directory names |
| **Reliable removal** | Always remove after success **and** on failure paths (`try`/`finally`, process exit handlers, CI cleanup jobs that always run) |
| **Idempotency** | Re-runs must not accumulate garbage; prefer wipe-and-recreate of run-scoped dirs |
| **Secrets** | Never write credentials or vault material to repo-adjacent temps that might be committed |
| **CI** | Prefer runner-provided temp; upload only intentional artifacts |
| **Agents** | Keep session drafts under gitignored temp dirs; never commit them; run the public-safe gate before any public write |

---

## Bootstrap checklist (new public repo)

1. Initialize GitHub Flow + protect `main`
2. Add comprehensive `.gitignore` (include `.xgic/`, `tmp/`, and other temp/build dirs)
3. Add `README.md`, `AGENTS.md`, `CONTRIBUTING.md`
4. Add docs skeleton and CI as needed
5. Link multi-repo policy to `https://github.com/xgic/ai`
6. Human review of the bootstrap PR
7. Register or update the public namespace summary when a new public Python package is introduced
8. Confirm temporary-file lifecycle rules are followed in scripts/CI that create scratch files

---

## Related hub documents

- [Architecture](architecture.md)
- [Orchestration workflow](orchestration-workflow.md)
- [Grok playbooks](grok-playbooks.md)
- [Python namespace convention](xgic-python-namespace-convention.md)
- [Python package release process](python-package-release.md) (TestPyPI → PyPI, OIDC, `uv` smoke)
- [ADR index](adr/README.md)
