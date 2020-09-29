from django.test import TestCase
from django.contrib.auth.models import User
import secrets
import string
from blog import models as blog_models

Article = blog_models.Article
char_string = string.ascii_letters + string.digits


def getRandomString(size):
    return ''.join(secrets.choice(char_string) for _ in range(size))


# noinspection DuplicatedCode
class Test404(TestCase):
    def test_article_route_without_article(self):
        response = self.client.get("/komitee")
        self.assertEqual(response.status_code, 404)

    def test_article_route_undefined(self):
        response = self.client.get("/komitee/lol")
        self.assertEqual(response.status_code, 404)


# noinspection DuplicatedCode
class TestNormal(TestCase):
    def test_normal_behaviour(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="lorem ipsum", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.status_code, 200)

    def test_normal_behaviour_is_template_used(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="lorem ipsum", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertTemplateUsed(response, "detail.html")

    def test_normal_behaviour_context(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="lorem ipsum", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.context["article"], test_article)

    def test_normal_behaviour_context_author(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="lorem ipsum", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.context["article"].author, superuser)

    def test_normal_behaviour_context_title(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="lorem ipsum", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.context["article"].title, "test")

    def test_normal_behaviour_context_description(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="testdescription", body="lorem ipsum", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.context["article"].description, "testdescription")

    def test_normal_behaviour_context_body(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="testdescription", body="lorem ipsum", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.context["article"].body, "lorem ipsum")

    def test_normal_behaviour_context_is_post(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="testdescription", body="lorem ipsum", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.context["article"].is_post, False)

    def test_normal_behaviour_contains_title(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="testdescription", body="lorem ipsum", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertIn(b"test", response.content)

    def test_normal_behaviour_contains_body(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="testdescription", body="lorem ipsum", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertIn(b"lorem ipsum", response.content)


# noinspection DuplicatedCode
class TestRandomBehaviour(TestCase):
    def test_random_behaviour(self):
        title = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title=title, description=getRandomString(5),
                               body=getRandomString(10), is_post=False)
        test_article.save()
        response = self.client.get("/komitee/" + title)
        self.assertEqual(response.status_code, 200)

    def test_normal_behaviour_is_template_used(self):
        title = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title=title, description=getRandomString(5),
                               body=getRandomString(10), is_post=False)
        test_article.save()
        response = self.client.get("/komitee/" + title)
        self.assertTemplateUsed(response, "detail.html")

    def test_normal_behaviour_context(self):
        title = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title=title, description=getRandomString(5),
                               body=getRandomString(10), is_post=False)
        test_article.save()
        response = self.client.get("/komitee/" + title)
        self.assertEqual(response.context["article"], test_article)

    def test_normal_behaviour_context_author(self):
        title = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title=title, description=getRandomString(5),
                               body=getRandomString(10), is_post=False)
        test_article.save()
        response = self.client.get("/komitee/" + title)
        self.assertEqual(response.context["article"].author, superuser)

    def test_normal_behaviour_context_title(self):
        title = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title=title, description=getRandomString(5),
                               body=getRandomString(10), is_post=False)
        test_article.save()
        response = self.client.get("/komitee/" + title)
        self.assertEqual(response.context["article"].title, title)

    def test_normal_behaviour_context_description(self):
        title = getRandomString(5)
        description = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title=title, description=description,
                               body=getRandomString(10), is_post=False)
        test_article.save()
        response = self.client.get("/komitee/" + title)
        self.assertEqual(response.context["article"].description, description)

    def test_normal_behaviour_context_body(self):
        title = getRandomString(5)
        body = getRandomString(10)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title=title, description=getRandomString(5),
                               body=body, is_post=False)
        test_article.save()
        response = self.client.get("/komitee/" + title)
        self.assertEqual(response.context["article"].body, body)

    def test_normal_behaviour_context_is_post(self):
        title = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title=title, description=getRandomString(5),
                               body=getRandomString(10), is_post=False)
        test_article.save()
        response = self.client.get("/komitee/" + title)
        self.assertEqual(response.context["article"].is_post, False)

    def test_normal_behaviour_contains_title(self):
        title = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title=title, description=getRandomString(5),
                               body=getRandomString(10), is_post=False)
        test_article.save()
        response = self.client.get("/komitee/" + title)
        self.assertIn(str.encode(title), response.content)

    def test_normal_behaviour_contains_body(self):
        body = getRandomString(10)
        title = getRandomString(5)
        superuser = User(username=getRandomString(5), password=getRandomString(5), is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title=title, description=getRandomString(5),
                               body=body, is_post=False)
        test_article.save()
        response = self.client.get("/komitee/" + title)
        self.assertIn(str.encode(body), response.content)


# noinspection DuplicatedCode
class TestXssProtection(TestCase):
    def test_xss_protection(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="<script>alert(1)</script>", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.status_code, 200)

    def test_xss_protection_is_template_used(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="<script>alert(1)</script>", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertTemplateUsed(response, "detail.html")

    def test_xss_protection_context(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="<script>alert(1)</script>", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.context["article"], test_article)

    def test_xss_protection_context_author(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="<script>alert(1)</script>", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.context["article"].author, superuser)

    def test_xss_protection_context_title(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="test", body="<script>alert(1)</script>", is_post=False)
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.context["article"].title, "test")

    def test_xss_protection_context_description(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="testdescription",
                               body="<script>alert(1)</script>", is_post=False)  # noqa: E501
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.context["article"].description, "testdescription")

    def test_xss_protection_context_body(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="testdescription",
                               body="<script>alert(1)</script>", is_post=False)  # noqa: E501
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.context["article"].body, "<script>alert(1)</script>")

    def test_xss_protection_context_is_post(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="testdescription",
                               body="<script>alert(1)</script>", is_post=False)  # noqa: E501
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertEqual(response.context["article"].is_post, False)

    def test_xss_protection_contains_title(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="testdescription",
                               body="<script>alert(1)</script>", is_post=False)  # noqa: E501
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertIn(b"test", response.content)

    def test_xss_protection_contains_body(self):
        superuser = User(username="admin", password="admin", is_superuser=True)
        superuser.save()
        test_article = Article(author=superuser, title="test", description="testdescription",
                               body="<script>alert(1)</script>", is_post=False)  # noqa: E501
        test_article.save()
        response = self.client.get("/komitee/test")
        self.assertIn(b"&lt;script&gt;alert(1)&lt;/script&gt;", response.content)
