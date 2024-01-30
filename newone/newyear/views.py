import datetime
from django.shortcuts import render

# # Create your views here.
# def greet(request,name):
#     # return render(f"newyear, {name}!"),
#     return render(request,"greet.html",{
#         "name":name.capitalize()
#     })

def newyear_view(request):
    now=datetime.datetime.now()
    return render(request,"newyear.html",{
        "newyear":now.month == 1 and now.day == 1
    })