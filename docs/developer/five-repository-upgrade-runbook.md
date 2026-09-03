---
title: Five-Repository Upgrade Runbook
reviewers: Dr Marcus Baw
audience: developers
tags:
  - Versioning
  - Testing
  - Contributing
---

# Upgrading the dGC Platform

Use this runbook when a change might cross repository boundaries, alter a public contract, or need coordinated releases. It works just as well for one repository as for all five: mark anything that does not apply and say why.

!!! note "Work in progress"

    We are still learning the best way to coordinate and test upgrades across these repositories. Treat this runbook as practical guidance that will improve with each upgrade, and record anything that was unclear, missing, or unnecessarily difficult.

The five repositories normally flow in this order:

1. `rcpchgrowth-python` - calculations
2. `digital-growth-charts-server` - API
3. `digital-growth-charts-react-component-library` - charts
4. `digital-growth-charts-react-client` - Demo Client and E2E harness
5. `digital-growth-charts-documentation` - integration, safety, and release documentation

!!! important

    A green test run is evidence, not approval. Changes affecting clinical behaviour, safety controls, security, accessibility, or public contracts still need the appropriate human review.

## 1. Start An Upgrade Record

Open one issue or document that follows the upgrade from idea to closure. Keep it brief, but answer these questions before changing code:

```text
Upgrade:
Owner and reviewers:
Why are we doing it?
Repositories affected:
Repositories not affected, and why:
Users or integrations affected:
Known-good baseline versions:
Proposed candidate versions:
What may change?
What must not change?
How will we test it?
Rollback versions and triggers:
Evidence and approvals:
```

Do not assume that only RCPCH applications consume a library. The Python package, API, and React component all have direct users.

## 2. Capture What Works Now

Before upgrading, record the exact versions, commits, image digests, deployed URLs, and known failures in the current supported stack. Run the relevant tests once against this baseline.

This gives you something honest to compare with. Otherwise, an old warning can look like a new regression, or a new failure can be dismissed as "probably already there".

Also write down a coherent rollback stack now. Five individually old versions are not useful if they were never known to work together.

## 3. Agree The Contract

List anything another layer or user could notice: calculation results, Python imports, API routes and schemas, validation and error responses, authentication, React props and types, warnings, exports, UI behaviour, or documentation.

For each expected difference, say whether it is compatible, deprecated, intentionally breaking, or unsupported. If it is breaking, agree the migration and communication before release.

When the API is involved, review a normalized OpenAPI diff. Do not check only successful responses; errors, optional fields, bulk results, and authentication are contracts too.

## 4. Build From Upstream To Downstream

Work through only the rows that apply, usually from top to bottom:

| Repository | Before moving on |
|---|---|
| Python | Clinical vectors, boundaries, regressions, package API, and intended numerical differences are reviewed. Record the candidate package and commit. |
| API | It uses the exact Python candidate. Review OpenAPI and real success/error responses, then record the image digest and deployment identity. |
| Chart Component | Test genuine API responses, public props/types, npm and CDN surfaces, persisted legacy responses, accessibility, and exports as applicable. Run Storybook and Chromatic checks for component behaviour and visual regressions. |
| Demo Client | Build with the exact API and component candidates. Exercise real browser workflows and confirm the selected component is actually in the bundle. |
| Documentation | Update integration, compatibility, migration, versioning, safety, and support guidance, but do not describe a candidate as production. |

Use each repository's own test, build, and release commands. Test local work in isolated worktrees, packages, or containers rather than rewriting another checkout's dependency files.

## 5. Test The Combination

Run the Demo Client E2E harness against real API responses and a real browser. Record both what you requested and what actually ran; caches, lockfiles, mutable tags, and deployments can quietly select something else.

Storybook and Chromatic add another useful testing layer. Stories built from reviewed, genuine API-shaped responses can expose incompatibilities originating in Python calculations, API response contracts, or React rendering, while Chromatic can make unintended visual changes easy to review. They complement the Python and API suites and the live E2E harness; they do not replace them, because fixture-backed stories do not prove that the selected Python and API versions are running together.

Choose the smallest useful matrix:

- The current supported stack, to confirm the baseline.
- One changed layer at a time, to locate boundary regressions.
- The complete candidate stack.
- Persisted legacy responses when response data may outlive an API version.
- The rollback stack.

Do not run every historical combination. Mark a combination as unsupported when that is the policy; do not disguise it as a failed test or a silent skip.

Use only fictional data. Redact credentials before retaining logs, traces, screenshots, requests, responses, or exported charts.

## 6. Stop And Review

Pause here. Review the contract diffs, clinical and UI evidence, unexpected warnings, skipped tests, migration advice, known exceptions, and rollback plan with the people named in the upgrade record.

Do not continue if:

- The observed versions do not match the candidate.
- A changed result has no agreed explanation.
- OpenAPI or package exports changed unexpectedly.
- A required test was weakened, skipped, or had its expected output silently replaced.
- The rollback combination is unavailable or untested.
- A required clinical, safety, security, or accessibility reviewer has not approved the change.

## 7. Release In Small Steps

Freeze the approved version set, then release in the agreed dependency order. Prefer promoting the artefacts you tested rather than rebuilding them.

After each package publication or deployment:

1. Check the public package, image, CDN, or website really contains the intended version.
2. Run the agreed smoke test.
3. Record what was released and observed.
4. Stop if a rollback trigger is met.

Never overwrite or erase a published package to simulate rollback. Publish a corrective version or restore the approved deployment, and preserve the audit trail.

## 8. Document, Watch, And Close

Once the runtime stack is real, update the documentation with exact released versions, compatibility, migration steps, limitations, and support information. Run the documentation checks and publish through the repository's normal release process.

Verify the documentation release, PDFs, production site, links, and displayed version separately; those surfaces can succeed or fail independently. Use a fresh browser context when checking version information that may be cached.

Watch the agreed technical, clinical, security, and support signals. Close the upgrade record only when the release is accepted or has been coherently rolled back. Record the final versions, evidence, approvals, residual risks, follow-up work, and anything that should improve this runbook next time.

## The Short Version

Know what works now. Say what may change. Build upstream to downstream. Test the real combination. Check what actually ran. Get human approval. Release one step at a time. Keep rollback ready. Document reality, then watch it.

The detailed design and outstanding decisions are recorded in the [runbook specification](https://github.com/rcpch/digital-growth-charts-documentation/blob/live/spec/five-repository-upgrade-runbook.md).
