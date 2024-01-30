from django.shortcuts import render
from .models import EmployeeData
from django.http.response import HttpResponse
import random
import faker
fake=faker.Faker()
def employeeData(request):
    for i in range(49):
        fname=fake.first_name()
        lname=fake.last_name()
        sal=fake.random_element(elements=(2000,1000,3000,4000))
        com=fake.random_element(elements=('tcs','infosys','wipro','cts'))
        city=fake.random_element(elements=('hyd','bang','pune','chennai'))
        email=fake.email()
        address=fake.address()


        EmployeeData(
        first_name=fname,
        last_name=lname,
        salary=sal,
        company=com,
        city=city,
        email=email,
        address=address,
        ).save()
    return HttpResponse('Data Saved')

def fetching_data(request):
    employees=EmployeeData.objects.all()
    return render(request,'employeedata.html',{'employees':employees})

def mainpage(request):
    return render(request,'mainpage.html')

def hyderabad(request):
    if request.method=='GET':
       hydData=EmployeeData.objects.filter(city='hyd')
       return render(request,'hydData.html',{'hydData':hydData})
    else:
        company1=request.POST.get('com')
        hydData=EmployeeData.objects.filter(Q(city='hyd')&Q(company=company1))
        return render(request,'hydData.html',{'hydData':hydData})
def banglore(request):
    if request.method=='GET':
       bangData=EmployeeData.objects.filter(city='bang')
       return render(request,'bangData.html',{'bangData':bangData})
    else:
        company1=request.POST.get('com')
        bangData=EmployeeData.objects.filter(city='bang')
        return render(request,'bangData.html',{'bangData':bangData})

def chennai(request):
    if request.method=='GET':
       chenData=EmployeeData.objects.filter(city='chennai')
       return render(request,'chenData.html',{'chenData':chenData})
    else:
        company1=request.POST.get('com')
        chenData=EmployeeData.objects.filter(city='chennai')
        return render(request,'chenData.html',{'chenData':chenData})

def pune(request):
    if request.method=='GET':
       puneData=EmployeeData.objects.filter(city='pune')
       return render(request,'puneData.html',{'puneData':puneData})
    else:
        company1=request.POST.get('com')
        puneData=EmployeeData.objects.filter(city='pune')
        return render(request,'puneData.html',{'puneData':puneData})