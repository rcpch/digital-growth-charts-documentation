# 2026 Documentation Review Roadmap

- [x] Review all docs files to create generalised high-level features (`spec.md`), implementation guidances (`implementation.md`), and style guide (`style-guide.md`) for the RCPCH Digital Growth Charts platform documentation.
- [x] Audit all docs files for compliance with the `spec/style-guide.md` and create this roadmap of changes that will improve the docs site to meet those standards.
- [x] Add further convenience scripts to `s/` as needed to help with documentation development and maintenance.
- [x] Add dependabot configuration to keep documentation dependencies up to date.
- [x] Add linting and spellchecking scripts to make it easier to use these consistently and regularly.
- [x] Run linting and spellchecking across all docs files and fix any issues found.
 - <https://github.com/rcpch/digital-growth-charts-documentation/issues>
- [x] Add automated `LLMs.txt` generation to the build output to meet `spec/spec.md` requirements. There is a plugin for MkDocs at <https://github.com/pawamoy/mkdocs-llmstxt> which should help achieve this goal.
- [ ] Expand the home page audience routing in `rcpch-theme/overrides/home.html` to include parents/carers, researchers, and safety/compliance audiences, not just integrators/clinicians/contributors.
- [ ] Add missing `audience` frontmatter to content pages: `docs/index.md`, `docs/developer/react-component.md`, `docs/products/api-server.md`, `docs/products/command-line-client(deprecated).md`, `docs/products/flutter-app.md`, `docs/products/pricing.md`, `docs/products/python-library.md`, `docs/products/react-client.md`, `docs/products/react-component.md`, `docs/products/react-native.md`, `docs/safety/overview.md`, `docs/safety/download.md`, `docs/safety/dtac.md`, `docs/safety/medical-device-reg/mhra.md`, `docs/safety/medical-device-reg/essential-req.md`, `docs/safety/medical-device-reg/doc-api.md`, `docs/safety/medical-device-reg/mdr-technical-docs.md`, `docs/safety/csmf/clinical-risk-mgmt-plan.md`, `docs/safety/csmf/clinical-risk-mgmt-system.md`, `docs/safety/csmf/clinical-safety-case-report.md`, `docs/safety/csmf/hazard-log.md`, `docs/safety/csmf/third-party-tools-safety-assmt.md`, `docs/safety/csmf/license.md`, `docs/technical/security.md`, `docs/technical/status.md`, `docs/technical/data-security-protection-toolkit.md`.
- [ ] Add missing `reviewers` frontmatter to `docs/index.md` and `docs/safety/download.md`.
- [ ] Add short purpose/intro paragraphs where pages currently jump straight to embeds or snippets: `docs/integrator/api-reference.md`, `docs/technical/status.md`, `docs/safety/download.md`, `docs/legal/disclaimer.md`.
- [ ] Update `docs/developer/writing-documentation.md` to explicitly cover markdown linting, UK English spelling, and running `s/codespell` per `spec/implementation.md`.
- [ ] Audit duplicated content across audience sections (clinicians/parents/integrators) and replace repeats with shared snippets and cross-links, per `spec/spec.md` non-goal.
- [ ] Investigate whether PDF export can be constrained to specific parts of the documentation.
- [ ] Dark mode?
- [ ] Review the Medical Device Regulation technical documentation in `docs/safety/medical-device-reg/mdr-technical-docs.md` for compliance with recent EU MDR updates.
- [ ] Review the Clinical Safety Management File documents in `docs/safety/csmf/` 
- [ ] Hero section - width should match rest of site? Reduce size of text. Add some more interesting RCPCH colours? Make the hero dismissible.

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/clinician/faqs-for-clinicians.md:
[✖] ../safety/overview.md
[✖] https://forum.rcpch.tech

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/clinician/chart-information-health-staff.md:
[✖] ../_assets/_images/centile-terminology.png
[✖] https://pubmed.ncbi.nlm.nih.gov/10451401/

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/researchers/introduction.md:
[✖] ../developer/api-python
[✖] ../developer/api-python

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/_assets/_snippets/dgc-platform-comprises.md:
[✖] ../../products/api-server.md
[✖] ../../products/react-component.md
[✖] ../../products/python-library.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/_assets/_snippets/docs-contributions.md:
[✖] /about/acknowledgements

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/about/about.md:
[✖] ../legal/licensing-copyright.md
[✖] videos.md
[✖] https://forum.rcpch.tech

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/integrator/getting-started.md:
[✖] ../contact/contact.md
[✖] ../_assets/_images/forum-user-summary-link.png
[✖] ../_assets/_images/forum-user-api-keys.png
[✖] ../integrator/making-api-calls.md
[✖] https://forum.rcpch.tech/

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/integrator/making-api-calls.md:
[✖] api-reference.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/integrator/using-the-chart-component.md:
[✖] ../_assets/_images/theme-builder.png
[✖] https://live--6732292d6f3624b0036f84b4.chromatic.com/
[✖] https://www.npmjs.com/package/@rcpch/digital-growth-charts-react-component-library
[✖] https://live--6732292d6f3624b0036f84b4.chromatic.com/?path=/docs/rcpchchart--docs

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/integrator/faqs-for-integrators.md:
[✖] ../products/products-overview.md
[✖] ../developer/start-here.md
[✖] ../products/react-component.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/integrator/support.md:
[✖] ../products/pricing.md
[✖] ../integrator/getting-started.md
[✖] ../clinician/faqs-for-clinicians.md
[✖] ../developer/start-here.md
[✖] ../safety/overview.md
[✖] ../_assets/_images/forum-screenshot.png
[✖] https://forum.rcpch.tech
[✖] https://forum.rcpch.tech
[✖] https://forum.rcpch.tech/

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/integrator/client-specification.md:
[✖] ../clinician/chart-information-health-staff.md
[✖] ../products/react-component.md
[✖] ../parents/chart-information-families.md
[✖] ../clinician/chart-information-health-staff.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/safety/overview.md:
[✖] ../contact/contact.md
[✖] ../safety/csmf/clinical-risk-mgmt-system.md
[✖] ../safety/csmf/hazard-log.md
[✖] ../about/team.md
[✖] ../safety/dtac.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/safety/medical-device-reg/doc-api.md:
[✖] ../../_assets/_images/marcus-signature-only-used-for-docs.jpg

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/safety/medical-device-reg/mdr-technical-docs.md:
[✖] doc-api.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/safety/medical-device-reg/mhra.md:
[✖] ../../_assets/_images/ukca_filled.png
[-] 
[-] 
[-] 

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/safety/csmf/clinical-safety-case-report.md:
[✖] clinical-risk-mgmt-system.md
[✖] clinical-risk-mgmt-plan.md
[✖] hazard-log.md
[✖] ../../_assets/_images/risk-matrix.png

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/safety/csmf/clinical-risk-mgmt-plan.md:
[✖] ../../about/team.md
[✖] hazard-log.md
[✖] clinical-safety-case-report.md
[✖] clinical-safety-case-report.md
[✖] hazard-log.md
[✖] https://forum.rcpch.tech/

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/products/python-library.md:
[✖] ../_assets/_images/python_library_carbon.png
[✖] ../developer/contributing.md
[✖] https://github.com/{{ repository_name }}/issues
[✖] https://github.com/{{ repository_name }}/stargazers
[✖] https://github.com/{{ repository_name }}/network/members
[✖] https://github.com/{{repository_name }}/blob/live/LICENSE
[✖] https://forum.rcpch.tech/

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/products/command-line-client(deprecated).md:
[✖] python-library.md
[✖] ../_assets/_images/command-line-tool.png
[✖] ../developer/rcpchgrowth-cli.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/products/google-sheets-plugin.md:
[✖] ../_assets/_images/gsheets_screenshot_navigation_apps_script.png
[✖] ../_assets/_images/gsheets_screenshot_gapps_blank.png
[✖] ../_assets/_images/gsheets_screenshot_gapps_blank_no_code.png
[✖] ../_assets/_images/gsheets_screenshot_gapps_filled_code.png
[✖] ../_assets/_images/gsheets_screenshot_gapps_working.png
[✖] ../integrator/getting-started.md
[✖] ../_assets/_images/gsheets_example_sds_centile.png
[✖] ../integrator/getting-started.md
[✖] ../_assets/_images/gsheets_example_decimal_age.png

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/products/react-client.md:
[✖] ../clinician/how-the-api-works.md
[✖] ../integrator/getting-started.md
[✖] ../integrator/api-reference.md
[✖] ../developer/react-client.md
[✖] ../developer/start-here.md
[✖] https://github.com/{{ repository_name }}/issues
[✖] https://github.com/{{ repository_name }}/stargazers
[✖] https://github.com/{{ repository_name }}/network/members
[✖] https://github.com/{{ repository_name }}/blob/live/LICENSE
[✖] https://github.com/{{ repository_name }}
[✖] https://github.com/rcpch/digital-growth-charts-flask-client

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/products/products-overview.md:
[✖] ../products/api-server.md
[✖] ../products/react-component.md
[✖] ../products/react-client.md
[✖] ../products/python-library.md
[✖] ../products/command-line-client(deprecated
[✖] ../safety/overview.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/products/api-server.md:
[✖] ../_assets/_images/api_server_postman.png
[✖] ../integrator/getting-started.md
[✖] https://github.com/{{ repository_name }}/issues
[✖] https://github.com/{{ repository_name }}/stargazers
[✖] https://github.com/{{repository_name }}/blob/live/LICENSE
[✖] https://github.com/{{ repository_name }}
[✖] https://forum.rcpch.tech/

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/products/react-component.md:
[✖] ../_assets/_images/height-chart-girl-component.png
[✖] ../integrator/client-specification.md
[✖] ../developer/contributing.md
[✖] ../contact/contact.md
[✖] ../contact/contact.md
[✖] https://live--6732292d6f3624b0036f84b4.chromatic.com/
[✖] https://github.com/{{ repository_name }}
[✖] https://forum.rcpch.tech/

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/products/flask(deprecated).md:
[✖] ../_assets/_images/flask-client.png
[✖] https://github.com/rcpch/digital-growth-charts-flask-client

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/products/react-native.md:
[✖] image
[✖] ../products/react-component.md
[✖] https://github.com/{{ repository_name }}/issues
[✖] https://github.com/{{ repository_name }}/stargazers
[✖] https://github.com/{{ repository_name }}/network/members
[✖] https://github.com/{{repository_name }}/blob/live/LICENSE
[✖] https://github.com/{{ repository_name }}

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/products/pricing.md:
[✖] ../contact/contact.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/developer/rcpchgrowth.md:
[✖] ../clinician/chart-information-health-staff.md
[✖] https://pubmed.ncbi.nlm.nih.gov/10451401/

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/developer/api-python.md:
[✖] ./api-python.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/developer/rcpchgrowth-cli.md:
[✖] ./api-python.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/developer/start-here.md:
[✖] ../integrator/support.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/developer/contributing.md:
[✖] ../contact/contact.md
[✖] api-python.md
[✖] ../about/acknowledgements.md

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/technical/security.md:
[✖] data-security-protection-toolkit.md
[✖] https://digital.nhs.uk/about-nhs-digital/our-work/nhs-digital-data-and-technology-standards/framework/beta---data-security-standards

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/legal/data-protection.md:
[✖] privacy-notice.md
[✖] https://forum.rcpch.tech/

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/clinician/how-the-api-works.md:
[✖] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3920659/

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/contact/contact.md:
[✖] https://forum.rcpch.tech

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/about/acknowledgements.md:
[✖] https://azure.microsoft.com/

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/about/awards-press-blogs.md:
[✖] https://marcus-baw.medium.com/royal-colleges-3-0-best-practice-as-code-7065bce821a7
[✖] https://pubmed.ncbi.nlm.nih.gov/37463736/

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/safety/csmf/clinical-risk-mgmt-system.md:
[✖] https://digital.nhs.uk/data-and-information/information-standards/information-standards-and-data-collections-including-extractions/publications-and-notifications/standards-and-collections/dcb0160-clinical-risk-management-its-application-in-the-deployment-and-use-of-health-it-systems

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/safety/csmf/license.md:
[✖] https://github.com/rcpch/clinical-risk-management-file

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/safety/dtac.md:
[✖] https://digital.nhs.uk/data-and-information/looking-after-information/data-security-and-information-governance/data-security-and-protection-toolkit
[✖] https://ico.org.uk/media/for-organisations/documents/2553993/dpia-template.docx
[✖] https://www.gov.uk/government/publications/data-protection-law-eu-exit
[✖] https://www.iso.org/standard/46493.html

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/developer/writing-documentation.md:
[✖] https://github.com/rcpch/digital-growth-charts-documentation/blob/live/.github/workflows/build-and-deploy-to-gh-pages-and-azure.yml

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/developer/react-component.md:
[✖] https://live--6732292d6f3624b0036f84b4.chromatic.com/?path=/docs/rcpchchart--docs
[✖] https://live--6732292d6f3624b0036f84b4.chromatic.com/?path=/story/rcpchchart--theme-builder

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/developer/faqs-for-developers.md:
[✖] https://marcus-baw.medium.com/why-we-chose-python-for-the-rcpch-digital-growth-charts-project-2d61e2766c3b

/home/marcus/code/rcpch/digital-growth-charts-documentation/docs/legal/licensing-copyright.md:
[✖] https://forum.rcpch.tech/
[✖] https://github.com/python/cpython/blob/master/LICENSE
[✖] https://directory.fsf.org/wiki/License:Python-2.0.1
[✖] https://directory.fsf.org/wiki/License:Expat
[✖] https://github.com/facebook/react/blob/master/LICENSE
[✖] https://directory.fsf.org/wiki/License:Expat
[✖] https://github.com/squidfunk/mkdocs-material/blob/master/LICENSE
[✖] https://directory.fsf.org/wiki/License:Expat