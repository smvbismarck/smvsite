from django.shortcuts import get_object_or_404, render
from blog import models as blog_models
from mistune import markdown
from django.views.decorators.cache import cache_page


@cache_page(30)
def blogEntry(request, article_name):
    komitee_article = get_object_or_404(blog_models.Article, title=article_name, blogpost=False)
    komitee_article.body = markdown(komitee_article.body, bodyescape=True, hard_wrap=True)
    articles = blog_models.Article.objects.all()
    return render(request, "detail.html", {"article": komitee_article, "articles": articles})
