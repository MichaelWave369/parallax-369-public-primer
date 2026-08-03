#!/usr/bin/env python3
"""Validate public-primer JSON receipts using the documented schema subset."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from schema_subset import load_json, resolve_repo_path, validate_instance


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RECEIPT_DIR = REPO_ROOT / "examples" / "receipts"


def receipt_paths(arguments: list[str]) -> list[Path]:
    if arguments:
        return [resolve_repo_path(REPO_ROOT, item) for item in arguments]
    return sorted(DEFAULT_RECEIPT_DIR.glob("*.json"))


def validate_receipt(path: Path) -> list[str]:
    try:
        instance = load_json(path)
    except ValueError as exc:
        return [str(exc)]

    if not isinstance(instance, dict):
        return [f"{path}: receipt root must be a JSON object"]

    schema_file = instance.get("schema_file")
    if not isinstance(schema_file, str) or not schema_file:
        return [f"{path}: missing non-empty schema_file"]

    try:
        schema_path = resolve_repo_path(REPO_ROOT, schema_file)
        schema = load_json(schema_path)
    except ValueError as exc:
        return [f"{path}: {exc}"]

    if not isinstance(schema, dict):
        return [f"{schema_path}: schema root must be a JSON object"]

    errors = validate_instance(instance, schema)

    evidence_ids = {
        item.get("id")
        for item in instance.get("evidence", [])
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    for index, claim in enumerate(instance.get("claims", [])):
        if not isinstance(claim, dict):
            continue
        for evidence_id in claim.get("evidence_ids", []):
            if evidence_id not in evidence_ids:
                errors.append(
                    f"$.claims[{index}].evidence_ids: unknown evidence id {evidence_id!r}"
                )

    return [f"{path.relative_to(REPO_ROOT)}: {error}" for error in errors]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate public JSON receipts. Defaults to examples/receipts/*.json."
    )
    parser.add_argument(
        "receipts",
        nargs="*",
        help="Repository-relative receipt paths. Absolute and escaping paths are rejected.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        paths = receipt_paths(args.receipts)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if not paths:
        print("ERROR: no public receipt files found", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for path in paths:
        errors = validate_receipt(path)
        if errors:
            all_errors.extend(errors)
        else:
            print(f"PASS receipt: {path.relative_to(REPO_ROOT)}")

    if all_errors:
        for error in all_errors:
            print(f"FAIL receipt: {error}", file=sys.stderr)
        return 1

    print(f"PASS: validated {len(paths)} public receipt(s) in declared schema scope")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
