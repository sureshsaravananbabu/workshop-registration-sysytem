from django.shortcuts import render,redirect
from addworkshop.models import addworkshop
# Create your views here.
def update(request,courseid,professor,timings,maxstrength,title,description):
    dicti = {
        'id': courseid,
        'professor': professor,
        'timings': timings,
        'maxstrength': maxstrength,
        'title': title,
        'description': description
    }
    return render(request,'update.html',dicti)
def index(request):
    if request.method=='POST':
        addworkshop.objects.filter(courseid=request.POST.get("courseid")).update(professor=request.POST.get("professor"),timings=request.POST.get("timings"),description=request.POST.get("description"),title=request.POST.get("coursename"),maxstrength=request.POST.get("maxclassstrength"))
    return redirect('/home/')
    



