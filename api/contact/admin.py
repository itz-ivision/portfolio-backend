from django.contrib import admin
from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    """
        Admin interface for managing ContactMessage instances.
    """
    list_display = ('name', 'email', 'phone', 'subject', 'reason', 'sent_at', 'read')
    list_filter = ('sent_at', 'read', 'reason')
    search_fields = ('name', 'email', 'subject', 'message')
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        """
            Action to mark selected message as read
        """
        rows_updated = queryset.update(read=True)

        if rows_updated == 1:
            message_bit = "1 message"
        else:
            message_bit = f"{rows_updated} message"
        self.message_user(request, f"{message_bit} were successfully marked as read.")

    mark_as_read.sort_description = "Mark selected messages as read."


admin.site.register(ContactMessage, ContactMessageAdmin)
