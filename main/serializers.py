from rest_framework import serializers

from main.models import Mailing, CodeMobile, Tag


class MailingSerializer(serializers.ModelSerializer):
    """Serializer for mailing"""

    class Meta:
        model = Mailing
        fields = ('id', 'message', 'mobile_codes', 'tags', 'start', 'stop')


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
