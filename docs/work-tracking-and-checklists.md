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

## Issue-first tracking (mandatory)

**Default:** For any **bug, feature, DX defect, or standards change**, create or reuse a **same-repo issue** **before** opening the pull request.

Then:

1. Assign **labels** and **assignee** (public default `@xgic` unless help-wanted / explicit unassigned).  
2. Assign a **milestone** when the work is part of a release train or multi-issue effort. Small one-off chores may omit a milestone.  
3. Open the PR from a branch **named with the tracking issue number** (see [community-health.md](community-health.md)).  
4. PR body includes `Fixes #N` / `Closes #N` (same repo) or an explicit “Tracks #N” link.  
5. Put acceptance checklists on the **issue** (and/or PR). Prefer the issue as the durable tracker if a PR is superseded.  

**Why:** Milestones and backlog planning attach cleanly to issues. Issue-less PRs often never get a milestone, bury acceptance in the diff, and break the branch-naming convention.

### Exceptions (no prior issue required)

| Exception | Still required |
|-----------|----------------|
| Dependabot / Renovate dependency PRs | Labels; optional milestone |
| Pure **version-bump / release** PRs that only change version strings under an already-tracked release issue or train | `release` label; link the release train/milestone |
| Trivial typo-only docs with no behavior change | Labels; human LGTM |
| Emergency hotfix with human waiver in the PR body | Open a follow-up issue the **same day** |

PRs **may** also be added to milestones; the issue remains the stable handle.

### Agent obligation

Agents **must not** open a public PR for in-scope work without a tracking issue, except for the table above. If an issue is missing, **create the issue first** (public-safe draft gate), then the PR.

---

## GitHub practice

1. **Issue first** (see above); put the checklist in the issue body when multi-step.  
2. Link PRs with `Fixes #N` / `Refs #N` / `Tracks #N`.  
3. For single-PR work under an exception, the PR description may hold the acceptance checklist.  
4. For a release train or multi-issue feature, create a **repository milestone**, assign issues/PRs, and track progress there (not in Markdown tables).  
5. Before closing an issue or PR that contains task lists, mark required items complete (`- [x]`) or document a human waiver (see [BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)).  
6. **Assign before close.** `gh issue view --json assignees` (or the PR equivalent). If empty, assign `@xgic` then close, unless a written exception below applies. Never close then assign.

---

## Assign before close (mandatory)

Every issue and pull request is assigned at **create** (same command as labels; default `@xgic`) **and** still assigned at **close**.

GitHub rulesets cannot require an assignee as a condition of closing. The guarantee is layered process, not a native lock.

### Close-time agent gate

1. Read `assignees`.  
2. If empty and no written exception, assign `@xgic`.  
3. Then close.  

Empty assignee at close is a process defect except the table below.

### Exceptions (close without an assignee)

Write **one** of these on the artifact (body or closing comment):

| Exception | Required writing |
|-----------|------------------|
| Human unassigned waiver | Human asked for unassigned (help-wanted / community pickup); close note repeats the waiver |
| Spam / abuse / invalid | Labeled `invalid` (or equivalent) |
| Duplicate | Closed as duplicate of an issue or PR that **is** assigned; link required |
| Platform artifact | GitHub-generated item the API cannot assign; name the type in the close note |

**Dependabot / Renovate:** keep labels. Prefer assigning `@xgic` when GitHub permits. Closing a bot-owned PR without `@xgic` is allowed only when the org cannot assign that PR.

**Not an exception:** completed work, merged PRs, or “the bot forgot.”

Optional GitHub Actions repair on `issues: closed` / `pull_request: closed` is follow-up only. It runs after close and does not replace this gate.

**Sizing:** not every PR needs a milestone. Prefer milestones for releases and coordinated multi-issue work. Small independent changes can use labels and the issue/PR checklist alone.

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
- **Issue-first** before PRs for in-scope work (see above); do not open issue-less feature/bug/DX/standards PRs.  
- Prefer milestones for release trains and multi-issue features; assign the **issue** (and optionally the PR) to the milestone.  
- For work spanning **2+ public repos**: create or update a **parent milestone on `xgic/ai`** with a link map to child milestones or PRs/issues.  
- Do not open documentation-only PRs whose sole purpose is updating checklist ticks or status tables.  
- Before close: checklists ticked **and** assignee set (or a written exception). Assign first, then close.  
- Keep public issue/PR/milestone text **public-safe** ([BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)).

---

## Related

- [BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)  
- [orchestration-workflow.md](orchestration-workflow.md)  
- [community-health.md](community-health.md)  
- [grok-playbooks.md](grok-playbooks.md)  
