# Public Schemas

These schemas describe small machine-readable structures for public receipts, report inputs, local project manifests, and field-trial observations. They are public-primer artifacts only and do not expose or represent private Parallax schemas.

## Files

- `public-receipt.schema.json` — common receipt identity, authority, evidence, claims, limitations, and status fields.
- `report-input.schema.json` — structured input accepted by the local Markdown report generator.
- `public-project.schema.json` — manifest for a local Stage 3 / Stage 6 / Stage 9 project scaffold.
- `field-trial-receipt.schema.json` — minimal, identity-free structure for voluntary public-primer usability observations.

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

## Receipt discovery

By default:

- `validate_receipts.py` checks `examples/receipts/*.json`;
- `validate_projects.py` checks `examples/scaffolded-project/project.json` and its declared local artifacts;
- `validate_field_trials.py` checks `examples/field-trials/*.json`.

Public receipt envelopes may name a local schema using `schema_file`. Declared repository paths are resolved within the repository root; traversal outside the repository is rejected.

Project manifests resolve artifact paths within the project folder. Stage 3, Stage 6, Stage 9, and field-trial artifacts must remain distinct files.

## Field-trial privacy design

The field-trial JSON schema intentionally contains no participant-name, email, phone, handle, recording, or contact field.

That design reduces collection pressure but is not a complete privacy safeguard. Free-text observations still require human review before public submission.

## Status and claim boundaries

Schema validity means the file has the required shape and permitted values. It does not establish that:

- a project or trial actually occurred;
- evidence is authentic;
- observations are accurate;
- consent was legally or ethically sufficient;
- claims are true;
- tests were competently designed;
- a project is safe, legal, accessible, production-ready, or certified;
- a human release decision has been granted.

## Adaptation

Downstream projects may copy and extend these schemas under the MIT License. Extensions should publish an adaptation receipt and must not imply official Parallax endorsement, certification, or access to private systems.
