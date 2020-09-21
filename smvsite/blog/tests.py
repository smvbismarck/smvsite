from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article


class route_tests(TestCase):
    def test_article_route_without_article(self):
        response = self.client.get("/article")
        self.assertEqual(response.status_code, 404)

    def test_article_route_undefined(self):
        response = self.client.get("/article/lol")
        self.assertEqual(response.status_code, 404)

    def test_article_route_int(self):
        response = self.client.get("/article/5")
        self.assertEqual(response.status_code, 404)

    def test_article_route_normal_behavior(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/article/1")
        self.assertEqual(response.status_code, 200)

    def test_article_route_normal_behavior_body(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/article/1")
        self.assertEqual(response.content, b"lorem ipsum")

    def test_article_route_id_as_name(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="1", description="test", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/article/1")
        self.assertEqual(response.status_code, 200)

    def test_article_route_id_as_name_body(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="1", description="test", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/article/1")
        self.assertEqual(response.content, b"lorem ipsum")

    def test_article_empty_name(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="", description="test", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/article/")
        self.assertEqual(response.status_code, 404)

    def test_article_empty(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="")
        test_article.save()
        response = self.client.get("/article/1")
        self.assertEqual(response.status_code, 200)

    def test_article_empty_body(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="")
        test_article.save()
        response = self.client.get("/article/1")
        self.assertEqual(response.content, b"")

    def test_article_without_text(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test")
        test_article.save()
        response = self.client.get("/article/1")
        self.assertEqual(response.status_code, 200)

    def test_article_without_text_body(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test")
        test_article.save()
        response = self.client.get("/article/1")
        self.assertEqual(response.content, b"")

    def test_description_empty(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/article/1")
        self.assertEqual(response.status_code, 200)

    def test_description_empty_body(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/article/1")
        self.assertEqual(response.content, b"lorem ipsum")

    def test_xss_protection(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="xss", description="test", body="<script>alert(1)</script>")
        test_article.save()
        response = self.client.get("/article/1")
        self.assertEqual(response.status_code, 200)

    def test_xss_protection_body(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="xss", description="test", body="<script>alert(1)</script>")
        test_article.save()
        response = self.client.get("/article/1")
        self.assertEqual(response.content, b"&lt;script&gt;alert(1)&lt;/script&gt;")
