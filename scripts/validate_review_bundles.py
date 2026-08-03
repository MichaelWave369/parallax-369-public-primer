#!/usr/bin/env python3
"""Validate public evidence-review bundles without authenticating their evidence."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from schema_subset import load_json, resolve_repo_path, validate_instance
from validate_field_trials import validate_receipt


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "schemas" / "review-bundle.schema.json"


def validate_bundle(path: Path) -> list[str]:
    try:
        schema = load_json(SCHEMA_PATH)
        bundle = load_json(path)
    except ValueError as exc:
        return [str(exc)]

    if not isinstance(schema, dict) or not isinstance(bundle, dict):
        return ["schema and review bundle must both be JSON objects"]

    errors = validate_instance(bundle, schema)
    if errors:
        return errors

    receipt_files: list[str] = []
    trial_ids: list[str] = []

    for index, entry in enumerate(bundle["receipts"]):
        declared_file = entry["receipt_file"]
        declared_trial_id = entry["declared_trial_id"]
        receipt_files.append(declared_file)
        trial_ids.append(declared_trial_id)

        try:
            receipt_path = resolve_repo_path(REPO_ROOT, declared_file)
        except ValueError as exc:
            errors.append(f"$.receipts[{index}].receipt_file: {exc}")
            continue

        if not receipt_path.is_file():
            errors.append(
                f"$.receipts[{index}].receipt_file: referenced receipt does not exist: {declared_file}"
            )
            continue

        receipt_errors = validate_receipt(receipt_path)
        for error in receipt_errors:
            errors.append(f"$.receipts[{index}]: source receipt invalid: {error}")
        if receipt_errors:
            continue

        try:
            receipt = load_json(receipt_path)
        except ValueError as exc:
            errors.append(f"$.receipts[{index}]: {exc}")
            continue
        if not isinstance(receipt, dict):
            errors.append(f"$.receipts[{index}]: source receipt must be a JSON object")
            continue

        actual_trial_id = receipt.get("trial_id")
        if actual_trial_id != declared_trial_id:
            errors.append(
                f"$.receipts[{index}].declared_trial_id: expected {actual_trial_id!r} from source, got {declared_trial_id!r}"
            )

        source_project = receipt.get("project_key")
        if not isinstance(source_project, str) or not source_project.strip():
            errors.append(
                f"$.receipts[{index}]: source receipt must declare project_key for v0.5 review"
            )
        elif source_project != bundle["project_key"]:
            errors.append(
                f"$.receipts[{index}]: project_key {source_project!r} does not match bundle project_key {bundle['project_key']!r}"
            )

    if len(set(receipt_files)) != len(receipt_files):
        errors.append("$.receipts: receipt_file values must be unique")
    if len(set(trial_ids)) != len(trial_ids):
        errors.append("$.receipts: declared_trial_id values must be unique")

    return errors


def discover_default_bundles() -> list[Path]:
    folder = REPO_ROOT / "examples" / "review-bundles"
    return sorted(folder.glob("*.json")) if folder.exists() else []


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate public evidence-review bundles")
    parser.add_argument("bundles", nargs="*", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    bundles = args.bundles or discover_default_bundles()
    if not bundles:
        print("BLOCK: no review bundles supplied or discovered", file=sys.stderr)
        return 1

    failed = False
    for bundle in bundles:
        errors = validate_bundle(bundle)
        if errors:
            failed = True
            print(f"FAIL review bundle: {bundle}", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
        else:
            print(f"PASS review bundle: {bundle}")

    if failed:
        return 1

    print(f"PASS IN SCOPE: validated {len(bundles)} evidence-review bundle(s)")
    print("NO SYNTHETIC AUTHORITY: bundle validation does not score evidence or authorize a decision")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
