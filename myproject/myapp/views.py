from django.shortcuts import render
from .models import CoursesData

def homepage(request):
    return render(request,'homepage.html')

def contactpage(request):
    return render(request,'contactpage.html')

def servicepage(request):
    courses=CoursesData.objects.all()
    return render(request,'servicepage.html',{'courses':courses})

def feedbackpage(request):
    return render(request,'feedbackpage.html')

def gallerypage(request):
    return render(request,'gallerypage.html')


# Create your views here.
