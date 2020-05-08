from django.db import models
from django.urls import reverse
from clients.models import Client
from skills.models import Skill

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='category')
    short_description = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)

    class Meta:
        """
        Enforcing that there can not be two categories under a parent
        with same slug.
        """
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }

        return reverse('category', kwargs=kwargs)

class TechStack(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/techstack/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }

        return reverse('techstack', kwargs=kwargs)

class Project(models.Model):
    PRIVATE = 'P'
    PUBLIC = 'PB'

    STATUS = [
        (PRIVATE, 'private'),
        (PUBLIC, 'public')
    ]


    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=50, choices=STATUS)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    tech_stack = models.ManyToManyField(TechStack)
    url = models.URLField(max_length=200)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/projects/')
    started_on = models.DateField()
    finished_on = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
