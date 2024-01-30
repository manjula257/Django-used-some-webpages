from django.db import models

class Enjoy(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Date=models.DateField()
    Mobile=models.BigIntegerField()
    Email=models.EmailField()
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
