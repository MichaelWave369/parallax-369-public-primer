#!/usr/bin/env python3
"""Run every v0.3 public-primer validation helper in a deterministic sequence."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"


def run(label: str, command: list[str]) -> bool:
    print(f"\n== {label} ==")
    completed = subprocess.run(command, cwd=REPO_ROOT, check=False)
    if completed.returncode != 0:
        print(f"FAIL: {label} exited with {completed.returncode}", file=sys.stderr)
        return False
    return True


def invalid_receipt_smoke_test() -> bool:
    print("\n== Invalid receipt rejection smoke test ==")
    command = [
        sys.executable,
        str(SCRIPTS / "validate_receipts.py"),
        "tests/fixtures/invalid-public-receipt.json",
    ]
    completed = subprocess.run(
        command,
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    combined = f"{completed.stdout}\n{completed.stderr}"
    required_failures = [
        "expected at least 1 items, got 0",
        "unknown evidence id 'EV-MISSING'",
    ]

    if completed.returncode == 0:
        print("FAIL: intentionally invalid receipt was accepted", file=sys.stderr)
        return False
    missing = [phrase for phrase in required_failures if phrase not in combined]
    if missing:
        for phrase in missing:
            print(
                f"FAIL invalid-receipt smoke test: missing expected diagnostic {phrase!r}",
                file=sys.stderr,
            )
        print(combined, file=sys.stderr)
        return False

    print("PASS: invalid receipt was rejected for both structural and evidence-reference errors")
    return True


def generator_smoke_test() -> bool:
    print("\n== Local report generator smoke test ==")
    with tempfile.TemporaryDirectory(prefix="parallax-public-") as temp_dir:
        output = Path(temp_dir) / "pocket-beacon-report.md"
        command = [
            sys.executable,
            str(SCRIPTS / "generate_report.py"),
            "examples/report-input/pocket-beacon.json",
            "--output",
            str(output),
        ]
        completed = subprocess.run(command, cwd=REPO_ROOT, check=False)
        if completed.returncode != 0:
            print(
                f"FAIL: report generator exited with {completed.returncode}", file=sys.stderr
            )
            return False
        try:
            text = output.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"FAIL: could not read generated report: {exc}", file=sys.stderr)
            return False

        required = [
            "# Public Proving-Ground Draft — Pocket Beacon",
            "| fail | 1 |",
            "The persistence criterion failed.",
            "**Pending human review.**",
            "- **Decision:** Pending",
        ]
        missing = [phrase for phrase in required if phrase not in text]
        if missing:
            for phrase in missing:
                print(f"FAIL generator smoke test: missing {phrase!r}", file=sys.stderr)
            return False

    print("PASS: generator preserved the failed test and pending human decision")
    return True


def main() -> int:
    python_files = sorted(str(path) for path in SCRIPTS.glob("*.py"))
    checks = [
        (
            "Python syntax compilation",
            [sys.executable, "-m", "py_compile", *python_files],
        ),
        (
            "Public receipt validation",
            [sys.executable, str(SCRIPTS / "validate_receipts.py")],
        ),
        (
            "Template completeness",
            [sys.executable, str(SCRIPTS / "check_templates.py")],
        ),
        (
            "Local links and static site",
            [sys.executable, str(SCRIPTS / "check_links.py")],
        ),
    ]

    passed = True
    for label, command in checks:
        if not run(label, command):
            passed = False

    if not invalid_receipt_smoke_test():
        passed = False
    if not generator_smoke_test():
        passed = False

    print("\n== Public validation result ==")
    if not passed:
        print("BLOCK: one or more declared public checks failed", file=sys.stderr)
        return 1

    print("PASS IN SCOPE: all declared public structural checks passed")
    print("NO AUTHORIZATION: human review is still required for merge and publication")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
