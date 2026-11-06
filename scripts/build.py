#!/usr/bin/env python3
"""Build README.md and dist/FULL.md from scripts/README.template.md and modules/*.md.

Usage:
  python scripts/build.py --repo YOUR_USER/YOUR_REPO [--branch main]
In GitHub Actions the repo is taken from GITHUB_REPOSITORY automatically.
"""
import argparse, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORDER = ["product-map", "styles", "landing-patterns", "palettes", "typography", "ux-rules", "charts", "stacks"]
README_LIMIT_CHARS = 16000   # ~6k tokens, README must stay small

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", "YOUR_USER/YOUR_REPO"))
    ap.add_argument("--branch", default="main")
    a = ap.parse_args()

    raw = f"https://raw.githubusercontent.com/{a.repo}/{a.branch}"
    def sub(text):
        return text.replace("{{RAW}}", raw).replace("{{REPO}}", a.repo)

    template = (ROOT / "scripts" / "README.template.md").read_text(encoding="utf-8")
    readme = sub(template)
    (ROOT / "README.md").write_text(readme, encoding="utf-8")

    start_tpl = ROOT / "scripts" / "START.template.md"
    if start_tpl.exists():
        (ROOT / "prompts").mkdir(exist_ok=True)
        (ROOT / "prompts" / "START.md").write_text(sub(start_tpl.read_text(encoding="utf-8")), encoding="utf-8")

    # FULL.md = README body without the human section + all modules
    body = readme.split("\n---\n\n## Для человека")[0]
    parts = [body.rstrip(), ""]
    for name in ORDER:
        p = ROOT / "modules" / f"{name}.md"
        if not p.exists():
            print(f"warning: missing {p}", file=sys.stderr)
            continue
        parts += ["\n---\n", p.read_text(encoding="utf-8").strip(), ""]
    # modules not listed in ORDER are appended too, so nothing is lost
    for p in sorted((ROOT / "modules").glob("*.md")):
        if p.stem not in ORDER:
            parts += ["\n---\n", p.read_text(encoding="utf-8").strip(), ""]
    (ROOT / "dist").mkdir(exist_ok=True)
    full = "\n".join(parts)
    (ROOT / "dist" / "FULL.md").write_text(full, encoding="utf-8")

    print(f"README.md: {len(readme):,} chars (~{len(readme)//4:,} tokens)")
    print(f"dist/FULL.md: {len(full):,} chars (~{len(full)//4:,} tokens)")
    if len(readme) > README_LIMIT_CHARS:
        print("warning: README is large; move details into modules/", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
