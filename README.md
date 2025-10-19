# Book Library (Django)

This is a Django-based Book Library project. It organizes books, volumes, and chapters in Markdown format and uses Django templates for rendering.

### Features

- Organizes books into volumes and chapters using Markdown.
- Reusable base templates for header, footer, and hero section.
- App templates for home page, book listing, chapters, search results, sitemap, and login.
- Static folder for CSS, JS, and images.

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
django-admin startproject common .
```

**g.** Run Django development server on port 4000:

```
python manage.py runserver 4000
```

After this, open `http://127.0.0.1:4000/` in your browser to see the default Django welcome page.

