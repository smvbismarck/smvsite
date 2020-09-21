from django.http import HttpResponse
import html
from django.shortcuts import get_object_or_404
from .models import Komitee


def blogEntry(request, article_name):
    komitee_article = get_object_or_404(Komitee, title=article_name)
    return HttpResponse(html.escape(komitee_article.body))
