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
        start = datetime_str_to_datetime(data.get('start'))
        stop = datetime_str_to_datetime(data.get('stop'))
        if stop <= start:
            raise ValidationError({'message': 'stop < start'})
        super().save(**kwargs)


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
