# Commands to setup Flask

## Install virtualenv
This is a tool to create isolated Python environments. It creates a folder which contains all the necessary executables to use the packages that a Python project would need.

```bash
pip install virtualenv
```

## Create a virtual environment
This command creates a folder named `env` which contains all the necessary executables to use the packages that a Python project would need.

```bash
virtualenv env
```

## Activate the virtual environment
This command activates the virtual environment.

```bash
.\env\Scripts\activate
```

## Install Flask
This command installs Flask and SQLAlchemy. Flask is a web framework and SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python.

```bash
pip install Flask flask-sqlalchemy
```

