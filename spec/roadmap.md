# 2026 Documentation Review Roadmap

The bulk of the 2026 documentation review is complete and is captured in [PR #161](https://github.com/rcpch/digital-growth-charts-documentation/pull/161). What remains is grouped below: work that is blocked on an upstream dependency, and improvements deferred to a future cycle.

## Completed

- [x] Apply page-level tags via frontmatter across the docs for an extra layer of search discoverability (the first half of <https://github.com/rcpch/digital-growth-charts-documentation/issues/73>). Zensical now supports frontmatter `tags`, which render at the foot of each page and are indexed into search (<https://zensical.org/docs/setup/tags/>). The tag vocabulary and convention are documented in `docs/developer/writing-documentation.md`.

## Blocked Upstream

- [ ] Add a tags index/listing page that aggregates all tags into a browsable `tags.md` (the second half of <https://github.com/rcpch/digital-growth-charts-documentation/issues/73>). Page-level tags themselves now ship via frontmatter (see the Completed section), but tag *listings* are still not supported by Zensical (tracking: <https://github.com/zensical/backlog/issues/38>). Add the index page once Zensical supports it.

## Future Improvements

### Safety and compliance

- [ ] Review the Medical Device Regulation technical documentation in `docs/safety/medical-device-reg/mdr-technical-docs.md` for compliance with recent EU MDR updates.
- [ ] Review the Clinical Safety Management File documents in `docs/safety/csmf/`, addressing the outstanding hazard issues (<https://github.com/rcpch/digital-growth-charts-documentation/issues/48>, <https://github.com/rcpch/digital-growth-charts-documentation/issues/49>, <https://github.com/rcpch/digital-growth-charts-documentation/issues/50>, <https://github.com/rcpch/digital-growth-charts-documentation/issues/51>, <https://github.com/rcpch/digital-growth-charts-documentation/issues/88>) and the missing-section fix in <https://github.com/rcpch/digital-growth-charts-documentation/issues/116>.
- [ ] Government Digital Service Open API best-practice review (<https://github.com/rcpch/digital-growth-charts-documentation/issues/61>).
- [ ] WCAG 2.1 level AA compliance (<https://github.com/rcpch/digital-growth-charts-documentation/issues/62>).
- [ ] Accessibility Statement (<https://github.com/rcpch/digital-growth-charts-documentation/issues/63>).
- [ ] Benefits case describing the objectives of the project (<https://github.com/rcpch/digital-growth-charts-documentation/issues/64>).
- [ ] Add a DPIA (Data Protection Impact Assessment) section (<https://github.com/rcpch/digital-growth-charts-documentation/issues/113>).

### New or expanded content

- [ ] FHIR and openEHR implementation sections (<https://github.com/rcpch/digital-growth-charts-documentation/issues/117>). The SNOMED CT part shipped in the 2026 review (`docs/integrator/snomed-codes.md`); FHIR (Magentus mapping WIP) and openEHR (Apperta archetype) are larger and less generically useful, so are deferred.
- [ ] Add an information-security-oriented flowchart (<https://github.com/rcpch/digital-growth-charts-documentation/issues/129>).
- [ ] Add a high-level flowchart (<https://github.com/rcpch/digital-growth-charts-documentation/issues/130>).

### Site and UI

- [ ] Hero section - width should match rest of site? Reduce size of text. Add some more interesting RCPCH colours? Make the hero dismissible.
</content>
</invoke>
