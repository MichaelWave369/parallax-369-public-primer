#!/usr/bin/env python3
"""Validate machine-readable public field-trial receipts in declared scope."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from schema_subset import load_json, validate_instance


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "schemas" / "field-trial-receipt.schema.json"


def validate_receipt(path: Path) -> list[str]:
    try:
        schema = load_json(SCHEMA_PATH)
        receipt = load_json(path)
    except ValueError as exc:
        return [str(exc)]

    if not isinstance(schema, dict) or not isinstance(receipt, dict):
        return ["schema and field-trial receipt must both be JSON objects"]

    errors = validate_instance(receipt, schema)
    if errors:
        return errors

    observation_ids = [item["id"] for item in receipt["observations"]]
    if len(set(observation_ids)) != len(observation_ids):
        errors.append("$.observations: observation IDs must be unique")

    if receipt["maintainer_decision"]["status"] != "Pending":
        authority = receipt["maintainer_decision"]["authority"].strip()
        if not authority:
            errors.append("$.maintainer_decision.authority: required for a non-pending decision")

    return errors


def discover_default_receipts() -> list[Path]:
    folder = REPO_ROOT / "examples" / "field-trials"
    return sorted(folder.glob("*.json")) if folder.exists() else []


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate public field-trial JSON receipts")
    parser.add_argument("receipts", nargs="*", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    receipts = args.receipts or discover_default_receipts()
    if not receipts:
        print("BLOCK: no field-trial receipts supplied or discovered", file=sys.stderr)
        return 1

    failed = False
    for receipt in receipts:
        errors = validate_receipt(receipt)
        if errors:
            failed = True
            print(f"FAIL field trial: {receipt}", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
        else:
            print(f"PASS field trial: {receipt}")

    if failed:
        return 1

    print(f"PASS IN SCOPE: validated {len(receipts)} field-trial receipt(s)")
    print("NO AUTHENTICATION: validation does not prove the trial occurred or observations are accurate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
