from rest_framework import generics
from rest_framework.generics import get_object_or_404

from main.models import CodeMobile, Tag, Mailing
from main.serializers import MailingSerializer, MobileCodeSerializer, TagSerializer, StatisticSerializer
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


class StatisticListApiView(generics.ListAPIView):
    """Mailing statistics"""
    serializer_class = StatisticSerializer
    queryset = Mailing.objects.all()


class StatisticDetailApiView(generics.RetrieveAPIView):
    """Mailing statistic detail"""
    serializer_class = StatisticSerializer
    queryset = Mailing.objects.all()
    lookup_field = ('mailing_id',)

    def get_object(self):
        mailing_id = self.kwargs.get('mailing_id')
        return get_object_or_404(self.queryset, id=mailing_id)


class MobileCodeListApiView(generics.ListAPIView):
    """Get list mobile codes"""
    serializer_class = MobileCodeSerializer
    queryset = CodeMobile.objects.all()


class TagListApiView(generics.ListAPIView):
    """Get list tags"""
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
