from rest_framework import serializers
from .models import *

class BookSerializer(serializers.Serializer):  # Here Book is our table name with APIView
    id = serializers.IntegerField(label="Enter Book Id")
    title=serializers.CharField(label="Enter the Book Title")
    author=serializers.CharField(label="Enter the author name")


class StudentSerializer(serializers.ModelSerializer):  # Here Student serializer with ModelViewSet
    class Meta:
        model = Student
        fields = '__all__'  # This will include all fields from the model
