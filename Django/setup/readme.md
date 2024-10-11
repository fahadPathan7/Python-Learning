# <div align='center'> Django Setup </div>

## Step 1: Install uv
```bash
pip install uv
```

- this is a package that allows us to run our Django server in a more efficient way.
- it is faster than pip.
- it does not require us to restart the server every time we make a change to our code.

## Step 2: Create a virtual environment
```bash
uv venv
```

- this will create a virtual environment in the current directory.
- it will also create a folder called `venv` which will contain all the necessary packages for our Django project.
- this is useful because it allows us to keep our project dependencies separate from the global dependencies.

## Step 3: Activate the virtual environment
```bash
. venv/Scrips/activate
```

- this will activate the virtual environment.
- this means that any packages we install will be installed in the `venv` folder.

## Step 4: Install Django
```bash
uv pip install Django
```

- this will install Django in the virtual environment.

## Step 5: Create a Django project
```bash
django-admin startproject myproject
```

- this will create a Django project called `myproject`.

## Step 6: Run the Django server
```bash
cd myproject
python manage.py runserver
```

- this will start the Django server.
- we can now access our Django project by going to `http://localhost:8000` in our browser. (default port)
- this will also create a database for our project. (sqlite3)

## Step 7: Create a Django app
```bash
python manage.py startapp myapp
```