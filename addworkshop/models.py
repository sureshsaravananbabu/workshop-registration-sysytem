from django.db import models

# Create your models here.
class addworkshop(models.Model):
    courseid=models.CharField(max_length=10,unique=True)
    professor=models.CharField(max_length=15)
    timings=models.TimeField(max_length=5)
    maxstrength=models.CharField(max_length=3)
    title=models.CharField(max_length=10)
    description=models.CharField(max_length=250)
