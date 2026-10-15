# Practical 15 - Deploying a Flask / Django Web Application

## Option A: PythonAnywhere (free, easiest for students)
1. Create a free account at pythonanywhere.com.
2. **Files** tab -> upload this folder (or `git clone https://github.com/<you>/<repo>.git` from a Bash console).
3. Bash console:
   ```bash
   mkvirtualenv --python=python3.12 myenv
   pip install -r requirements.txt
   ```
4. **Web** tab -> *Add a new web app* -> *Manual configuration* -> Python 3.12.
5. Set **Source code** to the folder path, **Virtualenv** to `/home/<user>/.virtualenvs/myenv`.
6. Edit the **WSGI configuration file**:
   ```python
   import sys
   path = "/home/<user>/<repo>/WDP/p15_deployment"
   if path not in sys.path:
       sys.path.append(path)
   from app import app as application
   ```
7. In **Environment variables** (or the WSGI file) set `SECRET_KEY` to a long random string.
8. Click **Reload**. Site is live at `https://<user>.pythonanywhere.com`.

## Option B: Render.com (Gunicorn)
1. Push the repo to GitHub.
2. Render -> *New* -> *Web Service* -> connect the repo, root directory `WDP/p15_deployment`.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn wsgi:app`
5. Add environment variable `SECRET_KEY`. Deploy.

## Deploying Django (Practicals 10-14 project) - changes needed in `core/settings.py`
```python
import os
DEBUG = False
SECRET_KEY = os.environ["SECRET_KEY"]
ALLOWED_HOSTS = ["<user>.pythonanywhere.com"]       # or your domain
STATIC_ROOT = BASE_DIR / "staticfiles"
```
Then run:
```bash
pip install -r requirements.txt gunicorn
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
gunicorn core.wsgi:application          # start command on Render
```
On PythonAnywhere use `core/wsgi.py` in the WSGI file and map `/static/` to `STATIC_ROOT`.

## Pre-deployment checklist
- [ ] `DEBUG = False`
- [ ] Secret key in environment variable, not in Git
- [ ] `requirements.txt` up to date (`pip freeze`)
- [ ] `ALLOWED_HOSTS` set (Django)
- [ ] Database migrated / tables created
- [ ] `.gitignore` excludes `*.db`, `__pycache__`, `.env`

> Note: SQLite files on free hosts may reset on redeploy; use PostgreSQL for real projects.
