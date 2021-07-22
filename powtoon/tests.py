import unittest
from django.test import Client


class PowtoonViewSetTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_create(self):
        response = self.client.post('/powtoon/', {
            'name': 'Powtoon 1',
            'content': '{"hello": "world"}',
            'owner': '1'
        })
        self.assertEqual(response.status_code, 200)
