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

**Never** place any of the following in this repository (files, issues, **PR/issue/Discussion bodies and comments**, commits, package metadata, or agent output intended for commit):

- Private repository names, private hub names, paths, hostnames, or internal URLs
- Private issue / merge-request identifiers from private trackers (including private work-item links)
- Internal workspace paths, session store paths, or private plan locations
- Credentials, tokens, or environment secrets
- Real private hostnames or tracker paths used as “forbidden examples” on public surfaces
- Phrases that acknowledge or name private coordination systems on public project artifacts

**Allowed on project artifacts** (PR/issue bodies, release notes):

- Technical summary of the public change only
- Full HTTPS links to **public** GitHub artifacts (`https://github.com/xgic/...`)
- Same-repo short refs (`#N`) for issues/PRs **in this public repository only**

**Do not** restate hard-security rules in PR/issue bodies—rules live in this file and [BASE-STANDARDS](docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md). When work is coordinated privately, omit that fact from public artifacts entirely.

**Pre-publish checklist:** no private hosts; no private hub/repo names; no private tracker IDs/links; no private local paths; no hard-coded private project/user IDs in tests or source; no rule restatement in project artifacts; labels applied.

**Mandatory before `gh issue create|edit`, `gh pr create|edit`, or any public comment** (agent gate — do not skip):

1. Draft offline; scan for private hostnames, private DNS zones, private project paths, private tracker issue/MR numbers, and real operator identities.  
2. Replace with **fictional placeholders only** (e.g. `https://gitlab.example.com`, `group/project`, `TOKEN`).  
3. Prefer describing defects generically (“self-hosted instance missing field X”) over naming any private deployment.  
4. Re-scan the **final** body after any edit.  
5. If a leak was published: **sanitize immediately** (edit/delete), then treat as a security incident—without restating the private values on public surfaces.  

Optional: `python scripts/public-safe-scan.py path/to/draft.md` (generic patterns only). Full multi-repo rule: [BASE-STANDARDS](docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md).

**Configuration over hard-coding:** hosts, namespace paths, user IDs, and credentials come from env/config or synthetic fixtures—not literals that identify private systems. See [BASE-STANDARDS](docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md).

**Mandatory checklist completion before close** (issues, PRs, and any Markdown task lists on those artifacts):

1. Enumerate every unchecked item (`- [ ]`).  
2. Verify each against evidence (merged PRs, CI, Releases, live docs).  
3. Update the body so completed items are `- [x]`.  
4. Do **not** close while required items remain unchecked unless a human documents an explicit waiver on the artifact.  
5. **Assignee before close:** `gh issue view --json assignees` (or the PR equivalent). If the list is empty and no written exception applies, **assign `@xgic` first, then close**. Never close then assign.  
6. Reviewers (human today; AI agent later) apply the same gate.

Closing with unchecked required checklist items or missing required assignees is a process defect: reopen, assign, fix fields, then close.

**Close without an assignee** only when **one** of these is written on the artifact (body or closing comment). See [work-tracking-and-checklists.md](docs/work-tracking-and-checklists.md):

1. Human unassigned waiver (help-wanted / community pickup), repeated in the close note.  
2. Spam / abuse / invalid (`invalid` or equivalent).  
3. Duplicate of another issue or PR that **is** assigned (link required).  
4. Rare platform artifact the API cannot assign (name the type in the close note).  

Completed work, merged PRs, and “the bot forgot” are **not** exceptions.

Violations are security incidents: stop, sanitize public text immediately, and correct before merge.

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
- **GitHub Flow**: **issue first** (bugs/features/DX/standards), then short-lived branches named with the issue number (e.g. `58-issue-first-tracking`). See [docs/work-tracking-and-checklists.md](docs/work-tracking-and-checklists.md).
- **Post-merge workspace cleanup:** After a PR merges to `main`, automatically remove extra git worktrees and OS temp dirs created for that issue. Keep the canonical clone, session files, virtualenvs, and dirty/unmerged trees. See [BASE-STANDARDS](docs/BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md) and [grok-playbooks.md](docs/grok-playbooks.md) playbook G.
- **Human review gate**: agents prepare complete drafts; humans review and approve in the GitHub UI before merge to `main`. Agents never approve or merge their own PRs.
- **Conventional Commits**: `type(scope): subject` plus a body explaining *what* and *why*.
- **Atomic changes**: include relevant doc updates in the same commit when they are part of the change.
- **Labels (mandatory):** apply proper labels to every issue, PR, and Discussion welcome post before considering the artifact complete. Welcome posts: `welcome` + `documentation`. See [docs/community-health.md](docs/community-health.md).
- **Assignee (mandatory at create and before close):** Every issue and pull request must have an assignee at create (same command as labels; default **`@xgic`**). Empty assignee after create is a process defect: assign immediately. Before close, re-check `assignees`; assign then close. Exceptions are the short table in [work-tracking-and-checklists.md](docs/work-tracking-and-checklists.md). GitHub cannot native-lock close on assignee; this is layered process. Optional post-close repair workflows are follow-up only.
- **Rule text lives in standards docs** (this file, base standards). Do not restate full rule procedures in issue/PR templates.

---

## Session startup checklist

1. `git status -sb` and confirm branch / remote  
2. Read this file, `README.md`, and `docs/agent/knowledge-model.md`  
3. Skim `docs/ecosystem/catalog.md` for the domains you will touch  
4. List open issues/PRs: `gh issue list`, `gh pr list`  
5. Confirm the change is **public-safe** (hard security scan)  
6. Before any public `gh issue`/`gh pr` create/edit or public comment: complete the **mandatory public-safe draft gate** above  
7. Prefer full `https://github.com/xgic/...` URLs for cross-repo links  

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
