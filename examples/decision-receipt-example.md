# Synthetic Decision Receipt Example

This fictional receipt demonstrates how a material decision can remain reconstructable. It is an educational example, not evidence about a real product.

## Receipt identity

- **Receipt ID:** DR-PB-002
- **Project:** Pocket Beacon synthetic walkthrough
- **Stage:** 6 — Build
- **Status:** Superseded by test evidence
- **Decision authority:** Fictional project maintainer
- **Recorded:** 2026-08-02

## Decision question

How should the candidate retain the selected workshop status after a browser refresh?

## Controlling requirement

`REQ-04`: The most recently selected status must remain visible after the page is refreshed in the same browser.

## Options considered

### Option A — In-memory state only

**Advantages**

- smallest implementation;
- no storage API dependency;
- easy to inspect.

**Limitations**

- state is lost during refresh;
- does not satisfy `REQ-04`.

### Option B — Browser local storage

**Advantages**

- survives refresh in the same browser;
- remains local-first;
- requires no account or server.

**Limitations**

- storage may be unavailable or cleared;
- behavior must handle malformed or missing values;
- does not synchronize between devices.

### Option C — Server persistence

**Advantages**

- can synchronize across devices;
- permits centralized history.

**Limitations**

- exceeds the candidate's offline and no-account scope;
- introduces hosting, privacy, authentication, and network dependencies.

## Evidence available at decision time

- The controlling specification requires same-browser refresh retention.
- The public candidate is intentionally local-first and offline-capable.
- No multi-device synchronization requirement exists.
- No persistence test had yet been run.

## Assumptions

- A modern browser with local-storage support is available.
- Same-browser persistence is sufficient for the current scope.
- Stored values can be constrained to the three allowed status identifiers.

## Decision

Select **Option B — Browser local storage** for the candidate.

## Rationale

Option B is the smallest approach that could satisfy `REQ-04` without introducing server infrastructure or expanding the claim boundary.

## Consequences

- Add read, validate, write, and fallback behavior.
- Add an acceptance test covering refresh persistence.
- Document that private/incognito modes and browser storage policies may affect behavior.
- Do not claim cross-device persistence.

## Dissent and concerns

A reviewer noted that local storage is sometimes disabled or cleared and requested an explicit fallback to the default status. The concern was accepted and added to the test plan.

## Revisit conditions

Revisit this decision if:

- the scope adds multiple devices or users;
- storage of sensitive information is proposed;
- browser compatibility evidence shows unacceptable failure rates;
- offline operation is removed from the controlling specification.

## Later Stage 9 evidence

The first candidate failed the refresh-retention acceptance test because the implementation wrote the selected value but did not restore it during initialization.

## Receipt update

The decision itself remained valid, but the implementation was incomplete. The failure returned the candidate to Stage 6. This distinction matters:

> A reasonable decision does not prove that the decision was implemented correctly.
