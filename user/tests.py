import unittest
from django.test import Client


class UserViewSetTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_register(self):
        self.client.post('/auth/register', {
            'email': 'user@user.com',
            'password1': 'password',
            'password2': 'password'
        })

    def test_login(self):
        self.client.post('/auth/login', {
            'email': 'user@user.com',
            'password': 'password'
        })
