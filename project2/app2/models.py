from django.db import models

class LoginPage(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)

class RegistrationPage(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)

class StudentInfo(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    mobile=models.BigIntegerField()

    school_name=models.CharField(max_length=50)
    shl_cmplted_year=models.IntegerField()
    shl_percent=models.IntegerField()

    inter_clg_name=models.CharField(max_length=50)
    clg_cmplted_year=models.IntegerField()
    inter_percent=models.IntegerField()

    graduationc_clg_name=models.CharField(max_length=50)
    grdtion_cmplted_year=models.IntegerField()
    grdtion_percent=models.IntegerField()




