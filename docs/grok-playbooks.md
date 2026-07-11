# Grok Build playbooks (public)

Concrete playbooks for AI-assisted work on XGIC **public** repositories. Adapt step counts to the task; keep the security and review gates.

For structured recommendation format, see [agent/recommendation-guide.md](agent/recommendation-guide.md).

## Playbook A — Contribute to this hub (`xgic/ai`)

1. Read `AGENTS.md`, [agent/knowledge-model.md](agent/knowledge-model.md), and the docs index.  
2. Open or select a tracking issue.  
3. Branch: `<issue>-short-kebab-description` from latest `main`.  
4. Edit the right layer (catalog, platform, ADR, standards, README).  
5. Leakage scan: private hosts, private IDs, internal paths must not appear.  
6. Commit (Conventional Commits) and open a PR.  
7. Human reviews and merges in the GitHub UI.  

## Playbook B — Multi-repo implementation recommendation

1. Load catalog + composition + knowledge model.  
2. Classify goal (library, CLI, image, app, ops, docs).  
3. Emit the recommendation template from [recommendation-guide.md](agent/recommendation-guide.md).  
4. Default deploy path: **Compose**; escalate to **Kubernetes** only with explicit requirements.  
5. Cite ADRs 0001–0004 as applicable.  

## Playbook C — Adopt a hub standard in a product repo

1. Confirm canonical text in `https://github.com/xgic/ai`.  
2. In the product repo, open an issue and dedicated branch.  
3. Update local `AGENTS.md` / docs to **link** the hub; keep local copies minimal.  
4. Align license metadata with Apache-2.0 when the repo is a public XGIC solution.  
5. PR + human review.  

## Playbook D — New public Python package announcement

1. Align namespace with [xgic-python-namespace-convention.md](xgic-python-namespace-convention.md).  
2. Follow [ADR-0002](adr/0002-standardize-on-python-3-14.md) and [ADR-0004](adr/0004-apache-2-0-for-public-solutions.md).  
3. Ensure package author/metadata is public-safe (`XGIC`).  
4. PR on **this hub** updating catalog + namespace tables.  
5. Link the new repo from relevant READMEs.  

## Playbook E — Public leakage scan (before every public PR)

Search the diff and new text for:

- Private hostnames / non-GitHub internal URLs  
- Private project IDs or `Closes` targets that are not same-repo public issues  
- Absolute internal workspace paths  
- Secrets (`.env`, tokens, keys)  

If found: remove or rewrite with high-level public wording; do not describe private details in the public PR body.

## Playbook F — Session status report (local only)

1. Use [templates/status-report-template.md](templates/status-report-template.md).  
2. Write to `.xgic/grok-build/status-report.md` (gitignored).  
3. Never commit `.xgic/`.  

## Related

- [Orchestration workflow](orchestration-workflow.md)
- [Base standards](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)
- [Ecosystem catalog](ecosystem/catalog.md)

