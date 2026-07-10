# Grok Build playbooks (public)

Concrete playbooks for AI-assisted work on XGIC **public** repositories. Adapt step counts to the task; keep the security and review gates.

## Playbook A — Contribute to this hub (`xgic/ai`)

1. Read `AGENTS.md` and the docs index.
2. Open or select a tracking issue.
3. Branch: `<issue>-short-kebab-description` from latest `main`.
4. Edit the appropriate docs (standards, ADR, namespace, README).
5. Leakage scan: private hosts, private IDs, internal paths must not appear.
6. Commit (Conventional Commits) and open a PR.
7. Human reviews and merges in the GitHub UI.

## Playbook B — Adopt a hub standard in a product repo

1. Confirm the canonical text in `https://github.com/xgic/ai` (BASE-STANDARDS, ADR, namespace).
2. In the product repo, open an issue and dedicated branch.
3. Update local `AGENTS.md` / docs to **link** the hub; copy only short local necessities.
4. Avoid rewriting multi-repo policy differently in each repo.
5. PR + human review.

## Playbook C — New public Python package announcement

1. Align namespace with [xgic-python-namespace-convention.md](xgic-python-namespace-convention.md).
2. Follow [ADR-0002](adr/0002-standardize-on-python-3-14.md) for Python baseline.
3. Ensure package author/metadata is public-safe (`XGIC`, public contact only).
4. Open a PR on **this hub** updating the namespace table when the public repo exists or is intentionally listed as planned.
5. Link the new repo from product READMEs as appropriate.

## Playbook D — Public leakage scan (before every public PR)

Search the diff and new text for:

- Private hostnames / non-GitHub internal URLs
- Private project IDs or `Closes` targets that are not same-repo public issues
- Absolute internal workspace paths
- Secrets (`.env`, tokens, keys)

If found: remove or rewrite with high-level public wording; do not describe the private details in the public PR body.

## Playbook E — Session status report (local only)

1. Use [templates/status-report-template.md](templates/status-report-template.md).
2. Write to `.xgic/grok-build/status-report.md` (gitignored).
3. Never commit `.xgic/`.

## Related

- [Orchestration workflow](orchestration-workflow.md)
- [Base standards](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)
