from rest_framework import serializers
from projects.models import (
    Category,
    TechStack,
    Project
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'slug',
            'parent',
            'short_description',
            'description'
        ]


class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = [
            'name',
            'slug',
            'short_description',
            'description',
            'image'
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
