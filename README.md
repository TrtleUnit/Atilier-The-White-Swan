# Atelier The White Swan

Django + PostgreSQL website.

Open a terminal **in the project folder** (where `manage.py` is), then pick your system:
[Windows](#windows) · [Linux](#linux)

---

## Windows

### 1. Check the tools
```powershell
python --version
```
Needs **3.12 or newer**. Not installed? Get it from https://www.python.org/downloads/ and tick **"Add python.exe to PATH"**.

**PostgreSQL:** if it's not installed, get it from https://www.postgresql.org/download/windows/.
Remember the password you set for `postgres` and keep port `5432`.

### 2. Create the database
Open **"SQL Shell (psql)"** from the Start menu. Press **Enter** four times to accept the defaults, then type your `postgres` password.
```sql
CREATE USER admin WITH PASSWORD 'admin';
CREATE DATABASE atelier_db OWNER admin;
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET timezone TO 'UTC';
\q
```

### 3. Virtual environment and packages
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
> **"running scripts is disabled"?** Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then activate again.

### 4. Settings file
```powershell
copy .env.example .env
```
Fill in `.env`:
```
DB_NAME=atelier_db
DB_USER=admin
DB_PASSWORD=admin
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run
```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000 and http://127.0.0.1:8000/admin

### Daily
```powershell
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

---

## Linux
(Ubuntu / Debian / WSL)

### 1. Install the tools
```bash
sudo apt update
sudo apt install python3 python3-venv postgresql postgresql-contrib
sudo service postgresql start
```

### 2. Create the database
```bash
sudo -u postgres psql
```
```sql
CREATE USER admin WITH PASSWORD 'admin';
CREATE DATABASE atelier_db OWNER admin;
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET timezone TO 'UTC';
\q
```

### 3. Virtual environment and packages
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Settings file
```bash
cp .env.example .env
```
Fill in `.env`:
```
DB_NAME=atelier_db
DB_USER=admin
DB_PASSWORD=admin
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000 and http://127.0.0.1:8000/admin

### Daily
```bash
source venv/bin/activate
sudo service postgresql start
python manage.py runserver
```

---

## Team rules

| When you... | Do this |
|---|---|
| Pull new code | `pip install -r requirements.txt` then `python manage.py migrate` |
| Install a package | `pip freeze > requirements.txt` and commit it |
| Change a model | `python manage.py makemigrations` and commit the migration files |
| Commit | Never commit `.env` or `venv/` |

## Problems?

| Error | Fix |
|---|---|
| `connection refused` | PostgreSQL isn't running. Linux: `sudo service postgresql start`. Windows: **Services** → `postgresql-x64-…` → Start |
| `password authentication failed` | The `.env` password doesn't match `CREATE USER` |
| `No module named 'django'` | The venv isn't active |
| `python` not found (Windows) | Use `py` instead of `python` |
