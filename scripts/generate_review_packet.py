#!/usr/bin/env python3
"""Generate a local review packet without scoring or choosing a decision."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable

from schema_subset import load_json, resolve_repo_path
from validate_review_bundles import REPO_ROOT, validate_bundle


def safe(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def condition_summary(receipt: dict[str, Any]) -> str:
    data = receipt.get("conditions")
    if not isinstance(data, dict):
        return "Not declared"
    return "; ".join(
        f"{key}={data.get(key, 'Unknown')}"
        for key in ("interaction_mode", "platform", "facilitation", "notes")
    )


def grouped(receipts: list[dict[str, Any]], getter: Callable[[dict[str, Any]], Any]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = defaultdict(list)
    for receipt in receipts:
        result[str(getter(receipt))].append(receipt["trial_id"])
    return dict(sorted(result.items()))


def add_inventory(lines: list[str], title: str, values: dict[str, list[str]]) -> None:
    lines.extend([f"### {title}", "", "| Declared value | Count | Source trial IDs |", "|---|---:|---|"])
    for value, trial_ids in values.items():
        lines.append(f"| {safe(value)} | {len(trial_ids)} | {safe(', '.join(trial_ids))} |")
    lines.append("")


def load_sources(bundle: dict[str, Any]) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    sources = []
    for entry in bundle["receipts"]:
        receipt = load_json(resolve_repo_path(REPO_ROOT, entry["receipt_file"]))
        if not isinstance(receipt, dict):
            raise ValueError(f"source receipt is not an object: {entry['receipt_file']}")
        sources.append((entry, receipt))
    return sources


def render(bundle: dict[str, Any]) -> str:
    sources = load_sources(bundle)
    receipts = [receipt for _, receipt in sources]
    lines = [
        f"# Public Evidence Review Packet — {bundle['project_label']}",
        "",
        "> Generated locally from declared receipts. This packet organizes evidence; it does not authenticate, score, or authorize it.",
        "",
        "## Review identity",
        "",
        f"- **Bundle ID:** {bundle['bundle_id']}",
        f"- **Project key:** `{bundle['project_key']}`",
        f"- **Primer version:** {bundle['primer_version']}",
        f"- **Human authority:** {bundle['human_authority']}",
        f"- **Review status:** {bundle['review_status']}",
        f"- **Source receipt count:** {len(receipts)}",
        "",
        "## Review questions",
        "",
    ]
    lines.extend(f"- {item}" for item in bundle["review_questions"])
    lines.extend([
        "", "## Source receipt inventory", "",
        "| Trial ID | Source file | Inclusion reason | Completion | Conditions | Decision status |",
        "|---|---|---|---|---|---|",
    ])
    for entry, receipt in sources:
        lines.append(
            f"| {safe(receipt['trial_id'])} | {safe(entry['receipt_file'])} | {safe(entry['inclusion_reason'])} | "
            f"{safe(receipt['completion'])} | {safe(condition_summary(receipt))} | "
            f"{safe(receipt['maintainer_decision']['status'])} |"
        )

    lines.extend(["", "## Declared outcome inventory", ""])
    add_inventory(lines, "Completion", grouped(receipts, lambda item: item["completion"]))
    add_inventory(lines, "Assistance", grouped(receipts, lambda item: item["help_needed"]))
    lines.extend(["### Understanding", "", "| Dimension | Declared value | Count | Source trial IDs |", "|---|---|---:|---|"])
    dimensions = (
        ("Stage separation", "stage_separation"),
        ("Human authority", "human_authority"),
        ("Validator boundary", "validator_boundary"),
    )
    for label, key in dimensions:
        for value, ids in grouped(receipts, lambda item, k=key: item["understanding"][k]).items():
            lines.append(f"| {label} | {safe(value)} | {len(ids)} | {safe(', '.join(ids))} |")

    comparisons = (
        ("Project type", lambda item: item["project_type"]),
        ("Completion", lambda item: item["completion"]),
        ("Time band", lambda item: item["time_band"]),
        ("Help needed", lambda item: item["help_needed"]),
        ("Stage separation", lambda item: item["understanding"]["stage_separation"]),
        ("Human authority", lambda item: item["understanding"]["human_authority"]),
        ("Validator boundary", lambda item: item["understanding"]["validator_boundary"]),
        ("Maintainer decision", lambda item: item["maintainer_decision"]["status"]),
    )
    agreements, divergences = [], []
    for label, getter in comparisons:
        values = grouped(receipts, getter)
        if len(values) == 1:
            agreements.append(f"- **{label}:** all receipts declare `{next(iter(values))}`.")
        else:
            detail = "; ".join(f"`{value}` — {', '.join(ids)}" for value, ids in values.items())
            divergences.append(f"- **{label}:** {detail}.")
    conditions = {condition_summary(receipt) for receipt in receipts}
    if len(conditions) > 1:
        divergences.append("- **Declared conditions differ:** do not treat these receipts as controlled replications or average them as equivalent trials.")

    lines.extend(["", "## Points of agreement", ""])
    lines.extend(agreements or ["- No complete field-level agreement was detected."])
    lines.extend(["", "## Points of divergence", ""])
    lines.extend(divergences or ["- No field-level divergence was detected; equivalence is still unproven."])
    lines.extend(["", "## Preserved source observations", "", "| Trial ID | Observation ID | Observation |", "|---|---|---|"])
    for receipt in receipts:
        for observation in receipt["observations"]:
            lines.append(f"| {safe(receipt['trial_id'])} | {safe(observation['id'])} | {safe(observation['observation'])} |")

    lines.extend(["", "## Evidence limitations", "", "### Bundle limits", ""])
    lines.extend(f"- {item}" for item in bundle["known_limits"])
    for receipt in receipts:
        lines.extend(["", f"### {receipt['trial_id']}", ""])
        lines.extend(f"- {item}" for item in receipt["evidence_limits"])

    lines.extend([
        "", "## Human interpretation", "",
        "**Pending.** Review the source receipts before recording agreement, dissent, proposed changes, or additional evidence needs.",
        "", "## Candidate actions", "",
        "No automated recommendation generated. Human proposals must preserve supporting evidence, counterevidence, dissent, and scope.",
        "", "## Human decision", "",
        "- **Decision:** Pending",
        f"- **Authority:** {bundle['human_authority']}",
        "- **Scope:** Pending",
        "- **Reasoning:** Pending",
        "- **Unresolved dissent:** Pending review",
        "- **Date:** Pending",
        "", "## Claim boundary", "",
        "- Counts are inventories, not scores or statistical findings.",
        "- Agreement does not authenticate evidence or establish truth.",
        "- Divergence is preserved rather than resolved by majority vote.",
        "- Different conditions block automatic claims of replication or comparability.",
        "- This packet does not rank trials, certify the project, recommend release, or authorize a roadmap change.",
        "- Human interpretation, publication, and release authority remain external to the generator.",
        "", "> Source receipts remain controlling for their own observations. This packet cannot replace them.", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a local public evidence-review packet")
    parser.add_argument("bundle", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    bundle_path = args.bundle if args.bundle.is_absolute() else (REPO_ROOT / args.bundle).resolve()
    errors = validate_bundle(bundle_path)
    if errors:
        print(f"BLOCK: invalid review bundle: {bundle_path}", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    output = args.output.resolve()
    if output.exists() and not args.force:
        print(f"BLOCK: output exists; choose another path or use --force: {output}", file=sys.stderr)
        return 1
    try:
        bundle = load_json(bundle_path)
        if not isinstance(bundle, dict):
            raise ValueError("review bundle must be a JSON object")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render(bundle), encoding="utf-8")
    except (OSError, ValueError) as exc:
        print(f"BLOCK: could not generate packet: {exc}", file=sys.stderr)
        return 1
    print(f"PASS generator: wrote {output}")
    print("NO SCORE: no ranking, confidence percentage, or majority-truth claim was generated")
    print("NO DECISION: human review and authority remain pending")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
