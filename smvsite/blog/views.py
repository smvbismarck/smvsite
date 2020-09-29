from django.shortcuts import get_object_or_404, render
from .models import Article
from mistune import markdown


def blogEntry(request, article_id):
    articles = Article.objects.all()
    blog_article = get_object_or_404(Article, id=article_id, is_post=True)
    blog_article.body = markdown(blog_article.body)
    return render(request, "detail.html", {"article": blog_article, "articles": articles})
