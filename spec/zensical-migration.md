# Zensical Migration Notes

This file documents issues and compatibility concerns identified during the migration from Material for MkDocs to Zensical.

## Changes Made

| File | Change |
|------|--------|
| `requirements.txt` | Replaced `mkdocs-material` with `zensical`; suspended incompatible plugins with tracking comments |
| `mkdocs.yml` | Removed `theme.name: material`; added `theme.variant: classic`; updated emoji module paths to `zensical.extensions.emoji.*`; commented out suspended plugins |
| `docker-compose.yml` | Replaced `mkdocs serve` with `zensical serve`; renamed service from `mkdocs` to `zensical` |
| `.github/workflows/ALL-BRANCHES-ALL-PRs-build-and-deploy-to-azure.yml` | Replaced `mkdocs build` with `zensical build --clean`; updated comment |
| `Dockerfile` | Updated plugin comment |
| `docs/developer/writing-documentation.md` | Updated all MkDocs/Material CLI and wording references; fixed stale CI workflow filename link |
| `docs/legal/licensing-copyright.md` | Updated MkDocs entry in software bill of materials table |
| `docs/about/acknowledgements.md` | Updated technical acknowledgements |
| `docs/safety/download.md` | Added notice that PDF is the last pre-migration build; link retained |
| `spec/spec.md` | Updated tooling references |
| `s/README.md` | Updated server description |
| `docs/_utilities/page-template.md` | Updated MkDocs references in template comments |
| `rcpch-theme/overrides/home.html` | Refactored hero section: collapsible toggle, `md-grid` width constraint, reduced padding |
| `docs/_assets/_stylesheets/extra.css` | Scoped iframe margin to `#demo-iframe` only |

## Flagged Issues

### 1. `mkdocs-with-pdf` plugin — suspended

**File:** `requirements.txt`, `mkdocs.yml` (`plugins.with-pdf`)

**Status: suspended** — the plugin is commented out in both `requirements.txt` and `mkdocs.yml`. The download page (`docs/safety/download.md`) links to the last PDF generated before the migration and carries a notice explaining this.

A GitHub issue has been created to track re-enablement: [rcpch/digital-growth-charts-documentation#150](https://github.com/rcpch/digital-growth-charts-documentation/issues/150)

Awaiting Zensical native PDF support: [zensical/backlog#25](https://github.com/zensical/backlog/issues/25)

---

### 2. `custom_dir: rcpch-theme` — needs review

**File:** `mkdocs.yml` (`theme.custom_dir`)

The `rcpch-theme/` directory contains template overrides built against Material for MkDocs' Jinja2 template structure. These overrides may reference Material-specific template blocks or macros that do not exist in Zensical's classic variant, causing build errors or silent rendering failures.

**Recommendation:** Inspect each file in `rcpch-theme/` and verify it only extends/overrides blocks that exist in Zensical's classic variant templates.

---

### 3. Material-specific `theme.features` — confirmed supported

**File:** `mkdocs.yml` (`theme.features`)

**Status: resolved** — all features in use are confirmed supported by Zensical's classic variant. Verified against [zensical.toml](https://github.com/zensical/zensical/blob/bf930dd84ba8f9013fa83752d130e2fc833462c8/python/zensical/bootstrap/zensical.toml). No CLI errors and no broken formatting observed.

---

### 4. `theme.palette` — confirmed supported

**File:** `mkdocs.yml` (`theme.palette`)

**Status: resolved** — `[[project.theme.palette]]` with `scheme: default` is confirmed supported in Zensical's classic variant, as shown in the bootstrap `zensical.toml`. No changes required.

---

### 5. `theme.font` — confirmed supported

**File:** `mkdocs.yml` (`theme.font`)

**Status: resolved** — font configuration (`text: Montserrat`, `code: Roboto Mono`) works correctly under Zensical. Google Fonts are loaded as expected.

---

### 6. `docker-compose.yml` service name — resolved

**File:** `docker-compose.yml`

**Status: resolved** — service renamed from `mkdocs` to `zensical`.

---

### 7. `docs/developer/writing-documentation.md` — stale CI workflow link — resolved

**File:** `docs/developer/writing-documentation.md`

**Status: resolved** — link corrected to `ALL-BRANCHES-ALL-PRs-build-and-deploy-to-azure.yml`.

---

### 8. Other suspended plugins

The following plugins were also suspended pending Zensical module system support. Each has a tracking issue linked in `requirements.txt` and is commented out in `mkdocs.yml`:

| Plugin | Zensical tracking issue |
|--------|------------------------|
| `mkdocs-git-committers-plugin-2` | [zensical/backlog#17](https://github.com/zensical/backlog/issues/17) |
| `mkdocs-git-revision-date-localized-plugin` | [zensical/backlog#18](https://github.com/zensical/backlog/issues/18) |
| `mkdocs-macros-plugin` | [zensical/backlog#16](https://github.com/zensical/backlog/issues/16) |
| `mkdocs-llmstxt` | [zensical/backlog#92](https://github.com/zensical/backlog/issues/92) |

---

## Validation Steps

Build and serve without optional plugins (current state):

```bash
pip install -r requirements.txt
zensical build --clean
zensical serve
```

Once plugins are re-enabled, verify each individually:

```bash
ENABLE_PDF_EXPORT=1 zensical build --clean
ENABLE_GIT_COMMITTERS=True zensical build --clean
```
