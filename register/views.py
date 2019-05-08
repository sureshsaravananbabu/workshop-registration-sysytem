from django.shortcuts import render,redirect
from .models import register

# Create your views here.
def registerr(request,courseid):
    dicti={
        'course':courseid
    }
    return render(request,'register.html',dicti)

def index(request):
    if request.method=='POST':
        a=register.objects.create(courseid=request.POST.get("courseid"),name=request.POST.get("name"),email=request.POST.get("email"),collegename=request.POST.get("collegename"),address=request.POST.get("address"),number=request.POST.get("number"),quries=request.POST.get("quries"))
        a.save()
        return redirect('/homeuser/')