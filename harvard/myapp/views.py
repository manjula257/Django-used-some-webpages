import datetime
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def newyear_view(request):
    now=datetime.datetime.now()
    # return render(request, "newyear.html", {"newyear": True})
    return render(request,"newyear.html",{
        # "newyear":now.month == 1 and now.day == 1
        "newyear":True
    })


def Indexpage(request):
    return render(request,"index.html")


def uploadimg(request):
    if request.method == "POST":
        imagename = request.POST['imgname']
        pics = request.FILES['image']

        newimg = ImageData.objects.create(Imgname=imagename, Image=pics)
        return redirect('show')

    
def Imagefetch(request):
    all_img = ImageData.objects.all()
    return render(request, "show.html", {'key1': all_img})
