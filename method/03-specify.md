# 3 — Specify

## Question

> What are we actually proposing, and what must be true for it to count as successful?

Stage 3 turns a rough idea into a versioned, reviewable controlling specification. It does not prove that the idea is correct or that the product exists.

## Minimum inputs

- the original idea in the contributor's own words;
- intended users and use context;
- known constraints and risks;
- the human decision-maker;
- any source material that may affect requirements.

## Required separations

Record statements using clear categories:

- **Fact:** supported by an identified source or direct observation;
- **Assumption:** temporarily accepted for planning;
- **Hypothesis:** testable explanation or prediction;
- **Proposal:** a suggested choice, design, or action;
- **Unknown:** material information not yet established.

Never silently upgrade one category into another.

## Public Stage 3 contract

A Stage 3 output should include:

1. title, version, status, owner, and date;
2. original input preserved without rewriting its intent;
3. problem and purpose;
4. scope and explicit non-scope;
5. users, stakeholders, and human authority;
6. facts, assumptions, hypotheses, proposals, and unknowns;
7. functional and non-functional requirements;
8. constraints, risks, and prohibited behavior;
9. candidate architecture at an appropriate level;
10. acceptance criteria that can actually be evaluated;
11. open questions and deferred decisions;
12. provenance and decision receipts;
13. a handoff describing what Stage 6 may build.

## Acceptance-criterion test

A useful criterion identifies:

- the thing being evaluated;
- the test or observation;
- the threshold or expected result;
- the environment and preconditions;
- the evidence that must be retained.

Weak: “The app should be fast.”

Stronger: “On the documented reference device, the local dashboard reaches an interactive state within 2 seconds for at least 18 of 20 cold-start trials; retain timestamps, device details, version, and failed-run logs.”

## Stage gate

Proceed to Stage 6 only when:

- the human authority accepts the candidate specification;
- material scope-changing decisions are resolved or explicitly deferred;
- acceptance criteria are testable;
- known risks and unknowns are visible;
- the Stage 6 handoff states what may and may not be built.

## Stage 3 does not claim

A complete specification does not establish feasibility, implementation, safety, effectiveness, legality, or truth. It establishes a controlled target for the next stage.