from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from client.models import Client


class Tag(models.Model):
    """Model Tag"""
    tag = models.CharField(max_length=64, unique=True, verbose_name='tag')

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return f'{self.tag}'

    @receiver(post_save, sender=Client)
    def create_tag(sender, instance, created, **kwargs):
        if created:
            Tag.objects.get_or_create(tag=instance.tag)


class CodeMobile(models.Model):
    """Model Code Mobile"""
    code_mobile = models.CharField(max_length=3, unique=True, verbose_name='code mobile')

    class Meta:
        verbose_name = 'code mobile'
        verbose_name_plural = 'codes mobile'

    def __str__(self):
        return f'{self.code_mobile}'

    @receiver(post_save, sender=Client)
    def create_code_mobile(sender, instance, created, **kwargs):
        if created:
            CodeMobile.objects.get_or_create(code_mobile=instance.phone[1:4])


class Mailing(models.Model):
    """Model mailing"""
    message = models.TextField(verbose_name='message')
    mobile_codes = models.ManyToManyField(CodeMobile, blank=True, related_name='mailing_codes', verbose_name='codes')
    tags = models.ManyToManyField(Tag, blank=True, related_name='mailing_tags', verbose_name='tags')
    start = models.DateTimeField(verbose_name='start date time')
    stop = models.DateTimeField(verbose_name='stop date time')

    class Meta:
        verbose_name = 'mailing'
        verbose_name_plural = 'mailings'

    def __str__(self):
        return f'{self.id}'


class Message(models.Model):
    """Model message"""
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, null=True, related_name='msg_client', verbose_name='client')
    mailing = models.ForeignKey(
        Mailing, on_delete=models.SET_NULL, null=True, related_name='msg_mailing', verbose_name='mailing')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    send = models.BooleanField(default=False, verbose_name='send message')

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        return f'{self.client}'
