#!/usr/bin/env python3
"""Validate local public-primer project manifests and scaffold boundaries."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from schema_subset import load_json, validate_instance


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "schemas" / "public-project.schema.json"
REQUIRED_STAGE_PHRASES = {
    "stage_3": ["Stage 3", "Human authority", "Acceptance criteria"],
    "stage_6": ["Stage 6", "Human authority", "Requirement traceability"],
    "stage_9": ["Stage 9", "Human authority", "Human release decision"],
    "field_trial": ["Field-Trial", "Human authority", "Consent and data boundary"],
}


def resolve_inside(root: Path, declared: str) -> Path:
    candidate = (root / declared).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"artifact path escapes project root: {declared}") from exc
    return candidate


def validate_project(project_root: Path) -> list[str]:
    errors: list[str] = []
    project_root = project_root.expanduser().resolve()
    manifest_path = project_root / "project.json"

    try:
        schema = load_json(SCHEMA_PATH)
        manifest = load_json(manifest_path)
    except ValueError as exc:
        return [str(exc)]

    if not isinstance(schema, dict) or not isinstance(manifest, dict):
        return ["schema and project manifest must both be JSON objects"]

    errors.extend(validate_instance(manifest, schema))
    if errors:
        return errors

    artifacts = manifest["artifacts"]
    declared_paths = list(artifacts.values())
    if len(set(declared_paths)) != len(declared_paths):
        errors.append("$.artifacts: stage and field-trial files must be distinct")

    for key, required_phrases in REQUIRED_STAGE_PHRASES.items():
        declared = artifacts[key]
        try:
            path = resolve_inside(project_root, declared)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if not path.is_file():
            errors.append(f"missing declared artifact {key}: {declared}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"could not read {declared}: {exc}")
            continue
        for phrase in required_phrases:
            if phrase not in text:
                errors.append(f"{declared}: missing required phrase {phrase!r}")

    readme = project_root / "README.md"
    if not readme.is_file():
        errors.append("missing README.md")
    else:
        try:
            readme_text = readme.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"could not read README.md: {exc}")
        else:
            authority = manifest["human_authority"]["role"]
            if authority not in readme_text:
                errors.append("README.md does not preserve the declared human authority")
            if "does not certify" not in readme_text:
                errors.append("README.md is missing the structural-validation claim boundary")

    return errors


def discover_default_projects() -> list[Path]:
    example = REPO_ROOT / "examples" / "scaffolded-project"
    return [example] if example.exists() else []


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate public-primer project folders")
    parser.add_argument("projects", nargs="*", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    projects = args.projects or discover_default_projects()
    if not projects:
        print("BLOCK: no project folders supplied or discovered", file=sys.stderr)
        return 1

    failed = False
    for project in projects:
        errors = validate_project(project)
        if errors:
            failed = True
            print(f"FAIL project: {project}", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
        else:
            print(f"PASS project: {project}")

    if failed:
        return 1

    print(f"PASS IN SCOPE: validated {len(projects)} public project scaffold(s)")
    print("NO CERTIFICATION: structural validation does not establish project quality or readiness")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
