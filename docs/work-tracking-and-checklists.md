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
2. Assign every issue that belongs to the effort to that repository's **milestone**, including siblings. Leave an issue off a milestone only when its description states why it is unscheduled.  
3. Open the PR from a branch **named with the tracking issue number** (see [community-health.md](community-health.md)).  
4. PR body includes `Fixes #N` / `Closes #N` (same repo) or an explicit “Tracks #N” link.  
5. Put acceptance checklists on the **issue** (and/or PR). Prefer the issue as the durable tracker if a PR is superseded.  

**Why:** Milestones and backlog planning attach cleanly to issues. Issue-less PRs often never get a milestone, bury acceptance in the diff, and break the branch-naming convention.

### Exceptions (no prior issue required)

| Exception | Still required |
|-----------|----------------|
| Dependabot / Renovate dependency PRs | Labels; the release milestone that contains the merge |
| Pure **version-bump / release** PRs that only change version strings under an already-tracked release issue or train | `release` label; link the release train/milestone |
| Trivial typo-only docs with no behavior change | Labels; human LGTM |
| Emergency hotfix with human waiver in the PR body | Open a follow-up issue the **same day** |

GitHub keeps a separate milestone on the issue and on the pull request.
Setting the issue does not set the pull request. A semantic-version
release sets `X.Y.Z` on both, as the section below requires. On another
effort, the pull request may carry that effort's milestone. The issue
remains the stable handle.

### Agent obligation

Agents **must not** open a public PR for in-scope work without a tracking issue, except for the table above. If an issue is missing, **create the issue first** (public-safe draft gate), then the PR.

---

## GitHub practice

1. **Issue first** (see above); put the checklist in the issue body when multi-step.  
2. Link PRs with `Fixes #N` / `Refs #N` / `Tracks #N`.  
3. For single-PR work under an exception, the PR description may hold the acceptance checklist.  
4. Create a **repository milestone** for the effort. Assign every issue in the effort, including siblings, and track progress there (not in Markdown tables). A repository that publishes semantic versions uses the `X.Y.Z` milestone in the next section.  
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

Assign every issue that belongs to an effort to that repository's milestone, including siblings. Keep child links on the parent issue. Leave an issue off a milestone only when its description states why it is unscheduled. The milestone description names the parent issue only.

## Semantic-version release milestones

A repository that publishes semantic versions uses one milestone per
final version. The title is `X.Y.Z`, the same version the package
metadata publishes. The Git tag remains `vX.Y.Z`.

The release candidate and the final publish belong to that same
milestone. Create it when the release is intended, with a parent issue
in the same repository. The milestone description names that issue
only.

`X.Y.Z` is the milestone for the release that ships the change. GitHub
keeps a separate milestone on the issue and on the pull request.
Setting the issue does not set the pull request. Set `X.Y.Z` on every
issue and every pull request included in that release, including
siblings and both the candidate and the final version bump. When the
shipped version differs from the version first planned, move the issue
and its pull requests to the shipped `X.Y.Z` before that milestone
closes.

A parent issue whose sub-issues span more than one release is on the
milestone of the release that completes every sub-issue. The parent
does not need its own pull request for that assignment. Each
sub-issue, and each pull request that changes code, stays on the
release that contains that change. A parent that also changes code
keeps those pull requests on the releases that contain the code. The
parent issue still marks the release that finishes the parent. It is
not placed on an interim release. An open parent on an interim
milestone would block the tag that release exists to ship. When
acceptance cannot be finished and a release must ship work that
belongs to that parent, create the next patch of the current minor
and put the new child issues and pull requests on that patch. When
the interim release is not part of that parent, the hotfix is that
same next patch and is not one of the parent's sub-issues. Do not
open the next minor or major for the hotfix. Use an unreleased patch
milestone for that minor when one already exists. A
parent with no code and no sub-issues in a release stays unscheduled.

A completed proof of a release uses that same milestone. Every issue
and pull request merged into `main` after the previous final tag is
on the `X.Y.Z` milestone of the release that contains that change.
The version-bump pull request stays on the milestone it publishes.
Dependency-update pull requests, typo-only documentation, and hotfixes
are included when they are merged to `main`. After a milestone is
closed, reopen it only to set a missed assignment, then close it
again. The release tag is not moved.

A hub effort milestone stays on the hub issue. The releasing
repository's issue and pull requests use `X.Y.Z` only.

An omitted issue says why in its description.

Close the parent issue first, then the milestone, after the final
publish and its acceptance are done. Publishing the release candidate
does not close the milestone.

Do not open a version milestone before its parent issue exists.

A repository that does not publish semantic versions uses an open
milestone that already matches the effort. When none matches and the
effort has two or more issues or pull requests, create one milestone
titled for the effort. One item with no matching milestone stays
unscheduled, and its description says why. That repository does not
take a version milestone for another repository's release. Work that
spans repositories keeps an effort milestone on this hub, titled for
the effort. Each publishing repository keeps its own `X.Y.Z`
milestone.

---

## Multi-repository public work (required parent milestone)

GitHub milestones are repository-scoped on every GitHub plan. GitHub
has no organization milestone and no cross-repository milestone.
**This repository (`xgic/ai`) is the public multi-repo hub.** Each
other public repository still uses its own milestone for its own
issues, including siblings.

GitLab project milestones are project-scoped. GitLab group milestones
are available on the Free tier and apply to issues and merge requests
in that group's projects. A group milestone does not cross groups, and
it does not cross to GitHub.

### Parent issue tracking

Parent **milestones must not** hard-code active issues or child
milestones in their descriptions. Those lists go stale and force agents
to rewrite Markdown instead of using GitHub’s automated tracking.

**Parent milestone description** (stable only):

```markdown
## Scope

Public-safe one-paragraph goal.

## Parent issue

#N
```

Create a **parent issue in the same repository** as that parent
milestone and assign the issue **to** the milestone.

Attach children with native GitHub features:

| Child location | Attach how |
|----------------|------------|
| Same repository | **Sub-issues** |
| Other public `xgic/*` repo | Tracked task-list item `owner/repo#n`, or that repo’s own parent issue |
| Child milestone on a consumer repo | Link that repo’s **parent issue**, not every leaf PR |

Agents **open, close, and track** issues. They do **not** edit the
parent milestone description to add or remove children. Wave progress
is the milestone % complete plus sub-issue / tracked-by widgets.

When an effort spans **two or more** public repositories under
`github.com/xgic/*`:

1. **Required:** create a **parent milestone** on
   **https://github.com/xgic/ai** (title = stable effort name).
2. Create a **parent issue** in `xgic/ai` and assign it to that
   milestone. Point the milestone description at `#N` only.
3. Attach children:
   - **Larger / multi-PR per repo:** child milestone on the consumer
     repo **plus** a parent issue there; track that parent issue from
     the `xgic/ai` parent issue (`owner/repo#n`).
   - **Smaller effort:** tracked task-list items or sub-issues for the
     PRs/issues (no child milestone if a single PR per repo is enough).
4. Keep all public milestone, issue, and PR text **public-safe**.
5. Close the parent issue, then the parent milestone, when the
   multi-repo effort is accepted.

**Example:** a new mandatory rule that must land in this hub and several
other public repos → one `xgic/ai` parent milestone, one `xgic/ai`
parent issue, tracked child parent-issues or PRs.

A single-repository release uses the `X.Y.Z` milestone in that
repository only. No hub parent milestone is required. The
semantic-version section above is the rule.

### Paid-tier revision

GitHub milestones stay repository-scoped on every plan, including paid
plans. GitLab Epics, the roadmap, and burndown charts are paid GitLab
features and are not required here.

---

## Agent obligations

- Prefer numbered procedures in docs; open issues/PRs for acceptance lists.
- **Issue-first** before PRs for in-scope work (see above); do not open issue-less feature/bug/DX/standards PRs.
- Assign every issue that belongs to an effort to that repository's milestone, including siblings. Keep child links on the parent issue. Leave an issue off a milestone only when its description states why it is unscheduled.
- For a repository that publishes semantic versions, use one milestone titled `X.Y.Z` for the release that ships the change. Set it on every included issue and pull request, including work merged to `main` after the previous final tag. A parent whose sub-issues span more than one release is on the release that completes every sub-issue, even when the parent has no pull request of its own. It is not placed on an interim patch. A shippable slice uses the next patch of the current minor. A hotfix that is not part of that parent is that same next patch. A pull request that changes code stays on the release that contains that change. GitHub does not copy the issue milestone onto the pull request. When the shipped version changes, move both to that `X.Y.Z` before the milestone closes. A hub effort milestone stays on the hub issue. Close the parent issue, then the milestone, after the final publish and its acceptance.
- For work spanning **2+ public repos**: create a **parent milestone and
  parent issue on `xgic/ai`**; attach children with sub-issues or
  tracked `owner/repo#n` items. Do not inventory children on the
  milestone description.
- Do not edit a parent milestone description to add or remove child
  issues or child milestones.
- Do not open documentation-only PRs whose sole purpose is updating checklist ticks or status tables.
- Before close: checklists ticked **and** assignee set (or a written exception). Assign first, then close.
- Keep public issue/PR/milestone text **public-safe** ([BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)).

---

## Related

- [BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)
- [orchestration-workflow.md](orchestration-workflow.md)
- [community-health.md](community-health.md)
- [grok-playbooks.md](grok-playbooks.md)
- Tracking: https://github.com/xgic/ai/issues/86  
