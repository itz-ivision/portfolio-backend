from django.db import models
from django.utils import timezone


class GithubRepo(models.Model):
    """
        Model to store information about GitHub repositories.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    url = models.URLField()
    stars = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)
    language = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
