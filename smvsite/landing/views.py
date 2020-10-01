from django.shortcuts import render, HttpResponse
# Marked as error but actually it is not
from blog import models as blog_models
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from smvsite import settings

@cache_page(60)
def index(request):
    blogs = blog_models.Article.objects.all()
    return render(request, "index.html", {'articles': blogs})


@cache_page(300)
def about(request):
    return HttpResponse("about page")


@cache_page(300)
def dsgvo(request):
    return HttpResponse("dsgvo")


@cache_page(300)
def impressum(request):
    return HttpResponse("impressum")
