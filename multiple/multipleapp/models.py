from django.db import models

# This is code for multiple inheritance:

class Student(models.Model):
    Student_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)

class Employee(models.Model):
    Employee_id=models.AutoField(primary_key=True)
    salary=models.IntegerField()
    department=models.CharField(max_length=50)

class Customer(Student,Employee):
    Customer_id=models.AutoField(primary_key=True)
    product=models.CharField(max_length=50)
    payment=models.IntegerField()


