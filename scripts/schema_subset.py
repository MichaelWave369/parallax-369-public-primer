#!/usr/bin/env python3
"""Small JSON-schema subset used by the public-primer validation helpers.

This module intentionally does not implement the complete JSON Schema standard.
See schemas/README.md for the supported keywords and claim boundary.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


SUPPORTED_TYPES = {
    "object": dict,
    "array": list,
    "string": str,
    "integer": int,
    "number": (int, float),
    "boolean": bool,
    "null": type(None),
}


def load_json(path: Path) -> Any:
    """Load UTF-8 JSON and raise a readable ValueError on failure."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"invalid JSON in {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def _matches_type(value: Any, expected: str) -> bool:
    if expected not in SUPPORTED_TYPES:
        return False
    if expected in {"integer", "number"} and isinstance(value, bool):
        return False
    return isinstance(value, SUPPORTED_TYPES[expected])


def validate_instance(value: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    """Validate a value against the documented schema subset."""
    errors: list[str] = []

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}, got {value!r}")

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value {value!r} is not in {schema['enum']!r}")

    expected_type = schema.get("type")
    if expected_type is not None:
        if not isinstance(expected_type, str) or expected_type not in SUPPORTED_TYPES:
            errors.append(f"{path}: schema uses unsupported type {expected_type!r}")
            return errors
        if not _matches_type(value, expected_type):
            actual = type(value).__name__
            errors.append(f"{path}: expected {expected_type}, got {actual}")
            return errors

    if isinstance(value, dict):
        required = schema.get("required", [])
        if not isinstance(required, list):
            errors.append(f"{path}: schema required keyword must be an array")
            return errors
        for key in required:
            if key not in value:
                errors.append(f"{path}: missing required property {key!r}")

        properties = schema.get("properties", {})
        if not isinstance(properties, dict):
            errors.append(f"{path}: schema properties keyword must be an object")
            return errors

        for key, child_value in value.items():
            child_path = f"{path}.{key}"
            child_schema = properties.get(key)
            if child_schema is not None:
                if not isinstance(child_schema, dict):
                    errors.append(f"{child_path}: property schema must be an object")
                else:
                    errors.extend(validate_instance(child_value, child_schema, child_path))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{child_path}: additional property is not allowed")

    if isinstance(value, list):
        minimum_items = schema.get("minItems")
        if isinstance(minimum_items, int) and len(value) < minimum_items:
            errors.append(f"{path}: expected at least {minimum_items} items, got {len(value)}")
        item_schema = schema.get("items")
        if item_schema is not None:
            if not isinstance(item_schema, dict):
                errors.append(f"{path}: items schema must be an object")
            else:
                for index, item in enumerate(value):
                    errors.extend(validate_instance(item, item_schema, f"{path}[{index}]"))

    if isinstance(value, str):
        minimum_length = schema.get("minLength")
        if isinstance(minimum_length, int) and len(value) < minimum_length:
            errors.append(
                f"{path}: expected at least {minimum_length} characters, got {len(value)}"
            )

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        minimum = schema.get("minimum")
        if isinstance(minimum, (int, float)) and value < minimum:
            errors.append(f"{path}: expected value >= {minimum}, got {value}")

    return errors


def resolve_repo_path(repo_root: Path, declared_path: str) -> Path:
    """Resolve a repository-relative path without allowing traversal outside the repo."""
    candidate = (repo_root / declared_path).resolve()
    root = repo_root.resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"path escapes repository root: {declared_path}") from exc
    return candidate
