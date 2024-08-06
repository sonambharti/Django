from django.db import models

# Create your models here.

class Book(models.Model):  # Here Book is our table name
    id = models.IntegerField(primary_key=True)
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=200)


class Student(models.Model):  # Here Student is our table name
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
