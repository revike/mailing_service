from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from users.models import User
from config.settings import ADMIN_EMAIL, ADMIN_PASSWORD


class Command(BaseCommand):
    """Команда для создания супер юзера"""

    def handle(self, *args, **options):
        password = make_password(ADMIN_PASSWORD)
        data = {
            'is_active': True,
            'is_staff': True,
            'is_superuser': True,
            'password': password,
        }
        User.objects.update_or_create(email=ADMIN_EMAIL, defaults=data)
