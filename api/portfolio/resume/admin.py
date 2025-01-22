from django.contrib import admin
from .models import Resume


class ResumeAdmin(admin.ModelAdmin):
    """
    Admin interface for managing resumes.
    """
    # Display relevant fields in the list view
    list_display = ('title', 'resume_format', 'created_at', 'updated_at')
    
    # Enable search functionality for title and resume_url
    search_fields = ('title', 'resume_url')
    
    # Add filters for resume format and date range
    list_filter = ('resume_format', 'created_at', 'updated_at')
    
    # Allow filtering by resume format in the list view
    list_editable = ('resume_format',)
    
    # Add date hierarchy for easy navigation of records by date
    date_hierarchy = 'created_at'


admin.site.register(Resume, ResumeAdmin)
