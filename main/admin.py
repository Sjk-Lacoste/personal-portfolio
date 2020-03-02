from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


class ServiceAdmin(SummernoteModelAdmin):
    summenote_field = '__all__'
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug':('name',)}


# Register your models here.
admin.site.register(Service, ServiceAdmin)