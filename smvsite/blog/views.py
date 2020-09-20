from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Article


def blogEntry(request, article_name):
    blog_article = get_object_or_404(Article, title=article_name)
    return HttpResponse(blog_article.body)
