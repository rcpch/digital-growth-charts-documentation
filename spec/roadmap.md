# 2026 Documentation Review Roadmap

The bulk of the 2026 documentation review is complete and is captured in [PR #161](https://github.com/rcpch/digital-growth-charts-documentation/pull/161). What remains is grouped below: work that is blocked on an upstream dependency, improvements deferred to a future cycle, and findings from the latest house-style audit.

Legend: [x] done, [~] in progress or partially done, [ ] not started

## Completed

- [x] **DOC-1 - Add page-level tags.** Apply tags via frontmatter across the docs for an extra layer of search discoverability (the first half of [issue #73](https://github.com/rcpch/digital-growth-charts-documentation/issues/73)). Zensical now renders tags at the foot of each page and indexes them for search; the controlled vocabulary is documented in `docs/developer/writing-documentation.md`.

## Blocked Upstream

- [ ] **DOC-2 - Add a tags index page.** Aggregate all tags into a browsable `tags.md` (the second half of [issue #73](https://github.com/rcpch/digital-growth-charts-documentation/issues/73)) once Zensical supports tag listings ([Zensical backlog #38](https://github.com/zensical/backlog/issues/38)).

## Future Improvements

### Safety And Compliance

- [ ] **DOC-3 - Review EU MDR documentation.** Review `docs/safety/medical-device-reg/mdr-technical-docs.md` against current EU MDR requirements.
- [ ] **DOC-4 - Review the Clinical Safety Management File.** Address outstanding hazard issues [#48](https://github.com/rcpch/digital-growth-charts-documentation/issues/48), [#49](https://github.com/rcpch/digital-growth-charts-documentation/issues/49), [#50](https://github.com/rcpch/digital-growth-charts-documentation/issues/50), [#51](https://github.com/rcpch/digital-growth-charts-documentation/issues/51), and [#88](https://github.com/rcpch/digital-growth-charts-documentation/issues/88), plus missing-section issue [#116](https://github.com/rcpch/digital-growth-charts-documentation/issues/116).
- [ ] **DOC-5 - Review GDS Open API compliance.** Complete [issue #61](https://github.com/rcpch/digital-growth-charts-documentation/issues/61).
- [ ] **DOC-6 - Complete WCAG AA review.** Complete [issue #62](https://github.com/rcpch/digital-growth-charts-documentation/issues/62).
- [ ] **DOC-7 - Publish an accessibility statement.** Complete [issue #63](https://github.com/rcpch/digital-growth-charts-documentation/issues/63).
- [ ] **DOC-8 - Document the benefits case.** Complete [issue #64](https://github.com/rcpch/digital-growth-charts-documentation/issues/64).
- [ ] **DOC-9 - Add a DPIA section.** Complete [issue #113](https://github.com/rcpch/digital-growth-charts-documentation/issues/113).

### New Or Expanded Content

- [ ] **DOC-10 - Add FHIR and openEHR implementation guidance.** Complete [issue #117](https://github.com/rcpch/digital-growth-charts-documentation/issues/117). The SNOMED CT guidance shipped in the 2026 review; FHIR and openEHR are larger and remain deferred.
- [ ] **DOC-11 - Add an information-security flowchart.** Complete [issue #129](https://github.com/rcpch/digital-growth-charts-documentation/issues/129).
- [ ] **DOC-12 - Add a high-level platform flowchart.** Complete [issue #130](https://github.com/rcpch/digital-growth-charts-documentation/issues/130).

### Site And UI

- [ ] **DOC-13 - Refine the home-page hero.** Review content width, reduce text size, consider additional RCPCH colours, and make the hero dismissible.

## House-Style Audit

Audit date: 2026-09-01

Audited against the adopted `house-style` standards, especially agent guidance, security, licensing, scripts, repository presentation, Zensical documentation, specifications, CI, dependencies, and clinical safety. The audit included read-only inspection of GitHub repository metadata, `live` branch protection, and environments.

This repository already has strong foundations: external Actions are pinned to full SHAs, checkout credentials are disabled, Zizmor runs in CI, Dependabot uses cooldowns and grouping, unsupported MkDocs plugins are suspended, useful documentation checks exist under `s/`, and the extensive clinical-safety/QMS content is version-controlled and code-owned. The tasks below address gaps between those documented controls and what is currently enforced.

### P1 - Safety, Supply Chain, Release, And CI

- [ ] **HS-1 - Make `live` protection and releases match the QMS.** `docs/safety/qms.md:68-83` says changes are reviewed and CI-gated, but the GitHub settings inspected on 2026-09-01 had no required status checks, code-owner review, stale-review dismissal, latest-push approval, or conversation-resolution requirement, and administrators could bypass protection. Configure the intended clinical-repository controls, document emergency bypass, update stale `spec/qms.md:439-450` branch/path claims, and change `s/version++:51-114` to enter the reviewed PR path while retaining CI-owned tagging.
- [ ] **HS-2 - Make Docker and dependency builds private and reproducible.** `Dockerfile:30-32` copies the whole repository without a `.dockerignore`; `requirements.txt:4,40,43,49-50`, `Dockerfile:2,21-22`, and the CI install steps resolve mutable dependencies. Add a strict `.dockerignore`, pin the Python base and direct dependencies, adopt a reviewed resolved lock or generated requirements with hashes where practical, add Docker Dependabot, and align `docs/safety/csmf/third-party-tools-safety-assmt.md` with the real control.
- [ ] **HS-3 - Isolate and protect deployment authority.** `.github/workflows/ALL-BRANCHES-ALL-PRs-build-and-deploy-to-azure.yml` combines repository-controlled build code, PR write access, preview deployment, production deployment, and one long-lived Azure token without an `environment:` or concurrency control. Separate read-only build, preview, and production jobs; add a protected production environment and deployment concurrency; investigate workload identity or document the token's scope, owner, and rotation; separate preview and production authority where supported.
- [ ] **HS-4 - Enforce documentation quality in PR CI.** Current workflows do not run `s/lint`, `s/spellcheck`, `s/linkcheck`, navigation completeness, dependency audit, or REUSE, and branch protection requires no checks. Add a read-only PR workflow for Markdown lint, spelling, strict Zensical build/link validation, named navigation exceptions, PDF generation, dependency auditing, Zizmor, and later REUSE; require its checks on `live` and keep deployment separate.
- [ ] **HS-5 - Resolve licensing and copyright conflicts.** `LICENSE` declares CC-BY-SA-4.0 content and MIT code owned by "The contributors"; several workflows declare AGPL-3.0-or-later; `docs/safety/csmf/license.md` names and links CC-BY-SA but reproduces CC-BY-NC-SA terms; site/legal text names RCPCH as owner. Obtain an owner/legal decision, align all licence and holder statements, correct the clinical-safety licence page, then add `REUSE.toml`, SPDX coverage, and blocking REUSE CI.

### P2 - Important Maintenance And Governance

- [ ] **HS-6 - Add root maintenance, security, and safety entry points.** Add `agent-instructions.md` with thin `AGENTS.md` and `CLAUDE.md` pointers, plus concise root `SECURITY.md` and `SAFETY.md` files linking to the detailed site content. Include purpose, read-first order, clinical invariants, exact checks, `live` workflow, protected paths, assurance, vulnerability reporting, ownership, and approval requirements. Add `.editorconfig`.
- [ ] **HS-7 - Refresh the medical-device applicability record.** `docs/safety/medical-device-reg/mhra.md:9-17` records a determination from 7 May 2021 but no next review, current guidance access dates, reassessment triggers, or consequent actions/owner. Review against current MHRA and NHS England guidance, record the required fields, and link it from the future root `SAFETY.md`.
- [ ] **HS-8 - Finish the Zensical migration.** Remove the stale Material badge and `spec/implementation.md` instruction, verify or remove Material-style `theme.features` and `palette` settings in `mkdocs.yml`, and update `docs/developer/writing-documentation.md` plus `.github/workflows/release.yml` to describe the actual Zensical and WeasyPrint workflow.
- [ ] **HS-9 - Establish specification and QMS authority.** Add `spec/README.md` with reading order, status, authority, and supersession; remove, supersede, or clearly label the stale 528-line `spec/qms.md` draft so it cannot compete with `docs/safety/qms.md`; keep this roadmap's stable IDs and remove obsolete process claims.
- [ ] **HS-10 - Reconcile hosting documentation and automation.** `spec/spec.md:66-70` and `docs/developer/writing-documentation.md:23-25` claim GitHub Pages publication/backup, but only Azure deployment is active and the sole `github-pages` environment is unprotected and unused. Either add and monitor an artifact-based Pages backup or remove the claim; document Azure as a deliberate exception and name its operational owner.

### P3 - Consistency And Presentation

- [ ] **HS-11 - Standardise scripts and local preview.** Most wrappers use `#!/bin/bash`, verbose mode, no `set -euo pipefail`, no repository-root entry, and no `exec`. Normalise them without changing behaviour, add canonical `s/docs` for Docker-based preview, retain `s/up` only if useful, bind preview to loopback, and avoid fixed-port collisions where practical.
- [ ] **HS-12 - Improve README and licence presentation.** Keep the concise purpose, live-site link, and quick start, but replace the stale Material badge and add brief status, audience/scope, contribution, clinical-safety, and licence sections. State CC-BY-SA-4.0 in the README and `mkdocs.yml` once `HS-5` settles the canonical licensing language.
- [~] **HS-13 - Complete disposable-agent and environment ignores.** `.private/`, `.playwright/`, and `.playwright-mcp/` are now ignored. Add `/playwright-report`, `/blob-report`, `/test-results`, suitable disposable `.claude/` state, and explicit `.env` protection while retaining source/configuration files that belong in Git.

### Deliberate Exceptions And Non-Applicable Standards

- `live` rather than `main`, Azure hosting, Docker-based local preview, Zensical classic variant, date-based documentation releases, and issue-based hazard records are reasonable project choices; document them as exceptions rather than replacing them automatically.
- Rust, Cargo, cargo-dist, Homebrew, crates.io, Tauri, and library-extraction standards do not apply.
- A package-level `s/test`, registry badges, installation instructions, or a duplicate implementation conformance suite are not required for this documentation repository.
- Per-hazard Markdown files are optional because the GitHub-Issue hazard-log process is deliberate and documented.
