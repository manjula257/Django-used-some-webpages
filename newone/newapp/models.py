from django.db import models

class Students(models.Model):
    sname=models.CharField(max_length=50)
    loc=models.CharField(max_length=50)
    marks=models.BigIntegerField()

    def __str__(self):
        return self.sname
    
class Courses(models.Model):
    students=models.ForeignKey(Students,on_delete=models.CASCADE)
    cname=models.CharField(max_length=50)
    iname=models.CharField(max_length=50)
    fee=models.BigIntegerField()

'''class Students(models.Model):
    sname=models.CharField(max_length=50)
    loc=models.CharField(max_length=50)
    marks=models.BigIntegerField()

    def __str__(self):
        return self.sname
    
class Courses(models.Model):
    students=models.OneToOneField(Students,on_delete=models.CASCADE)
    cname=models.CharField(max_length=50)
    iname=models.CharField(max_length=50)
    fee=models.BigIntegerField()
    '''