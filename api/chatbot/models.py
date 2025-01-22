from django.db import models

class FAQ(models.Model):
    question = models.TextField(unique=True)
    answer = models.TextField()

    def __str__(self):
        return self.question
