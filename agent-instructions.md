# Agent Instructions

This repository is the authoritative public documentation site for the RCPCH Digital Growth Charts platform. It contains integration, clinical, safety, regulatory, legal, and contributor documentation, but it does not implement the clinical calculation engine or API service.

This file is the entry point for AI coding agents. Read it before changing anything.

## Read First

- [README.md](README.md) - project purpose and local setup.
- [spec/README.md](spec/README.md) - specification authority and reading order.
- [spec/roadmap.md](spec/roadmap.md) - current improvements and deferred work.
- [docs/safety/overview.md](docs/safety/overview.md) - clinical safety overview.
- [docs/safety/qms.md](docs/safety/qms.md) - quality-management controls.
- [RCPCH house style](https://github.com/rcpch/rcpch-house-style) - organisation-wide engineering standards.

## Core Invariants

- Treat `docs/safety/`, medical-device records, investigations, legal documents, and QMS configuration as controlled material. Preserve evidence and obtain the CODEOWNER review required by `.github/CODEOWNERS`.
- Do not introduce or disclose real patient data, credentials, vulnerability details, or private working material.
- Do not hand-edit generated `site/` output or the generated safety PDF. Edit the Markdown or exporter source and rebuild it.
- Keep implementer guidance consistent with the API and calculation-engine repositories. Do not invent clinical behaviour, package versions, regulatory conclusions, or provenance values.
- Use a descriptive branch and a pull request into `live`. Do not push directly to `live` or bypass its protection unless the repository owner explicitly authorises an exceptional release action.

## Workflow

- `./s/docs` - build and serve the site through Docker Compose, then open it locally.
- `./s/lint` - lint Markdown.
- `./s/spellcheck` - check spelling.
- `./s/check-docs-nav` - detect missing navigation entries and stale exceptions.
- `./s/linkcheck` - run a clean strict Zensical build.
- `./s/build-pdf` - generate the safety documentation PDF.
- `./s/audit` - resolve and audit the declared Python dependencies for known vulnerabilities.

## Before Every Commit

```sh
./s/lint
./s/spellcheck
./s/check-docs-nav
./s/linkcheck
./s/build-pdf
./s/audit
git diff --check
```

Review the resulting diff as well as the command results. Clinical or regulatory correctness requires independent review against authoritative evidence; successful automation is not sufficient assurance.

## Approval Required

Ask before publishing a release, deploying or pushing directly to `live`, changing secrets or repository settings, modifying branch protection, deleting branches or published records, rewriting history, or changing clinical safety and regulatory conclusions.
