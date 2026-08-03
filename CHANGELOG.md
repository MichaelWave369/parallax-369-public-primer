# Changelog

All notable public changes to this repository will be recorded here.

## [Unreleased]

### Planned

- gather and classify real public feedback, field-trial observations, and evidence-review experience;
- run additional user and assistive-technology tests without overstating coverage;
- revise the public roadmap only after evidence or a clearly documented maintainer decision justifies new work.

## [0.5.0-candidate] — 2026-08-02

### Added

- public evidence-review protocol for multiple same-project field-trial receipts;
- evidence-review receipt template preserving compatibility limits, divergence, dissent, and human decision authority;
- machine-readable review-bundle schema with explicit no-score, no-majority-truth, and no-automatic-decision rules;
- standard-library-only review-bundle validator;
- local review-packet generator with safe overwrite refusal;
- second synthetic Pocket Beacon field-trial receipt under different declared conditions;
- synthetic Pocket Beacon review bundle and human-readable packet preserving conflicting outcomes;
- negative fixtures proving cross-project bundles and missing source files are rejected;
- GitHub Pages evidence-review guide;
- v0.5 roadmap proposal issue and public-release review receipt.

### Changed

- field-trial schema now accepts compatible receipt versions `0.4` and `0.5` plus optional `project_key` and `conditions` fields;
- existing synthetic Pocket Beacon trial now declares its project key and conditions for review compatibility;
- unified validation runner now validates review bundles and tests review-packet generation, divergence preservation, no-score language, pending authority, and overwrite refusal;
- template checks now cover six public template contracts;
- local static-site checks now require the evidence-review page;
- README, field-trial protocol, schema guide, validation guide, roadmap, and landing page now surface v0.5.

### Synthesis boundary

The review tools inventory declared outcomes and expose agreement or divergence. They do not authenticate receipts, calculate usability or confidence scores, average incompatible conditions, resolve disagreement by majority vote, recommend release, certify a project, or authorize a roadmap change.

The included receipts, bundle, and packet are synthetic. They do not establish real participant experience, representative usability, accessibility, or controlled replication.

### Public-boundary statement

The v0.5 protocol, schema, validator, generator, fixtures, and examples were authored specifically for this public primer. They do not intentionally include or reconstruct private Parallax prompts, SkillSet logic, agent or swarm orchestration, canon, private validators or schemas, project records, conversations, credentials, connected-account data, or accumulated internal intelligence.

## [0.4.0-candidate] — 2026-08-02

### Added

- first-project quickstart for a local, non-sensitive public-primer project;
- standard-library-only project scaffolder with no network submission and safe overwrite refusal;
- machine-readable public project manifest schema;
- local project validator preserving distinct Stage 3, Stage 6, Stage 9, and field-trial artifacts;
- voluntary, identity-minimized public field-trial protocol and Markdown receipt template;
- machine-readable field-trial receipt schema and validator;
- synthetic first-use field-trial receipt with a partially clear validator-boundary finding;
- intentionally invalid field-trial fixture proving false consent and empty observations are rejected;
- synthetic scaffolded Tool Sign-Out Board project with a preserved failed understanding test;
- field-trial feedback issue template;
- GitHub Pages quickstart guide;
- v0.4 roadmap proposal issue and public-release review receipt.

### Changed

- unified validation runner checks public projects, field-trial receipts, scaffold creation, authority preservation, no-network declaration, and overwrite refusal;
- template completeness checks include the field-trial receipt contract;
- schema and validation documentation covers project manifests and field-trial limitations;
- README and live site identify v0.4 and surface the adoption kit;
- roadmap records that no real feedback issue existed at planning time and keeps real feedback gathering open.

### Adoption boundary

The scaffolder creates a local folder from public templates. It does not upload content, authenticate evidence, establish project quality, validate consent, certify usability, or authorize release.

The included field trial is synthetic. It does not establish real participant experience or complete the ongoing public-feedback roadmap item.

## [0.3.0-candidate] — 2026-08-02

### Added

- documented public validation-helper contract and claim boundaries;
- lightweight public receipt and report-input schemas;
- standard-library-only receipt validator with claim-to-evidence reference checks;
- public template completeness checks tied to method boundaries;
- local Markdown and HTML link checks plus static-site entry-point checks;
- local-only Markdown proving-report generator that preserves supplied failures and leaves release authority pending;
- unified local runner with Python syntax compilation and generator smoke testing;
- synthetic machine-readable receipt and generator input examples;
- read-only GitHub Actions workflow for pull requests and pushes to `main`;
- GitHub Pages validation-helper guide;
- v0.3 public-release review receipt.

### Validation boundary

A passing helper or workflow result establishes only that the declared structural checks passed against the inspected public files. It does not authenticate evidence, establish truth, certify safety or accessibility, accept risk, or authorize merge, publication, deployment, release, or endorsement.

## [0.2.0-candidate] — 2026-08-02

### Added

- structured public feedback guide and GitHub issue template;
- accessibility review receipt with preserved limitations and future evidence requests;
- concise printable one-page primer for screen and paper;
- public glossary for governance, evidence, receipt, and status terminology;
- filled synthetic decision-receipt example;
- Community Seed-Swap Station non-software walkthrough with a preserved participant-understanding failure;
- downstream compatibility, adaptation, migration, and versioning rules;
- v0.2 resources surfaced through the GitHub Pages site.

### Accessibility boundary

The v0.2 source review is not WCAG certification or proof that no accessibility barriers remain. It records current structure, known limitations, and requested future tests.

## [0.1.0-candidate] — 2026-08-02

### Added

- public Stage 3, Stage 6, and Stage 9 guides;
- controlling-specification, implementation-receipt, proving-report, and release-review templates;
- controlling public-release boundary;
- governance, security, contribution, conduct, licensing, and notice documents;
- fictional Pocket Beacon end-to-end walkthrough with a preserved failed test;
- responsive GitHub Pages site with an accessible stage explorer.

### Boundary statement

This release was authored as a limited public primer. It does not intentionally include private Parallax prompts, skill logic, orchestration, canon, schemas, project records, conversations, connected-account data, or accumulated internal intelligence.
