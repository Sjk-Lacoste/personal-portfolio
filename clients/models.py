from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    email = models.EmailField(max_length=150, unique=True)
    phone_number = PhoneNumberField()
    website_url = models.URLField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }

        return reverse('client', kwargs=kwargs)
