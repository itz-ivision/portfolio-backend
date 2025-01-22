from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    issuer = models.CharField(max_length=255)
    date = models.DateField()
    link = models.URLField()
    preview_image = models.URLField()

    def __str__(self):
        return self.title
