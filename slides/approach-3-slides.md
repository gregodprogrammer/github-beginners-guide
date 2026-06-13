# Approach 3: Story-Mode — Slide Deck
*DevOps Team Onboarding | 5 Sessions | 1 Hour Each*

---

## How to Use These Slides

- Each session = 15 minutes of slides (approximately 6-8 slides)
- Speaker notes are in **italics below each slide**
- Present left-to-right, top-to-bottom
- Leave the analogy slide up for at least 2 minutes — let it sink in

---

---

# SESSION 1: "Day 1 at the Company"
## Create Your First Repository

---

## Slide 1: Welcome to TechCorp!

**You're the new DevOps engineer.**

*Today you join the team. Your badge works. Your desk is clean. Your boss says: "Set up the project folder."*

> **Speaker note:** Set the scene. Students should feel like they're starting a real job.

---

## Slide 2: The Problem with No Version Control

Have you ever saved a file as...

```
report_final.doc
report_final_v2.doc
report_final_v2_ACTUAL.doc
report_final_v2_ACTUAL_FOR_REAL.doc
```

**This is manual version control. It doesn't scale.**

> **Speaker note:** Ask for a show of hands. Everyone has done this.

---

## Slide 3: The Magic Camera

**Git is like a magic camera.**

- You build something good → take a photo
- You mess up later → say "Take me back to photo #3!"
- **Poof.** Everything is restored.

**In Git:**
- The drawing = your project files
- The photo = a **commit**
- The camera = Git
- The photo album = the **repository**

> **Speaker note:** Draw a camera on the whiteboard. Label: commit = photo.

---

## Slide 4: The Three-Stage Model

Git doesn't take photos automatically. You must:

| Stage | Analogy | Git Command |
|-------|---------|-------------|
| Working Directory | Your messy desk | Edit files |
| Staging Area | The box before the photo | `git add` |
| Commit | The permanent photo | `git commit` |

> **Speaker note:** Physically mime it. Pretend to put a file in a box, then take a photo.

---

## Slide 5: Key Terms

| Simple Word | Professional Word |
|-------------|-------------------|
| Folder with the camera inside | **Repository** |
| Photo | **Commit** |
| Photo album | **History** |
| Box before the photo | **Staging Area** |
| Messy desk | **Working Directory** |

> **Speaker note:** Write both columns on the board. Students need to hear both.

---

## Slide 6: Today's Mission

**Create your first repo and save your first snapshot.**

1. Create a folder
2. Initialize Git (hire the security guard)
3. Create a file
4. Stage it (put it in the box)
5. Commit it (take the photo)
6. Check your history

> **Speaker note:** Pause. Let students open their terminals.

---

## Slide 7: `git status` Is Your Dashboard

Run it constantly. It tells you:
- Which files are new (untracked)
- Which files changed (modified)
- What's ready to commit (staged)

**If you're ever confused, run `git status`.**

> **Speaker note:** This is the #1 command students should memorize.

---

## Slide 8: Commits Need Good Messages

❌ Bad: "stuff", "changes", "asdf"

✅ Good:
- "Add homepage with welcome message"
- "Fix navigation CSS"
- "Update database config for staging"

> **Speaker note:** Emphasize: in production incidents, clear commit messages save hours.

---

---

# SESSION 2: "Fixing Your First Bug"
## Branching and Merging

---

## Slide 1: Oh No! A Typo on the Home Page

A customer emailed:

> "Your website says 'We build **amaizing** things.' That's not a word."

**Your task: Fix it WITHOUT breaking the live site.**

> **Speaker note:** Make it relatable. We've all shipped a typo.

---

## Slide 2: The Highway Analogy

**`main` is the highway** that customers drive on.

You don't dig up the highway to fix a pothole. You:
1. Close off a **lane** (create a branch)
2. Work safely there
3. Merge back when tested

**The lane = a branch.**

> **Speaker note:** Draw a highway. Label `main` as the road and branches as closed-off lanes.

---

## Slide 3: Branch Naming

| Good Name | Why |
|-----------|-----|
| `fix-typo` | Clear what it fixes |
| `feature-contact-form` | Clear what it adds |

| Bad Name | Why |
|----------|-----|
| `branch1` | Meaningless |
| `temp` | Will you remember it in 2 weeks? |

> **Speaker note:** Show this as a real list. Make students laugh at "asdf".

---

## Slide 4: The Branch Workflow

```
main (safe)  →  create branch  →  fix bug  →  test  →  merge  →  main (still safe)
```

**If you mess up on the branch:**
- Delete it
- Start over
- NO CUSTOMERS WERE HARMED

> **Speaker note:** Emphasize the safety. Branching is insurance.

---

## Slide 5: Fast-Forward Merge

When `main` hasn't changed since you branched, Git just moves the pointer forward.

No merge commit needed. Clean and simple.

> **Speaker note:** Draw it as a straight line.

---

## Slide 6: Today's Mission

1. Check your branch (`git branch`)
2. Create `fix-typo`
3. Switch to it
4. Fix the file
5. Commit
6. Switch to `main` — verify it's still broken
7. Switch back — verify it's fixed
8. Merge
9. Delete the branch

> **Speaker note:** Students should follow along in real time.

---

---

# SESSION 3: "Submitting Your Work"
## GitHub Remotes, Push, Pull, and Pull Requests

---

## Slide 1: Your Code Is on Your Laptop

**Problem:** Your boss can't see it. Your teammates can't see it.

**Solution:** Bring it to the library.

> **Speaker note:** Transition: "Your desk → the school library."

---

## Slide 2: GitHub Is the Library

GitHub is a website that stores your repo so others can:
- View it
- Review it
- Comment on it
- Approve it

**Your laptop = your bedroom desk.**
**GitHub = the school library.**

> **Speaker note:** Ask: "Would you write homework on your desk and never show anyone?"

---

## Slide 3: The Workflow

```
Local:    [create branch] → [make changes] → [commit]
                                ↓
Remote:                        [push]
                                ↓
GitHub:   [open Pull Request] → [review] → [merge]
                                ↓
Local:                        [pull]
```

> **Speaker note:** This diagram should be on the wall by the end of the course.

---

## Slide 4: What Is a Pull Request?

A Pull Request is a **permission slip**:

> "I want to add my homework to the class folder.
> Please check it first."

Your teacher reviews it, says "Looks good!", and signs it.

**In DevOps:** Nobody pushes to `main` directly. All changes go through PR + code review.

> **Speaker note:** Emphasize: this is how real companies work.

---

## Slide 5: Code Review Catches Bugs

Without PRs:
```
You → push to main → BUG IN PRODUCTION → customers angry
```

With PRs:
```
You → open PR → teammate sees bug → you fix it → merge → production safe
```

> **Speaker note:** This is why PRs exist. Not bureaucracy — safety.

---

## Slide 6: Today's Mission

1. Create a GitHub repo
2. Add `origin` remote to your local repo
3. Push `main` to GitHub
4. Create a feature branch (`feature-faq`)
5. Build the FAQ page, commit
6. Push the branch
7. Open a Pull Request on GitHub
8. Review it, approve it, merge it
9. Pull `main` locally
10. Delete branch

> **Speaker note:** This is the longest session. Pace carefully.

---

---

# SESSION 4: "The Deploy Broke!"
## Reverting, Conflicts, and Stash

---

## Slide 1: 3 AM Page

**Production is down.**

The last deploy was 20 minutes ago.
The website shows a white screen.
The boss is calling.

**You need to undo it — FAST.**

> **Speaker note:** Set tension. This is the real world.

---

## Slide 2: Use the Time Machine

1. Look at history (`git log --oneline`)
2. Find the bad commit
3. **Revert it** (`git revert BAD_COMMIT`)
4. Push the revert

**`git revert` creates a NEW commit that undoes the old one.**

History stays intact. The code goes back to working.

> **Speaker note:** Emphasize: we NEVER erase history in production.

---

## Slide 3: Revert vs. Delete

| | `git revert` | `git reset --hard` |
|---|---|---|
| **History** | Kept | Erased |
| **Safety** | Safe for shared repos | DANGEROUS |
| **Best for** | Production fixes | Local only |

> **Speaker note:** Write this on the board. Quiz students.

---

## Slide 4: What Is a Merge Conflict?

When two branches change the **same line**, Git says:

> "I don't know which version you want.
> You must tell me manually."

**This is normal. Don't panic.**

> **Speaker note:** Normalize conflicts. Students think they broke something.

---

## Slide 5: Conflict Markers

```
<<<<<<< HEAD
This is what your branch has
=======
This is what the other branch has
>>>>>>> other-branch
```

**Fix:** Edit the file. Remove the markers. Keep what you want.

> **Speaker note:** Show this in a text editor live.

---

## Slide 6: Git Stash — The Backpack

You're in the middle of something, but production is on fire.

1. **Stash** your work (put it in a backpack)
2. Fix the fire
3. **Pop** the stash (unpack your backpack)

> **Speaker note:** Mime putting a laptop in a backpack.

---

## Slide 7: Today's Mission

1. Break something on purpose (overwrite a file)
2. Commit the "bug"
3. Revert it
4. Verify the original is restored
5. Create a conflict scenario
6. Resolve it
7. Try `git stash` and `git stash pop`

> **Speaker note:** Session 4 is the most technical. Go slow.

---

---

# SESSION 5: "Automating Everything"
## CI/CD with GitHub Actions

---

## Slide 1: Robots Do the Boring Work

Every time someone pushes code, a **robot** can:
1. Check if required files exist
2. Run tests
3. Check formatting
4. Report PASS or FAIL

**You don't have to do it manually.**

> **Speaker note:** Tie everything together. This is the payoff.

---

## Slide 2: CI/CD Is the Heart of DevOps

| Without CI/CD | With CI/CD |
|---------------|------------|
| Developer pushes code | Developer pushes code |
| Team lead emails "Did you test?" | Robot tests immediately |
| Bug found in production | Bug caught before merge |
| Manual deployment | Automatic deployment |
| Blame and stress | Confidence and speed |

> **Speaker note:** This is why DevOps exists.

---

## Slide 3: The Recipe (YAML)

GitHub Actions uses **YAML** — like a recipe in a cookbook.

```yaml
name: Check Files
on:
  push:
    branches: [ main ]
jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: test -f index.txt && echo "OK"
```

> **Speaker note:** Don't explain every line yet. Just show it looks simple.

---

## Slide 4: The Robot Catches Mistakes

1. Create a branch
2. Delete a required file
3. Push and open PR
4. **Robot says: ❌ FAIL**
5. Bug caught BEFORE merge

> **Speaker note:** Emphasize: the robot is the safety net.

---

## Slide 5: Branch Protection = The Safety Lock

Lock `main` so:
- No direct pushes
- All changes must go through PR
- The robot must give a green checkmark

**This is how real DevOps teams protect production.**

> **Speaker note:** Use a padlock emoji or draw a lock.

---

## Slide 6: Today's Mission

1. Create `.github/workflows/check-files.yml`
2. Write a workflow that checks your files exist
3. Commit and push
4. Watch it pass ✅ in the Actions tab
5. Create a branch that breaks the build
6. See it fail ❌
7. Set up branch protection on `main`
8. Try to push directly — get blocked

> **Speaker note:** This is the graduation moment.

---

## Slide 7: Capstone Demo

**Show your work:**
- GitHub repo with all files
- Commit history with good messages
- Merged Pull Requests
- Passing Action
- Branch protection enabled

**You are now a DevOps engineer.**

---

*End of Approach 3 Slide Deck*
