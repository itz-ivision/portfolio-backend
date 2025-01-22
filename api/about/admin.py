from django.contrib import admin
from .models import AboutPage


class AboutPageAdmin(admin.ModelAdmin):
    """
    Admin interface for managing AboutPage instances.
    """
    list_display = (
        'mission_statement',
        'values',
        'history'
    )

    search_fields = (
        'mission_statement',
        'values',
        'history',
    )

    fieldsets = (
        (None, {
            'fields': (
                'mission_statement',
                'values',
                'history',
            )
        }),
        ('Contact Information', {
            'fields': (
                'contact_info',
            ),
            'classes': ('wide',),
        }),
        ('Team Members', {
            'fields': (
                'team_members',
            ),
            'classes': ('wide',),
        }),
        ('Social Links', {
            'fields': (
                'social_links',
            ),
            'classes': ('wide',),
        }),
    )


# Register the AboutPage model with the custom admin interface
admin.site.register(AboutPage, AboutPageAdmin)
