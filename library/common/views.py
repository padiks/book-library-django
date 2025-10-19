from django.shortcuts import render
from django.http import Http404
from pathlib import Path
from django.conf import settings
import markdown

BASE_BOOKS_PATH = Path(settings.BASE_DIR) / "books"


def home(request):
    """Homepage: list all books with dynamic title"""
    books = [b.name for b in BASE_BOOKS_PATH.iterdir() if b.is_dir()]
    return render(request, 'home.html', {
        'books': books,
        'title': 'Home',
    })


def book_index(request, book_name, subpath=None):
    """
    Handles all routes:
      - /book/<book_name>/
      - /book/<book_name>/<volume>/
      - /book/<book_name>/<volume>/<chapter>/
      - /book/<book_name>/<chapter>/
    Auto-detects folder vs. .md file and builds dynamic title.
    """
    current_path = BASE_BOOKS_PATH / book_name
    if subpath:
        current_path = current_path / subpath

    if not current_path.exists():
        # Try treating as .md file if user omitted suffix
        md_candidate = current_path.with_suffix(".md")
        if md_candidate.exists():
            current_path = md_candidate
        else:
            raise Http404("Book or folder not found")

    # ── Case 1: Direct .md file ─────────────────────────────
    if current_path.is_file() and current_path.suffix == ".md":
        html = markdown.markdown(
            current_path.read_text(encoding="utf-8"),
            extensions=["nl2br"]  # <-- Enables automatic line breaks
        )

        # Auto-title: Book / Volume / Chapter
        title_parts = [book_name.replace('-', ' ').title()]
        if subpath:
            for part in Path(subpath).parts:
                title_parts.append(part.replace('-', ' ').title())
        title = " / ".join(title_parts)

        return render(request, "markdown_page.html", {
            "book": book_name,
            "subpath": subpath,
            "content": html,
            "title": title,
        })

    # ── Case 2: Folder ──────────────────────────────────────
    folder_index = current_path / "folder_index.html"
    readme = current_path / "README.md"
    index_md = current_path / "index.md"

    if folder_index.exists():
        html = folder_index.read_text(encoding="utf-8")
    elif readme.exists():
        html = markdown.markdown(
            readme.read_text(encoding="utf-8"),
            extensions=["nl2br"]  # <-- Enables automatic line breaks
        )
    elif index_md.exists():
        html = markdown.markdown(
            index_md.read_text(encoding="utf-8"),
            extensions=["nl2br"]  # <-- Enables automatic line breaks
        )
    else:
        html = "<p>No description available.</p>"

    # List subfolders and .md files
    volumes = sorted([p.name for p in current_path.iterdir() if p.is_dir()])
    chapters = sorted([
        p.stem for p in current_path.glob("*.md")
        if p.name not in ("README.md", "index.md")
    ])

    # Auto-title: Book / Volume
    title_parts = [book_name.replace('-', ' ').title()]
    if subpath:
        for part in Path(subpath).parts:
            title_parts.append(part.replace('-', ' ').title())
    title = " / ".join(title_parts)

    return render(request, "book_index.html", {
        "book": book_name,
        "subpath": subpath,
        "content": html,
        "volumes": volumes,
        "chapters": chapters,
        "title": title,
    })


def handler404(request, exception):
    """Fallback 404 page using book_index template"""
    return render(request, "book_index.html", {
        "title": "Page Not Found",
        "content": "<p>Page not found.</p>",
        "volumes": [],
        "chapters": [],
    }, status=404)
