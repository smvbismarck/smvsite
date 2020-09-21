from django.http import HttpResponse
import html
from django.shortcuts import get_object_or_404
from .models import Article


def blogEntry(request, article_id):
    blog_article = get_object_or_404(Article, id=article_id)
    return HttpResponse(html.escape(blog_article.body))
