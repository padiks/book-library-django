# Run Django with Apache (mod_wsgi) Instead of Gunicorn

Quick setup to run your Django app with Apache, including file permissions and port configuration.

---

## **Step 1: Stop and disable Gunicorn**

```bash
sudo systemctl stop library.service      # Stop the running Gunicorn service immediately
sudo systemctl disable library.service   # Prevent Gunicorn from starting on boot
sudo systemctl status library.service    # Check if the service is stopped
```

---

## **Step 2: Install Apache and mod_wsgi**

```bash
sudo apt update                          # Update package lists
sudo apt install apache2 libapache2-mod-wsgi-py3  # Install Apache and WSGI module
sudo a2enmod wsgi                        # Enable WSGI module in Apache
sudo systemctl restart apache2           # Restart Apache to apply changes
```

---

## **Step 3: Collect static files**

```bash
cd /home/user/Public/web/library        # Go to your Django project
python3 manage.py collectstatic         # Collect all static files (CSS, JS, images)
```

*Static files will be placed in `STATIC_ROOT` for Apache to serve.*

---

## **Step 4: Configure Apache Virtual Host**

```bash
sudo nano /etc/apache2/sites-available/library.conf
```

Paste the following:

```apache
<VirtualHost *:4000>
    ServerName 127.0.0.1

    # Serve static files
    Alias /static /home/user/Public/web/library/static
    <Directory /home/user/Public/web/library/static>
        Require all granted
    </Directory>

    # Allow Apache to access Django wsgi.py
    <Directory /home/user/Public/web/library/common>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    # Run Django in a separate WSGI daemon process
    WSGIDaemonProcess library python-home=/home/user/Public/web/library/venv python-path=/home/user/Public/web/library
    WSGIProcessGroup library
    WSGIScriptAlias / /home/user/Public/web/library/common/wsgi.py
</VirtualHost>
```

*Explanation:*

* `*:4000` → Apache listens on port 4000
* `Alias /static` → Serves static files directly
* `WSGIDaemonProcess` → Runs Django in its own process with virtualenv
* `WSGIScriptAlias` → Points Apache to `wsgi.py`

---

## **Step 5: Configure Apache to listen on port 4000**

```bash
sudo nano /etc/apache2/ports.conf       # Add the line:
# Listen 4000
```

---

## **Step 6: Enable site and restart Apache**

```bash
sudo a2ensite library.conf              # Enable your site configuration
sudo systemctl restart apache2          # Restart Apache to apply changes
```

---

## **Step 7: Check Apache and logs**

```bash
sudo ss -tuln | grep 4000               # Verify Apache is listening on port 4000
sudo netstat -tuln | grep 4000          # Alternative check
sudo tail -n 20 /var/log/apache2/error.log  # View last 20 lines of Apache error log
```

---

## **Step 8: Set proper file permissions**

```bash
sudo chmod o+rx /home/user/Public/web            # Allow Apache to traverse home directory
sudo chmod o+rx /home/user/Public/web/library
sudo chmod -R o+rx /home/user/Public/web/library/static  # Static files readable by Apache

sudo chown -R user:www-data /home/user/Public/web/library  # Set user owner, Apache group

# Owner full access, group read+execute
sudo chmod -R 750 /home/user/Public/web/library

# Ensure all directories are searchable
find /home/user/Public/web/library -type d -exec chmod 750 {} \;

# Ensure all files are readable by group
find /home/user/Public/web/library -type f -exec chmod 640 {} \;
```

*Explanation:* Proper permissions allow Apache to read and serve your project safely.

---

## **Step 9: Test**

Open in your browser:

```
http://127.0.0.1:4000/
```

Your Django app should now load without `runserver` or Gunicorn.
