from rest_framework import serializers
from main.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'name',
            'slug',
            'short_description',
            'description',
            'icon'
        ]
