from django.contrib import admin

from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Register Client to admin panel"""
    list_display = ['id', 'phone', 'tag', 'location']
    list_display_links = list_display
    search_fields = list_display[1:]
    list_filter = ['tag']
