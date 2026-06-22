#!/usr/bin/env python3
"""Self-hosted PDF export for the Clinical Safety and Medical Device documentation.

Zensical does not yet provide a native PDF export (tracking
https://github.com/zensical/backlog/issues/25), and we only need to export the
safety documentation rather than the whole site. This script reimplements just
that slice: it reads the already-built HTML in ``site/``, extracts the rendered
content of each safety page, stitches them together with a cover page and a
print stylesheet, and renders a single PDF with WeasyPrint.

Run it AFTER ``zensical build`` so that ``site/`` exists. The local wrapper
``s/build-pdf`` does both steps for you, and the build-and-deploy workflow runs
it before uploading ``site/`` to Azure.

Usage:
    python pdf-export/build-safety-pdf.py [--site-dir site] [--output PATH]
"""

from __future__ import annotations

import argparse
import datetime as _dt
from pathlib import Path

from bs4 import BeautifulSoup
from weasyprint import HTML

# Pages to include, in reading order (mirrors the "Clinical Safety" nav order).
# Paths are relative to the built site directory and point at the page folder
# that contains the rendered ``index.html``.
#
# ``safety/download`` is deliberately excluded: it is the page that links to
# this very PDF, so including it would be circular.
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

DOCUMENT_TITLE = "RCPCH Digital Growth Charts"
DOCUMENT_SUBTITLE = "Clinical Safety and Medical Device Documentation"

REPO_ROOT = Path(__file__).resolve().parent.parent
PRINT_CSS = Path(__file__).resolve().parent / "print.css"
LOGO = REPO_ROOT / "docs" / "_assets" / "_images" / "rcpch_logo.png"


def _extract_article(page_dir: Path) -> str:
    """Return the cleaned inner HTML of a built page's main content article."""
    index_html = page_dir / "index.html"
    if not index_html.is_file():
        raise FileNotFoundError(f"Built page not found: {index_html}")

    soup = BeautifulSoup(index_html.read_text(encoding="utf-8"), "html.parser")
    article = soup.find("article", class_="md-content__inner")
    if article is None:
        raise ValueError(f"No content article found in {index_html}")

    # Strip elements that make no sense in a printed document.
    for headerlink in article.select("a.headerlink"):
        headerlink.decompose()
    for button in article.select("a.md-content__button"):
        button.decompose()

    # Resolve relative asset URLs (images) to absolute file paths so that
    # WeasyPrint can load them once the articles are merged into one document.
    for img in article.find_all("img"):
        src = img.get("src")
        if src and not src.startswith(("http://", "https://", "data:", "/")):
            resolved = (page_dir / src).resolve()
            img["src"] = resolved.as_uri()

    return article.decode_contents()


def _cover_page() -> str:
    today = _dt.date.today().strftime("%-d %B %Y")
    logo_html = (
        f'<img class="cover-logo" src="{LOGO.as_uri()}" alt="RCPCH logo">'
        if LOGO.is_file()
        else ""
    )
    return f"""
    <section class="cover">
      {logo_html}
      <h1 class="cover-title">{DOCUMENT_TITLE}</h1>
      <p class="cover-subtitle">{DOCUMENT_SUBTITLE}</p>
      <p class="cover-date">Generated {today}</p>
    </section>
    """


def build(site_dir: Path, output: Path) -> Path:
    sections: list[str] = [_cover_page()]
    for page in SAFETY_PAGES:
        content = _extract_article(site_dir / page)
        sections.append(f'<section class="page">{content}</section>')

    document = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        f"<title>{DOCUMENT_TITLE} - {DOCUMENT_SUBTITLE}</title></head>"
        f'<body class="md-typeset">{"".join(sections)}</body></html>'
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
        "--output",
        type=Path,
        default=REPO_ROOT / "site" / "_assets" / "_pdfs" / "safety-documentation.pdf",
        help="Output PDF path (default: site/_assets/_pdfs/safety-documentation.pdf)",
    )
    args = parser.parse_args()

    site_dir = args.site_dir.resolve()
    if not site_dir.is_dir():
        raise SystemExit(
            f"Built site not found at {site_dir}. Run 'zensical build' first."
        )

    output = build(site_dir, args.output.resolve())
    size_kb = output.stat().st_size / 1024
    print(f"Wrote {output} ({size_kb:.0f} KB) from {len(SAFETY_PAGES)} pages.")


if __name__ == "__main__":
    main()
