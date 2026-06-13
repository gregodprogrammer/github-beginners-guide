# Approach 1: Linear Lecture + Lab — Slide Deck
*Theory First, Then Practice | 5 Sessions | 1 Hour Each*

---

## How to Use These Slides

- 6-8 slides per session
- Speaker notes in italics
- Leave analogy slides up for 2+ minutes

---

---

# SESSION 1: What is Git? Your First Repository

---

## Slide 1: The Chaos of Manual Version Control

Have you ever named a file:

```
report_final.doc
report_final_v2.doc
report_final_v2_ACTUAL.doc
report_final_v2_ACTUAL_FOR_REAL.doc
```

**This is manual version control.**

*It works until you have 50 files, 3 people, and a deadline.*

> **Speaker note:** Show of hands. Everyone has done this.

---

## Slide 2: The Magic Camera Analogy

**Git is a magic camera for your files.**

- Build something good → take a photo (**commit**)
- Mess up later → say "Take me back to Photo #3"
- **Poof.** Restored.

| Simple | Technical |
|--------|-----------|
| Photo | **Commit** |
| Photo album | **Repository** |
| Box before photo | **Staging Area** |
| Messy desk | **Working Directory** |

> **Speaker note:** Draw a camera. Label commit = photo.

---

## Slide 3: The Three-Stage Model

```
Working Directory  --git add-->  Staging Area  --git commit-->  Git Repository
   (messy desk)                    (prep box)         (permanent album)
```

1. Edit files (desk)
2. Stage files (prep box)
3. Commit files (album)

> **Speaker note:** Physically mime it.

---

## Slide 4: `git status` Is Your Dashboard

Run it **constantly**. It tells you:
- Which files are **new**
- Which files **changed**
- What's **ready to commit**

**Confused? Run `git status`.**

> **Speaker note:** #1 command students should memorize.

---

## Slide 5: Commit Messages Matter

❌ Bad: "stuff", "changes", "asdf"

✅ Good:
- "Add nginx config for production"
- "Fix database timeout"
- "Update Terraform module"

**In incidents, clear messages save hours.**

> **Speaker note:** Give a real example from your experience.

---

## Slide 6: Lab Overview

**Goal:** Create a repo, make commits, view history.

1. `mkdir devops-course && cd devops-course`
2. `git init`
3. `echo "Welcome" > readme.txt`
4. `git add readme.txt`
5. `git commit -m "Add welcome message"`
6. `git log --oneline`

> **Speaker note:** Have students follow along live.

---

---

# SESSION 2: Branching and Merging

---

## Slide 1: Why Branch?

Three developers edit the same file:
- A rewrites the header
- B adds a footer
- C deletes the sidebar

**Result: CHAOS.**

> **Speaker note:** Ask who has experienced this.

---

## Slide 2: The Parallel Universe

A branch is a **parallel universe**.

- Universe A: You're adding a contact form
- Universe B: Your teammate is redesigning the homepage
- Neither affects the other

When ready: **merge** the universes together.

> **Speaker note:** Draw two parallel lines that merge.

---

## Slide 3: Names Matter

| ✅ Good | ❌ Bad |
|---------|--------|
| `feature-auth` | `branch1` |
| `fix-broken-link` | `temp` |
| `update-about-page` | `asdf` |

> **Speaker note:** Use humor.

---

## Slide 4: Fast-Forward vs. Merge Commit

- **Fast-forward:** `main` hasn't changed. Just move pointer.
- **Merge commit:** `main` has new commits. Create a new commit combining both.

> **Speaker note:** Draw both scenarios.

---

## Slide 5: Lab Overview

1. `git branch` — check where you are
2. `git branch feature-about` — create
3. `git switch feature-about` — move there
4. Create `about.txt`, commit
5. `git switch main` — verify unchanged
6. `git merge feature-about` — bring it in
7. `git branch -d feature-about` — cleanup

> **Speaker note:** Students do this independently after demo.

---

---

# SESSION 3: GitHub, Remotes, and Pull Requests

---

## Slide 1: Local vs. Remote

- **Local:** On your laptop (bedroom desk)
- **Remote:** On GitHub (school library)

**The remote is the "source of truth."**

> **Speaker note:** Emphasize: GitHub is not just storage — it's collaboration.

---

## Slide 2: The Complete Workflow

```
[Branch] → [Edit] → [Commit] → [Push] → [PR] → [Review] → [Merge] → [Pull]
```

**No direct pushes to `main` in production teams.**

> **Speaker note:** This diagram should be memorized.

---

## Slide 3: What Is a Pull Request?

A Pull Request is a **formal request** to merge your work.

Steps:
1. Push your branch
2. Open PR on GitHub
3. Team reviews code
4. CI runs tests
5. Approve and merge

> **Speaker note:** Compare to getting homework signed by a teacher.

---

## Slide 4: Code Review Catches Bugs

Without PR:
```
You → push to main → production breaks
```

With PR:
```
You → PR → teammate sees bug → fix → merge → safe
```

> **Speaker note:** The value of PRs is catching mistakes.

---

## Slide 5: Lab Overview

1. Create GitHub repo
2. `git remote add origin ...`
3. `git push -u origin main`
4. Branch, create `faq.txt`, commit
5. `git push -u origin feature-faq`
6. Open PR, review, merge
7. `git pull` locally
8. Delete branch

> **Speaker note:** Walk through GitHub UI slowly.

---

---

# SESSION 4: Undoing Changes and Handling Conflicts

---

## Slide 1: The Philosophy of Undoing

| Situation | Right Tool |
|-----------|-----------|
| Bad edit, not committed | `git restore` |
| Wrong file staged | `git restore --staged` |
| Bad commit, local only | `git reset --soft HEAD~1` |
| Bad commit, already pushed | `git revert` |

> **Speaker note:** Write this as a decision tree on the board.

---

## Slide 2: Revert Is Always Safe

`git revert COMMIT` — creates a NEW commit that undoes an OLD commit.

- History is preserved
- Audit trail intact
- Safe for shared branches

**This is how professionals fix production.**

> **Speaker note:** Emphasize NEVER use `reset` on shared branches.

---

## Slide 3: Conflicts Are Normal

When two branches change the same line:

```
<<<<<<< HEAD
main's version
=======
branch's version
>>>>>>> branch-name
```

**Fix:** Edit, remove markers, stage, commit.

> **Speaker note:** Normalize this. It happens daily.

---

## Slide 4: Git Stash

You're mid-task. Boss says: "Fix production NOW."

1. `git stash` — save work in a backpack
2. Fix production
3. `git stash pop` — unpack backpack

> **Speaker note:** Mime the backpack.

---

## Slide 5: Lab Overview

1. Break something, commit it
2. `git log --oneline` — find bad commit
3. `git revert` — fix it
4. Create conflict scenario
5. Resolve it
6. `git stash` and `git stash pop`

> **Speaker note:** This session is the most technical.

---

---

# SESSION 5: DevOps Patterns and GitHub Actions

---

## Slide 1: CI/CD Is the Heart of DevOps

| Without | With |
|---------|------|
| Manual tests | Robot tests |
| Bugs in production | Bugs caught before merge |
| Days to deploy | Minutes to deploy |

> **Speaker note:** This is why they took this course.

---

## Slide 2: GitHub Actions

- **Workflow:** YAML recipe
- **Trigger:** Events like `push`, `pull_request`
- **Job:** Group of steps
- **Runner:** VM that runs your code

> **Speaker note:** Analogy: recipe, trigger, kitchen, chef.

---

## Slide 3: YAML Is Just a Recipe

```yaml
name: Portfolio CI
on:
  push:
    branches: [ main ]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: test -f home.txt && echo "OK"
```

> **Speaker note:** Show it line by line.

---

## Slide 4: Branch Protection

Lock `main`:
- Require PR
- Require CI pass
- Require code review

**This protects production.**

> **Speaker note:** Draw a padlock on `main`.

---

## Slide 5: Lab Overview

1. Create `.github/workflows/ci.yml`
2. Check files exist
3. Push, watch it pass
4. Create break branch, see it fail
5. Set branch protection
6. Try direct push — get blocked

> **Speaker note:** This is graduation.

---

*End of Approach 1 Slide Deck*
