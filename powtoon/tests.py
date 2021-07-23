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

        self.assertEqual(login.status_code, status.HTTP_200_OK)

        headers = {
            'HTTP_AUTHORIZATION': 'JWT ' + login.data.get('token')
        }

        response = self.client.post('/powtoon/', {
            'name': 'Powtoon 1',
            'content': '{"hello": "world"}',
            'owner': '1'
        }, **headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read(self):
        login = self.client.post('/auth/login', {
            'email': 'user@user.com',
            'password': 'aIZtrBcF'
        })

        self.assertEqual(login.status_code, status.HTTP_200_OK)

        headers = {
            'HTTP_AUTHORIZATION': 'JWT ' + login.data.get('token')
        }

        response = self.client.get('/powtoon/1/', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        login = self.client.post('/auth/login', {
            'email': 'user@user.com',
            'password': 'aIZtrBcF'
        })

        self.assertEqual(login.status_code, status.HTTP_200_OK)

        headers = {
            'HTTP_AUTHORIZATION': 'JWT ' + login.data.get('token')
        }

        response = self.client.patch('/powtoon/1/', {
            'name': 'Updated powtoon 1'
        }, content_type='application/json', **headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        login = self.client.post('/auth/login', {
            'email': 'user@user.com',
            'password': 'aIZtrBcF'
        })

        self.assertEqual(login.status_code, status.HTTP_200_OK)

        headers = {
            'HTTP_AUTHORIZATION': 'JWT ' + login.data.get('token')
        }

        response = self.client.delete('/powtoon/2/', **headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_share(self):
        login = self.client.post('/auth/login', {
            'email': 'user@user.com',
            'password': 'aIZtrBcF'
        })

        self.assertEqual(login.status_code, status.HTTP_200_OK)

        headers = {
            'HTTP_AUTHORIZATION': 'JWT ' + login.data.get('token')
        }

        share = self.client.patch('/powtoon/1/', {
            'shared_with': [2]
        }, content_type='application/json', **headers)

        self.assertEqual(share.status_code, status.HTTP_200_OK)

    def test_shared(self):
        login = self.client.post('/auth/login', {
            'email': 'user@user.com',
            'password': 'aIZtrBcF'
        })

        self.assertEqual(login.status_code, status.HTTP_200_OK)

        headers = {
            'HTTP_AUTHORIZATION': 'JWT ' + login.data.get('token')
        }

        shared = self.client.get('/user/1/shared_with_me/', **headers)
        self.assertEqual(shared.status_code, status.HTTP_200_OK)
