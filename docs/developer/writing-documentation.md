---
title: Writing Documentation
reviewers: Dr Marcus Baw, Dr Anchit Chandran
audience: developers
tags:
  - Contributing
---

# Writing dGC Documentation

Where possible, we have tried to bring together **all** documentation relating to any aspect of the dGC project into this one Zensical site, published at [growth.rcpch.ac.uk](https://growth.rcpch.ac.uk)

## Zensical

The documentation for the Digital Growth Charts project is created using [Zensical](https://zensical.org/), a documentation framework built on MkDocs. It uses the classic variant, which provides a Material-like appearance with additional features.

## Adding or editing documentation

Mostly this just requires creating Markdown files in the `docs/` directory of the [documentation repository](https://github.com/rcpch/digital-growth-charts-documentation).

Use other pages within this repo to get ideas on the style and the features available such as emoji, icons, and admonitions (refer to the Zensical documentation for available extensions).

### Continuous Integration via GitHub Actions

Any changes to the `live` branch of the documentation repository trigger a [GitHub Action](https://github.com/rcpch/digital-growth-charts-documentation/blob/live/.github/workflows/ALL-BRANCHES-ALL-PRs-build-and-deploy-to-azure.yml). This runs Zensical in a temporary application container, builds the site from the Markdown source into a set of static HTML pages, and [publishes the site to Azure](https://growth.rcpch.ac.uk/), with a [backup in GitHub Pages](https://rcpch.github.io/digital-growth-charts-documentation/).

This occurs whether changes are made using online or local, offline editing methods.

!!! note "GitHub Branch Protection"

    Ensure you make Pull Requests to `prerelease`, or any other branch name of your choosing, but not `live`.

    We have enabled GitHub branch protection to `live` so changes cannot be made directly there but **must** be made through an intermediate branch, and then Pull Requested into `live`.

### Online editing of the Markdown

If you are new to Markdown editing, you can use GitHub's interface itself to edit online, by clicking the 'pencil' edit icon in the top right corner of any source code page. There are also external tools like [Prose.io](http://prose.io/) and [StackEdit](https://stackedit.io/) which give you a nice interface for editing MarkDown online, and will sync the changes with GitHub for you.

We will need to review your changes before they are merged into the `live` branch, so please make a Pull Request to the `prerelease` branch, or any other branch of your choosing, and we will review it and merge it into `live` when ready.

Once merged, the changes will be automatically deployed to the live site, and you can see them at [growth.rcpch.ac.uk](https://growth.rcpch.ac.uk).

### Using a text editor and editing locally

More experienced coders can `git clone` the repo and make changes offline on their local machine before pushing to the remote to either the `rcpch` organisation's remote, or their own fork. This allows you to run Zensical locally and preview the site as it will appear when pushed to `live`.

### Setting up a development environment for the dGC documentation site

For all platforms we recommend using the `docker compose` setup, which will run the Zensical site in a Docker container, so you don't need to install Python or Zensical locally. This is the easiest way to get started, and it isolates your local development environment from any conflicting dependencies.

#### Prerequisites

- [Docker](https://www.docker.com/get-started) installed and running on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed (this is included with Docker Desktop on Windows and Mac, but needs to be installed separately on Linux).
- [Git](https://git-scm.com/downloads) installed on your machine, to clone the repository.

#### Steps to set up the development environment

1. Clone the repository:

   ```console
   git clone https://github.com/rcpch/digital-growth-charts-documentation.git
   ```

2. Change into the cloned directory:

   ```console
   cd digital-growth-charts-documentation
   ```

3. Start the Zensical development server using Docker Compose:

   ```console
   docker compose up
   ```

### `git-committers` and `mkdocs-with-pdf` plugins

These plugins can add 10-15 seconds of build time to the site, so when developing locally, they are disabled by default. They are enabled by using environment variables, if you want to test that they work locally before pushing to the remote:

```console
export ENABLE_GIT_COMMITTERS=true; zensical serve
export ENABLE_PDF_EXPORT=true; zensical serve
```

You should always build the site at least once with both PDF export and Git Committers enabled, to ensure there are no issues, before pushing to the remote.

## Adding a new page

- Create a new Markdown file in a subfolder in the `docs` folder. There is now also a template to get you started, in `docs/_utilities/page-template.md`, which you would copy into your new page file.

!!! info
Because of the way we have set up the left sidebar navigation, new pages are **not** automatically added to the navigation.

    (This allows us to have pages which are work-in-progress, available on the live site for review, but not in the navigation, hence only those who have the link would easily find it)

    See the next section for how to add pages to the navigation.

### Adding navigation for the page

Add navigation by editing the `nav:` tree element in `mkdocs.yml`. Below is an excerpt from the `nav:` in this project. You can see how the top level Navbar headings `Home` and About `are` defined, and how the sidebar headings work. You can nest several levels deep, if needed.

```yaml
nav:
  - Home: "index.md"
  - About:
      - "about/about.md"
      - "about/overview.md"
```

By manually specifying the navigation in this way, we have control over the precise appearance of subfolder names (which are otherwise rendered in Title Case, but this doesn't work for acronyms). Also, we can customise the order of listing of sidebar headings, which would otherwise be ordered alphabetically.

### Page title in the navigation

The page title that will be displayed in the left sidebar navigation is set in the YAML front matter:

```yaml hl_lines="2"
---
title: Some Page Title
reviewers: Dr Reviewer
---
```

### Heading on the page

The heading that will be displayed on the page is set using the first `<h1>` heading (i.e. one hashtag `#`)

```markdown
# Heading, which can be different to the sidebar title
```

### Reviewers

Reviewers are encouraged to add their details to the `reviewers:` section of the YAML front matter, this enables us to evidence that each page has been reviewed by multiple members of the team.

```yaml hl_lines="3"
---
title: Some Page Title
reviewers: Dr Marcus Baw, Dr Simon Chapman, Other Reviewer ...
---
```

### Tags

Pages can be categorised with **tags** in the YAML front matter. Zensical renders these tags at the foot of the page and indexes them into the site search, giving readers an extra layer of discoverability on top of the navigation tree and full-text search.

```yaml hl_lines="4 5 6 7"
---
title: Some Page Title
reviewers: Dr Marcus Baw
tags:
  - API
  - Integration
---
```

To keep tags useful, please reuse the **controlled vocabulary** already in use across the docs rather than inventing new, one-off tags. The current vocabulary is:

`API`, `API Reference`, `Integration`, `SNOMED CT`, `Growth Charts`, `Growth References`, `Centiles`, `Date and Age Calculations`, `React`, `Python`, `Docker`, `Flutter`, `Command Line`, `Testing`, `Versioning`, `Contributing`, `Getting Started`, `FAQ`, `Clinical Safety`, `Hazards`, `Medical Device Regulation`, `DTAC`, `Data Protection`, `Privacy`, `Security`, `Licensing`, `Legal`, `Pricing`, `Research`, `Support`, `Team`, `Press and Awards`, `Videos`, `Overview`, `Deprecated`.

Aim for two to four tags per page that describe its **subject matter**. If a page genuinely needs a new tag, add it here too so the vocabulary stays consistent.

!!! note "Tag index page"

    Zensical does not yet support a generated tags *index/listing* page (a single page that lists every tag and its pages). When [that feature ships](https://github.com/zensical/backlog/issues/38) we can add a `tags.md` listing page.

## Markdown Linting and Spellchecking

We maintain consistent documentation quality through automated linting and spellchecking. All contributors should run these tools locally before submitting changes.

### Markdown Linting

Run markdown linting to check for style issues, broken links, and formatting problems:

```console
./s/lint
```

This runs [PyMarkdown](https://pymarkdownlnt.readthedocs.io/) with the ruleset defined in `.pymarkdown.yml`.

### Spellchecking

Run spellchecking to catch typos and ensure UK English spelling conventions (e.g. "colour", "centre" not "center"):

```console
./s/spellcheck
```

This runs [Codespell](https://github.com/codespell-project/codespell) with a `.codespellrc` configuration file. The tool uses UK English by default.

### Before pushing

Before submitting a Pull Request, ensure both tools pass without errors:

```console
./s/lint && ./s/spellcheck
```

If either tool reports issues, fix them in your editor and re-run.

## Publishing is automated

When you push new changes to ANY branch of this repo, or it you open a Pull Request, Azure will automatically build a version of the site for review. You need to visit [this Static Web App deployment resource on the Azure portal](https://portal.azure.com/#@rcpch.ac.uk/resource/subscriptions/99e313f5-79fe-4480-b867-8daf2800cf22/resourceGroups/RCPCH-Dev-API-Growth/providers/Microsoft.Web/staticSites/documentation-demo-static-site/environments) to see the URL of the deployment, as it depends on the branch name. To obtain Azure access contact Marcus Baw of the RCPCH developer team.

Therefore, you don't need to do `zensical build --clean` command manually or locally - it’s done for you if you push to branches or PRs on GitHub.

## Plugins

Zensical supports many MkDocs-compatible plugins. We already use some to extend the capabilities of Markdown, making the documentation look nicer and function better.
