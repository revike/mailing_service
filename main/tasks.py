import requests
from celery import shared_task

from config.settings import MAILING_URL, MAILING_TOKEN
from main.models import Message


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 6, 'countdown': 10})
def send_mailing(msg_id, text, client_id, phone, send=False):
    """Send mailing now"""
    data = {
        'id': msg_id,
        'phone': int(phone),
        'text': text
    }
    headers = {
        'Authorization': MAILING_TOKEN,
        'Content-Type': 'application/json'
    }
    data_message = {
        'client_id': client_id,
        'mailing_id': msg_id,
    }
    response = requests.post(url=f'{MAILING_URL}/send/{msg_id}', json=data, headers=headers)
    if response.ok:
        send = True
    Message.objects.update_or_create(**data_message, defaults={'send': send})
