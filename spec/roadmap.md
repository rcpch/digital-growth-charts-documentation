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
- [~] **DOC-7 - Review and complete the accessibility statement.** An [accessibility statement](../docs/legal/accessibility-statement.md) is published; review it against the current service and complete [issue #63](https://github.com/rcpch/digital-growth-charts-documentation/issues/63).
- [ ] **DOC-8 - Document the benefits case.** Complete [issue #64](https://github.com/rcpch/digital-growth-charts-documentation/issues/64).
- [ ] **DOC-9 - Add a DPIA section.** Complete [issue #113](https://github.com/rcpch/digital-growth-charts-documentation/issues/113).

### New Or Expanded Content

- [ ] **DOC-10 - Add FHIR and openEHR implementation guidance.** Complete [issue #117](https://github.com/rcpch/digital-growth-charts-documentation/issues/117). The SNOMED CT guidance shipped in the 2026 review; FHIR and openEHR are larger and remain deferred.
- [ ] **DOC-11 - Add an information-security flowchart.** Complete [issue #129](https://github.com/rcpch/digital-growth-charts-documentation/issues/129).
- [ ] **DOC-12 - Add a high-level platform flowchart.** Complete [issue #130](https://github.com/rcpch/digital-growth-charts-documentation/issues/130).

### Site And UI

- [ ] **DOC-13 - Refine the home-page hero.** Review content width, reduce text size, consider additional RCPCH colours, and make the hero dismissible.

## House-Style Audit

Audit date: 2026-09-04

Audited against [`rcpch/rcpch-house-style`](https://github.com/rcpch/rcpch-house-style), especially agent guidance, security, licensing, scripts, Zensical documentation, specifications, CI, Docker, dependencies, and clinical safety. The audit included read-only inspection of GitHub repository metadata, `live` branch protection, environments, tracked-file references, and historical context for suspected redundant files.

This repository already has strong foundations: external Actions are pinned to full SHAs, checkout credentials are disabled, Zizmor runs in CI, Dependabot uses cooldowns and grouping, unsupported MkDocs plugins are suspended, useful documentation checks exist under `s/`, and the extensive clinical-safety/QMS content is version-controlled and code-owned. The tasks below address gaps between those documented controls and what is currently enforced.

### P1 - Safety, Supply Chain, Release, And CI

- [ ] **HS-1 - Make `live` protection and releases match the QMS.** `docs/safety/qms.md:68-83` says changes are reviewed and CI-gated, but the GitHub settings inspected on 2026-09-04 had no required status checks, code-owner review, stale-review dismissal, latest-push approval, or conversation-resolution requirement, and administrators could bypass protection. Configure the intended clinical-repository controls, document emergency bypass, update stale `spec/qms.md:439-450` branch/path claims, and change `s/version++:51-114` to enter the reviewed PR path while retaining CI-owned tagging.
- [~] **HS-2 - Make Docker and dependency builds private and reproducible.** A strict `.dockerignore` now excludes local/private material from the build context, direct Python tools are version-pinned, and Docker Dependabot is configured. Remaining work is to review and pin the Python base image more precisely, adopt a resolved requirements file with hashes where practical, control OS and pip resolution, and align `docs/safety/csmf/third-party-tools-safety-assmt.md` with the implemented controls.
- [ ] **HS-3 - Isolate and protect deployment authority.** `.github/workflows/deploy-docs.yml` combines repository-controlled build code, PR write access, preview deployment, production deployment, and one long-lived Azure token without an `environment:` or concurrency control. Repository-controlled code runs on the same runner before the deployment credential is used, and deployment does not depend on the separate quality workflow succeeding. Separate read-only build, preview, and production jobs; make deployment depend on the quality gate; add a protected production environment and deployment concurrency; investigate workload identity or document the token's scope, owner, and rotation; separate preview and production authority where supported.
- [~] **HS-4 - Enforce documentation quality in PR CI.** `.github/workflows/docs-quality.yml` now runs Markdown linting, spelling, navigation completeness, strict Zensical validation, PDF generation, and dependency auditing independently from deployment; Zizmor remains a separate check. Remaining work is to require these checks on `live` and add REUSE after `HS-5` resolves the repository's licence declarations.
- [ ] **HS-5 - Resolve licensing and copyright conflicts.** `LICENSE` declares CC-BY-SA-4.0 content and MIT code owned by "The contributors"; several workflows declare AGPL-3.0-or-later; `docs/safety/csmf/license.md` names and links CC-BY-SA but reproduces CC-BY-NC-SA terms; site/legal text names RCPCH as owner. Obtain an owner/legal decision, align all licence and holder statements, correct the clinical-safety licence page, then add `REUSE.toml`, SPDX coverage, and blocking REUSE CI.

### P2 - Important Maintenance And Governance

- [x] **HS-6 - Add root maintenance, security, and safety entry points.** `agent-instructions.md`, thin `AGENTS.md` and `CLAUDE.md` pointers, `SECURITY.md`, `SAFETY.md`, and `.editorconfig` provide the repository-level purpose, read-first order, clinical invariants, validation commands, workflow, ownership, vulnerability reporting, assurance, and approval requirements.
- [ ] **HS-7 - Refresh the medical-device applicability record.** `docs/safety/medical-device-reg/mhra.md:9-17` records a determination from 7 May 2021 but no next review, current guidance access dates, reassessment triggers, or consequent actions/owner. Review against current MHRA and NHS England guidance, record the required fields, and link it from the future root `SAFETY.md`.
- [~] **HS-8 - Finish the Zensical migration.** The stale Material badge, obsolete `spec/implementation.md`, ineffective plugin environment variables, and outdated contributor/release instructions have been removed. Verify the remaining Material-style `theme.features` and `palette` settings through rendered comparison before removing them.
- [~] **HS-9 - Establish specification and QMS authority.** `spec/README.md` now supplies reading order and identifies `docs/safety/qms.md` as the controlled quality manual. The stale 528-line `spec/qms.md` remains clearly identified as a non-authoritative draft pending quality-management review of its deletion or formal supersession.
- [x] **HS-10 - Reconcile hosting documentation and automation.** Contributor documentation and the site specification now describe the active Azure publication and pull-request preview workflow, with Azure recorded as a deliberate project exception rather than claiming a nonexistent GitHub Pages backup.

### P3 - Consistency And Presentation

- [x] **HS-11 - Standardise scripts and local preview.** Wrappers now use portable Bash, strict mode, repository-root entry, argument forwarding, and `exec` where appropriate. `s/docs` is the canonical Docker preview command, `s/up` remains the Compose alias, and the fixed development port binds only to loopback.
- [~] **HS-12 - Improve README and licence presentation.** The README now leads with purpose, status, audience, production site, preview, checks, contribution, clinical-safety, security, and the licences declared in `LICENSE`. Final copyright-holder and software-licence alignment remains part of `HS-5`.
- [x] **HS-13 - Complete disposable-agent and environment ignores.** `.gitignore` now covers disposable Claude/Playwright state, browser reports, test results, local environments, and secrets while retaining a separate `.private/` block for useful local-only material.

### Deliberate Exceptions And Non-Applicable Standards

- `live` rather than `main`, Azure hosting, Docker-based local preview, Zensical classic variant, date-based documentation releases, and issue-based hazard records are reasonable project choices; document them as exceptions rather than replacing them automatically.
- Rust, Cargo, cargo-dist, Homebrew, crates.io, Tauri, and library-extraction standards do not apply.
- A package-level `s/test`, registry badges, installation instructions, or a duplicate implementation conformance suite are not required for this documentation repository.
- Per-hazard Markdown files are optional because the GitHub-Issue hazard-log process is deliberate and documented.
