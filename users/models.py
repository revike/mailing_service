from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from users.services import LowerCaseEmailField


class User(AbstractUser):
    """Model User"""
    email = LowerCaseEmailField(_("email address"), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f'{self.email}'
