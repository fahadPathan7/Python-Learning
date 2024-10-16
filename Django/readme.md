# <div align='center'> 🧩 Django </div>

## 📝 Table of Contents
- [ 🧩 Django ](#--django-)
  - [📝 Table of Contents](#-table-of-contents)
  - [🪛 Project Setup](#-project-setup)
  - [📚 Django Basics](#-django-basics)
  - [📚 Project Structure](#-project-structure)
  - [📚 Django Admin](#-django-admin)
  - [📚 Django Models](#-django-models)
  - [📚 Django Forms](#-django-forms)
  - [📚 Django Views](#-django-views)
  - [📚 Django URLs](#-django-urls)
  - [📚 Django Templates](#-django-templates)
  - [📚 Handle the forms in the frontend](#-handle-the-forms-in-the-frontend)
  - [📚 Django Middleware](#-django-middleware)
  - [📚 Django authentication (register, login, logout)](#-django-authentication-register-login-logout)
  - [📚 CRUD Operations](#-crud-operations)
<hr>
<br><br>

## 🪛 Project Setup
- [Project Setup](../Django/setup/)

<br>

## 📚 Django Basics
- Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- It follows the model-view-template architectural pattern.
   - **Model**: It describes the database schema and data structure.
   - **View**: It controls logic and flow of data between models and templates.
   - **Template**: It describes how the data is presented to the user. (HTML files)
- **Security**: Django helps developers avoid many common security mistakes by providing a framework that has been engineered to "do the right things" to protect the website automatically.
   - **SQL Injection**: Django uses built-in ORM (Object Relational Mapping) system that helps developers avoid SQL injection attacks.
   - **Cross-Site Scripting (XSS)**: Django template system is designed to automatically escape any data that is output into HTML.
   - **Cross-Site Request Forgery (CSRF)**: Django has built-in protection against CSRF attacks. and many more.
- **Scalability**: Django can handle the high traffic and complex web applications.
- **Versatile**: Django can be used to build any type of website or web application.

<br>

## 📚 Project Structure
```bash
myproject/
│
├── myproject/                 # Root folder for your Django project.
│   ├── __init__.py            # Marks the directory as a Python package.
│   ├── settings.py            # Project-level settings (development, production, etc.).
│   ├── urls.py                # Project-level URL routing.
│   ├── asgi.py                # ASGI configuration for asynchronous applications.
│   ├── wsgi.py                # WSGI configuration for deployment (traditional servers).
│   └── manage.py              # Command-line utility for administrative tasks.
│
├── apps/                      # Directory for all your Django apps.
│   ├── __init__.py            # Marks this as a Python package.
│   ├── app_name_1/            # First Django app folder.
│   │   ├── __init__.py        # Marks the directory as a Python package.
│   │   ├── admin.py           # Django admin panel configuration for the app.
│   │   ├── apps.py            # Configuration for the app itself.
│   │   ├── models.py          # Models (database schema) for the app.
│   │   ├── views.py           # Application logic (handling requests).
│   │   ├── urls.py            # URL routing specific to the app.
│   │   ├── forms.py           # Django forms (optional).
│   │   ├── serializers.py     # DRF serializers for APIs (optional).
│   │   ├── signals.py         # Signals for handling events (optional).
│   │   ├── tasks.py           # Celery or background tasks (optional).
│   │   ├── static/            # Static files (CSS, JavaScript, images) for this app.
│   │   │   └── app_styles.css
│   │   ├── templates/         # HTML templates specific to this app.
│   │   │   └── app_name_1/
│   │   │       └── index.html
│   │   └── migrations/        # Database migrations for the app.
│   │       ├── __init__.py    # Marks this as a Python package.
│   │       └── 0001_initial.py
│   └── app_name_2/            # Additional apps follow the same structure.
│
├── static/                    # Global static files (CSS, JavaScript, images).
│   └── global_styles.css
│
├── templates/                 # Global HTML templates (shared across apps).
│   └── base.html
│
├── media/                     # Uploaded media files (user uploads, etc.).
│
├── env/                       # Virtual environment for Python dependencies.
│
├── requirements.txt           # Python package dependencies for the project.
│
└── README.md                  # Project documentation.
```

<br>

## 📚 Django Admin
- Django provides a built-in admin panel that can be used to manage the application data.
- The admin panel is a powerful tool for developers to manage the application data without writing any code.
- The admin panel can be customized to add, update, and delete the data. (CRUD operations)
- The admin panel can be accessed at `http://localhost:8000/admin/` by default.
- To create a superuser, run the following command:
```bash
python manage.py createsuperuser
```

<br>

## 📚 Django Models
- Django models are Python classes that represent database tables.
- Each model class corresponds to a database table, and each attribute of the class represents a database field.
- Django models are defined in the `models.py` file of the app. (e.g., `myapp/models.py`)
```python
from django.db import models
from django.contrib.auth.models import User # Django's built-in User model

class Author(models.Model):
    # enum choices (dropdown)
    role_choices = (
        ('A', 'Author'),
        ('E', 'Editor'),
        ('R', 'Reviewer'),
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField() # it will validate the email format automatically
    role = models.CharField(max_length=1, choices=role_choices) # for choices (dropdown)
    photo = models.ImageField(upload_to='authors/', null=True, blank=True) # for image files (will create at media/authors/)
    # one to one relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # one to one relationship
    # one to many relationship
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='authors') # related_name is used
      ## to access the related objects from the other model
    # many to many relationship
    books = models.ManyToManyField('Book', related_name='authors')
    salary = models.DecimalField(max_digits=10, decimal_places=2) # for decimal numbers (int, float)
    is_active = models.BooleanField(default=True) # for boolean values (True, False)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add will set the current date and time when the object is created
    updated_at = models.DateTimeField(auto_now=True) # auto_now will update the date and time whenever the object is updated

    # optional
    def __str__(self):
        return self.name # it will return the name of the author when the object is printed or displayed in the admin panel.
```

- To create the database table for the model, run the following command:
```bash
python manage.py makemigrations {app_name} # don't include the curly braces. e.g., python manage.py makemigrations myapp
python manage.py migrate
```
- **field types:**
  - **CharField**: It is used to store a small amount of text. (max_length is required)
  - **IntegerField**: It is used to store integer values.
  - **EmailField**: It is used to store email addresses.
  - **ImageField**: It is used to store image files.
  - **PasswordField**: It is used to store passwords.
  - **DateField**: It is used to store dates.
  - **DateTimeField**: It is used to store date and time.
  - **DecimalField**: It is used to store decimal numbers.
  - **BooleanField**: It is used to store boolean values (True, False).
  - **ForeignKey**: It is used to create a one-to-many relationship.
  - **ManyToManyField**: It is used to create a many-to-many relationship.
  - **OneToOneField**: It is used to create a one-to-one relationship.
  - **TextField**: It is used to store a large amount of text.
  - **URLField**: It is used to store URLs.

<br>

## 📚 Django Forms
- Django forms are used to collect user data and validate it. (e.g., login form, registration form, etc.)
- Django forms can be created using the `forms.py` file of the app. (e.g., `myapp/forms.py`)
```python
from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__' # to include all fields of the model
        # fields = ['name', 'age', 'email'] # to include specific fields
        # exclude = ['email'] # to exclude specific fields

# custom form
class SelectAuthorForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label='Select Author', label='Select Author')
      ## queryset is used to fetch the data from the Author model
      ## empty_label is used to display the default text in the dropdown
      ## label is used to display the label of the dropdown
```

<br>

## 📚 Django Views
- Django views are Python functions that take a web request and return a web response.
- Django views are defined in the `views.py` file of the app. (e.g., `myapp/views.py`)
```python
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Author # import the model
from .forms import AuthorForm, SelectAuthorForm # import the forms

def home(request):
   return HttpResponse('Hello, World!') # return the HTTP response

for json response
def author_list_json(request):
   authors = Author.objects.all() # fetch all authors from the database
   data = {'authors': list(authors.values())} # convert the queryset to a list of dictionaries
   return JsonResponse(data) # return the JSON response

def author_list(request):
   authors = Author.objects.all() # fetch all authors from the database
   return render(request, 'authors/author_list.html', {'authors': authors}) # render the template with the data
      ## 'authors' is the context variable that can be accessed in the template. request is the request object.
      ## request must be passed as the first argument to the render function.

def author_detail(request, author_id):
   author = Author.objects.get(id=author_id) # fetch the author by id (id is the primary key. default field)
   return render(request, 'authors/author_detail.html', {'author': author}) # render the template with the data

def create_author(request):
   if request.method == 'POST':
      form = AuthorForm(request.POST, request.FILES) # create the form with the POST data (including files)
      if form.is_valid(): # validate the form
         new_author = form.cleaned_data # cleaned data is the validated data
         Author.objects.create(**new_author) # create the author object
         # or
         # form.save() # save the form data to the database (if the form is created using ModelForm not Form)
         return redirect('author_list') # redirect to the author list page (name of a view)
   else:
      form = AuthorForm() # create the form
   return render(request, 'authors/create_author.html', {'form': form}) # render the template with the form

def select_author(request):
   if request.method == 'POST':
      select_author_form = SelectAuthorForm(request.POST) # create the form with the POST data
      if select_author_form.is_valid(): # validate the form
         author_id = select_author_form.cleaned_data['author'].id # get the author id from the form
         return redirect('author_detail', author_id=author_id) # redirect to the author detail page with the author id
   else:
      select_author_form = SelectAuthorForm() # create the form
   return render(request, 'authors/select_author.html', {'select_author_form': select_author_form}) # render the template with the form
```

<br>

## 📚 Django URLs
- Django URLs are used to map the URL patterns to the views.
- When a user visits a URL, Django will look for the matching URL pattern in the `urls.py` file.
- Django URLs are defined in the `urls.py` file of the app. (e.g., `myapp/urls.py`)
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # home page
    path('authors/', views.author_list, name='author_list'), # author list page
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'), # author detail page
    path('authors/create/', views.create_author, name='create_author'), # create author page
    path('authors/select/', views.select_author, name='select_author'), # select author page
]
```

- `<int:author_id>`: It is used to capture the integer value from the URL. (e.g., `/authors/1/`)
- name is used to reference the URL pattern in the templates or views. (e.g., redirect('author_list'))
- To include the app URLs in the project URLs, add the app URLs to the project URLs. <br>
  (because the django searches for the URLs in the project URLs. so we need to include the app URLs in the project URLs)
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')), # include the app URLs
]
```

<br>

## 📚 Django Templates
- Before using the templates, we need do setup in the `settings.py` file. [(For Setup)](../Django/setup/readme.md#-step-8-add-static-and-templates-directories)
- After the setup, we can create the templates in the `templates` folder of the app.
- Django templates are used to render the HTML content dynamically.
- Django templates are HTML files with additional template tags and filters.
- One HTML file can extend another HTML file to reuse the common parts. (the html is called the layout or base template)
```html
<!-- layout.html -->
{% load static tailwind_tags %}
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        {% block title %}
        Default Title
        {% endblock %}
    </title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
    {% tailwind_css %}
</head>
<body>
    <nav> This is the navigation bar </nav>
    {% block content %}{% endblock %}
</body>
</html>
```

```html
<!-- home.html -->
{% extends 'layout.html' %}

{% block title %}
Home Page
{% endblock %}

{% block content %}
<h1>Welcome to the Home Page</h1>
{% endblock %}
```

- **Template Tags:**
  - **{% block %}**: It defines a block that can be overridden in the child template.
  - **{% extends %}**: It extends the parent template.
  - **{% include %}**: It includes another template.
  - **{% for %}**: It loops over each item in a list.
  - **{% if %}**: It checks a condition.
  - **{% url %}**: It generates a URL.
  - **{% load %}**: It loads a template library.
  - **{% static %}**: It generates a static file URL.
  - **{% csrf_token %}**: It generates a CSRF token. (before using django forms it is required)

<br>

## 📚 Handle the forms in the frontend
```html
<!-- create_author.html -->
{% block content %}
<h1>Create Author</h1>
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <!-- {{ form.as_table }} -->
    <button type="submit">Create Author</button>
</form>
{% endblock %}
```

```html
<!-- select_author.html -->
{% block content %}
<h1>Select Author</h1>
<form method="POST">
    {% csrf_token %}
    {{ select_author_form.as_p }}
    <button type="submit">Select Author</button>
</form>
{% endblock %}
```

- **form.as_p**: It renders the form fields as paragraphs.
- **form.as_table**: It renders the form fields as a table.
- **form.as_ul**: It renders the form fields as an unordered list.
- **enctype="multipart/form-data"**: It is used to upload files in the form.
- The form sends a GET request by default. After that it sends a POST request when the form is submitted.

## 📚 Django Middleware
- Django middleware is a framework of hooks into Django's request/response processing.
- It is a lightweight, low-level plugin system for globally altering Django's input or output.
- Django middleware is used to perform the following tasks:
  - **Authentication**: It is used to authenticate the user.
  - **Logging**: It is used to log the requests and responses.
  - **Caching**: It is used to cache the responses.
  - **Compression**: It is used to compress the responses.
  - **Security**: It is used to add security headers.
  - **Session Management**: It is used to manage the user sessions.
  - **Error Handling**: It is used to handle the errors. and many more.

<br>

## 📚 Django authentication (register, login, logout)
- Django provides built-in authentication views for user registration, login, and logout.
- To use the built-in authentication views, add the following URLs to the app URLs.
```python
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'), # login page
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'), # logout page
    path('accounts/register/', auth_views.RegisterView.as_view(), name='register'), # register page
]
```
---
<br>

- To customize the authentication views, create the custom views in the `views.py` file.
```python
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password) # create the user
            ## if user already exists, it will raise an error
        messages.success(request, 'User registered successfully.')
        return redirect('login')
    return render(request, 'accounts/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # check the user credentials
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

def logout_user(request):
   logout(request)
   return redirect('home')
```

- To use the custom authentication views, add the following URLs to the app URLs.
```python
urlpatterns = [
    path('accounts/register/', views.register_user, name='register'), # register page
    path('accounts/login/', views.login_user, name='login'), # login page
    path('accounts/logout/', views.logout_user, name='logout'), # logout page
]
```
---
<br>

- Create user with custom fields (using forms)
```python
# forms.py
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] # include the fields
```

```python
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # commit is False to prevent saving the user object
            user.set_password(form.cleaned_data['password1']) # set the password (first password field)
            user.save() # save the user object
            messages.success(request, 'User registered successfully.')
            login(request, user) # login the user
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})
```
---
<br>

- **Default User Model fields:**
  - **username**: It is used to store the username of the user.
  - **password**: It is used to store the password of the user.
  - **email**: It is used to store the email address of the user.
  - **first_name**: It is used to store the first name of the user.
  - **last_name**: It is used to store the last name of the user.
  - **is_active**: It is used to activate or deactivate the user.
  - **is_staff**: It is used to give staff permissions to the user.
  - **is_superuser**: It is used to give superuser permissions to the user.
  - **date_joined**: It is used to store the date and time when the user is created.
  - **last_login**: It is used to store the date and time when the user last logged in.
  - **groups**: It is used to assign the user to the groups.
  - **user_permissions**: It is used to assign the user permissions.
  - **is_authenticated**: It is used to check if the user is authenticated.
  - **is_anonymous**: It is used to check if the user is anonymous.
  - **get_full_name()**: It is used to get the full name of the user.
  - **get_short_name()**: It is used to get the short name of the user.
  - **check_password()**: It is used to check the password of the user.
  - **set_password()**: It is used to set the password of the user.
  - **has_perm()**: It is used to check if the user has a specific permission.
  - **has_module_perms()**: It is used to check if the user has permissions for a specific module.
  - **get_group_permissions()**: It is used to get the permissions of the user group.
  - **get_all_permissions()**: It is used to get all the permissions of the user.

<br>

- **Custom User Model:**
  - Django provides a built-in User model that can be customized to add additional fields.
  - To create a custom user model, create a new model that inherits from the AbstractUser model.
  - The default User model attributes will be inherited by the custom user model.
  - If you override any attribute, it will replace the default attribute.
  - The custom user model can be created in the `models.py` file of the app.
```python
from django.contrib.auth.models import AbstractUser # import the AbstractUser model

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='users/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
```

- To use the custom user model, add the following settings to the `settings.py` file.
```python
AUTH_USER_MODEL = 'myapp.CustomUser'
```

<br>

## 📚 CRUD Operations
- **Create Operation:**
```python
author = Author.objects.create(name='No Name', password='123')
```
- **Read Operation:**
```python
authors = Author.objects.all() # fetch all authors
author = Author.objects.get(id=1) # fetch the author by id
author = Author.objects.filter(name='No Name') # fetch the author by name
author = Author.objects.first() # fetch the first author
author = Author.objects.last() # fetch the last author
author = Author.objects.order_by('name') # fetch the authors ordered by name
author = Author.objects.order_by('-name') # fetch the authors ordered by name in descending order
author = Author.objects.exclude(name='No Name') # fetch the authors excluding the name
author = Author.objects.filter(name__contains='No') # fetch the authors whose name contains 'No'
```
- **Update Operation:**
```python
author = Author.objects.get(id=1) # fetch the author by id
author.name = 'New Name' # update the name
author.save() # save the changes
```
- **Delete Operation:**
```python
author = Author.objects.get(id=1) # fetch the author by id
author.delete() # delete the author
```

<hr>