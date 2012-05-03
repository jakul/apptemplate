from django.test import TestCase, Client

from apptemplate import VERSION

class VersionViewTest(TestCase):
    def test_basic(self):
        client = Client()
        response = client.get('/version/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, VERSION)
