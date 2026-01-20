# Documentation Style Guide (RCPCH dGC)

This guide sets the baseline style and structure for the documentation site. Keep it consistent across new and edited pages.

## Formatting

- Use YAML frontmatter on all docs pages with at least `title` and `reviewers`. Include `audience` where possible.
- Use a single H1 (`#`) per page for the on-page title; use H2/H3 for sectioning.
- Prefer Markdown over raw HTML; only use HTML when necessary for embeds (iframes, objects) or advanced layout.
- Use fenced code blocks with an info string (e.g., `bash`, `json`, `html`) and keep examples minimal.
- Use admonitions for key callouts (`note`, `info`, `tip`, `warning`, `danger`, `success`) and keep them short.
- Use tables sparingly and keep them readable on mobile.
- Keep lists short and parallel; use bullets for unordered items and numbers for sequences.

## Structure

- Start with a brief purpose statement or short intro paragraph.
- Split long pages with clear H2 headings every 3–6 paragraphs.
- Group related content into sections and avoid mixing audiences in one section.
- Use reusable snippets for repeated content via `--8<--` includes.
- Keep page length reasonable; split into multiple pages if a topic grows too large.

## Navigation

- Place new pages under `docs/` in the most relevant folder.
- Add new pages to `mkdocs.yml` `nav` to control ordering and sidebar labels.
- Use `not_in_nav` only for drafts or utility pages that should not appear in navigation.
- Keep nav titles human-readable; acronyms and product names should match existing casing.

## Writing Style and Tone

- Professional, concise, and clear; avoid unnecessary verbosity.
- Tailor language to the `audience` in frontmatter: avoid deep technical or clinical jargon unless needed.
- Prefer plain English and active voice.
- Define abbreviations on first use and add them to `includes/_abbreviations.md`.
- Be explicit about safety, licensing, and compliance constraints when relevant.

## Links and Assets

- Use relative links for internal pages (e.g., `../integrator/getting-started.md`).
- Use absolute links for external sites and label them clearly.
- Store images in `docs/_assets/_images` and PDFs in `docs/_assets/_pdfs`.
- Provide meaningful alt text for images.

## Frontmatter Conventions

Use the existing pattern from `docs/_utilities/page-template.md`:

```yaml
---
title: Page Title
reviewers: Name 1, Name 2
audience: integrators, clinicians
---
```

## Reuse and Consistency

- Reuse existing phrasing for platform/product names (e.g., "Digital Growth Charts", "dGC API").
- Align terminology with the site’s clinical guidance and the API specification.
- When adding new products or features, update relevant overview pages and FAQs.
