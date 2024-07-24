# Django
Django is a free and open source web application written in Python. <br/>
It provides collection of modules that make development easier. <br/>

To create a conda env <br/>
`conda create -n <env-name> <python=version-tag>` <br/>
`conda create -n django_project_env python=3.11` <br/>

To activate conda env <br/>
`conda activate <env-name>` <br/>
`conda activate django_project_env` <br/>

Install Django using conda <br/>
`conda install -c anaconda django=3 ` <br/>

To start a new Django project: <br/>
`django-admin startproject <project-name>` <br/>
`django-admin startproject Intro` <br/>

To start a new Django application:  <br/>
`python manage.py startapp <app-name>` <br/>
`python manage.py startapp myfirstapp` <br/>

To run the project: <br/>
`python manage.py runserver` <br/>

To deactivate conda env <br/>
`conda deactivate` <br/>

To remove/delete conda env <br/>
`conda remove --name <env-name> --all` <br/>
`conda remove -n django_project_env --all` <br/>



## Folder Structure

Basic Project Folder Structure------- <br/>

Project-name <br/>
| <br/>
|----Project-name <br/>
|    | <br/>
|    |---__init__.py <br/>
|    | <br/>
|    |---asgi.py <br/>
|    |
|    |---settings.py <br/>
|    | <br/>
|    |---urls.py <br/>
|    | <br/>
|    |---wsgi.py <br/>
|    <br/>
|----manage.py <br/>



Folder structure after starting your application ---------- <br/>

Project-name <br/>
| <br/>
|----Project-name <br/>
|    | <br/>
|    |---__init__.py <br/>
|    | <br/>
|    |---asgi.py <br/>
|    |
|    |---settings.py <br/>
|    | <br/>
|    |---urls.py <br/>
|    | <br/>
|    |---wsgi.py <br/>
|    <br/>
|----manage.py <br/>
|---db.sqlite3 <br/>
| <br/>
|----myapp <br/>
|    |---migrations <br/>
|    |    |---__init__.py <br/>
|    | <br/>
|    |---__init__.py <br/>
|    | <br/>
|    |---admin.py <br/>
|    | <br/>
|    |---apps.py <br/>
|    | <br/>
|    |---models.py <br/>
|    | <br/>
|    |---tests.py <br/>
|    | <br/>
|    |---views.py <br/>




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

Note: <br/>
In one Django project we can have more than one Django applications. <br/>

`pip install freeze` <br/>
`conda install freeze` <br/>

`pip freeze` <br/>
`conda freeze` <br/>

`conda freeze>requirements.txt` <br/>



To use Django Admin Login, we need to create one use. Steps to create a Django super user: <br/>

Step 1: We need to migrate the project <br/>

`python manage.py makemigrations` <br/>

`python manage.py migrate` <br/>

Step 2: Then create super user <br/>
 `python manage.py createsuperuser` <br/>

    Username (leave blank to use 'sonambharti'): admin <br/>
    Email address: admin@gmail.com <br/>
    Password: admin@321 <br/>
    Password (again): admin@321 <br/>


Note: <br/>
Django access the data stored in the database in Object Oriented fashion using it's feature **ORM (object relational mapping)**.
