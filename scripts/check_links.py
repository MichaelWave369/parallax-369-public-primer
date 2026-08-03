#!/usr/bin/env python3
"""Check local Markdown/HTML links and static-site entry points without network access."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


REPO_ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__"}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)
        for attribute in ("href", "src"):
            target = values.get(attribute)
            if target:
                self.links.append(target)


def discover_files(suffix: str) -> list[Path]:
    return sorted(
        path
        for path in REPO_ROOT.rglob(f"*{suffix}")
        if not any(part in SKIP_DIRS for part in path.parts)
    )


def markdown_targets(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    targets: list[str] = []
    in_fence = False
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in MARKDOWN_LINK.finditer(line):
            raw = match.group(1).strip()
            if raw.startswith("<") and ">" in raw:
                raw = raw[1 : raw.index(">")]
            elif " " in raw:
                raw = raw.split(" ", 1)[0]
            targets.append(raw)
    return targets


def html_data(path: Path) -> tuple[list[str], set[str]]:
    parser = LinkParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.links, parser.ids


def resolve_target(source: Path, raw_target: str) -> tuple[Path | None, str]:
    parsed = urlsplit(raw_target)
    if parsed.scheme.lower() in EXTERNAL_SCHEMES or parsed.netloc:
        return None, ""
    if not parsed.path and not parsed.fragment:
        return None, ""

    decoded_path = unquote(parsed.path)
    if decoded_path.startswith("/"):
        candidate = REPO_ROOT / "docs" / decoded_path.lstrip("/")
    elif decoded_path:
        candidate = source.parent / decoded_path
    else:
        candidate = source

    candidate = candidate.resolve()
    try:
        candidate.relative_to(REPO_ROOT.resolve())
    except ValueError:
        return candidate, parsed.fragment

    if candidate.is_dir():
        if (candidate / "index.html").is_file():
            candidate = candidate / "index.html"
        elif (candidate / "README.md").is_file():
            candidate = candidate / "README.md"

    return candidate, parsed.fragment


def check_target(source: Path, raw_target: str, html_ids: dict[Path, set[str]]) -> list[str]:
    candidate, fragment = resolve_target(source, raw_target)
    if candidate is None:
        return []

    try:
        candidate.relative_to(REPO_ROOT.resolve())
    except ValueError:
        return [f"{source.relative_to(REPO_ROOT)}: target escapes repository: {raw_target}"]

    if not candidate.exists():
        return [f"{source.relative_to(REPO_ROOT)}: missing local target {raw_target}"]

    if fragment and candidate.suffix.lower() == ".html":
        ids = html_ids.get(candidate)
        if ids is None:
            _, ids = html_data(candidate)
            html_ids[candidate] = ids
        if fragment not in ids:
            return [
                f"{source.relative_to(REPO_ROOT)}: missing HTML fragment #{fragment} in {candidate.relative_to(REPO_ROOT)}"
            ]
    return []


def static_site_checks() -> list[str]:
    errors: list[str] = []
    required = [
        "docs/index.html",
        "docs/styles.css",
        "docs/app.js",
        "docs/primer.html",
        "docs/primer.css",
        "docs/validation.html",
        "docs/quickstart.html",
        "docs/.nojekyll",
    ]
    for relative_path in required:
        if not (REPO_ROOT / relative_path).exists():
            errors.append(f"missing static-site artifact {relative_path}")

    for html_path in discover_files(".html"):
        text = html_path.read_text(encoding="utf-8").lower()
        if "<title>" not in text:
            errors.append(f"{html_path.relative_to(REPO_ROOT)}: missing title element")
        if "<main" not in text:
            errors.append(f"{html_path.relative_to(REPO_ROOT)}: missing main element")
        if 'lang="' not in text and "lang='" not in text:
            errors.append(f"{html_path.relative_to(REPO_ROOT)}: missing document language")
    return errors


def main() -> int:
    markdown_files = discover_files(".md")
    html_files = discover_files(".html")
    html_ids: dict[Path, set[str]] = {}
    errors = static_site_checks()
    checked = 0

    for path in markdown_files:
        for target in markdown_targets(path):
            checked += 1
            errors.extend(check_target(path, target, html_ids))

    for path in html_files:
        targets, ids = html_data(path)
        html_ids[path.resolve()] = ids
        for target in targets:
            checked += 1
            errors.extend(check_target(path, target, html_ids))

    if errors:
        for error in errors:
            print(f"FAIL link/site: {error}", file=sys.stderr)
        return 1

    print(
        f"PASS: checked {checked} local link reference(s), {len(html_files)} HTML page(s), and required static-site artifacts"
    )
    print("NOTE: external links were not fetched or validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
