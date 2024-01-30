from django.db import models

#This code is for abstraction:

class CommonData(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)

class Student(CommonData):
    marks=models.IntegerField()
    institute=models.CharField(max_length=50)

class Employee(CommonData):
    salary=models.IntegerField()
    company=models.CharField(max_length=50)

class Customer(CommonData):
    sales=models.IntegerField()
    products=models.IntegerField()

