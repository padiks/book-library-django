## **Run Django with Apache (mod_wsgi) Instead of Gunicorn**

### **Step 1: Stop and disable Gunicorn service**

```bash
sudo systemctl stop library.service
sudo systemctl disable library.service
```

* **`stop`**: Immediately stops the running Gunicorn service.
* **`disable`**: Prevents it from starting automatically on boot.

Check status:

```bash
sudo systemctl status library.service
```

---

### **Step 2: Install Apache and mod_wsgi**

```bash
sudo apt update
sudo apt install apache2 libapache2-mod-wsgi-py3
```

* **Apache2**: Web server to serve your Django app.
* **mod_wsgi**: Apache module that allows Python apps (like Django) to run inside Apache.

Enable mod_wsgi:

```bash
sudo a2enmod wsgi
sudo systemctl restart apache2
```

---

### **Step 3: Prepare Django app for Apache**

1. **Collect static files**:

```bash
cd /path/to/your/project
python3 manage.py collectstatic
```

* Copies all static files (CSS, JS, images) to `STATIC_ROOT`.

2. **Check settings**:

```python
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
```

---

### **Step 4: Configure Apache Virtual Host**

Create `/etc/apache2/sites-available/library.conf` with this content:

```apache
<VirtualHost *:4000>
    ServerName 127.0.0.1

    Alias /static /path/to/your/project/static
    <Directory /path/to/your/project/static>
        Require all granted
    </Directory>

    <Directory /path/to/your/project/library>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess library python-path=/path/to/your/project python-home=/path/to/your/venv
    WSGIProcessGroup library
    WSGIScriptAlias / /path/to/your/project/library/wsgi.py
</VirtualHost>
```

* **`<VirtualHost *:4000>`** → Apache listens on port 4000.
* **`Alias /static`** → Serves static files.
* **`WSGIDaemonProcess`** → Runs Django in its own process using your virtualenv.
* **`WSGIScriptAlias`** → Points Apache to your `wsgi.py` file.

---

### **Step 5: Enable site and restart Apache**

```bash
sudo a2ensite library.conf
sudo systemctl restart apache2
```

---

### **Step 6: Test**

Open your browser:

```
http://127.0.0.1:4000/
```

Your Django app should load automatically without typing `runserver`.