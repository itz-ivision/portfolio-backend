from django.db import models


class SkillsCategory(models.Model):
    """
        Category to group similar skills (e.g., Programming Languages, Frameworks).
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Skills(models.Model):
    """
        Represents a specific skill or tool.
    """
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)],
                                      help_text="Proficiency level from 1 to 10")
    category = models.ForeignKey(SkillsCategory, related_name='skills', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.proficiency}/10)"
