# <div align='center'> 🔦 Flask and SQLAlchemy Overview </div>

## 📑 Table of Contents
- [ 🔦 Flask and SQLAlchemy Overview ](#--flask-and-sqlalchemy-overview-)
  - [📑 Table of Contents](#-table-of-contents)
  - [🪶 Flask](#-flask)
  - [🪶 SQLAlchemy](#-sqlalchemy)
  - [🪶 Imports](#-imports)
  - [🪶 Create an instance of the Flask class](#-create-an-instance-of-the-flask-class)
  - [🪶 Configure the database](#-configure-the-database)
  - [🪶 Create an instance of the SQLAlchemy class](#-create-an-instance-of-the-sqlalchemy-class)
  - [🪶 Define a model](#-define-a-model)
  - [🪶 Create the database tables](#-create-the-database-tables)
  - [🪶 Define a route](#-define-a-route)
  - [🪶 SQLAlchemy Commands](#-sqlalchemy-commands)
<hr>
<br><br>

## 🪶 Flask
Flask is a web framework written in Python. It is based on the Werkzeug WSGI toolkit and Jinja2 template engine. It is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. WSGI stands for Web Server Gateway Interface. It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.

<br><br>

## 🪶 SQLAlchemy
SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language. With this, we can interact with several databases like SQLite, PostgreSQL, MySQL, etc.

<br><br>

## 🪶 Imports
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
```

- `Flask` is the class that we use to create an application object.
- `render_template` is a function that we use to render HTML templates.
- `request` is an object that encapsulates the contents of a request sent to the server.
- `redirect` is a function that we use to redirect the user to another endpoint.
- `url_for` is a function that generates a URL to the given endpoint.
- `SQLAlchemy` is a library that facilitates the communication between Python programs and databases. It is an Object-Relational Mapping (ORM) library.

<br><br>

## 🪶 Create an instance of the Flask class
```python
app = Flask(__name__)
```

- `__name__` is a special variable in Python that is used to determine whether the script is being run standalone or being imported as a module.
- If the script is being run standalone, `__name__` is set to `'__main__'`. If the script is being imported as a module, `__name__` is set to the name of the module.
- By passing `__name__` to the `Flask` class, we are telling Flask to use the current module as the application package.
- This is necessary so that Flask knows where to look for templates, static files, and other resources.
- The `app` object is an instance of the `Flask` class. It is the central object of the application.
- We use it to configure the application, define routes, and handle requests.
- The `app` object is the WSGI application.

<br><br>

## 🪶 Configure the database
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # Database URI (SQLite)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database' # Database URI (PostgreSQL)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/database' # Database URI (MySQL)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Disable tracking modifications
```

- We configure the database by setting the `SQLALCHEMY_DATABASE_URI` and `SQLALCHEMY_TRACK_MODIFICATIONS` configuration options.
- The `SQLALCHEMY_DATABASE_URI` option specifies the URI of the database.
- In this case, we are using SQLite as the database. The URI `sqlite:///database.db` specifies that the database is located in the file `database.db` in the current directory. If the file does not exist, it will be created automatically.
- We can also use other databases like PostgreSQL and MySQL by changing the URI accordingly.
- The `SQLALCHEMY_TRACK_MODIFICATIONS` option specifies whether to track modifications to objects and emit signals. We set it to `False` to disable this feature.
- If it is set to `True`, SQLAlchemy will emit a `before_insert`, `before_update`, and `before_delete` event for every object that is modified.
- This can be useful for debugging, but it can also have a performance impact, especially in large applications.

<br><br>

## 🪶 Create an instance of the SQLAlchemy class
```python
db = SQLAlchemy(app)
```

- We create an instance of the `SQLAlchemy` class and pass the `app` object to it.
- This creates a database session that we can use to interact with the database.
- The `db` object is an instance of the `SQLAlchemy` class. It is the central object for interacting with the database.
- We use it to define models, create tables, and perform database operations.

<br><br>

## 🪶 Define a model
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

- We define a model by creating a class that inherits from the `db.Model` class.
- The class represents a table in the database.
- Each attribute of the class represents a column in the table.
- The `id` attribute is a primary key column that uniquely identifies each row in the table.
- The `name` attribute is a string column that stores the name of the user. It is required and cannot be null.
- The `email` attribute is a string column that stores the email address of the user. It is unique and cannot be null.

<br>

**All Attributes:**
- `db.Integer` is an integer column.
- `db.String(80)` is a string column with a maximum length of 80 characters. If longer data is provided, it will be truncated.
- `primary_key=True` specifies that the column is a primary key. A primary key uniquely identifies each row in the table.
- `db.ForeignKey('table.column')` specifies that the column is a foreign key that references the specified column in the specified table.
    ```bash
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # user_id is a foreign key
        # that references the id column in the User table.
    ```
- `nullable=False` specifies that the column cannot be null. It is required to have a value.
- `unique=True` specifies that the column must have a unique value. No two rows can have the same value for this column. (primary key is always unique)
- `default='default value'` specifies a default value for the column. If no value is provided, the default value will be used.
- `index=True` specifies that an index should be created for the column. This can improve query performance for columns that are frequently searched or sorted.
    ```python
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        __table_args__ = (
            db.Index('idx_name_email', 'name', 'email'), # Create an index on the name and email columns.
        )

    # Create an index on the name and email columns. (Alternative way)
    index = db.Index('idx_name_email', User.name, User.email) # Create an index on the name and email columns.
    ```

<br><br>

## 🪶 Create the database tables
```python
db.create_all()
```

- We create the database tables by calling the `create_all()` method on the `db` object.
- This method creates all the tables that have been defined as models.
- If the tables already exist, this method will not modify them.
- If a table does not exist, it will be created.
- This method should be called after all the models have been defined.
- It is typically called in the main script of the application.

<br><br>

## 🪶 Define a route
```python
# Route without a parameter. The route is specified as a string.
@app.route('/')
def index():
    return render_template('index.html')

# Route with a parameter. The parameter is passed to the function as an argument.
@app.route('/users/<int:id>')
def user(id):
    user = User.query.get(id) # Get the user with the specified id.
    return render_template('user.html', user=user) # Render the user.html template with the user object.

# Route with methods. The route can handle GET and POST requests. The request method is checked using request.method.
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST': # Check if the request method is POST.
        name = request.form['name'] # Get the value of the name field from the form. `name` is name of the input field.
        email = request.form['email'] # Get the value of the email field from the form. `email` is name of the input field.
        user = User(name=name, email=email) # Create a new user object with the provided name and email.
        db.session.add(user) # Add the user object to the session.
        db.session.commit() # Commit the session to the database.
        return redirect(url_for('users')) # Redirect the user to the users route.
    else:
        users = User.query.all() # Get all the users from the database.
        return render_template('users.html', users=users) # Render the users.html template with the users object.
```

```html
<!-- this form is used to submit the user data to the server -->
<form method="POST" action="/users">
    <input type="text" name="name" placeholder="Name">
    <input type="email" name="email" placeholder="Email">
    <button type="submit">Submit</button>
</form>
```

- We define routes by using the `@app.route()` decorator.
- The decorator specifies the URL path that the route should respond to.
- The route is specified as a string. For example, `'/'` specifies the root URL, and `'/users/<int:id>'` specifies a URL with a parameter.
- The parameter is passed to the function as an argument. For example, `def user(id):` receives the `id` parameter.
- The function returns a response that is sent back to the client. For example, `return render_template('index.html')` renders the `index.html` template.
- The `render_template()` function is used to render HTML templates. It takes the name of the template as an argument.
- The `request` object is used to access the contents of the request sent to the server. For example, `request.form['name']` gets the value of the `name` field from a form submitted via POST.
  ```html
    <form method="POST" action="/users">
        <input type="text" name="name" placeholder="Name">
        <input type="email" name="email" placeholder="Email">
        <button type="submit">Submit</button>
    </form>
    ```
- The `redirect()` function is used to redirect the user to another endpoint. For example, `return redirect(url_for('users'))` redirects the user to the `users` route. Here, the page is redirected to the same route after adding a new user. This is done to display the updated list of users.

<br><br>

## 🪶 Run the server
```python
if __name__ == '__main__':
    app.run(debug=True)
```

- We run the application by calling the `run()` method on the `app` object.
- The `debug=True` option enables the debug mode. In debug mode, the server will reload itself on code changes and provide a helpful debugger in case of errors.
- The `if __name__ == '__main__':` block ensures that the server is only started if the script is run standalone, not if it is imported as a module.
- This is necessary to prevent the server from starting multiple times if the script is imported by other scripts.
- The server listens on port 5000 by default. We can change the port by passing the `port` argument to the `run()` method.
    ```python
    app.run(debug=True, port=8000) # Run the server on port 8000.
    ```
- The server listens on all network interfaces by default. We can change the host by passing the `host` argument to the `run()` method.
    ```python
    app.run(debug=True, host='0.0.0.0') # Run the server on all network interfaces.
    # app.run(debug=True, host='hostname') # Run the server on the specified hostname.
    ```

<br><br>

## 🪶 SQLAlchemy Commands
- **Create a new record:**
  ```python
    user = User(name='Alice', email='alice@gmail.com') # Create a new user object.
    db.session.add(user) # Add the user object to the session.
    db.session.commit() # Commit the session to the database.
    ```
- **Update an existing record:**
  ```python
    user = User.query.get(1) # Get the user with the specified id.
    user.name = 'Bob' # Update the name of the user.
    db.session.commit() # Commit the session to the database.
    ```
- **Delete an existing record:**
    ```python
        user = User.query.get(1) # Get the user with the specified id.
        db.session.delete(user) # Delete the user object from the session.
        db.session.commit() # Commit the session to the database.
        ```
- **Query records:**
    - **Get all records:**
        ```python
        users = User.query.all() # Get all the users from the database.
        ```
    - **Get a record by id:**
        ```python
        user = User.query.get(1) # Get the user with the specified id.
        ```
    - **Filter records:**
        ```python
        users = User.query.filter_by(name='Alice').all() # Get all the users with the name 'Alice'.
        user = User.query.filter_by(name='Alice').first() # Get the first user with the name 'Alice'.
        ```
    - **Order records:**
        ```python
        users = User.query.order_by(User.name).all() # Get all the users ordered by name.
        users = User.query.order_by(User.name.desc()).all() # Get all the users ordered by name in descending order.
        ```
    - **Limit records:**
        ```python
        users = User.query.limit(10).all() # Get the first 10 users.
        users = User.query.limit(10).offset(5).all() # Get 10 users starting from the 6th user.
        ```
    - **Count records:**
        ```python
        count = User.query.count() # Get the total number of users.
        count = User.query.filter_by(name='Alice').count() # Get the number of users with the name 'Alice'.
        ```
    - **Join tables:**
        ```python
        # Here, we have two tables: User and UserRole. User has a one-to-many relationship with UserRole. (inner join)
        users = User.query.join(UserRole).filter(UserRole.role == 'admin').all() # Get all the users with the role 'admin'.
            # This query joins the User and UserRole tables and filters the results based on the role column in the UserRole table.
        users = User.query.join(UserRole, User.id == UserRole.user_id).filter(UserRole.role == 'admin').all() # Get all the users with the role 'admin'. (inner join)
            # This query explicitly specifies the join condition between the User and UserRole tables.
        ```

<hr>