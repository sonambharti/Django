# Introduction to Django First Project

To activate conda env
`conda activate <env-name>`
`conda activate django_project_env`

To start a new Django project:
`django-admin startproject Intro`

To start a new Django application:
`python manage.py startapp myfirstapp`

To run the project:
`python manage.py runserver`


## Folder Structure

Basic Project Folder Structure-------

Project-name
|
|----Project-name
|    |
|    |---__init__.py
|    |
|    |---asgi.py
|    |
|    |---settings.py
|    |
|    |---urls.py
|    |
|    |---wsgi.py
|    
|----manage.py



Folder structure after starting your application ----------

Project-name
|
|----Project-name
|    |
|    |---__init__.py
|    |
|    |---asgi.py
|    |
|    |---settings.py
|    |
|    |---urls.py
|    |
|    |---wsgi.py
|   
|---db.sqlite3 
|----manage.py
|
|----myapp
|    |---migrations
|    |    |---__init__.py
|    |
|    |---__init__.py
|    |
|    |---admin.py
|    |
|    |---apps.py
|    |
|    |---models.py
|    |
|    |---tests.py
|    |
|    |---views.py




### manage.py
It is used to run management commands related to our project.
We will use to run the development server, create migrations and much more.

### settings.py
This file contains all the project's configuration

## urls.py
This file contains all the project's URL mappings.

## views.py
This file handles the request/response cycle of our Web Application.

## models.py
In this file, we define the entities i.e. database tables of our Web Application.

Steps to develop your first basic Django project:

1. Go to **myfirstapp/views.py** and do these changes/additions as follows.
    - Import **HTTPResponse** from **django.http**
    - Define your view function
2. Go to **Intro/urls.py** and do these changes/additions as follows.
    - Import Django URLS and Configuration files from **django.conf.urls**
    - Import your view function from **myfirstapp.views**
    - Add a URL mapping for your view function
3. Save your project.
4. Go to your terminal and run the following command to start the development server.