from django.test import TestCase


class PageTests(TestCase):

    def test_root_status_code(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)


# noinspection DuplicatedCode
class TestEmpty(TestCase):
    def test_empty_is_template_used(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "index.html")