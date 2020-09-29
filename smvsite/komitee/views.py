from django.shortcuts import get_object_or_404, render
from .models import Komitee


def blogEntry(request, article_name):
    komitee_article = get_object_or_404(Komitee, title=article_name)
    komitee_list = Komitee.objects.all()
    return render(request, "detail.html", {"article": komitee_article, "komitees": komitee_list})
