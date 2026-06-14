#!/usr/bin/env python3
"""
Convert ALL markdown files into beautiful, navigable HTML pages.
This turns the repo into a fully functional static website with no 404s.
"""
import os
import sys
import markdown
from pathlib import Path

BASE = Path("/home/greg/learnkimchi")

# CSS shared by ALL content pages
CONTENT_CSS = """
:root {
    --bg: #ffffff;
    --bg-warm: #f6f8fa;
    --text: #1f2328;
    --text-sec: #656d76;
    --text-muted: #8c959f;
    --accent: #2dba4e;
    --accent-soft: #3fb950;
    --navy: #0d1117;
    --navy-light: #161b22;
    --border: rgba(31,35,40,0.08);
    --radius: 12px;
    --font-head: 'Space Grotesk', 'Inter', system-ui, sans-serif;
    --font-body: 'Inter', system-ui, sans-serif;
}
* { margin:0; padding:0; box-sizing:border-box; }
html { scroll-behavior: smooth; }
body {
    font-family: var(--font-body);
    color: var(--text);
    background: var(--bg);
    line-height: 1.65;
    font-size: 15px;
    -webkit-font-smoothing: antialiased;
}

/* Top nav */
.topbar {
    position: sticky; top:0; z-index:1000;
    background: rgba(255,255,255,0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
    padding: 12px 24px;
    display: flex; align-items: center; justify-content: space-between;
}
.topbar-brand {
    display: flex; align-items: center; gap: 8px;
    font-family: var(--font-head); font-size: 1.1rem; font-weight: 700;
    color: var(--text); text-decoration: none;
}
.topbar-brand span { color: var(--accent); }
.topbar-nav { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.topbar-nav a {
    color: var(--text-sec); text-decoration: none; font-size: 0.8rem;
    font-weight: 500; padding: 6px 12px; border-radius: 100px;
    background: var(--bg-warm); transition: 0.2s;
}
.topbar-nav a:hover { color: var(--text); background: #eef1f4; }
.topbar-home { background: var(--accent) !important; color: white !important; }
.topbar-home:hover { background: var(--accent-soft) !important; }

/* Layout */
.page { max-width: 920px; margin: 0 auto; padding: 40px 24px 80px; }
.page-title {
    font-family: var(--font-head); font-size: 2.2rem; font-weight: 700;
    margin-bottom: 8px; line-height: 1.2;
}
.page-subtitle { color: var(--text-sec); margin-bottom: 32px; font-size: 1rem; }

/* Typography */
h1, h2, h3, h4 { font-family: var(--font-head); line-height: 1.3; }
h1 { font-size: 1.8rem; margin: 40px 0 16px; color: var(--navy); }
h2 { font-size: 1.4rem; margin: 32px 0 12px; color: var(--navy-light); border-bottom: 1px solid var(--border); padding-bottom: 8px; }
h3 { font-size: 1.15rem; margin: 24px 0 10px; color: var(--text); }
h4 { font-size: 1rem; margin: 18px 0 8px; font-style: italic; color: var(--text-sec); }
p { margin-bottom: 14px; }
a { color: var(--accent); text-decoration: none; font-weight: 500; }
a:hover { text-decoration: underline; }

/* Code */
code {
    font-family: 'SF Mono', 'Fira Code', 'Courier New', monospace;
    background: #f4f4f5; padding: 2px 6px; border-radius: 4px;
    font-size: 0.88em; color: #d73a49;
}
pre {
    background: #f6f8fa; border: 1px solid var(--border);
    border-left: 4px solid var(--accent); padding: 16px;
    border-radius: var(--radius); overflow-x: auto;
    font-size: 0.85rem; line-height: 1.5; margin: 16px 0;
}
pre code { background: none; padding: 0; color: inherit; }

/* Tables */
table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 0.9rem; }
th, td { border: 1px solid var(--border); padding: 10px 12px; text-align: left; }
th { background: var(--navy); color: white; font-weight: 600; }
tr:nth-child(even) { background: var(--bg-warm); }

/* Blockquote */
blockquote {
    border-left: 4px solid var(--accent); margin: 16px 0;
    padding: 12px 18px; background: #f0fdf3; font-style: italic;
    border-radius: 0 var(--radius) var(--radius) 0;
}

/* Details / Summary */
details { background: #f0f5ff; border: 1px solid #dbe4f0; border-radius: var(--radius); margin: 16px 0; overflow: hidden; }
summary {
    padding: 12px 16px; font-weight: 600; cursor: pointer;
    color: var(--navy-light); background: #e6edfa;
    list-style: none;
}
details > *:not(summary) { padding: 16px; }
details pre { margin: 0; border-left-color: var(--accent-purple); }

/* Lists */
ul, ol { margin: 12px 0; padding-left: 24px; }
li { margin: 6px 0; }

/* Horizontal rule */
hr { border: none; border-top: 1px solid var(--border); margin: 32px 0; }

/* Image wrapper */
img { max-width: 100%; height: auto; border-radius: var(--radius); }

/* Footer inside page */
.page-footer {
    margin-top: 60px; padding-top: 24px;
    border-top: 1px solid var(--border);
    text-align: center; color: var(--text-muted);
    font-size: 0.85rem;
}

/* Responsive */
@media (max-width: 640px) {
    .page { padding: 24px 16px 60px; }
    .page-title { font-size: 1.6rem; }
    .topbar-nav { display: none; }
    pre { font-size: 0.78rem; padding: 12px; }
    table { font-size: 0.82rem; }
    th, td { padding: 8px; }
}
"""

# Navigation mapping for topbar (label, relative_url)
NAV_LINKS = [
    ("🏠 Home", "/"),
    ("📖 Bible", "/git-github-devops-bible/"),
    ("🎓 Linear", "/approach-1-linear/"),
    ("🚀 Project", "/approach-2-project-driven/"),
    ("📖 Story", "/approach-3-story-mode/"),
    ("📝 Exercises", "/student-handout-with-solutions/"),
    ("❓ Quizzes", "/quizzes-and-assessments/"),
]

def discover_md_files(base: Path):
    """Find all .md files and their relative paths."""
    skip = {"downloads", "repo-template", "website", ".git", ".github"}
    mds = []
    for f in sorted(base.rglob("*.md")):
        rel = f.relative_to(base)
        parts = rel.parts
        if parts[0] in skip:
            continue
        if f.name == "index.md":
            continue
        mds.append(rel)
    return mds

def make_slug(rel: Path):
    """Turn a markdown relative path into a slug (directory + filename without ext)."""
    if rel.name.lower() == "readme.md":
        return "about"
    if rel.name == "curriculum.md" and len(rel.parts) > 1:
        return str(rel.parent)
    # For root-level files, use stem
    if len(rel.parts) == 1:
        return rel.stem
    return str(rel.with_suffix(""))

def compute_url(slug: str):
    """HTML page URL relative to root."""
    return f"/{slug}/"

def compute_depth(rel_url: str):
    """How many ../ needed to reach root."""
    # Count actual directory segments by splitting on /
    parts = rel_url.split("/")
    return len([p for p in parts if p])

def relative_root(depth: int):
    if depth <= 0:
        return "./"
    return "../" * depth

def topbar_html(depth: int):
    root = relative_root(depth)
    links = []
    for label, url in NAV_LINKS:
        if url == "/":
            href = root
            cls = 'topbar-home'
        else:
            # Build relative path: go up 'depth' levels to root, then down to target
            parts = url.strip("/").split("/")
            href = "../" * depth + "/".join(parts) + "/"
            cls = ''
        links.append(f'<a href="{href}" class="{cls}">{label}</a>')
    return '\n'.join(links)

def wrap_html(title: str, body_html: str, depth: int, subtitle: str = "") -> str:
    root = relative_root(depth)
    nav = topbar_html(depth)
    sub = f'<p class="page-subtitle">{subtitle}</p>' if subtitle else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Git & GitHub for DevOps</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<style>{CONTENT_CSS}</style>
</head>
<body>
<nav class="topbar">
    <a href="{root}" class="topbar-brand">DevOps<span>Git</span></a>
    <div class="topbar-nav">
        {nav}
    </div>
</nav>
<main class="page">
    <h1 class="page-title">{title}</h1>
    {sub}
    {body_html}
    <div class="page-footer">
        <p>© Git & GitHub for DevOps Teaching Package — Free to use and share</p>
    </div>
</main>
</body>
</html>"""

def convert_md(md_path: Path, out_dir: Path, depth: int, title: str, subtitle: str = ""):
    """Convert one markdown file to a directory with index.html."""
    text = md_path.read_text(encoding="utf-8")
    body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "toc", "nl2br", "sane_lists"]
    )
    html = wrap_html(title, body, depth, subtitle)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    return out_dir

def build_all():
    md_files = discover_md_files(BASE)
    print(f"Found {len(md_files)} markdown files")

    # Map slugs to paths
    slug_to_dir = {}
    for rel in md_files:
        slug = make_slug(rel)
        slug_to_dir[slug] = BASE / slug

    # Convert each
    for rel in md_files:
        slug = make_slug(rel)
        out_dir = BASE / slug
        depth = compute_depth(compute_url(slug))
        nice_title = slug.replace("-", " ").replace("_", " ").title()

        # Nicer titles
        title_map = {
            "about": "About This Package",
            "git-github-devops-bible": "The DevOps Bible",
            "student-handout-with-solutions": "Student Handout",
            "quizzes-and-assessments": "Quizzes & Assessments",
            "slides/approach-1-slides": "Approach 1 Slides",
            "slides/approach-2-slides": "Approach 2 Slides",
            "slides/approach-3-slides": "Approach 3 Slides",
            "approach-1-linear": "Approach 1: Linear Lecture",
            "approach-2-project-driven": "Approach 2: Project-Driven",
            "approach-3-story-mode": "Approach 3: Story-Mode",
        }
        title = title_map.get(slug, nice_title)

        subtitle_map = {
            "about": "Navigation hub, quick start, and FAQ",
            "git-github-devops-bible": "12-part reference manual from beginner to advanced",
            "student-handout-with-solutions": "Every exercise with solutions and expected output",
            "quizzes-and-assessments": "Session quizzes + final exam with answer keys",
        }
        sub = subtitle_map.get(slug, "")

        convert_md(BASE / rel, out_dir, depth, title, sub)
        print(f"  ✅ {rel} → /{slug}/")

    print("\nAll content pages built!")

if __name__ == "__main__":
    build_all()
