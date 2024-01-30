from django.db import models

class CoursesData(models.Model):
    course_name=models.CharField(max_length=50)
    duration=models.CharField(max_length=50)
    fee=models.BigIntegerField()
    start_date=models.DateField()
    timings=models.TimeField()
    trainer_name=models.CharField(max_length=50)
    trainer_experience=models.CharField(max_length=50)
    trainer_mode=models.CharField(max_length=50)

# Create your models here.
