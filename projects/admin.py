from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Category,
    TechStack,
    Project
)


class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    prepopulated_fields = {"slug": ("name",)}

class TechStackAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('name', 'slug', 'short_description',)
    prepopulated_fields = {"slug": ("name",)}

class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('title', 'status', 'client', 'url','is_complete',)
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(TechStack, TechStackAdmin)
admin.site.register(Project, ProjectAdmin)
