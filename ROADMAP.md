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
- [`schemas/public-receipt.schema.json`](schemas/public-receipt.schema.json)
- [`schemas/report-input.schema.json`](schemas/report-input.schema.json)
- [`scripts/`](scripts/)
- [`examples/receipts/pocket-beacon-proving-receipt.json`](examples/receipts/pocket-beacon-proving-receipt.json)
- [`examples/report-input/pocket-beacon.json`](examples/report-input/pocket-beacon.json)
- [`.github/workflows/public-validation.yml`](.github/workflows/public-validation.yml)
- [`docs/validation.html`](docs/validation.html)
- [`releases/v0.3-public-release-review.md`](releases/v0.3-public-release-review.md)

### v0.3 authority boundary

The validation workflow may return a pass or failure and may be configured by a human administrator as a required status check. It has no authority or mechanism to merge, publish, deploy, tag, release, certify, or approve a change.

## Post-v0.3 direction

The next public roadmap revision should be informed by real usage and feedback rather than invented solely to continue version numbering. Candidate directions must remain subject to the public-release boundary and a human-controlled roadmap decision.

## Deferred

The following are intentionally not promised by this public repository:

- release of private Parallax SkillSet instructions;
- internal agent or swarm orchestration;
- private canon, validators, research, schemas, or project records;
- automated Parallax certification;
- autonomous publication authority;
- claims that the method guarantees scientific, legal, engineering, financial, medical, or safety validity.

## Roadmap governance

A roadmap item is a proposal, not a commitment or proof of implementation. Completed items should link to a versioned artifact and review receipt. Ongoing work must remain marked ongoing rather than being converted into a completed claim for release convenience.
