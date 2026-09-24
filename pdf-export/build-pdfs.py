#!/usr/bin/env python3
"""Build the complete-site and controlled safety PDFs from rendered Zensical pages.

Zensical does not yet provide native PDF export (tracking
https://github.com/zensical/backlog/issues/25). This exporter reads the
already-built HTML in ``site/``, extracts each rendered article, and uses one
shared print stylesheet to create both downloadable documents.

Run it after ``zensical build``. The local ``s/build-pdf`` wrapper performs both
steps, and deployment runs the exporter before uploading ``site/`` to Azure.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import html
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urljoin

import yaml
from bs4 import BeautifulSoup
from weasyprint import HTML

# This controlled subset deliberately remains explicit. Adding the complete-site
# PDF must not silently change the reviewed scope of the safety PDF.
SAFETY_PAGES: list[str] = [
    "safety/overview",
    "safety/csmf/clinical-risk-mgmt-system",
    "safety/csmf/clinical-risk-mgmt-plan",
    "safety/csmf/clinical-safety-case-report",
    "safety/csmf/hazard-log",
    "safety/csmf/third-party-tools-safety-assmt",
    "safety/csmf/license",
    "safety/dtac",
    "safety/medical-device-reg/mhra",
    "safety/medical-device-reg/essential-req",
    "safety/medical-device-reg/doc-api",
    "safety/medical-device-reg/mdr-technical-docs",
]

# The homepage is an interactive custom template. Download pages are excluded to
# avoid embedding links to the document currently being generated.
FULL_SITE_EXCLUSIONS = {
    "index.md",
    "contact/downloads.md",
    "safety/download.md",
}

DOCUMENT_TITLE = "RCPCH Digital Growth Charts"
SITE_URL = "https://growth.rcpch.ac.uk/"

REPO_ROOT = Path(__file__).resolve().parent.parent
MKDOCS_CONFIG = REPO_ROOT / "mkdocs.yml"
PRINT_CSS = Path(__file__).resolve().parent / "print.css"
LOGO = REPO_ROOT / "docs" / "_assets" / "_images" / "rcpch_logo.png"


def _nav_source_pages(value: Any) -> list[str]:
    """Flatten Markdown source paths from the configured navigation tree."""
    if isinstance(value, str):
        return [value] if value.endswith(".md") else []
    if isinstance(value, list):
        return [page for item in value for page in _nav_source_pages(item)]
    if isinstance(value, dict):
        return [page for item in value.values() for page in _nav_source_pages(item)]
    return []


def _source_to_built_page(source: str) -> str:
    """Map a Markdown source path to its directory in the built site."""
    path = PurePosixPath(source)
    if path.name == "index.md":
        return path.parent.as_posix()
    return path.with_suffix("").as_posix()


def _full_site_pages() -> list[str]:
    """Return all navigated content pages in published reading order."""
    config = yaml.load(MKDOCS_CONFIG.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
    source_pages = _nav_source_pages(config.get("nav", []))
    return [
        _source_to_built_page(source)
        for source in source_pages
        if source not in FULL_SITE_EXCLUSIONS
    ]


def _published_page_url(page: str) -> str:
    suffix = f"{page.strip('/')}/" if page.strip("/") else ""
    return urljoin(SITE_URL, suffix)


def _extract_article(site_dir: Path, page: str) -> str:
    """Return print-safe article HTML from one rendered page."""
    page_dir = site_dir / page
    index_html = page_dir / "index.html"
    if not index_html.is_file():
        raise FileNotFoundError(f"Built page not found: {index_html}")

    soup = BeautifulSoup(index_html.read_text(encoding="utf-8"), "html.parser")
    article = soup.find("article", class_="md-content__inner")
    if article is None:
        raise ValueError(f"No content article found in {index_html}")

    for element in article.select("a.headerlink, a.md-content__button, script"):
        element.decompose()

    page_url = _published_page_url(page)
    for embedded in article.find_all(["iframe", "object"]):
        resource = embedded.get("src") or embedded.get("data")
        if resource:
            fallback = soup.new_tag("p", attrs={"class": "print-fallback"})
            link = soup.new_tag("a", href=urljoin(page_url, resource))
            link.string = "View this embedded content on the documentation site"
            fallback.append(link)
            embedded.replace_with(fallback)
        else:
            embedded.decompose()

    for details in article.find_all("details"):
        details["open"] = ""

    for image in article.find_all("img"):
        source = image.get("src")
        if not source or source.startswith(("http://", "https://", "data:")):
            continue
        resolved = site_dir / source.lstrip("/") if source.startswith("/") else page_dir / source
        if resolved.is_file():
            image["src"] = resolved.resolve().as_uri()
        else:
            image["src"] = urljoin(page_url, source)
        image.attrs.pop("srcset", None)

    for link in article.find_all("a"):
        target = link.get("href")
        if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:")):
            continue
        link["href"] = urljoin(page_url, target)

    return article.decode_contents()


def _cover_page(subtitle: str) -> str:
    today = _dt.date.today().strftime("%-d %B %Y")
    logo_html = (
        f'<img class="cover-logo" src="{LOGO.as_uri()}" alt="RCPCH logo">'
        if LOGO.is_file()
        else ""
    )
    return f"""
    <section class="cover">
      {logo_html}
      <h1 class="cover-title">{html.escape(DOCUMENT_TITLE)}</h1>
      <p class="cover-subtitle">{html.escape(subtitle)}</p>
      <p class="cover-date">Generated {today}</p>
    </section>
    """


def build_pdf(
    site_dir: Path,
    pages: list[str],
    subtitle: str,
    running_header: str,
    output: Path,
) -> Path:
    """Build one PDF from an ordered collection of rendered pages."""
    sections = [_cover_page(subtitle)]
    for page in pages:
        content = _extract_article(site_dir, page)
        sections.append(f'<section class="page">{content}</section>')

    document = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        f"<title>{html.escape(DOCUMENT_TITLE)} - {html.escape(subtitle)}</title></head>"
        '<body class="md-typeset">'
        f'<span class="document-header">{html.escape(running_header)}</span>'
        f'{"".join(sections)}</body></html>'
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=document, base_url=str(site_dir)).write_pdf(
        target=str(output),
        stylesheets=[str(PRINT_CSS)],
    )
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--site-dir",
        type=Path,
        default=REPO_ROOT / "site",
        help="Path to the built Zensical site (default: ./site)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="PDF output directory (default: SITE_DIR/_assets/_pdfs)",
    )
    args = parser.parse_args()

    site_dir = args.site_dir.resolve()
    if not site_dir.is_dir():
        raise SystemExit(
            f"Built site not found at {site_dir}. Run 'zensical build' first."
        )
    output_dir = (
        args.output_dir.resolve()
        if args.output_dir
        else site_dir / "_assets" / "_pdfs"
    )

    documents = [
        (
            SAFETY_PAGES,
            "Clinical Safety and Medical Device Documentation",
            "RCPCH Digital Growth Charts - Safety Documentation",
            output_dir / "safety-documentation.pdf",
        ),
        (
            _full_site_pages(),
            "Complete Documentation Manual",
            "RCPCH Digital Growth Charts - Complete Documentation",
            output_dir / "digital-growth-charts-documentation.pdf",
        ),
    ]

    for pages, subtitle, running_header, output in documents:
        built = build_pdf(site_dir, pages, subtitle, running_header, output)
        size_mb = built.stat().st_size / (1024 * 1024)
        print(f"Wrote {built} ({size_mb:.1f} MB) from {len(pages)} pages.")


if __name__ == "__main__":
    main()
