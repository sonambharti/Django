# Django Admin Database
Django provides a free and open source SQLite DB server written in Python. <br/>
It provides UI to interact and create ORMs that make development easier. <br/>

To activate conda env <br/>
`conda activate django_project_env` <br/>

To start a new Django project: <br/>
`django-admin startproject Intro` <br/>

To start a new Django application:  <br/>
`python manage.py startapp <app-name>` <br/>
`python manage.py startapp myfirstapp` <br/>

To run the project: <br/>
`python manage.py runserver` <br/>


## Folder Structure


Folder structure after starting your application ---------- <br/>

Project-name <br/>
|----DBapp <br/>
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





### manage.py
It is used to run management commands related to our project. <br/>
We will use to run the development server, create migrations and much more.

### settings.py
This file contains all the project's configuration.

## urls.py
This file contains all the project's URL mappings.

## views.py
This file handles the request/response cycle of our Web Application.

## models.py
In this file, we define the entities i.e. database tables of our Web Application.



##To use Django Admin Login,  <br/>
we need to create one use. Steps to create a Django super user: <br/>

#### Step 1: We need to migrate the project <br/>

`python manage.py makemigrations` <br/>

`python manage.py migrate` <br/>

#### Step 2: Then create super user <br/>
 `python manage.py createsuperuser` <br/>


    Username (leave blank to use 'sonambharti'): admin 
    Email address: admin@gmail.com 
    Password: admin@321 
    Password (again): admin@321 



Note: <br/>
Django access the data stored in the database in Object Oriented fashion using it's feature **ORM (object relational mapping)**.


Steps to develop your first basic Django project:

1. Go to **DBapp/views.py** and do these changes/additions as follows.
    - Import **HTTPResponse** from **django.http**
    - Define your view function

2. Go to **Intro/urls.py** and do these changes/additions as follows.
    - Import Django URLS and Configuration files from **django.conf.urls**
    - Import your view function from **DBapp.views**
    - Add a URL mapping for your view function

3. Create models in **DBapp.models** and define the entities i.e. database tables of our Web Application.

4. Add/ Define Django application in **INSTALLED_APPS** in  **IntroDB2/IntroDB2/settings.py**

5. Save your project.

6. Go to your terminal and run the following command to migrate DB: <br/> ` python manage.py makemigrations -n <db changes description>`.<br/> Eg: ` python manage.py makemigrations -n Added_Location_Table`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;### Output: <br/>
     
     (django_project_env) sonambharti@sonambharti IntroDB2 % python manage.py makemigrations -n Added_Location_Table 
     Migrations for 'DBapp': 
       DBapp/migrations/0001_Added_Location_Table.py 
         - Create model Location 
     

7. Now, run migrate command: `python manage.py migrate`
8. Now, run the server: `python manage.py runserver`
