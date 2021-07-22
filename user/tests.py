import unittest
from django.test import Client


class UserViewSetTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_register(self):
        response = self.client.post('/auth/register/', {
            'email': 'user@user.com',
            'password1': 'password',
            'password2': 'password'
        })

        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post('/auth/login/', {
            'email': 'user@user.com',
            'password': 'password'
        })

        self.assertEqual(response.status_code, 200)
