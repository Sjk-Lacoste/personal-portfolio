from django.db import models
from django.urls import reverse

# Create your models here.
class Skill(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/skills/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }

        return reverse('skill', kwargs=kwargs)
