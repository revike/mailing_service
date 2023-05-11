from django.urls import reverse
from rest_framework import status

from base.tests import BaseTestCase
from client.models import Client


class TestClient(BaseTestCase):
    """Test Client"""

    def setUp(self) -> None:
        super().setUp()
        client_data = {
            'phone': '79290342123',
            'tag': 'test_tag',
            'is_active': True,
        }
        self.client_ = Client.objects.create(**client_data)

    def test_create_client(self):
        """Test create client"""
        url = reverse('client:create')
        data = {'phone': '79200405111', 'tag': 'tag'}
        response = self._make_post(url, '', data, status.HTTP_201_CREATED)
        self.assertEqual(response['phone'], data['phone'])

    def test_update_client(self):
        """Test update client"""
        url = reverse('client:update', kwargs={'pk': self.client_.id})
        data = {'tag': 'my_tag'}
        response = self._make_patch(url, '', data, status.HTTP_200_OK)
        self.assertNotEqual(response['tag'], self.client_.tag)

    def test_delete_client(self):
        """Test delete client"""
        url = reverse('client:delete', kwargs={'pk': self.client_.id})
        response = self._make_delete(url, '')
        self.assertEqual(response, None)
        client = Client.objects.get(id=self.client_.id)
        self.assertEqual(client.is_active, False)

    def test_location(self):
        """Test locations"""
        url = reverse('client:locations')
        response = self._make_get(url)
        self.assertNotEqual(len(response), 0)

        url += '?location=moscow'
        response = self._make_get(url)
        self.assertEqual(len(response), 1)
