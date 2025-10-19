import os
import re
from pathlib import Path
from django.shortcuts import render
from django.conf import settings
from django.utils.html import escape

# Base path to your markdown books
BASE_BOOKS_PATH = Path(settings.BASE_DIR) / "books"


def search_view(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        for root, _, files in os.walk(BASE_BOOKS_PATH):
            for filename in files:
                if filename.endswith('.md'):
                    file_path = Path(root) / filename
                    rel_path = file_path.relative_to(BASE_BOOKS_PATH)

                    try:
                        content = file_path.read_text(encoding="utf-8")
                    except Exception:
                        continue

                    # Search query (case-insensitive)
                    match = re.search(re.escape(query), content, re.IGNORECASE)
                    if match:
                        start = max(0, match.start() - 30)
                        snippet = content[start:start + 150]

                        # Remove Markdown symbols and HTML tags
                        snippet = re.sub(r'[>#*_`~\-]+', '', snippet)
                        snippet = re.sub(r'<[^>]+>', '', snippet)
                        snippet = escape(snippet)

                        parts = rel_path.parts
                        book = parts[0]
                        volume = os.path.splitext(parts[-1])[0]

                        # Construct URL similar to your book_index route
                        # e.g. /book/<book>/<volume>/<chapter>/
                        if len(parts) == 1:
                            url = f"/book/{book}/{volume}/"
                        else:
                            subpath = "/".join(parts[1:])
                            url = f"/book/{book}/{subpath.replace('.md','')}/"

                        results.append({
                            'path': str(rel_path),
                            'url': url,
                            'book': book,
                            'volume': volume,
                            'match_snippet': snippet + '...',
                        })

    context = {
        'query': query,
        'results': results,
    }

    # Render from common/app folder
    return render(request, 'search_results.html', context)
