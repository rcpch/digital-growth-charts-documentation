# `s/`

The `s/` directory contains some simple convenience scripts to speed up and standardise working with this repository.

## Scripts

- `s/up` starts the local MkDocs server via Docker Compose.
	- `./s/up`
- `s/down` stops the Docker Compose stack (keeps containers/images).
	- `./s/down`
- `s/remove-containers-and-images` stops Docker Compose and removes local images.
	- `./s/remove-containers-and-images`
- `s/spellcheck` runs `codespell` in Docker.
	- `./s/spellcheck` checks the default docs/spec paths.
	- `./s/spellcheck docs/about/team.md` checks a specific file.