# `s/`

The `s/` directory contains some simple convenience scripts to speed up and standardise working with this repository.

## Scripts

- `s/version++` creates a dated version tag for documentation releases.
  - `./s/version++` - creates a minor release tag (YYYY.MM.DD format)
  - `./s/version++ major` - major documentation revision
  - `./s/version++ minor` - minor documentation revision (default)
  - `./s/version++ patch` - patch/small documentation update
- `s/up` starts the local Zensical (documentation) server via Docker Compose.
  - `./s/up`
  - `./s/up -d` (detached)
- `s/down` stops the Docker Compose stack (keeps containers/images).
  - `./s/down`
  - `./s/down --remove-orphans`
- `s/remove-containers-and-images` stops Docker Compose and removes local images.
  - `./s/remove-containers-and-images`
- `s/lint` runs a Markdown linter (PyMarkdown) in Docker.
  - `./s/lint` checks the default docs/spec paths.
  - `./s/lint docs/about/team.md` checks a specific file.
- `s/spellcheck` runs `codespell` in Docker.
  - `./s/spellcheck` checks the default docs/spec paths.
  - `./s/spellcheck docs/about/team.md` checks a specific file.
- `s/linkcheck` runs `mkdocs-linkcheck` in Docker.
  - `./s/linkcheck` builds the site then checks local links in `site/`.
  - `./s/linkcheck -r site` checks local + remote links.
  - `./s/linkcheck --help` shows available options.
- `s/build-pdf` produces the PDF version of the safety documentation.
