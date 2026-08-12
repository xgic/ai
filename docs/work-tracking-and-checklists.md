# Work tracking and checklists (public)

**Status:** Living standard  
**Audience:** Maintainers, contributors, AI agents (including Grok Build)  
**Authority:** Prefer this document in [xgic/ai](https://github.com/xgic/ai) for public repositories  

---

## Rule

**Do not put progress checklists in living documentation** unless an exception below applies.

Use **platform-native** tracking instead:

| Forge | Put checklists here |
|-------|---------------------|
| **GitHub** | Issues and pull request descriptions |
| **GitLab** (when used) | Issues, child work items/tasks, and merge request descriptions |

Markdown task lists (`- [ ]` / `- [x]`) in README files, runbooks, architecture notes, and similar docs create unnecessary churn: every tick would otherwise require a docs PR. That is inefficient for daily work.

---

## Documentation vs work items

| Put in docs | Put on issues / PRs / MRs |
|-------------|---------------------------|
| Stable **how-to** procedures (numbered steps) | Acceptance criteria for a change |
| Architecture and policy | Operator job completion lists |
| Links to the tracking issue | Status of “what’s done” |
| Design rationale | Cross-task breakdown (child items where supported) |

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
4. Before closing an issue or PR that contains task lists, mark required items complete (`- [x]`) or document a human waiver (see [BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)).

---

## GitLab practice (when applicable)

Prefer issues and **child work items** for complex breakdown, and **link** related work items and MRs instead of duplicating status in Markdown files. Hierarchical create/link automation may use the public [XGIC GitLab GraphQL client](https://github.com/xgic/gitlab-graphql) ([PyPI](https://pypi.org/project/xgic-gitlab-graphql/)) with a pinned version in automation.

---

## Agent obligations

- Prefer numbered procedures in docs; open issues/PRs for acceptance lists.  
- Do not open documentation-only PRs whose sole purpose is updating checklist ticks.  
- Keep public issue/PR text **public-safe** ([BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)).

---

## Related

- [BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)  
- [orchestration-workflow.md](orchestration-workflow.md)  
- [community-health.md](community-health.md)  
- [grok-playbooks.md](grok-playbooks.md)  
