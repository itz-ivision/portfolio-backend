from django.contrib import admin
from .models import HomePage


class HomePageAdmin(admin.ModelAdmin):
    """
    Admin interface for managing HomePage instances.
    """
    # Displayed fields in the list view
    list_display = (
        'header_title',
        'introduction',
        'call_to_action',
        'summary',
        'professional_summary'
    )

    # Fields to filter the list view
    list_filter = (
        'header_title',
        'introduction',
    )

    # Search fields in the list view
    search_fields = (
        'header_title',
        'introduction',
        'summary',
    )

    # Fields to be used in the detail view and edit form
    # fields = (
    #     'introduction',
    #     'call_to_action',
    #     'header_title',
    #     'header_subtitle',
    #     'summary',
    #     'professional_summary',
    #     'contact_info',
    #     'social_links'
    # )

    # Controls the layout of fields in the edit form
    fieldsets = (
        (None, {
            'fields': (
                'introduction',
                'call_to_action',
            )
        }),
        ('Header Information', {
            'fields': (
                'header_title',
                'header_subtitle',
            ),
            'classes': ('collapse',),  # Makes this section collapsible
        }),
        ('Summary', {
            'fields': (
                'summary',
                'professional_summary',
            ),
        }),
        ('Additional Information', {
            'fields': (
                'contact_info',
                'social_links',
            ),
            'classes': ('wide',),  # Makes this section wider
        }),
    )

    # Adding custom actions
    actions = ['clear_all_fields']

    def clear_all_fields(self, request, queryset):
        """
        Custom action to clear specific fields for selected HomePage instances.
        """
        updated_count = 0
        for home_page in queryset:
            home_page.introduction = ''
            home_page.call_to_action = ''
            home_page.header_title = ''
            home_page.header_subtitle = ''
            home_page.summary = ''
            home_page.professional_summary = ''
            home_page.contact_info = {}
            home_page.social_links = {}
            home_page.save()
            updated_count += 1

        self.message_user(request, f'{updated_count} HomePage instances were successfully updated.')

    clear_all_fields.short_description = "Clear all fields of selected HomePage instances"


# Register the HomePage model with the custom admin interface
admin.site.register(HomePage, HomePageAdmin)
