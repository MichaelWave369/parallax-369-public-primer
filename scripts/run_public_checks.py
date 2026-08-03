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
    if completed.returncode:
        print(f"FAIL: {label} exited with {completed.returncode}", file=sys.stderr)
        return False
    return True


def expected_failure(label: str, command: list[str], diagnostics: list[str]) -> bool:
    print(f"\n== {label} ==")
    completed = subprocess.run(command, cwd=REPO_ROOT, check=False, capture_output=True, text=True)
    combined = f"{completed.stdout}\n{completed.stderr}"
    if completed.returncode == 0:
        print(f"FAIL: {label} unexpectedly passed", file=sys.stderr)
        return False
    missing = [phrase for phrase in diagnostics if phrase not in combined]
    if missing:
        for phrase in missing:
            print(f"FAIL {label}: missing diagnostic {phrase!r}", file=sys.stderr)
        print(combined, file=sys.stderr)
        return False
    print(f"PASS: {label} was correctly rejected")
    return True


def invalid_receipt_test() -> bool:
    return expected_failure(
        "Invalid receipt rejection smoke test",
        [sys.executable, str(SCRIPTS / "validate_receipts.py"), "tests/fixtures/invalid-public-receipt.json"],
        ["expected at least 1 items, got 0", "unknown evidence id 'EV-MISSING'"],
    )


def invalid_field_trial_test() -> bool:
    return expected_failure(
        "Invalid field-trial rejection smoke test",
        [sys.executable, str(SCRIPTS / "validate_field_trials.py"), "tests/fixtures/invalid-field-trial.json"],
        ["expected constant True, got False", "expected at least 1 items, got 0"],
    )


def invalid_review_bundle_tests() -> bool:
    cross_project = expected_failure(
        "Cross-project review bundle rejection",
        [sys.executable, str(SCRIPTS / "validate_review_bundles.py"), "tests/fixtures/invalid-review-bundle-cross-project.json"],
        ["does not match bundle project_key"],
    )
    missing_file = expected_failure(
        "Missing-source review bundle rejection",
        [sys.executable, str(SCRIPTS / "validate_review_bundles.py"), "tests/fixtures/invalid-review-bundle-missing-file.json"],
        ["referenced receipt does not exist"],
    )
    return cross_project and missing_file


def report_generator_test() -> bool:
    print("\n== Local report generator smoke test ==")
    with tempfile.TemporaryDirectory(prefix="parallax-public-") as temp_dir:
        output = Path(temp_dir) / "pocket-beacon-report.md"
        completed = subprocess.run(
            [sys.executable, str(SCRIPTS / "generate_report.py"), "examples/report-input/pocket-beacon.json", "--output", str(output)],
            cwd=REPO_ROOT,
            check=False,
        )
        if completed.returncode:
            print(f"FAIL: report generator exited with {completed.returncode}", file=sys.stderr)
            return False
        text = output.read_text(encoding="utf-8")
        required = [
            "# Public Proving-Ground Draft — Pocket Beacon",
            "| fail | 1 |",
            "The persistence criterion failed.",
            "**Pending human review.**",
            "- **Decision:** Pending",
        ]
        if any(phrase not in text for phrase in required):
            print("FAIL: report generator did not preserve failure and pending authority", file=sys.stderr)
            return False
    print("PASS: report generator preserved the failed test and pending human decision")
    return True


def review_generator_test() -> bool:
    print("\n== Evidence review generator smoke test ==")
    with tempfile.TemporaryDirectory(prefix="parallax-review-") as temp_dir:
        output = Path(temp_dir) / "pocket-beacon-review.md"
        command = [
            sys.executable,
            str(SCRIPTS / "generate_review_packet.py"),
            "examples/review-bundles/pocket-beacon-review.json",
            "--output",
            str(output),
        ]
        completed = subprocess.run(command, cwd=REPO_ROOT, check=False)
        if completed.returncode:
            print(f"FAIL: review generator exited with {completed.returncode}", file=sys.stderr)
            return False
        text = output.read_text(encoding="utf-8")
        required = [
            "FT-PB-001",
            "FT-PB-002",
            "## Points of divergence",
            "Declared conditions differ",
            "No automated recommendation generated",
            "- **Decision:** Pending",
            "Counts are inventories, not scores",
        ]
        missing = [phrase for phrase in required if phrase not in text]
        if missing:
            print(f"FAIL: generated review packet missing: {', '.join(missing)}", file=sys.stderr)
            return False
        repeated = subprocess.run(command, cwd=REPO_ROOT, check=False, capture_output=True, text=True)
        if repeated.returncode == 0 or "output exists" not in repeated.stderr:
            print("FAIL: review generator did not refuse overwrite", file=sys.stderr)
            return False
    print("PASS: review packet preserved both trials, divergence, no score, pending authority, and overwrite refusal")
    return True


def scaffolder_test() -> bool:
    print("\n== Local project scaffolder smoke test ==")
    with tempfile.TemporaryDirectory(prefix="parallax-scaffold-") as temp_dir:
        output = Path(temp_dir) / "notice-board"
        command = [
            sys.executable,
            str(SCRIPTS / "init_public_project.py"),
            "--name", "Neighborhood Notice Board",
            "--human-authority", "Project owner",
            "--classification", "Fictional",
            "--output", str(output),
        ]
        if subprocess.run(command, cwd=REPO_ROOT, check=False).returncode:
            print("FAIL: scaffolder failed", file=sys.stderr)
            return False
        if subprocess.run([sys.executable, str(SCRIPTS / "validate_projects.py"), str(output)], cwd=REPO_ROOT, check=False).returncode:
            print("FAIL: scaffold validation failed", file=sys.stderr)
            return False
        required = {"README.md", "project.json", "stage-3-specification.md", "stage-6-implementation-receipt.md", "stage-9-proving-report.md", "field-trial-receipt.md"}
        if required - {path.name for path in output.iterdir() if path.is_file()}:
            print("FAIL: scaffold is incomplete", file=sys.stderr)
            return False
        manifest = json.loads((output / "project.json").read_text(encoding="utf-8"))
        if manifest["privacy"]["network_submission"] is not False or manifest["human_authority"]["role"] != "Project owner":
            print("FAIL: scaffold lost privacy or authority boundary", file=sys.stderr)
            return False
        repeated = subprocess.run(command, cwd=REPO_ROOT, check=False, capture_output=True, text=True)
        if repeated.returncode == 0 or "refusing to overwrite" not in repeated.stderr:
            print("FAIL: scaffolder did not reject overwrite", file=sys.stderr)
            return False
    print("PASS: scaffold created, validated, preserved authority, and refused overwrite")
    return True


def main() -> int:
    python_files = sorted(str(path) for path in SCRIPTS.glob("*.py"))
    checks = [
        ("Python syntax compilation", [sys.executable, "-m", "py_compile", *python_files]),
        ("Public receipt validation", [sys.executable, str(SCRIPTS / "validate_receipts.py")]),
        ("Public project validation", [sys.executable, str(SCRIPTS / "validate_projects.py")]),
        ("Public field-trial validation", [sys.executable, str(SCRIPTS / "validate_field_trials.py")]),
        ("Public review-bundle validation", [sys.executable, str(SCRIPTS / "validate_review_bundles.py")]),
        ("Template completeness", [sys.executable, str(SCRIPTS / "check_templates.py")]),
        ("Local links and static site", [sys.executable, str(SCRIPTS / "check_links.py")]),
    ]
    passed = all(run(label, command) for label, command in checks)
    for test in (
        invalid_receipt_test,
        invalid_field_trial_test,
        invalid_review_bundle_tests,
        report_generator_test,
        review_generator_test,
        scaffolder_test,
    ):
        if not test():
            passed = False

    print("\n== Public validation result ==")
    if not passed:
        print("BLOCK: one or more declared public checks failed", file=sys.stderr)
        return 1
    print("PASS IN SCOPE: all declared public structural checks passed")
    print("NO TELEMETRY: local tools perform no network submission")
    print("NO SCORE: evidence review does not rank, average, or vote truth into existence")
    print("NO AUTHORIZATION: human review is still required for merge and publication")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
