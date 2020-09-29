from django.shortcuts import get_object_or_404, render
from blog import models as blog_models


def blogEntry(request, article_name):
    komitee_article = get_object_or_404(blog_models.Article, title=article_name, is_post=False)
    articles = blog_models.Article.objects.all()
    return render(request, "detail.html", {"article": komitee_article, "articles": articles})
