# Parallax 3–6–9 Public Primer

> **Public Candidate v0.3** — A human-led method for moving from idea, to implementation, to evidence.

The Parallax 3–6–9 Method separates three activities that are often blurred together:

| Stage | Job | Primary public artifact |
|---|---|---|
| **3 — Specify** | Define what is being proposed, what must be true, who retains authority, and what remains unknown. | Controlling specification |
| **6 — Build** | Create the smallest honest candidate while preserving traceability, limitations, and deviations. | Implementation receipt |
| **9 — Prove** | Test the candidate against explicit criteria and preserve evidence, failures, and unsupported claims. | Proving-ground report |

## Core rule

> **A specification is not an implementation. An implementation is not evidence. Evidence does not authorize claims beyond its scope.**

## Why this primer exists

Development processes often let intent, construction, and validation collapse into one polished output. That makes it easy for assumptions to become “facts,” mocks to become “features,” and successful demonstrations to become claims far beyond the tested conditions.

The public method introduces a simpler discipline:

1. define the target without pretending it has been built;
2. build the candidate without rewriting the target to match it;
3. test the candidate without hiding failure or expanding the evidence.

Humans retain authority over scope, risk, acceptance, publication, and release.

## Start here

- [Live public site](https://michaelwave369.github.io/parallax-369-public-primer/)
- [One-page printable primer](https://michaelwave369.github.io/parallax-369-public-primer/primer.html)
- [Public validation helpers](https://michaelwave369.github.io/parallax-369-public-primer/validation.html)
- [Stage 3 — Specify](method/03-specify.md)
- [Stage 6 — Build](method/06-build.md)
- [Stage 9 — Prove](method/09-prove.md)
- [Public glossary](GLOSSARY.md)
- [Public-release boundary](PUBLIC_RELEASE_BOUNDARY.md)

## Public templates

- [Controlling specification](templates/controlling-specification.md)
- [Implementation receipt](templates/implementation-receipt.md)
- [Proving-ground report](templates/proving-ground-report.md)
- [Public-release review](templates/public-release-review.md)

## Synthetic examples

- [Pocket Beacon — software walkthrough](examples/pocket-beacon/README.md)
- [Community Seed-Swap Station — non-software walkthrough](examples/seed-swap-station/README.md)
- [Filled decision receipt](examples/decision-receipt-example.md)
- [Machine-readable proving receipt](examples/receipts/pocket-beacon-proving-receipt.json)
- [Local report-generator input](examples/report-input/pocket-beacon.json)

The examples are fictional. They teach traceability and scoped evidence; they are not product validation or field proof.

## v0.3 public validation helpers

Version 0.3 adds local-first structural checks without adding autonomous authority:

- [Validation guide and claim boundaries](VALIDATION.md)
- [Public receipt schemas](schemas/README.md)
- [Validation scripts](scripts/)
- [Read-only GitHub Actions gate](.github/workflows/public-validation.yml)
- [v0.3 public-release review](releases/v0.3-public-release-review.md)

Run every public check from the repository root:

```bash
python scripts/run_public_checks.py
```

The helpers validate public receipt shape, required template sections, local links, static-site entry points, and deterministic report generation. A passing result is limited to those declared structural checks. It is not certification, evidence authentication, risk acceptance, or release approval.

The GitHub workflow can report a blocking failure when branch protection is configured by a human administrator. It has read-only repository permissions and no merge, publication, deployment, tagging, release, or certification step.

## v0.2 usability and review kit

- [Accessibility review receipt](ACCESSIBILITY_REVIEW_v0.2.md)
- [Public feedback guide](FEEDBACK.md)
- [Compatibility and versioning rules](COMPATIBILITY_AND_VERSIONING.md)
- [v0.2 public-release review](releases/v0.2-public-release-review.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

The repository includes a public feedback issue template. Feedback gathering remains ongoing after release; the existence of a feedback channel is not evidence that every user or accessibility need has been represented.

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
- a green workflow for human approval;
- model confidence for independent evidence;
- repository inclusion for Parallax certification.

## Status vocabulary

Use explicit labels where applicable:

`Proposed` · `Candidate` · `Implemented` · `Simulated` · `Mocked` · `Deferred` · `Failed` · `Blocked` · `Inconclusive` · `Not run` · `Verified in scope` · `Unknown`

## Tool independence

The public method is not tied to a particular model, company, programming language, project-management platform, or deployment service. A person or team can use the templates manually or adapt them to their own accountable workflow.

The optional v0.3 helpers use Python 3.11 or newer and only the Python standard library. Downstream projects should read [COMPATIBILITY_AND_VERSIONING.md](COMPATIBILITY_AND_VERSIONING.md) before describing themselves as compatible with the public primer.

## Contributing and feedback

Public contributions are welcome when they are independently created for this primer and respect the publication boundary. Read [CONTRIBUTING.md](CONTRIBUTING.md), [FEEDBACK.md](FEEDBACK.md), [SECURITY.md](SECURITY.md), and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License and notice

Repository content is available under the [MIT License](LICENSE). The license does not authorize false claims of origin, affiliation, certification, endorsement, or review. Read [NOTICE.md](NOTICE.md).

## Important limitation

**Educational / experimental public candidate.** Use of this repository does not constitute Parallax certification, scientific validation, legal approval, safety approval, or evidence that a downstream project is suitable beyond its documented test conditions.

---

**Do not ask people to trust the intelligence. Let them inspect the decisions, implementation, and receipts.**
