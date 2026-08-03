# Public Primer Glossary

This glossary defines terms as they are used in the Parallax 3–6–9 Public Primer. It does not claim universal definitions outside this repository.

## Acceptance criterion

A testable condition used to evaluate whether a requirement has been satisfied. A useful criterion names the expected result, conditions, and method of observation.

## Artifact

A versioned output such as a specification, candidate build, test record, decision receipt, or report.

## Assumption

A condition treated as true for planning or construction without sufficient evidence to classify it as a fact. Assumptions must remain visible because a changed assumption can invalidate downstream work.

## Authority

The person or body permitted to approve scope, accept risk, authorize publication, or make another defined decision. Tools may recommend; they do not silently inherit authority.

## Blocked

A test or task that could not be completed because a required dependency, environment, permission, or decision was unavailable.

## Candidate

An artifact offered for evaluation. Candidate status does not mean final, approved, safe, certified, or production-ready.

## Claim

A statement asserting that something is true. Claims must be limited to what the available evidence supports.

## Claim boundary

The explicit limit around what an artifact, test, or body of evidence is allowed to establish.

## Controlling specification

The Stage 3 artifact that defines the governed target for a candidate build. Stage 6 may report deviations but must not silently rewrite the controlling specification.

## Decision receipt

A reconstructable record of a decision, including the question, options, evidence, assumptions, authority, rationale, consequences, dissent, and revisit conditions.

## Deferred

Known work intentionally postponed. Deferred work remains visible and must not be described as implemented.

## Deviation

A documented difference between the controlling specification and the candidate implementation.

## Evidence

Recorded observations that support or weaken a claim within stated conditions. Evidence is not the same as confidence, reputation, polish, or repetition.

## Fact

A statement treated as established within the artifact's declared source and evidence boundary. A fact may still require citation and can be revised when stronger evidence appears.

## Failed

A test result in which the observed outcome did not satisfy the acceptance criterion.

## Handoff

A versioned package that transfers the governing inputs, required outputs, unresolved decisions, and constraints from one stage to the next.

## Hypothesis

A testable explanatory statement that has not yet been established by sufficient evidence.

## Implementation receipt

The Stage 6 record connecting requirements to components, statuses, commands, dependencies, limitations, deviations, and artifact identity.

## Inconclusive

A result that does not support a pass or fail determination because observations were insufficient, conflicting, or outside the required conditions.

## Mock

A substitute that imitates an interface or behavior without providing the full real capability. Mock status must be disclosed.

## Non-scope

Work, behavior, environments, or claims intentionally excluded from the current artifact.

## Proposal

A suggested action, design, or interpretation that has not been authorized as a requirement or accepted decision.

## Provenance

The traceable history of where information, decisions, artifacts, and changes came from.

## Receipt

A durable record that allows another reviewer to reconstruct what was attempted, decided, built, or observed.

## Release recommendation

A Stage 9 recommendation to proceed, proceed with conditions, revise, or stop. It informs the authorized human but does not replace that person's decision.

## Requirement

A governed statement of necessary behavior, quality, interface, or constraint.

## Simulation

A model-based representation of behavior under declared assumptions. A simulation result is not automatically a physical, field, or real-world result.

## Stage gate

A human-controlled decision point between pipeline stages. A gate verifies that the required artifacts exist and that material unresolved decisions have not been hidden.

## Status classification

A controlled label such as implemented, mocked, simulated, deferred, failed, blocked, inconclusive, or not run.

## Traceability

The ability to connect intent to requirement, requirement to implementation, implementation to test, and test to evidence.

## Unknown

A material question for which the current artifact does not have a supported answer. Unknowns should be preserved rather than guessed away.

## Validation

An evaluation against declared criteria. Validation is always scoped; passing one validation does not establish universal correctness.

## v0.5 evidence-review terms

### Condition record

A short, non-identifying description of the interaction mode, platform, facilitation, and other context that may affect a field-trial result. Matching project keys do not make different condition records equivalent.

### Evidence-review packet

A human-readable synthesis that inventories declared outcomes, agreement, divergence, source observations, and limitations from multiple receipts. It does not replace the source receipts or authorize a decision.

### Field-trial receipt

A record of a voluntary, non-sensitive public-primer trial. It preserves declared conditions, observations, limitations, and a maintainer-decision status without authenticating that the trial occurred.

### Majority-truth claim

The invalid inference that the most common declared result in a small or incompatible evidence set becomes true merely because it appears more often.

### Project key

A stable, non-sensitive identifier used to state that field-trial receipts concern the same project. It does not establish equivalent versions, participants, environments, or conditions.

### Review bundle

A machine-readable manifest naming two or more validated field-trial receipts for one declared project, the human authority, review questions, known limits, and rules that prohibit scoring and automatic decisions.

### Synthesis

The organization of multiple source receipts into a reviewable packet. Synthesis may expose patterns and conflict; it does not create stronger evidence simply by combining files.
