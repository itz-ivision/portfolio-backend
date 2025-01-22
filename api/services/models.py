from django.db import models


class Technology(models.Model):
    """
        Represents a technology or tool used in services.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    icon_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    """
        Represents a service offered by the agency.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    pricing = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the service in USD")
    duration = models.CharField(max_length=100, help_text="Estimated time to complete the service")
    technologies = models.ManyToManyField(Technology, related_name='services')
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False, help_text="Highlight this service on the homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.pricing}"
