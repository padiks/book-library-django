## Project Structure

```
library/                    # Django project root
├── manage.py               # Django management script
├── db.sqlite3              # SQLite database
├── venv/                   # Python virtual environment
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
│
├── common/                 # Django app for the library
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project/app routing
│   ├── views.py            # Main controllers (home, book, chapter, search)
│   ├── app/                # App templates
│   │   ├── home.html
│   │   ├── book_index.html
│   │   ├── markdown_page.html
│   │   ├── search_results.html
│   │   ├── sitemap.html    # Still not available 
│   │   └── login.html      # Still not available
│   │
│   └── base/               # Header/footer templates
│       ├── header.html
│       ├── footer.html
│       └── hero.html
│
├── books/                  # Planned Markdown content (books/volume/chapter)
│   ├── <book_name>/
│   │   ├── volume-1/
│   │   │   ├── chapter-1.md
│   │   │   ├── chapter-2.md
│   │   │   └── ...
│   │   ├── volume-2/
│   │   │   └── ...
│   │   └── index.md        # Optional TOC for the book
│   └── ...
│
├── static/                 # Development static files (CSS/JS/images)
│   ├── css/
│   ├── js/
│   ├── img/
│   └── vendor/
│
├── staticfiles/            # Collected static files for Apache
│   ├── admin/
│   ├── css/
│   ├── js/
│   ├── img/
│   └── vendor/
│
└── media/                  # Optional uploaded files
```

---

### ✅ Notes

* `common/` → Django project/app files, templates, and views.
* `books/` → Planned structure for Markdown content (books/volumes/chapters).
* `static/` → Development static files (CSS/JS/images).
* `staticfiles/` → Collected static files (`collectstatic`) for Apache.
* `venv/` → Python virtual environment.
* `db.sqlite3` → SQLite database.
