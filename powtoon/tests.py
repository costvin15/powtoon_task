import unittest
from django.test import Client
from rest_framework import status


class PowtoonViewSetTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_create(self):
        login = self.client.post('/auth/login', {
            'email': 'user@user.com',
            'password': 'aIZtrBcF'
        })

        headers = {
            'HTTP_AUTHORIZATION': 'JWT ' + login.data.get('token')
        }

        response = self.client.post('/powtoon/', {
            'name': 'Powtoon 1',
            'content': '{"hello": "world"}',
            'owner': '1'
        }, **headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
