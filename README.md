# Book Library (Django)

This is a Django-based Book Library project. It organizes books, volumes, and chapters in Markdown format and uses Django templates for rendering.

## Project Structure

library/                    # Django project root
├── manage.py               # Django management script
├── library/                # Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py             # Project-level routing
│   └── wsgi.py
│
├── books/                  # Markdown content (books/volume/chapter)
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
├── library/                # Django app for the library
│   ├── __init__.py
│   ├── admin.py            # Optional admin
│   ├── apps.py
│   ├── models.py           # Optional DB models
│   ├── views.py            # Main controllers (home, book, chapter, search)
│   ├── urls.py             # App-specific routing
│   ├── forms.py            # Optional search/login forms
│   ├── helpers.py          # Markdown parser utility
│   └── templates/
│       ├── base/           # Header/footer templates
│       │   ├── header.html
│       │   ├── footer.html
│       │   └── hero.html
│       │
│       ├── app/            # App templates
│       │   ├── home.html
│       │   ├── book_index.html    # Lists volumes/chapters
│       │   ├── chapter.html       # Render Markdown chapter
│       │   ├── search_results.html
│       │   ├── sitemap.html
│       │   └── login.html
│       │
│       └── static/         # About, Help, etc.
│           └── file1.html
│
├── static/                 # Global CSS/JS/images
│   ├── css/
│   ├── js/
│   ├── vendor/
│   └── img/
│
└── media/                  # Optional uploaded files

## Features

- Organizes books into volumes and chapters using Markdown.
- Reusable base templates for header, footer, and hero section.
- App templates for home page, book listing, chapters, search results, sitemap, and login.
- Static folder for CSS, JS, and images.
- Media folder for optional uploaded files.

## Requirements

- Python 3.x
- Django 5.x
- Optional: Markdown parsing library if rendering chapters dynamically.

## Usage

1. Clone the repository.
2. Create a virtual environment and install dependencies.
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver 4000
   ```
5. Open your browser at `http://127.0.0.1:4000/`.
6. Access the Django admin at `http://127.0.0.1:4000/admin/`.

## License

This project is intended for private use and learning purposes.