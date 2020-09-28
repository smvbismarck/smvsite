from django.shortcuts import render, HttpResponse
# Marked as error but actually it is not
from blog import models as blog_models
from komitee import models as komitee_models


def index(request):
    blogs = blog_models.Article.objects.all()
    komitees = komitee_models.Komitee.objects.all()
    return render(request, "index.html", {'articles': blogs, 'komitees': komitees})


def about(request):
    return HttpResponse("about page")


def dsgvo(request):
    return HttpResponse("dsgvo")


def impressum(request):
    return HttpResponse("impressum")
