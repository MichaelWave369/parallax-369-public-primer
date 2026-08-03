# Governance

## 1. Purpose

This repository presents a limited, public, educational version of the Parallax 3–6–9 Method. Governance exists to preserve human authority, traceability, claim discipline, and the separation between public teaching material and private Parallax systems.

## 2. Human authority

Humans retain authority over:

- project scope and intended outcomes;
- acceptance criteria and risk tolerances;
- publication, release, and certification decisions;
- exceptions, waivers, and unresolved disagreements;
- whether evidence is sufficient for a specific claim.

Automation may organize, compare, draft, build, test, and recommend. It may not silently redefine the project, expand a claim, approve its own work, or publish protected material.

## 3. The 3–6–9 separation

The public method is governed by three distinct stages:

### 3 — Specify

Create a controlling description of the intended work. Separate facts, assumptions, hypotheses, and proposals. Record requirements, authority, open questions, acceptance criteria, and provenance.

### 6 — Build

Create the smallest honest candidate that addresses the controlling specification. Preserve implementation status, deviations, dependencies, limitations, mocks, simulations, and reproducible build information.

### 9 — Prove

Evaluate the candidate against the acceptance criteria. Preserve passing and failing evidence, environmental limits, reproducibility information, unresolved claims, and the human release decision.

No stage may impersonate another.

## 4. No trust laundering

The following substitutions are prohibited:

- a polished document for a validated specification;
- a specification for a working implementation;
- a simulation or mock for field evidence;
- a passing test for universal truth;
- model confidence for independent evidence;
- contributor reputation for reproducibility;
- repository inclusion for Parallax certification.

## 5. Status vocabulary

Public artifacts should use explicit status language where applicable:

- **Proposed** — suggested but not accepted;
- **Candidate** — accepted for evaluation, not proven;
- **Implemented** — present in the candidate;
- **Simulated** — represented in a controlled simulation only;
- **Mocked** — substituted with a non-production component;
- **Deferred** — intentionally postponed;
- **Failed** — did not satisfy the stated criterion;
- **Verified in scope** — supported only within the documented test conditions;
- **Unknown** — evidence is insufficient.

## 6. Decision and dissent preservation

Material disagreements should be recorded rather than silently flattened. A decision receipt should state:

- the decision;
- who held authority;
- the alternatives considered;
- the evidence available;
- dissent or unresolved concerns;
- the date and version affected.

## 7. Public release control

`PUBLIC_RELEASE_BOUNDARY.md` is controlling for publication safety. Any conflict is resolved in favor of the stricter privacy, security, licensing, and capability boundary.

## 8. Changes to the method

Substantive changes should arrive through a pull request containing:

- the reason for the change;
- affected public contracts or templates;
- compatibility implications;
- a synthetic example when practical;
- an explicit statement that no private Parallax material was used.

## 9. Certification and endorsement

This repository is a primer, not a certification authority. Forks and downstream projects must not imply official approval, validation, endorsement, or affiliation without explicit written authorization.

## 10. Versioning

Public releases use semantic-style version labels while the primer is experimental:

- patch: corrections that do not change the public method;
- minor: additive templates, examples, or compatible clarifications;
- major: changes to stage boundaries, governance, or public contracts.

Every release should preserve a changelog and a release-boundary review receipt.