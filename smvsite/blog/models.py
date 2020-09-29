from django.db import models


class Article(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, )
    title = models.CharField(max_length=100, unique=True)
    time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    body = models.TextField()
    is_post = models.BooleanField(default=True)

    def __str__(self):
        return self.title
