from django.shortcuts import render
from django.http import HttpResponse
from.models import ContactData

def contactview(request):
    if request.method=='GET':
        return render(request,"contact.html")
    else:
        ContactData(
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            Email=request.POST.get('Email'),
            course=request.POST.get('course'),
            location=request.POST.get('location'),
            mobile=request.POST.get('mobile'),
        ).save()
        return render(request,'contact.html')


def home(request):
    x="hii from homepage"
    return HttpResponse(x)

def gallery(request):
    x="hii from gallerypage"
    return HttpResponse(x)

def service(request):
    x="hii from servicepage"
    return HttpResponse(x)

def feedback(request):
    x="hii from feedbackpage"
    return HttpResponse(x)

def manjuhome(request):
    return render(request,'manjuhome.html')

def manjuservice(request):
    return render(request,'manjuservice.html')



