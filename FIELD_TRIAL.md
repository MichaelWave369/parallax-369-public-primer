# Public Field-Trial Protocol

This protocol helps maintainers gather real usability observations about the public primer without turning a small trial into a claim of comprehensive research.

## Scope

A field trial evaluates whether a participant can understand and use the **public artifacts** for a small, non-sensitive task.

It does not evaluate private Parallax systems and is not presented as formal human-subjects research, accessibility certification, professional validation, or proof that the method works for every person or domain.

## Trial principles

1. **Voluntary participation** — explain the task and allow the participant to stop at any time.
2. **Data minimization** — collect only what is needed to understand the workflow.
3. **No sensitive projects** — use fictional, public, or deliberately non-sensitive material.
4. **No hidden recording** — obtain explicit agreement before recording audio, video, screen activity, or identifiable quotes.
5. **No forced success** — preserve confusion, abandonment, failure, and disagreement.
6. **Visible conditions** — record enough context to prevent unlike trials from being presented as equivalent.
7. **Human authority** — a maintainer reviews the receipt and decides whether it supports a change.

## Recommended trial task

Ask the participant to:

1. read the one-page primer or quickstart;
2. create a project scaffold;
3. identify the purpose of Stage 3, Stage 6, and Stage 9;
4. complete one small section in each artifact;
5. run the local project validator;
6. explain what the validator does and does not prove;
7. identify one confusing or unnecessary part of the workflow.

## Suggested measures

Record approximate, non-identifying observations:

- completion status: completed / partial / abandoned / blocked;
- time band: under 15 minutes / 15–30 / 31–60 / over 60;
- help needed: none / quick clarification / repeated assistance / facilitator takeover;
- stage-separation understanding: clear / partly clear / unclear;
- authority-boundary understanding: clear / partly clear / unclear;
- validator-boundary understanding: clear / partly clear / unclear;
- barriers and unexpected behavior.

Do not convert these categories into scientific measurements without an appropriate study design.

## Condition notes for later review

Version 0.5 permits an optional `conditions` object in the JSON receipt. Record short, non-identifying descriptions of:

- interaction mode, such as keyboard only or keyboard and pointer;
- platform, such as desktop browser and local terminal;
- facilitation, such as no assistance or quick clarification available;
- other material notes needed to understand comparison limits.

Condition notes do not prove that trials are comparable. Their purpose is to make differences harder to hide.

## Project key for review bundles

Version 0.5 permits an optional `project_key` in a field-trial receipt. It is required when the receipt is included in an evidence-review bundle.

Use a stable, non-sensitive identifier such as `pocket-beacon`. Do not infer project identity from task prose, participant details, or filenames.

A shared project key is necessary for bundling but does not establish equivalent candidate versions, environments, participant roles, or test conditions.

## Observation discipline

Separate:

- **Observation:** what the participant did or said;
- **Interpretation:** what the observer thinks it means;
- **Proposal:** what might be changed;
- **Decision:** what a human maintainer authorizes.

A single observation can motivate a candidate change. It does not prove that every user has the same need.

## Machine-readable receipt

A JSON field-trial receipt may be validated with:

```text
python scripts/validate_field_trials.py path/to/field-trial.json
```

The validator checks declared structure and allowed status values. It does not verify that the trial occurred, that observations are accurate, or that consent was valid.

The schema accepts receipt versions `0.4` and `0.5`. Existing v0.4 receipts remain valid, but they need an explicit `project_key` before they can enter a v0.5 review bundle.

## Reviewing multiple receipts

When two or more receipts describe the same project, follow [EVIDENCE_REVIEW.md](EVIDENCE_REVIEW.md). The review process preserves each source, surfaces agreement and divergence, and refuses scoring or automatic decisions.

Do not combine unrelated project receipts merely because they use the same public primer.

## Public submission boundary

Before opening an issue, remove:

- participant names, email addresses, handles, precise ages, or contact details;
- client, employer, project, or account identifiers;
- recordings or quotes without explicit publication permission;
- credentials, private URLs, local machine paths, and private repository references;
- private Parallax prompts, skills, orchestration, canon, or project records.

When public disclosure is not appropriate, retain the receipt locally and submit only a safely generalized observation.

## Trial decision receipt

After reviewing one or more trials, maintainers should record:

- which receipts were considered;
- repeated and conflicting observations;
- material condition differences;
- evidence limitations;
- accepted, declined, deferred, or needs-evidence proposals;
- dissent;
- the authorized roadmap or release decision.

The existence of a field trial or review packet does not authorize publication or certification.
