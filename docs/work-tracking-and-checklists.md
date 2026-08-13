# Work tracking, checklists, and milestones (public)

**Status:** Living standard  
**Audience:** Maintainers, contributors, AI agents (including Grok Build)  
**Authority:** Prefer this document in [xgic/ai](https://github.com/xgic/ai) for public repositories  

---

## Rule

**Do not put progress checklists or living phase/status tables in documentation** unless an exception below applies.

Use **platform-native** tracking on **GitHub**:

| Concern | Put it here |
|---------|-------------|
| Acceptance / operator completion lists | **Issues** and **pull request** descriptions |
| Release train / multi-issue feature progress | **Repository milestones** |
| Procedures and architecture | **Docs** (stable numbered steps + permanent tracker links only) |

Markdown task lists (`- [ ]` / `- [x]`) and Done/Pending tables in README files, runbooks, and similar docs create unnecessary churn: every tick would otherwise require a docs PR. That is inefficient for daily work.

---

## Documentation vs platform

| Put in docs | Put on issues / PRs / milestones |
|-------------|---------------------|
| Stable **how-to** procedures (numbered steps) | Acceptance criteria for a change |
| Architecture and policy | Operator job completion lists |
| Permanent links to milestones or parent issues | Status of “what’s done” |
| Design rationale | Release trains (milestones) |

---

## Exceptions

Documentation may include a task list only when:

1. It is explicitly a **template to copy** into a new issue or PR (and states that progress is not tracked in the doc), or  
2. A human records a rare waiver for a specific artifact.

Fixed **policy verification** lists (for example public-safe gates in BASE-STANDARDS) should use **numbered requirements**, not interactive task lists, unless they live on a PR template.

---

## GitHub practice

1. Create a labeled issue for multi-step work; put the checklist in the issue body.  
2. Link PRs with `Fixes #N` / `Refs #N`.  
3. For single-PR work, the PR description may hold the acceptance checklist.  
4. For a release train or multi-issue feature, create a **repository milestone**, assign issues/PRs, and track progress there (not in Markdown tables).  
5. Before closing an issue or PR that contains task lists, mark required items complete (`- [x]`) or document a human waiver (see [BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)).

**Sizing:** not every PR needs a milestone. Prefer milestones for releases and coordinated multi-issue work. Small independent changes can use labels and the PR checklist alone.

---

## Multi-repository public work (required parent milestone)

GitHub Free does not provide an organization-wide milestone across all `xgic/*` repositories. **This repository (`xgic/ai`) is the public multi-repo hub.**

When an effort spans **two or more** public repositories under `github.com/xgic/*`:

1. **Required:** create a **parent milestone** on **https://github.com/xgic/ai**.  
2. In that milestone’s description, maintain a **public-safe link map**:
   - **Larger / multi-PR efforts:** link **child milestones** on each consumer repository (assign PRs/issues to those child milestones).  
   - **Smaller efforts:** link the **PRs and issues** directly (child milestones optional when a single PR per repo is enough).  
3. Close the parent milestone only when the multi-repo effort is accepted.

**Example:** implementing a new mandatory rule or standard that must land in this hub and several other public repos → one `xgic/ai` parent milestone with links to each repo’s PR or child milestone.

Single-repo release trains may use a milestone **only** on that repository (no `xgic/ai` parent required).

Keep all public milestone, issue, and PR text **public-safe**.

---

## Agent obligations

- Prefer numbered procedures in docs; open issues/PRs for acceptance lists.  
- Prefer milestones for release trains and multi-issue features.  
- For work spanning **2+ public repos**: create or update a **parent milestone on `xgic/ai`** with a link map to child milestones or PRs/issues.  
- Do not open documentation-only PRs whose sole purpose is updating checklist ticks or status tables.  
- Keep public issue/PR/milestone text **public-safe** ([BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)).

---

## Related

- [BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)  
- [orchestration-workflow.md](orchestration-workflow.md)  
- [community-health.md](community-health.md)  
- [grok-playbooks.md](grok-playbooks.md)  
