from django.contrib import admin
from .models import GithubRepo


class GithubRepoAdmin(admin.ModelAdmin):
    """
        Admin interface for managing GitHubRepository instances.
    """
    list_display = ('name', 'url', 'stars', 'forks', 'language', 'created_at')
    search_fields = ('name', 'description', 'language')
    list_filter = ('language', 'created_at')


admin.site.register(GithubRepo, GithubRepoAdmin)
