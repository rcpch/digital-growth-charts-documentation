# `s/`

The `s/` directory contains some simple convenience scripts to speed up and standardise working with this repository.

## Scripts

- `s/up` starts the local Zensical (documentation) server via Docker Compose.
  - `./s/up`
  - `./s/up -d` (detached)
- `s/down` stops the Docker Compose stack (keeps containers/images).
  - `./s/down`
  - `./s/down --remove-orphans`
- `s/remove-containers-and-images` stops Docker Compose and removes local images.
  - `./s/remove-containers-and-images`
- `s/markdownlint` runs a Markdown linter (PyMarkdown) in Docker.
  - `./s/markdownlint` checks the default docs/spec paths.
  - `./s/markdownlint docs/about/team.md` checks a specific file.
- `s/spellcheck` runs `codespell` in Docker.
  - `./s/spellcheck` checks the default docs/spec paths.
  - `./s/spellcheck docs/about/team.md` checks a specific file.
- `s/check-links` runs `mkdocs-linkcheck` in Docker.
  - `./s/check-links` builds the site then checks local links in `site/`.
  - `./s/check-links -r site` checks local + remote links.
  - `./s/check-links --help` shows available options.
