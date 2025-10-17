from django.shortcuts import render
from django.http import Http404
from pathlib import Path
import markdown
from django.conf import settings

BASE_BOOKS_PATH = Path(settings.BASE_DIR) / "books"


def home(request):
    """Homepage: list all books"""
    books = [b.name for b in BASE_BOOKS_PATH.iterdir() if b.is_dir()]
    return render(request, 'home.html', {'books': books})


def book_index(request, book_name, subpath=None):
    """
    One route that handles:
      - /book/<book_name>/
      - /book/<book_name>/<volume>/
      - /book/<book_name>/<volume>/<chapter>/
      - /book/<book_name>/<chapter>/
    Detects automatically if it's a folder or .md file.
    """
    current_path = BASE_BOOKS_PATH / book_name
    if subpath:
        current_path = current_path / subpath

    if not current_path.exists():
        # Maybe user requested without trailing slash for an .md file name
        md_candidate = current_path.with_suffix(".md")
        if md_candidate.exists():
            current_path = md_candidate
        else:
            raise Http404("Book or folder not found")

    # ── Case 1: Direct .md file ─────────────────────────────
    if current_path.is_file() and current_path.suffix == ".md":
        html = markdown.markdown(current_path.read_text(encoding="utf-8"))
        return render(request, "chapter.html", {
            "content": html,
            "book": book_name,
            "subpath": subpath,
        })

    # ── Case 2: Folder ──────────────────────────────────────
    folder_index = current_path / "folder_index.html"
    readme = current_path / "README.md"
    index_md = current_path / "index.md"

    if folder_index.exists():
        html = folder_index.read_text(encoding="utf-8")
    elif readme.exists():
        html = markdown.markdown(readme.read_text(encoding="utf-8"))
    elif index_md.exists():
        html = markdown.markdown(index_md.read_text(encoding="utf-8"))
    else:
        html = "<p>No description available.</p>"

    # Build folder + .md file listings
    volumes = sorted([p.name for p in current_path.iterdir() if p.is_dir()])
    mdfiles = sorted([
        p.stem for p in current_path.glob("*.md")
        if p.name not in ("README.md", "index.md")
    ])

    return render(request, "book_index.html", {
        "book": book_name,
        "subpath": subpath,
        "content": html,
        "volumes": volumes,
        "chapters": mdfiles,
    })


def handler404(request, exception):
    return render(request, "404.html", status=404)
