from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from client.models import Client
from client.serializers import ClientSerializer
from client.services import get_timezones


class ClientCreateApiView(generics.CreateAPIView):
    """Create client"""
    serializer_class = ClientSerializer


class ClientUpdateApiView(generics.UpdateAPIView):
    """Update client"""
    serializer_class = ClientSerializer
    queryset = Client.objects.filter(is_active=True)


class ClientDeleteApiView(generics.DestroyAPIView):
    """Delete client"""
    queryset = Client.objects.filter(is_active=True)

    def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = False
            instance.save()


class LocationListApiView(APIView):
    """Get list locations"""
    location_params = openapi.Parameter(
        'location', in_=openapi.IN_QUERY, description='location', type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[location_params])
    def get(self, request):
        search = request.GET.get('location', None)
        locations = get_timezones()
        data = [location[0] for location in locations]
        if search:
            data = [location for location in data if search.lower() in location.lower()]
        return Response(data, status=status.HTTP_200_OK)
