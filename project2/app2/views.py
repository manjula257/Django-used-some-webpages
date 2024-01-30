from django.shortcuts import render
from django.http import HttpResponse
from.models import LoginPage
from.models import RegistrationPage
from.models import StudentInfo

def myloginpage(request):
    if request.method=='GET':
        return render(request,"contact.html")
    else:
        LoginPage(
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            Email=request.POST.get('Email'),
            mobile=request.POST.get('mobile'),
        ).save()
        return render(request,'contact.html')
    

def myregis_page(request):
    if request.method=='GET':
        return render(request,"registration.html")
    else:
        RegistrationPage(
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            Email=request.POST.get('Email'),
            mobile=request.POST.get('mobile'),
            password=request.POST.get('password'),
            confirmpassword=request.POST.get('confirmpassword'),
        ).save()
        return render(request,'registration.html')
    
def student_infon(request):
    if request.method=='GET':
        return render(request,"student.html")
    else:
        StudentInfo(
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            Email=request.POST.get('Email'),
            mobile=request.POST.get('mobile'),

            school_name=request.POST.get('school_name'),
            shl_cmplted_year=request.POST.get('shl_cmplted_year'),
            shl_percent=request.POST.get('shl_percent'),

            inter_clg_name=request.POST.get('inter_clg_name'),
            clg_cmplted_year=request.POST.get('clg_cmplted_year'),
            inter_percent=request.POST.get('inter_percent'),   

            graduationc_clg_name=request.POST.get('graduationc_clg_name'),
            grdtion_cmplted_year=request.POST.get('grdtion_cmplted_year'),
            grdtion_percent=request.POST.get('grdtion_percent'),

        ).save()
        return render(request,"student.html")
