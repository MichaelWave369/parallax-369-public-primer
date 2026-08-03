# Security Policy

## Supported material

This repository contains public educational documentation, templates, synthetic examples, and a static website. It should not contain credentials, private datasets, internal prompts, private Parallax artifacts, or production infrastructure.

## Reporting a concern

Do not open a public issue containing:

- credentials, tokens, keys, or private endpoints;
- personal or client information;
- private prompts or internal Parallax material;
- exploit details that would increase immediate risk;
- links to exposed private artifacts.

Instead, contact the repository owner through a private GitHub channel available on the owner profile. Share only the minimum information needed to identify the affected path and risk.

## Publication-boundary incidents

A disclosure may be a security incident even when no software vulnerability exists. Examples include:

- accidental publication of private project material;
- internal orchestration or prompt leakage;
- release of identifying conversation content;
- exposure of deployment configuration or local paths;
- licensing or provenance uncertainty that makes distribution unsafe.

`PUBLIC_RELEASE_BOUNDARY.md` controls the response.

## Maintainer response

Maintainers should:

1. acknowledge and privately assess the report;
2. stop further publication where necessary;
3. rotate exposed secrets immediately;
4. remove affected content from branches, releases, and Pages deployments;
5. assess history, caches, forks, and artifacts;
6. publish a scoped, non-sensitive correction receipt when appropriate.

## Safe contribution rule

Never use real secrets as examples. Use obvious placeholders such as `EXAMPLE_TOKEN_NOT_REAL`. Never submit content copied from a private Parallax repository.