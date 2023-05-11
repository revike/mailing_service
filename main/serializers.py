from django.db.models import Count, Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from main.models import Mailing, CodeMobile, Tag
from main.services import datetime_str_to_datetime


class MailingSerializer(serializers.ModelSerializer):
    """Serializer for mailing"""

    class Meta:
        model = Mailing
        fields = ('id', 'message', 'mobile_codes', 'tags', 'start', 'stop', 'is_active')

    def to_representation(self, instance):
        mobile_codes = [code.code_mobile for code in instance.mobile_codes.all()]
        tags = [tag.tag for tag in instance.tags.all()]
        representation = super().to_representation(instance)
        representation['mobile_codes'] = mobile_codes
        representation['tags'] = tags
        return representation

    def save(self, **kwargs):
        data = self.context['request'].data
        start, stop = data.get('start'), data.get('stop')
        if start and stop:
            start = datetime_str_to_datetime(start)
            stop = datetime_str_to_datetime(stop)
            if stop <= start:
                raise ValidationError({'message': 'stop < start'})
        super().save(**kwargs)


class StatisticSerializer(serializers.ModelSerializer):
    """Serializer for statistics"""

    class Meta:
        model = Mailing
        fields = ('id', 'message', 'is_active')

    def to_representation(self, instance):
        message_count = instance.msg_mailing.aggregate(
            send=Count('mailing', filter=Q(send=True)),
            not_send=Count('mailing', filter=Q(send=False))
        )
        representation = super().to_representation(instance)
        representation['message_count'] = message_count
        return representation


class MobileCodeSerializer(serializers.ModelSerializer):
    """Serializer for mobile code"""

    class Meta:
        model = CodeMobile
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag"""

    class Meta:
        model = Tag
        fields = '__all__'
