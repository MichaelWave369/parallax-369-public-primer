# Public Schemas

These schemas describe small machine-readable structures for public receipts, report inputs, local project manifests, field-trial observations, and same-project evidence-review bundles. They are public-primer artifacts only and do not expose or represent private Parallax schemas.

## Files

- `public-receipt.schema.json` — common receipt identity, authority, evidence, claims, limitations, and status fields.
- `report-input.schema.json` — structured input accepted by the local Markdown report generator.
- `public-project.schema.json` — manifest for a local Stage 3 / Stage 6 / Stage 9 project scaffold.
- `field-trial-receipt.schema.json` — identity-minimized structure for voluntary public-primer usability observations.
- `review-bundle.schema.json` — manifest for locally reviewing two or more field-trial receipts from one declared project.

## Supported validation subset

The public validators intentionally support only:

- `type`;
- `required`;
- `properties`;
- `items`;
- `enum`;
- `const`;
- `minLength`;
- `minItems`;
- `minimum`;
- `additionalProperties: false`.

They do not claim full JSON Schema compatibility. Keywords outside this list are documentation unless another validator is used.

## Discovery and path rules

By default:

- `validate_receipts.py` checks `examples/receipts/*.json`;
- `validate_projects.py` checks `examples/scaffolded-project/project.json` and its declared local artifacts;
- `validate_field_trials.py` checks `examples/field-trials/*.json`;
- `validate_review_bundles.py` checks `examples/review-bundles/*.json` and every referenced field-trial receipt.

Declared repository paths are resolved within the repository root; traversal outside the repository is rejected. Review bundles reject missing source files, duplicate references, trial-ID mismatches, invalid source receipts, and receipts whose `project_key` differs from the bundle.

Project manifests resolve artifact paths within the project folder. Stage 3, Stage 6, Stage 9, and field-trial artifacts must remain distinct files.

## Field-trial v0.5 compatibility extension

The field-trial receipt schema accepts receipt versions `0.4` and `0.5`. Version 0.5 adds optional public fields:

- `project_key` — required when a receipt is included in a review bundle;
- `conditions` — interaction mode, platform, facilitation, and notes used to keep comparison limits visible.

Existing v0.4 receipts remain structurally valid without these fields. They must be migrated or adapted before v0.5 bundle review because cross-receipt project identity cannot be inferred safely from prose.

## Privacy design

The field-trial and review-bundle schemas contain no participant-name, email, phone, handle, recording, or contact field.

That design reduces collection pressure but is not a complete privacy safeguard. Free-text observations, condition notes, inclusion reasons, and evidence limits still require human review before public submission.

## Review-bundle authority boundary

The review bundle requires explicit rules preserving:

- one declared project;
- every source trial;
- no scoring;
- no majority-vote truth claim;
- no automatic decision.

The validator checks those declarations and source relationships. It does not determine whether the chosen receipts are representative, comparable, ethically gathered, accurate, or sufficient for action.

## Status and claim boundaries

Schema validity means the file has the required shape and permitted values. It does not establish that:

- a project or trial actually occurred;
- evidence or consent is authentic;
- observations are accurate;
- source conditions are comparable;
- combining receipts strengthens the evidence;
- claims are true;
- tests were competently designed;
- a project is safe, legal, accessible, production-ready, or certified;
- a human release or roadmap decision has been granted.

## Adaptation

Downstream projects may copy and extend these schemas under the MIT License. Extensions should publish an adaptation receipt and must not imply official Parallax endorsement, certification, or access to private systems.
