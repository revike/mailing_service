import datetime

import pytz
from django.db.models import Q

from client.models import Client
from config.settings import DATETIME_FORMAT, REST_FRAMEWORK, TIME_ZONE
from main.models import Message, TaskMailing
from main.tasks import send_mailing


def datetime_str_to_datetime(date_time, date_time_format=None):
    """Datetime string to datetime"""
    if date_time_format is None:
        date_time_format = DATETIME_FORMAT
    try:
        return datetime.datetime.strptime(date_time, date_time_format)
    except ValueError:
        date_time_format = REST_FRAMEWORK['DATETIME_FORMAT']
        return datetime.datetime.strptime(date_time, date_time_format)


def start_mailing(mailing, clients, start, stop, task_id=None):
    """Start mailing"""
    msg_id, text = mailing.get('id'), mailing.get('message')
    start = datetime_str_to_datetime(start)
    stop = datetime_str_to_datetime(stop)

    for client in clients:
        tz = 'UTC'
        if client.location:
            tz = client.location.split('-')[-1].strip()
        datetime_now = datetime.datetime.now(pytz.timezone(tz))
        start = start.astimezone(pytz.timezone(TIME_ZONE))
        stop = stop.astimezone(pytz.timezone(TIME_ZONE))
        phone = client.phone
        if start < datetime_now < stop:
            task_id = send_mailing.apply_async(countdown=1, args=[msg_id, text, client.id, phone])
        if datetime_now < start:
            seconds = int((start - datetime_now).total_seconds())
            task_id = send_mailing.apply_async(countdown=seconds, args=[msg_id, text, client.id, phone])
        data_message = {
            'client_id': client.id,
            'mailing_id': msg_id,
            'created': datetime_now,
        }
        Message.objects.create(**data_message)
        if task_id:
            TaskMailing.objects.update_or_create(client_id=client.id, mailing_id=msg_id, defaults={'task_id': task_id})


def run_mailing(serializer, update=False):
    """Run mailing"""
    mailing = serializer.data
    start = mailing.get('start')
    stop = mailing.get('stop')
    is_active = mailing.get('is_active')
    mobile_codes = mailing.get('mobile_codes')
    tags = mailing.get('tags')
    clients = Client.objects.filter(Q(tag__in=tags) | Q(mobile_code__in=mobile_codes)).distinct()
    if clients:
        if update:
            tasks_old = TaskMailing.objects.filter(
                client_id__in=clients.values_list('id', flat=True), mailing_id=mailing.get('id'))
            tasks_old.delete()
        if is_active:
            start_mailing(mailing, clients, start, stop)
