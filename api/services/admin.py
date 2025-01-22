from django.contrib import admin
from .models import Service, Technology


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'pricing', 'duration', 'is_active', 'featured')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'featured', 'technologies')
    filter_horizontal = ('technologies',)
    readonly_fields = ('created_at', 'updated_at')


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'version')
    search_fields = ('name', 'description')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Technology, TechnologyAdmin)
