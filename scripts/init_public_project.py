#!/usr/bin/env python3
"""Create a local, non-sensitive Parallax 3-6-9 public-primer project.

The scaffolder copies only public templates, performs no network request, and
refuses to overwrite an existing destination.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PRIMER_VERSION = "0.4.0-candidate"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "public-project"


def read_template(name: str) -> str:
    path = REPO_ROOT / "templates" / name
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RuntimeError(f"could not read public template {path}: {exc}") from exc


def write_text(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def build_stage_document(
    title: str,
    project_name: str,
    human_authority: str,
    template: str,
) -> str:
    return f"""# {title} — {project_name}

- **Generated from:** Parallax 3–6–9 Public Primer {PRIMER_VERSION}
- **Project:** {project_name}
- **Human authority:** {human_authority}
- **Status:** Proposed

> This local scaffold is not certification, approval, or evidence that the project works.

---

{template}
"""


def create_project(args: argparse.Namespace) -> Path:
    output = args.output.expanduser().resolve()
    repo_root = REPO_ROOT.resolve()

    if output == repo_root:
        raise RuntimeError("output cannot be the public-primer repository root")
    if output.exists():
        raise RuntimeError(f"destination already exists; refusing to overwrite: {output}")

    output.mkdir(parents=True)

    project_id = slugify(args.name)
    artifacts = {
        "stage_3": "stage-3-specification.md",
        "stage_6": "stage-6-implementation-receipt.md",
        "stage_9": "stage-9-proving-report.md",
        "field_trial": "field-trial-receipt.md",
    }

    manifest = {
        "manifest_version": "0.4",
        "primer_version": PRIMER_VERSION,
        "project_id": project_id,
        "project_name": args.name,
        "status": "Proposed",
        "human_authority": {
            "role": args.human_authority,
            "scope": "Scope, risk acceptance, release, and publication decisions",
        },
        "privacy": {
            "classification": args.classification,
            "network_submission": False,
            "contains_private_parallax_material": False,
        },
        "artifacts": artifacts,
    }

    readme = f"""# {args.name}

This folder was generated locally from the **Parallax 3–6–9 Public Primer {PRIMER_VERSION}**.

## Authority

**{args.human_authority}** retains authority over scope, risk acceptance, release, and publication.

## Sequence

1. Complete `stage-3-specification.md` without pretending the project has been built.
2. Build the smallest honest candidate and complete `stage-6-implementation-receipt.md`.
3. Test the candidate and complete `stage-9-proving-report.md`.
4. Use `field-trial-receipt.md` only for a voluntary, non-sensitive usability trial.

## Local validation

From the public-primer repository root:

```text
python scripts/validate_projects.py {output}
```

A passing structural check does not certify this project or authorize release.

## Privacy boundary

This scaffold makes no network request. Do not add credentials, private conversations, client data, regulated information, or private Parallax material.
"""

    write_text(output / "README.md", readme)
    write_text(output / "project.json", json.dumps(manifest, indent=2))
    write_text(
        output / artifacts["stage_3"],
        build_stage_document(
            "Stage 3 Controlling Specification",
            args.name,
            args.human_authority,
            read_template("controlling-specification.md"),
        ),
    )
    write_text(
        output / artifacts["stage_6"],
        build_stage_document(
            "Stage 6 Implementation Receipt",
            args.name,
            args.human_authority,
            read_template("implementation-receipt.md"),
        ),
    )
    write_text(
        output / artifacts["stage_9"],
        build_stage_document(
            "Stage 9 Proving-Ground Report",
            args.name,
            args.human_authority,
            read_template("proving-ground-report.md"),
        ),
    )
    write_text(
        output / artifacts["field_trial"],
        build_stage_document(
            "Public Field-Trial Receipt",
            args.name,
            args.human_authority,
            read_template("field-trial-receipt.md"),
        ),
    )

    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a local public-primer project without network access."
    )
    parser.add_argument("--name", required=True, help="Public or non-sensitive project name")
    parser.add_argument(
        "--human-authority",
        required=True,
        help="Person or role retaining scope and release authority",
    )
    parser.add_argument("--output", required=True, type=Path, help="New destination folder")
    parser.add_argument(
        "--classification",
        choices=["Public", "Non-sensitive local", "Fictional"],
        default="Non-sensitive local",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        output = create_project(args)
    except (OSError, RuntimeError) as exc:
        print(f"BLOCK: {exc}", file=sys.stderr)
        return 1

    print(f"PASS scaffold: created local project at {output}")
    print("NO NETWORK: no content was uploaded or transmitted")
    print("NO AUTHORIZATION: human review is required before release or publication")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
