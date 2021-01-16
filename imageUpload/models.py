from django.db import models

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=50)
    image_file = models.ImageField(upload_to='')
    # upload image to images folder
