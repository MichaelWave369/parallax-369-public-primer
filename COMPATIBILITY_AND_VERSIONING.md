# Compatibility and Versioning Rules

These rules apply to the independently authored public primer and downstream adaptations of its public artifacts. They do not govern private Parallax systems.

## Version format

Public primer releases use semantic-style versions:

- **Major** (`1.0.0`) — a change to the public method contract that may require downstream adaptation.
- **Minor** (`0.2.0`) — backward-compatible additions, clarifications, examples, or usability improvements.
- **Patch** (`0.2.1`) — corrections that do not intentionally change the public method contract.

Versions below `1.0.0` remain public candidates. Candidate status does not remove the obligation to document breaking changes.

## Stable method contract

A downstream adaptation may describe itself as **Parallax 3–6–9 compatible** only when it preserves all of the following:

1. **Stage separation** — specification, implementation, and evidence remain distinct.
2. **Human authority** — publication and material risk decisions remain assigned to an identified human authority.
3. **Visible uncertainty** — assumptions, unknowns, limitations, and unresolved decisions are not silently converted into facts.
4. **Traceability** — requirements can be connected to implementation status and evidence.
5. **Status honesty** — mocks, simulations, deferred work, failures, blocked tests, and inconclusive results remain labeled.
6. **Claim boundaries** — evidence is not extended beyond its declared conditions.
7. **Receipt preservation** — decisions and changes can be reconstructed from versioned records.
8. **No self-certification** — compatibility does not imply Parallax endorsement, certification, professional approval, or scientific validity.

## Compatibility statements

Use one of these statements:

### Inspired by

Use when an adaptation borrows ideas but does not preserve the complete public method contract.

> Inspired by the Parallax 3–6–9 Public Primer.

### Public-primer compatible

Use only when the stable method contract above is preserved.

> Designed for compatibility with Parallax 3–6–9 Public Primer v0.2.0. This statement is self-declared and does not imply endorsement or certification.

### Traceably adapted

Use when the adaptation preserves the contract and publishes a mapping of changed fields, terminology, or workflow.

> Traceably adapted from Parallax 3–6–9 Public Primer v0.2.0. See the adaptation receipt for modifications and limitations.

## Adaptation receipt

A downstream adaptation should publish:

- source primer version;
- files or templates used;
- renamed or removed fields;
- added stages, gates, or statuses;
- changed authority model;
- changed claim or evidence rules;
- known incompatibilities;
- migration guidance;
- license and attribution notice.

## Compatibility does not require identical formatting

An adaptation may use different software, file formats, terminology, visual design, or organizational structure. Compatibility concerns the method contract, not cosmetic identity.

## Breaking changes

A change is breaking when it removes or materially alters a required public method behavior, including:

- merging specification, implementation, and proof into an indistinguishable artifact;
- removing human release authority;
- eliminating visible failure or deferred-work statuses;
- allowing simulation to be reported as field evidence without qualification;
- removing the ability to reconstruct requirement-to-evidence traceability.

Breaking changes require a major-version increment or an explicit incompatibility statement.

## Deprecation

A public field or rule should be marked deprecated before removal when practical. A deprecation notice should name:

- the affected artifact;
- the replacement;
- the first version carrying the notice;
- the earliest version in which removal may occur.

## Migration principle

Migrations must preserve provenance. Do not overwrite the original artifact merely to make it conform to a newer version. Retain the source, produce a separately versioned candidate, and record the transformation.

## Publication boundary

No compatibility claim authorizes access to or reconstruction of private Parallax prompts, orchestration, canon, validators, schemas, research, conversations, or project records.
