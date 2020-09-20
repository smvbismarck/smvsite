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
        response = self.client.get("/article/test")
        self.assertEqual(response.status_code, 200)
