from django.db import models

class EmployeeData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    salary=models.BigIntegerField()
    email=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    models=models.CharField(max_length=50)


