from django.contrib import admin
from .models import Skills, SkillsCategory


class SkillAdmin(admin.ModelAdmin):
    """
    Admin interface for managing skills.
    """
    list_display = ('name', 'proficiency', 'category')
    search_fields = ('name',)
    list_filter = ('category', 'proficiency')


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for managing categories.
    """
    list_display = ('name', 'description')
    search_fields = ('name',)


admin.site.register(Skills, SkillAdmin)
admin.site.register(SkillsCategory, CategoryAdmin)
