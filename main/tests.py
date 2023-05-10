from datetime import timedelta

from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from base.tests import BaseTestCase
from main.models import Mailing


class TestMailing(BaseTestCase):
    """Test Mailing"""

    def setUp(self) -> None:
        super().setUp()
        mailing_data = {
            'message': 'test_mailing',
            'start': f'{timezone.now()}',
            'stop': f'{timezone.now() + timedelta(days=1)}',
            'is_active': True,
        }
        self.mailing = Mailing.objects.create(**mailing_data)

    def test_create_mailing(self):
        """Test create mailing"""
        url = reverse('mailing:create')
        data = {'message': 'msg', 'start': f'{timezone.now()}', 'stop': f'{timezone.now() + timedelta(days=1)}'}
        response = self._make_post(url, '', data, status.HTTP_201_CREATED)
        self.assertEqual(response['message'], data['message'])

    def test_update_mailing(self):
        """Test update mailing"""
        url = reverse('mailing:update', kwargs={'pk': self.mailing.id})
        data = {'message': 'new_text'}
        response = self._make_patch(url, '', data)
        self.assertNotEqual(response['message'], self.mailing.message)

    def test_delete_mailing(self):
        """Test delete mailing"""
        url = reverse('mailing:delete', kwargs={'pk': self.mailing.id})
        response = self._make_delete(url, '')
        self.assertEqual(response, None)
        mailing = Mailing.objects.get(id=self.mailing.id)
        self.assertEqual(mailing.is_active, False)

    def test_code_mobile(self):
        """Test code mobile"""
        url = reverse('mailing:mobile_code')
        response = self._make_get(url)
        self.assertEqual(len(response), 0)

    def test_tags(self):
        """Test tag"""
        url = reverse('mailing:tags')
        response = self._make_get(url)
        self.assertEqual(len(response), 0)
