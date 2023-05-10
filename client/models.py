from django.db import models

from client.services import get_timezones
from client.validators import validate_phone


class Client(models.Model):
    """Model client"""
    TIMEZONES = get_timezones()
    phone = models.CharField(max_length=16, validators=[validate_phone], unique=True, verbose_name='phone')
    tag = models.CharField(max_length=64, verbose_name='tag')
    location = models.CharField(max_length=128, choices=TIMEZONES, verbose_name='location')

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'

    def __str__(self):
        return f'{self.phone}'
