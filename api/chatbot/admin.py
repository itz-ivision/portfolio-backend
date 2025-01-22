from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')
    search_fields = ('question', 'answer')  # Allows searching by question or answer
    list_per_page = 20  # Pagination for long FAQ lists


admin.site.register(FAQ, FAQAdmin)