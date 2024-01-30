from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student_Data

def homepage(request):
    students=Student_Data.objects.all()
    return render(request,'homepage.html',{'students':students})

def add_student(request):
    if request.method=='GET':
        return render(request,'add_student.html')
    else:
            Student_Data(
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'), 
            course=request.POST.get('course'),
            fee=request.POST.get('fee'),
            dob=request.POST.get('dob'),
            location=request.POST.get('location'),
            img=request.POST.get('img'),
            ).save()
            return redirect('homepage')
    
def studentdata(request,id):
    student=Student_Data.objects.get(id=id)
    return render(request,'studentdata.html',{'student':student})

def deletedata(request,id):
    student=Student_Data.objects.get(id=id)
    student.delete()
    return redirect('homepage')


def gallery(request):
    return render(request,"gallery.html")
def service(request):
    return render(request,"service.html")


