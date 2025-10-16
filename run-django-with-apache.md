# Run Django with Apache (mod_wsgi) Instead of Gunicorn

Quick setup to run your Django app with Apache, including static files, database permissions, and port configuration.

---

## **Step 1: Stop and disable Gunicorn**

```bash
sudo systemctl stop library.service      # Stop the running Gunicorn service immediately
sudo systemctl disable library.service   # Prevent Gunicorn from starting on boot
sudo systemctl status library.service    # Check the current status of Gunicorn
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

## **Step 3: Configure Apache Virtual Host**

```bash
sudo nano /etc/apache2/sites-available/library.conf
```

Paste the following:

```apache
<VirtualHost *:4000>
    ServerName 127.0.0.1

    # Serve collected static files
    Alias /static /home/user/Public/web/library/staticfiles
    <Directory /home/user/Public/web/library/staticfiles>
        Require all granted
    </Directory>

    # Allow Apache to access Django wsgi.py
    <Directory /home/user/Public/web/library/common>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    # Run Django in its own WSGI daemon process
    WSGIDaemonProcess library python-home=/home/user/Public/web/library/venv python-path=/home/user/Public/web/library
    WSGIProcessGroup library
    WSGIScriptAlias / /home/user/Public/web/library/common/wsgi.py
</VirtualHost>
```

*Explanation:*

* `*:4000` → Apache listens on port 4000
* `Alias /static` → Serves static files from `staticfiles`
* `WSGIDaemonProcess` → Runs Django in a separate process using your virtual environment
* `WSGIScriptAlias` → Points Apache to your `wsgi.py` file

---

## **Step 4: Collect static files**

```bash
cd /home/user/Public/web/library
source venv/bin/activate                  # Activate your virtual environment
python3 manage.py collectstatic           # Copy all static files to STATIC_ROOT
```

---

## **Step 5: Set static file permissions**

```bash
sudo chown -R user:www-data /home/user/Public/web/library/staticfiles  # Apache can read static files
sudo chmod -R 755 /home/user/Public/web/library/staticfiles            # Ensure read + execute access
```

---

## **Step 6: Enable site and restart Apache**

```bash
sudo a2ensite library.conf              # Enable your site configuration
sudo systemctl restart apache2          # Restart Apache to apply changes
```

---

## **Step 7: Configure Apache ports**

```bash
sudo nano /etc/apache2/ports.conf       # Add the line:
# Listen 4000
```

Then reload site:

```bash
sudo a2ensite library.conf
sudo systemctl restart apache2
```

---

## **Step 8: Verify Apache**

```bash
sudo ss -tuln | grep 4000               # Verify Apache is listening on port 4000
sudo netstat -tuln | grep 4000          # Alternative check
sudo tail -n 20 /var/log/apache2/error.log  # View last 20 lines of Apache error log
```

Check VirtualHost configuration:

```
*:8080                 debian.workgroup (/etc/apache2/sites-enabled/000-default.conf:1)
*:4000                 127.0.0.1 (/etc/apache2/sites-enabled/library.conf:1)
```

---

## **Step 9: Set project file permissions**

```bash
# Allow Apache to traverse home and project directories
sudo chmod o+rx /home/user
sudo chmod o+rx /home/user/Public
sudo chmod o+rx /home/user/Public/web
sudo chmod o+rx /home/user/Public/web/library

# Ensure source static files readable by Apache
sudo chmod -R o+rx /home/user/Public/web/library/static

# Set project ownership: user as owner, Apache group
sudo chown -R user:www-data /home/user/Public/web/library

# Set directory permissions: owner full, group read+execute
sudo chmod -R 750 /home/user/Public/web/library

# Ensure all directories are searchable
find /home/user/Public/web/library -type d -exec chmod 750 {} \;

# Ensure files are readable by group
find /home/user/Public/web/library -type f -exec chmod 640 {} \;

# Admin static & database adjustments
sudo chown -R user:www-data /home/user/Public/web/library/static
sudo chmod -R 755 /home/user/Public/web/library/static
sudo chown -R user:www-data /home/user/Public/web/library
find /home/user/Public/web/library -type d -exec chmod 775 {} \;
find /home/user/Public/web/library -type f -exec chmod 664 {} \;
sudo chmod -R 755 /home/user/Public/web/library/static
sudo chmod 664 /home/user/Public/web/library/db.sqlite3

sudo systemctl restart apache2          # Apply all permission changes
```

*Explanation:* Proper permissions allow Apache to read static files, access the database, and serve the Django app securely.

---

## **Step 10: Test**

Open in your browser:

```
http://127.0.0.1:4000/
```

Your Django app should now load **fully styled** with working admin CSS/JS, without using `runserver` or Gunicorn.

Do you want me to do that?
