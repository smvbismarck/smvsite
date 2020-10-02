from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
import string
import secrets
from blog.models import Article
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
lorem_img_location = str(BASE_DIR) + "/static/lorem.jpg"

char_string = string.ascii_letters + string.digits
file_mock = SimpleUploadedFile(name='lorem.jpg', content=open(lorem_img_location, 'rb').read(), content_type='image/jpeg')


def getRandomString(size):
    return ''.join(secrets.choice(char_string) for _ in range(size))


# noinspection DuplicatedCode
class PageTests(TestCase):

    def test_root_status_code(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)


# noinspection DuplicatedCode
class TestEmpty(TestCase):
    def test_empty_is_template_used(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "index.html")


# noinspection DuplicatedCode
class TestSingle(TestCase):
    def test_single_title(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="test", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/")
        self.assertEquals(response.context["articles"][0].title, "test")

    def test_single_description(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="testdescription", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/")
        self.assertEquals(response.context["articles"][0].description, "testdescription")

    def test_single_body(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="test", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/")
        self.assertEquals(response.context["articles"][0].body, "lorem ipsum")

    def test_single_title_author(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="test", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/")
        self.assertEquals(response.context["articles"][0].author, superuser)

    def test_single_contains_title(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="testdescription", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/")
        self.assertIn(b"test", response.content)

    def test_single_contains_description(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="testdescription", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/")
        self.assertIn(b"testdescription", response.content)

    def test_single_contains_url(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="testdescription", body="lorem ipsum")
        test_article.save()
        response = self.client.get("/")
        self.assertIn(str.encode(reverse("article", args=[1])), response.content)


# noinspection DuplicatedCode
class TestRandomSingle(TestCase):
    def test_random_single_title(self):
        title = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title=title, description=getRandomString(5), body=getRandomString(10))
        test_article.save()
        response = self.client.get("/")
        self.assertEquals(response.context["articles"][0].title, title)

    def test_random_single_description(self):
        description = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title=getRandomString(5), description=description, body=getRandomString(10))  # noqa: E501
        test_article.save()
        response = self.client.get("/")
        self.assertEquals(response.context["articles"][0].description, description)

    def test_random_single_body(self):
        body = getRandomString(10)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title=getRandomString(5), description=getRandomString(5), body=body)
        test_article.save()
        response = self.client.get("/")
        self.assertEquals(response.context["articles"][0].body, body)

    def test_random_single_title_author(self):
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title=getRandomString(5), description=getRandomString(5), body=getRandomString(10))  # noqa: E501
        test_article.save()
        response = self.client.get("/")
        self.assertEquals(response.context["articles"][0].author, superuser)

    def test_random_single_contains_title(self):
        title = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title=title, description=getRandomString(5), body=getRandomString(10))
        test_article.save()
        response = self.client.get("/")
        self.assertIn(str.encode(title), response.content)

    def test_random_single_contains_description(self):
        description = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title=getRandomString(5), description=description, body=getRandomString(10))  # noqa: E501
        test_article.save()
        response = self.client.get("/")
        self.assertIn(str.encode(description), response.content)

    def test_random_single_contains_url(self):
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title=getRandomString(5), description=getRandomString(5), body=getRandomString(10))  # noqa: E501
        test_article.save()
        response = self.client.get("/")
        self.assertIn(str.encode(reverse("article", args=[1])), response.content)


# noinspection DuplicatedCode
class TestMulti(TestCase):
    def test_multi_title(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="test", body="lorem ipsum")
        test_article.save()
        test_article2 = Article(cover=file_mock, author=superuser, title="test2", description="test2", body="lorem ipsum2")
        test_article2.save()
        response = self.client.get("/")
        self.assertEquals(response.context["articles"][0].title, "test")
        self.assertEqual(response.context["articles"][1].title, "test2")

    def test_multi_description(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="testdescription", body="lorem ipsum")
        test_article.save()
        test_article2 = Article(cover=file_mock, author=superuser, title="test2", description="testdescription2", body="lorem ipsum2")
        test_article2.save()
        response = self.client.get("/")
        self.assertEquals(response.context["articles"][0].description, "testdescription")
        self.assertEquals(response.context["articles"][1].description, "testdescription2")

    def test_multi_body(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="test", body="lorem ipsum")
        test_article.save()
        test_article2 = Article(cover=file_mock, author=superuser, title="test2", description="testdescription2", body="lorem ipsum2")
        test_article2.save()
        response = self.client.get("/")
        self.assertEquals(response.context["articles"][0].body, "lorem ipsum")
        self.assertEquals(response.context["articles"][1].body, "lorem ipsum2")

    def test_multi_title_author(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="test", body="lorem ipsum")
        test_article.save()
        test_article2 = Article(cover=file_mock, author=superuser, title="test2", description="testdescription2", body="lorem ipsum2")
        test_article2.save()
        response = self.client.get("/")
        self.assertEquals(response.context["articles"][0].author, superuser)
        self.assertEquals(response.context["articles"][1].author, superuser)

    def test_multi_contains_title(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="testdescription", body="lorem ipsum")
        test_article.save()
        test_article2 = Article(cover=file_mock, author=superuser, title="test2", description="testdescription2", body="lorem ipsum2")
        test_article2.save()
        response = self.client.get("/")
        self.assertIn(b"test", response.content)
        self.assertIn(b"test2", response.content)

    def test_multi_contains_description(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="testdescription", body="lorem ipsum")
        test_article.save()
        test_article2 = Article(cover=file_mock, author=superuser, title="test2", description="testdescription2", body="lorem ipsum2")
        test_article2.save()
        response = self.client.get("/")
        self.assertIn(b"testdescription", response.content)
        self.assertIn(b"testdescription2", response.content)

    def test_multi_contains_url(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(cover=file_mock, author=superuser, title="test", description="testdescription", body="lorem ipsum")
        test_article.save()
        test_article2 = Article(cover=file_mock, author=superuser, title="test2", description="testdescription2", body="lorem ipsum2")
        test_article2.save()
        response = self.client.get("/")
        self.assertIn(str.encode(reverse("article", args=[1])), response.content)
        self.assertIn(str.encode(reverse("article", args=[2])), response.content)
