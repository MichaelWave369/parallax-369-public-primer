# Public Evidence Review Protocol

Version 0.5 adds a local-first way to review multiple public field-trial receipts for the **same project**. The purpose is to help a human maintainer inspect patterns, contradictions, conditions, failures, and limitations without turning a small evidence set into a score or automated decision.

## Core rule

> A review packet may organize evidence. It may not increase the evidence, authenticate it, erase disagreement, or inherit release authority.

## Appropriate use

Use this protocol when:

- two or more field-trial receipts describe the same public or non-sensitive project;
- every receipt has passed the public structural validator;
- source files can remain local;
- a named human authority will review the packet;
- the goal is clarification, not certification.

Do not use it to combine unrelated projects, private records, regulated data, personal conversations, or evidence that cannot safely enter the public workflow.

## Required review sequence

### 1. Confirm source scope

Before synthesis, confirm:

- every receipt names the same `project_key`;
- each referenced file exists and remains unchanged during the review;
- all trials are explicitly synthetic, public, or non-sensitive local work;
- free-text observations have been reviewed for identifying material;
- the selected receipts answer a shared review question.

A shared project key does not prove that trial conditions are comparable.

### 2. Preserve each trial independently

The review packet must retain, per receipt:

- trial ID;
- completion status;
- time band;
- assistance level;
- stage-separation, human-authority, and validator-boundary understanding;
- declared conditions;
- every observation;
- every evidence limitation;
- the source maintainer-decision status.

Never replace the source receipts with the synthesis packet.

### 3. Separate agreement from divergence

The local generator may identify fields where all receipts use the same declared value and fields where values differ. A difference is not automatically an error, and agreement is not proof of truth.

Possible causes of divergence include:

- different environments or input methods;
- different facilitation;
- different participant roles;
- changed documentation or candidate versions;
- observation error;
- genuine variation;
- insufficient evidence.

### 4. Refuse false arithmetic

The public review process does not produce:

- a Parallax score;
- a usability percentage;
- a confidence score;
- a winner or ranking;
- a majority-vote truth claim;
- an automated release recommendation;
- an automated roadmap decision.

Counts may be shown only as an inventory of declared outcomes. They do not make incompatible trials statistically comparable.

### 5. Record human interpretation separately

After reading the packet and source receipts, the human authority may record:

- what appears consistent;
- what remains contested;
- which conditions limit comparison;
- what change is proposed, if any;
- what additional evidence is needed;
- dissent or alternative interpretations;
- the decision and its scope.

The generator leaves this section pending.

## Local workflow

Validate all public artifacts:

```bash
python scripts/run_public_checks.py
```

Validate review bundles only:

```bash
python scripts/validate_review_bundles.py
```

Generate one review packet:

```bash
python scripts/generate_review_packet.py \
  examples/review-bundles/pocket-beacon-review.json \
  --output /tmp/pocket-beacon-review.md
```

No command uploads receipts, sends telemetry, merges changes, publishes a site, or approves a decision.

## Review-bundle status

Use one of these statuses:

- `Draft` — bundle composition is still changing;
- `Human review pending` — structural checks may have passed, but interpretation is not complete;
- `Reviewed in scope` — a named human has reviewed the packet within documented limits;
- `Superseded` — a later bundle or decision replaces the packet while preserving it for provenance.

## Evidence boundary

A structurally valid bundle does not establish that:

- any field trial occurred;
- consent was valid;
- observations are accurate;
- participants were representative;
- conditions were comparable;
- a project is usable, accessible, safe, legal, complete, or production-ready;
- a release or roadmap change is authorized.

## Privacy boundary

The generator copies source observations and evidence limits into the output. It is not a redaction or sanitization system. Human review must remove identifying, confidential, or sensitive content before a receipt or packet is committed or shared.

## Human authority

Automation may validate structure, reject incompatible bundles, and generate a draft packet. A named human remains responsible for interpretation, risk, change acceptance, publication, and release.