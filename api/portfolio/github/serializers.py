from rest_framework import serializers
from .models import GithubRepo


class GithubRepoSerializer(serializers.ModelSerializer):
    """
        Serializer for GitHubRepository model.
    """
    class Meta:
        model = GithubRepo
        fields = ['id', 'name', 'description', 'image', 'video', 'url',
                  'stars', 'forks', 'language', 'created_at']
        read_only_fields = ['created_at']