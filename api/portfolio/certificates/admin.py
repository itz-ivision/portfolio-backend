from django.contrib import admin
from .models import Certificate


class CertificateAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Certificate model.
    """
    list_display = ("title", "issuer", "date")  # Fields displayed in the list view
    search_fields = ("title", "issuer")  # Fields searchable in the admin
    list_filter = ("issuer", "date")  # Filters for the list view
    ordering = ("-date",)  # Default ordering by date, descending


admin.site.register(Certificate, CertificateAdmin)