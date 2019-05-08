from django.shortcuts import render
from register.models import register

# Create your views here.
def viewparticipant(request,courseidd):
    a=register.objects.filter(courseid=courseidd)
    context={
          'id':a
        }
    return render(request ,'participants.html',context)