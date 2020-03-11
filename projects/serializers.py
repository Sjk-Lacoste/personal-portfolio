from rest_framework import serializers
from .models import Skill, Category, TechStack, Project


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'slug', 'short_description', 'description', 'image',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'parent', 'short_description', 'description',)


class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = ('name', 'slug', 'short_description', 'description', 'image',)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'title',
            'slug',
            'status',
            'client',
            'tech_stack',
            'url',
            'short_description',
            'description',
            'image',
            'started_on',
            'finished_on',
            'is_complete',
        )
