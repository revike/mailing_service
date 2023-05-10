from rest_framework import serializers

from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for create or update client"""

    class Meta:
        model = Client
        fields = ('id', 'phone', 'tag', 'location')
