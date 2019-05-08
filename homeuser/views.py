from django.shortcuts import render
from addworkshop.models import addworkshop
# Create your views here.

def homeuser(request):
    workshops = addworkshop.objects.all()
    context = {
        'workshops' : workshops
    }
    return render(request,'homeuser.html',context)