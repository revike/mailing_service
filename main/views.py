from rest_framework import generics

from client.models import Client
from main.models import CodeMobile, Tag, Mailing
from main.serializers import MailingSerializer, MobileCodeSerializer, TagSerializer
from main.services import start_mailing


class MailingCreateApiView(generics.CreateAPIView):
    """Create mailing"""
    serializer_class = MailingSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        mailing = serializer.data
        start = mailing.get('start')
        stop = mailing.get('stop')
        mobile_codes = mailing.get('mobile_codes')
        tags = mailing.get('tags')
        clients = Client.objects.filter(tag__in=tags, mobile_code__in=mobile_codes)
        if clients:
            start_mailing(mailing, clients, start, stop)


class MailingUpdateApiView(generics.UpdateAPIView):
    """Update mailing"""
    serializer_class = MailingSerializer
    queryset = Mailing.objects.filter(is_active=True)


class MailingDeleteApiView(generics.DestroyAPIView):
    """Delete mailing"""
    queryset = Mailing.objects.filter(is_active=True)

    def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = False
            instance.save()


class MobileCodeListApiView(generics.ListAPIView):
    """Get list mobile codes"""
    serializer_class = MobileCodeSerializer
    queryset = CodeMobile.objects.all()


class TagListApiView(generics.ListAPIView):
    """Get list tags"""
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
