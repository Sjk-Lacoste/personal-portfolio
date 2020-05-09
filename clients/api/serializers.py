from rest_framework import serializers
from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'name',
            'slug',
            'email',
            'phone_number',
            'website_url',
            'logo'
        ]
