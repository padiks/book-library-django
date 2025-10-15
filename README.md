# Book Library (Django)

This is a Django-based Book Library project. It organizes books, volumes, and chapters in Markdown format and uses Django templates for rendering.

## Project Structure

<pre>library/                    # Django project root
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
└── media/                  # Optional uploaded files</pre>

### Features

- Organizes books into volumes and chapters using Markdown.
- Reusable base templates for header, footer, and hero section.
- App templates for home page, book listing, chapters, search results, sitemap, and login.
- Static folder for CSS, JS, and images.
- Media folder for optional uploaded files.

### Requirements

- Python 3.x
- Django 5.x
- Optional: Markdown parsing library if rendering chapters dynamically.

### Usage

## Step 1 – Set up Python, virtual environment, and Django project

**a.** Check Python and pip versions:

```
python3 --version
pip3 --version
```

**b.** Update system and install Python if needed:

```
sudo apt update
sudo apt install python3 python3-pip -y
```

**c.** Create project folder:

```
mkdir ~/Public/web
cd ~/Public/web
mkdir library
cd library
```

**d.** Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

*Tip:* Always activate the environment before working on this project.

**e.** Install Django:

```
pip install django
django-admin --version
```

**f.** Start Django project in the current folder:

```
django-admin startproject library .
```

**g.** Run Django development server on port 4000:

```
python manage.py runserver 4000
```

After this, open `http://127.0.0.1:4000/` in your browser to see the default Django welcome page.

---

2. Create a virtual environment and activate it (from the main folder `library`):

```bash
# Create the virtual environment (only needed once)
python -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate

# (Optional) Install dependencies if not already installed
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Run the development server on port 4000:

```bash
python manage.py runserver 4000
```

5. Access the site in your browser:

```
http://127.0.0.1:4000/
```

6. Optional: Create a superuser to access the Django admin:

```bash
python manage.py createsuperuser
```

---

This `README.md` preserves all commands as plain text and code blocks, ready to upload to a private GitHub repository.

## License

This project is intended for private use and learning purposes.