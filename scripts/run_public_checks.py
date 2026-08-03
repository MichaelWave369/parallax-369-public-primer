#!/usr/bin/env python3
"""Run every public-primer validation helper in a deterministic sequence."""

from __future__ import annotations

import json
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


def expected_failure(
    label: str,
    command: list[str],
    required_diagnostics: list[str],
) -> bool:
    print(f"\n== {label} ==")
    completed = subprocess.run(
        command,
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    combined = f"{completed.stdout}\n{completed.stderr}"
    if completed.returncode == 0:
        print(f"FAIL: {label} unexpectedly passed", file=sys.stderr)
        return False
    missing = [phrase for phrase in required_diagnostics if phrase not in combined]
    if missing:
        for phrase in missing:
            print(f"FAIL {label}: missing expected diagnostic {phrase!r}", file=sys.stderr)
        print(combined, file=sys.stderr)
        return False
    print(f"PASS: {label} was correctly rejected")
    return True


def invalid_receipt_smoke_test() -> bool:
    return expected_failure(
        "Invalid receipt rejection smoke test",
        [
            sys.executable,
            str(SCRIPTS / "validate_receipts.py"),
            "tests/fixtures/invalid-public-receipt.json",
        ],
        [
            "expected at least 1 items, got 0",
            "unknown evidence id 'EV-MISSING'",
        ],
    )


def invalid_field_trial_smoke_test() -> bool:
    return expected_failure(
        "Invalid field-trial rejection smoke test",
        [
            sys.executable,
            str(SCRIPTS / "validate_field_trials.py"),
            "tests/fixtures/invalid-field-trial.json",
        ],
        [
            "expected constant True, got False",
            "expected at least 1 items, got 0",
        ],
    )


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
            print(f"FAIL: report generator exited with {completed.returncode}", file=sys.stderr)
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


def scaffolder_smoke_test() -> bool:
    print("\n== Local project scaffolder smoke test ==")
    with tempfile.TemporaryDirectory(prefix="parallax-scaffold-") as temp_dir:
        output = Path(temp_dir) / "notice-board"
        command = [
            sys.executable,
            str(SCRIPTS / "init_public_project.py"),
            "--name",
            "Neighborhood Notice Board",
            "--human-authority",
            "Project owner",
            "--classification",
            "Fictional",
            "--output",
            str(output),
        ]
        created = subprocess.run(command, cwd=REPO_ROOT, check=False)
        if created.returncode != 0:
            print(f"FAIL: scaffolder exited with {created.returncode}", file=sys.stderr)
            return False

        validated = subprocess.run(
            [sys.executable, str(SCRIPTS / "validate_projects.py"), str(output)],
            cwd=REPO_ROOT,
            check=False,
        )
        if validated.returncode != 0:
            print("FAIL: generated scaffold did not pass project validation", file=sys.stderr)
            return False

        required_files = {
            "README.md",
            "project.json",
            "stage-3-specification.md",
            "stage-6-implementation-receipt.md",
            "stage-9-proving-report.md",
            "field-trial-receipt.md",
        }
        actual_files = {path.name for path in output.iterdir() if path.is_file()}
        missing = sorted(required_files - actual_files)
        if missing:
            print(f"FAIL: scaffold missing files: {', '.join(missing)}", file=sys.stderr)
            return False

        manifest = json.loads((output / "project.json").read_text(encoding="utf-8"))
        if manifest["privacy"]["network_submission"] is not False:
            print("FAIL: scaffold manifest does not preserve no-network boundary", file=sys.stderr)
            return False
        if manifest["human_authority"]["role"] != "Project owner":
            print("FAIL: scaffold did not preserve declared human authority", file=sys.stderr)
            return False

        repeated = subprocess.run(
            command,
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if repeated.returncode == 0 or "refusing to overwrite" not in repeated.stderr:
            print("FAIL: scaffolder did not reject an existing destination", file=sys.stderr)
            return False

    print("PASS: scaffold created, validated, preserved authority, and refused overwrite")
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
            "Public project validation",
            [sys.executable, str(SCRIPTS / "validate_projects.py")],
        ),
        (
            "Public field-trial validation",
            [sys.executable, str(SCRIPTS / "validate_field_trials.py")],
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
    if not invalid_field_trial_smoke_test():
        passed = False
    if not generator_smoke_test():
        passed = False
    if not scaffolder_smoke_test():
        passed = False

    print("\n== Public validation result ==")
    if not passed:
        print("BLOCK: one or more declared public checks failed", file=sys.stderr)
        return 1

    print("PASS IN SCOPE: all declared public structural checks passed")
    print("NO TELEMETRY: the adoption kit performs no network submission")
    print("NO AUTHORIZATION: human review is still required for merge and publication")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
