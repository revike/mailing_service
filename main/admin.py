from django.contrib import admin

from main.filters import date_range_filter_builder
from main.models import Mailing, Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    """Register Mailing to admin panel"""
    list_display = ['id', 'start', 'stop']
    list_display_links = list_display
    filter_horizontal = ['mobile_codes', 'tags']
    search_fields = ['mobile_codes__code_mobile', 'tags__tag']
    list_filter = (
        (
            'start', date_range_filter_builder(
                title='Filter start',
            )
        ),
        (
            'stop',
            date_range_filter_builder(
                title='Filter stop',
            ),
        ),
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Register Message to admin panel"""
