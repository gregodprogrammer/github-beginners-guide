# Approach 2: Project-Driven (Build-Along) — Slide Deck
*One Continuous Project Across 5 Sessions*

---

## How to Use These Slides

- Each session opens with "Project Status" and "Today's Goal"
- Demos should happen in real time as students follow
- By Session 5, every student has a real portfolio with CI/CD

---

---

# SESSION 1: Foundation — Home Page and First Commits

---

## Slide 1: Welcome to the Build-Along

**You will build `my-devops-portfolio`.**

By Session 5 it will have:
- ✅ `home.txt` — Home page
- ✅ `about.txt` — About page
- ✅ `projects.txt` — Projects page
- ✅ `contact.txt` — Contact page
- ✅ `skills.txt` — Skills list
- ✅ A CI robot that auto-checks everything
- ✅ Branch protection on `main`

**This repo goes on your GitHub. Show it in interviews.**

> **Speaker note:** Motivation is everything. Students need to see the finish line.

---

## Slide 2: Today's Goal

Build the `home.txt` file and save it with Git.

**By the end, you'll know:**
- `git init` — hire the security guard
- `git add` — put files in the box
- `git commit` — take the photo
- `git log --oneline` — view the album

> **Speaker note:** Tie every command to the project.

---

## Slide 3: The Build

```bash
$ mkdir my-devops-portfolio
$ cd my-devops-portfolio
$ git init
```

Create `home.txt`:
```
================================
  MY DEVOPS PORTFOLIO
================================

Hi, I'm [Your Name]!
I'm learning DevOps.

Navigation: Home | About | Projects | Contact
```

Stage and commit:
```bash
$ git add home.txt
$ git commit -m "Add homepage"
```

> **Speaker note:** Students type this. Their project is born.

---

## Slide 4: What Just Happened?

1. `git init` — Git started watching this folder
2. `git add` — Told Git to include `home.txt` in the next photo
3. `git commit` — Took the photo
4. `git log` — Looked at the album

**These 4 commands are 80% of Git.**

> **Speaker note:** Repeat until it's muscle memory.

---

---

# SESSION 2: Two New Pages — Branching

---

## Slide 1: Project Status

✅ `home.txt` — Done

⏳ `about.txt` — Today

⏳ `projects.txt` — Today

**Rule:** We never edit `main` directly. Create branches.

> **Speaker note:** Reinforce the safety rule.

---

## Slide 2: Branch = Parallel Universe

You're writing a book. The published version is `main`.

- Photocopy the book
- Write a new chapter in the copy
- If it's good → paste it into the real book
- If it's bad → throw away the copy

**The copy = a branch.**

> **Speaker note:** Draw a book being photocopied.

---

## Slide 3: Today's Build

1. `git branch feature-about-page`
2. `git switch feature-about-page`
3. Create `about.txt` with your bio
4. Commit
5. `git switch main` — verify unchanged
6. `git merge feature-about-page`
7. Repeat for `projects.txt`
8. `git branch -d feature-about-page`

> **Speaker note:** Two features in one session. Pace it.

---

## Slide 4: Check Before You Merge

```bash
$ ls
```

On `main` (before merge): only `home.txt`

On `feature-about-page`: `home.txt` + `about.txt`

**The original is safe the entire time.**

> **Speaker note:** This is the "aha!" moment.

---

---

# SESSION 3: Going Online — GitHub and PRs

---

## Slide 1: Project Status

✅ `home.txt`

✅ `about.txt`

✅ `projects.txt`

✅ `skills.txt`

⏳ Push to GitHub — Today

⏳ `contact.txt` via PR — Today

> **Speaker note:** Show growth. 3 pages done.

---

## Slide 2: Your Desk vs. The Library

- **Your laptop** = your bedroom desk
- **GitHub** = the school library

You write on your desk. Then you bring it to the library so everyone can see it.

**Your homework on GitHub = your portfolio.**

> **Speaker note:** Tie GitHub to career goals.

---

## Slide 3: Today's Build

1. Create `my-devops-portfolio` on GitHub
2. `git remote add origin ...`
3. `git push -u origin main`
4. Create branch `feature-contact-page`
5. Build `contact.txt`
6. Commit and push
7. Open Pull Request on GitHub
8. Review, merge, delete branch
9. `git pull` locally

> **Speaker note:** The PR workflow is the core skill. Go slow.

---

## Slide 4: By the End of Today

Go to `https://github.com/YOURNAME/my-devops-portfolio`

**You'll see your code on the internet.**

> **Speaker note:** Make students open their repo in a browser. Celebrate.

---

---

# SESSION 4: Fixing Mistakes and The Unexpected

---

## Slide 1: Project Status

✅ All pages built

✅ On GitHub

⚠️ **Today we break things on purpose.**

> **Speaker note:** Set expectation: controlled chaos.

---

## Slide 2: The Revert

You committed a bad change.

Don't panic. Don't delete history.

Use `git revert` — it adds a NEW commit that undoes the bad one.

**Safe. Traceable. Professional.**

> **Speaker note:** This is how real engineers fix production at 3 AM.

---

## Slide 3: The Merge Conflict

Two branches changed the same line.

Git shows:
```
<<<<<<< HEAD
main version
=======
branch version
>>>>>>> branch
```

**Fix it, remove markers, stage, commit.**

> **Speaker note:** Normalize conflicts. Students panic otherwise.

---

## Slide 4: Git Stash

Mid-task, boss says production is down.

1. `git stash` — save work in backpack
2. Fix the fire
3. `git stash pop` — unpack backpack

> **Speaker note:** The most practical command for interruptions.

---

## Slide 5: Today's Challenges

1. Break `home.txt` on purpose → commit → revert
2. Create two branches that edit `about.txt` differently
3. Merge both → conflict → resolve
4. `git stash` a work-in-progress

> **Speaker note:** This is problem-solving practice.

---

---

# SESSION 5: Robots Do the Work — CI/CD

---

## Slide 1: Project Status

✅ Full website

✅ On GitHub

✅ PR workflow mastered

⚡ **Final step: Add a robot.**

> **Speaker note:** This is the graduation moment.

---

## Slide 2: The Robot Chef

Every time a chef puts a dish on the menu, a robot:
1. Tastes it
2. Checks temperature
3. Photographs it
4. Approves or rejects it

**GitHub Actions = that robot.**

> **Speaker note:** Students love the robot analogy.

---

## Slide 3: What the Robot Does for Us

Our robot will:
1. Check that all pages exist
2. Verify the navigation section is present
3. Report ✅ or ❌

**If it fails, we can't merge.**

> **Speaker note:** This is quality gates in action.

---

## Slide 4: The Recipe (YAML)

```yaml
name: Portfolio CI
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          for file in home.txt about.txt projects.txt contact.txt; do
            test -f "$file" || exit 1
          done
          echo "All pages present!"
```

> **Speaker note:** Walk through line by line.

---

## Slide 5: Branch Protection

Lock `main`:
- No direct pushes
- Must use PR
- Robot must pass

**This is how real companies protect production.**

> **Speaker note:** The padlock on `main`.

---

## Slide 6: Today's Build

1. Create `.github/workflows/portfolio-ci.yml`
2. Commit and push
3. Watch it pass ✅
4. Break something on a branch
5. See it fail ❌
6. Set branch protection
7. Try direct push → blocked

> **Speaker note:** Make students do the final push themselves.

---

## Slide 7: Graduation

You now have:
- A real GitHub repo
- Commits with good messages
- Merged PRs
- A passing CI pipeline
- Branch protection

**Add this to your resume:**

> "Proficient in Git, GitHub, CI/CD pipelines, and branch protection."

> **Speaker note:** This is the payoff. Make students proud.

---

*End of Approach 2 Slide Deck*
