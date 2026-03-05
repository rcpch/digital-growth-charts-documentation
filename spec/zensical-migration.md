# Zensical Migration Notes

This file documents issues and compatibility concerns identified during the migration from Material for MkDocs to Zensical.

## Changes Made

| File | Change |
|------|--------|
| `requirements.txt` | Replaced `mkdocs-material` with `zensical` |
| `mkdocs.yml` | Removed `theme.name: material`; added `theme.variant: classic`; updated emoji module paths to `zensical.extensions.emoji.*` |
| `docker-compose.yml` | Replaced `mkdocs serve` with `zensical serve` |
| `.github/workflows/ALL-BRANCHES-ALL-PRs-build-and-deploy-to-azure.yml` | Replaced `mkdocs build` with `zensical build --clean` |
| `Dockerfile` | Updated comment |
| `docs/developer/writing-documentation.md` | Updated all MkDocs/Material CLI and wording references |
| `docs/legal/licensing-copyright.md` | Updated MkDocs entry in software bill of materials table |
| `docs/about/acknowledgements.md` | Updated technical acknowledgements |
| `spec/spec.md` | Updated tooling references |
| `s/README.md` | Updated server description |
| `docs/_utilities/page-template.md` | Updated MkDocs references in template comments |

## Flagged Issues

### 1. `mkdocs-with-pdf` plugin — likely incompatible

**File:** `requirements.txt`, `mkdocs.yml` (`plugins.with-pdf`)

The `mkdocs-with-pdf` plugin is specifically designed for Material for MkDocs. It hooks into Material's rendering pipeline and may not function correctly under Zensical's classic variant. The PDF export feature (controlled by `ENABLE_PDF_EXPORT` env var) should be tested after migration.

**Recommendation:** Test PDF generation with `ENABLE_PDF_EXPORT=1 zensical build --clean`. If it fails, the plugin may need to be replaced or removed; flag in the migration. The `extra.pdf_export` variable and `output_path: pdf/digital-growth-charts-documentation.pdf` config will also be affected if the plugin is dropped.

> * comment out PDF generation in `mkdocs.yml` 
> * hard-wire a recent version of the PDF export to the download button
> * Await zensical PDF module https://github.com/zensical/backlog/issues/25
> * note all this in a GitHub issue to remind us to re-enable PDF export once zensical supports it natively

---

### 2. `custom_dir: rcpch-theme` — needs review

**File:** `mkdocs.yml` (`theme.custom_dir`)

The `rcpch-theme/` directory contains template overrides built against Material for MkDocs' Jinja2 template structure. These overrides may reference Material-specific template blocks or macros that do not exist in Zensical's classic variant, causing build errors or silent rendering failures.

**Recommendation:** Inspect each file in `rcpch-theme/` and verify it only extends/overrides blocks that exist in Zensical's classic variant templates.

---

### 3. Material-specific `theme.features` — may be silently ignored or unsupported

**File:** `mkdocs.yml` (`theme.features`)

The following features are Material for MkDocs-specific and may not be recognised by Zensical:

- `content.action.edit`
- `content.action.view`
- `content.code.copy`
- `content.code.select`
- `navigation.expand`
- `navigation.footer`
- `navigation.instant`
- `navigation.tabs`
- `navigation.tabs.sticky`
- `navigation.top`
- `navigation.tracking`
- `toc.follow`

**Recommendation:** Check Zensical's classic variant documentation for supported feature flags. Remove or replace any that are not supported to avoid unexpected behaviour.

> So far most seem like they work natievly. 

---

### 4. `theme.palette` — Material-specific setting

**File:** `mkdocs.yml` (`theme.palette`)

The `palette` block with `scheme: default` is a Material for MkDocs construct. Zensical may not use this key, or may interpret it differently.

**Recommendation:** Verify that Zensical's classic variant supports a `palette` configuration. If not, this block can be removed without affecting functionality (it only controls light/dark mode, and dark mode was intentionally disabled in the comments).

---

### 5. `theme.font` — Material-specific setting

**File:** `mkdocs.yml` (`theme.font`)

The `font` block (`text: Montserrat`, `code: Roboto Mono`) uses Material for MkDocs' mechanism for loading Google Fonts. Zensical may handle fonts differently.

**Recommendation:** Verify font loading still works after migration. If Montserrat and Roboto Mono are not rendered, fonts may need to be loaded via `extra_css` instead.

---

### 6. `docker-compose.yml` service name

**File:** `docker-compose.yml`

The Docker Compose service is still named `mkdocs`. This is a minor cosmetic issue and does not affect functionality, but may cause confusion.

**Recommendation:** Optionally rename the service from `mkdocs` to `zensical` or `docs` for clarity.

---

### 7. `docs/developer/writing-documentation.md` — workflow filename in CI link

**File:** `docs/developer/writing-documentation.md` (line ~25)

The page links to a GitHub Actions workflow filename (`build-and-deploy-to-gh-pages-and-azure.yml`) that does not match the actual workflow filename (`ALL-BRANCHES-ALL-PRs-build-and-deploy-to-azure.yml`). This predates the Zensical migration but should be corrected.

---

## Validation Steps

After completing the migration, verify with:

```bash
pip install -r requirements.txt
zensical build --clean
zensical serve
```

Also run with PDF and git-committers enabled to confirm those optional plugins are functional:

```bash
ENABLE_PDF_EXPORT=1 ENABLE_GIT_COMMITTERS=True zensical build --clean
```
