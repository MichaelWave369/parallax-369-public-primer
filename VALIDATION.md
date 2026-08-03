# Public Validation Helpers

Version 0.3 adds small, local-first checks for the independently authored public primer. These tools are intentionally limited. They help detect structural problems; they do not certify truth, safety, legality, accessibility, engineering adequacy, or release readiness.

## Design rules

1. **Standard library only.** The helpers require Python 3.11 or newer and no network access or third-party packages.
2. **Public artifacts only.** They inspect this repository's public templates, static site, schemas, and synthetic examples.
3. **Fail visibly.** A failed or blocked check returns a non-zero exit code and prints the affected path.
4. **No authority inheritance.** Checks may block a pull request. They cannot approve, merge, publish, tag, release, or certify anything.
5. **No external-link claims.** The link checker verifies local targets only; it does not claim that external websites are reachable or trustworthy.
6. **Schema scope is explicit.** The receipt validator implements the documented subset in `schemas/README.md`, not the entire JSON Schema standard.

## Run all public checks

From the repository root:

```bash
python scripts/run_public_checks.py
```

The command runs:

- public JSON receipt validation;
- Markdown template completeness checks;
- local Markdown and HTML link checks;
- static-site entry-point and asset checks;
- a deterministic report-generator smoke test.

## Run one check

```bash
python scripts/validate_receipts.py
python scripts/check_templates.py
python scripts/check_links.py
python scripts/generate_report.py examples/report-input/pocket-beacon.json --output /tmp/pocket-beacon-report.md
```

## Exit status

- `0` — every check executed by that command passed in its declared scope.
- `1` — at least one check failed.
- `2` — command usage or input parsing failed.

A passing exit status means only that the declared structural checks passed against the inspected files.

## GitHub Actions behavior

`.github/workflows/public-validation.yml` runs on pull requests and pushes to `main`. It has read-only repository permissions and contains no merge, release, Pages, deployment, or write step.

A maintainer may use the workflow as a required status check. GitHub branch protection remains a human-administered repository setting; the workflow cannot configure or bypass it.

## Public receipt format

Machine-readable examples live in `examples/receipts/`. Each receipt names its local schema using `schema_file`. The schema captures a small common envelope:

- identity and version;
- stage and status;
- identified human authority;
- evidence records;
- claim classifications and evidence links;
- limitations;
- timestamp.

Projects may add fields. Additional fields do not become official Parallax fields merely because the lightweight validator permits them.

## Generator boundary

The local report generator converts a structured test-input file into a Markdown proving-ground draft. It:

- counts test outcomes;
- preserves observations and evidence references;
- lists limitations;
- leaves the release decision pending.

It does not infer truth, hide failures, choose a release recommendation, or sign on behalf of a human reviewer.

## Security and privacy

Do not run these public tools against secrets, private Parallax material, client records, personal conversations, or regulated data. They are not a sanitization system. Review content before placing it in a public working tree.
