from django.shortcuts import render
from .models import LoginData
from .models import SignupPage

def homepage(request):
    return render(request,'homepage.html')

def accessories(request):
    return render(request,'accessories.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def dresses(request):
    return render(request,'dresses.html')

def loginpage(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        LoginData(
            user_name=request.POST.get('user_name'),
            password=request.POST.get('password'),
        ).save()
        return render(request,'login.html')

def signupage(request):
    if request.method=='GET':
        return render(request,'signupage.html')
    else:
        SignupPage(
            user_name=request.POST.get('user_name'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            confirm_password=request.POST.get('confirm_password'),
        ).save()
        return render(request,"signupage.html")