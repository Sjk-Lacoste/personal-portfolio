from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_descripion = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')