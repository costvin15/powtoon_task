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

    def become_admin(self):
        login = self.client.post('/auth/login/', {
            'email': 'user@user.com',
            'password': 'aIZtrBcF'
        })

        self.assertEqual(login.status_code, status.HTTP_200_OK)

        headers = {
            'HTTP_AUTHORIZATION': 'JWT ' + login.data.get('token')
        }

        response = self.client.post('/user/1/add_to_group/', {
            'group': 1
        }, content_type='application/json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
