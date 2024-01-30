from django.db import models

class LoginData(models.Model):
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class SignupPage(models.Model):
    user_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
