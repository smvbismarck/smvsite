from django.shortcuts import get_object_or_404, render
from .models import Article


def blogEntry(request, article_id):
    articles = Article.objects.all()
    blog_article = get_object_or_404(Article, id=article_id)
    return render(request, "detail.html", {"article": blog_article, "articles": articles})
