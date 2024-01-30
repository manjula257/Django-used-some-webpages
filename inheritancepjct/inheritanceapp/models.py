from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)

class Employee(Student):
    salary=models.IntegerField()
    department=models.CharField(max_length=50)

class Customer(Employee):
    product=models.CharField(max_length=50)
    payment=models.IntegerField()

