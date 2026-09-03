# Five-Repository Upgrade Runbook Specification

Status: initial draft for iterative development

## Purpose

The Five-Repository Upgrade Runbook will define a safe, reproducible procedure for coordinating significant changes across the RCPCH Digital Growth Charts platform while minimising regressions, unintended contract changes, and broken user integrations.

The name describes the full platform boundary, not a requirement to change every repository in every upgrade. Each upgrade must explicitly identify its affected repository set and justify any repository excluded from implementation, testing, release, or documentation work.

This specification records what the runbook must eventually require. Commands, approver roles, evidence-retention locations, and automation details can be added as the cross-repository E2E harness and repository release processes mature.

## Goals

- Make the safest path the simplest path for maintainers.
- Make the exact baseline, candidate, and rollback combinations explicit and reproducible.
- Detect unintended API, package, UI, clinical, and integration changes before release.
- Scale from a one-repository dependency upgrade to a coordinated five-repository change without separate competing procedures.
- Separate automated evidence from human review and approval.
- Preserve an auditable record of what was requested, built, tested, observed, approved, released, deployed, and documented.
- Ensure users and integrators receive accurate compatibility and migration guidance.
- Make rollback a prepared and tested action rather than an improvised response to failure.

## Non-Goals

- The runbook does not replace each repository's normal contribution, test, security, release, or deployment instructions.
- The runbook does not define clinical calculation correctness independently of reviewed calculation-engine tests and source evidence.
- A green E2E run does not itself constitute clinical, safety, security, regulatory, or release approval.
- The runbook does not require an exhaustive Cartesian product of every historical version.
- The runbook must not encourage rewriting published history, deleting release evidence, or silently replacing immutable package artefacts.

## Platform Boundary

| Order | Repository | Primary responsibility | Typical distributed artefact |
|---|---|---|---|
| 1 | `rcpch/rcpchgrowth-python` | Clinical calculation engine and growth-reference implementations | Python package from PyPI |
| 2 | `rcpch/digital-growth-charts-server` | HTTP API, request/response contracts, authentication, validation, and engine integration | Container image and cloud deployment |
| 3 | `rcpch/digital-growth-charts-react-component-library` | Reusable chart rendering and its public React/TypeScript interface | npm package and supported CDN artefact |
| 4 | `rcpch/digital-growth-charts-react-client` | Public demonstration and integration client; home of the cross-repository E2E harness | Static web build and deployment |
| 5 | `rcpch/digital-growth-charts-documentation` | Integration guidance, compatibility policy, safety/QMS records, release evidence, and this runbook | Documentation site, GitHub release, and PDF artefacts |

The default dependency flow is from calculation engine to API server to Chart Component to Demo Client, with documentation following reviewed behaviour. Some changes cross different boundaries, and public consumers may use the Python package, API, or Chart Component directly without using downstream RCPCH applications. Excluding a downstream RCPCH repository therefore does not remove the need to assess its external users.

## Terminology

- **Upgrade**: a coordinated change record executed through this runbook, whether it modifies one repository or all five.
- **Upgrade record**: the durable human-readable record containing scope, decisions, evidence, approvals, releases, deployment results, and follow-up work.
- **Affected repository set**: repositories requiring a code, dependency, test, deployment, documentation, or assurance change for this upgrade.
- **Baseline stack**: the currently supported immutable version set against which the candidate is compared.
- **Candidate stack**: the immutable version set proposed for release or deployment.
- **Rollback stack**: a coherent immutable version set approved for restoration if promotion fails.
- **Stack manifest**: requested and resolved identities for all relevant layers, including package versions, commits, dirty state, image digests, artefact checksums, and deployment URLs.
- **Contract**: externally observable behaviour on which another layer or user may depend, including APIs, schemas, package exports, UI props, errors, clinical interpretation, generated artefacts, and documented behaviour.
- **Compatibility claim**: a reviewed statement that a named version combination is supported for specified capabilities and scenarios.
- **Gate**: an explicit hold point that cannot be passed until its required evidence and approvals are present.
- **Promotion**: moving an approved candidate artefact or deployment towards production use without rebuilding it.
- **Release evidence**: automated and reviewed records demonstrating what was tested and what actually ran.

## Governing Principles

- Start from immutable identities. Resolve mutable branches, tags, Docker tags, npm tags, CDN aliases, and deployment names to commits, versions, digests, or checksums before approval.
- Record requested and observed versions separately. Never claim that a selected dependency ran merely because it was requested or installed.
- Build once and promote the same artefact where repository tooling permits. Rebuilding between test and production weakens the evidence chain.
- Change one layer at a time during diagnosis. A coordinated candidate may contain several changes, but boundary tests should isolate which changed layer introduced a regression.
- Preserve source checkouts. Test orchestration must use isolated worktrees, package contexts, containers, and caches rather than editing dependency files or disturbing local work.
- Test public contracts, not only internal implementation. Include direct consumers of the Python package, API, and Chart Component in the impact assessment.
- Prefer semantic comparisons over formatting-sensitive snapshots unless formatting is itself a public contract.
- Treat warning, validation, authentication, and error responses as contracts alongside successful responses.
- Use only fictional, non-identifiable data in fixtures, logs, traces, screenshots, exports, and retained evidence.
- Keep confidential credentials out of committed configuration, browser bundles, logs, and evidence. Browser-injected demo keys are public constrained credentials, not secrets.
- Stop when evidence contradicts the plan. Do not reinterpret a failed gate as success by weakening assertions or silently accepting changed goldens.
- Record exceptions explicitly with owner, rationale, risk, expiry or review point, and compensating control.
- Prepare rollback before promotion and test the rollback combination where practical.

## Runbook At A Glance

| Gate | Question answered |
|---|---|
| 0. Initiate and classify | What is changing, who owns it, which repositories and users are affected, and who must review it? |
| 1. Capture the baseline | What exact stack works now, and which failures or limitations already exist? |
| 2. Define contracts | What may change, what must not change, and how will tests distinguish the two? |
| 3. Prepare candidates | Have applicable repositories produced identifiable candidates that pass their own checks? |
| 4. Verify together | Does the candidate work across selected boundaries with real API responses and browser interactions? |
| 5. Review and approve | Have the right humans reviewed the evidence, migration, exceptions, and rollback plan? |
| 6. Release and promote | Are the tested artefacts being promoted in a controlled order with hold points? |
| 7. Document and communicate | Do published instructions accurately describe the versions actually released and deployed? |
| 8. Observe and close | Has the upgrade been accepted or coherently rolled back, with follow-up work owned? |

For a smaller upgrade, keep all gates but mark non-applicable repository steps with a reason. The procedure becomes shorter by reducing the affected set and evidence proportionately, not by silently skipping the controls that show why the change is safe.

## Selecting The Upgrade Path

Every upgrade starts by selecting an affected repository set. The selection determines which repository-specific phases execute, but the scope, contract, evidence, approval, documentation, and closure gates always apply.

| Change shape | Usually affected | Required assessment beyond changed repositories |
|---|---|---|
| Documentation correction with no product claim change | Documentation | Confirm no code, contract, safety, or supported-version claim is altered |
| Python implementation or dependency change | Python; often API and documentation | Direct Python users, API pin/build, clinical vectors, provenance, numerical and error behaviour |
| API implementation, framework, authentication, or schema change | API and documentation; often client/component | OpenAPI diff, direct integrators, client requests, component response consumption, cloud deployment |
| Chart Component behaviour or public-interface change | Component and documentation; often Demo Client | npm/CDN users, React peer compatibility, real API responses, persisted data, accessibility, exports |
| Demo Client-only change | Demo Client; documentation when user guidance changes | Installed component/API combination, production build, browser workflows, public credential boundary |
| Cross-layer contract or clinical change | All affected upstream/downstream layers and documentation | Full boundary matrix, migration, persisted data, safety record, coordinated rollback |

SemVer alone must not determine the process depth. A patch dependency can alter clinical output or a transitive API schema, while a deliberate major release can preserve runtime compatibility through migration support.

## Required Upgrade Record

Before implementation begins, create an upgrade record containing at least:

- Stable upgrade identifier and title.
- Owner, technical reviewer, and any required clinical, safety, security, regulatory, accessibility, or documentation reviewers.
- Problem statement and intended outcome.
- Affected repository set, excluded repositories, and rationale for both.
- User groups and direct integration surfaces affected.
- Baseline stack manifest.
- Proposed candidate stack or unresolved candidate selectors.
- Known contracts and capabilities that may change.
- Explicit non-goals.
- Risk and safety-impact assessment, including linked hazards or a statement that no hazard is affected.
- Compatibility and migration policy.
- Required test matrices and acceptance criteria.
- Rollback stack and rollback triggers.
- Release and deployment order.
- Documentation and communication changes.
- Open decisions, assumptions, exceptions, and owners.
- Evidence links, approvals, actual released identities, monitoring results, and closure decision as work progresses.

The exact storage template remains open. A GitHub issue may coordinate work, but durable contract decisions and controlled evidence must remain findable after issue and CI artefact retention periods expire.

## End-To-End Procedure

### Gate 0 - Initiate And Classify

1. Create the upgrade record and appoint an owner.
2. Describe the user-visible or operational outcome without assuming an implementation.
3. Classify the change surfaces: clinical calculation, API/schema, authentication/security, component interface/rendering, client workflow, deployment/infrastructure, documentation, safety/QMS, or dependency/toolchain.
4. Select the affected repository set and identify direct consumers outside that set.
5. Decide whether the upgrade is routine, significant, clinically consequential, security-sensitive, or breaking. More than one classification may apply.
6. Link source issues, advisories, upstream release notes, hazards, incidents, and prior decisions.

Exit criteria: the scope, owner, affected repositories, impacted contracts, and required reviewers are explicit. Unknowns are recorded rather than silently assumed.

### Gate 1 - Capture The Baseline

1. Record exact supported production versions, commits, image digests, package checksums, deployment URLs, and documentation release.
2. Run the current fast test suites and the applicable E2E baseline against the current stack.
3. Preserve representative genuine API responses and browser evidence using fictional data.
4. Record known baseline failures, warnings, skips, capability gaps, and accepted risks so they are not misattributed to the candidate.
5. Confirm that the rollback stack is obtainable and that its deployment inputs have not expired or moved.

Exit criteria: the baseline is reproducible enough to compare against the candidate, and pre-existing failures are distinguished from regressions.

### Gate 2 - Define Contracts And Acceptance Criteria

1. Inventory contracts touched at each selected boundary.
2. Classify every expected difference as additive compatible, behavioural compatible, deprecated, breaking with migration, or intentionally unsupported.
3. Define semantic assertions for values and structures that must remain stable.
4. Define reviewed expected diffs for intended changes. Do not approve broad snapshot replacement without explaining each material difference.
5. Select practical matrices: current supported, one-layer boundary, coordinated candidate, persisted legacy data, adjacent supported versions, nominated cloud deployment, and coherent rollback as applicable.
6. Define stop conditions, acceptance thresholds, required screenshots/exports, and human review requirements.

Exit criteria: tests can distinguish an intended change from an accidental regression, and every breaking change has an explicit migration and communication plan.

### Gate 3 - Prepare Candidates In Dependency Order

Prepare only the applicable repository steps, normally moving from upstream dependencies to downstream consumers.

#### Calculation Engine

- Review upstream dependency and growth-reference changes against primary evidence.
- Run unit, property, golden, literature-vector, edge-boundary, and regression tests required by that repository.
- Compare representative successful values, validation failures, and metadata semantically against the baseline.
- Verify all affected growth references and measurement methods rather than one convenient example.
- Build an immutable candidate package and record version, commit, build environment, and checksum.
- Confirm package API changes and migration guidance for direct Python users.

#### API Server

- Install or pin the exact candidate engine into an isolated build without modifying the engine checkout.
- Verify from real responses that the observed engine identity matches the requested candidate.
- Diff the normalized OpenAPI document and classify every changed route, parameter, schema, required field, status code, error shape, server declaration, and security scheme.
- Exercise single calculations, successful and partially invalid bulk requests, fictional-child data, chart data, utilities, authentication, validation, and application errors as applicable.
- Build an immutable image and record its digest, server version, commit, configuration class, and dependency lock state.
- Deploy to an isolated candidate environment before changing a shared or production environment.

#### Chart Component

- Consume genuine baseline and candidate API responses without relabelling or recalculating them.
- Review public React props, exported TypeScript types, npm entry points, peer dependencies, DOM/accessibility behaviour, warnings, tooltips, results, and SVG exports.
- Test direct npm use and the supported CDN surface independently where both are published.
- Replay authentic persisted legacy responses where users may retain old API results.
- Run component tests at desktop and mobile widths and inspect designated screenshots for intended visual changes.
- Build immutable npm/CDN candidates and record package contents and checksums.

#### Demo Client

- Build against the exact candidate API and Chart Component, recording how each was injected.
- Verify that the built bundle contains the selected component rather than a cached or lockfile-selected alternative.
- Exercise real user workflows in a browser, including input, reference and measurement-method selection, centile/SDS transitions, results, errors, warnings, accessibility, responsiveness, and export where applicable.
- Detect page errors, unexpected console errors, failed network requests, missing assets, stale requests, and horizontal overflow.
- Treat all `VITE_*` values as public and keep confidential credentials out of the bundle.
- Produce an immutable candidate build or deployment identity.

#### Documentation

- Update API, Python, component, client, compatibility, migration, versioning, safety, and support guidance affected by the candidate.
- Ensure examples use the candidate contract and do not describe future behaviour as already deployed.
- Update linked hazard, QMS, regulatory, and release evidence where the impact assessment requires it.
- Build the site and PDFs, run linting, spelling, strict internal-link/anchor checks, and inspect changed presentation pages.
- Do not publish final compatibility claims until the coordinated candidate passes its gates and is approved.

Exit criteria: every selected repository has an immutable or explicitly dirty development candidate, passes its local required checks, and exposes enough identity to prove what downstream tests consume.

### Gate 4 - Run Boundary And Coordinated Verification

1. Run one-layer boundary comparisons where practical to isolate regressions.
2. Run the coordinated candidate through the Demo Client E2E harness using real HTTP responses and a real browser.
3. Compare requested, resolved, and observed stack identities and fail on unexplained drift.
4. Run the selected compatibility matrices without expanding to an uncontrolled Cartesian product.
5. Classify each result as pass, product failure, unsupported combination, capability-based skip, test failure, or infrastructure failure.
6. Preserve redacted evidence, checksums, traces, screenshots, logs, exports, and environment metadata.
7. Re-run the baseline when environmental or harness failures make comparison uncertain.

Exit criteria: all required scenarios pass or have an explicitly approved exception; no identity drift remains unexplained; evidence is sufficient to reproduce and review the run.

### Gate 5 - Review And Approve

1. Review all semantic diffs, OpenAPI diffs, package/API changes, UI evidence, accessibility results, security changes, safety impact, known exceptions, and evidence limitations.
2. Confirm that direct consumers and persisted-data scenarios are represented, not only the RCPCH Demo Client happy path.
3. Confirm version increments match the actual compatibility impact in each released repository.
4. Confirm migration guidance, deprecation periods, customer communication, monitoring, and support arrangements.
5. Confirm the rollback stack is coherent, available, and compatible with data or contracts introduced during promotion.
6. Record named approval, rejection, or a request for further work. Automation must not self-approve.

Exit criteria: every required reviewer has made a recorded decision and no unresolved blocker is hidden in a test skip, warning, or exception.

### Gate 6 - Release And Promote

1. Freeze the approved candidate manifest and verify repositories have not moved since testing.
2. Release and promote in the dependency order approved for the change. Published libraries may need to precede downstream builds; shared deployments may need a compatibility window before downstream promotion.
3. Use each repository's canonical release mechanism. Do not improvise tags, package replacement, or deployment commands in the runbook.
4. Verify each release from its public distribution surface before proceeding: package registry, container registry, CDN, deployed API, client deployment, or documentation release as applicable.
5. At each hold point, run the nominated smoke checks and compare observed identity to the frozen manifest.
6. Stop promotion and evaluate rollback when a trigger is met. Do not continue merely because later layers might mask an upstream fault.
7. Record actual release versions, commits, digests, URLs, timestamps, workflow runs, and deviations from the plan.

Exit criteria: the approved artefacts are released and promoted in the intended order, public surfaces report the intended identities, and no rollback trigger is active.

### Gate 7 - Publish Documentation And Communicate

1. Replace candidate language with exact released versions, support status, effective dates, and deployment state.
2. Publish compatibility tables, migration instructions, deprecations, known limitations, and rollback/support guidance.
3. Link the upgrade record, immutable evidence summary, releases, issues, contract decisions, and safety/QMS records.
4. Run the documentation checks and create the dated documentation release through the repository's canonical `s/version++` flow.
5. Verify the documentation tag, GitHub release, expected PDF artefacts, production deployment, links, and displayed version in a fresh browser context.
6. Communicate through the channels selected in the upgrade record, with extra notice for breaking changes or required consumer action.

Exit criteria: public guidance describes what is actually released and deployed, not merely what was planned, and users can find migration and support information.

### Gate 8 - Observe, Close, Or Roll Back

1. Monitor nominated technical, clinical, support, security, and usage signals for the defined observation period.
2. Re-run production-compatible smoke scenarios against the promoted stack.
3. Triage reports against the frozen manifest and retained evidence.
4. If rollback criteria are met, execute the coherent rollback plan, verify every restored layer, communicate status, and preserve the failed release evidence.
5. If accepted, close the upgrade record with actual outcome, residual risks, follow-up issues, superseded combinations, evidence retention location, and lessons for this runbook.

Exit criteria: the upgrade is explicitly accepted or rolled back; there is no ambiguous partially promoted state; follow-up work has owners.

## Contract Regression Controls

The runbook must require the following controls when the relevant surface is affected:

- Normalized OpenAPI comparison with human classification of every material difference.
- Semantic request/response fixtures for success, partial success, validation, authentication, application errors, and absent optional fields.
- Public Python import/signature and serialization checks.
- Public npm exports, TypeScript declarations, React props, peer-dependency, and CDN checks.
- Real browser workflows using accessible roles and names where practical.
- Persisted-response replay without recalculation or silent field rewriting.
- Accessibility and responsive checks for changed user workflows.
- Exported artefact inspection where SVG or PDF output is part of the user contract.
- Documentation example execution or validation where examples can drift from the API.

When growth-reference identity or provenance is affected, regression coverage must include all six canonical selectors and the established Turner naming distinction between API route/React prop `turner` and canonical provenance `turners-syndrome`. Existing legacy, unknown, matching, mixed, and confirmed-mismatch behaviour must be tested according to the current provenance contract rather than inferred from newly generated happy-path responses.

## Rollback Requirements

- Define rollback triggers before promotion, including clinical-value discrepancy, contract regression, elevated error rate, authentication failure, rendering failure, inaccessible critical workflow, or unverifiable version drift.
- Define a complete rollback stack, not independent per-repository versions that may never have been compatible together.
- Record whether rollback means deployment restoration, dependency repinning, a new corrective package release, feature disablement, traffic routing, or documentation correction.
- Never rely on overwriting an existing PyPI, npm, GitHub, or CDN release. Immutable publication normally requires a new corrective version.
- Account for forward-only data, cache, contract, or deployment changes that make rollback unsafe.
- Preserve withdrawn or superseded release records and explain their status rather than deleting the audit trail.
- Verify rollback with the same identity, smoke, and critical-contract checks used during promotion.
- Keep user communication ready for upgrades where rollback may affect integrators or persisted responses.

## Known Cross-Repository Edge Cases

- Requested versions can differ from observed versions because of lockfiles, Docker cache, mutable tags, dependency resolution, CDN aliases, or stale deployments.
- A dirty local checkout can report a package version that does not uniquely identify its code. Development evidence must include dirty state and a diff checksum and must not be represented as release-reproducible.
- A cloud API is immutable from the harness's perspective. Its calculation engine cannot be swapped by selecting a different Python version.
- Older APIs may lack provenance, deployment identity, OpenAPI `servers`, or authentication metadata. Record capability absence without fabricating data, and keep explicit URL/authentication overrides for legacy testing.
- Users may persist authentic API responses indefinitely. A new component must be tested against legacy responses, not only responses regenerated by the candidate API.
- Bulk endpoints may combine successful items and inline errors, so schema comparison must not assume one uniform item shape.
- A passing API smoke test does not prove that the selected component was embedded in the selected client or that browser interactions work.
- A passing current-stack test does not establish compatibility at each upgrade boundary.
- CI evidence links can expire. Controlled release records need durable summaries and checksums.
- Network traces, logs, screenshots, and exports can leak credentials or patient data unless redacted before persistence.
- A GitHub release, package publication, cloud deployment, PDF build, and browser-displayed version can diverge even when initiated by one release process. Verify each public surface independently.
- Browser session caches can display stale dynamic release information while the deployed static site is current. Use a fresh browser context and inspect the authoritative release source.
- Rolling back only the deployment does not remove an already published package or documentation release. Mark superseded artefacts accurately.
- Documentation can accidentally describe a candidate as production or preserve obsolete integration advice after rollback. Effective status and version applicability must be explicit.

## Minimum Outputs

Each completed upgrade should leave:

- The final upgrade record.
- Baseline, candidate, released, and rollback stack manifests.
- Classified contract and OpenAPI diffs.
- Local repository test results and coordinated E2E result summary.
- Redacted evidence bundle index and checksums.
- Named review and approval decisions.
- Release and deployment identifiers for every affected repository.
- Compatibility, migration, deprecation, and rollback guidance.
- Updated safety, hazard, QMS, regulatory, and support records where applicable.
- Observation outcome, residual risks, follow-up issues, and lessons learned.

## Roadmap

Legend: [x] done, [~] in progress or partially done, [ ] not started

- [x] **RUN-1 - Establish the initial runbook specification.** Define scope, terminology, gates, repository responsibilities, evidence, and rollback principles.
- [~] **RUN-2 - Consolidate repository contributions.** Merge requirements and edge cases collected from all five repositories and remove contradictory or duplicate guidance.
- [ ] **RUN-3 - Define the upgrade-record template.** Choose its canonical location and required metadata, decision, evidence, approval, and closure fields.
- [ ] **RUN-4 - Inventory canonical repository commands.** Record the authoritative test, build, version, release, deployment, and verification entry points without duplicating their implementation.
- [ ] **RUN-5 - Define machine-readable stack and evidence schemas.** Align the runbook with the Demo Client E2E harness's requested, resolved, observed, result, and evidence contracts.
- [ ] **RUN-6 - Define the supported compatibility policy.** Decide how current, previous, candidate, legacy, and unsupported combinations are selected, reviewed, published, and retired.
- [ ] **RUN-7 - Add contract-diff procedures.** Prototype normalized OpenAPI, Python API, npm/TypeScript export, CDN, and documentation-example comparisons.
- [ ] **RUN-8 - Define approval and exception policy.** Name required roles and approval depth for routine, breaking, clinically consequential, security-sensitive, and emergency changes.
- [ ] **RUN-9 - Define durable evidence retention.** Select locations, access controls, retention periods, redaction checks, checksums, and links from controlled documentation.
- [ ] **RUN-10 - Define deployment promotion and rollback procedures.** Capture current infrastructure mechanisms, immutable artefact promotion, hold points, monitoring, and coherent rollback stacks.
- [ ] **RUN-11 - Rehearse representative upgrade shapes.** Dry-run documentation-only, one-runtime-repository, API contract, component major, and full coordinated upgrades in non-production environments.
- [ ] **RUN-12 - Publish the operational runbook.** Move settled procedure into the appropriate developer/QMS documentation location, link it from contributor guidance, and retain this spec for design history or mark it superseded.

## Open Decisions

- Where the active upgrade record should live and how records spanning several GitHub repositories are indexed.
- Which repository or service stores durable E2E evidence after normal CI artefacts expire.
- The exact machine-readable stack-manifest and result schemas.
- Which supported-version combinations form mandatory release gates rather than periodic or opt-in matrices.
- How candidate Python and npm packages are distributed before public release without confusing them with supported releases.
- Whether container images and static client/component artefacts are currently built once and promoted or rebuilt per environment.
- How deployed API, Demo Client, and documentation versions expose immutable commit/deployment identity for automated verification.
- Which OpenAPI changes can be classified automatically and which always require human integrator review.
- Required approver roles for each change classification, including emergency security upgrades.
- Evidence-retention periods and access controls for traces, logs, screenshots, fixtures, exports, and release summaries.
- Monitoring signals, observation periods, and quantitative rollback thresholds for each deployable layer.
- The canonical public compatibility-table format and policy for retiring support.
- How emergency upgrades shorten the sequence without omitting retrospective evidence, approval, communication, and review.
