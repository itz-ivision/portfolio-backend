from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class ContactMessage(models.Model):
    """
        Model to store contact messages from users.
    """
    CONTACT_REASONS = [
        ('inquiry', 'General Inquiry'),
        ('hire', 'Hire'),
        ('support', 'Support Request'),
        ('collaboration', 'Collaboration'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                   message="Phone number must be entered in the format: "
                                           "'+999999999'. Up to 15 digits allowed.")]
    )
    subject = models.CharField(max_length=255)
    reason = models.CharField(max_length=20, choices=CONTACT_REASONS, default='inquiry')
    other_reason = models.CharField(max_length=255, blank=True, null=True)  # Field for custom reason
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)  # To track if the message has been read

    class Meta:
        ordering = ['-sent_at']
        indexes = [
            models.Index(fields=['sent_at']),
            models.Index(fields=['read']),
        ]

    def __str__(self):
        return f'{self.name} - {self.subject}'
