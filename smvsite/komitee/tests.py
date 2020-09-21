from django.test import TestCase
from .models import Komitee


# TODO Rename the funcs
class route_tests(TestCase):
    def test_article_route_without_article(self):
        response = self.client.get("/komitee")
        self.assertEqual(response.status_code, 404)

    def test_komitee_route_undefined(self):
        response = self.client.get("/komitee/lol")
        self.assertEqual(response.status_code, 404)

    def test_komitee_route_int(self):
        response = self.client.get("/komitee/5")
        self.assertEqual(response.status_code, 404)

    def test_komitee_route_normal_behavior(self):
        test_komitee = Komitee(title="test", description="test", body="lorem ipsum")
        test_komitee.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.status_code, 200)

    def test_komitee_route_normal_behavior_body(self):
        test_komitee = Komitee(title="test", description="test", body="lorem ipsum")
        test_komitee.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.content, b"lorem ipsum")

    def test_komitee_route_id_as_name(self):
        test_komitee = Komitee(title="1", description="test", body="lorem ipsum")
        test_komitee.save()
        response = self.client.get("/komitee/1")
        self.assertEqual(response.status_code, 200)

    def test_komitee_route_id_as_name_body(self):
        test_komitee = Komitee(title="1", description="test", body="lorem ipsum")
        test_komitee.save()
        response = self.client.get("/komitee/1")
        self.assertEqual(response.content, b"lorem ipsum")

    def test_komitee_empty_name(self):
        test_komitee = Komitee(title="", description="test", body="lorem ipsum")
        test_komitee.save()
        response = self.client.get("/komitee/")
        self.assertEqual(response.status_code, 404)

    def test_komitee_empty(self):
        test_komitee = Komitee(title="test", description="test", body="")
        test_komitee.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.status_code, 200)

    def test_komitee_empty_body(self):
        test_komitee = Komitee(title="test", description="test", body="")
        test_komitee.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.content, b"")

    def test_komitee_without_text(self):
        test_komitee = Komitee(title="test", description="test")
        test_komitee.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.status_code, 200)

    def test_komitee_without_text_body(self):
        test_komitee = Komitee(title="test", description="test", body="")
        test_komitee.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.content, b"")

    def test_description_empty(self):
        test_komitee = Komitee(title="test", description="", body="lorem ipsum")
        test_komitee.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.status_code, 200)

    def test_description_empty_body(self):
        test_komitee = Komitee(title="test", description="", body="lorem ipsum")
        test_komitee.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.content, b"lorem ipsum")

    def test_special_char_name(self):
        test_komitee = Komitee(title="§&%&())", description="test", body="lorem ipsum")
        test_komitee.save()
        response = self.client.get("/komitee/§&%&())")
        self.assertEqual(response.status_code, 200)

    def test_special_char_name_body(self):
        test_komitee = Komitee(title="§&%&())", description="test", body="lorem ipsum")
        test_komitee.save()
        response = self.client.get("/komitee/§&%&())")
        self.assertEqual(response.content, b"lorem ipsum")

    def test_xss_protection(self):
        test_komitee = Komitee(title="xss", description="test", body="<script>alert(1)</script>")
        test_komitee.save()
        response = self.client.get("/komitee/xss")
        self.assertEqual(response.status_code, 200)

    def test_xss_protection_body(self):
        test_komitee = Komitee(title="xss", description="test", body="<script>alert(1)</script>")
        test_komitee.save()
        response = self.client.get("/komitee/xss")
        self.assertEqual(response.content, b"&lt;script&gt;alert(1)&lt;/script&gt;")
