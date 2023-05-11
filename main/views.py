from rest_framework import generics

from main.models import CodeMobile, Tag, Mailing
from main.serializers import MailingSerializer, MobileCodeSerializer, TagSerializer
from main.services import run_mailing


class MailingCreateApiView(generics.CreateAPIView):
    """Create mailing"""
    serializer_class = MailingSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        run_mailing(serializer)


class MailingUpdateApiView(generics.UpdateAPIView):
    """Update mailing"""
    serializer_class = MailingSerializer
    queryset = Mailing.objects.filter(is_active=True)

    def perform_update(self, serializer):
        super().perform_update(serializer)
        run_mailing(serializer, update=True)


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
