from django.db import models


class HomePage(models.Model):

    introduction = models.TextField()
    header_title = models.CharField(max_length=200, blank=True, null=True)
    header_subtitle = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    professional_summary = models.TextField(blank=True, null=True)
    # key_skills = models.JSONField(blank=True, null=True)  # Store key skills as a list of strings
    # featured_projects = models.JSONField(blank=True, null=True)  # Store featured projects with titles and links
    call_to_action = models.URLField()
    contact_info = models.JSONField(blank=True, null=True)  # Store contact information like email, phone, etc.
    social_links = models.JSONField(blank=True, null=True)  # Store social media links like LinkedIn, Twitter, etc.

    def __str__(self):
        return "HomePage"
