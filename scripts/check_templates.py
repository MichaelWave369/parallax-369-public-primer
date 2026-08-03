#!/usr/bin/env python3
"""Check that public Markdown templates retain their required method sections."""

from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SECTIONS = {
    "templates/controlling-specification.md": [
        "## Document control",
        "## 1. Original input",
        "## 3. Scope",
        "## 5. Statement ledger",
        "### Facts",
        "### Assumptions",
        "### Hypotheses",
        "### Proposals",
        "### Unknowns",
        "## 6. Requirements",
        "## 9. Acceptance criteria",
        "## 12. Decision receipts",
        "## 13. Stage 6 handoff",
        "## Stage gate approval",
    ],
    "templates/implementation-receipt.md": [
        "## Candidate identity",
        "## Supported environment",
        "## Reproduction",
        "## Requirement traceability",
        "## Deviations",
        "## Mocks and simulations",
        "## Known limitations",
        "## Construction tests",
        "## Stage 9 evidence handoff",
        "## Human acceptance",
    ],
    "templates/proving-ground-report.md": [
        "## Evaluation identity",
        "## Environment and preconditions",
        "## Test results",
        "## Raw observations",
        "## Negative and unexpected findings",
        "## Reproducibility",
        "## Claim matrix",
        "## Unsupported claims",
        "## Residual risks and unknowns",
        "## Reviewer dissent",
        "## Release recommendation",
        "## Human release decision",
    ],
    "templates/public-release-review.md": [
        "## Origin and purpose",
        "## Privacy",
        "## Capability and canon",
        "## Security",
        "## Claims and authority",
        "## Licensing and attribution",
        "## Findings",
        "## Decision receipt",
    ],
}

REQUIRED_PHRASES = {
    "templates/controlling-specification.md": [
        "Human authority",
        "Acceptance criterion",
        "Material decisions that must return to Stage 3",
    ],
    "templates/implementation-receipt.md": [
        "Implemented / Simulated / Mocked / Deferred / Failed / Unknown",
        "What it cannot prove",
        "The controlling specification was not silently rewritten",
    ],
    "templates/proving-ground-report.md": [
        "Pass / Fail / Blocked / Inconclusive / Not run",
        "Observed / Repeated / Verified in scope / Unsupported / Unknown",
        "Passing this report does not establish performance, safety, legality, or truth outside the recorded evidence scope.",
    ],
    "templates/public-release-review.md": [
        "A single **No**, **Unknown**, or unresolved concern blocks publication.",
        "Human publication authority is explicit.",
        "No private prompts, hidden rubrics, skill instructions, or orchestration logic are present.",
    ],
}


def main() -> int:
    errors: list[str] = []

    for relative_path, headings in REQUIRED_SECTIONS.items():
        path = REPO_ROOT / relative_path
        if not path.is_file():
            errors.append(f"{relative_path}: file is missing")
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                errors.append(f"{relative_path}: missing required heading {heading!r}")
        for phrase in REQUIRED_PHRASES.get(relative_path, []):
            if phrase not in text:
                errors.append(f"{relative_path}: missing required boundary phrase {phrase!r}")

    if errors:
        for error in errors:
            print(f"FAIL template: {error}", file=sys.stderr)
        return 1

    print(f"PASS: {len(REQUIRED_SECTIONS)} public templates retain required sections and boundaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
