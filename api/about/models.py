from django.db import models


class AboutPage(models.Model):

    mission_statement = models.TextField()
    values = models.TextField()
    history = models.TextField()
    team_members = models.JSONField(default=dict, help_text="List of team members with details.")
    contact_info = models.JSONField(default=dict, help_text="Contact Information.")
    social_links = models.JSONField(default=dict, help_text="Social media links.")

    def __str__(self):
        return "About Us"

