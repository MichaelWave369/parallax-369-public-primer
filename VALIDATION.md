# Public Validation Helpers

Version 0.3 introduced small, local-first structural checks. Version 0.4 extended them to project scaffolds and voluntary field-trial receipts. Version 0.5 adds same-project review-bundle validation and a local evidence-review packet generator.

These tools are intentionally limited. They do not certify truth, safety, legality, accessibility, engineering adequacy, consent validity, evidence authenticity, comparability, or release readiness.

## Design rules

1. **Standard library only.** The helpers require Python 3.11 or newer and no third-party packages.
2. **Local by default.** The scripts make no network request and submit no telemetry.
3. **Public artifacts only.** They inspect public templates, static pages, schemas, synthetic examples, and user-supplied local public artifacts.
4. **Fail visibly.** A failed or blocked check returns a non-zero exit code and prints the affected path.
5. **No overwrite by default.** The project scaffolder and evidence-review generator refuse to replace an existing destination unless an explicit override is supplied where supported.
6. **No authority inheritance.** Checks may block a pull request. They cannot approve, merge, publish, tag, release, deploy, certify, or choose a roadmap change.
7. **No external-link claims.** The link checker verifies local targets only.
8. **Schema scope is explicit.** The validators implement the documented subset in `schemas/README.md`, not the complete JSON Schema standard.
9. **No synthetic score.** Review packets may inventory declared outcomes but do not rank, average, calculate confidence, or resolve disagreement by majority vote.

## Run all public checks

From the repository root:

```bash
python scripts/run_public_checks.py
```

The command runs:

- public JSON proving-receipt validation;
- public project-manifest and stage-artifact validation;
- public field-trial receipt validation;
- public review-bundle and referenced-source validation;
- Markdown template completeness checks;
- local Markdown and HTML link checks;
- static-site entry-point and asset checks;
- intentionally invalid proving, field-trial, cross-project, and missing-source rejection tests;
- deterministic proving-report and evidence-review generator smoke tests;
- a local project-scaffolder smoke test, including overwrite rejection.

## Create and validate a local project

```bash
python scripts/init_public_project.py \
  --name "Neighborhood Notice Board" \
  --human-authority "Project owner" \
  --output work/notice-board

python scripts/validate_projects.py work/notice-board
```

The scaffolder copies public templates into a new folder and writes a `project.json` manifest. It does not upload the project or decide whether it is safe to release.

## Validate and review field-trial receipts

```bash
python scripts/validate_field_trials.py
python scripts/validate_review_bundles.py
python scripts/generate_review_packet.py \
  examples/review-bundles/pocket-beacon-review.json \
  --output /tmp/pocket-beacon-review.md
```

The review validator requires at least two valid source receipts with matching declared project keys. It rejects missing files, duplicate references, mismatched trial IDs, and cross-project bundles.

The generator inventories completion, assistance, and understanding values; surfaces agreement and divergence; preserves every observation and evidence limit; and leaves interpretation, candidate actions, and the human decision pending.

## Run one check

```bash
python scripts/validate_receipts.py
python scripts/validate_projects.py
python scripts/validate_field_trials.py
python scripts/validate_review_bundles.py
python scripts/check_templates.py
python scripts/check_links.py
python scripts/generate_report.py examples/report-input/pocket-beacon.json --output /tmp/pocket-beacon-report.md
```

## Exit status

- `0` — every check executed by that command passed in its declared scope.
- `1` — at least one check failed or a safe-write boundary blocked the operation.
- `2` — command usage or input parsing failed.

A passing exit status means only that the declared structural checks passed against the inspected files.

## GitHub Actions behavior

`.github/workflows/public-validation.yml` runs on pull requests and pushes to `main`. It has read-only repository permissions and contains no merge, release, Pages, deployment, or write step.

A maintainer may use the workflow as a required status check. GitHub branch protection remains a human-administered repository setting; the workflow cannot configure or bypass it.

## Public artifact formats

Machine-readable examples live under:

- `examples/receipts/`;
- `examples/scaffolded-project/`;
- `examples/field-trials/`;
- `examples/review-bundles/`.

Human-readable generated or filled examples live under `examples/review-packets/` and the other example folders.

The public structures preserve:

- identity and version;
- identified human authority;
- stage separation;
- privacy and no-network declarations;
- evidence or observation records;
- source conditions and limitations;
- pending or human-authorized decision status.

Additional fields do not become official Parallax fields merely because a downstream validator permits them.

## Proving-report generator boundary

The proving-report generator converts a structured test-input file into a Markdown proving-ground draft. It counts test outcomes, preserves observations and evidence references, lists limitations, and leaves the release decision pending.

It does not infer truth, hide failures, choose a release recommendation, or sign on behalf of a human reviewer.

## Field-trial boundary

The field-trial validator checks required consent flags, allowed status values, observation structure, evidence limits, and maintainer-decision fields.

It cannot verify that participation was actually voluntary, that the trial occurred, that observations are accurate or representative, that identifying information was fully removed, or that a proposed change should be accepted.

## Evidence-review boundary

The review validator and generator cannot establish that:

- source receipts are authentic;
- consent or observation quality was sufficient;
- different conditions are comparable;
- repeated values are true or representative;
- divergent values should be resolved in one direction;
- combining receipts produces stronger evidence;
- a release, documentation change, or roadmap decision is justified.

Counts in a packet are inventories of declared values. They are not usability scores, statistical findings, confidence estimates, or votes.

## Security and privacy

Do not run these public tools against secrets, private Parallax material, client records, personal conversations, regulated data, or sensitive research. They are not a sanitization system. Review free text before placing it in a public working tree, generated packet, or GitHub issue.
