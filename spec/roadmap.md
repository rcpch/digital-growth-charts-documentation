# Documentation Roadmap

This roadmap records only outstanding or partially completed work. Completed work is preserved in Git history and the linked issues and pull requests rather than retained as a growing checklist here.

Last reviewed: 2026-09-24

Legend: [~] in progress or partially complete, [ ] not started

## P1 - Controlled Change And Deployment

- [~] **HS-1 - Enforce the QMS on `live` and releases.** Require the existing documentation-quality and workflow-security checks, require CODEOWNER review for controlled paths, dismiss stale approvals, require approval after the latest push and resolve conversations before merge. Apply equivalent controls to administrators through enforcement or a narrowly controlled and audited emergency bypass. Correct stale branch and path claims in `spec/qms.md`, route `s/version++` through a reviewed release pull request, and decide whether manual `v*` tag pushes remain an authorised emergency release path.
- [ ] **HS-3 - Separate and protect Azure deployment authority.** Split the read-only build from credentialed preview and production deployment, pass a built artifact between jobs, make production depend on successful quality and security checks, use protected GitHub environments, and add deployment concurrency. Give preview deployment separate authority where Azure supports it. Prefer workload identity; otherwise document the deployment token's owner, scope, rotation and incident-response procedure, and remove any confirmed obsolete token.
- [ ] **HS-5 - Resolve licensing and add REUSE enforcement.** Obtain the copyright-holder and licence decisions, align repository and documentation declarations, correct the inconsistent clinical-safety licence page, preserve third-party notices, add `REUSE.toml` and SPDX coverage, and make `reuse lint` a blocking CI check.
- [~] **HS-4 - Finish the pull-request quality gate.** The documentation-quality and Zizmor workflows pass but are not required by branch protection. Require both checks now, then require the REUSE check delivered by HS-5.

## P2 - Safety, Compliance And Reproducibility

- [~] **DOC-4 - Reconcile actionable Clinical Safety Management File records.** Update hazard [#49](https://github.com/rcpch/digital-growth-charts-documentation/issues/49) so its cause analysis covers reference-selection and presentation failures as well as arithmetic; complete triage and governance for hazard [#173](https://github.com/rcpch/digital-growth-charts-documentation/issues/173); and apply the agreed deprecated-hazard lifecycle to [#178](https://github.com/rcpch/digital-growth-charts-documentation/issues/178). Accepted open hazards are retained safety records and are not incomplete merely because they remain open.
- [~] **HS-2 - Make builds reproducible and least-privileged.** Pin the Python base image immutably, lock and hash resolved Python dependencies, control pip and operating-system package resolution, run the container as a non-root user, and align the supplier-control record with the implemented controls.
- [~] **HS-7 - Refresh medical-device applicability.** Update `docs/safety/medical-device-reg/mhra.md` with dated current guidance, decision-maker role, next review, actions and owner, and reassessment triggers.
- [ ] **DOC-5 - Evidence GDS Open API compliance.** Review the service against current guidance and replace the unsupported assertion in `docs/safety/dtac.md` with a linked review record, resolving [issue #61](https://github.com/rcpch/digital-growth-charts-documentation/issues/61).
- [ ] **DOC-6 - Complete and evidence the WCAG review.** Audit the current site, record tested scope, results and remediation, resolve [issue #62](https://github.com/rcpch/digital-growth-charts-documentation/issues/62), and update the accessibility statement to remove or substantiate claims about external evaluation, testing with disabled users and regular automated scanning.
- [~] **DOC-9 - Publish the DPIA applicability decision.** Promote the existing DTAC determination and DPO consultation into a findable controlled section, then resolve [issue #113](https://github.com/rcpch/digital-growth-charts-documentation/issues/113).

## P3 - Site And Content

- [~] **HS-8 - Complete the Zensical compatibility review.** Compare rendered output with and without the remaining Material-style `theme.features` and `palette` settings, then remove or document each setting.
- [~] **HS-9 - Retire or formally supersede `spec/qms.md`.** The controlled quality manual is `docs/safety/qms.md`; the older draft still contains stale branch and path controls and requires quality-management review before deletion or formal archival.
- [ ] **DOC-8 - Publish the benefits case.** Define the intended audience and evidence, then complete [issue #64](https://github.com/rcpch/digital-growth-charts-documentation/issues/64).
- [ ] **DOC-11 - Publish the information-security flowchart.** Review the existing draft, publish an accessible maintained version, and complete [issue #129](https://github.com/rcpch/digital-growth-charts-documentation/issues/129).
- [ ] **DOC-14 - Restore metadata on investigation reports.** Add reviewed frontmatter and controlled-vocabulary tags to the pooled-term and Trisomy 21 investigation reports added after the page-tagging review.

## Deliberate Exceptions And Deferred Work

- EU MDR review is demand-triggered because EU-market deployment is currently out of scope. Reopen it before any EU deployment or conformity claim.
- FHIR and openEHR guidance is demand-triggered under the closure decision for [issue #117](https://github.com/rcpch/digital-growth-charts-documentation/issues/117); SNOMED CT guidance remains supported.
- Open hazard issues are retained safety records rather than unfinished implementation tasks.
- `live` branch naming, Azure hosting, Docker-based local preview, the Zensical classic variant, date-based documentation releases, and issue-based hazard records are deliberate project choices.
- Migration away from the monitored Azure deploy action remains deferred under [issue #181](https://github.com/rcpch/digital-growth-charts-documentation/issues/181); HS-3 still applies to credential and deployment isolation with the current mechanism.
- Rust, Cargo, cargo-dist, Homebrew, crates.io, Tauri, library-extraction, package-installation guidance, and a duplicate implementation conformance suite do not apply to this repository.
