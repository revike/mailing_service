import datetime

import pytz

from config.settings import DATETIME_FORMAT, REST_FRAMEWORK, TIME_ZONE
from main.models import Message
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


def start_mailing(mailing, clients, start, stop):
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
            send_mailing.apply_async(countdown=1, args=[msg_id, text, client.id, phone])
        if datetime_now < start:
            run_mailing = int((start-datetime_now).total_seconds())
            send_mailing.apply_async(countdown=run_mailing, args=[msg_id, text, client.id, phone])
        data_message = {
            'client_id': client.id,
            'mailing_id': msg_id,
            'created': datetime_now,
        }
        Message.objects.create(**data_message)
