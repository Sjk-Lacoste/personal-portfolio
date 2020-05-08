from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Skill


class SkillAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('name', 'slug', 'short_description',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Skill, SkillAdmin)
