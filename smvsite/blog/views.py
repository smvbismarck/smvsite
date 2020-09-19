from django.http import HttpResponse


def blogEntry(request, article_name):
    return HttpResponse(article_name)
