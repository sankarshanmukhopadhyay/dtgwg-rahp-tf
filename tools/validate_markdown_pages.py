#!/usr/bin/env python3
"""Pre-Jekyll validation for Markdown and Pages-projected repository content.

This catches failures that GitHub's renderer/Jekyll would otherwise expose late:
- malformed YAML front matter;
- unbalanced fenced code blocks;
- literal ``\n`` accidentally embedded inside Mermaid diagrams;
- local Markdown links whose source target does not exist;
- Pages links to .html when the source is a corresponding .md file.

Final rendered-link validation remains the responsibility of validate_jtd_site.py.
"""
from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse, unquote
import json
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parent.parent
SKIP_PARTS = {".git", "_site", ".pytest_cache", "__pycache__", "vendor"}
# Frozen historical generated packages are retained for provenance and are not
# maintained as current authored Markdown.
SKIP_PREFIXES = ("archive/historical-builds/",)
STRUCTURED_ROOTS = ("corpora", "method", "data", "build/derived", "build/jsonld", "examples", "archive/historical-builds")
STRUCTURED_EXACT = (
    "instances/cawg/mandate-readiness.yaml",
    "instances/cawg/watch/issues.yaml",
    "instances/dtg/watch/issues.yaml",
)
STRUCTURED_EXTENSIONS = {".yaml", ".yml", ".json", ".jsonld"}

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^```.*$", re.M)
MERMAID_RE = re.compile(r"```mermaid\s*\n(.*?)```", re.S)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def source_target_exists(page: Path, href: str) -> bool:
    raw = href.strip()
    # Optional Markdown link titles follow whitespace after the destination.
    # Repository paths with spaces should be percent-encoded or enclosed in <>.
    if raw.startswith("<") and ">" in raw:
        raw = raw[1:raw.index(">")]
    elif re.search(r'\s+["\']', raw):
        raw = re.split(r'\s+["\']', raw, maxsplit=1)[0]
    raw = raw.strip("<>")
    if not raw or raw.startswith(("#", "mailto:", "javascript:", "tel:")):
        return True
    parsed = urlparse(raw)
    if parsed.scheme or parsed.netloc:
        return True
    path_text = unquote(parsed.path)
    if not path_text or "{{" in path_text or "{%" in path_text:
        return True

    if path_text.startswith("/rahp-toolkit/"):
        target = ROOT / path_text[len("/rahp-toolkit/"):]
    elif path_text.startswith("/dtgwg-rahp-tf/"):
        target = ROOT / path_text[len("/dtgwg-rahp-tf/"):]
    elif path_text.startswith("/"):
        # External/site-root paths outside this repository base are resolved
        # after Jekyll rendering.
        return True
    else:
        target = (page.parent / path_text).resolve()

    candidates = [target]
    if target.suffix.lower() == ".html":
        candidates.extend([target.with_suffix(".md"), target.parent / (target.stem + "/README.md")])
    elif target.suffix.lower() == ".md":
        candidates.extend([target.with_suffix(".html")])
    elif target.suffix == "":
        candidates.extend([
            target.with_suffix(".md"),
            target / "README.md",
            target / "index.md",
            target.with_suffix(".yaml"),
            target.with_suffix(".yml"),
            target.with_suffix(".json"),
            target.with_suffix(".jsonld"),
        ])

    return any(candidate.exists() for candidate in candidates)


def main() -> int:
    errors: list[str] = []
    pages = []
    for page in ROOT.rglob("*.md"):
        rp = rel(page)
        if any(part in SKIP_PARTS for part in page.parts):
            continue
        if rp.startswith(SKIP_PREFIXES):
            continue
        pages.append(page)

    for page in pages:
        text = page.read_text(encoding="utf-8", errors="replace")
        rp = rel(page)

        if text.startswith("---\n"):
            end = text.find("\n---\n", 4)
            if end < 0:
                errors.append(f"{rp}: unclosed YAML front matter")
            else:
                try:
                    parsed = yaml.safe_load(text[4:end]) or {}
                    if not isinstance(parsed, dict):
                        errors.append(f"{rp}: front matter must be a mapping")
                    elif not parsed.get("layout"):
                        errors.append(f"{rp}: front-matter page must declare a layout (use layout: default for Pages)")
                except Exception as exc:
                    errors.append(f"{rp}: invalid YAML front matter: {exc}")

        fences = FENCE_RE.findall(text)
        if len(fences) % 2:
            errors.append(f"{rp}: unbalanced fenced code blocks")

        for diagram in MERMAID_RE.findall(text):
            if "\\n" in diagram:
                errors.append(f"{rp}: literal \\\\n found inside Mermaid block")

        # Ignore code fences while checking prose links.
        prose = re.sub(r"```.*?```", "", text, flags=re.S)
        for href in LINK_RE.findall(prose):
            if not source_target_exists(page, href):
                errors.append(f"{rp}: unresolved local link: {href}")

    structured_paths: set[Path] = set()
    for root_name in STRUCTURED_ROOTS:
        structured_root = ROOT / root_name
        if structured_root.exists():
            structured_paths.update(
                p for p in structured_root.rglob("*")
                if p.is_file() and p.suffix.lower() in STRUCTURED_EXTENSIONS
            )
    structured_paths.update(
        ROOT / name for name in STRUCTURED_EXACT if (ROOT / name).exists()
    )

    structured_count = 0
    for path in sorted(structured_paths):
        structured_count += 1
        raw = path.read_text(encoding="utf-8", errors="strict")
        try:
            if path.suffix.lower() in {".yaml", ".yml"}:
                yaml.safe_load(raw)
            else:
                json.loads(raw)
        except Exception as exc:
            errors.append(f"{rel(path)}: projected structured data is not parseable: {exc}")

    if errors:
        for error in errors[:120]:
            print("ERROR", error)
        print(f"Markdown/Pages source validation failed: {len(errors)} error(s).")
        return 1

    print(f"Markdown/Pages source validation clean: {len(pages)} Markdown file(s), {structured_count} structured-data projection(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
