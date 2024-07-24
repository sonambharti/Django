from django.db import models

# Create your models here.

class Location(models.Model):  # Here Location is our table name
    id = models.IntegerField(primary_key=True)
    value=models.CharField(max_length=30)
