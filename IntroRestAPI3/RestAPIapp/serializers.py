from rest_framework import serializers


class BookSerializer(serializers.Serializer):  # Here Location is our table name
    id = serializers.IntegerField(label="Enter Book Id")
    title=serializers.CharField(label="Enter the Book Title")
    author=serializers.CharField(label="Enter the author name")
