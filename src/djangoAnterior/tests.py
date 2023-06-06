from django.test import TestCase, Client


class IndexViewTest(TestCase):
    def test_index_view(self):
        client = Client()
        response = client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn(response.content.decode(), "<h1>Hello, world !</h1>", )
