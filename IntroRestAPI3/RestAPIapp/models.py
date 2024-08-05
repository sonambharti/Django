from django.db import models

# Create your models here.

class Book(models.Model):  # Here Location is our table name
    id = models.IntegerField(primary_key=True)
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=200)
