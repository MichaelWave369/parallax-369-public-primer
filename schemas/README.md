# Public Receipt Schemas

These schemas describe a small machine-readable envelope for public receipts and report-generator inputs. They are public-primer artifacts only and do not expose or represent private Parallax schemas.

## Files

- `public-receipt.schema.json` — common receipt identity, authority, evidence, claims, limitations, and status fields.
- `report-input.schema.json` — structured input accepted by the local Markdown report generator.

## Supported validation subset

`scripts/validate_receipts.py` intentionally supports only:

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

It does not claim full JSON Schema compatibility. Keywords outside this list are documentation unless another validator is used.

## Receipt discovery

By default, the validator checks every `*.json` file under `examples/receipts/`. A receipt must include:

```json
{
  "schema_file": "schemas/public-receipt.schema.json"
}
```

The path is resolved from the repository root. Absolute paths and paths outside the repository are rejected.

## Status and claim boundaries

Schema validity means the file has the required shape and permitted values. It does not establish that:

- evidence is authentic;
- observations are accurate;
- claims are true;
- tests were competently designed;
- a project is safe, legal, accessible, production-ready, or certified;
- a human release decision has been granted.

## Adaptation

Downstream projects may copy and extend these schemas under the MIT License. Extensions should publish an adaptation receipt and must not imply official Parallax endorsement or access to private systems.
