# First Project Quickstart

This guide helps a person or small team start a **public, local, non-sensitive** project with the Parallax 3–6–9 Public Primer.

It does not provide access to private Parallax systems, certify a project, or replace domain expertise.

## Before you begin

Use a project that is safe to document publicly or keep the generated folder outside a public repository.

Do not place credentials, client data, personal conversations, regulated information, private product designs, or private Parallax material into the starter kit.

You need:

- Python 3.11 or newer;
- a local copy of this public repository;
- a project name;
- the name or role of the human who retains scope and release authority.

## 1. Create the local project folder

From the repository root:

```text
python scripts/init_public_project.py \
  --name "Neighborhood Notice Board" \
  --human-authority "Project owner" \
  --output work/notice-board
```

The command refuses to overwrite an existing destination.

It creates:

```text
work/notice-board/
├── README.md
├── project.json
├── stage-3-specification.md
├── stage-6-implementation-receipt.md
├── stage-9-proving-report.md
└── field-trial-receipt.md
```

Nothing is uploaded or transmitted.

## 2. Validate the empty scaffold

```text
python scripts/validate_projects.py work/notice-board
```

A pass means the expected files, manifest fields, stage separation, and human-authority declaration are present. It does not mean the project is complete or valid in the real world.

## 3. Complete Stage 3 — Specify

Open `stage-3-specification.md` and define:

- the original request;
- purpose and scope;
- facts, assumptions, hypotheses, proposals, and unknowns;
- requirements and acceptance criteria;
- risks and prohibited substitutions;
- human authority and the Stage 6 handoff.

Do not begin by polishing a solution. First make the target and uncertainty inspectable.

## 4. Complete Stage 6 — Build

Create the smallest honest candidate and record it in `stage-6-implementation-receipt.md`.

Every in-scope requirement should have a visible status such as:

`Implemented` · `Simulated` · `Mocked` · `Deferred` · `Failed` · `Unknown`

Do not rewrite Stage 3 merely because the build differs from the target. Record deviations and return material scope changes to human review.

## 5. Complete Stage 9 — Prove

Run the acceptance tests and record them in `stage-9-proving-report.md`.

Preserve:

- failed, blocked, inconclusive, and not-run tests;
- raw observations;
- environment and reproduction limits;
- unsupported claims;
- residual risks;
- the human release decision.

A green structural validator cannot make that release decision.

## 6. Run a small field trial

Use `FIELD_TRIAL.md` and `field-trial-receipt.md` to observe whether another person can understand and use the public workflow.

Keep the trial voluntary, minimal, non-sensitive, and scoped. Do not collect unnecessary personal information.

## 7. Run all public checks

From the primer repository root:

```text
python scripts/run_public_checks.py
```

For the generated project:

```text
python scripts/validate_projects.py work/notice-board
```

For completed machine-readable field-trial receipts:

```text
python scripts/validate_field_trials.py path/to/trial.json
```

## What success means

A successful first use produces reconstructable artifacts and honest evidence boundaries.

It does **not** automatically establish:

- product quality;
- safety;
- legality;
- scientific validity;
- professional approval;
- Parallax certification;
- readiness for deployment.

## Return useful feedback

After trying the method, submit a public issue using the **Field Trial Feedback** template only when the content is safe to publish.

Useful feedback names:

- the task attempted;
- where the workflow became clear or confusing;
- what was completed, blocked, or abandoned;
- approximate effort without identifying participants;
- the smallest change likely to improve the public primer.

Human maintainers decide what changes enter a later release.