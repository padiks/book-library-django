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

---

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

### License

This project is intended for private use and learning purposes.

## Usage

### Step 1 – Set up Python, virtual environment, and Django project

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

### Step 2 – Create Django app, templates, and Python code

**a.** Activate your virtual environment:

```bash
cd ~/Public/web/library
source venv/bin/activate
```

**b.** Create a Django app called `library`:

```bash
python manage.py startapp library
```

**c.** Add the app to `INSTALLED_APPS` in `library/settings.py`:

```python
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library',  # our app
]
```

**d.** Create folders for templates inside the app:

```bash
mkdir -p library/templates/base
mkdir -p library/templates/app
```

**e.** Create simple Bootstrap templates:

**`library/templates/base/header.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}Library{% endblock %}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="{% url 'home' %}">Raito Noberu Toshokan</a>
</nav>
<div class="container mt-4">
```

**`library/templates/base/footer.html`**

```html
</div>
<footer class="bg-light text-center py-3 mt-4">
  &copy; 2025 Raito Noberu Toshokan. All Rights Reserved.
</footer>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**`library/templates/app/home.html`**

```html
{% include 'base/header.html' %}
<h2 class="title">Welcome to Raito Noberu Toshokan</h2>
<p>This is the home page. List of books will go here.</p>
{% include 'base/footer.html' %}
```

**f.** Create the home view in `library/views.py`:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')
```

**g.** Set up `library/urls.py` for the app:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

**h.** Include app URLs in the project `library/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
]
```

**i.** Run the development server to test:

```bash
python manage.py runserver 4000
```

Open your browser at `http://127.0.0.1:4000/` to see the home page with header and footer.

---

### Step 3 – Set up Django webserver with Gunicorn and systemd

**a.** Update system and install required packages:

```
sudo apt update
sudo apt install python3-venv python3-pip python3-dev build-essential libpq-dev nginx -y
```

**b.** Activate your virtual environment in the project folder:

```
cd /home/user/Public/web/library
source venv/bin/activate
```

**c.** Install Gunicorn:

```
pip install gunicorn
```

**d.** Test Gunicorn locally:

```
gunicorn --bind 0.0.0.0:4000 library.wsgi
```

**e.** Create a systemd service file for Gunicorn:

```
sudo nano /etc/systemd/system/library.service
```

**f.** Add the following content inside the service file (replace `user` with your username):

```
[Unit]
Description=Gunicorn instance to serve Django library
After=network.target

[Service]
User=user
Group=www-data
WorkingDirectory=/home/user/Public/web/library
Environment="PATH=/home/user/Public/web/library/venv/bin"
ExecStart=/home/user/Public/web/library/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:4000 library.wsgi:application

[Install]
WantedBy=multi-user.target
```

**g.** Reload systemd and start the service:

```
sudo systemctl daemon-reload
sudo systemctl start library
sudo systemctl enable library
```

**h.** Check the status of the service:

```
sudo systemctl status library
```

**i.** Verify that Gunicorn is listening on port 4000:

```
sudo lsof -i -P -n | grep LISTEN
```

---
