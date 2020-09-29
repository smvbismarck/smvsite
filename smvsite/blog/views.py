from django.shortcuts import get_object_or_404, render
from .models import Article
from komitee import models as komitee_models


def blogEntry(request, article_id):
    komitee_list = komitee_models.Komitee.objects.all()
    blog_article = get_object_or_404(Article, id=article_id)
    return render(request, "detail.html", {"article": blog_article, "komitees": komitee_list})
