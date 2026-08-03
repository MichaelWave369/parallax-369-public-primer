# Parallax 3–6–9 Public Primer

> **Public Candidate v0.5** — A human-led method for moving from idea, to implementation, to evidence.

The Parallax 3–6–9 Method separates three activities that are often blurred together:

| Stage | Job | Primary public artifact |
|---|---|---|
| **3 — Specify** | Define what is being proposed, what must be true, who retains authority, and what remains unknown. | Controlling specification |
| **6 — Build** | Create the smallest honest candidate while preserving traceability, limitations, and deviations. | Implementation receipt |
| **9 — Prove** | Test the candidate against explicit criteria and preserve evidence, failures, and unsupported claims. | Proving-ground report |

## Core rule

> **A specification is not an implementation. An implementation is not evidence. Evidence does not authorize claims beyond its scope.**

Humans retain authority over scope, risk, interpretation, acceptance, publication, and release.

## Start here

- [Live public site](https://michaelwave369.github.io/parallax-369-public-primer/)
- [First project quickstart](https://michaelwave369.github.io/parallax-369-public-primer/quickstart.html)
- [Evidence review guide](https://michaelwave369.github.io/parallax-369-public-primer/review.html)
- [One-page printable primer](https://michaelwave369.github.io/parallax-369-public-primer/primer.html)
- [Public validation helpers](https://michaelwave369.github.io/parallax-369-public-primer/validation.html)
- [Stage 3 — Specify](method/03-specify.md)
- [Stage 6 — Build](method/06-build.md)
- [Stage 9 — Prove](method/09-prove.md)
- [Public glossary](GLOSSARY.md)
- [Public-release boundary](PUBLIC_RELEASE_BOUNDARY.md)

## v0.5 evidence review and synthesis kit

Version 0.5 adds a local-first way to review multiple field-trial receipts from the **same declared project** without flattening disagreement or manufacturing authority.

- [Evidence Review Protocol](EVIDENCE_REVIEW.md)
- [Evidence-review receipt template](templates/evidence-review-receipt.md)
- [Review-bundle schema](schemas/review-bundle.schema.json)
- [Review-bundle validator](scripts/validate_review_bundles.py)
- [Local review-packet generator](scripts/generate_review_packet.py)
- [Synthetic Pocket Beacon bundle](examples/review-bundles/pocket-beacon-review.json)
- [Synthetic review packet](examples/review-packets/pocket-beacon-review.md)
- [v0.5 roadmap proposal](https://github.com/MichaelWave369/parallax-369-public-primer/issues/7)

Validate and generate locally:

```bash
python scripts/validate_review_bundles.py
python scripts/generate_review_packet.py \
  examples/review-bundles/pocket-beacon-review.json \
  --output /tmp/pocket-beacon-review.md
```

The review kit:

- requires at least two valid source receipts;
- requires every receipt to declare the same `project_key`;
- preserves each trial, condition, observation, limitation, and source decision status;
- surfaces points of agreement and divergence separately;
- inventories declared outcomes without producing a score;
- refuses missing files, cross-project bundles, duplicate sources, and trial-ID mismatches;
- leaves interpretation, candidate actions, and the human decision pending;
- performs no network submission or telemetry.

Counts in a review packet are inventories—not statistical findings, confidence values, rankings, or votes.

## v0.4 adoption and field-trial kit

Version 0.4 makes it easier to try the public method in a local workflow without adding telemetry, private machinery, or autonomous authority.

- [First Project Quickstart](QUICKSTART.md)
- [Public Field-Trial Protocol](FIELD_TRIAL.md)
- [Field-trial receipt template](templates/field-trial-receipt.md)
- [Public project manifest schema](schemas/public-project.schema.json)
- [Field-trial receipt schema](schemas/field-trial-receipt.schema.json)
- [Synthetic scaffolded project](examples/scaffolded-project/)
- [Synthetic first-use trial](examples/field-trials/pocket-beacon-first-use.json)

Create and validate a local project:

```bash
python scripts/init_public_project.py \
  --name "Neighborhood Notice Board" \
  --human-authority "Project owner" \
  --output work/notice-board

python scripts/validate_projects.py work/notice-board
```

The scaffolder copies only public templates, creates separate Stage 3, Stage 6, Stage 9, and field-trial artifacts, performs no network submission, records human authority, and refuses to overwrite an existing destination.

## Public templates

- [Controlling specification](templates/controlling-specification.md)
- [Implementation receipt](templates/implementation-receipt.md)
- [Proving-ground report](templates/proving-ground-report.md)
- [Field-trial receipt](templates/field-trial-receipt.md)
- [Evidence-review receipt](templates/evidence-review-receipt.md)
- [Public-release review](templates/public-release-review.md)

## Synthetic examples

- [Pocket Beacon — software walkthrough](examples/pocket-beacon/README.md)
- [Community Seed-Swap Station — non-software walkthrough](examples/seed-swap-station/README.md)
- [Scaffolded Tool Sign-Out Board](examples/scaffolded-project/README.md)
- [Filled decision receipt](examples/decision-receipt-example.md)
- [Machine-readable proving receipt](examples/receipts/pocket-beacon-proving-receipt.json)
- [Pocket Beacon field trial A](examples/field-trials/pocket-beacon-first-use.json)
- [Pocket Beacon field trial B](examples/field-trials/pocket-beacon-keyboard-only.json)
- [Pocket Beacon review bundle](examples/review-bundles/pocket-beacon-review.json)
- [Pocket Beacon review packet](examples/review-packets/pocket-beacon-review.md)

The examples are fictional. They teach traceability and scoped evidence; they are not product validation, participant research, representative usability evidence, or field proof.

## Public validation helpers

Run every public check from the repository root:

```bash
python scripts/run_public_checks.py
```

The suite checks:

- proving receipts and evidence references;
- project manifests and stage separation;
- field-trial receipts and consent declarations;
- review bundles and source relationships;
- six public template contracts;
- local Markdown and HTML links;
- static-site entry points;
- proving-report and review-packet generation;
- project scaffolding and safe-write behavior;
- intentional invalid fixtures that must be rejected.

Read [VALIDATION.md](VALIDATION.md) and [schemas/README.md](schemas/README.md) for exact scope and limitations.

The GitHub workflow can report a blocking failure when branch protection is configured by a human administrator. It has read-only repository permissions and no merge, publication, deployment, tagging, release, or certification step.

## Usability, accessibility, and adaptation

- [Accessibility review receipt](ACCESSIBILITY_REVIEW_v0.2.md)
- [Public feedback guide](FEEDBACK.md)
- [Compatibility and versioning rules](COMPATIBILITY_AND_VERSIONING.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

Public feedback gathering remains ongoing. Issue templates, synthetic trials, and synthetic review packets are not evidence that every user, accessibility need, or domain has been represented.

## GitHub Pages site

The static site lives in [`docs/`](docs/) and is published through GitHub Pages from the `main` branch `/docs` folder. It uses no external framework, analytics, remote fonts, or third-party runtime assets.

## Public-release boundary

This repository is independently authored as an intentionally limited **public primer**. It is not a direct mirror, sanitized export, or reconstruction path for:

- private Parallax skill instructions or system prompts;
- internal agent or swarm orchestration;
- private canon, ledgers, validators, schemas, or research;
- private project files, evidence, decisions, or accumulated intelligence;
- personal conversations, client information, credentials, connected-account data, or deployment configuration.

Read [`PUBLIC_RELEASE_BOUNDARY.md`](PUBLIC_RELEASE_BOUNDARY.md) before contributing or releasing anything.

## No trust laundering

The primer prohibits substitutions such as:

- a polished document for a validated specification;
- a specification for a working implementation;
- a simulation or mock for field evidence;
- a passing test for universal truth;
- schema validity for evidence authenticity;
- a scaffold for project quality;
- a field-trial receipt for representative research;
- repeated values for statistical truth;
- a review bundle for comparability;
- a count for a score or vote;
- a green workflow for human approval;
- model confidence for independent evidence;
- repository inclusion for Parallax certification.

## Tool independence

The method is not tied to a particular model, company, language, project-management platform, or deployment service. The optional public helpers use Python 3.11 or newer and only the Python standard library.

Downstream projects should read [COMPATIBILITY_AND_VERSIONING.md](COMPATIBILITY_AND_VERSIONING.md) before describing themselves as compatible with the public primer.

## Contributing and feedback

Public contributions are welcome when they are independently created for this primer and respect the publication boundary. Read [CONTRIBUTING.md](CONTRIBUTING.md), [FEEDBACK.md](FEEDBACK.md), [FIELD_TRIAL.md](FIELD_TRIAL.md), [EVIDENCE_REVIEW.md](EVIDENCE_REVIEW.md), [SECURITY.md](SECURITY.md), and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License and notice

Repository content is available under the [MIT License](LICENSE). The license does not authorize false claims of origin, affiliation, certification, endorsement, or review. Read [NOTICE.md](NOTICE.md).

## Important limitation

**Educational / experimental public candidate.** Use of this repository does not constitute Parallax certification, scientific validation, legal approval, safety approval, consent verification, statistical validation, or evidence that a downstream project is suitable beyond its documented conditions.

---

**Do not ask people to trust the intelligence. Let them inspect the decisions, implementation, and receipts.**
