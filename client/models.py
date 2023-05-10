from django.db import models

from base.models import NULLABLE
from client.services import get_timezones
from client.validators import validate_phone


class Client(models.Model):
    """Model client"""
    TIMEZONES = get_timezones()
    phone = models.CharField(max_length=16, validators=[validate_phone], unique=True, verbose_name='phone')
    tag = models.CharField(max_length=64, **NULLABLE, verbose_name='tag')
    location = models.CharField(max_length=128, **NULLABLE, choices=TIMEZONES, verbose_name='location')
    is_active = models.BooleanField(default=True, verbose_name='is_active')

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'

    def __str__(self):
        return f'{self.phone}'
