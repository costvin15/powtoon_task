import unittest
from rest_framework import status
from django.test import Client


class UserViewSetTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_register(self):
        response = self.client.post('/auth/register/', {
            'email': 'user@user.com',
            'password1': 'aIZtrBcF',
            'password2': 'aIZtrBcF'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        response = self.client.post('/auth/login/', {
            'email': 'user@user.com',
            'password': 'aIZtrBcF'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
