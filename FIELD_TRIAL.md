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
6. **Human authority** — a maintainer reviews the receipt and decides whether it supports a change.

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
- participant-reported confidence: low / medium / high;
- barriers and unexpected behavior.

Do not convert these categories into scientific measurements without an appropriate study design.

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
- evidence limitations;
- accepted, declined, deferred, or needs-evidence proposals;
- dissent;
- the authorized roadmap or release decision.

The existence of a field trial does not authorize publication or certification.