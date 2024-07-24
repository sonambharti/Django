# Introduction to Django First Project

To activate conda env <br/>
`conda activate django_project_env` <br/>

To start a new Django project: <br/>
`django-admin startproject Intro` <br/>

To start a new Django application:  <br/>
`python manage.py startapp myfirstapp` <br/>

To run the project: <br/>
`python manage.py runserver` <br/>



## Folder Structure

Basic Project Folder Structure------- <br/>

Project-name <br/>
| <br/>
|----Project-name <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---__init__.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---asgi.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---settings.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---urls.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---wsgi.py <br/>
|<br/>
|----manage.py <br/>



Folder structure after starting your application ---------- <br/>

Project-name <br/>
| <br/>
|----Project-name <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---__init__.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---asgi.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---settings.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---urls.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---wsgi.py <br/>
|<br/>
|----manage.py <br/>
|---db.sqlite3 <br/>
| <br/>
|----myfirstapp <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---migrations <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---__init__.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---__init__.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---admin.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---apps.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---models.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---tests.py <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---views.py <br/>



### manage.py
It is used to run management commands related to our project. <br/>
We will use to run the development server, create migrations and much more.

### settings.py
This file contains all the project's configuration

## urls.py
This file contains all the project's URL mappings.

## views.py
This file handles the request/response cycle of our Web Application.

## models.py
In this file, we define the entities i.e. database tables of our Web Application. <br/>

## Steps to develop your first basic Django project:

1. Go to **myfirstapp/views.py** and do these changes/additions as follows.
    - Import **HTTPResponse** from **django.http**
    - Define your view function
2. Go to **Intro/urls.py** and do these changes/additions as follows.
    - Import Django URLS and Configuration files from **django.conf.urls**
    - Import your view function from **myfirstapp.views**
    - Add a URL mapping for your view function
3. Save your project.
4. Go to your terminal and run the following command to start the development server.
