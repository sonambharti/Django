from django.shortcuts import render

# Create your views here.

# Introduction Project code addition
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class BookApiView(APIView):
    serializer_class = BookSerializer
    def get(self, request):
        allBooks = Book.objects.all().values()
        return Response({"Message": "List of Books", "Book List": list(allBooks)})
    
    def post(self, request):
        serializer_obj = BookSerializer(data=request.data)
        if (serializer_obj.is_valid()):
            Book.objects.create(id=serializer_obj.data.get("id"),
                            title=serializer_obj.data.get("title"),
                            author=serializer_obj.data.get("author")
                            )
        
        book = Book.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message": "Books added in the list", "Book List": book})
    

class Home():
    def hello(request):
        return HttpResponse("Hello world ! ")


    # def about(request):
    #     return HttpResponse("This is my first Django Demo application🙂. 👍🏻")


