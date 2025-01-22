from django.db import models
from django.utils import timezone

class Resume(models.Model):
    """
     Model to store resume files.
    """
    PDF = 'pdf'
    DOCX = 'docx'
    RESUME_FORMAT_CHOICES = [
        (PDF, 'PDF'),
        (DOCX, 'DOCX'),
    ]

    title = models.CharField(max_length=255, verbose_name="Resume Title")
    resume_format = models.CharField(
        max_length=4,
        choices=RESUME_FORMAT_CHOICES,
        default=PDF,
        verbose_name="Resume Format"
    )
    resume_url = models.URLField(blank=False, verbose_name="Resume URL")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Date Created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    class Meta:
        indexes = [
            models.Index(fields=['resume_url']),
            models.Index(fields=['resume_format']),
        ]
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"
    
    def __str__(self):
        return self.title
