from django.shortcuts import render

# Create your views here.


# Introduction Project code addition
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world ! ")


def about(request):
    return HttpResponse("This is my first Django Demo application🙂. 👍🏻")

