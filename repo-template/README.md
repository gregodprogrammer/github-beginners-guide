# DevOps Portfolio Template

> **A starter template for your Git & GitHub DevOps course project.**

This template gives you a ready-to-use repository with:
- ✅ A basic project structure
- ✅ A working GitHub Actions CI workflow
- ✅ A `.gitignore` file
- ✅ A sample README

**Use this as your starting point** and customize it for your own portfolio.

---

## How to Use This Template

### Option 1: Fork This Repo (Easy)

1. On GitHub, click the **"Use this template"** button (or **Fork**)
2. Name your new repo (e.g., `my-devops-portfolio`)
3. Clone it to your computer:
   ```bash
   git clone git@github.com:YOURNAME/my-devops-portfolio.git
   cd my-devops-portfolio
   ```

### Option 2: Create From Scratch

```bash
git init
# Copy these files into your repo
git add .
git commit -m "Initial commit from template"
git remote add origin git@github.com:YOURNAME/my-devops-portfolio.git
git branch -M main
git push -u origin main
```

---

## Project Structure

```
my-devops-portfolio/
├── .github/
│   └── workflows/
│       └── ci.yml        ← GitHub Actions workflow
├── .gitignore            ← Files Git should ignore
├── README.md             ← This file (replace with your info)
├── home.txt              ← Home page
├── about.txt             ← About page
└── ...                   ← Add more pages as you learn
```

---

## The CI Workflow

This template includes `.github/workflows/ci.yml` which:
1. Runs on every push and pull request to `main`
2. Checks that required files exist
3. Reports pass or fail

**Check the Actions tab on GitHub to see it run!**

---

## Customize This README

Replace the content above with your own portfolio info:

```markdown
# My DevOps Portfolio

Hi! I'm [Your Name].

This portfolio demonstrates my Git, GitHub, and CI/CD skills.

## Pages
- [home.txt](home.txt) - Welcome page
- [about.txt](about.txt) - About me
- [projects.txt](projects.txt) - My projects

## CI/CD
This repo has automated checks via GitHub Actions.

Last updated: [Date]
```

---

## What You Learned

By using this template and the course materials, you now have:
- A Git repository with good commit history
- GitHub Actions CI/CD pipeline
- Branch protection on `main`
- Clean project structure

**Add this to your resume:**
> "Proficient in Git version control, GitHub collaboration, Pull Requests, code review, and CI/CD pipelines."

---

*Template from the Git & GitHub for DevOps course.*
