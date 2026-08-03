# Public Roadmap

The roadmap applies only to this independently authored public primer. It is not a roadmap for private Parallax systems.

## v0.1 — Public foundation

- [x] Explain the 3–6–9 stage separation.
- [x] Establish the public-release boundary.
- [x] Publish blank templates.
- [x] Publish one synthetic end-to-end example.
- [x] Build the static GitHub Pages site.
- [x] Add governance, security, contribution, and licensing documents.

## v0.2 — Usability and review

- [x] Open a structured public feedback channel and issue template.
- [ ] Gather public feedback on clarity and usefulness. **Ongoing after v0.2 publication.**
- [x] Run and publish an accessibility review of the site and templates.
- [x] Add a concise one-page printable primer.
- [x] Add a glossary and decision-receipt example.
- [x] Add a second synthetic example in a non-software context.
- [x] Clarify compatibility and versioning rules for downstream adaptations.

### v0.2 receipts

- [`FEEDBACK.md`](FEEDBACK.md)
- [`ACCESSIBILITY_REVIEW_v0.2.md`](ACCESSIBILITY_REVIEW_v0.2.md)
- [`docs/primer.html`](docs/primer.html)
- [`GLOSSARY.md`](GLOSSARY.md)
- [`examples/decision-receipt-example.md`](examples/decision-receipt-example.md)
- [`examples/seed-swap-station/README.md`](examples/seed-swap-station/README.md)
- [`COMPATIBILITY_AND_VERSIONING.md`](COMPATIBILITY_AND_VERSIONING.md)
- [`releases/v0.2-public-release-review.md`](releases/v0.2-public-release-review.md)

## v0.3 — Public validation helpers

- [x] Add lightweight schema validation for public receipts.
- [x] Add local broken-link and static-site checks.
- [x] Add public template completeness checks.
- [x] Add a local-only example report generator.
- [x] Add public release-review automation that can block but never self-authorize publication.

### v0.3 receipts

- [`VALIDATION.md`](VALIDATION.md)
- [`schemas/README.md`](schemas/README.md)
- [`scripts/`](scripts/)
- [`.github/workflows/public-validation.yml`](.github/workflows/public-validation.yml)
- [`docs/validation.html`](docs/validation.html)
- [`releases/v0.3-public-release-review.md`](releases/v0.3-public-release-review.md)

### v0.3 authority boundary

The validation workflow may return a pass or failure and may be configured by a human administrator as a required status check. It has no authority or mechanism to merge, publish, deploy, tag, release, certify, or approve a change.

## v0.4 — Adoption and field-trial kit

### Roadmap decision basis

No open public feedback or usability issue was present when v0.4 planning began. Maintainers documented the candidate direction in [roadmap proposal issue #4](https://github.com/MichaelWave369/parallax-369-public-primer/issues/4).

- [x] Add a concise first-project quickstart.
- [x] Add a standard-library-only local project scaffolder.
- [x] Add a public project manifest and schema.
- [x] Add a voluntary, identity-minimized field-trial protocol and receipt.
- [x] Add a synthetic scaffolded-project fixture with a preserved failed understanding test.
- [x] Add structural validation for projects and field-trial receipts.
- [x] Prove that the scaffolder refuses overwrite and performs no declared network submission.
- [x] Add a GitHub Pages quickstart page and public feedback issue template.

### v0.4 receipts

- [`QUICKSTART.md`](QUICKSTART.md)
- [`FIELD_TRIAL.md`](FIELD_TRIAL.md)
- [`templates/field-trial-receipt.md`](templates/field-trial-receipt.md)
- [`schemas/public-project.schema.json`](schemas/public-project.schema.json)
- [`schemas/field-trial-receipt.schema.json`](schemas/field-trial-receipt.schema.json)
- [`scripts/init_public_project.py`](scripts/init_public_project.py)
- [`scripts/validate_projects.py`](scripts/validate_projects.py)
- [`scripts/validate_field_trials.py`](scripts/validate_field_trials.py)
- [`examples/scaffolded-project/`](examples/scaffolded-project/)
- [`examples/field-trials/pocket-beacon-first-use.json`](examples/field-trials/pocket-beacon-first-use.json)
- [`docs/quickstart.html`](docs/quickstart.html)
- [`.github/ISSUE_TEMPLATE/field-trial-feedback.md`](.github/ISSUE_TEMPLATE/field-trial-feedback.md)
- [`releases/v0.4-public-release-review.md`](releases/v0.4-public-release-review.md)

### v0.4 evidence boundary

The included field trial is synthetic. It proves only that the public receipt format and validation path can preserve an observation, an evidence limitation, and a pending human decision. It is not real user research and does not complete the ongoing v0.2 feedback item.

## v0.5 — Evidence review and synthesis kit

### Roadmap decision basis

No open public field-trial, feedback, or accessibility issue was present when v0.5 planning began. The maintainer explicitly requested the next version, and [roadmap proposal issue #7](https://github.com/MichaelWave369/parallax-369-public-primer/issues/7) records the selected need: review multiple same-project receipts without flattening conditions, failures, or disagreement.

- [x] Add a public evidence-review protocol.
- [x] Add an evidence-review receipt template.
- [x] Add a review-bundle manifest and schema.
- [x] Add a standard-library-only review-bundle validator.
- [x] Add a local review-packet generator that produces no score or automatic decision.
- [x] Add two synthetic same-project trials with different conditions and outcomes.
- [x] Add a synthetic review bundle and packet preserving agreement, divergence, observations, and limits.
- [x] Add negative fixtures for cross-project bundling and missing source files.
- [x] Extend the read-only validation suite and static site.

### v0.5 receipts

- [`EVIDENCE_REVIEW.md`](EVIDENCE_REVIEW.md)
- [`templates/evidence-review-receipt.md`](templates/evidence-review-receipt.md)
- [`schemas/review-bundle.schema.json`](schemas/review-bundle.schema.json)
- [`scripts/validate_review_bundles.py`](scripts/validate_review_bundles.py)
- [`scripts/generate_review_packet.py`](scripts/generate_review_packet.py)
- [`examples/field-trials/pocket-beacon-first-use.json`](examples/field-trials/pocket-beacon-first-use.json)
- [`examples/field-trials/pocket-beacon-keyboard-only.json`](examples/field-trials/pocket-beacon-keyboard-only.json)
- [`examples/review-bundles/pocket-beacon-review.json`](examples/review-bundles/pocket-beacon-review.json)
- [`examples/review-packets/pocket-beacon-review.md`](examples/review-packets/pocket-beacon-review.md)
- [`docs/review.html`](docs/review.html)
- [`releases/v0.5-public-release-review.md`](releases/v0.5-public-release-review.md)

### v0.5 synthesis boundary

A review packet may inventory declared outcomes and expose agreement or divergence. It may not authenticate receipts, calculate a usability score, average incompatible conditions, resolve disagreement by majority vote, recommend release, certify a project, or authorize a roadmap change.

All included review receipts and packets remain synthetic and do not complete the ongoing public-feedback item.

## Post-v0.5 direction

The next roadmap revision should be informed by actual public use, submitted feedback, accessibility evidence, a discovered maintenance need, or a separately documented maintainer decision. The repository should not create a v0.6 solely because v0.5 exists.

Candidate directions may include remediations based on real reports, packaging improvements, explicit migrations, or long-term maintenance hardening. Each remains subject to the public-release boundary and human approval.

## Deferred

The following are intentionally not promised by this public repository:

- release of private Parallax SkillSet instructions;
- internal agent or swarm orchestration;
- private canon, validators, research, schemas, or project records;
- telemetry or automatic upload of generated projects, trial receipts, or review packets;
- automated scoring, ranking, certification, or majority-vote truth claims;
- autonomous publication or roadmap authority;
- claims that the method guarantees scientific, legal, engineering, financial, medical, accessibility, consent, or safety validity.

## Roadmap governance

A roadmap item is a proposal, not a commitment or proof of implementation. Completed items should link to a versioned artifact and review receipt. Ongoing work must remain marked ongoing rather than being converted into a completed claim for release convenience.
