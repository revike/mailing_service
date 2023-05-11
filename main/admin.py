from django.contrib import admin

from client.models import Client
from config.settings import REST_FRAMEWORK
from main.filters import date_range_filter_builder
from main.models import Mailing, Message, TaskMailing
from main.services import start_mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    """Register Mailing to admin panel"""
    list_display = ['id', 'start', 'stop', 'is_active']
    list_display_links = list_display
    filter_horizontal = ['mobile_codes', 'tags']
    search_fields = ['mobile_codes__code_mobile', 'tags__tag']
    list_filter = (
        'is_active',
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

    def response_add(self, request, obj, post_url_continue=None):
        create_obj = super().response_add(request, obj, post_url_continue)
        self.run_mailing(obj)
        return create_obj

    def response_change(self, request, obj):
        change_obj = super().response_change(request, obj)
        self.run_mailing(obj, update=True)
        return change_obj

    @staticmethod
    def run_mailing(obj, update=False):
        start = obj.start.strftime(REST_FRAMEWORK['DATETIME_FORMAT'])
        stop = obj.stop.strftime(REST_FRAMEWORK['DATETIME_FORMAT'])
        mobile_codes = obj.mobile_codes.all().values_list('code_mobile', flat=True)
        tags = obj.tags.all().values_list('tag', flat=True)
        clients = Client.objects.filter(tag__in=tags, mobile_code__in=mobile_codes)
        if clients:
            mailing = {'id': obj.id, 'message': obj.message}
            if update:
                tasks_old = TaskMailing.objects.filter(
                    client_id__in=clients.values_list('id', flat=True), mailing_id=mailing.get('id'))
                tasks_old.delete()
            start_mailing(mailing, clients, start, stop)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Register Message to admin panel"""
    list_display = ['id', 'client', 'mailing', 'created', 'send']
    list_display_links = list_display
    search_fields = ['client__phone']
    list_filter = (
        'send',
        (
            'created', date_range_filter_builder(
                title='Created',
            )
        )
    )
    fields = ['client', 'mailing', 'send', 'created', 'get_message']
    readonly_fields = list_display

    def get_message(self, obj):
        if obj:
            return obj.mailing.message

    get_message.short_description = 'message'

    def has_add_permission(self, request):
        pass

    def has_change_permission(self, request, obj=None):
        pass
