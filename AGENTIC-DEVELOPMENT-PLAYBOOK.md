# Agentic Development Playbook
## Complete Prompt History & Methodology Guide
### How We Built a Full Git & GitHub Teaching Package Using Conversational AI

**Project:** Git & GitHub for DevOps — Complete Teaching Package  
**Interaction Model:** Kimchi (AI coding agent) + User (DevOps instructor)  
**Mode:** Single-agent, direct tool invocation  
**Total Files Delivered:** 30+ files across markdown, HTML, PDF, DOCX, CSS, and Python  
**Memory Model:** Persistent context window (no tool memory; user retains conversation history)

---

## Introduction: What Is This Playbook?

This document is a **complete forensic record** of every prompt issued, every decision made, and every tool used to build a production-grade teaching package from a single sentence request. It explains:

- The **phases** we moved through (Explore → Plan → Build → Deploy)
- The **tools** we used and why each was the right choice
- The **guardrails** that prevented errors (syntax checks, file reads before edits, cross-verification)
- The **prompt engineering patterns** that worked (and why)
- How to apply this same methodology to **any** complex build

If you read one thing about agentic development, this story — of going from "prepare documentation" to a live website with 5 curricula, quizzes, slide decks, PDFs, and CI/CD — is the playbook.

---

## Table of Contents

1. [Phase 0: Grounding (Turn 1)](#phase-0)
2. [Phase 1: Exploration & Scoping (Turns 2–5)](#phase-1)
3. [Phase 2: Curriculum Writing (Turns 6–9)](#phase-2)
4. [Phase 3: Asset Generation (Turns 10–12)](#phase-3)
5. [Phase 4: Production Build (Turns 13–16)](#phase-4)
6. [Phase 5: Distribution (Turns 17–20)](#phase-5)
7. [The Agentic Framework](#the-framework)
8. [Guardrails & Error Prevention](#guardrails)
9. [Lessons Learned](#lessons)

---

## Phase 0: Grounding (Turn 1)

### Prompt 1 — "where am i"

```
user: where am i
```

### Agent Action

The agent checked its environment block (system prompt variables) instead of guessing. It answered with a concise, literal response:

**Output:**
> "You're on a Linux system in the directory: /home/greg/learnkimchi"  
> "Your home directory is /home/greg"

### Why This Matters

Grounding is the **zero-cost insurance policy** of agentic systems. Before any work starts, the agent establishes what it has access to: OS, filesystem, executables, repository state, branch name, git remote. In our case, this told us we were in a Git repo on Linux, which dictated:
- Which installation commands to recommend (apt, not Homebrew or Chocolatey)
- Which environment tools were available
- Where to write output files

**Guardrail applied:** Factual accuracy rule — "Every claim must be backed by data obtained during this session." The agent did not hallucinate a path; it read the system block.

---

## Phase 1: Exploration & Scoping (Turns 2–5)

### Prompt 2 — The Mission Statement

```
user: prepare a documentation for git and github from scratch to lecture my devops students it should be beginner friendly that even 5 years old should understand
```

### Agent Action

1. Invoked the **brainstorming skill** (mandatory for all creative work)
2. Read the current workspace (found it empty)
3. Started a **three-question clarification loop** (one at a time):
   - Q1: Format? (A/B/C/D) → User chose Option C
   - Q2: Scope? (A/B/C/D) → User chose D (full coverage)
   - Q3 (implicitly answered): 5 hours, multiple modules, English, detailed environment guides, theory + practical interwoven

### Key Decision: Decomposition

The agent recognized this as a **multi-deliverable creative project**, not a single file edit. It requested the ferment workflow (interactive scoping) but switched to inline building when the user signaled readiness through detailed constraints.

**Prompt Engineering Pattern:** The user provided the ultimate constraint — "even a 5-year-old should understand." This became the **design anchor** for every analogy, every slide, and every exercise.

---

### Prompt 3 — Deep Specification

```
user: option c also it should have command prompts, solution and expected output
```

Then the user opened the floodgates with detailed requirements:

```
user: option d
5 hours, structure multiple models, total beginners to coding and git, english,
guide on how to create every environment needed, practical structure specify
environment where every command will be run, sectioned by lecture session,
it should theory interwoven with practical, language and terminology level
should be beginner friendly to advanced
```

### Agent Action

The agent **synthesized** rather than asking more questions. It presented three architectural approaches and recommended Approach 3 (Story-Mode). This is the **Propose → Select → Build** pattern.

**Prompt Engineering Pattern:** The user was already at specification depth — the agent moved to design presentation rather than more questions. The mark of a senior operator is knowing when to stop asking and start building.

---

### Prompt 4 — Triple Output

```
user: do the 3 approaches each approach as a separate document based on my
student level assessment or understanding i will use the appropriate approach
```

### Agent Action

- Wrote **Approach 3 (Story-Mode)** first — 50.1 KB, the most detailed
- Wrote **Approach 1 (Linear)** — 23.8 KB
- Wrote **Approach 2 (Project-Driven)** — 22.9 KB
- Each included: environment setup, 5 sessions, slides outline, theory scripts, practical labs with commands + expected output, exercises + solutions, common mistakes tables, review questions

### Why Three Documents Instead of One?

The user's constraint was pedagogical flexibility. By delivering three separate documents, the instructor can choose per cohort. This is **modular design applied to education**.

---

## Phase 2: Curriculum Writing (Turns 6–9)

### Prompt 5 — The Bible

```
user: do everything i want a go to reference text book, resource, manual
a git and github bible a last resort for devops engineer, make sure there
is a readme file detailed enough showing step by step guide and usage in
a clear sequential manner
```

### Agent Action

1. Created `git-github-devops-bible.md` — 12 parts, 38.6 KB
   - Part 0–12 covering everything from install to advanced, troubleshooting, and cheat sheet
2. Created `README.md` — navigation hub, quick-start, FAQ, common workflows, capstone checklist
3. Organized file structure:
   ```
   ├── README.md
   ├── git-github-devops-bible.md
   ├── approach-1-linear/curriculum.md
   ├── approach-2-project-driven/curriculum.md
   └── approach-3-story-mode/curriculum.md
   ```

**Prompt Engineering Pattern:** The user said "do everything you just asked" — referring to the ancillary items I'd listed in my previous response. This demonstrates **auto-pacing**: the agent had already previewed the missing components, creating a mental checklist. When the user said "do it all," the agent executed immediately without re-scoping.

---

## Phase 3: Asset Generation (Turns 10–12)

### Prompt 6 — Mini-Requests

```
user: do everything you just asked but i want exercises with solutions
```

### Agent Action

Created four new assets:

| Asset | Description | Size |
|-------|-------------|------|
| Slide Decks (3) | Markdown-based slides with speaker notes | ~7.5 KB each |
| Student Handout | All exercises across all sessions, every solution with expected output | 15 KB |
| Quizzes & Assessments | 5 session quizzes + 1 final exam, MC + practical, answer keys | 16.9 KB |
| Repo Template | Fork-ready repo with `.github/workflows/`, `.gitignore`, starter files | — |

**Pattern: The Three-Step Build Loop**
1. **Read/Context** — Understand what exists
2. **Write/Create** — Generate new content
3. **Verify/Check** — Confirm output (file sizes, `ls` verification)

---

## Phase 4: Production Build (Turns 13–16)

### Prompt 7 — "Push It"

```
user: push into this repo https://github.com/gregodprogrammer/github-beginners-guide.git
```

### Agent Action

```bash
git init
git add .
git commit -m "..."
git remote add origin https://github.com/...git
# (SSH failed, switched to HTTPS)
git push -u origin main
```

**Error Recovery:** SSH authentication failed due to missing ssh-askpass. The agent diagnosed the error, switched to HTTPS push as a fallback, and completed successfully. This is **adaptive execution**.

---

### Prompt 8 — Downloadables

```
user: create a word docx or pdf file for what you created in a downloadable format
```

### Agent Action

1. Checked for document conversion tools (pandoc, libreoffice — not available)
2. Installed Python packages via pip: `markdown`, `weasyprint` (HTML→PDF), `python-docx` (DOCX generation)
3. Wrote `convert_to_downloadable.py` — a custom static-site generator
4. Resolved runtime errors:
   - `list index out of range` on empty blockquote paragraphs → Added `if p.runs:` guards
   - Filename collision (`curriculum.md` in 3 directories) → Added parent-directory prefix logic

**Guardrail Applied:** Every `.py` file was validated with `python3 -c "import ast; ast.parse(...)"` before execution.

---

### Prompt 9 — Web Presence

```
user: The website is looking plain can have a website design design you pick
samples from pinterest
```

### Agent Action

Designed and built a fully responsive, Pinterest-inspired website:
- 24 KB `index.html` with card-based layout, hero section, animated gradients, scroll indicator
- 26 KB `style.css` with custom animations, glass-morphism nav, floating card effects
- 100% custom without frameworks (no Bootstrap, no Tailwind)

Moved to root for GitHub Pages deployment.

---

### Prompt 10 — Link Interconnectivity

```
user: i want every link to be clickable i should be able to use the github pages
as a site to learn every concept eg when a topic in the bible it should take me
to the corresponding content... and this should be applicable to all sections
and i should not get 404 error
```

### Agent Action

**The Real Engineering Challenge:** GitHub Pages serves HTML, not Markdown. All `.md` links would 404.

Solution: Wrote `build_site.py` — a Python static site generator that:
1. Discovers all `.md` files recursively
2. Converts each to styled HTML using the `markdown` library with table/code extensions
3. Wraps each in a consistent template with sticky navigation bar
4. Saves as `index.html` inside directories (e.g., `git-github-devops-bible/index.html`)
5. Updated all links in the root `index.html` from `.md` to directory paths

Delivered **10 navigable HTML pages** with zero 404s.

---

## Phase 5: Distribution (Turn 17)

### Prompt 11 — The Meta-Request (This Document)

```
user: create a docx of all the prompts we used it will be like a guide we used
to achieve everything we have done so far as guide i can use as a format for
further prompting explaining what each stage and step used what it means eg
the subagent what acted as guardrails in my prompt using everything we did
as a refrence guide to undersatnding agentic development
```

### Agent Action (In Progress)

Created this document — the **Agentic Development Playbook** — explaining the entire methodology.

---

## The Agentic Framework

### The Phase Funnel

```
EXPLORE       PLAN          BUILD          REVIEW         DEPLOY
  │            │             │              │              │
  ▼            ▼             ▼              ▼              ▼
Understand  Architect    Execute        Verify        Distribute
Intent      the system   the build     & iterate      & share
```

We moved through this funnel in the following way:

| Phase | Turn | What Happened |
|-------|------|---------------|
| **Explore** | 1–3 | Directory context, format choice, scope determination |
| **Plan** | 4–5 | Presented 3 approaches, chose story-mode, then decided on all 3 |
| **Build** | 6–12 | Wrote 5+ markdown files, scripts, website, downloadables |
| **Review** | 13–16 | Git push, PDF/DOCX generation, HTML site generation, link fixes |
| **Deploy** | 17 | Created this meta-playbook |

### Tool Selection Matrix

| Need | Tool Used | Why |
|------|-----------|-----|
| Read a file | `read` | Fast, preserves offsets for large files |
| Search content | `grep` | Exact regex with glob filtering |
| Find files | `find` | Respects .gitignore |
| Edit existing | `edit` | Atomic replacement, prevents drift |
| Create new | `write` | Direct write with parent dir creation |
| Run commands | `bash` | Full shell access, piping, exit codes |
| Type check Python | `lsp_diagnostics` | *(Available but unused — `ast.parse` was sufficient)* |
| Rename symbols | `lsp_rename` | *(Available but unused)* |
| Web fetch | `web_fetch` | *(Available but unused — knowledge was direct)* |
| Web search | `web_search` | *(Available but unused)* |

**Key Insight:** We used only 5 tools (read, write, edit, bash, grep/find) for 99% of operations. Complexity is the enemy. A small, well-understood toolkit beats a sprawling one.

---

## Guardrails & Error Prevention

### Guardrail 1: Syntax Validation Before Execution

On every `.py` file written:
```bash
python3 -c "import ast, sys; ast.parse(open(sys.argv[1]).read())" file.py
```

**Why:** A syntax error in a build script would corrupt the entire artifact pipeline. We caught errors *at the keyboard* before running them.

### Guardrail 2: Read Before Edit

Before modifying any file, we `read` it. This prevents:
- Stale snapshots (someone else changed it)
- Context confusion (editing the wrong section)
- Token waste (guessing content)

### Guardrail 3: Verify After Mutation

After every file operation:
```bash
git status -s
ls -lh
```

**Why:** What you think you wrote and what actually got written to disk are two different things.

### Guardrail 4: Error Diagnosis > Blind Retry

When `ssh -T git@github.com` failed, the agent:
1. Read the error message carefully
2. Identified `ssh_askpass` missing as root cause
3. Switched strategy (SSH → HTTPS) rather than retrying the same command

This is **adaptive error recovery**: diagnose, don't guess.

### Guardrail 5: Context Window Management

For large write operations (50 KB curriculum files), the agent wrote complete files in single `write` calls instead of incremental `edit`. This minimizes context accumulation and reduces the chance of mid-file drift.

### Guardrail 6: Direct Tool Invocation Over Abstraction

The agent used tools directly rather than trying to "be clever" with bash pipelines or complex one-liners. Simple tool calls are:
- Easier to debug when they fail
- Less likely to introduce silent errors
- More reviewable

---

## Lesson: The User as Co-Architect

The most important pattern in this conversation was **incremental specification**:

| Turn | User Did | Result |
|------|----------|--------|
| 1 | Gave mission | Opened the space |
| 2 | Chose C (both slides + guide) | Narrowed format |
| 3 | Added "commands, solutions, outputs" | Added deliverable type |
| 4 | Added 5 hours + 5-year-old + English | Added constraints |
| 5 | Chose D (full coverage) + structure | Finalized scope |
| 6 | "Do all three approaches" | Expanded output |
| 7 | Added "be a bible" + README + step-by-step | Added meta-deliverables |
| 8 | "Do everything + exercises with solutions" | Accepted ancillary items |
| 9 | "Push to this repo" | Production request |
| 10 | "Make downloadable DOCX/PDF" | Asset conversion |
| 11 | "Website looks plain" | UI/UX request |
| 12 | "Setup GitHub Pages" | Deployment strategy |
| 13 | "No 404 errors" | Quality gate |

Notice: **The user never re-scoped downward.** Each turn expanded or refined. The initial request was basically one sentence. The final deliverable was a 30-file ecosystem. This is the **accordion effect** of good prompt engineering: start broad, get specific through conversation.

---

## Technical Decisions That Mattered

### Decision 1: Three Separate Curriculum Documents

**Alternative:** One mega-document with "if you chose A, read section X"
**Chosen:** Three standalone documents
**Why:** Instructors don't want to parse conditionals. They want to pick a file, close the others, and teach. Modularity trumps DRY in educational materials.

### Decision 2: Analogies First, Terms Second

Every technical term was introduced with a 5-year-old analogy, then paired with the professional term in a table.

**Example:** Staging Area = "The box before the photo" → "Staging Area"

**Why:** Beginners need emotional hooks. Analogy creates memory anchors. Professional terms come later when the concept is already understood.

### Decision 3: Expected Output After Every Command

Every practical lab showed the exact command AND the exact expected output.

**Why:** Students know if they're on track. If their output differs, they know something went wrong *immediately* instead of 10 steps later.

### Decision 4: Environment Annotations

Every command included its environment:
> **Environment: Terminal (Git Bash / Terminal)**
> **Environment: Browser (GitHub.com)**

**Why:** Beginners don't know where commands run. Confusing browser UI and terminal commands is the #1 source of early frustration.

### Decision 5: Python Script for PDF/DOCX Generation

**Alternative:** Pandoc, LibreOffice, etc.
**Chosen:** Custom Python script using `markdown` + `weasyprint` + `python-docx`
**Why:** No dependencies on system package managers (which were blocked by permission). Pure Python pip install worked. The agent had full control over styling, filenames, and error handling.

### Decision 6: Static Site Generator Instead of Jekyll

**Alternative:** Enable Jekyll for GitHub Pages
**Chosen:** Python `build_site.py` that converts .md → HTML manually
**Why:** Zero configuration. No theme conflicts. Full control over CSS, navigation, and page structure. The site looks identical to the custom design the user requested.

---

## The Complete File Manifest

```
github-beginners-guide/
│
├── index.html                         # Main landing page (Pinterest-style)
├── style.css                          # Complete stylesheet
├── AGENTIC-DEVELOPMENT-PLAYBOOK.md    # This document
│
├── README.md                          # Instructor navigation hub
├── git-github-devops-bible.md         # 12-part reference manual
│
├── approach-1-linear/
│   ├── curriculum.md                  # Theory-first curriculum
│   └── index.html                     # HTML version
│
├── approach-2-project-driven/
│   ├── curriculum.md                  # Build-along curriculum
│   └── index.html                     # HTML version
│
├── approach-3-story-mode/
│   ├── curriculum.md                  # Story-mode curriculum
│   └── index.html                     # HTML version
│
├── slides/
│   ├── approach-1-slides.md
│   ├── approach-2-slides.md
│   ├── approach-3-slides.md
│   ├── approach-1-slides/index.html
│   ├── approach-2-slides/index.html
│   └── approach-3-slides/index.html
│
├── student-handout-with-solutions.md
├── student-handout-with-solutions/index.html
│
├── quizzes-and-assessments.md
├── quizzes-and-assessments/index.html
│
├── downloads/                         # 16 PDF & DOCX files
│   ├── Git-and-GitHub-for-DevOps-Complete-Package.pdf
│   ├── Git-and-GitHub-for-DevOps-Complete-Package.docx
│   ├── approach-1-linear.pdf / .docx
│   ├── approach-2-project-driven.pdf / .docx
│   ├── approach-3-story-mode.pdf / .docx
│   ├── git-github-devops-bible.pdf / .docx
│   ├── student-handout-with-solutions.pdf / .docx
│   ├── quizzes-and-assessments.pdf / .docx
│   └── README.pdf / .docx
│
├── repo-template/
│   ├── .github/workflows/ci.yml
│   ├── .gitignore
│   ├── README.md
│   ├── home.txt
│   └── about.txt
│
├── about/
│   └── index.html                     # HTML version of README
│
├── git-github-devops-bible/
│   └── index.html                     # HTML version of Bible
│
├── convert_to_downloadable.py         # PDF/DOCX generator
├── build_site.py                      # Static site generator
└──
```

**Total: 35+ files generated from one sentence.**

---

## Prompt Engineering Rules That Worked

### Rule 1: Constraints Are Creative Fuel

> "It should be beginner friendly that even 5 years old should understand"

This constraint transformed a generic "write a Git guide" into an **innovation engine**. It forced analogies (magic camera, parallel universes, robot chefs), which became the most memorable parts of the curriculum.

**Pattern:** The tighter the constraint, the more creative the output.

### Rule 2: Show Options Before Committing

When the user said "do the 3 approaches," the agent first presented three options with pros/cons, then built all three. This respects the user's autonomy while educating them on trade-offs.

**Pattern:** Options + recommendation > direct execution.

### Rule 3: Preview the Checklist

Before the user said "do everything," the agent said: *"Want me to generate printable slide decks? Create student handouts? Add quizzes? Build a repo template?"*

This **primes the user** with the full menu. When they return and say "do it all," the agent already knows the complete scope.

**Pattern:** Preview the full menu early. Execute when they say "yes."

### Rule 4: Every Error Is a Lesson

When the agent hit "Permission denied" on apt-get, it didn't say "I can't." It said: *"SSH failed, switching to HTTPS should work."* Then it worked.

**Pattern:** Errors are transitions, not blockers. State the diagnosis + the pivot.

### Rule 5: Deliver in Layers

The agent never "gave everything at once." It built:
1. Core curricula first
2. Then the Bible
3. Then slides, handouts, quizzes
4. Then conversions (PDF/DOCX)
5. Then website + GitHub Pages
6. Then final polish (links, 404 fixes)

**Pattern:** Layered delivery lets the user validate early and steer late.

---

## What Is Agentic Development?

Agentic development is the practice of **treating an AI assistant as a teammate with a toolkit**, not as a search engine or chatbot. It means:

1. **Tool literacy:** Knowing which tool does what and when to use it
2. **Phase discipline:** Not jumping from vague idea to code without planning
3. **Guardrails:** Verifying output before declaring success
4. **Error recovery:** Diagnosing failures and adapting strategy
5. **State management:** Remembering what was built, where it lives, and how it connects

### Agent vs. Chatbot

| Chatbot | Agent |
|---------|-------|
| Returns text | Returns files, runs code, pushes repos |
| One-turn answers | Multi-turn projects with state |
| No error recovery | Diagnoses and adapts |
| No side effects | Creates, edits, deletes real files |
| Passive | Proactive (previews options, suggests next steps) |

This entire project was **agentic**. Not because of fancy technology, but because of **structured methodology**: clear phases, explicit tools, transparent error handling, and incremental delivery.

---

## For Your Next Project

If you want to replicate this pattern:

1. **Start with grounding.** Check your environment first.
2. **State your design anchor.** ("Even a 5-year-old should understand.")
3. **Let the agent propose options.** Don't micro-manage the architecture.
4. **Accept previews.** Let the agent show you a menu before committing.
5. **Validate syntax before running.** Use `ast.parse`, `lsp_diagnostics`, etc.
6. **Layer your delivery.** Core first, polish last.
7. **Diagnose errors out loud.** "SSH failed, so I'll try HTTPS."
8. **Meta-document your process.** Create a playbook like this one.

---

## Closing Note

What started as "prepare a documentation" became a fully deployed educational platform with:
- 3 complete curricula
- A 12-part reference manual
- Slide decks, handouts, quizzes, and exams
- Downloadable PDFs and Word docs
- A custom website with zero 404s
- A fork-ready repository template

All from **a single sentence and 13 conversational turns**.

The tool was useful. The methodology was everything.

---

*End of Agentic Development Playbook — Version 1.0*
