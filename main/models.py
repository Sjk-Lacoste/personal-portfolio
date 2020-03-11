from django.db import models
# from fontawesome_5.fields import IconField


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.name