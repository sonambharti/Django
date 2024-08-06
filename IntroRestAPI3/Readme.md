# RestAPI in Django
In the world of web development, APIs play a pivotal role in connecting different applications and services. Have you ever wondered what an API is and how it works? we'll demystify APIs and delve into the concept of Rest API, using practical examples to solidify our understanding. <br/>

To activate conda env <br/>
`conda activate django_project_env` <br/>

To start a new Django project: <br/>
`django-admin startproject IntroRestAPI3` <br/>

To start a new Django application:  <br/>
`python manage.py startapp RestAPIapp` <br/>

To run the project: <br/>
`python manage.py runserver` <br/>


## Folder Structure


Folder structure after starting your application ---------- <br/>



Project-name
|----RestAPIapp <br/>
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
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---serializers.py <br/>
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



# API 
**API** - Application Programming Interface <br/>
- set of rules
- Allows programs to talk to each other

**Rest API** - Representational State Transfer Application Programming Interface
- set of rules that developers follow when they create their API
- API that uses HTTP requests to send data back and forth between the client and the server

## RestAPI Methods 
- GET - retrieve data from a specific resource
- POST - create a new resource
- PUT - update a resource
- DELETE - delete a resource
- PATCH - update a resource
- HEAD - retrieve metadata about a resource
- OPTIONS - retrieve information about what methods are supported by a resource

##To use Django Admin Login,  <br/>
we need to create one use. Steps to create a Django super user: <br/>

#### Step 1: We need to migrate the project <br/>

`python manage.py makemigrations` <br/>

`python manage.py migrate` <br/>

#### Step 2: Then create super user <br/>
 `python manage.py createsuperuser` <br/>


    Username (leave blank to use 'sonambharti'): admin
    Email address: admin@gmail.com
    Password: admin123
    Password (again): admin123


Note: <br/>
Django access the data stored in the database in Object Oriented fashion using it's feature **ORM (object relational mapping)**. <br/>


Steps to develop your first basic Django project: <br/>

1. Install djangorestframework using `pip install djangorestframework`

2. Add/ Define Django application `RestAPIapp`, and `rest_framework` in **INSTALLED_APPS** in  **IntroRestAPI3/IntroRestAPI3/settings.py**

3. Create models in **RestAPIapp.models** and define the entities i.e. database tables of our Web Application.

4. Go to **RestAPIapp/views.py** and do these changes/additions as follows.
    - Import **APIView** from **rest_framework.views**.
    - Import **Response** from **rest_framework.response**.
    - Define your view class and CRUD function inheriting the `APIView` class in our `Book` class.

5. Go to **IntroRestAPI3/urls.py** and do these changes/additions as follows.
    - Import Django URLS and Configuration files from **django.conf.urls**
    - Import your view function from **RestAPIapp.views**
    - Add a URL mapping for your view function


6. Save your project.

7. Go to your terminal and run the following command to migrate DB: ` python manage.py makemigrations -n <db changes description>`. Eg: ` python manage.py makemigrations -n Added_Book_Table`.

    ##Output:

    (django_project_env) sonambharti@sonambharti IntroDB2 % python manage.py makemigrations -n Added_Book_Table
    Migrations for 'DBapp':
    DBapp/migrations/0001_Added_Book_Table.py
        - Create model Book


7. Now, run migrate command: `python manage.py migrate`

8. Now, run the server: `python manage.py runserver` to check `GET` and `POST` method of BookAPIView class.

9. To add validations, create `serializers.py` to validate the type of the object.

10. Add `serializers` in the view of the application.

11. Now, I'll write an API using `ModelViewSet` in vies for Student models, and then will serialize the model using `ModelSerializer`.

12. Then, In url.py we will create a `router` object and we will `register` student url and class in it. After that, include all the urls present in router to `urlpattern`.

<br/><br/>
Note: We can use `ModelViewSet` instead of `APIView` in views and `ModelSerializer` instead of `Serializer` in serializer in order to write minimum no. of lines in code to save time and complexity.
<br/><br/>

**!IMPORTANT**

<br/>
IF you want to update or delete an object/compontent/row from the database table, we can directly go to the Django framework using the unique keyword (here, In student table `id` is unique)

Also, we can use  `Postman` for the same. Here are some examples to `Create`, `GET`, `Put`, `Patch`, and `Delete` method for Student table ----- 
1. CREATE 
    - URL: http://127.0.0.1:8000/student/ 
    - Method: POST 
    - Body: raw/json
    - Data: {
                "id": 203,
                "first_name": "Niharika",
                "last_name": "Dilaik",
                "dob": "1996-11-20"
            }

2. READ
    - URL: http://127.0.0.1:8000/student/ 
    - Method: GET 
    
3. UPDATE
    - URL: http://127.0.0.1:8000/student/203/
    - Method: PUT
    - Body: raw/json
    - Data: {
                "id": 203,
                "first_name": "Niharika",
                "last_name": "Sharma",
                "dob": "1996-11-20"
            }
    <br/>
    OR,
    <br/>
    - URL: http://127.0.0.1:8000/student/203/
    - Method: PATCH
    - Body: raw/json
    - Data: {
                "last_name": "Sharma"
            }

4. DELETE
    - URL: http://127.0.0.1:8000/student/203/
    - Method: DELETE

