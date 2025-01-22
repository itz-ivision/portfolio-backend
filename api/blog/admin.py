from django.contrib import admin
from .models import BlogPost, Tag, BlogCategory


class BlogPostAdmin(admin.ModelAdmin):
    """
        Admin interface for managing BlogPost instances.
    """
    list_display = ('title', 'author', 'published_date', 'slug')
    list_filter = ('published_date', 'author', 'categories')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    """
        Admin interface for managing Tag instances.
    """
    list_display = ('name',)
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
        Admin interface for managing Category instances.
    """
    list_display = ('name', 'description')
    search_fields = ('name',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(BlogCategory, CategoryAdmin)
