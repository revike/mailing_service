from django.urls import path

from main.views import MailingCreateApiView, MobileCodeListApiView, TagListApiView, MailingUpdateApiView, \
    MailingDeleteApiView, StatisticListApiView, StatisticDetailApiView

app_name = 'main'

urlpatterns = [
    path('create/', MailingCreateApiView.as_view(), name='create'),
    path('update/<int:pk>/', MailingUpdateApiView.as_view(), name='update'),
    path('delete/<int:pk>/', MailingDeleteApiView.as_view(), name='delete'),

    path('statistics/', StatisticListApiView.as_view(), name='statistics'),
    path('statistic/<int:mailing_id>/', StatisticDetailApiView.as_view(), name='statistic_detail'),

    path('mobile/codes/', MobileCodeListApiView.as_view(), name='mobile_code'),
    path('tags/', TagListApiView.as_view(), name='tags'),
]
