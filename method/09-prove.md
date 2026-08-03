# 9 — Prove

## Question

> What demonstrably works, under which conditions, and what still fails or remains unknown?

Stage 9 evaluates a specific candidate against the acceptance criteria in a specific controlling specification. It produces scoped evidence and a human release recommendation.

## Inputs

- the accepted controlling specification and acceptance criteria;
- the identified implementation candidate;
- the Stage 9 evidence handoff;
- test environment, tools, data, and risk controls;
- the human authority for release decisions.

## Public Stage 9 contract

A Stage 9 report should include:

1. specification and candidate identifiers;
2. tester, date, environment, and preconditions;
3. test plan mapped to acceptance criteria;
4. raw observations and retained evidence locations;
5. pass, fail, blocked, inconclusive, and not-run results;
6. negative findings and unexpected behavior;
7. reproduction instructions and reproducibility limits;
8. evidence quality and source limitations;
9. claims supported within scope;
10. claims not supported;
11. residual risks, unknowns, and deferred work;
12. dissent or reviewer disagreement;
13. a human release decision and rationale.

## Result vocabulary

- **Pass:** the stated criterion was satisfied under documented conditions.
- **Fail:** the stated criterion was not satisfied.
- **Blocked:** the test could not run because a prerequisite was unavailable.
- **Inconclusive:** the observations do not support a reliable determination.
- **Not run:** the test was intentionally or accidentally omitted.

Only **Pass** supports the criterion, and only within the documented scope.

## Evidence quality

Record enough context to understand and reproduce the observation:

- versions and commit identifiers;
- hardware, operating system, browser, network, or laboratory conditions;
- configuration and test data;
- timestamps and trial counts;
- logs, screenshots, measurements, or generated receipts;
- anomalies and excluded runs;
- who performed or witnessed the test.

## Claim ladder

Keep conclusions proportional:

1. **Observed:** what happened in one recorded event;
2. **Repeated:** what happened across documented repetitions;
3. **Verified in scope:** what satisfied a criterion within stated limits;
4. **Generalized hypothesis:** a broader proposition requiring additional evidence.

Do not jump from an observation to a universal claim.

## Failure is evidence

A failed criterion is a valid and useful result. Preserve it. Do not delete, redefine, or weaken the criterion after seeing the outcome without a new Stage 3 decision receipt.

## Release recommendations

A Stage 9 reviewer may recommend:

- release within explicit limits;
- conditional release with required mitigations;
- another Stage 6 iteration;
- return to Stage 3 because the target changed;
- no release because risk or evidence is unacceptable.

The reviewer recommends. The authorized human decides.

## Stage 9 does not claim

Passing tests do not establish universal safety, scientific truth, legal compliance, market fitness, or performance outside the documented conditions. Evidence supports only the claims it actually tests.