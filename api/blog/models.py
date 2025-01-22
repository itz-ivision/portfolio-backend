from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class BlogCategory(models.Model):
    """
        Model for categorizing blog post
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """
        Model for blog posts
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=500, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    categories = models.ManyToManyField(BlogCategory, blank=True, related_name='blog_posts')
    tags = models.ManyToManyField('Tag', blank=True, related_name='blog_posts')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    """
        Model for tags associated with blog post
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name