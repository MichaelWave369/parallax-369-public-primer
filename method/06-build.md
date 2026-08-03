# 6 — Build

## Question

> What is the smallest honest candidate we can build against the accepted specification?

Stage 6 creates an implementation candidate. It preserves the Stage 3 target and records where reality differs from the plan.

## Inputs

- the accepted controlling specification;
- the Stage 6 handoff;
- approved constraints, dependencies, and risk controls;
- the human authority for implementation decisions.

## Preserve the target

Do not rewrite the controlling specification to make the implementation appear successful. Proposed changes should be recorded as deviations or returned to Stage 3 for a versioned decision.

## Public Stage 6 contract

A Stage 6 output should include:

1. candidate name, version, commit, and build date;
2. exact controlling-specification version;
3. supported environment and dependencies;
4. build, run, and cleanup commands;
5. requirement-to-implementation traceability;
6. component and interface summary;
7. configuration and data assumptions;
8. implemented, simulated, mocked, deferred, failed, and unknown status;
9. deviations from the specification;
10. known limitations and safety boundaries;
11. generated artifacts and checksums where practical;
12. tests performed during construction;
13. a Stage 9 evidence handoff.

## Honest status rules

- **Implemented:** the behavior exists in the candidate.
- **Simulated:** the behavior exists only in a controlled simulation.
- **Mocked:** a substitute stands in for a real dependency or component.
- **Deferred:** the requirement is intentionally postponed.
- **Failed:** an attempted implementation does not satisfy the requirement.
- **Unknown:** the team cannot yet determine the status.

A mock can be valuable. The problem is not mocking; the problem is labeling a mock as complete.

## Traceability example

| Requirement | Component | Status | Evidence target |
|---|---|---|---|
| R-01 Local operation | `local-server` | Implemented | PG-01 |
| R-02 Battery telemetry | `sensor-adapter` | Mocked | PG-02 must report limitation |
| R-03 Export receipts | `receipt-writer` | Implemented | PG-03 |

## Deviation rule

Every material deviation should record:

- the affected requirement;
- what changed;
- why it changed;
- who authorized it;
- impact on tests and claims;
- whether Stage 3 must be revised.

## Stage gate

Proceed to Stage 9 only when:

- the candidate can be reproduced or its reproducibility limit is explicit;
- traceability covers every in-scope requirement;
- mocks, simulations, failures, and deferrals are visible;
- testable artifacts and instructions are available;
- the human authority accepts the evidence handoff.

## Stage 6 does not claim

A built candidate is not proof that requirements are satisfied. Completion, polish, and successful startup are implementation facts, not acceptance evidence.