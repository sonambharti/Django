# Django
Django is a free and open source web application written in Python.
It provides collection of modules that make development easier.

To create a conda env
`conda create -n <env-name> <python=version-tag>`
`conda create -n django_project_env python=3.11`

To activate conda env
`conda activate <env-name>`
`conda activate django_project_env`

Install Django using conda
`conda install -c anaconda django=3 `

To start a new Django project:
`django-admin startproject <project-name>`
`django-admin startproject Intro`

To start a new Django application:
`python manage.py startapp <app-name>`
`python manage.py startapp myfirstapp`

To run the project:
`python manage.py runserver`

To deactivate conda env
`conda deactivate`

To remove/delete conda env
`conda remove --name <env-name> --all`
`conda remove -n django_project_env --all`



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
|----manage.py
|---db.sqlite3
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

Note:
In one Django project we can have more than one Django applications.

`pip install freeze`
`conda install freeze`

`pip freeze`
`conda freeze`

`conda freeze>requirements.txt`



To use Django Admin Login, we need to create one use. Steps to create a Django super user:

Step 1: We need to migrate the project

`python manage.py makemigrations`

`python manage.py migrate`

Step 2: Then create super user
 `python manage.py createsuperuser`

    Username (leave blank to use 'sonambharti'): admin
    Email address: admin@gmail.com
    Password: admin@321
    Password (again): admin@321


Note: Django access the data stored in the database in Object Oriented fashion using it's feature **ORM (object relational mapping)**.