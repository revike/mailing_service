from django.urls import path

from client.views import ClientCreateApiView, LocationListApiView, ClientUpdateApiView, ClientDeleteApiView

app_name = 'client'

urlpatterns = [
    path('create/', ClientCreateApiView.as_view(), name='create'),
    path('update/<int:pk>/', ClientUpdateApiView.as_view(), name='update'),
    path('delete/<int:pk>/', ClientDeleteApiView.as_view(), name='delete'),

    path('locations/', LocationListApiView.as_view(), name='locations'),
]
