#!/usr/bin/env python3
"""Generate a Markdown proving-ground draft from local structured input.

The generator preserves supplied results and leaves release authority pending.
It does not infer missing evidence, choose a release recommendation, or publish.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from schema_subset import load_json, resolve_repo_path, validate_instance


REPO_ROOT = Path(__file__).resolve().parents[1]
RESULT_ORDER = ["pass", "fail", "blocked", "inconclusive", "not-run"]


def cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def validate_input(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        data = load_json(path)
    except ValueError as exc:
        return None, [str(exc)]
    if not isinstance(data, dict):
        return None, [f"{path}: input root must be a JSON object"]

    schema_file = data.get("schema_file")
    if not isinstance(schema_file, str) or not schema_file:
        return None, [f"{path}: missing non-empty schema_file"]

    try:
        schema_path = resolve_repo_path(REPO_ROOT, schema_file)
        schema = load_json(schema_path)
    except ValueError as exc:
        return None, [f"{path}: {exc}"]
    if not isinstance(schema, dict):
        return None, [f"{schema_path}: schema root must be a JSON object"]

    return data, validate_instance(data, schema)


def render_report(data: dict[str, Any]) -> str:
    criteria = data["criteria"]
    counts = Counter(item["result"] for item in criteria)
    environment = data["environment"]
    claims = data.get("claims", [])

    lines = [
        f"# Public Proving-Ground Draft — {data['project']}",
        "",
        "> Generated locally from structured input. This draft does not authorize release, certify the candidate, or replace human review.",
        "",
        "## Evaluation identity",
        "",
        f"- **Project:** {data['project']}",
        f"- **Candidate tested:** {data['candidate']}",
        f"- **Controlling specification:** {data['controlling_specification']}",
        f"- **Tester / reviewer:** {data['tester']}",
        f"- **Test date:** {data['test_date']}",
        "- **Human release authority:** Pending assignment or confirmation",
        "",
        "## Environment and preconditions",
        "",
        f"- **Platform:** {environment['platform']}",
        f"- **Configuration:** {environment['configuration']}",
        f"- **External services:** {environment.get('external_services', 'Not stated')}",
        f"- **Safety controls:** {environment.get('safety_controls', 'Not stated')}",
        "",
        "## Outcome summary",
        "",
        "| Result | Count |",
        "|---|---:|",
    ]

    for result in RESULT_ORDER:
        lines.append(f"| {result} | {counts.get(result, 0)} |")

    lines.extend(
        [
            "",
            "## Test results",
            "",
            "| Test ID | Criterion | Method | Result | Observation | Evidence |",
            "|---|---|---|---|---|---|",
        ]
    )
    for item in criteria:
        lines.append(
            "| "
            + " | ".join(
                cell(item[key])
                for key in ["id", "criterion", "method", "result", "observation", "evidence"]
            )
            + " |"
        )

    lines.extend(["", "## Claim matrix", ""])
    if claims:
        lines.extend(
            [
                "| Claim | Classification | Scope / limitation |",
                "|---|---|---|",
            ]
        )
        for claim in claims:
            lines.append(
                f"| {cell(claim['text'])} | {cell(claim['classification'])} | {cell(claim['scope_limit'])} |"
            )
    else:
        lines.append("No claims were supplied. Claim review remains pending.")

    lines.extend(["", "## Limitations", ""])
    for limitation in data["limitations"]:
        lines.append(f"- {limitation}")

    lines.extend(
        [
            "",
            "## Release recommendation",
            "",
            "**Pending human review.** The generator does not select a release disposition.",
            "",
            "Available human dispositions:",
            "",
            "- [ ] Release within documented limits",
            "- [ ] Conditional release with listed mitigations",
            "- [ ] Return to Stage 6",
            "- [ ] Return to Stage 3",
            "- [ ] Do not release",
            "",
            "## Human release decision",
            "",
            "- **Decision:** Pending",
            "- **Authorized by:**",
            "- **Date:**",
            "- **Conditions / limits:**",
            "- **Decision receipt:**",
            "",
            "> A generated report is a formatting aid. Its contents remain subject to evidence review, dissent, and explicit human authority.",
            "",
        ]
    )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a local Markdown proving-ground draft.")
    parser.add_argument("input", help="Repository-relative JSON input path")
    parser.add_argument("--output", help="Output path. Omit to print to stdout.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        input_path = resolve_repo_path(REPO_ROOT, args.input)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    data, errors = validate_input(input_path)
    if errors:
        for error in errors:
            print(f"FAIL generator input: {error}", file=sys.stderr)
        return 1
    assert data is not None

    report = render_report(data)
    if args.output:
        output_path = Path(args.output).expanduser().resolve()
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(report, encoding="utf-8")
        except OSError as exc:
            print(f"ERROR: could not write {output_path}: {exc}", file=sys.stderr)
            return 2
        print(f"PASS generator: wrote {output_path}")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
