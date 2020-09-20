from django.test import TestCase


class PageTests(TestCase):

    def test_root_status_code(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_root_content(self):
        response = self.client.get("/")
        self.assertEquals(response.content, b"Hello World")

# Create your tests here.
