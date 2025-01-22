from rest_framework import serializers
from .models import Service, Technology


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology
        fields = ['id', 'name', 'description', 'version', 'website']


class ServiceSerializer(serializers.ModelSerializer):

    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = [
            'id', 'title', 'description', 'pricing', 'duration',
            'technologies', 'image', 'is_active', 'featured',
            'created_at', 'updated_at'
        ]
