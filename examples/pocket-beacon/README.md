# Synthetic Example — Pocket Beacon

> This example was invented specifically for the public primer. It is not based on a private Parallax project, conversation, client, or internal artifact.

## Original idea

“Create a tiny browser page that lets a workshop coordinator display one of three local status messages—Open, Quiet Work, or Closed—even if the internet connection drops.”

The example intentionally stays small so the stage boundaries are easy to inspect.

---

# 3 — Specify

## Document control

- **Specification:** PB-SPEC-001
- **Version:** 0.1
- **Status:** Accepted candidate for implementation
- **Human authority:** Fictional workshop coordinator

## Scope

### In scope

- one static browser page;
- three selectable status states;
- current state stored in the browser;
- readable on a 360-pixel-wide display;
- no network required after the files are loaded.

### Out of scope

- synchronization between devices;
- authentication;
- remote control;
- emergency notification;
- accessibility certification;
- claims about all browsers or hardware.

## Statement ledger

| ID | Category | Statement |
|---|---|---|
| F-01 | Fact | A static HTML file can be opened locally in the selected test browser. |
| A-01 | Assumption | The coordinator uses one dedicated device. |
| H-01 | Hypothesis | Browser local storage will retain the selected state after restart. |
| P-01 | Proposal | Use three large buttons and a single status panel. |
| U-01 | Unknown | Whether older browsers used by downstream users will behave identically. |

## Requirements

| ID | Requirement | Acceptance criterion |
|---|---|---|
| R-01 | Show Open, Quiet Work, and Closed controls | AC-01: all three controls are visible and selectable at 360 px width |
| R-02 | Display the selected state | AC-02: selecting each control updates the panel correctly in 9 of 9 scripted selections |
| R-03 | Retain the state locally | AC-03: selected state remains after 10 browser restarts |
| R-04 | Operate without a network | AC-04: all scripted interactions pass with network interfaces disabled |

## Stage 6 handoff

Build a static HTML, CSS, and JavaScript candidate. No framework, server, account, analytics, or remote dependency is authorized. Local storage is allowed. No accessibility or emergency-use claim is authorized.

---

# 6 — Build

## Candidate

- **Version:** PB-CAND-0.1
- **Specification:** PB-SPEC-001 v0.1
- **Environment:** one fictional reference laptop and one current desktop browser

## Traceability

| Requirement | Component | Status | Stage 9 test |
|---|---|---|---|
| R-01 | HTML controls and responsive CSS | Implemented | PG-01 |
| R-02 | JavaScript state handler | Implemented | PG-02 |
| R-03 | Browser local storage adapter | Implemented | PG-03 |
| R-04 | Static local files | Implemented | PG-04 |

## Known limitations

- Only one browser and one device profile are in the planned evidence scope.
- Local-storage clearing resets the state.
- There is no synchronization or user identity.
- The interface has not received an independent accessibility review.
- “Offline” means the tested local interaction works with network interfaces disabled; it does not mean every browser or device is supported.

## Stage 9 handoff

Test the four acceptance criteria on the identified candidate without changing the specification after observing results. Retain a test log, browser version, viewport size, restart count, and any failures.

---

# 9 — Prove

## Environment

- **Candidate:** PB-CAND-0.1
- **Browser:** fictional reference browser 100.0
- **Viewport:** 360 × 800
- **Network:** Wi-Fi and wired adapters disabled for PG-04
- **Trials:** as specified below

## Results

| Test | Criterion | Result | Evidence summary |
|---|---|---|---|
| PG-01 | AC-01 | Pass | Three controls remained visible and selectable at the documented viewport. |
| PG-02 | AC-02 | Pass | All 9 scripted selections produced the expected status. |
| PG-03 | AC-03 | Fail | State persisted after 8 restarts but reset after restart 9 because the test profile cleared site data. |
| PG-04 | AC-04 | Pass | Scripted interactions passed with network interfaces disabled. |

## Supported claims

- The candidate displayed and changed all three states in the documented browser and viewport.
- The candidate completed the scripted interaction while network interfaces were disabled.

## Unsupported claims

- Reliable state retention across all restart or browser-cleanup conditions.
- Compatibility with other browsers, devices, or kiosk systems.
- Accessibility compliance.
- Suitability for emergency or safety-critical communication.

## Recommendation

**Return to Stage 6.** The local-retention requirement failed. The implementation team should define and test behavior when browser data is cleared. If the project owner wants the requirement changed instead, that decision must return to Stage 3 rather than weakening AC-03 inside the report.

## What this example demonstrates

The candidate is useful and mostly functional, but it is not allowed to call itself fully compliant. The failure remains visible, the claim stays scoped, and the next step is governed.