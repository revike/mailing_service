import json
import pytz
from typing import Any
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User


class BaseTestCase(APITestCase):
    """Base class test"""
    access_token: str
    password = '123qwe456rty'

    def setUp(self) -> None:
        new_user = {
            'email': 'admin@example.com',
            'password': self.password,
            'is_active': True
        }
        self.maxDiff = None
        self.user = User.objects.create(**new_user)

    @staticmethod
    def _get_serialized_data(user, serializer_class):
        return serializer_class(user).data

    @staticmethod
    def _get_datetime_with_tz_as_string(datetime_item):
        return datetime_item. \
            astimezone(pytz.timezone(settings.TIME_ZONE)). \
            strftime(settings.DATETIME_FORMAT)

    def _login(self, email):
        self.client = APIClient()
        response = self.client.post(
            reverse('user:login'),
            {'email': email, 'password': self.password}
        )
        self.access_token = response.json().get('access')

    def _make_request(self, method: str, url: str, user_email: str = None, data: dict = None,
                      status_code: int = status.HTTP_200_OK, headers: dict = None) -> dict:
        headers_to_send = {}
        if user_email:
            self._login(user_email)
            headers_to_send = {"HTTP_AUTHORIZATION": f'Bearer {self.access_token}'}
            if headers is not None:
                headers_to_send.update(headers)
        request_data = {
            'path': url,
            'content_type': 'application/json',
        }

        request_data.update(headers_to_send)
        if data and method.lower() != 'get':
            request_data['data'] = json.dumps(data)
        elif method.lower() == 'get':
            request_data['data'] = data

        response = None

        if method == 'POST':
            response = self.client.post(
                **request_data
            )
        elif method == 'GET':
            response = self.client.get(
                **request_data
            )
        elif method == 'PATCH':
            response = self.client.patch(
                **request_data
            )
        elif method == 'PUT':
            response = self.client.put(
                **request_data
            )
        elif method == 'DELETE':
            response = self.client.delete(
                **request_data
            )

        self.assertIsNotNone(response)

        self.assertEqual(response.status_code, status_code)
        if method != 'DELETE':
            return response.json()

    def _make_post(self, url: str, user_email: str, data: Any, status_code: int, headers: dict = None):
        return self._make_request('POST', url, user_email, data, status_code, headers)

    def _make_get(self, url: str, user_email: str = None, params: dict = None, status_code: int = status.HTTP_200_OK,
                  headers: dict = None):
        return self._make_request('GET', url, user_email, params, status_code, headers)

    def _make_patch(self, url: str, user_email: str, data: dict, status_code: int = status.HTTP_200_OK,
                    headers: dict = None):
        return self._make_request('PATCH', url, user_email, data, status_code, headers)

    def _make_put(self, url: str, user_email: str, data: dict, status_code: int = status.HTTP_200_OK,
                  headers: dict = None):
        return self._make_request('PUT', url, user_email, data, status_code, headers)

    def _make_delete(self, url: str, user_email: str, data: dict = None, status_code: int = status.HTTP_204_NO_CONTENT,
                     headers: dict = None):
        return self._make_request('DELETE', url, user_email, data, status_code, headers)
