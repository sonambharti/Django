"""IntroRestAPI3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


# importing django url configuration files and views 
# from django.conf.urls import url
from django.urls import re_path as url
from RestAPIapp import views
from RestAPIapp.views import Home
from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('student', views.StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #adding URL pattern links
    # url(r'^$', views.Home.hello, name='Home'),
    url("book/", views.BookApiView.as_view()),
    path('', include(router.urls))
    # url(r'^about$', views.about, name='About')
]
