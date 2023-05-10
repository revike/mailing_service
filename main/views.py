from rest_framework import generics

from main.models import CodeMobile, Tag, Mailing
from main.serializers import MailingSerializer, MobileCodeSerializer, TagSerializer


class MailingCreateApiView(generics.CreateAPIView):
    """Create mailing"""
    serializer_class = MailingSerializer


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
