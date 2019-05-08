import csv,io
from django.shortcuts import render,redirect
from .models import addworkshop
from random import randint
from django.shortcuts import HttpResponse   
from .models import addworkshop
from django.contrib.auth.decorators import permission_required
# Create your views here.
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
def index(request):
    if request.method=='POST':
        courseid1= random_with_N_digits(8)
        professor1=request.POST.get("professor")
        timings1=request.POST.get("timings")
        maxstrength1=request.POST.get("maxclassstrength")
        coursename1=request.POST.get("coursename")
        description1=request.POST.get("description")
        a=addworkshop.objects.create(courseid=courseid1,professor=professor1,timings=timings1,maxstrength=maxstrength1,title=coursename1,description=description1)
        a.save()
        return redirect('/home/')
    return render(request,'addworkshop.html')
@permission_required('admin.can_add_log_entry')
def addworkshop_download(request):
    items= addworkshop.objects.all()
    response=HttpResponse(content_type='text/csv')
    response['content-Disposition']='attachment: filename="addworkshop.csv"'

    writer =csv.writer(response,delimiter=' ')
    writer.writerow(['courseid','professor','timings','maxstrength','title','description'])

    for obj in items:
        writer.writerow([obj.courseid,obj.professor,obj.timings,obj.maxstrength,obj.title,obj.description])
    return response
