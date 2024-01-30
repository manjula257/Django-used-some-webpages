
from django.db import models

class ImageData(models.Model):
    Imgname = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='images/')
