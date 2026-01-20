# RCPCH Digital Growth Charts Documentation - Site Specification

## Purpose

Provide a single, authoritative documentation hub for the RCPCH Digital Growth Charts (dGC) platform, covering product overview, integration guidance, clinical context, safety/regulatory evidence, legal/compliance details, and contribution workflows.

## Primary Audiences

- Integrators and implementers building dGC into EPR/EHR/PHR or other systems.
- Clinicians and health staff needing chart interpretation guidance.
- Parents/carers seeking plain-language chart information.
- Researchers using bulk growth calculations in offline or secure environments.
- Developers and contributors extending the platform and its documentation.
- Clinical safety officers and compliance stakeholders.

The initial pages should assist users to find the part of the documentation that most closely matches their needs. We have a number of types of user - clincians, developers, researchers, parents, statisticians and so on. Each type of user should be able to quickly find the relevant sections of the documentation.

## Information Architecture (Top-Level)

- Home
- About: project background, open-source approach, scope, references, videos, awards.
- Products: platform components and clients (API server, React component, demo client, Python library, CLI, Google Sheets plugin, Flutter app, React Native client), pricing.
- Integrators: onboarding, API calls, API reference (Swagger), chart component usage, client specification, support, FAQs.
- Clinicians: how the API works, chart information, date/age calculations, growth references, FAQs.
- Researchers: guidance for using the Python package in research/SRE contexts.
- Parents: chart information in accessible language.
- Contributors: developer onboarding, environment setup, testing, versioning, writing documentation, contributing.
- Clinical Safety: CSMF documents, DTAC assessment, UK medical device registration, technical documentation, downloads.
- Legal: disclaimer, licensing/copyright, data protection, privacy notice.
- Technical: security, DSPT evidence, service status.
- Contact: forum, commercial, and general enquiries.

## Core Content Features

- Product and platform overview describing the API-first architecture and companion clients/libraries.
- Integration guidance with concrete request examples, Postman collections, and API key practices.
- Embedded Swagger UI for live API reference.
- Detailed client specification for clinically safe chart rendering.
- Clinical guidance on growth references, centiles/SDS, and gestational age correction.
- Research usage guidance for offline/secure environments via the Python package.
- Clinical safety management file (DCB0129/0160), hazard log, and DTAC evidence.
- Regulatory and compliance documentation (UKCA/MHRA, essential requirements, technical docs).
- Legal/privacy/data protection documentation emphasizing a stateless API model.
- Support pathways (forum, commercial support, contact channels).
- Downloadable full documentation PDF (when PDF export enabled).

## Key Assertions the Site Communicates

- The platform is open source, with clear licensing boundaries per component.
- The API is a regulated medical device and has associated clinical safety documentation.
- The API is stateless and does not persist patient-identifiable data.
- The platform targets accurate, clinically safe growth calculations across supported references.

## Presentation and Interaction Features

- Built with MkDocs + Material theme and a custom RCPCH theme.
- Tabbed navigation with expanded sidebar and anchor tracking.
- Search, code copy/select helpers, and edit/view buttons for GitHub source.
- Sortable tables and embedded assets (images, PDFs, iframes).
- Optional plugins for git committers and PDF generation.

## LLMs.txt Generation

- The site should have an LLMs.txt to make it easier for LLMs to read and understand the content, including the integration documentation. It should be possible to generate this file automatically from the existing documentation.

## Hosting and Maintenance Expectations

- Published at `https://growth.rcpch.ac.uk` with GitHub Pages published via GitHub Actions.
- Documentation changes follow GitHub workflow with protected `live` branch.
- Site supports local development via Docker and MkDocs.

---

## Goals

- Comprehensive and totally open documentation
-

## Non-Goals

- Avoid repetition of content across different user sections; instead, cross-reference to guide users to relevant information.
