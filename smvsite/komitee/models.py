from django.db import models


class Komitee(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
