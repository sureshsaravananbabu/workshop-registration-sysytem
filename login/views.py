from django.shortcuts import render,redirect
from .models import signup
from django.contrib import messages
# Create your views here.
def login(request):
    users = signup.objects.all()
    for user in users:
        if(user.username == request.POST.get("username") and user.password == request.POST.get("password")):
            if("admin" in request.POST.get("username")):
                return redirect('/home/'+request.POST['username'])
            else:
                return redirect('/homeuser/')

    
    return render(request,'login.html')

def sign(request):
    if(request.POST.get("username")!=None):
        errors = signup.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        first_name = request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        mail=request.POST.get("mail")
        gender=request.POST.get("gender") 
        department=request.POST.get("department")
        contactnumber=request.POST.get("contact")
        username=request.POST.get("username")
        password=request.POST.get("password")
        s = signup.objects.create(first_name=first_name,last_name=last_name,gender=gender,department=department,mail=mail,contactnumber=contactnumber,username=username,password=password)
        s.save()
    return render (request,'login.html')

