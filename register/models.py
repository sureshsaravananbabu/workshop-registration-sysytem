from django.db import models

# Create your models here.
class register(models.Model):
    courseid=models.CharField(max_length=10)
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=50,unique=True)
    collegename=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    number=models.CharField(max_length=10,unique=True)
    quries=models.CharField(max_length=200)