from django.shortcuts import render
# Marked as error but actually it is not
from blog import models


def index(request):
    blogs = models.Article.objects.all()
    return render(request, "index.html", {'articles': blogs})
