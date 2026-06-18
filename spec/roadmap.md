# 2026 Documentation Review Roadmap

- [x] Review all docs files to create generalised high-level features (`spec.md`), implementation guidances (`implementation.md`), and style guide (`style-guide.md`) for the RCPCH Digital Growth Charts platform documentation.
- [x] Audit all docs files for compliance with the `spec/style-guide.md` and create this roadmap of changes that will improve the docs site to meet those standards.
- [x] Add further convenience scripts to `s/` as needed to help with documentation development and maintenance.
- [x] Add dependabot configuration to keep documentation dependencies up to date.
- [x] Add linting and spellchecking scripts to make it easier to use these consistently and regularly.
- [x] Run linting and spellchecking across all docs files and fix any issues found.
 - <https://github.com/rcpch/digital-growth-charts-documentation/issues>
- [x] Add automated `LLMs.txt` generation to the build output to meet `spec/spec.md` requirements. There is a plugin for MkDocs at <https://github.com/pawamoy/mkdocs-llmstxt> which should help achieve this goal.
- [x] Expand the home page audience routing in `rcpch-theme/overrides/home.html` to include parents/carers, researchers, and safety/compliance audiences, not just integrators/clinicians/contributors.
- [x] Add missing `audience` frontmatter to content pages with no existing `audience` field.
- [x] Add missing `reviewers` frontmatter to `docs/index.md` and `docs/safety/download.md`.
- [x] Add short purpose/intro paragraphs where pages currently jump straight to embeds or snippets: `docs/integrator/api-reference.md`, `docs/technical/status.md`, `docs/safety/download.md`, `docs/legal/disclaimer.md`.
- [x] Update `docs/developer/writing-documentation.md` to explicitly cover markdown linting, UK English spelling, and running `s/codespell` per `spec/implementation.md`.
- [x] Audit duplicated content across audience sections (clinicians/parents/integrators) and replace repeats with shared snippets and cross-links, per `spec/spec.md` non-goal.
- [x] Investigate whether PDF export can be constrained to specific parts of the documentation. Implemented a self-hosted WeasyPrint exporter (`pdf-export/build-safety-pdf.py`, `s/build-pdf`) that builds a single PDF of the Clinical Safety and Medical Device sections from the built site, wired into the build-and-deploy workflow. This replaces the suspended `mkdocs-with-pdf` plugin for the safety documentation.
- [x] Document the `clinicianFocus` prop (and the rest of the `<RCPCHChart>` props) - addressed by the curated props table on `docs/integrator/using-the-chart-component.md` (closes <https://github.com/rcpch/digital-growth-charts-documentation/issues/89>).
- [x] Signpost why the example cURL command fails in Windows Command Prompt / PowerShell and offer alternatives (Git Bash, WSL, Postman) on `docs/integrator/making-api-calls.md` (closes <https://github.com/rcpch/digital-growth-charts-documentation/issues/138>).
- [x] Provide a PDF of the safety documentation - delivered by the self-hosted WeasyPrint exporter (see above), so this no longer depends on the `with-pdf` plugin landing in Zensical. There is no use-case for a whole-site PDF, so no further work is needed here (closes <https://github.com/rcpch/digital-growth-charts-documentation/issues/150>).
- [ ] Re-enable `git-committers` plugin once supported by Zensical and verify contributor metadata rendering (tracking: <https://github.com/zensical/backlog/issues/17>).
- [ ] Re-enable `git-revision-date-localized` plugin once supported by Zensical and verify page timestamp rendering (tracking: <https://github.com/zensical/backlog/issues/18>).
- [x] Re-enable `macros` for Jinja2 templating - now built into Zensical (0.0.40) as the `zensical.extensions.macros` markdown extension. Enabled in `mkdocs.yml` and verified the `{{ repository_name }}` badge substitution in `docs/products/*.md` (also fixed the python-library page, which was pointing at the wrong repository). Tracking: <https://github.com/zensical/backlog/issues/16>.
- [ ] Re-enable `llmstxt` plugin (or equivalent native feature) once supported by Zensical and verify `LLMs.txt` generation in build output (tracking: <https://github.com/zensical/backlog/issues/92>).
- [ ] Audit all overrides in `rcpch-theme/` against Zensical classic template blocks/macros to confirm `theme.custom_dir` compatibility and remove any Material-specific template assumptions.
- [ ] Dark mode?
- [ ] Review the Medical Device Regulation technical documentation in `docs/safety/medical-device-reg/mdr-technical-docs.md` for compliance with recent EU MDR updates.
- [ ] Review the Clinical Safety Management File documents in `docs/safety/csmf/`. This review should also address the outstanding hazard issues: <https://github.com/rcpch/digital-growth-charts-documentation/issues/48>, <https://github.com/rcpch/digital-growth-charts-documentation/issues/49>, <https://github.com/rcpch/digital-growth-charts-documentation/issues/50>, <https://github.com/rcpch/digital-growth-charts-documentation/issues/51>, <https://github.com/rcpch/digital-growth-charts-documentation/issues/88>, and the missing-section fix in <https://github.com/rcpch/digital-growth-charts-documentation/issues/116>.
- [ ] Hero section - width should match rest of site? Reduce size of text. Add some more interesting RCPCH colours? Make the hero dismissible.
- [ ] Institute some 'point' regression testing for key items of content, to help identify missing content caused by upstream framework bugs etc.

## Outstanding GitHub Issues

These are the open issues in the [documentation repository](https://github.com/rcpch/digital-growth-charts-documentation/issues) that are not already covered by a specific item above. They are mostly content and compliance work rather than the structural/migration tasks that make up the bulk of this roadmap. Grouped here so the 2026 review has a single view of the backlog.

### Blocked on upstream Zensical support

- [ ] Add Tags to the documentation site, applied via page frontmatter and indexed into a tags page, for an extra layer of discoverability (<https://github.com/rcpch/digital-growth-charts-documentation/issues/73>). Blocked until Zensical supports the `material/tags` plugin (tracking: <https://github.com/zensical/backlog/issues/38>).

### Compliance and governance

- [ ] Government Digital Service Open API best-practice review (<https://github.com/rcpch/digital-growth-charts-documentation/issues/61>).
- [ ] WCAG 2.1 level AA compliance (<https://github.com/rcpch/digital-growth-charts-documentation/issues/62>).
- [ ] Accessibility Statement (<https://github.com/rcpch/digital-growth-charts-documentation/issues/63>).
- [ ] Benefits case describing the objectives of the project (<https://github.com/rcpch/digital-growth-charts-documentation/issues/64>).
- [ ] Add a DPIA (Data Protection Impact Assessment) section (<https://github.com/rcpch/digital-growth-charts-documentation/issues/113>).

### New or expanded content

- [ ] User Journeys documentation (<https://github.com/rcpch/digital-growth-charts-documentation/issues/60>).
- [ ] Develop the "Subscriber Guide" section (<https://github.com/rcpch/digital-growth-charts-documentation/issues/98>).
- [ ] FHIR, SNOMED and openEHR implementation section (<https://github.com/rcpch/digital-growth-charts-documentation/issues/117>).
- [ ] De-emphasise Bone Age and Events in the introductory API examples and move them to a clearly-marked optional section, so implementers don't think they are required parameters (<https://github.com/rcpch/digital-growth-charts-documentation/issues/122>).
- [ ] Clarify what gestational age is in implementer-friendly terms, and that it is fixed once the child is born (<https://github.com/rcpch/digital-growth-charts-documentation/issues/123>).
- [ ] List of which NHS orgs, non-NHS orgs and suppliers are using dGC (<https://github.com/rcpch/digital-growth-charts-documentation/issues/127>). Relates to the existing `docs/about/whos-using-dgc.md` page.
- [ ] Add an information-security-oriented flowchart (<https://github.com/rcpch/digital-growth-charts-documentation/issues/129>).
- [ ] Add a high-level flowchart (<https://github.com/rcpch/digital-growth-charts-documentation/issues/130>).