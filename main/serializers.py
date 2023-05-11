import datetime
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from config.settings import DATETIME_FORMAT
from main.models import Mailing, CodeMobile, Tag


class MailingSerializer(serializers.ModelSerializer):
    """Serializer for mailing"""

    class Meta:
        model = Mailing
        fields = ('id', 'message', 'mobile_codes', 'tags', 'start', 'stop')

    def to_representation(self, instance):
        mobile_codes = [code.code_mobile for code in instance.mobile_codes.all()]
        tags = [tag.tag for tag in instance.tags.all()]
        representation = super().to_representation(instance)
        representation['mobile_codes'] = mobile_codes
        representation['tags'] = tags
        return representation

    def save(self, **kwargs):
        data = self.context['request'].data
        start_str = data.get('start')
        stop_str = data.get('stop')
        start = datetime.datetime.strptime(start_str, DATETIME_FORMAT)
        stop = datetime.datetime.strptime(stop_str, DATETIME_FORMAT)
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
