from django.shortcuts import render
from addworkshop.models import addworkshop
# Create your views here.
def home(request,username):
    workshops = addworkshop.objects.all()
    context = {
        'workshops' : workshops
    }
    return render(request,'home.html',context)


    
