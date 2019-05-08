# Create your models here.
from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        '''  if (postData['username'].isalpha()) =="False":
            if len(postData['username']) < 2:
                errors['name'] = " userName can not be shorter than 2 characters"

        if len(postData['email']) == None:
            errors['email'] = "You must enter an email"
        
        temp = 0
        users = signup.objects.all()
        for user in users:
            if(user.mail == postData['mail']):
                temp = 1
                errors['mail'] = "You must enter an email"

        if(temp==1):
            errors['email'] = "An account with this email already exists!"
        if len(postData['password']) <= 8:
            errors['password'] = "Password is too short!"'''

        if len(postData['contact']) <= 9:
            errors['contact'] = "You must enter  correct an Mobile Number"
        return errors


# Create your models here.
class signup(models.Model):
    first_name=models.CharField(max_length=264)
    last_name=models.CharField(max_length=264)
    gender=models.CharField(max_length=10)
    department=models.CharField(max_length=10)
    contactnumber=models.CharField(max_length=10)
    mail=models.EmailField(max_length=50,unique=True)
    username=models.CharField(max_length=15,unique=True)
    password=models.CharField(max_length=8)
    objects=UserManager()

