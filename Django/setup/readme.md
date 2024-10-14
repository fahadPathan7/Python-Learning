# <div align='center'> 🪛 Django Setup </div>

## 📌 Table of Contents
- [ 🪛 Django Setup ](#--django-setup-)
  - [📌 Table of Contents](#-table-of-contents)
  - [📝 Note](#-note)
  - [👉 Step 1: Install uv](#-step-1-install-uv)
  - [👉 Step 2: Create a virtual environment](#-step-2-create-a-virtual-environment)
  - [👉 Step 3: Activate the virtual environment](#-step-3-activate-the-virtual-environment)
  - [👉 Step 4: Install Django](#-step-4-install-django)
  - [👉 Step 5: Create a Django project](#-step-5-create-a-django-project)
  - [👉 Step 6: Run the Django server](#-step-6-run-the-django-server)
  - [👉 Step 7: Create a Django app](#-step-7-create-a-django-app)
  - [👉 Step 8: Add static and templates directories](#-step-8-add-static-and-templates-directories)
  - [👉 Step 9: Install pip](#-step-9-install-pip)
  - [👉 Step 10: Add INTERNAL\_IPS](#-step-10-add-internal_ips)
  - [👉 Step 11: Install django-tailwind](#-step-11-install-django-tailwind)
  - [👉 Step 12: Tailwind init](#-step-12-tailwind-init)
  - [👉 Step 13: Setting the npm path](#-step-13-setting-the-npm-path)
  - [👉 Step 14: Install tailwindcss](#-step-14-install-tailwindcss)
  - [👉 Step 15: Start tailwindcss](#-step-15-start-tailwindcss)
  - [👉 Step 16: Migrate the database](#-step-16-migrate-the-database)
  - [👉 Step 17: Create a superuser](#-step-17-create-a-superuser)
  - [👉 Step 18: Install Pillow](#-step-18-install-pillow)
  - [👉 Step 19: Migrate Models](#-step-19-migrate-models)

## 📝 Note
- every command which includes `manage.py` should be run inside the project root directory where `manage.py` is located.
  ```bash
    .venv/Scrips/activate # activate the virtual environment
    cd myproject # myproject is the name of the project (manage.py should be in this directory)
    ```
- other commands should be run just after activating the virtual environment.
  ```bash
    .venv/Scrips/activate # activate the virtual environment
    ```
- `urls.py` and `settings.py` files are located inside the project folder. (not the app folder)
- to stop the server, press `ctrl + c` in the terminal.
- if you don't want to use tailwindcss, you can skip the steps 11 to 15.

## 👉 Step 1: Install uv
```bash
pip install uv
```

- this is a package that allows us to run our Django server in a more efficient way.
- it is comparatively faster than the default Django server.
- it does not require us to restart the server every time we make a change to our code.

## 👉 Step 2: Create a virtual environment
```bash
uv venv
```

- this will create a virtual environment in the current directory.
- it will also create a folder called `venv` which will contain all the necessary packages for our Django project.
- this is useful because it allows us to keep our project dependencies separate from the global dependencies.

## 👉 Step 3: Activate the virtual environment
```bash
. venv/Scrips/activate
```

- this will activate the virtual environment.
- this means that any packages we install will be installed in the `venv` folder.

## 👉 Step 4: Install Django
```bash
uv pip install Django
```

- this will install Django in the virtual environment.

## 👉 Step 5: Create a Django project
```bash
django-admin startproject myproject
```

- this will create a Django project called `myproject`.

## 👉 Step 6: Run the Django server
```bash
cd myproject
python manage.py runserver
```

- this will start the Django server.
- we can now access our Django project by going to `http://localhost:8000` in our browser. (default port)
- this will also create a database for our project. (sqlite3)

## 👉 Step 7: Create a Django app
```bash
python manage.py startapp myapp
```

- this will create a Django app called `myapp`.
- an app is a web application that does something - for example, a blog, a forum, or a photo gallery.
- an app can be reused in multiple projects.
- an app can contain models, views, templates, and static files.
- it needs to be added to the `INSTALLED_APPS` list in the `settings.py` file.
  ```python
    INSTALLED_APPS = [
        ...
        'myapp',
    ]
    ```

## 👉 Step 8: Add static and templates directories
- create a folder named `static` in the root directory of the project. (for css)
- create a folder named `templates` in the root directory of the project. (for html)
- add the following to the `settings.py` file.
    ```python
    STATIC_URL = 'static/' # for css
    STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ] # for css

    TEMPLATES = [
        {
            ...
            'DIRS': ['templates'], # for html
            ...
        },
    ]
    ```

## 👉 Step 9: Install pip
```bash
uv pip install pip
```

- this will install the `pip` package manager.
- it is used to install Python packages from the Python Package Index (PyPI).
- it is also used to manage dependencies in our Django project.

## 👉 Step 10: Add INTERNAL_IPS
- Add the following to the `settings.py` file.
    ```python
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
    ```

- this will allow us to see the `tailwindcss` live reload feature in action.
- it will also allow us to see the `debug_toolbar` in action.
- the `debug_toolbar` is a Django app that provides a set of tools for debugging our Django project.
- it is useful for inspecting the SQL queries that are executed by our project.
- it is also useful for inspecting the HTTP requests that are made by our project.

## 👉 Step 11: Install django-tailwind
```bash
uv pip install django-tailwind
uv pip install 'django-tailwind[reload]' # for live reload
```

- this will install the `django-tailwind` package which allows us to use the `tailwindcss` framework in our Django project.
- it provides a set of templates and components that we can use in our project.
- it needs to be added to the `INSTALLED_APPS` list in the `settings.py` file.
    ```python
    INSTALLED_APPS = [
        ...
        'tailwind',
        'django_browser_reload',
    ]
    ```
- it also needs to be added to the `MIDDLEWARE` list in the `settings.py` file.
    ```python
    MIDDLEWARE = [
        ...
        'django_browser_reload.middleware.BrowserReloadMiddleware',
    ]
    ```
- it also needs to be added in the urls.py file. (it always needs to be the last url pattern)
    ```python
    urlpatterns = [
        ...
        path('__reload__/', include('django_browser_reload.urls')),
    ]
    ```

## 👉 Step 12: Tailwind init
```bash
python manage.py tailwind init
```

- this will create an app called theme in our project.
- it will also create a `tailwind.config.js` file in the `theme` folder. (for customizing tailwindcss)
- it will also create a `postcss.config.js` file. (for processing CSS files)
- this also needs to be added to the `INSTALLED_APPS` list in the `settings.py` file.
  ```python
    INSTALLED_APPS = [
        ...
        'theme',
    ]
    ```
- Additionally, a variable `TAILWIND_APP_NAME` needs to be added to the `settings.py` file.
    ```python
    TAILWIND_APP_NAME = 'theme'
    ```

## 👉 Step 13: Setting the npm path
```python
NPM_BIN_PATH = 'C:/Program Files/nodejs/npm.cmd'
```

- Add the following to the `settings.py` file. (nodejs should be installed)
- this is required to install the `tailwindcss` package.

## 👉 Step 14: Install tailwindcss
```bash
python manage.py tailwind install
```

- this will install the `tailwindcss` package.
- it is a utility that allows us to use the `tailwindcss` framework in our Django project.
- it will create a folder named templates inside theme folder and there will be a file named base.html.
- we need to copy the blocks and add those to our layout html file. (layout file should extend base.html)

## 👉 Step 15: Start tailwindcss
```bash
python manage.py tailwind start
```

- this will start the `tailwindcss` server.
- need to run this in a separate terminal and keep it running.
- this will compile the `tailwindcss` files and watch for changes.

## 👉 Step 16: Migrate the database
```bash
python manage.py migrate
```

- this will create the necessary database tables for our Django project.

## 👉 Step 17: Create a superuser
```bash
python manage.py createsuperuser
```

- this will create a superuser for our Django project.
- a superuser is a user who has all the permissions in our Django project.
- we can use this user to log in to the Django admin interface.
- we can access the Django admin interface by going to `http://localhost:8000/admin` in our browser.

## 👉 Step 18: Install Pillow
```bash
uv pip install Pillow
```

- this will install the `Pillow` package.
- it is a Python Imaging Library (PIL) that allows us to work with images in our Django project.
- `settings.py` file needs to be updated for the media files.
    ```python
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```
- `urls.py` file needs to be updated for the media files.
    ```python
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

- this will allow us to upload images to our Django project.
- we can use the `ImageField` model field to store images in our database.

## 👉 Step 19: Migrate Models
```bash
# python manage.py makemigrations # this will create the necessary database tables for our project (all apps)
python manage.py makemigrations myapp # myapp is the name of the app (specific app. better approach)
python manage.py migrate # this will create the necessary database tables for our app
```

- this will create the necessary database tables for our Django project.
- it will also create the necessary database tables for our app.
- we will see a folder called `migrations` inside our app folder.
- Inside the `migrations` folder, there will be a file called `0001_initial.py`. This file contains the database schema for our app.
- These need to run every time we make changes to our models.

<hr>